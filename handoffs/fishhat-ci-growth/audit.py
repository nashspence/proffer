"""Recompute retained research observations; never qualify fishhat or fetch data."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

SOURCE = "f96b83dc20f059d62a4363a63c37bb0ef8c642e5"
TREE = "32c329bd30e41405eaf49d3fc81577682cc00ccb"
RUN = 45156202495
ATTEMPT = 1
CONTROLLER = 137636936890
UNIT = 137635743188
HERE = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def instant(value):
    result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    require(result.tzinfo is not None, "timestamp lacks timezone")
    return result


def elapsed(row):
    seconds = (instant(row["completed_at"]) - instant(row["started_at"])).total_seconds()
    require(seconds >= 0, "negative duration")
    return seconds


def exactly_one(rows, predicate, label):
    selected = [row for row in rows if predicate(row)]
    require(len(selected) == 1, "missing or duplicate " + label)
    return selected[0]


def retained_inventory(directory):
    inventory = read(directory / "inventory.json")
    rows = inventory["files"]
    names = [row["path"] for row in rows]
    require(len(names) == len(set(names)), "duplicate retained filename")
    require(all(Path(name).name == name for name in names), "nonlocal retained filename")
    actual = {path.name for path in directory.iterdir() if path.is_file()}
    require(actual == {*names, "inventory.json"}, "retained inventory membership changed")
    for row in rows:
        data = (directory / row["path"]).read_bytes()
        require(len(data) == row["bytes"], "retained length mismatch: " + row["path"])
        require(sha256(data) == row["sha256"], "retained digest mismatch: " + row["path"])
    return len(rows)


def metadata(directory):
    run = read(directory / "accepted-main-run.json")
    require((run["id"], run["head_sha"], run["run_attempt"]) == (RUN, SOURCE, ATTEMPT),
            "unexpected workflow identity")
    require(run["status"] == "completed" and run["conclusion"] == "success",
            "unexpected workflow outcome")
    payload = read(directory / "accepted-main-jobs.json")
    jobs = payload["jobs"]
    require(len(jobs) == payload["total_count"] == 26, "incomplete retained job collection")
    require(len({job["id"] for job in jobs}) == len(jobs), "duplicate job")
    for job in jobs:
        require((job["run_id"], job["head_sha"], job["run_attempt"]) == (RUN, SOURCE, ATTEMPT),
                "job source/run/attempt mismatch")
        require(job["status"] == "completed", "incomplete job")
        elapsed(job)
    controller = exactly_one(jobs, lambda row: row["id"] == CONTROLLER, "controller")
    units = [row for row in jobs if row["name"].startswith("Unit shard (Python ")]
    require(len(units) == 6, "incomplete retained unit job collection")
    longest = max(units, key=elapsed)
    require(longest["id"] == UNIT, "longest unit identity changed")
    enrollment = exactly_one(
        controller["steps"],
        lambda row: "python -m scripts.native_linux_enrollment " in row["name"],
        "enrollment step",
    )
    upload = exactly_one(
        controller["steps"],
        lambda row: row["name"].startswith("Run actions/upload-artifact@"),
        "controller upload step",
    )
    require(enrollment["conclusion"] == upload["conclusion"] == "success",
            "controller step outcome changed")
    wait = (max(instant(job["completed_at"]) for job in jobs)
            - instant(run["run_started_at"])).total_seconds()
    occupied = sum(elapsed(job) for job in jobs)
    excerpt = (directory / "accepted-slow-unit-excerpt.log").read_bytes()
    meta = read(directory / "accepted-slow-unit-excerpt-metadata.json")
    require((meta["source_commit"], meta["run_id"], meta["run_attempt"], meta["job_id"])
            == (SOURCE, RUN, ATTEMPT, UNIT), "excerpt provenance mismatch")
    require(sha256(excerpt) == meta["excerpt_sha256"], "excerpt digest mismatch")
    matches = re.findall(r"(\d+) passed, (\d+) subtests passed in ([0-9.]+)s",
                         excerpt.decode("utf-8"))
    require(len(matches) == 1, "missing or ambiguous pytest summary")
    tests, subtests, seconds = matches[0]
    require((int(tests), int(subtests), float(seconds))
            == (meta["passed_tests"], meta["passed_subtests"], meta["pytest_seconds"]),
            "excerpt summary disagrees with metadata")
    return {
        "run_id": RUN,
        "run_attempt": ATTEMPT,
        "jobs": len(jobs),
        "job_outcomes": dict(sorted(Counter(job["conclusion"] for job in jobs).items())),
        "controller_seconds": elapsed(controller),
        "enrollment_step_seconds": elapsed(enrollment),
        "upload_step_seconds": elapsed(upload),
        "workflow_wait_seconds": wait,
        "occupied_job_seconds": occupied,
        "occupied_runner_minutes": occupied / 60,
        "longest_unit_job_seconds": elapsed(longest),
        "one_shard_pytest_seconds": float(seconds),
        "one_shard_tests": int(tests),
        "one_shard_subtests": int(subtests),
    }


def source_inventory(directory, checkout):
    inventory = read(directory / "source-inventory.json")
    require((inventory["commit"], inventory["tree"]) == (SOURCE, TREE),
            "unexpected source inventory identity")
    groups = inventory["groups"]
    require({row["group"] for row in groups} == {"schemas", "catalogues"} and len(groups) == 2,
            "source inventory groups changed")
    files = [item for group in groups for item in group["files"]]
    require(len({item["path"] for item in files}) == len(files), "duplicate contract path")
    for group in groups:
        require(len(group["files"]) == group["count"], "source inventory count mismatch")
        require(sum(row["bytes"] for row in group["files"]) == group["bytes"],
                "source inventory byte total mismatch")
    require(sum(group["bytes"] for group in groups) == inventory["total_bytes"],
            "source inventory grand total mismatch")
    if checkout is not None:
        checkout = checkout.resolve()

        def git(*args):
            return subprocess.check_output(
                ["git", "-C", str(checkout), *args], text=True, stderr=subprocess.PIPE
            ).strip()

        require(Path(git("rev-parse", "--show-toplevel")).resolve() == checkout,
                "--fishhat must name the repository root")
        require(git("rev-parse", "HEAD") == SOURCE, "checkout commit differs from research source")
        require(git("rev-parse", "HEAD^{tree}") == TREE, "checkout tree differs from research tree")
        require(not git("status", "--porcelain", "--untracked-files=normal"),
                "checkout is not unchanged")
        contract_dir = checkout / "packages/fishhat-contracts/src/fishhat_contracts/contracts"
        actual = {str(p.relative_to(checkout)) for p in contract_dir.glob("*.json")}
        require(actual == {row["path"] for row in files}, "contract-file membership differs")
        for row in files:
            path = checkout / row["path"]
            require(path.resolve().is_relative_to(checkout), "source path escaped checkout")
            data = path.read_bytes()
            require(len(data) == row["bytes"] and sha256(data) == row["sha256"],
                    "source byte mismatch: " + row["path"])
    return {
        "groups": [{key: value for key, value in group.items() if key != "files"}
                   for group in groups],
        "total_bytes": inventory["total_bytes"],
        "checkout_bytes_verified": checkout is not None,
    }


def callback_count(checkout):
    """Count named calls in the pinned function, without importing project code."""
    path = checkout / "scripts/native_linux_snapshots.py"
    module = ast.parse(path.read_text(encoding="utf-8"))
    function = next(node for node in module.body
                    if isinstance(node, ast.FunctionDef) and node.name == "copy_disk")
    nested = {node.name: node for node in function.body if isinstance(node, ast.FunctionDef)}

    def counts(body):
        result = Counter()

        class Calls(ast.NodeVisitor):
            def visit_FunctionDef(self, node):
                return  # Nested definitions are expanded separately below.

            def visit_Call(self, node):
                if isinstance(node.func, ast.Name):
                    result[node.func.id] += 1
                self.generic_visit(node)

        visitor = Calls()
        for statement in body:
            visitor.visit(statement)
        return result

    outer = counts(function.body)
    output = counts(nested["verify_output"].body)
    command = counts(nested["command"].body)
    observed = {key: outer[key] for key in ("verify", "command", "verify_output")}
    require(observed == {"verify": 2, "command": 4, "verify_output": 4},
            "copy callback syntax differs from inspected structure")
    require(output["verify"] == 1 and command["verify_output"] == 2,
            "nested callback syntax differs from inspected structure")
    total = outer["verify"] + (
        outer["verify_output"] + outer["command"] * command["verify_output"]
    ) * output["verify"]
    return {
        "normal_success_callbacks_per_copied_disk": total,
        "method": "Pinned-source AST call expansion, not dynamic execution or general flow analysis",
        "nested_two_scans_per_restore_callback": "Manually reviewed call graph; see HANDOFF.md",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence-dir", type=Path, default=HERE / "evidence")
    parser.add_argument("--fishhat", type=Path, help="unchanged checkout of the pinned fishhat commit")
    args = parser.parse_args()
    try:
        result = {
            "scope": "Offline research arithmetic and static source audit, not native qualification",
            "retained_files_verified": retained_inventory(args.evidence_dir),
            "actions": metadata(args.evidence_dir),
            "contracts": source_inventory(args.evidence_dir, args.fishhat),
        }
        if args.fishhat is not None:
            result["copy_callbacks"] = callback_count(args.fishhat.resolve())
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0
    except (OSError, ValueError, KeyError, TypeError, StopIteration, subprocess.CalledProcessError) as exc:
        print("Research audit failed: " + str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

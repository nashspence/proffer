# Research validation and limits

Validated on 2026-11-23 in Linux with Python 3.12.14, jsonschema 4.26.0 and referencing 0.37.0. Proffer's declared `jsonschema>=4.22,<5` dependency was already satisfied. The research worktree is based on Proffer commit `2ce5e15c3191fcdc2be70213c0170f57c852a883`; the existing protocol, validator, tests and workflow are unchanged.

## Executed checks

| Check | Result and scope |
| --- | --- |
| `python -m pip install -r requirements-dev.txt` | Passed; declared dependencies already installed |
| `python -m unittest discover -s tests -v` | Passed, all three existing Proffer tests, including valid fixtures and invalid-variant subtests |
| `python check.py .reference/proffer.json` | Passed; validates record structure and Proffer semantic constraints, not the truth of research claims or permission to integrate |
| `python handoffs/fishhat-ci-growth/audit.py` | Passed; retained-file identity, complete job collection, run/source/attempt joins, timing arithmetic, unit excerpt and source-inventory arithmetic |
| `python handoffs/fishhat-ci-growth/audit.py --fishhat /workspace/scratch/b0a12860d29d/fishhat` | Passed; also verifies the unchanged pinned fishhat checkout and bytes of all 81 contract/catalogue files, then performs the AST-only callback expansion |
| Four malformed copied-evidence controls | All rejected with exit code 1; see `AUDIT_CONTROLS.json` |
| `git diff --check` and handoff-relative link/artifact checks | Passed |

The complete audit output is in `AUDIT_RESULT.json`. The source-aware audit used fishhat commit `f96b83dc20f059d62a4363a63c37bb0ef8c642e5`, tree `32c329bd30e41405eaf49d3fc81577682cc00ccb`. It read static data and syntax; it imported and executed no fishhat code.

The four malformed-input controls used temporary copies of the retained evidence: changed bytes without changing the inventory, a missing job, a duplicate job, and one job from a foreign attempt. For the last three, the local byte inventory was recomputed so rejection exercised semantic collection/provenance checks rather than merely a hash mismatch. These are controls for this small research helper, not native product counterexamples or a general evidence-security qualification.

## Review

Separate read-only reviews covered source/evidence custody, CI topology and native lifetime boundaries, and official upstream tool behavior. The final handoff incorporates their corrections: exact required check names; the distinction between broad and module-restricted unit meters; cleanup's storage dependency; independent index validation; finite profile routing; and a coordinated pre-v1 format cut without current dual-format compatibility.

## Evidence boundary

The run/job files are retained projections retrieved through GitHub's API. The unit excerpt is an unchanged duration/summary block from the decoded GitHub job log; its metadata records the full decoded log digest, but the full log is not included. The source inventory records exact source-file lengths and SHA-256 values. The evidence inventory identifies retained bytes. None of those hashes independently authenticates a native qualification claim.

The 14 verification-callback expansion is checked from the pinned function's AST. The two nested sealed-set scans per restore callback and three copied disk roles were reviewed in the actual call graph. The resulting 84 scans are static partial-work accounting, not a dynamic trace, total pipeline work or measured physical I/O.

The original native JSON/ZIPs/traces, all 23 historical runs, nested-stage reconciliation, trace attribution and external frozen readers were **not** independently acquired or reauthenticated here. Their sizes/timings and retained synthesis identities remain explicitly attributed to the maintainer's issue comments. No causal performance improvement was measured.

No fishhat source, workload, required check, growth bound or qualification flag was changed. No fishhat test suite, CI rerun, native guest, product command or release operation was executed. Fishhat's existing implementation pause remains in force. Proffer's branch CI is a protocol test of the research delivery; it is not fishhat qualification. The final delivery identifies its exact remote commit and observed branch-check result separately, avoiding a self-referential publication record inside the commit.

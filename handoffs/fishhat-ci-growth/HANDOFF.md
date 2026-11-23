# Fishhat qualification growth: integration handoff

## Decision and first action

**Preserve the proof obligations and change how qualification owns, stores and consumes evidence before extending the serial native workload.** Start with a matched experiment that moves checkpoint trace scratch off the state image being qualified. Then separate original evidence by proof scope, measure repeated custody work, and partition only genuinely independent guest lifetimes. Unit instrumentation and cold imports need their own investigations.

This is a research handoff requested by nashspence, not an implementation or an acceptance receipt. It addresses [issue 84, comment 7102165515](https://github.com/nashspence/fishhat/issues/84#issuecomment-7102165515). The comment explicitly pauses product work, including the not-yet-started [local checkpoint inspection increment, issue 450](https://github.com/nashspence/fishhat/issues/450). This handoff does not lift that pause. The integration agent can evaluate the research now; implementation follows the maintainer's current direction. No additional numerical gate or approval condition is proposed.

**First step for the integration agent:** read this document and `.reference/proffer.json`; verify the current fishhat source and the latest issue discussion; obtain the retained independent acceptance readers and original-evidence locations; then define the evidence-sink experiment below against the complete existing workload. Do not start issue 450 as part of consuming this handoff. Keep future decisions and implementation tracking in the owning GitHub issues, as fishhat requires; these research files are not a patch to merge into fishhat.

| Identity | Pinned value |
| --- | --- |
| Research date | 2026-11-23 |
| Fishhat source | `f96b83dc20f059d62a4363a63c37bb0ef8c642e5` |
| Fishhat source tree | `32c329bd30e41405eaf49d3fc81577682cc00ccb` |
| Proffer protocol/base | `2ce5e15c3191fcdc2be70213c0170f57c852a883` |
| Accepted-main Actions run / attempt | `45156202495` / `1` |
| Controller job | `137636936890` |
| Independently inspected slow unit job | `137635743188`, Python 3.12, shard 1 |

The [Proffer contract](../../schema/proffer.schema.json) distinguishes a reference handoff from permission to integrate. The handoff manifest records an **unchanged** fishhat source. All additions on this branch are research, retained observations, and an offline arithmetic/source audit.

## What was independently checked

Three evidence classes remain separate throughout this document:

1. **Retrieved and recomputed here:** accepted-main run/job metadata, one unit log excerpt, the pinned source tree, contract-file byte inventory, workflow topology, and the normal-success restore callback expansion. The retained data and `audit.py` make the arithmetic and source inventory reviewable without running fishhat.
2. **Reported by the maintainer:** raw native report/trace sizes, the 23-run historical synthesis, trace fd/path attribution, exclusive nested native phases, 18 frozen-reader dispatch timings, failed-attempt totals and the accepted native qualification. We read these in the linked discussion; we did not independently acquire or authenticate the 1.68 GB aggregate, all original ZIPs, or the external frozen readers.
3. **Proposed/inferred:** causal explanations, scope layout, custody consolidation and lane cuts. They require matched experiments and independent acceptance before becoming qualified changes. No percentage saving or complete-product ETA is claimed.

### Independently reproduced baseline

| Observation | Value | Scope and interpretation |
| --- | ---: | --- |
| Controller job | 5,031 s / 83m51s | GitHub job `completed_at - started_at` |
| Enrollment step | 4,976 s / 82m56s | One named Actions step, contained within that job |
| Artifact-upload step | 32 s | Separate step in the same job |
| Main workflow wait | 6,066 s / 101m06s | Run start to last job completion; includes dependencies/queues |
| Summed job occupancy | 16,597 s / 276.6167 runner-minutes | All 26 returned jobs, including zero-duration skipped jobs; concurrent wall intervals are summed, not CPU or billed minutes |
| Longest unit job | 2,066 s / 34m26s | Python 3.12, shard 1 |
| Its pytest execution | 1,976.40 s | 3,625 tests + 172 subtests in this one shard; not the complete unit receipt |

Sources: [accepted main run](https://github.com/nashspence/fishhat/actions/runs/45156202495), [controller job](https://github.com/nashspence/fishhat/actions/runs/45156202495/job/137636936890), [unit job](https://github.com/nashspence/fishhat/actions/runs/45156202495/job/137635743188), and retained [job metadata](evidence/accepted-main-jobs.json), [run metadata](evidence/accepted-main-run.json), [unit excerpt](evidence/accepted-slow-unit-excerpt.log).

These measurements support prioritizing qualification structure. Upload took 32 seconds; reducing upload alone cannot explain away the 82m56s enrollment step. The unit job already supplies a substantial parallel-path floor. Timers inside these scopes overlap; do not add the controller, enrollment, checkpoint observer, capture lifetime and individual invocation clocks together.

The target comment reports 1,682,588,866 bytes of aggregate JSON and 1,220,331,199 bytes of checkpoint trace text across 68 invocations / 69 traced processes. Its preceding attribution reports 93.6% of trace text on installed runtime/package/schema reads. These figures are retained as **reported observations**, not newly reproduced findings. The reported 3,393,593,344-byte observer RSS is a process-lifetime high-water mark excluding children; it is neither simultaneous host/guest memory nor an OOM diagnosis. [Reported original accounting](https://github.com/nashspence/fishhat/issues/84#issuecomment-7101370355), [reported trace attribution](https://github.com/nashspence/fishhat/issues/84#issuecomment-7101638238).

Historical source/workload/runner differences prevent fitting a trustworthy timing curve to the milestone table. Thirty-seven prerequisite scopes are not thirty-seven equal features. The complete implementation routing in [issue 137](https://github.com/nashspence/fishhat/issues/137) cannot be estimated by multiplying a per-scope average.

## Source findings that sharpen the recommendation

### A. Trace scratch and retained reports enter later image custody

The guest creates `/var/lib/fishhat-checkpoint-fixture-<enrollment>/traces`, reads each original trace into a string, and retains it in the invocation result. Checkpoint qualification runs before stopped-source capture. The directory is removed after child settlement, but that removal alone does not demonstrate that its image allocation was discarded. The source confirms the coupling path; it does not establish the exact causal share of the historical image-size or timing increase.

There are two distinct costs to separate experimentally. Trace writes can affect later state-image work. Independently, `CaptureLifetime` deep-copies preceding nonempty reports and compares them during later protected observations, so the large checkpoint report participates in subsequent custody work.

**The guest already uses `json.dump`.** Replacing `json.dumps` with `json.dump` is not a sufficient remedy: all original trace strings are accumulated before emission, and the host receives, hashes, decodes and retains the whole document. A real layout change must alter retained representation and reader input extent, not merely the JSON writer call.

Source: [trace collection](https://github.com/nashspence/fishhat/blob/f96b83dc20f059d62a4363a63c37bb0ef8c642e5/scripts/native_checkpoint_fixture.py#L70-L124), [settlement and emission](https://github.com/nashspence/fishhat/blob/f96b83dc20f059d62a4363a63c37bb0ef8c642e5/scripts/native_checkpoint_fixture.py#L301-L322), [host receive/decode](https://github.com/nashspence/fishhat/blob/f96b83dc20f059d62a4363a63c37bb0ef8c642e5/scripts/native_linux_owner_checkpoint.py#L294-L326), [capture ordering](https://github.com/nashspence/fishhat/blob/f96b83dc20f059d62a4363a63c37bb0ef8c642e5/scripts/native_linux_enrollment.py#L947-L991), [report retention and comparisons](https://github.com/nashspence/fishhat/blob/f96b83dc20f059d62a4363a63c37bb0ef8c642e5/scripts/native_linux_successor.py#L62-L130).

### B. A successful restore preparation includes at least 84 sealed-set scans in copy callbacks

The source provides a useful, narrowly scoped work model:

| Expansion | Count on normal success path |
| --- | ---: |
| Direct `verify()` calls in `copy_disk` | 2 |
| Direct `verify_output()` calls | 4 |
| Four external commands, each enclosed by two `verify_output()` calls | 8 |
| Total supplied verification callbacks per copied disk | **14** |
| Sealed-set scans per `RestoreSource.verify()` | **2** |
| Disks copied in a complete restore preparation | **3** |
| Sealed-set scans from those copy callbacks alone | **14 × 2 × 3 = 84** |

`RestoreSource.verify()` calls `snapshots.verify()` directly and then calls `restore_observation → CaptureLifetime.observation → _protected`, which verifies the sealed set again. Each sealed-set verification hashes all three sealed image files. With sealed-file byte extent `S`, this portion processes `84 × S` hashing bytes on the successful path. This is a static partial-work model, not measured physical I/O, elapsed time or total job work. Page-cache behavior does not turn hashing bytes into a physical-disk measurement.

It excludes outer checks, original-source/base/tool/output hashes, qemu-img reads and subsequent lifetime verification. Snapshot creation supplies `guest.verify_tools` instead, so the restore expansion must not be generalized to every use of `copy_disk`. Most importantly, the count does not establish that any check is safe to remove.

Source: [copy callback structure](https://github.com/nashspence/fishhat/blob/f96b83dc20f059d62a4363a63c37bb0ef8c642e5/scripts/native_linux_snapshots.py#L246-L338), [sealed-set verifier](https://github.com/nashspence/fishhat/blob/f96b83dc20f059d62a4363a63c37bb0ef8c642e5/scripts/native_linux_snapshots.py#L217-L243), [restore verifier](https://github.com/nashspence/fishhat/blob/f96b83dc20f059d62a4363a63c37bb0ef8c642e5/scripts/native_linux_restore.py#L70-L92), [restore wiring](https://github.com/nashspence/fishhat/blob/f96b83dc20f059d62a4363a63c37bb0ef8c642e5/scripts/native_linux_restore.py#L223-L235), [second scan](https://github.com/nashspence/fishhat/blob/f96b83dc20f059d62a4363a63c37bb0ef8c642e5/scripts/native_linux_successor.py#L96-L145), [three disk roles and digest](https://github.com/nashspence/fishhat/blob/f96b83dc20f059d62a4363a63c37bb0ef8c642e5/scripts/native_linux_images.py#L25-L55).

### C. Import optimization must address closure consumers, not only the loader

A fresh static inventory confirms **73 schema files, 1,942,687 bytes, plus 8 catalogues, 99,591 bytes: 2,042,278 bytes total**. `validation.py` reads them at import and creates the resource registry. These are source-file bytes, not measured per-command physical I/O.

Changing that comprehension to a lazy mapping alone would miss other costs. `_schema_documents` and `_core_schema_digest` build an index through `SCHEMAS.values()`. Several modules read catalogues or schema-derived values at import. The digest cache intentionally checks complete mutable sources, including unused definitions and catalogue changes, before reuse. Lazy loading must preserve those semantics and remove unrelated enumeration where justified, not silently hide it behind a mapping.

The evaluation resources deliberately omit `$schema` while published schema bytes retain it, so `$ref` evolution keeps custom `uniqueItems` and `multipleOf` behavior. A generic registry rewrite could reintroduce the pairwise uniqueness regression. Retain complete closed-reference admission, document annotations, declared contract/catalogue dependencies, missing-resource and replacement detection, and custom-schema checks. Installed-resource retrieval must not become network or arbitrary-path loading.

Source: [eager construction and custom validator](https://github.com/nashspence/fishhat/blob/f96b83dc20f059d62a4363a63c37bb0ef8c642e5/packages/fishhat-contracts/src/fishhat_contracts/validation.py#L253-L299), [closure admission](https://github.com/nashspence/fishhat/blob/f96b83dc20f059d62a4363a63c37bb0ef8c642e5/packages/fishhat-contracts/src/fishhat_contracts/handoffs.py#L58-L177), [cache semantics](https://github.com/nashspence/fishhat/blob/f96b83dc20f059d62a4363a63c37bb0ef8c642e5/packages/fishhat-contracts/src/fishhat_contracts/handoffs.py#L284-L350), [mutation controls](https://github.com/nashspence/fishhat/blob/f96b83dc20f059d62a4363a63c37bb0ef8c642e5/tests/test_schema_identity_cache.py), [retained inventory](evidence/source-inventory.json).

### D. Units are already sharded; a single case remains indivisible

Current CI uses **two runner shards for each of Python 3.11, 3.12 and 3.13**, with four xdist workers per shard and duration-ordered selection. Its sharded execution uses `--dist=load --maxschedchunk=1 --max-worker-restart=0`. The older discussion's work-stealing advice is not the current sharded execution path. Stable `Contracts and unit tests (Python 3.11)`, `Contracts and unit tests (Python 3.12)` and `Contracts and unit tests (Python 3.13)` jobs aggregate complete receipts.

The inspected unit log contains individual call durations of 1,113.06 s for the replicated-proposal negative control, 922.16 s for adapter history attempts and 799.96 s for complete multi-owner work. These run under parallel workers and are not additive wall time. More shards cannot subdivide one test automatically.

`tests/linear_support.py` counts Python line execution, native container work/copies, serialization/parsing/encoding and SQLite progress. It enforces work-count growth, not elapsed thresholds. Profile instrumentation and implementation separately; replacing it with sampling or nominal operation counts would need equivalent regression sensitivity, not merely faster execution.

Source: [CI workflow](https://github.com/nashspence/fishhat/blob/f96b83dc20f059d62a4363a63c37bb0ef8c642e5/.github/workflows/ci.yml), [shard execution](https://github.com/nashspence/fishhat/blob/f96b83dc20f059d62a4363a63c37bb0ef8c642e5/scripts/unit_shards.py#L206-L223), [meter and oracle](https://github.com/nashspence/fishhat/blob/f96b83dc20f059d62a4363a63c37bb0ef8c642e5/tests/linear_support.py#L89-L189), [unit log excerpt](evidence/accepted-slow-unit-excerpt.log).

## Ordered experiments and acceptance criteria

This sequence is proposed implementation work after the existing maintainer pause permits it. Each change needs its owning issue decision, exact source identities and the full validation required by fishhat. Focused experiments supply attribution; they do not replace clean local, protected-PR, fresh-main or independent native acceptance.

### 1. Separate trace scratch from the captured state

Change **only the trace destination first**, retaining current rendering and complete report content. A separately enrolled ephemeral evidence volume is a concrete candidate. A host stream is an alternative, but adds backpressure/disconnection semantics; tmpfs trades disk pressure for memory pressure and should not be an automatic choice for this workload.

The existing input owner admits exactly base plus root/control/data disks. An observation volume needs an explicit separate owner, device/mount identity, permissions, lifecycle and profile treatment. Relocating to another directory on the same root, or reusing a protected control/data/authority/journal domain, does not establish separation. The producer/reader must change together because trace argv, paths, originals and cleanup are currently checked exactly. [Input inventory](https://github.com/nashspence/fishhat/blob/f96b83dc20f059d62a4363a63c37bb0ef8c642e5/scripts/native_linux_images.py#L89-L116), [exact trace joins](https://github.com/nashspence/fishhat/blob/f96b83dc20f059d62a4363a63c37bb0ef8c642e5/scripts/native_checkpoint_observation.py#L777-L905).

Use the complete 68-invocation/69-process workload with unchanged required outcomes. Match pinned tools, guest inputs/profile, selected cases and runner conditions; record exact baseline/candidate sources and every unavoidable difference in installed artifacts or observers. Keep independent disposable instances. Record run order and cold/warm conditions; retain all attempted outcomes, not just the fastest successful pair. Path/PID/timing bytes naturally differ between runs: equivalence means complete proof and workload preservation, not identical raw trace text.

Measure separately: bytes written per state/evidence device; qcow2 logical file length, host allocation and virtual capacity; trace/original/report/archive bytes; actual hash/copy bytes; elapsed/CPU/I/O with scope and availability; process-lifetime RSS; and success, refusal, interruption and cleanup results. The sought first result is evidence that observation scratch no longer enlarges the state being copied. A timing benefit remains advisory and may be unavailable if runs are not comparable.

Preserve existing exact installed-import, process/syscall, request/reply, marker and record-byte proofs. Add controls for substituted/aliased evidence devices, protected-domain overlap, symlink/hardlink/ownership/mode changes, late writers, mutation after sealing, lost final chunks, missing/duplicate traces, ENOSPC/EIO, interrupted collection, resource leaks and foreign-neighbor cleanup. If streaming is chosen, include backpressure and disconnection without inventing success or losing required originals.

Unlink and discard are different operations. QEMU exposes discard forwarding explicitly, and its image utility distinguishes virtual extent from allocation. Do not add live-image compaction as a shortcut; QEMU warns about modifications and inconsistent queries while an image has a writer. [QEMU block options](https://www.qemu.org/docs/master/system/invocation.html), [image utility](https://www.qemu.org/docs/master/tools/qemu-img.html), [fstrim semantics](https://man7.org/linux/man-pages/man8/fstrim.8.html).

### 2. Give each proof scope a complete original closure

Replace the giant inline evidence tree with original closures plus compact results and one authenticated current-run reconciliation. This is a design direction, not a new normative manifest specification in this branch. Existing executable declarations must continue owning the required scope set; do not introduce a parallel hand-maintained registry.

Each closure needs exact source/run/attempt, native profile/enrollment, installed artifact and observer/reader identities, required scope/dependency joins, and byte lengths/digests for every original. Readers validate original evidence and semantic joins for their own scope. A producer's `passed` field, a filtered projection or a matching digest without trusted provenance cannot establish independent qualification. The aggregate must reject missing, duplicate, stale, foreign or unvalidated scopes and incompatible cross-owner dependencies.

An independent validator must check the complete index and reconcile required scope membership against the existing authoritative declarations, independently of producer success assertions. Give each reader authenticated scope membership, provenance and required dependency bindings from that verification; a producer-filtered manifest cannot supply them. Do this global reconciliation once, without making every reader parse the entire global index or rewriting accumulated metadata at every append. The intended work is index processing plus the sum of genuinely required reader closures. Cross-owner promises still require the relevant multi-owner originals and end-to-end checks.

**Transport detail:** fishhat pins upload-artifact `ea165f8d65b6e75b540449e92b4886f43607fa02` and download-artifact `d3f86a106a0bac45b974a628896c90dbdf5c8093`. That upload version supplies whole immutable ZIPs; individual members are not independently downloadable. A compact index inside the old giant ZIP therefore leaves download amplification. Use separately identified scope/group artifacts. The downloader reports a digest mismatch as a warning, so add an explicit failing check. Bind artifact IDs/digests and original-member identities, not names alone. Hidden files are excluded by default and extracted modes are normalized: downloaded modes cannot prove original native custody. [Pinned upload behavior](https://github.com/actions/upload-artifact/blob/ea165f8d65b6e75b540449e92b4886f43607fa02/README.md), [pinned digest handling](https://github.com/actions/download-artifact/blob/d3f86a106a0bac45b974a628896c90dbdf5c8093/src/download-artifact.ts#L167-L196), [GitHub digest documentation](https://docs.github.com/en/actions/tutorials/store-and-share-data#validating-artifacts).

Preserve exact membership, byte completeness and path-safe extraction, including missing/duplicate members, path aliases, digest mismatch, truncated streams, wrong source/run/attempt/profile, forged summaries and foreign original substitution. Retain all original failure evidence. Grouping can control transport overhead without imposing a total scope/evidence cap.

The external frozen readers are a concrete dependency: their complete implementations were not available in the inspected fishhat tree. Obtain and inventory each reader's required fields/closure and independent controls before a format cut. Update current producer, readers and acceptance together. Fishhat's pre-v1 hard-cut policy excludes any current dual-format compatibility layer. If a dependent reader cannot change with the rest, report that blocker instead of retaining the obsolete current format. Historical originals remain immutable offline evidence; retaining them is distinct from accepting obsolete current formats. [Hard-cut and evidence rules](https://github.com/nashspence/fishhat/blob/f96b83dc20f059d62a4363a63c37bb0ef8c642e5/AGENTS.md).

### 3. Measure and narrow custody verification at proven boundaries

Instrument actual work at `native_linux_images.digest`, sealed-set verification, restore callbacks and `CaptureLifetime` comparisons. Attribute caller, purpose, transition, artifact role, invocation count, bytes read/hashed/compared, outcome and elapsed scope while the work happens. A logical hashing-byte counter is not physical I/O. Count originals, base, tools, sealed disks and output separately; avoid adding extra scans merely to measure scans.

Build a boundary table for admission, each external image operation, completed output, source advancement, restored boot, teardown and final preservation. For any consolidation, identify which mutation window it used to cover and demonstrate equivalent protection. A remembered digest, unchanged metadata, retained descriptor, or read-only mode alone is insufficient to establish immutable custody. No scan is removed solely on the 84-scan observation.

Keep the existing controlled failures: sealed-image byte mutation, handle/namespace rebinding, aliases, ownership/mode changes, modified earlier reports, forged source evidence, interruptions, abandoned/late writers and cleanup of only owned resources. [Snapshot controls](https://github.com/nashspence/fishhat/blob/f96b83dc20f059d62a4363a63c37bb0ef8c642e5/tests/test_native_linux_snapshots.py#L402-L468), [restore controls](https://github.com/nashspence/fishhat/blob/f96b83dc20f059d62a4363a63c37bb0ef8c642e5/tests/test_native_linux_restore.py#L280-L405), [successor controls](https://github.com/nashspence/fishhat/blob/f96b83dc20f059d62a4363a63c37bb0ef8c642e5/tests/test_native_linux_successor.py#L193-L244).

### 4. Partition by owned fixture lifetime and proof domain

After scope closures can be reconciled independently, evaluate these cuts. They are candidates requiring proof-equivalence review, not an approved job matrix or permission to select only convenient scopes.

| Candidate lane | Keep together | Preconditions and boundary |
| --- | --- | --- |
| Protected installed execution | Installation input, runtime/wheel, bootstrap, launcher and entrypoint chain | Own enrolled guest and exact current installed candidate; preserve their dependent custody checks |
| Protected checkpoint storage | All existing checkpoint invocations, held-process/failure cases and cleanup | Own guest, qualified storage and candidate input construction; no dependence on another lane's writable guest |
| State-image lifecycle | Storage/resource/reboot, cold capture, private restore, restored boot and original-disk restart | Preserve serial before/after identity, canary and original-source joins |
| Restored successor | Existing separate successor path, later-source advancement, older restored comparison and interruption | Retain the complete capture/advance/restore promise in its owning lifetime |

Initial extraction should evaluate checkpoint storage as one complete lane; its input preparation and storage prerequisites are explicit. Splitting individual failure positions first risks repeating setup while severing lifecycle promises. Share only independently verified immutable inputs. Keep writable authority, live guests, process groups and cleanup ownership exclusive to each lane. Reboot/restore/handoff promises stay sequential wherever their correctness spans that lifetime. [Enrollment orchestration](https://github.com/nashspence/fishhat/blob/f96b83dc20f059d62a4363a63c37bb0ef8c642e5/scripts/native_linux_enrollment.py), [checkpoint prerequisites](https://github.com/nashspence/fishhat/blob/f96b83dc20f059d62a4363a63c37bb0ef8c642e5/scripts/native_linux_owner_checkpoint.py), [successor lifetime](https://github.com/nashspence/fishhat/blob/f96b83dc20f059d62a4363a63c37bb0ef8c642e5/scripts/native_linux_successor.py).

Cleanup also needs explicit ownership: `verify_guest_cleanup()` currently expects storage evidence. An installed-only guest must gain complete cleanup checks for its real resources; passing an invented empty storage report would weaken the proof. See [current cleanup assumptions](https://github.com/nashspence/fishhat/blob/f96b83dc20f059d62a4363a63c37bb0ef8c642e5/scripts/native_linux_enrollment.py#L1040-L1089).

Preserve existing required status names, PR trust boundary and all currently required prerequisite scopes on main (37 at the pinned baseline; this count is not a cap). The final required result must actually reconcile complete current-run receipts; a skipped prerequisite, missing lane or failed cleanup is not success. Review workflow/check accounting and release policy with any topology change. Do not move required proofs to an optional nightly lane or substitute old-source receipts. [CI policy](https://github.com/nashspence/fishhat/blob/f96b83dc20f059d62a4363a63c37bb0ef8c642e5/tests/test_ci_config.py), [release policy](https://github.com/nashspence/fishhat/blob/f96b83dc20f059d62a4363a63c37bb0ef8c642e5/release.toml).

Measure both the critical path and summed occupied runner time, including new guest startups, duplicate prerequisite work and reconciliation. Parallelism can reduce wait while increasing total work. The appropriate lane size follows the longest necessary lane, including units; no arbitrary short-duration target is imposed. The documented six-hour hosted-job ceiling and public Ubuntu 4-CPU/16-GB resources are capacity boundaries, not desired feedback time. [Actions limits](https://docs.github.com/en/actions/reference/limits), [runner specifications](https://docs.github.com/en/actions/reference/runners/github-hosted-runners#standard-github-hosted-runners-for-public-repositories).

Follow the finite claimed-profile/adapter routing in issue 137 and [issue 138's facility assignment](https://github.com/nashspence/fishhat/issues/138#issuecomment-6727182512): Linux owned guests and separately owned method companions, macOS native accounts/prefixes/launchd domains, an isolated OpenWrt guest, and portable install/client lanes. Windows is a portable-client target in that routing, not a selected native-owner profile; unavailable GPU/device facilities remain blockers for their consumers. Qualify each promised composition and cross-owner end-to-end obligation. Avoid an unconditional Cartesian product of unrelated implementations, scales and fault positions; this does not authorize deleting any existing case or leaving a claimed composition unqualified.

### 5. Profile unit metering and cold imports separately

For units, retain the complete extents, comparisons across scales, retries/interleaved writers, cold reconstruction and injected superlinear regressions. Measure meter overhead and implementation work on equivalent workloads. Any replacement must still detect repeated-prefix serialization, pairwise uniqueness, whole-state copies, replicated manifests and owner-proof fanout. Preserve line-accounting coverage and restoration after exceptions; the current meter observes third-party Python calls too. Focused profiles cannot replace complete current-source receipts. [Independent meter control](https://github.com/nashspence/fishhat/blob/f96b83dc20f059d62a4363a63c37bb0ef8c642e5/tests/test_work_measurement.py), [growth controls](https://github.com/nashspence/fishhat/blob/f96b83dc20f059d62a4363a63c37bb0ef8c642e5/tests/test_linear_growth.py#L314-L355), [complete workflow growth](https://github.com/nashspence/fishhat/blob/f96b83dc20f059d62a4363a63c37bb0ef8c642e5/tests/test_workflow_journal_growth.py).

Distinguish the two meters: `tests/linear_support.py` counts broad Python execution outside the helper; `workflow_journal_support.WorkMeter.account` already restricts line tracing to selected modules while counting complete validation inputs and actual validation calls. A blanket proposal to restrict all tracing would miss this existing difference. An instrument-off diagnostic can help attribute overhead only as a separately labeled nonqualifying comparison; it cannot replace the counted run. [Workflow meter](https://github.com/nashspence/fishhat/blob/f96b83dc20f059d62a4363a63c37bb0ef8c642e5/tests/workflow_journal_support.py#L188-L290).

For cold imports, separate file reads/JSON decode/registry construction from the schema-identity consumers described above. Test genuinely fresh installed processes and warm-process reuse as different workloads; retaining one warm interpreter cannot replace process-isolation witnesses. A closed installed-URI retrieval mechanism is possible in the referencing API, but must preserve fixed dialect, custom validator evolution, full admitted document/catalogue dependencies and typed mutation detection. Unknown references must fail locally. Do not claim latency benefits from traced TCG timings. [Official referencing API](https://python-jsonschema.readthedocs.io/en/stable/referencing/).

Treat trace-rendering optimization as another isolated experiment. Globally lowering `-s`, using raw read rendering, or filtering fixed descriptor numbers can remove required bytes or calls. Preserve exact record/marker/request/reply reconstruction and process/fd lifetime joins; include close/reuse, dup/fork, short/split I/O, aliases and unfinished/resumed calls. Required truncated evidence must fail. Keep the observation-sink experiment separate so its effect remains attributable. [Upstream strace manual](https://github.com/strace/strace/blob/master/doc/strace.1.in).

## Growth model and measurement discipline

The current amplifiers are products of distinct extents, not proof that the entire pipeline has a measured quadratic regression:

| Subsystem | Work model to instrument | What the redesign should demonstrate |
| --- | --- | --- |
| Fresh installed commands | Process count × actually loaded contract/runtime closure | Unrelated contract growth does not force every command to decode the whole collection, while required closure validation remains complete |
| Image custody | Verification count × verified byte extent | Each required boundary has explicit work; narrower/reused verification is justified by custody, not hidden behind a cache |
| Evidence consumption | Sum over readers of their required closure bytes | Unrelated evidence is not decoded by every reader; complete index reconciliation and cross-scope joins remain explicit |
| Native lanes | Necessary sequential work + fixture/reconciliation overhead | Wait improves, total occupied work and evidence do not disappear from accounting |

Vary each axis independently and then together: fixed process/readers with growing bytes; fixed bytes with growing process/readers; and combined growth. Use complete increasing extents and actual counted work. The intended scope-index model is index work plus required closure work; it is not guaranteed linear if genuine dependency closures themselves grow densely. If the existing declared bound cannot be met, report the measured gap through fishhat's existing maintainer-exception rule. Do not invent a new performance threshold or reinterpret a growth failure as an advisory timing miss.

Use exclusive direct-child phase accounting only when nesting and non-overlap are established. Record lifetime clocks separately. Keep CPU, elapsed, I/O, physical allocation, logical lengths and process RSS scopes explicit. Report failures and unavailable metrics honestly. No evidence here establishes normal product speed, native recovery completion, competitor performance or a full-product ETA.

## Reproduce and consume this handoff

From the Proffer branch root:

```sh
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -v
python check.py .reference/proffer.json
python handoffs/fishhat-ci-growth/audit.py
python handoffs/fishhat-ci-growth/audit.py --fishhat /path/to/pinned/fishhat
```

The audit uses Python's standard library, reads retained evidence, and optionally verifies source identity/bytes and counts callback syntax in an unchanged pinned checkout. It does not import fishhat, start guests, run product commands, fetch the network, or establish native acceptance. The two nested sealed-set verifications are a manually reviewed call-graph result; the AST audit reproduces the 14-callback portion only. Recomputed timings are arithmetic over retained GitHub metadata, not a new CI run.

The evidence directory retains the selected maintainer comments, projected run/job records, one unit log excerpt with retrieval metadata, the 81-file source inventory, and the callback count. `evidence/inventory.json` identifies the exact retained bytes. Those hashes provide reproducibility; they do not authenticate a native qualification claim. See [VALIDATION.md](VALIDATION.md) for actual local verification and limits.

On consumption, record a Proffer disposition in the owning issue when the integration agent is authorized to publish it. Separate reused findings, adapted experiments, independently reproduced evidence and deferred work. No disposition or publication record is embedded in this commit, and this research branch is not a request to merge the Proffer protocol or research documents into fishhat.

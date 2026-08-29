# Scripts

Written 2026-08-29. Until then there was **no marker anywhere** saying which of
these run automatically and which are operator-invoked — a 2026-06 self-audit
asked for one and it was never added. The gap matters in both directions: a
reader can assume a script is guarding something when nothing calls it, or
assume it is inert when its output is committed content.

| Script | Runs automatically? | Output |
|---|---|---|
| [`measure-link-reachability.py`](measure-link-reachability.py) | **Yes** — `check-internal-links` job, every PR touching the paths in `link-checker.yml` | stdout only; the job gates on the `dangling` count. Its own job since 2026-08-29 — it used to sit behind a 7–15 min external scan inside `check-links` |
| [`test-measure-link-reachability.py`](test-measure-link-reachability.py) | **Yes** — `test-instruments` job | 11 checks, ~2m20s |
| [`test-close-superseded-workflow.js`](test-close-superseded-workflow.js) | **Yes** — `test-instruments` job | 43 checks, instant |
| [`check-measurement-expiry.py`](check-measurement-expiry.py) | **Yes** — `test-instruments` job, since 2026-08-29 (manual-only before that) | exits 1 on expired claims, 0 otherwise; expiring-soon is printed, not failed. `--create-issue` writes a gitignored file nothing reads |
| [`graphify_footer_inject.py`](graphify_footer_inject.py) | **No** — operator-run generator | **Committed content.** Emits the `<!-- graphify-footer:start -->` blocks in **20 of 26** `analysis/` docs |
| [`graphify_contradiction_lint.py`](graphify_contradiction_lint.py) | **No** — advisory, operator-run | stdout only; no committed output anywhere |
| [`list-declared-gaps.py`](list-declared-gaps.py) | **No** — weekly review step 5d, operator-run | stdout or `--json`; enumerates the `**Needs**:` gap declarations in `analysis/` |
| [`../automation/generate_index.py`](../automation/generate_index.py) | **Yes** — `.claude/hooks/post-tool-use.sh` on structure change | Rewrites `INDEX.md` |

## The two that look alike and are not

The 2026-06 self-audit grouped `graphify_footer_inject.py` and
`graphify_contradiction_lint.py` together and proposed marking both *"reference
pattern, not run in CI"*. **That would have been wrong for the first one.**

`graphify_footer_inject.py` is not a reference pattern. Its output is live,
committed corpus content, and it was bug-fixed at source on 2026-08-28
(`6b62c7e`) precisely because the links it emitted were not resolving — it had
rendered repo-root-relative targets into files under `analysis/`, so
`analysis/foo.md` inside an `analysis/` doc resolved to `analysis/analysis/foo.md`.
That single defect accounted for 54 of the corpus's root-relative links. Telling
a reader to ignore it would point them away from a script that actively produces
a fifth of the pointer graph.

`graphify_contradiction_lint.py` is the one that fits the description: nothing
calls it, nothing commits its output, and it is advisory by design.

Both require `graphify-out/graph.json`, which is **not** in the repo — running
`graphify` is an egress decision (see
[`analysis/memory-systems-archetype-recommendations.md`](../analysis/memory-systems-archetype-recommendations.md)
§ Archetype C-EC). Without that file the lint now skips cleanly; it used to
print *"Skipping (no-op)"* and then scan anyway against an empty ground truth,
emitting 32 confident findings built from nothing.

## Before you assume a script guards something

Check whether a workflow actually **runs** it, not whether a workflow
**mentions** it. Several of these appear in `link-checker.yml` only inside the
`paths:` trigger list — meaning a change to them starts CI, not that CI executes
them:

```bash
grep -rn "<script-name>" .github/workflows/*.yml    # mentions
grep -rn "python3 scripts/\|node scripts/" .github/workflows/*.yml    # invocations
```

That distinction is the whole reason this file exists.

# GitHub Workflows

> **Rewritten 2026-08-28.** The previous version documented `source-monitoring.yml`
> and its four jobs (`check-anthropic-releases`, `check-awesome-lists`,
> `check-anthropic-blog`, `check-practitioner-sources`) in detail. **That workflow
> does not exist** — it was deleted in the 2026-07 Reduction (Phase 6) because its
> issues sat unread. It also stated *"Secrets Required: None"* while
> `claude-code.yml` uses `ANTHROPIC_API_KEY`; the 2026-06 self-audit flagged both
> and neither was fixed. Roughly 40% of this file described machinery that had
> been gone for six weeks.
>
> This is the failure [`analysis/prose-corpus-discoverability.md`](../../analysis/prose-corpus-discoverability.md)
> measures: the prose stayed well-formed and confident after its subject was
> deleted, and nothing checks for that — which is why this file is now short
> enough to keep true.

## What actually exists

| File | Trigger | What it does |
|---|---|---|
| [`claude-code.yml`](claude-code.yml) | PR / issue comment | Claude Code review and `@claude` responses |
| [`link-checker.yml`](link-checker.yml) | daily cron, PR touching `**.md`, manual | Internal + external link validation, markdown lint, Tier-A source reachability |
| [`close-superseded-auto-issues.yml`](close-superseded-auto-issues.yml) | manual only | One-shot backlog drain for auto-filed, untriaged issues |

Nothing else. If you are looking for source monitoring, it was deliberately
retired — see DECISIONS.md Decision 11 and the Reduction Phase 6 notes.

## link-checker.yml

Five jobs (`check-internal-links`, `check-links`, `markdown-lint`,
`test-instruments`, `check-source-accessibility`). Said "Four" until 2026-08-29 —
the internal check became its own job in the 2026-08-29 split and this line was
not updated with it. The important structure is that **internal** and **external**
link failures are treated differently, because only one of them is this
repository's to fix.

> **None of these actually block a merge.** `master` is **unprotected**
> (`protected: false`, checked against the API 2026-08-29), so GitHub has no
> required-status-check list to enforce. A failing job turns the check red and
> nothing else — #999 was merged while `test-instruments` was still *running*.
> The "yes" column below means **the job fails**, not that the merge is stopped.
>
> To make it true: **Settings → Branches → Add branch protection rule** for
> `master` → *Require status checks to pass before merging* → select
> `test-instruments` and **`check-internal-links`** — not `check-links`. The
> deterministic internal gate has been its own job since the 2026-08-29 split;
> `check-links` is now the ~7-minute external scan whose failing step carries
> `continue-on-error: true`, so on a PR it cannot go red, and requiring it buys
> merge latency and no gating. Both jobs sit behind this workflow's
> `pull_request: paths:` filter, and a required check that never reports holds a
> PR at *Expected* forever — widen that filter before turning protection on.
> Until then, read the table as reporting,
> not gating. This correction exists because the repo asserted the stronger claim
> for a day — the exact defect it documents, committed by the person documenting it.

| Job | Fails on error? | Notes |
|---|---|---|
| `check-internal-links` | **yes** | `scripts/measure-link-reachability.py --links`. A new dangling internal link fails the job. Deterministic and ours to fix. Its own job since 2026-08-29; reports in seconds. |
| `check-links` (external) | no | `markdown-link-check`. Mostly upstream rot; triaged by exception. `continue-on-error: true`, so it cannot fail a PR. |
| `markdown-lint` | no (comments) | `npm run lint` |
| `test-instruments` | **yes** | Both instrument test suites — see below |
| `check-source-accessibility` | no | Probes a small set of critical Tier-A source URLs |

On the scheduled run it maintains **one standing issue**, updated in place and
closed automatically when the corpus is clean. It previously filed a fresh issue
every day, which produced ~900 open, zero-comment issues while 214 links stayed
broken — a check firing into a void. Do not revert that.

Config: [`../link-check-config.json`](../link-check-config.json) — ignore
patterns, retry/timeout, and the status codes treated as alive.

## Secrets and permissions

**Secrets required**: `ANTHROPIC_API_KEY` — used by `claude-code.yml` only.
`GITHUB_TOKEN` is provided automatically by Actions.

**Permissions**, per workflow rather than blanket:

- `claude-code.yml` — **`contents: write`**, `pull-requests: write`, `issues: write`, **`id-token: write`**, set at workflow level. This bullet claimed `contents: read` and omitted `id-token` entirely until 2026-08-29; the workflow has carried `contents: write` since it was added, so the line was **never true** — and a reviewer checking permissions here before approving the `@claude` trigger fix would have judged that fix far lower-risk than it was. `claude-review` inherits the workflow block deliberately: `contents: write` is what lets `@claude` on a PR actually change files. `daily-review-check` narrows to `contents: read` + `issues: write`, since posting a comment is its only output. **`process-source-update` was deleted 2026-08-29** — it was the externally-reachable write-scoped job the 2026-06 self-audit logged as Finding #1, and its only feeder (`source-monitoring.yml`) had been removed in `d9e484d`, so nothing had filed its trigger issues since. **Residual**: `claude-review` passes no `claude_args` — no `--allowedTools`, no `--max-turns` — so the `author_association` gate is the only control on that path.
- `link-checker.yml` — **no workflow-level block.** `contents: read` + `issues: write` are declared per job, on `check-links` (standing issue) and `check-source-accessibility` only. `check-internal-links`, `markdown-lint` and `test-instruments` declare nothing and run with the repository's default token permissions.
- `close-superseded-auto-issues.yml` — `issues: write`

## Running a workflow manually

**Use the Actions tab** → select the workflow → **Run workflow**. That is the
path that actually works for everyone.

```bash
# Requires the gh CLI, authenticated, with actions:write on this repo.
gh workflow run link-checker.yml
gh workflow run close-superseded-auto-issues.yml -f apply=false -f limit=500   # dry run first
```

`close-superseded-auto-issues.yml` is **dry-run by default** and never touches an
issue that carries a human comment. Run it once with `apply=false`, read the
list, then re-run with `apply=true`.

### Draining the backlog, in batches

Measured on the first dry run (2026-08-29): **935 open issues, 878 matching, 2
skipped for carrying a human comment, 55 untouched.**

**Correction (2026-08-29, later the same day):** those 55 were called *"human
issues"* here and in PLAN.md, and they are not human. All 55 are
`github-actions[bot]` output from two generator families the pattern list did not
carry — 49 `🤝 Community engagement triage` (bodies ending *"Automatically created
by source-monitoring workflow"*) and 6 `⚠️ Expired Measurement Claims Detected`
(*"Generated by: scripts/check-measurement-expiry.py"*). Verified by fetching them.
The mislabel is why the drain's completion notice was believed: with the residue
filed under "human", matching zero of them looked like success. Both families are
now in `PATTERNS`, both feeders were already deleted (`d9e484d`, `4875ed5`) so
nothing refills them, and the completion notice now reconciles unmatched issues
against the repo instead of only against what it matched.

**Second correction (2026-08-31) — the reconciliation was still not enough.** The
apply run closed 55 and reported *"every open issue was accounted for — the backlog
is drained."* It was not. That run **scanned 56 of 61** open issues; a re-run
scanned **1 of 6**, and both missed the *same five* (#689, #683, #646, #561, #554 —
all matching a pattern, all comment-free, all untouched since May 2026). The
2026-08-29 reconciliation compares *matched* against *scanned*, so when the listing
under-returns, `unmatched` is 0, every internal count agrees, and the all-clear is
vacuous — the same pathology one level below where it was just fixed.

The completion notice now cross-checks against a **different endpoint**:
`repos.get().open_issues_count` minus the open PR count is how many open issues the
repository itself reports. If the listing returned fewer, the run says so, names the
shortfall, and **never** claims the backlog is drained; if that endpoint is
unavailable, it says completeness could not be verified rather than implying it was.
Proven failure-capable: neutralise the check and 3 of 58 tests fail, with the notice
reverting to the exact false all-clear seen in production.

**The cause of the listing shortfall is not established.** The check deliberately
does not depend on knowing it — it only has to refuse to declare a victory it cannot
verify. The five issues above are still open.

**Set the `Mode` dropdown to `APPLY - actually close the matched issues`.** It
defaults to dry-run, and dry-run closes nothing.

> **Five consecutive runs came out as dry runs.** First as a text box pre-filled
> with `false` (easy to scroll past), then as a dropdown — and still dry. The
> matcher was verified byte-for-byte against the option string, so the remaining
> question was whether the value ever reached the script, and **the logs could not
> answer it.** The run now prints what it received from both input paths and the
> mode it resolved:
>
> ```
> input apply -> inputs context: "APPLY - actually close the matched issues"; event payload: null
> resolved mode: APPLY (will close issues)
> ```
>
> If a run is unexpectedly a dry run, read those two lines first. `null` from both
> sources means the value never arrived; a populated value with `resolved mode:
> DRY RUN` would be a matcher bug. An input you cannot observe is an input you
> cannot debug.

Closing one issue costs two API calls, and the comment is a *content-generating*
request — GitHub caps those near **80/minute and 500/hour**. So the job is built
to run **repeatedly**, not once:

| Input | Default | Why |
|---|---|---|
| `limit` | `250` | Fits inside one hour's content budget. ~4 passes to drain 878. |
| `delay_ms` | `1000` | 60 requests/min, under the 80/min ceiling. |
| `comment` | `true` | Set `false` to close silently — halves the calls, drains in **one** pass, but leaves no explanation behind. Prefer `true`. |

It is **idempotent**: each run re-scans and only sees issues that are still open,
so repeat until a dry run reports `0 match`. A rate-limit error **stops the run
cleanly** and reports how many closed, rather than throwing — progress is never
lost.

> The first version of this loop had none of that: it fired all ~1,756 calls
> back-to-back with `retries: 0`. At 878 matches it bursts the per-minute
> ceiling in seconds, 403s, and fails the job mid-drain. `scripts/test-close-superseded-workflow.js`
> now extracts the inline script straight from this YAML and runs it against a
> simulated 935-issue repo — the suite prints its own total (44 at time of
> writing), including the four checks that actually matter
> (never close a human issue, the standing issue, a commented issue, or a PR).
> It was verified to **fail against the pre-fix version** with the same
> unhandled 403 that would have hit production.

```bash
node scripts/test-close-superseded-workflow.js
```

> **A Claude Code session cannot dispatch these workflows.** Verified 2026-08-28
> against both the file name and the numeric workflow ID: `POST
> /actions/workflows/{id}/dispatches` returns **403 "Resource not accessible by
> integration"**. Claude Code on the web has no `gh` CLI and reaches GitHub only
> through the GitHub MCP server, whose app grant does not include
> `actions: write`. So `workflow_dispatch` is a **human-only trigger here**, and
> any plan that ends in "then Claude runs the workflow" does not complete.
>
> This is worth writing down rather than rediscovering: an agent can *author* a
> maintenance workflow and *not be able to fire it*, which is a quiet way for a
> shipped mechanism to sit unused. If a job must be agent-triggerable, give it a
> `schedule:` or a `repository_dispatch:` trigger, or have the agent do the work
> directly through the API tools it does hold.

## Keeping this file true

This README documents machinery that changes. It went stale once, comprehensively,
and nothing caught it. Two habits keep it honest:

1. When you add, delete, or rename a workflow, edit this file **in the same
   commit** — the checklist discipline in [`CONTRIBUTING.md`](../../CONTRIBUTING.md).
2. `ls .github/workflows/*.yml` against the table above. If they disagree, the
   table is wrong.
3. `node scripts/test-close-superseded-workflow.js` after touching the
   backlog-drain script. A workflow that closes hundreds of issues is not
   something to debug in production.

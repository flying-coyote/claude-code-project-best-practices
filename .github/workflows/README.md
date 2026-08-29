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

Four jobs. The important structure is that **internal** and **external** link
failures are treated differently, because only one of them is this repository's
to fix.

| Job | Blocks a PR? | Notes |
|---|---|---|
| `check-links` → internal | **yes** | `scripts/measure-link-reachability.py --links`. A new dangling internal link fails the PR. Deterministic and ours to fix. |
| `check-links` → external | no | `markdown-link-check`. Mostly upstream rot; triaged by exception. |
| `markdown-lint` | no (comments) | `npm run lint` |
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

- `claude-code.yml` — `contents: read`, `pull-requests: write`, `issues: write`
- `link-checker.yml` — `contents: read`, `issues: write` (standing issue)
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
skipped for carrying a human comment, 55 human issues untouched.**

**Set the `Mode` dropdown to `APPLY - actually close the matched issues`.** It
defaults to dry-run, and dry-run closes nothing. This began life as a text box
pre-filled with `false`, which produced three consecutive accidental dry runs
before anyone noticed the field — hence the dropdown, and hence the dry-run
notice now saying in as many words that nothing was closed.

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
> simulated 935-issue repo — 16 checks, including the four that actually matter
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

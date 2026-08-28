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

```bash
gh workflow run link-checker.yml
gh workflow run close-superseded-auto-issues.yml -f apply=false -f limit=500   # dry run first
```

Or via the Actions tab → select the workflow → **Run workflow**.

`close-superseded-auto-issues.yml` is **dry-run by default** and never touches an
issue that carries a human comment. Run it once with `apply=false`, read the
list, then re-run with `apply=true`.

## Keeping this file true

This README documents machinery that changes. It went stale once, comprehensively,
and nothing caught it. Two habits keep it honest:

1. When you add, delete, or rename a workflow, edit this file **in the same
   commit** — the checklist discipline in [`CONTRIBUTING.md`](../../CONTRIBUTING.md).
2. `ls .github/workflows/*.yml` against the table above. If they disagree, the
   table is wrong.

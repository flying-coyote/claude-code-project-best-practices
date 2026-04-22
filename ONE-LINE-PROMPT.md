# One-Prompt Project Review

Copy-paste this prompt into Claude Code in **any project** to get an evidence-based audit of your harness, commit patterns, CLAUDE.md, and model-migration exposure — with every recommendation tied to a specific analysis doc and evidence tier.

## The Prompt

```
Audit this project against Claude Code best practices.

STEP 1 — COLLECT SIGNALS (do these in parallel where possible):
- Read CLAUDE.md (check ./CLAUDE.md and .claude/CLAUDE.md; note line count and whether it references other files).
- Run: git log --oneline --since="90 days ago" | head -50
- Run: git log --since="90 days ago" --name-only --format="" | sort | uniq -c | sort -rn | head -20
- Inspect harness: ls -la .claude/ .claude/rules/ .claude/hooks/ .claude/skills/ .claude/agents/ .claude/commands/ .claude/settings.json 2>/dev/null
- Check model version in use: grep -r "opus\|sonnet\|haiku\|claude-" .claude/settings.json 2>/dev/null; also note model from any recent CI config, agent frontmatter, or MCP settings.
- Run session diagnostics: npx -y claude-doctor 2>/dev/null || echo "claude-doctor not available"
- Note the project type (docs, data pipeline, library, multi-repo, research, etc.) from README/structure.

STEP 2 — FETCH ROUTING MAP:
Fetch https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/AUDIT-CONTEXT.md

STEP 3 — ROUTE TO APPLICABLE ADVISORIES:
For each Signal row in AUDIT-CONTEXT.md that matches what you observed in Step 1, fetch the listed analysis doc(s) from https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/{path}. Also fetch the "Always Fetch" docs. Do not fetch docs whose signal you did not observe. Typical audit touches 4–8 analysis docs.

STEP 4 — PRODUCE AUDIT:
Use the STRUCTURED OUTPUT FORMAT below. Every recommendation must cite the analysis doc it came from and that doc's evidence tier (visible in the doc's header). If claude-doctor produced signals, act on edit-thrashing and error-loop counts; treat the composite health percentage as directional only.

Weight recommendations by source authority: Tier A (Anthropic/primary observation) > Tier B (expert practitioner) > Tier C (community). Prefer positive examples over MUST NOT rules (per the Anthropic Opus 4.7 migration guide).
```

> **Low-activity repos**: For repos with fewer than 10 commits in 90 days, extend the window — replace `90 days` with `365 days` in Step 1.

## What It Does

1. **Collects project signals** — CLAUDE.md state, harness layout, commit patterns, session quality, model version.
2. **Fetches the routing map** ([AUDIT-CONTEXT.md](AUDIT-CONTEXT.md)) — tells the agent which analysis docs apply to *your* signals.
3. **Conditionally fetches 4–8 analysis docs** — not all 28. Routing is deterministic and auditable.
4. **Produces a tiered recommendation set** — every recommendation cites its source doc + evidence tier.

This design solves a real problem: other projects do not need advice on federated query architecture if they are a library, and they do not need MCP advice if they have no MCP. The routing map filters the 28 analysis docs down to the ones that match what the agent actually observed.

## Structured Output Format

```markdown
---
audit-date: YYYY-MM-DD
repo-name: {name}
repo-path: {local path or GitLab path}
audit-type: local | gitlab-api
period-days: {90 or 365}
docs-fetched: [list of analysis/*.md files fetched]
---

# Audit: {repo-name}

## Vitals

| Metric | Value |
|--------|-------|
| Last commit | {date} |
| Commits in period | {N} |
| AI co-authoring rate | {X%} |
| Primary language | {lang} |
| Model version(s) in use | {e.g., Opus 4.7, Sonnet 4.6, unknown} |
| Harness components | {count — CLAUDE.md, hooks, rules, skills, agents, commands, settings.json} |

## Signals Observed

{Bulleted list of what triggered each fetch. Example:
- CLAUDE.md is 187 lines → fetched claude-md-progressive-disclosure.md (>150 trigger)
- settings.json references opus-4-7 → fetched model-migration-anti-patterns.md
- .claude/hooks/ present → fetched harness-engineering.md, safety-and-sandboxing.md}

## Harness Inventory

- [ ] CLAUDE.md (root or .claude/) — {line count or "missing"}
- [ ] .claude/settings.json — {yes/no}
- [ ] .claude/rules/ — {count} rule files
- [ ] .claude/hooks/ — {list or "none"}
- [ ] .claude/skills/ — {count} skills
- [ ] .claude/agents/ — {count} custom subagents
- [ ] .claude/commands/ — {count} commands

## Session Quality (claude-doctor)

| Signal | Count | Action |
|--------|-------|--------|
| edit-thrashing | {N} | {if >5: missing file-pattern knowledge — add rule or CLAUDE.md content} |
| error-loop | {N} | {if >3: no error recovery — add harness-level remediation} |
| negative-sentiment | {N} | {directional only — do not act on this alone} |
| repeated-instructions | {N} | {if >2: the repeated thing belongs in CLAUDE.md} |

**Sessions analyzed**: {N}
**Note**: The composite health percentage uses arbitrary severity weights. Interpret signals individually (see `analysis/session-quality-tools.md`).

## Commit Patterns

{2–4 bullets on what the commit history reveals — file hotspots, commit frequency, change categories, AI co-authoring trend.}

## Model Migration Exposure

{Only fill this section if model version was Opus 4.6 → 4.7 territory. List any of the six anti-patterns (vague descriptors, edge-case gestures, unanchored triggers, implicit subagent dispatch, missing verbosity directives, references without read-enforcement) found in CLAUDE.md, rules, skills, or agent frontmatter. Cite `analysis/model-migration-anti-patterns.md`.}

## Recommendations

### High Priority (Tier A backing)
1. **{recommendation}**
   - Signal: {what was observed}
   - Source: `analysis/{doc}.md` (Tier A)
   - Action: {concrete next step}

### Medium Priority (Tier B backing)
1. **{recommendation}**
   - Signal: {what was observed}
   - Source: `analysis/{doc}.md` (Tier B)
   - Action: {concrete next step}

### Low Priority (Tier C or advisory)
1. **{recommendation}** — Source: `analysis/{doc}.md` (Tier C)

## What's Working Well

{Positive patterns with evidence — confirm what not to change.}

## Staleness Assessment

**Status**: {active | maintenance | stale | dormant | archived}
{If stale: days since last activity; whether this seems intentional.}

## Open Revalidation Triggers

{Any claims in CLAUDE.md or rules that were validated on a prior model version and should be re-tested on the current model. See `analysis/evidence-based-revalidation.md`.}
```

## Why Routing Beats a Single Fetch

The prior version of this prompt fetched a sources index and asked the agent to cross-reference commits against it. That worked for authority weighting but had three gaps:

1. **Blind to applicability** — a library project got federated-query recommendations because the source was high-authority, not because it applied.
2. **Blind to model version** — no mechanism to surface Opus 4.7 migration risks, since the sources list is version-agnostic.
3. **No audit trail** — "Boris Cherny says so" is not the same as "`analysis/behavioral-insights.md` Tier A says so on line 43."

Routing via [AUDIT-CONTEXT.md](AUDIT-CONTEXT.md) fixes all three: advisories are matched to signals, model version is a signal, and every recommendation carries a doc+tier citation you can click through.

## Customization

Append to the prompt for a narrower audit:

- `...focus on security patterns` — Biases routing toward safety-and-sandboxing, secure-code-generation, mcp-patterns.
- `...focus on agent architecture` — Biases routing toward harness-engineering, orchestration-comparison, agent-principles.
- `...focus on Opus 4.7 migration readiness` — Forces a fetch of model-migration-anti-patterns.md regardless of model-version detection.
- `...compare against {other repo path}` — Runs the audit twice and produces a diff.

## Evidence Tiers Quick Reference

- **Tier A**: Anthropic engineering blog, Anthropic official docs, primary production observation (yours or the 7-repo portfolio).
- **Tier B**: Expert practitioner with production metrics, peer-reviewed research, validated community patterns.
- **Tier C**: Community observation, single-source reports, self-published tools.

Full authority-weighted list: [SOURCES-QUICK-REFERENCE.md](SOURCES-QUICK-REFERENCE.md). Tier definitions and citation format: [analysis/evidence-tiers.md](analysis/evidence-tiers.md).

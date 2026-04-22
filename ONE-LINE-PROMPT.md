# Adaptive Routing Audit (one copy-paste)

Copy-paste this prompt into Claude Code in **any project** to get an evidence-based audit of your harness, commit patterns, CLAUDE.md, and model-migration exposure — with every recommendation tied to a specific analysis doc, evidence tier, and the project signal that triggered the match.

**Expectation-setting**: This is one prompt, but not one network call. The audit fetches a routing map (1 request) plus 4–8 analysis docs (4–8 requests) via `WebFetch`. Typical round-trip: 6–10 requests, 1–5 minutes depending on connection. If that's too much, narrow the scope with one of the Customization flags at the bottom.

## The Prompt

```
Audit this project against Claude Code best practices using the adaptive routing protocol.

STEP 1 — COLLECT SIGNALS (in parallel where possible):
Run each of these and capture output for Step 3 routing:

- Read CLAUDE.md: check ./CLAUDE.md and .claude/CLAUDE.md. Note line count. Grep for vague descriptors and unanchored triggers:
  grep -nEi "\b(best practices|idiomatic|robust|proper|clean code)\b" CLAUDE.md .claude/CLAUDE.md 2>/dev/null
  grep -nEi "\b(where applicable|as needed|if relevant|consider edge cases)\b" CLAUDE.md .claude/CLAUDE.md 2>/dev/null
  grep -nE "see (rules/|\.claude/|[A-Z])" CLAUDE.md .claude/CLAUDE.md 2>/dev/null
- Commit patterns (90 days): git log --oneline --since="90 days ago" | head -50
  Files touched: git log --since="90 days ago" --name-only --format="" | sort | uniq -c | sort -rn | head -20
  If commit count < 10, retry with --since="365 days ago".
- Harness layout: ls -la .claude/ .claude/hooks/ .claude/rules/ .claude/skills/ .claude/agents/ .claude/commands/ 2>/dev/null
  cat .claude/settings.json 2>/dev/null | head -40
- Model version detection: grep -REi "opus-4-?[567]|sonnet-4-?[567]|claude-[0-9]" .claude/ .github/workflows/ 2>/dev/null
- Session diagnostics: npx -y claude-doctor 2>/dev/null || echo "claude-doctor not available"
- Project type: read README.md first 30 lines to classify (docs / data pipeline / library / hybrid-llm / research / multi-repo / other).

EDGE CASES — handle silently, do not fail the audit:
- No .claude/ directory: signal = harness-minimal (if CLAUDE.md exists) or claude-md-missing (if not).
- No git history or bare repo: skip commit-pattern rows; note in output.
- settings.json has no model field: signal = model-version-unknown.
- claude-doctor unavailable: skip session rows; note in output.
- WSL / non-POSIX paths: commands still work; treat any command failure as "signal not observed."

STEP 2 — FETCH ROUTING MAP:
WebFetch https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/AUDIT-CONTEXT.md

STEP 3 — ROUTE TO APPLICABLE ADVISORIES:
For each Signal row in AUDIT-CONTEXT.md whose verifiable condition matches what you observed in Step 1, note the Fetch column. Also include the three Always Fetch docs unconditionally.

Deduplicate: if multiple rows list the same doc, fetch it once.

Apply the Anti-Bloat Rule (AUDIT-CONTEXT.md § Anti-Bloat Rule):
- Count signal-triggered fetches only (Always Fetch docs don't count).
- If > 8, drop rows in the order specified: uncertain signals first, then overlap, then adjacent-not-central.
- Target 4–8 signal-triggered + 3 baseline = 7–11 total docs.

Fetch each selected doc from https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/{path}.

STEP 4 — PRODUCE AUDIT:
Use the structured output format below. Every recommendation MUST include:
- Signal key (e.g., model-version-4-7)
- Source doc path (e.g., analysis/model-migration-anti-patterns.md)
- Evidence tier (read from the doc's YAML frontmatter `evidence-tier:` field, NOT prose)
- Concrete action

For session diagnostics, act on edit-thrashing and error-loop counts only. Treat the composite health percentage as directional; do not cite it as a score.

Prefer positive examples over MUST NOT rules in recommendations (per Anthropic Opus 4.7 migration guide: "Positive examples... tend to be more effective than negative examples").
```

## Structured Output Format

```markdown
---
audit-date: YYYY-MM-DD
repo-name: {name}
repo-path: {local path}
period-days: {90 or 365}
docs-fetched: [analysis/foo.md, analysis/bar.md, ...]
signals-triggered: [signal-key-1, signal-key-2, ...]
---

# Audit: {repo-name}

## Vitals

| Metric | Value |
|--------|-------|
| Last commit | {date} |
| Commits in period | {N} |
| AI co-authoring rate | {X%} |
| Primary language | {lang} |
| Model version(s) detected | {e.g., Opus 4.7; or "unknown"} |
| Harness components | {count — which of: CLAUDE.md, hooks, rules, skills, agents, commands, settings.json} |

## Signals Observed

Bulleted list of what triggered each fetch. Example:
- `claude-md-size`: CLAUDE.md is 187 lines → fetched claude-md-progressive-disclosure.md
- `model-version-4-7`: settings.json references claude-opus-4-7 → fetched model-migration-anti-patterns.md
- `harness-hooks`: .claude/hooks/ present → fetched harness-engineering.md, safety-and-sandboxing.md

## Harness Inventory

- [ ] CLAUDE.md — {line count, or "missing"}
- [ ] .claude/settings.json — {yes/no}
- [ ] .claude/rules/ — {count}
- [ ] .claude/hooks/ — {list or "none"}
- [ ] .claude/skills/ — {count}
- [ ] .claude/agents/ — {count}
- [ ] .claude/commands/ — {count}

## Session Quality (claude-doctor)

| Signal | Count | Action |
|--------|-------|--------|
| edit-thrashing | {N} | {if >5: missing file-pattern knowledge — add rule or CLAUDE.md content} |
| error-loop | {N} | {if >3: no error recovery — add harness-level remediation} |
| negative-sentiment | {N} | {directional only — do not act on this alone} |
| repeated-instructions | {N} | {if >2: the repeated thing belongs in CLAUDE.md} |

**Note**: composite health percentage uses arbitrary severity weights. Interpret signals individually — see `analysis/session-quality-tools.md` § Gaps.

## Commit Patterns

2–4 bullets on what the commit history reveals: file hotspots, commit frequency, AI co-authoring trend, any security-sensitive paths touched.

## Model Migration Exposure

Only fill this section if model version signals triggered a fetch of `model-migration-anti-patterns.md`. For each of the six anti-patterns (vague quality descriptors, edge-case gestures, unanchored triggers, implicit subagent dispatch, missing verbosity directives, references without read-enforcement), report:

- **Found / Not found**
- **Locations** (file:line) if found
- **Recommended positive-framed fix** per the doc's remediation table

## Recommendations

### High Priority (Tier A backing)

1. **{recommendation title}**
   - Signal: `{signal-key}` — {what was observed}
   - Source: `analysis/{doc}.md` (evidence-tier: A)
   - Action: {concrete next step, with a file:line if applicable}

### Medium Priority (Tier B backing)

1. **{recommendation title}**
   - Signal: `{signal-key}`
   - Source: `analysis/{doc}.md` (evidence-tier: B)
   - Action: {concrete next step}

### Low Priority (Tier C or advisory)

1. **{recommendation}** — Source: `analysis/{doc}.md` (evidence-tier: C)

## What's Working Well

Positive patterns with evidence — confirm what not to change.

## Staleness Assessment

**Status**: `active | maintenance | stale | dormant | archived`

If stale: days since last activity; whether this seems intentional.

## Open Revalidation Triggers

Any claims in CLAUDE.md, rules, or skills that were validated on a prior model version and should be re-tested on the current model. Cite `analysis/evidence-based-revalidation.md`.
```

## Worked Example Recommendation

This is the exact citation format required:

```markdown
**Migrate implicit subagent dispatch in `.claude/agents/builder.md:14`**
- Signal: `model-version-4-7` (settings.json references `claude-opus-4-7`)
  AND `harness-custom-agents` (.claude/agents/builder.md exists)
- Source: `analysis/model-migration-anti-patterns.md` (evidence-tier: Mixed)
- Action: Replace the line "Dispatch the work to available subagents" with an explicit mechanism, e.g., "Use the Explore subagent to scan src/, then the Plan subagent to design the change." This matches Opus 4.7's explicit-dispatch default and aligns with Anthropic's preference for positive examples over MUST NOT rules.
```

Three things make this compliant:

1. **Signal key cited**, not a narrative description.
2. **Source doc + frontmatter-extracted tier**, not prose claims.
3. **Concrete action with file:line**, not a high-level suggestion.

## Why Routing Beats a Single Fetch

The prior version of this prompt fetched a sources index and asked the agent to cross-reference commits against it. That worked for authority weighting but had three gaps:

1. **Blind to applicability** — a library project got federated-query recommendations because the source was high-authority, not because the source applied to the project.
2. **Blind to model version** — no mechanism surfaced Opus 4.7 migration risks.
3. **No audit trail** — "Boris Cherny says so" is not the same as "`analysis/behavioral-insights.md` evidence-tier A says so."

Routing via [AUDIT-CONTEXT.md](AUDIT-CONTEXT.md) fixes all three: advisories match observable signals, model version is a first-class signal, and every recommendation carries a doc + tier + signal citation that a reader can verify.

## Customization

Append one of these to narrow the audit:

- `...focus on security patterns` — bias routing toward `safety-and-sandboxing.md`, `secure-code-generation.md`, `mcp-patterns.md`.
- `...focus on agent architecture` — bias routing toward `harness-engineering.md`, `orchestration-comparison.md`, `agent-principles.md`.
- `...focus on Opus 4.7 migration readiness` — force-fetch `model-migration-anti-patterns.md` regardless of model-version detection. Useful for pre-upgrade audits.
- `...compare against {other repo path}` — runs the audit twice and produces a diff.
- `...skip session diagnostics` — omits claude-doctor. Use when `~/.claude/projects/` is empty or transcripts are irrelevant.

## Evidence Tiers Quick Reference

- **Tier A**: Anthropic engineering blog, Anthropic official docs, first-party production observation.
- **Tier B**: Expert practitioner with production metrics, peer-reviewed research, validated community patterns.
- **Tier C**: Community observation, single-source reports, self-published tools.

Full authority-weighted list: [SOURCES-QUICK-REFERENCE.md](SOURCES-QUICK-REFERENCE.md). Tier definitions and citation format: [analysis/evidence-tiers.md](analysis/evidence-tiers.md). Routing map: [AUDIT-CONTEXT.md](AUDIT-CONTEXT.md).

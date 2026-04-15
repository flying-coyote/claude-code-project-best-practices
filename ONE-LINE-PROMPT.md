# One-Line Project Review Prompt

Copy-paste this prompt into Claude Code in **any project** to get authority-weighted
recommendations based on your recent work patterns and current best practices.

## The Prompt

```
Review this project: read the CLAUDE.md (check both ./CLAUDE.md and .claude/CLAUDE.md), analyze the last 90 days of git commits (git log --oneline --since="90 days ago" && git log --since="90 days ago" --name-only --format="" | sort | uniq -c | sort -rn | head 20), inspect harness structure (ls -la .claude/ .claude/rules/ .claude/hooks/ .claude/skills/ .claude/commands/ CLAUDE.md .claude/settings.json 2>/dev/null), then fetch https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/SOURCES-QUICK-REFERENCE.md and cross-reference my commit patterns and harness structure against those sources. Weight recommendations by the source authority tiers (5=Foundational like Anthropic docs, 2=Commentator like YouTube). Prioritize high-authority recent sources. Output using the STRUCTURED FORMAT described in the prompt source document.
```

> **Low-activity repos**: For repos with fewer than 10 commits in 90 days, extend
> the window: replace `90 days` with `365 days` to capture meaningful patterns.

## What It Does

1. **Reads your CLAUDE.md** — Understands your project's current configuration
2. **Analyzes recent commits** — Identifies patterns in how work is being done
3. **Inspects harness structure** — Checks for CLAUDE.md, rules, hooks, skills, commands, settings
4. **Fetches best-practice sources** — Cross-references against 21 authority-weighted sources
5. **Produces weighted recommendations** — High priority (Foundational sources) vs worth noting (Commentator sources)
6. **Celebrates what works** — Not just criticism; identifies positive patterns to keep

## Structured Output Format

Every audit must produce this exact structure so results can be aggregated across repos:

```markdown
---
audit-date: YYYY-MM-DD
repo-name: {name}
repo-path: {local path or GitLab path}
audit-type: local | gitlab-api
period-days: {90 or 365}
---

# Audit: {repo-name}

## Vitals

| Metric | Value |
|--------|-------|
| Last commit | {date} |
| Commits in period | {N} |
| Contributors | {names} |
| Primary language | {lang} |
| AI co-authoring rate | {X%} |
| Harness score | {0-6} |

## Harness Inventory

- [ ] CLAUDE.md (root or .claude/) — {line count or "missing"}
- [ ] .claude/settings.json — {yes/no}
- [ ] .claude/rules/ — {count} rule files
- [ ] .claude/hooks/ — {list or "none"}
- [ ] .claude/skills/ — {count} skills
- [ ] .claude/commands/ — {count} commands

## Commit Patterns

{2-4 bullet points on what the commit history reveals — file hotspots,
commit frequency, change categories, test co-location}

## Recommendations

### High Priority (Foundational/Authoritative backing)
1. **{recommendation}** — Source: {name} (Authority {tier}, Weight {score})

### Medium Priority (Practitioner backing)
1. **{recommendation}** — Source: {name} (Authority {tier}, Weight {score})

## What's Working Well

- {positive pattern with evidence}

## Staleness Assessment

**Status**: {active | maintenance | stale | dormant | archived}
{If stale: days since last activity, whether this seems intentional}

## Cross-Repo Notes

{Dependencies on or from other repos. Overlaps with similar projects. Gaps.}
```

## Authority Weighting

The prompt uses a 0-5 authority scale:
- **5 (Foundational)**: Boris Cherny, Anthropic engineering blog — always relevant
- **4 (Authoritative)**: OWASP, peer-reviewed research, Apache PMC
- **3 (Practitioner)**: Named engineers with production metrics
- **2 (Commentator)**: YouTube creators, bloggers — useful signals but verify claims
- **1 (Unverified)**: Vendor marketing, speculation
- **0 (Rejected)**: Debunked claims

Foundational sources have a recency floor of 0.7 — a 6-month-old Anthropic
engineering blog post (weight 0.70) outweighs a fresh YouTube clickbait video
(weight 0.35) by 2x.

## Customization

Add to the prompt for specific focus areas:
- `...focus on security patterns` — Emphasizes OWASP MCP Top 10, sandboxing
- `...focus on agent architecture` — Emphasizes harness engineering, orchestration
- `...focus on MCP usage` — Emphasizes MCP vs Skills economics, plugin patterns
- `...compare against [other project]` — Cross-project pattern comparison

# Hybrid Preset

> **ARCHIVED — but nothing live replaces it.** Archived in the v2.0 repositioning (March 2026, DECISIONS.md § Reposition as Analytical Layer) or a later reduction. Archived v1 material with no live successor. analysis/agent-driven-development.md and analysis/harness-engineering.md carry only this preset's generic "start minimal, add infrastructure when specific friction forces it" heuristic — they do not cover what this document is for: classifying mixed-purpose (code + content + research) projects, the tier-keyed starter component table (permissions.allow, Stop/Session hooks, GitHub Actions), the Quality Standards and Git Workflow CLAUDE.md blocks, or when to switch to a specialized preset. No live analysis document discusses mixed-purpose project classification; the four-preset scheme is retired v1 design (DECISIONS.md Decision 2), and this document's own pointer, archive/patterns-v1/project-infrastructure.md, is archived as well. This is a **coverage gap, not a currency gap** — the material is unreplaced, not merely out of date, so a reader who discards it is left with nothing. Its specifics are v1-era; its subject is still uncovered. (Marked 2026-08-28; successor determined by mapping plus adversarial verification, which overturned 35 of 39 successor claims — see `analysis/prose-corpus-discoverability.md`.)

For mixed-purpose projects combining code, content, and/or research.

## When to Use

Choose this preset when your project:
- Has both `src/` and `docs/`
- Combines code with documentation
- Doesn't fit cleanly into other categories
- Has unclear or evolving purpose

## Quality Standards

```markdown
## Quality Standards

- Clean code with clear intent and appropriate tests
- Evidence-based claims with documented sources
- Balanced perspective acknowledging trade-offs
- Meaningful commit messages
- Intellectual honesty over marketing claims
```

## Recommended Components

| Component | Tier | Recommended | Why |
|-----------|------|-------------|-----|
| permissions.allow | 1 | ✅ Yes (baseline) | Pre-approve git read commands |
| Stop hook | 1 | ✅ Yes (baseline) | Uncommitted/unpushed reminders |
| CLAUDE.md | 2 | ✅ Yes | Project context |
| Session hook | 2 | ✅ Yes | Shows project status |
| Post-tool hook | 2 | Optional | Based on workflow |
| GitHub Actions | 3 | For teams | @.claude reviews |

See [Project Infrastructure Pattern](../patterns-v1/project-infrastructure.md) for the full tiered approach.

## Flexibility

The hybrid preset is intentionally broad. Customize by:

1. **Starting minimal**: Just CLAUDE.md + session hook
2. **Adding as needed**: More sections, more hooks
3. **Specializing later**: Switch to specific preset if project focus clarifies

## Git Workflow

```markdown
## Git Workflow

Commit messages follow conventional format:
- `feat:` New features
- `fix:` Bug fixes
- `docs:` Documentation changes
- `refactor:` Code refactoring
- `test:` Test additions/changes
- `chore:` Maintenance tasks

Optional emoji prefixes:
- `✅` Milestone completions
- `📊` Research and analysis
- `🔧` Fixes and corrections
- `📚` Documentation improvements
```

## When to Switch Presets

Consider switching to a specific preset if:
- Project becomes primarily code → `coding`
- Project becomes primarily content → `writing`
- Project becomes primarily research → `research`

The hybrid preset works well for projects that genuinely serve multiple purposes.

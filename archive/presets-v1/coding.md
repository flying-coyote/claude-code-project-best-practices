# Coding Preset

> **ARCHIVED — but nothing live replaces it.** Archived in the v2.0 repositioning (March 2026, DECISIONS.md § Reposition as Analytical Layer) or a later reduction. Archived v1 artifact with no live successor. `analysis/agent-driven-development.md` is topically adjacent — its Infrastructure Maturity Model names harness component sets by level — but it does not cover this file: it contains no project-type recognition signals (package.json / Cargo.toml / pyproject.toml / go.mod / pom.xml), no code-quality-standards block, no conventional-commit workflow text, and none of the preset table's permissions.allow baseline, PostToolUse auto-format, or GitHub Actions PR-review rows. Its maturity levels are indexed on observed repo maturity, not on project type, so they answer a different question. The preset concept itself was retired in the v2.0 repositioning (DECISIONS.md Decisions 2 and 5) without replacement; both of this file's pointers are dead — `../patterns-v1/project-infrastructure.md` is itself archived, and `../examples/coding-project/.claude/CLAUDE.md` no longer exists. Read as v1 history only. This is a **coverage gap, not a currency gap** — the material is unreplaced, not merely out of date, so a reader who discards it is left with nothing. Its specifics are v1-era; its subject is still uncovered. (Marked 2026-08-28; successor determined by mapping plus adversarial verification, which overturned 35 of 39 successor claims — see `analysis/prose-corpus-discoverability.md`.)

For software development projects: libraries, tools, applications.

## When to Use

Choose this preset when your project:
- Has `package.json`, `Cargo.toml`, `pyproject.toml`, `go.mod`, or `pom.xml`
- Is primarily source code
- Focuses on building software

## Quality Standards

```markdown
## Code Quality Standards

- Write clean, maintainable code with clear intent
- Test-driven development where applicable
- Meaningful commit messages following conventional format
- No premature optimization
- Avoid over-engineering - only make requested changes
```

## Recommended Components

| Component | Tier | Recommended | Why |
|-----------|------|-------------|-----|
| permissions.allow | 1 | ✅ Yes (baseline) | Pre-approve git read commands |
| Stop hook | 1 | ✅ Yes (baseline) | Uncommitted/unpushed reminders |
| CLAUDE.md | 2 | ✅ Yes | Project context |
| Session hook | 2 | ✅ Yes | Shows git status, recent commits |
| Post-tool hook | 3 | Optional | Auto-format with prettier/black |
| GitHub Actions | 3 | For teams | @.claude PR reviews |

See [Project Infrastructure Pattern](../patterns-v1/project-infrastructure.md) for the full tiered approach.

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
```

## Example CLAUDE.md

See [examples/coding-project/.claude/CLAUDE.md](../examples/coding-project/.claude/CLAUDE.md)

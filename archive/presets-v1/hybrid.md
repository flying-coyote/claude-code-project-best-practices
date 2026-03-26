# Hybrid Preset

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

See [Project Infrastructure Pattern](../patterns/project-infrastructure.md) for the full tiered approach.

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

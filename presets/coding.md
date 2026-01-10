# Coding Preset

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

See [Project Infrastructure Pattern](../patterns/project-infrastructure.md) for the full tiered approach.

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

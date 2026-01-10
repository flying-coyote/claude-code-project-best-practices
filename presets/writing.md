# Writing Preset

For content creation projects: books, blogs, documentation.

## When to Use

Choose this preset when your project:
- Has `chapters/`, `drafts/`, or similar content structure
- Is primarily markdown or documentation
- Focuses on written content for publication

## Quality Standards

```markdown
## Content Quality Standards

- Evidence-based claims with documented sources
- Balanced perspective acknowledging trade-offs
- Consistent voice and tone throughout
- Intellectual honesty over marketing claims
- Academic quality suitable for peer review
```

## Recommended Components

| Component | Tier | Recommended | Why |
|-----------|------|-------------|-----|
| permissions.allow | 1 | ✅ Yes (baseline) | Pre-approve git read commands |
| Stop hook | 1 | ✅ Yes (baseline) | Uncommitted/unpushed reminders |
| CLAUDE.md | 2 | ✅ Yes | Project context, voice guidelines |
| Session hook | 2 | ✅ Yes | Shows current work status |
| Post-tool hook | 2 | Optional | Auto-update indexes if used |
| GitHub Actions | 3 | For teams | @.claude content reviews |

See [Project Infrastructure Pattern](../patterns/project-infrastructure.md) for the full tiered approach.

## Git Workflow

```markdown
## Git Workflow

Commit messages with optional emoji prefixes:
- `docs:` or `📚` Documentation changes
- `feat:` or `✅` New content sections
- `fix:` or `🔧` Corrections and fixes
- `refactor:` Content reorganization
- `chore:` Maintenance tasks
```

## Additional Sections

Consider adding to CLAUDE.md:

```markdown
## Voice and Tone

[Describe the voice/tone for this content]
- Conversational but authoritative
- Technical but accessible
- [Your specific guidelines]

## Citation Standards

Use evidence tiers for claims:
- Tier A: Primary sources, official documentation
- Tier B: Peer-reviewed, expert interviews
- Tier C: Industry reports, vendor docs
- Tier D: Opinions, speculation (label clearly)
```

## Example CLAUDE.md

See [examples/writing-project/.claude/CLAUDE.md](../examples/writing-project/.claude/CLAUDE.md)

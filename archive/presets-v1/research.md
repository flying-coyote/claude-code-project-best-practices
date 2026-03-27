# Research Preset

For analysis projects: studies, literature reviews, hypothesis tracking.

## When to Use

Choose this preset when your project:
- Has `concepts/`, `hypotheses/`, `bibliography/`, or `analysis/`
- Tracks research questions or hypotheses
- Requires rigorous evidence standards

## Quality Standards

```markdown
## Research Quality Standards

- Evidence tier classification for all claims (Tier A-D)
- Hypothesis tracking with confidence levels
- Source attribution and citation
- Document contradictions and limitations
- Reproducible methodology
```

## Recommended Components

| Component | Tier | Recommended | Why |
|-----------|------|-------------|-----|
| permissions.allow | 1 | ✅ Yes (baseline) | Pre-approve git read commands |
| Stop hook | 1 | ✅ Yes (baseline) | Uncommitted/unpushed reminders |
| CLAUDE.md | 2 | ✅ Yes | Project context, evidence tiers |
| Session hook | 2 | ✅ Yes | Shows research status |
| Post-tool hook | 2 | Optional | Auto-update indexes if tracking |
| GitHub Actions | 3 | For teams | @.claude research reviews |

See [Project Infrastructure Pattern](../patterns/project-infrastructure.md) for the full tiered approach.

## Evidence Tier System

Include in CLAUDE.md:

```markdown
## Evidence Tiers

- **Tier A**: Primary sources, production data, official specs
- **Tier B**: Peer-reviewed, expert interviews, validated analysis
- **Tier C**: Industry reports, vendor docs, practitioner blogs
- **Tier D**: Opinions, speculation (label as such)

Strong claims require Tier A or B evidence.
```

## Hypothesis Tracking

Consider adding:

```markdown
## Active Hypotheses

Track research hypotheses with:
- Clear, falsifiable statement
- Confidence level (1-5)
- Evidence tier of supporting data
- Validation method
```

## Git Workflow

```markdown
## Git Workflow

Commit messages:
- `research:` or `📊` New findings or analysis
- `docs:` or `📚` Documentation updates
- `data:` Data processing changes
- `hypothesis:` Hypothesis updates
- `cite:` Bibliography additions
```

## Example CLAUDE.md

See research project examples in the patterns documentation.

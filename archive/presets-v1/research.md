# Research Preset

> **ARCHIVED — not current guidance, and only partly succeeded.** Archived in the v2.0 repositioning (March 2026, DECISIONS.md § Reposition as Analytical Layer) or a later reduction. Partially superseded. The research-methodology half of this preset lives on in [analysis/evidence-tiers.md](../../analysis/evidence-tiers.md), which is a strict superset of both the evidence-tier block (Tier A-D with citation format, contradiction handling, and the merged HIGH/MEDIUM/LOW confidence framework) and the hypothesis-tracking block (its Documentation Format carries statement, evidence tier, contradictions, confidence, and validation status). The configuration half has no successor: the project-type recognition signals (`concepts/`, `hypotheses/`, `bibliography/`), the tiered component table (permissions.allow, Stop/Session/Post-tool hooks, GitHub Actions), and the research commit conventions (`research:`, `data:`, `hypothesis:`, `cite:`) appear nowhere in evidence-tiers.md or elsewhere in `analysis/` — this file remains their only record. Its v1-era specifics and dates are a snapshot, preserved as recorded — do not treat them as current. (Marked 2026-08-28; successor determined by mapping plus adversarial verification, which overturned 35 of 39 successor claims — see `analysis/prose-corpus-discoverability.md`.)

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

See [Project Infrastructure Pattern](../patterns-v1/project-infrastructure.md) for the full tiered approach.

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

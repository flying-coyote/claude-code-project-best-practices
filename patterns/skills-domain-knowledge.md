# Skills for Domain Knowledge: Embedding Expertise into AI Workflows

**Source**: [Aniket Panjwani](https://x.com/aniketapanjwani), validated by [Anthropic Skills Specification](https://agentskills.io)
**Evidence Tier**: A (Practitioner methodology + official specification)

## Overview

Domain knowledge skills embed specialized expertise into Claude Code workflows, enabling AI to operate with field-specific understanding rather than generic capabilities. This pattern extends beyond pure software development to research, content creation, analysis, and other knowledge work.

> "What makes Claude Code powerful are 'skills' and 'subagents,' which function as 'specialized AIs' for particular tasks, allowing researchers to embed their domain knowledge productively."
> — Aniket Panjwani

**Core Insight**: Skills aren't just coding instructions—they're containers for domain expertise that transform Claude from a general assistant into a specialized collaborator.

---

## The Pattern

### Why Domain Skills Matter

| Without Domain Skills | With Domain Skills |
|----------------------|-------------------|
| Generic responses | Field-specific outputs |
| Misses domain conventions | Follows established practices |
| Requires constant correction | Works within constraints |
| Reinvents from scratch | Builds on existing knowledge |
| Session-bound context | Persistent expertise |

### Domain Skill Structure

```
.claude/skills/<domain>/
├── SKILL.md              # Core domain knowledge + routing
├── workflows/
│   ├── research.md       # Phase 1: Discovery/gathering
│   ├── analysis.md       # Phase 2: Processing/reasoning
│   ├── creation.md       # Phase 3: Producing output
│   └── validation.md     # Phase 4: Quality verification
└── resources/
    ├── templates/        # Domain-specific templates
    ├── examples/         # Reference outputs
    └── constraints.md    # Rules and limitations
```

---

## Implementation Patterns

### Pattern 1: Phase-Based Skills

Break complex domain workflows into distinct skills per phase:

```
Newsletter Production (Aniket's Example):
├── research-skill/       → Gather local news sources
├── writing-skill/        → Draft content from research
├── polishing-skill/      → Refine and edit
└── deploy-skill/         → Publish to platform
```

**Benefits**:
- Each skill is focused and maintainable
- Phases can be run independently
- Easy to iterate on specific phases
- Reduces context per invocation

**SKILL.md Example** (Research Phase):

```markdown
---
name: local-news-research
description: Gather and synthesize local news for newsletter content
---

# Local News Research Skill

## Purpose
Collect, filter, and summarize local news from configured sources for newsletter production.

## Domain Knowledge

### Source Types
- Government meeting agendas (city council, school board)
- Local business announcements
- Community event calendars
- Police/fire department reports

### Quality Criteria
- Relevance to geographic area (configured in project)
- Timeliness (within last 7 days unless historical context needed)
- Community impact (affects residents, businesses, institutions)

### Output Format
Produce structured research notes:
- Source URL and date
- Key facts (who, what, when, where)
- Relevance score (HIGH/MEDIUM/LOW)
- Suggested angle for newsletter
```

### Pattern 2: Discipline-Specific Skills

Embed methodology from established fields:

#### Economics/Social Science Research

```markdown
---
name: causal-analysis
description: Conduct causal inference analysis following econometric best practices
---

# Causal Analysis Skill

## Domain Knowledge

### Identification Strategy
Before any regression:
1. State the causal question explicitly
2. Identify potential confounders
3. Describe the source of variation
4. Assess threats to internal validity

### Standard Approaches
- Difference-in-differences: parallel trends assumption
- Instrumental variables: relevance + exclusion restriction
- Regression discontinuity: manipulation tests, bandwidth sensitivity
- Matching: balance checks, sensitivity analysis

### Reporting Standards
- Always report robust standard errors
- Include relevant fixed effects
- Show balance tables for observational comparisons
- Discuss external validity limitations

### Red Flags
- NEVER claim causation without identification strategy
- ALWAYS acknowledge selection concerns
- FLAG if sample size is small for chosen method
```

#### Security Research

```markdown
---
name: vulnerability-assessment
description: Conduct security analysis following OWASP methodology
---

# Vulnerability Assessment Skill

## Domain Knowledge

### Assessment Framework (OWASP)
1. Information Gathering
2. Configuration Management Testing
3. Authentication Testing
4. Authorization Testing
5. Session Management Testing
6. Input Validation Testing

### Severity Classification (CVSS)
- Critical (9.0-10.0): Immediate action required
- High (7.0-8.9): Address within 24-48 hours
- Medium (4.0-6.9): Address within sprint
- Low (0.1-3.9): Track for future remediation

### Reporting Format
- Finding title
- Severity + CVSS score
- Affected component
- Steps to reproduce
- Recommended remediation
- References (CWE, CVE if applicable)
```

### Pattern 3: Workflow Integration Skills

Skills that connect domain knowledge to specific tools/processes:

```markdown
---
name: academic-paper-review
description: Review academic papers with domain-specific critical analysis
---

# Academic Paper Review Skill

## Domain Knowledge

### Review Dimensions
1. **Contribution**: Is the research question novel and important?
2. **Methodology**: Is the approach appropriate and rigorous?
3. **Evidence**: Do the results support the claims?
4. **Writing**: Is the paper clear and well-organized?

### Field-Specific Considerations
- For empirical work: identification strategy, data quality
- For theoretical work: assumptions, proof validity
- For applied work: practical relevance, implementation

### Output Structure
```
## Summary (2-3 sentences)
## Main Contribution
## Strengths
## Weaknesses
## Minor Issues
## Recommendation: Accept / Revise / Reject
```

### Integration with MCP
If Semantic Scholar MCP is enabled:
- Fetch citation context automatically
- Check if key claims are supported by cited works
- Identify missing relevant citations
```

---

## Creating Domain Skills

### Step 1: Identify Domain Boundaries

What field-specific knowledge does this workflow require?

```markdown
## Domain Checklist

- [ ] What terminology is unique to this field?
- [ ] What methodologies are standard practice?
- [ ] What output formats are expected?
- [ ] What quality criteria define "good work"?
- [ ] What mistakes would an expert never make?
- [ ] What constraints must always be respected?
```

### Step 2: Structure the Knowledge

Organize domain knowledge into actionable sections:

```markdown
# [Domain] Skill

## Terminology
[Key terms and their precise meanings]

## Methodology
[Standard approaches and when to use each]

## Quality Criteria
[What separates good from poor output]

## Constraints
[Non-negotiable rules]

## Examples
[Reference outputs to emulate]

## Anti-Patterns
[Common mistakes to avoid]
```

### Step 3: Add Phase Workflows

If the domain involves multi-step processes:

```
workflows/
├── phase-1-*.md    # First phase (e.g., research, discovery)
├── phase-2-*.md    # Second phase (e.g., analysis, processing)
├── phase-3-*.md    # Third phase (e.g., creation, synthesis)
└── phase-4-*.md    # Final phase (e.g., validation, delivery)
```

### Step 4: Include Resources

```
resources/
├── templates/      # Boilerplate for common outputs
├── examples/       # High-quality reference outputs
├── checklists/     # Verification checklists
└── constraints.md  # Hard rules and limitations
```

---

## Best Practices

### Do: Encode Tacit Knowledge

Domain experts often have implicit knowledge they don't articulate:

```markdown
## Tacit Knowledge (Economics Example)

### Things Every Economist Knows But Rarely States
- Correlation ≠ causation (always requires identification)
- Selection bias is everywhere
- Heterogeneous treatment effects are the norm
- External validity rarely transfers cleanly
- Standard errors matter more than point estimates
```

### Do: Include Failure Modes

What goes wrong when domain knowledge is missing:

```markdown
## Common Failures Without This Skill

- Claiming causation from OLS regression
- Ignoring clustered standard errors
- Cherry-picking specifications
- Conflating statistical and economic significance
- Overfitting with too many controls
```

### Do: Provide Calibration Examples

Show what "good" looks like:

```markdown
## Calibration: What Good Output Looks Like

### Example: Summary of Empirical Paper
"Smith (2024) exploits a natural experiment arising from
staggered rollout of a policy across states to estimate
causal effects using difference-in-differences. The
parallel trends assumption is supported by event study
plots, though the post-treatment dynamics suggest
potential anticipation effects worth investigating."

### Example: What to Avoid
"Smith (2024) runs regressions and finds significant
effects of the policy on outcomes."
```

### Don't: Overload Context

Each skill should be focused. Split if too large:

```
❌ economics-skill/           # Too broad
   SKILL.md (2000 lines)

✅ economics/
   causal-inference/         # Focused
   time-series/              # Focused
   panel-data/               # Focused
```

### Don't: Duplicate Core Documentation

Reference existing docs, don't repeat:

```markdown
## Standards
See project CLAUDE.md for coding style.
This skill adds economics-specific methodology.
```

---

## Integration with SDD Phases

| SDD Phase | Domain Skill Role |
|-----------|------------------|
| **Specify** | Domain skills define what "correct" means for the field |
| **Plan** | Methodology sections guide technical approach |
| **Tasks** | Phase workflows break down domain-appropriate steps |
| **Implement** | Constraints and examples guide execution |

---

## Examples by Field

### Research/Academic
- Literature review skill (systematic search, synthesis)
- Hypothesis development skill (theory → testable predictions)
- Statistical analysis skill (field-appropriate methods)
- Paper writing skill (journal conventions)

### Content Creation
- Research phase skill (source gathering)
- Writing phase skill (tone, structure)
- Editing phase skill (quality criteria)
- Publishing phase skill (platform requirements)

### Business Analysis
- Market research skill (data sources, frameworks)
- Financial modeling skill (assumptions, validation)
- Competitive analysis skill (Porter's, SWOT)
- Strategy synthesis skill (recommendations)

### Software Engineering
- Code review skill (language-specific patterns)
- Architecture review skill (design principles)
- Security review skill (OWASP, threat modeling)
- Performance analysis skill (profiling, optimization)

---

## Measuring Effectiveness

### Signals of Good Domain Skills

| Signal | Indicator |
|--------|-----------|
| Fewer corrections | AI output matches domain expectations |
| Faster iteration | Less back-and-forth on basics |
| Consistent quality | Outputs follow field conventions |
| Expert approval | Domain experts recognize quality |

### Improvement Loop

```
1. Run workflow with domain skill
2. Note where corrections were needed
3. Add missing knowledge to skill
4. Re-run and compare
5. Repeat until minimal corrections
```

---

## Related Patterns

- [Progressive Disclosure](./progressive-disclosure.md) - Phase-based skill loading
- [Planning-First Development](./planning-first-development.md) - Skills in the Specify phase
- [Context Engineering](./context-engineering.md) - Skills as deterministic context

---

## Sources

- [Aniket Panjwani - Claude Code Tips](https://x.com/aniketapanjwani/status/1999487999604605345) - Plan-then-act with domain skills
- [Agent Skills Specification](https://agentskills.io) - Official skill format
- [Claude Code Skills Documentation](https://docs.anthropic.com/en/docs/claude-code/skills) - Implementation reference

*Last updated: January 2026*

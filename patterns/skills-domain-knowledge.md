---
version-requirements:
  claude-code: "v2.0.0+"  # Official skills support
measurement-claims:
  - claim: "Skills are 50% cheaper than MCP for methodology guidance"
    source: "mcp-vs-skills-economics.md"
    date: "2025-12-01"
    revalidate: "2026-12-01"
status: "PRODUCTION"
last-verified: "2026-02-16"
---

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
├── scripts/              # Optional: executable code (Python, Bash, etc.)
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

## YAML Frontmatter Reference

The YAML frontmatter is the most important part of any skill—it determines whether and when Claude loads the skill. Get this right.

### Required Fields

| Field | Rules | Example |
|-------|-------|---------|
| `name` | Kebab-case only, no spaces/capitals, match folder name | `causal-analysis` |
| `description` | What + When + Capabilities, under 1024 chars, no XML tags | See formula below |

### Description Formula

Structure descriptions as: **[What it does] + [When to use it] + [Key capabilities]**

Include trigger phrases users would actually say:

```yaml
# Good - specific, includes trigger phrases
description: Conduct causal inference analysis following econometric
  best practices. Use when user asks for "regression analysis",
  "causal estimation", "diff-in-diff", or "treatment effects".

# Bad - too vague, no triggers
description: Helps with economics research.

# Bad - too technical, no user language
description: Implements the Project entity model with hierarchical relationships.
```

### Optional Fields

| Field | Purpose | Example |
|-------|---------|---------|
| `allowed-tools` | Restrict tool access per skill | `"Bash(python:*) Bash(npm:*) WebFetch"` |
| `license` | For open-source distribution | `MIT`, `Apache-2.0` |
| `compatibility` | Environment requirements (1-500 chars) | `"Requires Python 3.10+, pandas"` |
| `metadata` | Custom key-value pairs | See below |

```yaml
---
name: causal-analysis
description: Conduct causal inference analysis following econometric
  best practices. Use when user asks for "regression analysis",
  "causal estimation", "diff-in-diff", or "treatment effects".
allowed-tools: "Bash(python:*) Bash(Rscript:*)"
license: MIT
compatibility: "Requires R or Python with statsmodels"
metadata:
  author: Research Team
  version: 1.0.0
  category: research
  tags: [economics, statistics, causal-inference]
---
```

### Security Restrictions

**Forbidden in frontmatter** (because frontmatter appears in Claude's system prompt):
- XML angle brackets (`<` `>`) — malicious content could inject instructions
- Skills named with "claude" or "anthropic" prefix (reserved)
- Code execution in YAML (safe YAML parsing enforced)

---

## Design Heuristic: Problem-First vs. Tool-First

Before building a skill, decide which framing fits your use case:

| Approach | User Says | Skill Does |
|----------|-----------|------------|
| **Problem-first** | "I need to set up a project workspace" | Orchestrates the right tools in the right sequence |
| **Tool-first** | "I have Notion MCP connected" | Teaches Claude optimal Notion workflows and best practices |

**Problem-first**: Users describe outcomes; the skill handles tools. Best for workflow automation.
**Tool-first**: Users have tool access; the skill provides expertise. Best for MCP enhancement.

Most skills lean one direction. Knowing which framing fits helps you choose the right structure.

---

## Skill Categories

Anthropic identifies three common skill categories:

### Category 1: Document & Asset Creation
Creating consistent, high-quality output (documents, presentations, apps, code).
- Embedded style guides and brand standards
- Template structures for consistent output
- Quality checklists before finalizing
- No external tools required—uses Claude's built-in capabilities

### Category 2: Workflow Automation
Multi-step processes that benefit from consistent methodology.
- Step-by-step workflow with validation gates
- Templates for common structures
- Built-in review and improvement suggestions
- Iterative refinement loops

### Category 3: MCP Enhancement
Workflow guidance on top of MCP server tool access.
- Coordinates multiple MCP calls in sequence
- Embeds domain expertise for tool usage
- Provides context users would otherwise need to specify
- Error handling for common MCP issues

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

### Do: Use Negative Triggers

Prevent over-triggering by specifying what the skill should NOT handle:

```yaml
description: Advanced data analysis for CSV files. Use for statistical
  modeling, regression, clustering. Do NOT use for simple data
  exploration (use data-viz skill instead).
```

### Do: Debug Descriptions by Asking Claude

Test description quality by asking Claude directly: "When would you use the [skill name] skill?" Claude will quote the description back. Adjust based on what's missing or misleading.

### Do: Be Specific and Actionable in Instructions

```markdown
# Good - specific, actionable
Run `python scripts/validate.py --input {filename}` to check data format.
If validation fails, common issues include:
- Missing required fields (add them to the CSV)
- Invalid date formats (use YYYY-MM-DD)

# Bad - vague
Validate the data before proceeding.
```

### Do: Put Critical Instructions at the Top

Instructions buried deep in SKILL.md may be ignored. Use `## Important` or `## Critical` headers and put non-negotiable rules at the top, not the bottom.

### Do: Address Model Laziness Explicitly

For skills requiring thoroughness, add a performance section:

```markdown
## Performance Notes
- Take your time to do this thoroughly
- Quality is more important than speed
- Do not skip validation steps
```

> **Note**: Anthropic's guide observes this is more effective in **user prompts** than in SKILL.md. Consider adding to both.

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
- [Anthropic: The Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf) (Jan 2026) - YAML reference, description formula, skill categories, troubleshooting

*Last updated: February 2026*

# Architecture Decision Records (ADRs) for Claude Code Projects

**Source**: Production-validated pattern adapted from software engineering
**Evidence Tier**: B (Proven in software projects, emerging in research contexts)

## Purpose

Document "why" decisions were made, not just "what" was decided. ADRs create a decision audit trail that prevents amnesia and enables informed future choices.

## When to Use

ADRs are valuable for any project with:
- Architecture or design decisions
- Tool/vendor selection choices
- Research methodology decisions
- Infrastructure trade-offs
- Contradictory options requiring resolution

**Particularly useful for**:
- Software development projects
- Research projects with competing hypotheses
- Enterprise projects requiring governance
- Multi-person teams needing shared context
- Long-running projects where decisions compound

---

## Core Principles

### 1. Document Decisions, Not Implementations

**Good ADR**: "We chose Iceberg over Delta Lake because..."
**Bad ADR**: "Here's how Iceberg table format works..."

### 2. Capture Context and Constraints

The "why" requires understanding:
- What was the problem?
- What constraints existed?
- What alternatives were considered?
- What trade-offs did we accept?

### 3. ADRs Are Immutable

Once written, ADRs should not be edited (except for clarifications). If a decision changes, write a new ADR that supersedes the old one.

### 4. ADRs Link to Evidence

Every claim in an ADR should reference evidence tiers:
- Tier A/1: Production validation
- Tier B/2: Peer-reviewed research
- Tier C/3: Expert consensus

---

## ADR Structure

### Minimal Template

```markdown
# ADR-NNN: [Short Title]

**Status**: Proposed | Accepted | Deprecated | Superseded by ADR-XXX
**Date**: YYYY-MM-DD
**Deciders**: [Who made this decision]
**Evidence Tier**: [A/B/C/D for sources, 1-5 for research]

## Context

What is the issue we're trying to solve?
What constraints do we face?

## Decision

We will [decision statement].

## Rationale

Why this decision? What alternatives did we consider?

## Consequences

### Positive
- [Benefit 1]
- [Benefit 2]

### Negative
- [Trade-off 1]
- [Trade-off 2]

### Risks
- [Risk 1]
- [Risk 2]
```

### Comprehensive Template

For complex or high-stakes decisions:

```markdown
# ADR-NNN: [Short Title]

**Status**: Proposed | Accepted | Deprecated | Superseded by ADR-XXX
**Date**: YYYY-MM-DD
**Deciders**: [Names/Roles]
**Stakeholders**: [Who is affected]
**Evidence Tier**: [A/B/C/D], [1-5]
**Confidence**: HIGH | MEDIUM | LOW

## Context and Problem Statement

### The Problem
[Describe the problem in detail]

### Constraints
- [Constraint 1]
- [Constraint 2]

### Success Criteria
[How will we know this decision succeeded?]

## Considered Options

### Option 1: [Name]
**Pros**:
- [Pro 1]
- [Pro 2]

**Cons**:
- [Con 1]
- [Con 2]

**Evidence**: [Tier X sources]

### Option 2: [Name]
[Same structure]

### Option 3: [Name]
[Same structure]

## Decision

We chose **Option X: [Name]** because [primary reason].

## Detailed Rationale

### Why This Option
[Expanded reasoning]

### Why Not Other Options
- **Option 1**: [Specific reason for rejection]
- **Option 2**: [Specific reason for rejection]

### Evidence Supporting Decision
1. [Tier A/1 evidence]
2. [Tier B/2 evidence]
3. [Tier C/3 evidence]

### Contradictions and How We Resolved Them
- **Contradiction 1**: [Description and resolution]
- **Contradiction 2**: [Description and resolution]

## Consequences

### Immediate Impacts
- [Impact 1]
- [Impact 2]

### Long-Term Implications
- [Implication 1]
- [Implication 2]

### Accepted Trade-offs
- [Trade-off 1]
- [Trade-off 2]

### Mitigation Strategies
- [For trade-off 1]
- [For trade-off 2]

## Validation Plan

How will we validate this decision?
- [ ] Metric 1: [Target value]
- [ ] Metric 2: [Target value]
- [ ] Timeline: [When to review]

## Links and References

- [Related ADR-XXX]
- [Source 1] (Tier A)
- [Source 2] (Tier B)
- [Contradiction documented in ...]
```

---

## Directory Structure

### For Software Projects

```
your-project/
├── architecture/
│   └── decisions/
│       ├── ADR-001-database-selection.md
│       ├── ADR-002-api-authentication.md
│       └── ADR-003-deployment-strategy.md
└── .claude/
    └── CLAUDE.md (references ADR directory)
```

### For Research Projects

```
research-project/
├── decisions/
│   ├── ADR-001-hypothesis-testing-methodology.md
│   ├── ADR-002-evidence-tier-thresholds.md
│   └── ADR-003-publication-venue-selection.md
├── contradictions/
│   ├── iceberg-vs-delta-lake.md (links to ADR-001)
│   └── centralized-vs-federated-siem.md (links to ADR-002)
└── .claude/
    └── CLAUDE.md (references both directories)
```

### For Hybrid Projects

```
hybrid-project/
├── .claude/
│   ├── decisions/
│   │   ├── ADR-001-skill-infrastructure.md
│   │   ├── ADR-002-progressive-disclosure-adoption.md
│   │   └── ADR-003-evidence-tier-framework.md
│   └── CLAUDE.md
└── README.md (links to key ADRs)
```

---

## ADR Lifecycle

### 1. Proposed
Decision is under consideration. ADR drafted to frame the discussion.

### 2. Accepted
Decision has been made. ADR is finalized and becomes immutable.

### 3. Deprecated
Decision is no longer relevant but not replaced (e.g., feature removed).

### 4. Superseded
A new decision replaces this one. Link to the superseding ADR.

---

## Integration with Claude Code

### CLAUDE.md Reference

```markdown
## Decision Making

Key architectural decisions documented in:
- `architecture/decisions/` - Software architecture ADRs
- `decisions/` - Research methodology ADRs
- `.claude/decisions/` - Claude infrastructure ADRs

See [ADR-001](architecture/decisions/ADR-001-database-selection.md) for database choice rationale.
```

### Contradiction Resolution

ADRs are excellent for resolving documented contradictions:

```markdown
## Context

Documented contradiction: "Iceberg vs Delta Lake for security data lakes"
- Some experts prefer Iceberg (open source, vendor neutral)
- Others prefer Delta Lake (mature, Databricks ecosystem)

Sources:
- Ryan Blue (Iceberg creator): Tier 1 evidence for Iceberg
- Databricks team: Tier 1 evidence for Delta Lake

## Decision

We chose **Apache Iceberg** for our security data lake.

## Rationale

Despite Delta Lake's maturity, we prioritized:
1. Vendor neutrality (no lock-in)
2. Open governance (Apache Foundation)
3. Future flexibility (multiple compute engines)

Evidence:
- Tier 1: Netflix production deployment (500M events/day)
- Tier 2: Performance benchmark (IEEE 2024)
- Tier 3: Industry consensus at Data+AI Summit

We accept the trade-off:
- Less mature ecosystem than Delta Lake
- Fewer Databricks-specific optimizations
```

### Skill Integration

Skills can reference ADRs:

```markdown
## WORKFLOW ROUTING (SYSTEM PROMPT)

"Why did we choose [technology]?" → `decisions/ADR-XXX-[technology].md` → Decision rationale
"What alternatives were considered?" → `decisions/ADR-XXX-[technology].md` → Options section
"What are the trade-offs?" → `decisions/ADR-XXX-[technology].md` → Consequences section
```

---

## Best Practices

### Numbering

Use sequential numbering with leading zeros:
- `ADR-001`, `ADR-002`, ... `ADR-010`, `ADR-011`
- Maintains sort order in file systems

### Titles

Use verb phrases describing the decision:
- ✅ "Use Iceberg for security data lake"
- ✅ "Adopt progressive disclosure for skills"
- ❌ "Database selection" (too vague)
- ❌ "Iceberg" (what about it?)

### Evidence Attribution

Always cite evidence tier:
```markdown
**Claim**: DuckDB outperforms Spark for sub-1GB datasets

**Evidence**:
- Tier 1: Production deployment (2s vs 45s query time)
- Tier 2: VLDB 2024 benchmark study
- Tier 3: Creator confirms architecture advantage
```

### Keep ADRs Focused

One decision per ADR. If you have multiple related decisions, create multiple linked ADRs.

### Link Related ADRs

```markdown
## Related Decisions
- Supersedes: [ADR-003](ADR-003-old-database-choice.md)
- Builds on: [ADR-001](ADR-001-data-architecture.md)
- Conflicts with: None
```

---

## Common Use Cases

### 1. Tool Selection

**Example**: ADR-001: Adopt DuckDB for Local Security Analytics

### 2. Architecture Patterns

**Example**: ADR-002: Use Progressive Disclosure for Claude Skills

### 3. Research Methodology

**Example**: ADR-003: Adopt Evidence Tier 1-5 Classification

### 4. Process Decisions

**Example**: ADR-004: Require Peer Review for All Hypotheses

### 5. Contradiction Resolution

**Example**: ADR-005: Resolve Centralized vs Federated SIEM Debate

---

## Integration with Other Patterns

### With Confidence Scoring

ADRs should document confidence level of the decision:

```markdown
**Confidence**: MEDIUM (65%)

**Rationale**:
- Strong Tier 1-2 evidence for performance
- Limited production validation at our scale
- Need 6-month review to increase confidence to HIGH
```

### With Evidence Tiers

All ADR claims should reference evidence tiers:

```markdown
**Decision**: Use Apache Iceberg

**Evidence**:
- Tier A: Apache Iceberg official documentation
- Tier 1: Netflix production deployment (500M events/day)
- Tier 2: IEEE benchmark study (2024)
- Tier 3: Industry expert consensus
```

### With Documentation Maintenance

ADRs complement the ARCHITECTURE-PLAN-INDEX trio:

| Document | Purpose | Relation to ADRs |
|----------|---------|------------------|
| **ARCHITECTURE.md** | Current state | References key ADRs |
| **PLAN.md** | Future work | May trigger new ADRs |
| **ADRs** | Decision history | Explains why ARCHITECTURE exists |

---

## Anti-Patterns

**DON'T**:
- ❌ Document obvious or trivial decisions
- ❌ Edit ADRs after acceptance (create new superseding ADR)
- ❌ Write ADRs without evidence tier attribution
- ❌ Skip alternatives section (shows you considered options)
- ❌ Ignore contradictions (address them explicitly)

**DO**:
- ✅ Write ADRs for non-obvious decisions
- ✅ Keep ADRs immutable (historical record)
- ✅ Cite evidence tiers for all claims
- ✅ Document alternatives and why they were rejected
- ✅ Link contradictions to ADRs that resolved them

---

## Tools and Automation

### ADR Management with Claude

Create a skill or slash command:

```markdown
---
name: adr-creator
description: Create new Architecture Decision Record with proper structure and evidence validation
---

# ADR Creator

Helps create well-structured ADRs with:
- Evidence tier validation
- Contradiction checking
- Confidence assessment
- Proper formatting
```

### ADR Index

Maintain an index in ARCHITECTURE.md:

```markdown
## Key Decisions

- [ADR-001: Database Selection](decisions/ADR-001-database-selection.md) - Apache Iceberg (2024-Q3)
- [ADR-002: Authentication](decisions/ADR-002-api-authentication.md) - OAuth 2.0 (2024-Q4)
- [ADR-003: Deployment](decisions/ADR-003-deployment-strategy.md) - Kubernetes (2024-Q4)
```

---

## Related Patterns

- [Evidence Tiers](./evidence-tiers.md) - Classify evidence supporting decisions
- [Confidence Scoring](./confidence-scoring.md) - Assess decision confidence
- [Documentation Maintenance](./documentation-maintenance.md) - ARCHITECTURE-PLAN-INDEX trio

---

## Further Reading

**Tier A Sources**:
- Michael Nygard: "Documenting Architecture Decisions" (Original ADR concept)
- Thoughtworks Technology Radar: ADR adoption patterns

**Tier B Sources**:
- GitHub ADR organization: Templates and examples
- Production validation in 100+ software projects

**Evidence Tier**: A (Original source from Michael Nygard) + B (Production validation)

---

**Version**: 1.0
**Created**: 2025-12-13
**Source**: Adapted from software engineering practice, validated in research contexts
**Applies to**: Software projects, research projects, enterprise governance

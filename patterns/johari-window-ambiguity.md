---
version-requirements:
  claude-code: "v2.0.0+"
version-last-verified: "2026-02-27"
status: "PRODUCTION"
last-verified: "2026-02-16"
notes: "Methodology pattern - implements Johari Window framework for ambiguity detection"
---

# Johari Window Pattern for Ambiguity Surfacing

**Source**: [skribblez2718/caii](https://github.com/skribblez2718/caii) (CAII - Cognitive Agent Infrastructure Implementation)
**Evidence Tier**: B (Production implementation, documented methodology)

## Overview

The Johari Window pattern surfaces hidden assumptions and unknowns before task execution. By explicitly mapping what both parties know and don't know, it reduces the "we don't know what we don't know" problem that causes LLMs to "go off and do something you did not intend."

**SDD Phase**: Specify (critical for complex requirements)

> "Even well-written and well-structured prompts have ambiguity, which stems from the fact 'we don't know what we don't know.'"
> — CAII Documentation

---

## The Four Quadrants

The Johari Window organizes knowledge into four quadrants:

```
                      Known to Claude
                    YES            NO
                ┌─────────────┬─────────────┐
            YES │   ARENA     │   HIDDEN    │
Known to        │  (OPEN)     │             │
User            │             │             │
                ├─────────────┼─────────────┤
            NO  │ BLIND SPOT  │  UNKNOWN    │
                │             │             │
                │             │             │
                └─────────────┴─────────────┘
```

### Quadrant Details

| Quadrant | Description | Example |
|----------|-------------|---------|
| **Arena (Open)** | Known to both user and Claude | "We're building a REST API in Node.js" |
| **Hidden** | User knows, Claude doesn't | "Our team prefers functional patterns over OOP" |
| **Blind Spot** | Claude knows, user doesn't | "This pattern has a known security vulnerability" |
| **Unknown** | Neither party knows | "How will this scale under production load?" |

---

## The SAAE Protocol

SAAE (Share-Ask-Acknowledge-Explore) is a four-phase protocol for surfacing unknowns:

### Phase 1: SHARE

**Purpose**: Present what you already know about the task

```markdown
## What I Know (User SHARES)

- Building user authentication system
- Using JWT tokens
- Need to support OAuth2 providers
- Target: 10,000 concurrent users
```

**Claude also SHARES**: Technical knowledge, patterns, considerations

### Phase 2: ASK

**Purpose**: Solicit the other party's perspective on the problem space

```markdown
## Questions (ASK each other)

### Claude asks user:
- What token expiry duration do you prefer?
- Do you need refresh token rotation?
- Which OAuth2 providers specifically?
- What's your Redis infrastructure?

### User asks Claude:
- What security considerations am I missing?
- What's the standard approach for token storage?
- How do others handle multi-device sessions?
```

### Phase 3: ACKNOWLEDGE

**Purpose**: Recognize gaps between understandings

```markdown
## Acknowledged Gaps

### User acknowledges:
- Didn't consider refresh token rotation (Claude's blind spot → now Arena)
- Wasn't aware of token binding best practices

### Claude acknowledges:
- Now understands team prefers functional patterns (Hidden → now Arena)
- Clarified the specific OAuth2 providers needed
```

### Phase 4: EXPLORE

**Purpose**: Investigate unknowns systematically before execution

```markdown
## Exploring Unknowns

Neither party knows:
- [ ] How will this perform under 10K concurrent auth requests?
- [ ] What's the failure mode if Redis is unavailable?
- [ ] How will token rotation interact with mobile offline mode?

Investigation plan:
1. Benchmark current auth under load
2. Design Redis failover strategy
3. Research offline-first auth patterns
```

---

## When to Use This Pattern

### Strong Triggers

| Scenario | Why Johari Window Helps |
|----------|------------------------|
| **Complex implementations** (3+ files) | Many implicit assumptions need surfacing |
| **Architecture decisions** | Trade-offs require shared understanding |
| **Expert interviews** | Maximize knowledge transfer |
| **Multi-step workflows** | Dependencies create hidden assumptions |
| **Requirements unclear** | "I'll know it when I see it" situations |

### Weak Triggers (Skip It)

| Scenario | Why Skip |
|----------|----------|
| **Simple bug fixes** | Problem already well-defined |
| **Single-file changes** | Limited assumption space |
| **Repeating established patterns** | Prior work defined expectations |
| **Time-critical tasks** | Overhead exceeds benefit |

---

## Implementation in Claude Code

### Pre-Task Clarification Prompt

```markdown
## Johari Window Clarification

Before implementing, let's surface assumptions:

### ARENA (What we both know)
[List shared understanding]

### HIDDEN (What you know that I might not)
Please share:
- Team conventions or preferences
- Prior decisions that constrain this work
- Context I wouldn't have from the codebase

### BLIND SPOT (What I know that you might not)
I should mention:
- [Technical considerations]
- [Potential issues]
- [Alternative approaches]

### UNKNOWN (Neither of us knows yet)
We should investigate:
- [Uncertainties]
- [Risks]
- [Dependencies]

Before I proceed, are there Hidden items to surface?
```

### Skill Implementation

For repeatable use, create a `johari-window-clarifier` skill:

```yaml
---
name: johari-window-clarifier
description: Surface unknowns before complex task execution
trigger: Complex implementations, architecture decisions, unclear requirements
---

# Johari Window Clarifier

## When Triggered
Apply this methodology when:
- Task involves 3+ files
- Requirements have implicit assumptions
- Architecture decisions needed
- "I'll know it when I see it" situations

## Protocol

### Step 1: Map the Quadrants
Explicitly state what falls into each quadrant based on:
- User's prompt
- Codebase context
- Technical knowledge

### Step 2: Surface Hidden Information
Ask targeted questions to move items from Hidden → Arena:
- Team preferences?
- Prior constraints?
- Unstated requirements?

### Step 3: Share Blind Spots
Proactively share technical considerations the user might not know:
- Security implications
- Performance considerations
- Maintenance burden
- Alternative approaches

### Step 4: Identify Unknowns
Flag uncertainties that need investigation:
- Scaling behavior
- Edge cases
- Integration points
- Failure modes

### Step 5: Confirm Understanding
Summarize the expanded Arena before proceeding.
```

---

## Anti-Patterns

### ❌ Proceeding Without Surfacing Assumptions

**Problem**: Starting implementation with implicit assumptions
**Symptom**: "That's not what I meant" after significant work
**Solution**: Always map quadrants for complex tasks

### ❌ Asking Too Many Questions

**Problem**: Analysis paralysis, endless clarification
**Symptom**: User frustrated by question volume
**Solution**: Focus on high-impact unknowns; proceed with reasonable defaults

### ❌ Ignoring Blind Spots

**Problem**: Not sharing technical knowledge proactively
**Symptom**: User makes uninformed decisions
**Solution**: Always share relevant Blind Spot information

### ❌ Treating Unknowns as Blockers

**Problem**: Refusing to proceed until all unknowns resolved
**Symptom**: Progress stalls on theoretical concerns
**Solution**: Note unknowns, proceed with documented assumptions

---

## Integration with Other Patterns

| Pattern | Integration |
|---------|-------------|
| **GSD Orchestration** | SAAE during Discuss phase |
| **Spec-Driven Development** | Johari informs Specify phase |
| **Planning-First** | Surface unknowns before creating plan |
| **Context Engineering** | Hidden items become explicit context |

---

## Example: Database Migration Task

### Initial Request

> "Migrate our users table from PostgreSQL to DynamoDB"

### SAAE Application

**SHARE (Arena)**:
- Source: PostgreSQL users table
- Target: DynamoDB
- Goal: Migration with minimal downtime

**ASK (Surface Hidden)**:

Claude asks:
- What's the current row count and growth rate?
- Are there foreign key dependencies?
- What's the acceptable downtime window?
- Do you need the migration to be reversible?

User reveals (Hidden → Arena):
- 2 million rows, growing 50K/month
- FK constraints from orders and sessions tables
- Zero downtime required (24/7 production)
- Must be reversible for 30 days

**ACKNOWLEDGE (Blind Spots)**:

Claude shares:
- DynamoDB has no native FK support—need application-level enforcement
- Zero-downtime requires dual-write strategy
- DynamoDB pricing model differs significantly—estimated cost impact
- Pagination differs—existing queries need rewrite

**EXPLORE (Unknowns)**:
- Neither knows: Performance comparison for current query patterns
- Neither knows: How existing ORM handles DynamoDB
- Investigation needed: Benchmark representative queries

### Result

Instead of starting migration immediately, both parties now understand:
- Scope is larger than initially apparent (FK handling, query rewrites)
- Cost implications need evaluation
- Dual-write strategy needed for zero downtime
- 30-day reversibility affects architecture

---

## Quick Reference

### Trigger Questions

Ask yourself:
1. Could I be making assumptions the user doesn't share?
2. Does the user likely have context I'm missing?
3. Are there technical implications the user might not know?
4. Are there uncertainties that could derail this work?

If yes to any, apply Johari Window.

### One-Line Quadrant Prompts

- **Arena**: "Here's what I understand: [summary]. Is this accurate?"
- **Hidden**: "What context should I know that might not be in the codebase?"
- **Blind Spot**: "I should mention [technical consideration] before we proceed."
- **Unknown**: "We should investigate [uncertainty] before committing to this approach."

---

## Related Patterns

- [GSD Orchestration](./gsd-orchestration.md) - SAAE during Discuss phase
- [Spec-Driven Development](./spec-driven-development.md) - Requirements clarification
- [Planning-First Development](./planning-first-development.md) - Unknown surfacing before implementation
- [Cognitive Agent Infrastructure](./cognitive-agent-infrastructure.md) - Full CAII methodology

---

## Sources

**Primary (Tier B)**:
- [skribblez2718/caii](https://github.com/skribblez2718/caii) - CAII implementation and documentation

**Background**:
- Johari Window psychological model (Luft & Ingham, 1955)

*Last updated: January 2026*

---
version-requirements:
  claude-code: "v2.0.0+"
measurement-claims:
  - claim: "Skills are 50% cheaper than MCP ($10.27 vs $20.78 per task)"
    source: "Tenzir production data"
    date: "2026-01-15"
    revalidate: "2027-01-15"
  - claim: "MCP is 38% faster than Skills (6.2 min vs 8.6 min)"
    source: "Tenzir production data"
    date: "2026-01-15"
    revalidate: "2027-01-15"
  - claim: "Skills use 55% less cached tokens (4.0M vs 8.8M)"
    source: "Tenzir production data"
    date: "2026-01-15"
    revalidate: "2027-01-15"
status: "PRODUCTION"
last-verified: "2026-02-16"
---

# MCP vs Skills Economics

**Source**: [Tenzir Blog - "We Did MCP Wrong"](https://tenzir.com/blog/we-did-mcp-wrong) (Matthias Vallentin, January 2026)
**Evidence Tier**: B (Production data from active project)

## Overview

MCP (Model Context Protocol) and Skills represent two different approaches to extending Claude Code's capabilities. Production data shows **Skills can be 50% cheaper** than equivalent MCP implementations, though MCP may be faster. The choice depends on environment constraints and cost sensitivity.

**SDD Phase**: Cross-phase (architecture decision affecting all phases)

> "When you're paying per token, 'slower but half price' wins."
> — Matthias Vallentin, Tenzir

---

## The Production Data

Tenzir compared identical workflows delivered via MCP server vs Claude Code Skills:

| Metric | MCP | Skills | Winner |
|--------|-----|--------|--------|
| **Duration** | 6.2 min | 8.6 min | MCP (38% faster) |
| **Tool calls** | 61 | 52 | Skills (15% fewer) |
| **Cost** | $20.78 | $10.27 | **Skills (50% cheaper)** |
| **Cached tokens** | 8.8M | 4.0M | Skills (55% less) |

**Key Finding**: The Skills approach produced working output at half the cost of MCP.

---

## Why the Cost Difference?

### MCP Approach

```
MCP Server
├── Custom tools: run_pipeline, docs_read, run_test
├── Purpose-built infrastructure
├── Each tool call = interaction with custom server
└── 61 tool calls total
```

**Characteristics**:
- Heavy reliance on custom-built tools
- Each tool call involves MCP server round-trip
- Infrastructure must be maintained
- Optimized for specific domain (TQL in Tenzir's case)

### Skills Approach

```
Skills
├── Generic tools: Bash, Write, Read
├── Orchestration: Task, Skill, AskUserQuestion
├── Leverages Claude's native capabilities
└── 52 tool calls total
```

**Characteristics**:
- Uses mostly generic/native Claude Code tools
- Instructions loaded as context, not infrastructure
- No custom server to maintain
- Portable across projects

---

## The Philosophy Shift

### Before: Force-Feed Structured Context

```
┌─────────────────────────────────────────┐
│         MCP SERVER APPROACH             │
├─────────────────────────────────────────┤
│                                         │
│  Client ──► MCP Server ──► Tools        │
│               │                         │
│               ▼                         │
│    ┌──────────────────────┐            │
│    │ Custom infrastructure │            │
│    │ run_pipeline          │            │
│    │ docs_read             │            │
│    │ run_test              │            │
│    └──────────────────────┘            │
│                                         │
│  Philosophy: Build tools that          │
│  structure context FOR the AI          │
│                                         │
└─────────────────────────────────────────┘
```

### After: Provide Capabilities + Documentation

```
┌─────────────────────────────────────────┐
│          SKILLS APPROACH                │
├─────────────────────────────────────────┤
│                                         │
│  Claude ──► Native Tools + Skill Docs   │
│               │                         │
│               ▼                         │
│    ┌──────────────────────┐            │
│    │ Generic capabilities  │            │
│    │ Bash                  │            │
│    │ Read/Write            │            │
│    │ Task (orchestration)  │            │
│    └──────────────────────┘            │
│                                         │
│  Philosophy: Teach the AI HOW to use   │
│  existing capabilities effectively     │
│                                         │
└─────────────────────────────────────────┘
```

**Key Insight**: Instead of building custom tools that structure context, teach Claude how to use generic tools effectively via skill documentation.

---

## Decision Framework

### Use MCP When

| Scenario | Why MCP |
|----------|---------|
| **Sandboxed execution required** | MCP servers can run in isolated environments |
| **Deterministic validation needed** | Custom tools can enforce exact behavior |
| **Local/constrained models** | Models need more structured assistance |
| **Pipeline orchestration** | MCP excels at stateful multi-step workflows |
| **Persistent connections** | WebSocket-based MCP maintains state |
| **Speed critical** | 38% faster execution in benchmarks |

### Use Skills When

| Scenario | Why Skills |
|----------|------------|
| **Cost-sensitive workflows** | 50% cheaper per task |
| **Cloud/frontier models** | Models capable enough to use generic tools |
| **Portable instructions** | Skills work across projects without infrastructure |
| **Rapid iteration** | No server deployment, just markdown |
| **Internet-connected workflows** | Can leverage external resources |
| **Maintenance burden concern** | No custom infrastructure to maintain |

### The Environment Principle

> "Tools should match the environment."
> — Tenzir Team

| Environment | Recommendation |
|-------------|----------------|
| **Claude Marketplace + frontier models + internet** | Minimal Skills |
| **Local models + constrained environment** | Rich MCP servers |
| **Mixed environment** | Hybrid approach |

---

## Hybrid Architecture

For teams with both needs, consider a hybrid approach:

```
┌─────────────────────────────────────────────────────────┐
│                 HYBRID ARCHITECTURE                     │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌─────────────────┐      ┌─────────────────┐         │
│  │   MCP Layer     │      │  Skills Layer   │         │
│  ├─────────────────┤      ├─────────────────┤         │
│  │ Sandboxed exec  │      │ Workflow docs   │         │
│  │ Validation      │      │ Best practices  │         │
│  │ State mgmt      │      │ Domain knowledge│         │
│  └────────┬────────┘      └────────┬────────┘         │
│           │                        │                   │
│           └────────────┬───────────┘                   │
│                        ▼                               │
│              ┌─────────────────┐                       │
│              │  Claude Code    │                       │
│              │  Orchestration  │                       │
│              └─────────────────┘                       │
│                                                         │
│  MCP for: Execution, validation, state                 │
│  Skills for: Knowledge, workflows, practices           │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

**Key Principle**: Use MCP for what it's good at (execution infrastructure), Skills for what they're good at (knowledge transfer).

---

## Cost Optimization Strategies

### 1. Audit Tool Call Patterns

Before optimizing, understand current usage:

```markdown
## Tool Call Audit Questions

1. How many tool calls per typical task?
2. What percentage are custom MCP tools vs native tools?
3. Are custom tools doing things Claude could do natively?
4. What's the token cost breakdown (input vs output)?
```

### 2. Migrate Knowledge to Skills

Move domain knowledge from MCP tool implementations to skill documentation:

| Before (MCP) | After (Skills) |
|--------------|----------------|
| `docs_read` tool with embedded docs | Skill with documentation links |
| `run_test` with hardcoded patterns | Skill explaining test conventions |
| `validate_syntax` tool | Skill with syntax guidelines |

### 3. Reserve MCP for Execution

Keep MCP for things that truly need custom execution:

- Sandboxed code execution
- External API integrations requiring authentication
- Stateful operations across requests
- Operations Claude genuinely cannot do natively

### 4. Measure and Iterate

Track cost per task type and adjust:

```markdown
## Cost Tracking Template

| Task Type | MCP Cost | Skills Cost | Approach Used |
|-----------|----------|-------------|---------------|
| TQL dev   | $20.78   | $10.27      | Skills ✓      |
| Code review | $X     | $Y          | ?             |
| Deploy    | $X       | N/A         | MCP (required)|
```

---

## Anti-Patterns

### ❌ MCP for Everything

**Problem**: Routing all operations through MCP "because we built it"
**Symptom**: 2x cost, maintenance burden, slower iteration
**Solution**: Evaluate each workflow—many don't need custom tools

### ❌ Skills Without Structure

**Problem**: Dumping raw documentation into skills without organization
**Symptom**: Claude overwhelmed, inconsistent results
**Solution**: Structure skills with clear sections, examples, when-to-use guidance

### ❌ Ignoring Environment Context

**Problem**: Using same approach for local and cloud deployments
**Symptom**: Either over-engineering (cloud) or under-supporting (local)
**Solution**: Match tool richness to model capability and environment constraints

### ❌ Cost Blindness

**Problem**: Not measuring actual costs per approach
**Symptom**: Surprised by API bills, no optimization data
**Solution**: Instrument and track cost per task type

---

## Migration Path: MCP to Skills

If you have existing MCP infrastructure and want to reduce costs:

### Step 1: Inventory Current Tools

List all MCP tools and categorize:
- **Execution tools**: Actually run code, make API calls → Keep in MCP
- **Knowledge tools**: Return documentation, explain patterns → Migrate to Skills
- **Validation tools**: Check syntax, formats → Evaluate case-by-case

### Step 2: Create Equivalent Skills

For each knowledge tool:
1. Extract the documentation/knowledge it provides
2. Create a skill with that knowledge as context
3. Add usage examples and when-to-use guidance

### Step 3: Test Side-by-Side

Run identical tasks through both approaches:
- Measure cost
- Measure quality
- Measure duration
- Decide per-workflow

### Step 4: Gradual Transition

Don't rip out MCP overnight:
1. Start with lowest-risk workflows
2. Monitor for quality regressions
3. Expand as confidence grows

---

## Integration with Other Patterns

| Pattern | Integration |
|---------|-------------|
| **Progressive Disclosure** | Skills load only relevant context (token efficiency) |
| **GSD Orchestration** | Skills for knowledge, MCP for execution validation |
| **Context Engineering** | Skills = deterministic context, MCP = tool context |
| **MCP Patterns** | This pattern complements MCP security/architecture guidance |

---

## Summary

| Factor | MCP | Skills |
|--------|-----|--------|
| **Speed** | ✅ Faster (38%) | Slower |
| **Cost** | Expensive (2x) | ✅ Cheaper (50%) |
| **Infrastructure** | Requires servers | ✅ Just markdown |
| **Portability** | Project-specific | ✅ Cross-project |
| **Maintenance** | High | ✅ Low |
| **Capability** | ✅ Execution + Knowledge | Knowledge only |

**Rule of Thumb**: Default to Skills for knowledge transfer; reserve MCP for execution that Claude genuinely cannot do natively.

---

## Related Patterns

- [MCP Patterns](./mcp-patterns.md) - MCP security and architecture patterns
- [Progressive Disclosure](./progressive-disclosure.md) - Token-efficient skill loading
- [Skills Domain Knowledge](./skills-domain-knowledge.md) - Embedding expertise in skills
- [Context Engineering](./context-engineering.md) - Managing context effectively

---

## Sources

**Primary (Tier B)**:
- [Tenzir Blog - "We Did MCP Wrong"](https://tenzir.com/blog/we-did-mcp-wrong) - Matthias Vallentin, January 2026

**Supporting**:
- Tenzir Claude Marketplace plugins (10+ production plugins)
- Internal cost analysis across workflows

*Last updated: January 2026*

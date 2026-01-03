# Subagent Orchestration Patterns

**Source**: [Claude Code Documentation - Sub-agents](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
**Evidence Tier**: A (Primary vendor documentation)

## Overview

Subagents are specialized Claude instances spawned by a parent agent to handle specific tasks with isolated context. They enable parallel execution, context isolation, and specialized behavior without consuming the parent's context window.

**SDD Phase**: Tasks + Implement (execution layer optimization)

---

## When to Use Subagents

### Good Fits

| Scenario | Why Subagents Help |
|----------|-------------------|
| **Parallel research** | Multiple searches run simultaneously |
| **Large codebase exploration** | Each subagent has fresh context window |
| **Non-destructive analysis** | Read-only operations safe to parallelize |
| **Specialized methodologies** | Different subagent types for different tasks |
| **Long-running analysis** | Prevents context exhaustion in parent |

### Poor Fits

| Scenario | Why Not |
|----------|---------|
| **Sequential dependencies** | Can't parallelize if B depends on A |
| **Destructive operations** | Write conflicts, race conditions |
| **Simple tasks** | Subagent overhead exceeds benefit |
| **Tight coordination** | Parent can't see subagent intermediate work |

---

## Claude Code Subagent Types

Claude Code provides specialized subagent types via the Task tool:

| Type | Purpose | Best For |
|------|---------|----------|
| `Explore` | Fast codebase exploration | Finding files, searching code, answering architecture questions |
| `Plan` | Software architect planning | Implementation strategy, identifying critical files, trade-offs |
| `general-purpose` | Multi-step research | Complex questions, code search, autonomous task execution |
| `claude-code-guide` | Documentation lookup | Questions about Claude Code features, hooks, MCP, skills |

### Usage Pattern

```
Use Task tool with:
- subagent_type: "Explore"
- prompt: "Find all authentication-related files and explain how login works"
- description: "Explore auth flow"
```

---

## Orchestration Patterns

### 1. Parallel Research Pattern

**Use Case**: Gathering information from multiple sources simultaneously

```
Parent Agent:
├── [Subagent 1: Explore] "Find all API endpoints"
├── [Subagent 2: Explore] "Find database schema files"
└── [Subagent 3: Explore] "Find authentication middleware"

Result: All three search in parallel, parent synthesizes results
```

**Benefits**:
- 3x faster than sequential exploration
- Each subagent gets full context window
- Parent context preserved for synthesis

### 2. Specialist Delegation Pattern

**Use Case**: Applying different methodologies to same problem

```
Parent Agent (receives code review request):
├── [Subagent: Plan] "Analyze architecture implications"
├── [Subagent: general-purpose] "Check for security vulnerabilities"
└── [Subagent: Explore] "Find similar patterns in codebase"

Result: Comprehensive review from multiple perspectives
```

### 3. Context Window Recovery Pattern

**Use Case**: When parent context is near exhaustion

```
Parent Agent (low context):
└── [Subagent: general-purpose]
    "Continue implementing feature X. Here's the current state: [summary]"

Result: Fresh context window continues the work
```

**Key**: Summarize essential state in the subagent prompt.

### 4. Verification Isolation Pattern

**Use Case**: Independent verification of implementation

```
Parent Agent (after implementing):
└── [Subagent: Explore]
    "Verify the auth implementation matches requirements in specs/auth.md"

Result: Independent verification without implementation bias
```

---

## Best Practices

### Prompt Design

**Do**:
- Provide complete context in the prompt (subagent doesn't see conversation history)
- Specify expected output format
- Include relevant file paths or search starting points
- Set clear success criteria

**Don't**:
- Reference "the code we discussed" (subagent has no history)
- Expect subagent to ask clarifying questions
- Assume subagent knows project conventions

### Parallelization

**Safe to parallelize**:
- Read operations (Glob, Grep, Read)
- Independent research tasks
- Analysis that doesn't modify state

**Don't parallelize**:
- File writes to same location
- Git operations
- Operations with ordering dependencies

### Result Handling

Subagents return a single final message. Structure your prompt to ensure:
- Key findings are explicitly stated
- Relevant file paths are included
- Uncertainties are flagged
- Summary is actionable

---

## Integration with SDD Phases

| SDD Phase | Subagent Application |
|-----------|---------------------|
| **Specify** | Parallel research on requirements, competitive analysis |
| **Plan** | Architecture exploration, dependency analysis |
| **Tasks** | Complexity estimation, prerequisite identification |
| **Implement** | Code search, verification, parallel non-conflicting changes |

---

## Failure Modes

### 1. Over-Delegation

**Symptom**: Every small task spawns a subagent
**Impact**: Overhead exceeds benefit, fragmented workflow
**Fix**: Use subagents for tasks taking 30+ seconds or needing fresh context

### 2. Insufficient Context

**Symptom**: Subagent returns irrelevant results
**Impact**: Wasted tokens, repeated work
**Fix**: Include project context, file locations, success criteria in prompt

### 3. Parallel Write Conflicts

**Symptom**: Subagents overwrite each other's changes
**Impact**: Lost work, corrupted files
**Fix**: Only parallelize read operations; sequence writes

### 4. Result Integration Gaps

**Symptom**: Parent doesn't synthesize subagent findings
**Impact**: Fragmented understanding, missed connections
**Fix**: Always synthesize results after parallel subagent completion

---

## Pattern 5: Diversity Sampling (Self-Evolution)

**Use Case**: Exploring multiple solution approaches for the same problem

Unlike traditional parallel research (different tasks), diversity sampling runs the **same task** with different approaches to explore the solution space.

```
Traditional Parallel:              Diversity Sampling:
[Subagent 1: Find APIs]           [Candidate 1: Conservative analysis]
[Subagent 2: Find schemas]   vs   [Candidate 2: Balanced analysis]
[Subagent 3: Find auth]           [Candidate 3: Creative analysis]
      ↓                                  ↓
Different information             Different perspectives on SAME problem
```

### Implementation

Spawn 3 candidates with different analytical approaches:

```markdown
## Diversity Sampling Setup

Launch 3 subagents IN PARALLEL (single message, multiple Task calls):

[Task 1: Conservative Candidate]
- subagent_type: "general-purpose"
- prompt: "Analyze [TOPIC] with CONSERVATIVE approach:
  Focus on established patterns, proven solutions, risk mitigation"

[Task 2: Balanced Candidate]
- subagent_type: "general-purpose"
- prompt: "Analyze [TOPIC] with BALANCED approach:
  Consider trade-offs, apply best practices, acknowledge alternatives"

[Task 3: Creative Candidate]
- subagent_type: "general-purpose"
- prompt: "Analyze [TOPIC] with CREATIVE approach:
  Explore novel angles, challenge assumptions, consider innovations"
```

### Crossover Synthesis

After candidates complete, synthesize:
1. Identify unique strengths of each approach
2. Note where candidates agree (high confidence)
3. Reconcile conflicts (favor stronger evidence)
4. Merge into superior combined output

**Related**: See [Recursive Evolution](./recursive-evolution.md) for full Self-Evolution Algorithm with iterative refinement.

---

## Application Examples

### Research Project

```markdown
## Subagent Setup for Research

When researching a topic, spawn parallel subagents:
1. [Explore] "Find primary sources on topic X"
2. [Explore] "Find counter-arguments to hypothesis Y"
3. [general-purpose] "Search for recent publications (2024-2025)"

Synthesize findings in parent before drawing conclusions.
```

### Complex Feature Implementation

```markdown
## Subagent Setup for Features

Before implementing a complex feature:
1. [Plan] "Create implementation plan for feature X"
2. [Explore] "Find all files that will need modification"
3. [Explore] "Find existing patterns for similar features"

Then implement sequentially in parent with full context.
```

---

## Related Patterns

- [Recursive Evolution](./recursive-evolution.md) - Full Self-Evolution Algorithm with iterative refinement
- [Long-Running Agent](./long-running-agent.md) - External artifacts for context bridging
- [Progressive Disclosure](./progressive-disclosure.md) - Token-efficient methodology loading
- [Context Engineering](./context-engineering.md) - Managing context effectively

---

## Sources

- [Claude Code Sub-agents Documentation](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
- [Anthropic Engineering Blog: Effective Harnesses](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)

*Last updated: January 2026*

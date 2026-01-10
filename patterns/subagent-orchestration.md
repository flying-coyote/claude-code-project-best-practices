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

### 5. Background Agent Pattern (v2.0.60+)

**Use Case**: Long-running tasks that don't block the main conversation

```
Parent Agent:
├── [Background Subagent] "Run full test suite and report failures"
│   └── Runs asynchronously, notifies on completion
└── Continue working on other tasks while tests run
```

**Implementation**:
```
Task tool with:
- subagent_type: "general-purpose"
- run_in_background: true
- prompt: "Run the full test suite, analyze any failures, suggest fixes"
```

**Benefits**:
- Main conversation continues unblocked
- Long operations (tests, builds, analysis) run in parallel
- Results available when ready via TaskOutput tool

**When to use**:
- Test suite execution (5+ minutes)
- Large codebase analysis
- Build processes
- Any task where waiting blocks productivity

### 6. Subagent Resumption Pattern (v2.1.0+)

**Use Case**: Continuing interrupted subagent work

Claude can now pause and resume subagents, preserving their context:

```
Initial subagent work:
└── [Subagent: Plan] "Design auth architecture"
    └── Returns partial plan + agent_id: "abc123"

Later resumption:
└── [Task with resume: "abc123"]
    "Continue the auth design, focusing on token refresh"
    └── Subagent continues with full previous context
```

**Implementation**:
```
Task tool with:
- resume: "abc123"  # Agent ID from previous invocation
- prompt: "Continue where you left off, now focusing on X"
```

**When to use**:
- Complex multi-session planning
- Research that spans multiple interactions
- Iterative design refinement
- When new information requires revisiting previous analysis

### 7. Real-Time Steering Pattern (v2.1.0+)

**Use Case**: Redirecting Claude mid-task without starting over

You can send messages while Claude is working to adjust direction:

```
User: "Analyze the authentication system"
[Claude starts analyzing...]
User (mid-task): "Focus specifically on the OAuth flow, skip JWT"
[Claude adjusts without losing progress]
```

**Benefits**:
- Course-correct without restarting
- Refine scope as understanding develops
- Efficient for exploratory tasks

**Best Practices**:
- Use for clarification, not complete pivots
- Keep steering messages concise
- Allow current tool operation to complete before steering takes effect

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

## Pattern 6: Worktree Isolation

**Use Case**: Safe parallel execution of multiple agents on the same codebase

The core insight from multi-agent orchestration tools: **"Safety enables autonomy"** — structural isolation through git worktrees allows agents to work autonomously because worst-case scenarios are contained.

### Architecture

```
Main Branch (Protected)
    │
    ├── Worktree 1: Agent A working on Feature X
    │       └── Isolated directory, full git history
    │
    ├── Worktree 2: Agent B working on Feature Y
    │       └── Isolated directory, full git history
    │
    └── Worktree 3: Agent C working on Bug Fix Z
            └── Isolated directory, full git history

Result: Parallel development with zero risk to main branch
```

### Key Benefits

| Benefit | Description |
|---------|-------------|
| **Main branch protection** | Agents can't corrupt main; worst case = discard branch |
| **True parallelism** | No file locking needed; each agent has own filesystem |
| **Easy rollback** | Failed experiments = delete worktree, no cleanup |
| **Conflict isolation** | Merge conflicts handled at integration, not during work |

### Three-Layer Merge Resolution

When integrating worktree changes back to main:

```
Layer 1: Standard git auto-merge
    ↓ (if conflicts)
Layer 2: AI processes ONLY conflicting sections (~98% token savings)
    ↓ (if still unresolved)
Layer 3: Full-file AI resolution (fallback)
```

**Token Efficiency**: Processing only conflict hunks rather than full files saves ~98% of tokens on merge operations.

### Implementation with Claude Code

While Claude Code doesn't natively manage worktrees, the pattern applies when:
- Running multiple Claude Code instances on different branches
- Using external orchestration (Auto-Claude, scripts)
- Coordinating team members with AI agents

```bash
# Create isolated worktree for agent work
git worktree add ../feature-x-workspace feature-x

# Agent works in isolated directory
cd ../feature-x-workspace
# ... agent makes changes ...

# Integrate back when ready
git worktree remove ../feature-x-workspace
```

**Sources**: Auto-Claude, ccswarm (Tier C - community tools)

---

## Pattern 7: Tiered Model Strategy

**Use Case**: Optimizing cost and latency by matching model capability to task complexity

Not all tasks require the most powerful model. A tiered strategy allocates model resources based on task criticality.

### Model Tier Framework

| Tier | Model | Task Types | Rationale |
|------|-------|------------|-----------|
| **Tier 1** | Opus | Architecture, security review, complex reasoning | Highest capability for critical decisions |
| **Tier 2** | Sonnet | Standard development, moderate complexity | Balanced cost/capability for most work |
| **Tier 3** | Haiku | Fast operations, simple tasks, high volume | Speed and cost optimization |

### Claude Code Implementation

Use the `model` parameter in Task tool calls:

```markdown
## Tiered Subagent Deployment

### Critical Task (Tier 1 - Opus)
Task tool with:
- subagent_type: "Plan"
- model: "opus"
- prompt: "Design security architecture for authentication system"

### Standard Task (Tier 2 - Sonnet, default)
Task tool with:
- subagent_type: "Explore"
- prompt: "Find all files related to user authentication"

### Fast Task (Tier 3 - Haiku)
Task tool with:
- subagent_type: "Explore"
- model: "haiku"
- prompt: "Count lines of code in src/ directory"
```

### Decision Matrix

| Task Characteristic | Recommended Tier |
|---------------------|------------------|
| Security implications | Tier 1 (Opus) |
| Architectural decisions | Tier 1 (Opus) |
| Complex multi-step reasoning | Tier 1 (Opus) |
| Standard code generation | Tier 2 (Sonnet) |
| Code review | Tier 2 (Sonnet) |
| File search/exploration | Tier 3 (Haiku) |
| Simple transformations | Tier 3 (Haiku) |
| High-volume operations | Tier 3 (Haiku) |

### Cost/Latency Trade-offs

```
                    Capability
                        ↑
           Opus ────────●
                        │
          Sonnet ───────●
                        │
           Haiku ───────●
                        └──────────────→ Speed/Cost
```

**Rule of Thumb**: Default to Sonnet; escalate to Opus for critical decisions; drop to Haiku for volume operations.

**Sources**: wshobson/agents (Tier C - community tool, 24.2k stars)

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

## Anti-Patterns

### ❌ Over-Delegation
**Problem**: Spawning subagents for every small task
**Symptom**: Subagent overhead exceeds benefit, fragmented workflow
**Solution**: Reserve subagents for tasks taking 30+ seconds or needing fresh context

### ❌ Parallel Write Operations
**Problem**: Running multiple subagents that write to the same files
**Symptom**: Race conditions, overwritten changes, corrupted state
**Solution**: Only parallelize read operations; sequence all writes

### ❌ Assuming Shared Context
**Problem**: Writing subagent prompts that reference "the code we discussed"
**Symptom**: Subagent returns irrelevant results, misunderstands task
**Solution**: Include complete context in prompt—subagents have no conversation history

### ❌ Ignoring Result Synthesis
**Problem**: Collecting subagent results without integrating findings
**Symptom**: Fragmented understanding, missed connections between findings
**Solution**: Always synthesize and reconcile results after parallel subagent completion

---

## Sources

**Primary (Tier A)**:
- [Claude Code Sub-agents Documentation](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
- [Anthropic Engineering Blog: Effective Harnesses](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)

**Community Tools (Tier C)**:
- [Auto-Claude](https://github.com/AndyMik90/Auto-Claude) - Worktree isolation, parallel agents (5.1k stars)
- [wshobson/agents](https://github.com/wshobson/agents) - Tiered model strategy (24.2k stars)
- [ccswarm](https://github.com/nwiizo/ccswarm) - Git worktree + channel-based communication

*Last updated: January 2026*

---
version-requirements:
  claude-code: "v2.0.0+"  # Native subagent support
measurement-claims:
  - claim: "Native subagents handle ~80% of work with zero setup"
    source: "Claude Code Documentation"
    date: "2025-11-01"
    revalidate: "2026-11-01"
status: "PRODUCTION"
last-verified: "2026-02-16"
---

# Subagent Orchestration Patterns

**Source**: [Claude Code Documentation - Sub-agents](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
**Evidence Tier**: A (Primary vendor documentation)

> **This is the DEFAULT orchestration approach for Claude Code.** Native subagent patterns handle ~80% of work with zero additional setup. For specialized needs, see [Framework Selection Guide](./framework-selection-guide.md).

## Overview

Subagents are specialized Claude instances spawned by a parent agent to handle specific tasks with isolated context. They enable parallel execution, context isolation, and specialized behavior without consuming the parent's context window.

**SDD Phase**: Tasks + Implement (execution layer optimization)

**When to consider alternatives**:
- Multi-session continuity needed → [GSD Orchestration](./gsd-orchestration.md)
- Building reusable agent systems → [Cognitive Agent Infrastructure](./cognitive-agent-infrastructure.md)
- Enterprise scale (60+ agents) → Reference Claude-Flow in SOURCES.md

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

---

## Pattern 8: Thinking Mode Strategy

**Use Case**: Maximizing code quality with minimal steering corrections

Claude Opus 4.6 with extended thinking mode produces significantly higher-quality output, especially for complex tasks. Opus 4.6 also introduces adaptive reasoning controls (`effort` parameter) for fine-grained thinking depth.

### Boris Cherny's Recommendation

> "I use [Opus with extended thinking] for everything. It's the best coding model I've ever used... It's slower but because it's more reliable there's less course correcting and steering it towards what I wanted."
> — Boris Cherny, Claude Code Creator

### When to Use Thinking Mode

| Scenario | Thinking Mode | Rationale |
|----------|--------------|-----------|
| **Architecture design** | ✅ Yes | Complex trade-offs benefit from extended reasoning |
| **Security review** | ✅ Yes | Thoroughness critical, speed secondary |
| **Multi-file refactoring** | ✅ Yes | Need to hold many considerations simultaneously |
| **Debugging complex issues** | ✅ Yes | Root cause analysis requires deep reasoning |
| **Simple file edits** | ❌ No | Overhead not justified |
| **Quick searches** | ❌ No | Speed matters more than depth |
| **High-volume operations** | ❌ No | Latency compounds |

### Trade-offs

| Factor | With Thinking | Without Thinking |
|--------|--------------|------------------|
| **Latency** | Higher (2-3x) | Standard |
| **Quality** | Higher | Good |
| **Steering corrections** | Fewer | More frequent |
| **Token usage** | Higher | Lower |
| **Total time to completion** | Often lower (fewer retries) | Higher if steering needed |

### Implementation

Claude Code uses thinking mode based on the model setting. Opus 4.6 is the recommended default:

```bash
# Set default model (in claude.json or via CLI)
claude --model claude-opus-4-6

# Or configure in settings.json
{
  "model": "claude-opus-4-6"
}
```

**Key insight**: The time spent on extended thinking often saves more time by reducing back-and-forth steering corrections. Quality improves 2-3x with verification steps.

**Note on Opus 4.5/4.6 behavior**: These models are more responsive to system prompts and may overtrigger on aggressive tool/skill invocation language. If prompts were tuned for older models, dial back assertive language to avoid overengineering.

---

## Pattern 9: Three-Phase Exploration

**Use Case**: Comprehensive document/codebase exploration with cross-reference handling

This pattern structures exploration to maximize coverage while minimizing wasted effort. Based on agentic retrieval research, it outperforms single-pass exploration for complex codebases.

### The Three Phases

```
Phase 1: PARALLEL SCAN
    │
    ├── Quick overview of all candidates
    ├── Categorize: RELEVANT / MAYBE / SKIP
    └── Output: Triage list

Phase 2: DEEP DIVE
    │
    ├── Full extraction on RELEVANT items
    ├── Identify cross-references
    └── Output: Detailed findings + reference list

Phase 3: BACKTRACK
    │
    ├── Follow cross-references to SKIP/MAYBE items
    ├── Re-evaluate based on new context
    └── Output: Complete picture with dependencies
```

### Implementation with Explore Subagent

```markdown
## Three-Phase Exploration Prompt Template

Task tool with:
- subagent_type: "Explore"
- prompt: |
    Explore [TOPIC] in this codebase using three phases:

    **Phase 1 - Scan**: List all potentially relevant files/directories.
    Categorize each as RELEVANT, MAYBE, or SKIP with brief reasoning.

    **Phase 2 - Deep Dive**: For RELEVANT items, extract key information.
    Note any imports, references, or dependencies to other files.

    **Phase 3 - Backtrack**: For any references pointing to SKIP/MAYBE items,
    go back and extract the relevant context.

    Return:
    - Summary of findings
    - Key file locations with line numbers
    - Architecture/flow diagram if applicable
```

### When Three-Phase Excels

| Scenario | Benefit |
|----------|---------|
| **Understanding new codebase** | Systematic coverage, nothing missed |
| **Finding all usages** | Backtracking catches indirect references |
| **Architecture analysis** | Cross-references reveal structure |
| **Security audit** | Dependencies and data flow traced |
| **Refactoring planning** | Impact analysis with full reference chain |

### Parallel Three-Phase Exploration

For large codebases, run multiple three-phase explorations in parallel:

```markdown
## Parallel Three-Phase Setup

Launch IN PARALLEL (single message, multiple Task calls):

[Task 1: Explore] "Three-phase exploration of authentication"
[Task 2: Explore] "Three-phase exploration of authorization"
[Task 3: Explore] "Three-phase exploration of session management"

Each agent independently: scan → dive → backtrack
Parent synthesizes: merge findings, resolve overlaps
```

### Anti-Pattern: Single-Pass Exploration

**Problem**: Reading files once without revisiting based on discoveries
**Symptom**: "I found a reference to AuthHelper but didn't explore it"
**Solution**: Phase 3 backtracking ensures all references are followed

**Related**: See [Agentic Retrieval](./agentic-retrieval.md) for the theoretical foundation.

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

## Pattern 10: Agent Teams (Experimental)

**Source**: [Agent Teams Documentation](https://code.claude.com/docs/en/agent-teams) + [C Compiler Case Study](https://www.anthropic.com/engineering/building-a-c-compiler-with-parallel-claudes)
**Evidence Tier**: A (Primary vendor documentation)
**Status**: Research preview — experimental, disabled by default

> **This is NOT a replacement for subagents.** Agent teams are a fundamentally different coordination model for complex, multi-faceted problems.

### How Agent Teams Differ from Subagents

| Aspect | Subagents | Agent Teams |
|--------|-----------|-------------|
| **Communication** | Report back to parent only | Communicate with each other directly |
| **Context** | Fresh, isolated per subagent | Independent windows, shared task lists |
| **Coordination** | Parent orchestrates | Self-coordinating (lead + teammates) |
| **Lifetime** | Short-lived, task-specific | Long-lived, session-spanning |
| **Best for** | Quick focused tasks | Complex multi-faceted projects |

### Architecture

```
Lead Agent (orchestrator)
├── Teammate 1: [Own context window, own tools]
│   ├── Can communicate findings to other teammates
│   └── Can assign tasks to other teammates
├── Teammate 2: [Own context window, own tools]
│   └── Shares task list with all teammates
└── Teammate 3: [Own context window, own tools]
    └── Can challenge other teammates' findings
```

### Use Cases

| Scenario | Why Teams Help |
|----------|---------------|
| **Research + review** | Separate agents research and review simultaneously |
| **New module development** | Parallel implementation of interconnected components |
| **Debugging complex issues** | Multiple agents investigate different hypotheses |
| **Cross-layer coordination** | Frontend, backend, and database agents working together |

### Enabling Agent Teams

```bash
# Via environment variable
CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 claude

# Via settings.json
{
  "experimental": {
    "agentTeams": true
  }
}
```

### Case Study: C Compiler (Stress Test)

The most ambitious agent teams deployment to date:

| Metric | Value |
|--------|-------|
| **Agents** | 16 parallel |
| **Sessions** | ~2,000 |
| **Lines of code** | 100,000 (Rust) |
| **Cost** | ~$20,000 API |
| **Result** | C compiler capable of compiling Linux kernel (x86, ARM, RISC-V) |

### Current Limitations

- One team per lead agent (no nested teams)
- Session resumption can be unreliable
- Experimental — API and behavior may change
- Higher cost than subagent approaches for simpler tasks
- No deterministic control over teammate coordination

### When to Use Teams vs Subagents

| Factor | Use Subagents | Use Agent Teams |
|--------|--------------|-----------------|
| Task duration | Minutes | Hours to days |
| Coordination need | Report-back sufficient | Agents need to collaborate |
| Complexity | Single focused task | Multi-faceted problem |
| Cost sensitivity | Budget-conscious | Quality over cost |
| Stability requirement | Production | Research/experimentation |

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

- [GSD Orchestration](./gsd-orchestration.md) - Fresh context per subagent, STATE.md pattern
- [Cognitive Agent Infrastructure](./cognitive-agent-infrastructure.md) - 7 fixed cognitive agents vs domain proliferation
- [Johari Window](./johari-window-ambiguity.md) - SAAE protocol for surfacing unknowns
- [Agentic Retrieval](./agentic-retrieval.md) - Three-phase exploration theory and RAG comparison
- [Recursive Evolution](./recursive-evolution.md) - Full Self-Evolution Algorithm with iterative refinement
- [Long-Running Agent](./long-running-agent.md) - External artifacts for context bridging
- [Progressive Disclosure](./progressive-disclosure.md) - Token-efficient methodology loading
- [Context Engineering](./context-engineering.md) - Managing context effectively
- [Agent Principles](./agent-principles.md) - Six foundational principles for agent design
- [Advanced Hooks](./advanced-hooks.md) - SubagentStart/Stop hooks for orchestration
- [Safety and Sandboxing](./safety-and-sandboxing.md) - Security for multi-agent execution
- [Agent Evaluation](./agent-evaluation.md) - Evaluating agent team performance

---

## Orchestration Framework Comparison

Different frameworks take different approaches to agent orchestration:

| Framework | Agent Count | Context Strategy | State Management | Best For |
|-----------|-------------|------------------|------------------|----------|
| **GSD** | ~5 workflow | Fresh per subagent | STATE.md + .planning/ | Multi-phase projects |
| **CAII** | 7 cognitive | On-the-fly injection | Task-specific memories | Scalable architecture |
| **Domain-Specific** | N (grows) | Specialized | Varies | Deep domain expertise |
| **Standard Claude Code** | 1 + subagents | Accumulating | Conversation | Simple tasks |

### GSD Fresh Context Model

The GSD pattern addresses context rot by giving each executor a fresh context window:

```
Orchestrator (thin, coordination only)
    │
    ├── [Executor 1: Fresh 200K tokens] → Task 1 → Atomic Commit
    ├── [Executor 2: Fresh 200K tokens] → Task 2 → Atomic Commit
    └── [Executor 3: Fresh 200K tokens] → Task 3 → Atomic Commit
```

**Key Principles**:
- Orchestrator never implements directly
- Each executor receives only task spec + minimal context
- State externalized to STATE.md (survives context resets)
- One task = one atomic git commit

**See**: [GSD Orchestration](./gsd-orchestration.md) for full pattern documentation.

### CAII Cognitive Model

CAII organizes by cognitive function, not domain:

```
7 Fixed Cognitive Agents:
├── Clarification  → Transforms ambiguity into specs
├── Research       → Gathers domain knowledge
├── Analysis       → Decomposes problems
├── Synthesis      → Integrates findings
├── Generation     → Creates artifacts (TDD)
├── Validation     → Verifies quality
└── Memory         → Monitors progress, captures learnings
```

**Key Principles**:
- Fixed agent count (doesn't grow with scope)
- Domain context injected at runtime
- Deterministic Python orchestration (not LLM prompting)
- System improves over time via memory capture

**See**: [Cognitive Agent Infrastructure](./cognitive-agent-infrastructure.md) for full pattern documentation.

### Choosing an Orchestration Approach

| If You Need | Consider |
|-------------|----------|
| Multi-session continuity | GSD (STATE.md pattern) |
| Scalable, maintainable agents | CAII (fixed cognitive agents) |
| Deep domain specialization | Domain-specific agents |
| Simple coordination | Standard subagent patterns |
| Enterprise scale (60+ agents) | Claude-Flow |

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
- [Agent Teams Documentation](https://code.claude.com/docs/en/agent-teams)
- [Building a C Compiler with Parallel Claudes](https://www.anthropic.com/engineering/building-a-c-compiler-with-parallel-claudes) (February 2026)
- [How We Built Our Multi-Agent Research System](https://www.anthropic.com/engineering/how-we-built-our-multi-agent-research-system) (June 2025)

**Community Tools (Tier C)**:
- [Auto-Claude](https://github.com/AndyMik90/Auto-Claude) - Worktree isolation, parallel agents (5.1k stars)
- [wshobson/agents](https://github.com/wshobson/agents) - Tiered model strategy (24.2k stars)
- [ccswarm](https://github.com/nwiizo/ccswarm) - Git worktree + channel-based communication

*Last updated: February 2026*

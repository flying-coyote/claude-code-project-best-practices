# GSD (Get Shit Done) Orchestration Pattern

**Source**: [glittercowboy/get-shit-done](https://github.com/glittercowboy/get-shit-done)
**Evidence Tier**: B (Open source, production-validated)

## Overview

GSD is an orchestration pattern that maximizes Claude's effectiveness through **fresh context per subagent** and **state externalization**. The orchestrator never does heavy lifting—it spawns specialized agents, waits, and integrates results.

**SDD Phase**: Cross-phase orchestration (enhances Specify, Plan, Tasks, and Implement)

> "The orchestrator never does heavy lifting. It spawns agents, waits, integrates results."
> — GSD Architecture Principle

---

## Core Principles

### 1. Fresh Context Per Subagent

Each executor receives **200k tokens purely for implementation**, with zero accumulated garbage from previous tasks. This prevents "context rot"—quality degradation from filled context windows.

| Traditional Approach | GSD Approach |
|---------------------|--------------|
| Single agent accumulates context | Fresh agent per task |
| Quality degrades over time | Consistent quality throughout |
| Context exhaustion limits scope | Project scope unlimited |
| Must summarize to continue | Clean handoff via STATE.md |

### 2. Thin Orchestrator

The orchestrator coordinates but doesn't execute:

```
Orchestrator (coordination only)
    │
    ├── [Researcher] Domain investigation
    ├── [Planner] Task specification
    ├── [Executor] Implementation (fresh context)
    └── [Verifier] Acceptance testing
```

### 3. State Externalization

All project state persists in files, not in context:

```
.planning/
├── STATE.md              # Current position, decisions, blockers
├── config.json           # Project settings
├── research/             # Domain investigation artifacts
├── {phase}-CONTEXT.md    # Implementation decisions
├── {phase}-RESEARCH.md   # Ecosystem findings
├── {phase}-{N}-PLAN.md   # Atomic task specifications
└── {phase}-{N}-SUMMARY.md # Execution records
```

---

## The STATE.md Pattern

A persistent memory file that survives context resets:

```markdown
# STATE.md

## Current Phase
Implementing authentication (Phase 2)

## Last Action
Completed task 2.3: OAuth token refresh

## Decisions Made
- Using JWT with 15-minute expiry
- Refresh tokens stored in Redis
- No session cookies (stateless)

## Blockers
- Waiting on API key from auth provider

## Next Steps
1. Task 2.4: Implement logout endpoint
2. Task 2.5: Add rate limiting
```

**Purpose**: Any new agent can read STATE.md and understand exactly where the project is without requiring the orchestrator to explain.

---

## Workflow Phases

GSD defines six workflow phases with human checkpoints:

```
┌──────────────────────────────────────────────────────────────────┐
│                     GSD WORKFLOW PHASES                          │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  INITIALIZE ──► DISCUSS ──► PLAN ──► EXECUTE ──► VERIFY ──► COMPLETE │
│       │            │          │          │          │           │
│   Questions    Capture    Research    Parallel   User QA     Archive │
│   Research    Prefs      + Tasks     Impl       + Fixes      Tag    │
│   Scoping               + Verify                             │
│                         Loop                                      │
│       │            │          │          │          │           │
│       └────────────┼──────────┼──────────┼──────────┼───────────┘
│                    │          │          │          │
│              [HUMAN CHECKPOINT]    [HUMAN CHECKPOINT]
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

### Phase Details

| Phase | Purpose | Human Checkpoint? |
|-------|---------|------------------|
| **Initialize** | Questions, research, scoping | No |
| **Discuss** | Capture implementation preferences | **Yes** |
| **Plan** | Research + task creation + verification loop | No |
| **Execute** | Parallel implementation, atomic commits | No |
| **Verify** | User acceptance testing + failure diagnosis | **Yes** |
| **Complete** | Archive milestone, tag release | No |

---

## XML Task Formatting

Tasks use structured XML optimized for Claude's parsing:

```xml
<task type="auto">
  <name>Implement OAuth token refresh</name>
  <action>
    Create endpoint POST /auth/refresh that:
    1. Validates refresh token from Redis
    2. Issues new JWT with 15-minute expiry
    3. Rotates refresh token
    4. Returns new token pair
  </action>
  <verify>
    - Unit tests pass
    - Integration test with expired token
    - Redis entries cleaned up after rotation
  </verify>
  <done>
    Endpoint responds correctly to valid/invalid/expired tokens
  </done>
</task>
```

### Task Types

| Type | Behavior |
|------|----------|
| `auto` | Execute without confirmation |
| `confirm` | Pause for user approval before execution |
| `manual` | User executes, agent verifies result |

### Why XML?

XML provides:
- Clear delimiters for Claude's parsing
- Embedded verification criteria
- Machine-readable structure for automation
- Human-readable for review

---

## Implementation with Claude Code

### Directory Setup

```bash
# Create .planning directory structure
mkdir -p .planning/research
touch .planning/STATE.md
touch .planning/config.json
```

### Orchestrator Prompt Pattern

```markdown
## GSD Orchestrator Instructions

You are coordinating a project using GSD methodology.

### Rules
1. **Never implement directly** - spawn subagents for all work
2. **Update STATE.md** after every significant action
3. **One task per commit** - atomic, verifiable changes
4. **Fresh context** - each executor gets clean context with only task spec

### Current State
Read .planning/STATE.md for current position.

### Workflow
1. Parse user request
2. Update STATE.md with new objective
3. Spawn research subagent if needed
4. Create task XML specifications
5. Spawn executor per task (parallel where safe)
6. Spawn verifier after execution
7. Update STATE.md with results
8. Present summary to user
```

### Spawning Fresh Executors

```markdown
## Executor Subagent Pattern

Task tool with:
- subagent_type: "general-purpose"
- prompt: |
    You are an executor with fresh context.

    ## Task Specification
    [Paste XML task here]

    ## Project Context
    [Paste minimal necessary context from STATE.md]

    ## Rules
    - Implement ONLY what the task specifies
    - Create ONE atomic commit when done
    - Report success/failure with evidence

    Do NOT read STATE.md or other planning files.
    Your context is complete in this prompt.
```

---

## Atomic Commits Pattern

Each task produces exactly one commit:

```
Task 2.3: OAuth token refresh
    └── Commit: "feat(auth): implement token refresh endpoint"
         └── Files: auth/refresh.ts, auth/refresh.test.ts

Task 2.4: Logout endpoint
    └── Commit: "feat(auth): implement logout endpoint"
         └── Files: auth/logout.ts, auth/logout.test.ts
```

**Benefits**:
- Easy rollback (revert single commit)
- Clear audit trail (commit = task)
- Bisectable history (find which task broke build)
- Parallel-safe (no merge conflicts if tasks independent)

---

## When to Use GSD

### Good Fits

| Scenario | Why GSD Helps |
|----------|---------------|
| **Multi-phase projects** | State externalization enables session continuity |
| **Large features** | Fresh context per task prevents quality degradation |
| **Team handoffs** | STATE.md provides complete context for any agent |
| **Complex workflows** | Human checkpoints at discuss/verify phases |

### Poor Fits

| Scenario | Why Not |
|----------|---------|
| **Quick fixes** | Overhead exceeds benefit |
| **Single-file changes** | No orchestration needed |
| **Exploratory work** | Structure premature before understanding problem |
| **Time-critical tasks** | Orchestration adds latency |

---

## Comparison with Other Patterns

| Pattern | Agent Count | Context Strategy | State Management |
|---------|-------------|------------------|------------------|
| **GSD** | ~5 specialized | Fresh per subagent | STATE.md + .planning/ |
| **CAII Cognitive** | 7 fixed | On-the-fly context injection | Task-specific memories |
| **Domain-specific** | N (grows) | Specialized per domain | Varies |
| **Single agent** | 1 | Accumulating | Conversation history |

**Key GSD Differentiator**: Fresh context per executor prevents the quality degradation that occurs when agents work with filled context windows.

---

## Integration with Existing Patterns

| Pattern | Integration Point |
|---------|-------------------|
| **Subagent Orchestration** | GSD extends with state externalization |
| **Context Engineering** | STATE.md is context engineering for persistence |
| **Long-Running Agent** | .planning/ directory enables session continuity |
| **Progressive Disclosure** | Task XML loads only relevant context |

---

## Anti-Patterns

### ❌ Orchestrator Does Implementation

**Problem**: Orchestrator directly edits files instead of spawning executors
**Symptom**: Context fills with implementation details, quality degrades
**Solution**: Orchestrator only coordinates; spawn fresh executor for every change

### ❌ Accumulated Context

**Problem**: Executor carries context from previous tasks
**Symptom**: Later tasks have lower quality than early tasks
**Solution**: Each executor gets fresh context with only current task spec

### ❌ Skipping STATE.md Updates

**Problem**: State tracked in conversation, not externalized
**Symptom**: Context reset loses all progress understanding
**Solution**: Update STATE.md after every significant action

### ❌ Multi-Task Commits

**Problem**: Single commit contains multiple tasks
**Symptom**: Difficult to rollback, unclear audit trail
**Solution**: One task = one commit, always

---

## Example: Feature Implementation

### Phase 1: Initialize

```markdown
User: "Add user authentication to the app"

Orchestrator actions:
1. Create .planning/STATE.md with objective
2. Spawn research subagent: "Find existing auth patterns in codebase"
3. Spawn research subagent: "Identify dependencies and integration points"
4. Update STATE.md with research findings
```

### Phase 2: Discuss

```markdown
Orchestrator presents:
"Based on research, I recommend:
- JWT tokens with 15-minute expiry
- Refresh tokens in Redis
- OAuth2 with Google/GitHub providers

Do you have preferences on auth strategy?"

[Human confirms or adjusts]

Update STATE.md with decisions.
```

### Phase 3: Plan

```markdown
Orchestrator creates task specifications:

.planning/auth-1-PLAN.md:
<task type="auto">
  <name>Create user model</name>
  <action>...</action>
  <verify>...</verify>
  <done>...</done>
</task>

.planning/auth-2-PLAN.md:
<task type="auto">
  <name>Implement login endpoint</name>
  ...
</task>

[Continue for all tasks]
```

### Phase 4: Execute

```markdown
Orchestrator spawns executors (parallel where safe):

[Executor 1: Fresh context] → Task 1: User model → Commit
[Executor 2: Fresh context] → Task 2: Login endpoint → Commit
[Executor 3: Fresh context] → Task 3: Logout endpoint → Commit
...

Each executor:
- Receives ONLY its task XML + minimal context
- Implements the specified change
- Creates atomic commit
- Reports success/failure
```

### Phase 5: Verify

```markdown
Orchestrator presents:
"Implementation complete. 5 tasks executed:
✓ Task 1: User model
✓ Task 2: Login endpoint
✓ Task 3: Logout endpoint
✓ Task 4: Token refresh
✗ Task 5: Rate limiting (test failure)

Please verify tasks 1-4 work correctly.
Task 5 will be re-attempted after diagnosis."

[Human tests, provides feedback]
```

### Phase 6: Complete

```markdown
Orchestrator:
1. Archive phase artifacts
2. Update STATE.md: "Authentication complete"
3. Create git tag: v1.1.0-auth
4. Clean up temporary files
```

---

## Related Patterns

- [Subagent Orchestration](./subagent-orchestration.md) - Foundation patterns for parallel agents
- [Context Engineering](./context-engineering.md) - Managing context effectively
- [Long-Running Agent](./long-running-agent.md) - External artifacts for session continuity
- [Cognitive Agent Infrastructure](./cognitive-agent-infrastructure.md) - Alternative 7-agent architecture

---

## Sources

**Primary (Tier B)**:
- [glittercowboy/get-shit-done](https://github.com/glittercowboy/get-shit-done) - Production implementation

**Related (Tier B)**:
- [skribblez2718/caii](https://github.com/skribblez2718/caii) - Cognitive Agent Infrastructure (alternative approach)
- [ruvnet/claude-flow](https://github.com/ruvnet/claude-flow) - Enterprise orchestration patterns

*Last updated: January 2026*

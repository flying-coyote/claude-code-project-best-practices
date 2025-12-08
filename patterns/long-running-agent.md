# Long-Running Agent Harness Patterns

**Source**: Anthropic Engineering Blog (November 2025)
**URL**: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents

## The Core Problem

> "Each new session begins with no memory of what came before. Imagine a software project staffed by engineers working in shifts, where each new engineer arrives with no memory of what happened on the previous shift."

Context windows are limited. Complex projects cannot be completed in a single window. Agents need a way to bridge sessions.

## Key Insight

> "External artifacts become the agent's memory. Progress files, git history, and structured feature lists persist across sessions."

## Two-Part Architecture

### 1. Initializer Agent (Project Start)

Creates:
- `claude-progress.md` - Human-readable progress log
- `feature_list.json` - Structured task list with pass/fail status
- Initial git commit - Baseline for rollback

### 2. Coding Agent (Subsequent Sessions)

Workflow:
1. `pwd` - Verify working directory
2. Read `claude-progress.md` - Understand recent work
3. Read task list - What needs doing
4. `git log --oneline -20` - Recent commits for context
5. Basic test - Verify environment not broken
6. Pick ONE feature - Work incrementally
7. Test feature - E2E validation (not just unit tests)
8. `git commit` - Descriptive message
9. Update progress file - Externalize memory

## Design Decisions

### JSON Over Markdown for Task Tracking

```json
{
  "category": "functional",
  "description": "New chat button creates a fresh conversation",
  "passes": false
}
```

**Why**: Model is less likely to inappropriately modify structured data.

### One Feature at a Time

Prevents:
- Context exhaustion mid-implementation
- Undocumented partial work
- Complex merge conflicts

### Git as Recovery Mechanism

- Every completed feature = git commit
- Descriptive commit messages for context recovery
- Enables rollback when things break

## Failure Modes Addressed

| Failure Mode | Root Cause | Mitigation |
|--------------|------------|------------|
| **One-shotting** | Agent tries to complete entire project at once | Structured task list, one-at-a-time constraint |
| **Premature victory** | Agent sees progress, declares done | Pass/fail status per feature |
| **Incomplete testing** | Unit tests only | E2E testing requirement |
| **Broken handoffs** | No documentation of work state | Progress file + git history |
| **Environment corruption** | Starting with broken state | "Verify before work" startup protocol |

## Application to Your Projects

### Research Domain Adaptations

| Web Dev Pattern | Research Equivalent |
|-----------------|---------------------|
| `feature_list.json` | Hypothesis tracker with validation status |
| `passes: true/false` | Confidence rating (1-5) + evidence tier |
| E2E testing | Expert validation, production POC |
| Git commits | Document versions with clear deltas |
| `init.sh` | Session startup hook with project context |

### Implementation in Excellence Kit

The session-start hook implements:
- "Verify before work" - checks uncommitted changes, in-progress tasks
- Context loading - shows branch, recent commits, current phase
- Warning surfacing - alerts about potential issues before new work

---

## Related Patterns

- [Memory Architecture](./memory-architecture.md) - Lifecycle-based information management
- [Documentation Maintenance](./documentation-maintenance.md) - ARCH/PLAN/INDEX trio
- [Advanced Hooks](./advanced-hooks.md) - SessionStart implementation patterns

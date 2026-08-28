# Long-Running Agent Harness Patterns

> **ARCHIVED — but nothing live replaces it.** Archived in the v2.0 repositioning (March 2026, DECISIONS.md § Reposition as Analytical Layer) or a later reduction. No live successor covers this document. analysis/harness-engineering.md cites the same Anthropic primary source at Tier A and names the architecture in a single clause ("CLAUDE.md + progress file, a 2-agent architecture, external artifacts as memory") as a ranking datum, but carries none of this doc's substance; its "Where Failure Actually Lives" section is an unrelated failure taxonomy (flaky mocks, hermetic/production gap), and its Opus-5-era guidance to delete carried-over verification scaffolding runs against this doc's pass/fail-gate and verify-before-work mitigations. analysis/memory-system-patterns.md documents a different mechanism — Claude Code's typed auto-memory layer — and explicitly advises against persisting git history or task state. The operational core here is live nowhere in the repository: the nine-step startup sequence, JSON-over-markdown task tracking with its {category, description, passes} schema, one-feature-at-a-time, git-as-recovery, the five-failure-mode table (one-shotting, premature victory, incomplete testing, broken handoffs, environment corruption), and the research-domain adaptation table. Read this archived file directly for that material; treat it as unreplaced, not superseded. This is a **coverage gap, not a currency gap** — the material is unreplaced, not merely out of date, so a reader who discards it is left with nothing. Its specifics are v1-era; its subject is still uncovered. (Marked 2026-08-28; successor determined by mapping plus adversarial verification, which overturned 35 of 39 successor claims — see `analysis/prose-corpus-discoverability.md`.)

**Source**: Anthropic Engineering Blog (November 2025)
**URL**: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
**Evidence Tier**: A (Primary vendor documentation)

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

## Anti-Patterns

### ❌ One-Shotting Complex Features
**Problem**: Trying to complete entire projects in a single session
**Symptom**: Context exhaustion, abandoned work, no rollback points
**Solution**: One feature at a time with git commits as checkpoints

### ❌ In-Memory State Only
**Problem**: Keeping critical context only in conversation history
**Symptom**: Lost progress when session ends or context rotates
**Solution**: Externalize to progress files, git commits, task lists

### ❌ Skipping "Verify Before Work"
**Problem**: Starting work without checking project state
**Symptom**: Building on broken foundations, conflicting changes
**Solution**: Always run verification (git status, basic tests) at session start

### ❌ Premature Victory Declaration
**Problem**: Agent declares "done" after partial implementation
**Symptom**: Features that work in isolation but fail in integration
**Solution**: Use pass/fail status per feature, require E2E validation

---

## Related Patterns

- [Memory Architecture](./memory-architecture.md) - Lifecycle-based information management
- [Documentation Maintenance](./documentation-maintenance.md) - ARCH/PLAN/INDEX trio
- [Advanced Hooks](./advanced-hooks.md) - SessionStart implementation patterns
- [Subagent Orchestration](./subagent-orchestration.md) - Context window recovery via subagents
- Agent Principles (doc retired 2026-07-10 — official Anthropic best-practices carries this slice) - Foundational principles for agent design

*Last updated: January 2026*

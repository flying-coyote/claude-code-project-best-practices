# Orchestration Approaches: Comparative Analysis

**Evidence Tier**: Mixed (A-B) — Vendor documentation + production-validated community patterns

## Purpose

This document provides an **evidence-based comparison** of agent orchestration approaches for Claude Code. Instead of documenting how each works (covered extensively in [everything-claude-code](https://github.com/anthropics-solutions/everything-claude-code)), this focuses on *when to choose which approach and why*.

---

## The Five-Layer Architecture (Boris Cherny, March 2026)

Before comparing orchestration approaches, understand the Claude Code stack:

```
Layer 5: Agent Teams    <- Multi-agent coordination with shared task lists
Layer 4: Subagents      <- Parallel independent workers, report to parent
Layer 3: Agent          <- Primary worker (the main Claude session)
Layer 2: Skills         <- Task-specific knowledge and workflows
Layer 1: MCP            <- Connectivity to external tools and services
```

**Key principle**: Most work should start at Layer 3 and only escalate when needed. Premature orchestration adds complexity without benefit.

---

## Approach Comparison Matrix

| Factor | Native Subagents | GSD | CAII | Agent Teams | Domain-Specific |
|--------|-----------------|-----|------|-------------|-----------------|
| **Agent count** | 1 + ad hoc | ~5 workflow | 7 fixed cognitive | N (lead + teammates) | N (grows with scope) |
| **Context strategy** | Fresh per subagent | Fresh per executor | On-the-fly injection | Independent windows | Specialized |
| **State management** | Conversation | STATE.md + .planning/ | Task-specific memories | Shared task lists | Varies |
| **Orchestration** | Parent delegates | Human checkpoints | Deterministic state machine | Self-coordinating | Varies |
| **Setup cost** | Zero | Low (directory structure) | Medium (Python orchestration) | Low (env var) | High |
| **Maintenance** | None | Low | Low (7 constant agents) | Low | High (grows) |
| **Evidence tier** | A (Anthropic docs) | B (community) | B (community) | A (Anthropic, experimental) | C (varies) |

---

## Decision Framework

### Start Here: Do You Need Orchestration?

```
Single task, single session?
  -> NO orchestration needed. Use Layer 3 (main agent).

Task needs parallel research?
  -> Native subagents (Layer 4). Zero setup.

Multi-session project with state continuity?
  -> GSD pattern (STATE.md externalization).

Agents need to talk to each other?
  -> Agent Teams (Layer 5). Experimental.

Building reusable multi-agent system?
  -> CAII cognitive agents or custom .claude/agents/.

60+ agents, enterprise scale?
  -> External tools (Claude-Flow, Auto-Claude).
```

### Detailed Selection Guide

| If you need... | Use | Why |
|----------------|-----|-----|
| Quick parallel searches | Native subagents | Zero setup, built-in, production-ready |
| Fresh context for each task | Native subagents or GSD | Both isolate context; GSD adds state persistence |
| Multi-session continuity | GSD | STATE.md survives session boundaries |
| Scalable agent architecture | CAII | Fixed 7 agents regardless of domain growth |
| Agents that collaborate | Agent Teams | Direct inter-agent communication |
| Domain-deep specialization | Custom agents (.claude/agents/) | Dedicated prompts, tools, model per role |
| Complex research synthesis | Self-Evolution (diversity sampling) | Multiple perspectives, iterative refinement |

---

## Native Subagents: The Default

**Source**: Anthropic documentation (Tier A)

Native subagents handle ~80% of orchestration needs with zero setup. Four built-in types:

| Type | Purpose | Use When |
|------|---------|----------|
| `Explore` | Fast codebase search | Finding files, answering architecture questions |
| `Plan` | Design implementation strategy | Architecture decisions, trade-off analysis |
| `general-purpose` | Multi-step autonomous tasks | Complex research, code generation |
| `claude-code-guide` | Documentation lookup | Claude Code feature questions |

**Anti-pattern warning** (Boris Cherny): Custom subagents can "gatekeep context" and force rigid workflows. Prefer native delegation unless you need truly specialized roles.

### Key Patterns

| Pattern | What It Does | When |
|---------|-------------|------|
| Parallel Research | Multiple Explore agents simultaneously | Gathering info from multiple areas |
| Context Window Recovery | Delegate to fresh subagent when parent context fills | 60%+ context usage |
| Background Agent | `run_in_background: true` for long tasks | Tests, builds, large analysis |
| Worktree Isolation | `isolation: worktree` for safe parallel writes | Multiple agents modifying code |
| Tiered Models | Opus for critical, Sonnet default, Haiku for volume | Cost optimization |

---

## GSD: Multi-Session State Continuity

**Source**: glittercowboy/get-shit-done (Tier B)

GSD's unique contribution is **state externalization** — all project state persists in files, not conversation memory.

**Core principles**:
1. Fresh context per executor (200K tokens purely for implementation)
2. Thin orchestrator (coordinates but doesn't execute)
3. State in STATE.md (survives context resets and session boundaries)
4. One task = one atomic commit

**When GSD adds value over native subagents**:
- Project spans multiple sessions
- Multiple people/agents contribute to same project
- Need audit trail of decisions (STATE.md history)
- Complex workflow with human checkpoints (discuss/verify phases)

**When GSD is overkill**:
- Single-session tasks
- Quick fixes
- Exploratory work (structure premature)

---

## CAII: Cognitive Function Architecture

**Source**: skribblez2718/caii (Tier B)

CAII's unique insight: organize agents by *how they think*, not *what they work on*. Seven fixed cognitive agents handle any domain:

| Agent | Cognitive Function | Maps To |
|-------|-------------------|---------|
| Clarification | Ambiguity → specs | Johari Window / SAAE protocol |
| Research | Knowledge gathering | Explore subagent |
| Analysis | Problem decomposition | Plan subagent |
| Synthesis | Finding integration | general-purpose subagent |
| Generation | Artifact creation (TDD) | general-purpose subagent |
| Validation | Quality verification | Explore subagent |
| Memory | Progress monitoring | Hooks + external files |

**When CAII adds value**:
- Building reusable agent systems across multiple domains
- Agent count growing uncontrollably with each new project type
- Need deterministic orchestration (Python state machine, not prompt-based)
- Want system that improves over time via memory capture

**When CAII is overkill**:
- Well-defined single tasks
- Time-critical work (multi-phase adds latency)
- Already have working domain agents

---

## Agent Teams: Collaborative Agents

**Source**: Anthropic documentation (Tier A, experimental)

Agent teams are fundamentally different — agents communicate with each other directly, not just report to a parent.

**Case study**: 16 parallel agents, ~2,000 sessions, produced a 100K-line C compiler capable of compiling the Linux kernel. Cost: ~$20,000 API.

**When to use teams over subagents**:
- Agents need to challenge each other's findings
- Work requires cross-component coordination
- Task spans hours to days (not minutes)
- Quality justifies higher token cost

**Current limitations** (as of March 2026):
- Experimental (disabled by default, `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`)
- One team per lead agent (no nesting)
- Session resumption can be unreliable
- No deterministic control over coordination

---

## Self-Evolution: Quality Through Diversity

**Source**: Google TTD-DR Paper + OptILLM (Tier B)

Not a full orchestration framework, but a pattern applicable within any framework. Spawns multiple candidates with different analytical approaches, then synthesizes the best elements.

| Step | What Happens | Token Cost |
|------|-------------|------------|
| Multi-candidate init | 3 parallel subagents (conservative/balanced/creative) | 3x |
| Refinement loop | Each candidate iterated 3x with judge feedback | ~9x |
| Crossover synthesis | Best elements merged | ~13x total |

**When worth the cost**:
- High-stakes decisions (architecture, security)
- Complex research synthesis
- When single-pass quality is insufficient
- Quality-critical output where 13x tokens is justified

**When not worth it**:
- Simple factual lookups
- Time-critical responses
- Token-constrained environments

---

## Coverage Analysis: What ECC Covers vs. Unique Value

Based on analysis of [everything-claude-code](https://github.com/anthropics-solutions/everything-claude-code) (110K stars):

| Topic | ECC Coverage | This Document's Unique Value |
|-------|-------------|------------------------------|
| Native subagent API | IMPLEMENTED (125+ skills) | None — defer to ECC |
| GSD pattern | MENTIONED (reference) | Comparative analysis, when-to-use framework |
| CAII pattern | ABSENT | Only comparative documentation available |
| Agent teams | MENTIONED | Decision framework for teams vs subagents |
| Self-evolution | ABSENT | Only Claude Code adaptation documented |
| Boris Cherny warnings | ABSENT | Gatekeeping anti-pattern, five-layer model |
| Decision framework | ABSENT | Cross-approach comparison matrix |

---

## Anti-Patterns Across All Approaches

| Anti-Pattern | Applies To | Instead |
|-------------|-----------|---------|
| Orchestrator does implementation | GSD, CAII | Orchestrator coordinates only |
| Accumulated context across tasks | All | Fresh context per executor |
| Custom agents gatekeeping context | Native | Let main agent use native delegation |
| Parallel write operations | All | Only parallelize reads; sequence writes |
| Domain agent proliferation | Domain-specific | Use CAII cognitive functions or native subagents |
| Skipping state externalization | GSD | Always update STATE.md after significant actions |
| Over-delegation | All | Reserve orchestration for 30+ second tasks |

---

## Sources

**Tier A (Vendor)**:
- [Claude Code Sub-agents Documentation](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
- [Agent Teams Documentation](https://code.claude.com/docs/en/agent-teams)
- [Building a C Compiler with Parallel Claudes](https://www.anthropic.com/engineering/building-a-c-compiler-with-parallel-claudes)
- Boris Cherny: Five-layer architecture, subagent gatekeeping warning (March 2026)

**Tier B (Validated)**:
- [glittercowboy/get-shit-done](https://github.com/glittercowboy/get-shit-done) — GSD orchestration
- [skribblez2718/caii](https://github.com/skribblez2718/caii) — CAII cognitive agents
- Google TTD-DR Paper — Self-Evolution Algorithm

## Related Analysis

- [Harness Engineering](./harness-engineering.md) — Orchestration is one layer of the broader harness stack; see the 6-layer model and diagnostic framework

---

*Merged from: gsd-orchestration.md, cognitive-agent-infrastructure.md, subagent-orchestration.md, recursive-evolution.md*
*Last updated: March 2026*

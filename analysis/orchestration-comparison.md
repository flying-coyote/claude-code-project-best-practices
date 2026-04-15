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

| Factor | Native Subagents | GSD | CAII | Agent Teams | Advisor | Domain-Specific |
|--------|-----------------|-----|------|-------------|---------|-----------------|
| **Agent count** | 1 + ad hoc | ~5 workflow | 7 fixed cognitive | N (lead + teammates) | 1 + 1 advisor | N (grows with scope) |
| **Context strategy** | Fresh per subagent | Fresh per executor | On-the-fly injection | Independent windows | Shared | Specialized |
| **State management** | Conversation | STATE.md + .planning/ | Task-specific memories | Shared task lists | Conversation | Varies |
| **Orchestration** | Parent delegates | Human checkpoints | Deterministic state machine | Self-coordinating | Executor-driven escalation | Varies |
| **Setup cost** | Zero | Low (directory structure) | Medium (Python orchestration) | Low (env var) | Low (API config) | High |
| **Maintenance** | None | Low | Low (7 constant agents) | Low | None | High (grows) |
| **Evidence tier** | A (Anthropic docs) | B (community) | B (community) | A (Anthropic, experimental) | A (Anthropic) | C (varies) |

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

## Advisor Strategy: Tiered Collaboration Without Sub-Agent Overhead

**Source**: Anthropic API feature (Tier A), April 2026

A distinct pattern that sits between tiered model usage and full sub-agent orchestration. Opus serves as an advisor paired with a Sonnet/Haiku executor. The executor drives implementation and escalates to the advisor via tool call. Context is shared, but the advisor never writes code directly.

**Performance claims** (Anthropic's own benchmarks — treat with appropriate skepticism):
- 2% higher on multilingual SWE-bench vs non-advisor baselines
- 11% lower cost

**When to use over alternatives**:
- Need expert-level reasoning guidance without the overhead of full sub-agent decomposition
- Want cost optimization: executor runs on cheaper model, advisor consulted only when needed
- Tasks where architectural guidance matters more than parallel execution

**How it differs from other patterns**:
- Not tiered model usage (advisor is an active participant via tool call, not just a model tier switch)
- Not sub-agent decomposition (single executor, single advisor — no task splitting)
- Not Agent Teams (no peer-to-peer communication, strictly hierarchical escalation)

---

## Managed Agents: Anthropic-Hosted Agent Infrastructure

**Source**: Anthropic (Tier A), April 2026

A deployment layer rather than an orchestration pattern. Anthropic hosts and runs agents with secure sandboxing, removing the need for local execution infrastructure.

**Capabilities**:
- Secure sandboxed execution environment
- OAuth vaults for credential management
- Environment scoping with explicit permission grants
- Long-running sessions (hours, not minutes)
- Multi-agent coordination

**Pricing**: Standard token costs + $0.08/session-hour

**Operational gotchas**:
- Environments and agents have separate lifecycles (environment can outlive or be recycled independently of agent state)
- Currently locked to Sonnet 4.6 (no model selection)

**When to consider**:
- Need long-running agent sessions without keeping a local machine alive
- Security requirements demand sandboxed execution with managed credentials
- Multi-agent coordination where Anthropic handles the infrastructure layer

---

## Routines: Event-Driven Agent Execution

**Source**: Anthropic (Tier A, research preview), April 2026

Cloud-hosted workflows triggered by schedule, API call, or event. Think cron for agents — runs on Anthropic infrastructure without requiring a local machine.

**Trigger types**:
- Scheduled (time-based)
- API call (programmatic)
- Event-driven (webhook, external trigger)

**Current status**: Research preview. Not production-ready.

**When this becomes relevant**:
- Recurring agent tasks (nightly code reviews, scheduled report generation)
- Event-driven automation (PR opened -> agent runs analysis)
- Workflows where local machine availability is a constraint

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

## Measured Orchestration Overhead

**Source**: Chase AI (Tier C, Authority 2/5)

Measured token and time costs for a **simple greenfield web app task** across three approaches:

| Approach | Tokens | Time | Notes |
|----------|--------|------|-------|
| GSD | 1.2M | 105 min | Full orchestrator + executor workflow |
| Superpowers | 250K | 60 min | Prompt-based orchestration layer |
| Vanilla Claude Code | 200K | 20 min | No orchestration framework |

**Heavy caveats**: This data covers one task type only — a simple greenfield web app. It does NOT test:
- Complex brownfield codebases (where context management matters most)
- Multi-session projects (where GSD's state persistence pays off)
- Team handoff scenarios (where STATE.md provides continuity)
- Tasks requiring parallel execution

The overhead numbers are real, but the scenarios where orchestration tools claim differentiation were not tested. Do not use this data to dismiss orchestration for complex work.

---

## CRISPY: Structured Phase Decomposition (RPI Evolution)

**Source**: Dexter Horthy / Human Layer (Tier B, Authority 4/5)

CRISPY is the evolution of Research-Plan-Implement (RPI). Where RPI used 3 phases with 85+ instruction mega-prompts, CRISPY splits into 7 phases with each phase under 40 instructions.

**The 7 Phases**:
1. **Questions** — Surface unknowns before committing to a direction
2. **Research** — Gather codebase context and domain knowledge
3. **Design** — Produce a 200-line design doc (the key alignment artifact)
4. **Structure** — Define component boundaries and interfaces
5. **Plan** — Generate implementation steps (vertical slices, not horizontal layers)
6. **Work** — Execute implementation
7. **Implement + PR** — Finalize and submit

**Key principles**:
- "Don't use prompts for control flow; use control flow for control flow" — each phase is a discrete step, not a section within a mega-prompt
- Design doc (200 lines) replaces plan review (1000 lines) as the human-agent alignment artifact
- Vertical planning enforced: models default to horizontal (all DB, then all services, then all API), which produces untestable 1200+ line plans; vertical slicing creates testable checkpoints

**Relationship to other patterns**:
- Replaces RPI's monolithic approach with discrete, manageable phases
- Compatible with any orchestration layer (native subagents, GSD, CAII)
- The design doc pattern is independently useful regardless of phase adoption

---

## Coverage Analysis: What ECC Covers vs. Unique Value

Based on analysis of [everything-claude-code](https://github.com/anthropics-solutions/everything-claude-code) (110K stars):

| Topic | ECC Coverage | This Document's Unique Value |
|-------|-------------|------------------------------|
| Native subagent API | IMPLEMENTED (125+ skills) | None — defer to ECC |
| GSD pattern | MENTIONED (reference) | Comparative analysis, when-to-use framework |
| CAII pattern | ABSENT | Only comparative documentation available |
| Agent teams | MENTIONED | Decision framework for teams vs subagents |
| Advisor strategy | ABSENT | Comparative positioning vs sub-agents and tiered models |
| Managed Agents | ABSENT | Deployment layer analysis, operational gotchas |
| Routines | ABSENT | Event-driven execution pattern documentation |
| CRISPY / RPI evolution | ABSENT | Phase decomposition comparison, design doc pattern |
| Measured overhead | ABSENT | Empirical cost data with caveats |
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
- Anthropic: Advisor strategy, Managed Agents, Routines (April 2026)

**Tier B (Validated)**:
- [glittercowboy/get-shit-done](https://github.com/glittercowboy/get-shit-done) — GSD orchestration
- [skribblez2718/caii](https://github.com/skribblez2718/caii) — CAII cognitive agents
- Google TTD-DR Paper — Self-Evolution Algorithm
- Dexter Horthy / Human Layer: CRISPY methodology, design doc pattern (Authority 4/5)

**Tier C (Low Confidence)**:
- Chase AI: Measured orchestration overhead benchmarks (Authority 2/5, single task type only)

## Related Analysis

- [Harness Engineering](./harness-engineering.md) — Orchestration is one layer of the broader harness stack; see the 6-layer model and diagnostic framework
- [Agent-Driven Development](./agent-driven-development.md) — Parallel agent strategies and specialized agent design (finding-reviewer case study) from production repos

---

*Merged from: gsd-orchestration.md, cognitive-agent-infrastructure.md, subagent-orchestration.md, recursive-evolution.md*
*Last updated: April 2026*

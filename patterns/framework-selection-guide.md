# Framework Selection Guide

**Purpose**: Help users choose the right orchestration approach for their Claude Code projects
**Evidence Tier**: A/B (Synthesized from validated patterns and production implementations)

## The Key Insight

The frameworks documented in this repository aren't competing—they operate at **different levels**:

| Level | Question | Options |
|-------|----------|---------|
| **Methodology** | WHAT phases to follow? | SDD (Spec-Driven Development) |
| **Orchestration** | HOW to coordinate agents? | Native Subagent, GSD, CAII |
| **Execution** | WITH WHAT tools? | Skills, Hooks, MCP |

**SDD is always foundational.** The orchestration choice depends on project characteristics.

---

## Quick Decision Tree

```
START
  │
  ▼
Is this a simple, single-session task?
  │
  ├─YES──► Use NATIVE SUBAGENT ORCHESTRATION (Default)
  │        • Explore, Plan, general-purpose subagent types
  │        • Built into Claude Code, zero setup
  │        • See: patterns/subagent-orchestration.md
  │
  ▼
  NO
  │
  ▼
Do you need state persistence across sessions?
  │
  ├─YES──► Use GSD ORCHESTRATION
  │        • STATE.md for cross-session memory
  │        • Fresh context per executor (prevents rot)
  │        • .planning/ directory structure
  │        • See: patterns/gsd-orchestration.md
  │
  ▼
  NO
  │
  ▼
Are you building a reusable agent architecture?
  │
  ├─YES──► Use CAII COGNITIVE AGENTS
  │        • 7 fixed agents (constant complexity)
  │        • Deterministic orchestration
  │        • Learning & memory capture
  │        • See: patterns/cognitive-agent-infrastructure.md
  │
  ▼
  NO
  │
  ▼
Do you need 60+ specialized agents at enterprise scale?
  │
  ├─YES──► REFERENCE Claude-Flow (don't implement directly)
  │        • Vector memory, swarm topologies
  │        • Enterprise complexity—overkill for most
  │        • See: SOURCES.md (reference only)
  │
  ▼
  NO
  │
  ▼
Use NATIVE SUBAGENT ORCHESTRATION (Default)
```

---

## Framework Comparison

| Framework | Agent Model | Context Strategy | State Management | Evidence |
|-----------|-------------|------------------|------------------|----------|
| **Native Subagent** | 1 parent + N subagents | Accumulating | Conversation history | Tier A |
| **GSD** | ~5 workflow agents | Fresh per subagent | STATE.md + .planning/ | Tier B |
| **CAII** | 7 cognitive agents | On-the-fly injection | Task-specific memories | Tier B |
| **Claude-Flow** | 60+ specialized | Vector retrieval | ReasoningBank | Tier B (docs only) |

---

## Detailed Guidance

### Native Subagent Orchestration (DEFAULT)

**When to use**: Most Claude Code work

**Characteristics**:
- Built-in subagent types: `Explore`, `Plan`, `general-purpose`
- Zero infrastructure required
- Works with standard Claude Code features

**Best for**:
- Single-session development tasks
- Code exploration and understanding
- Standard feature implementation
- Bug fixes and refactoring

**Validated by**: H-CLAUDE-CODE-01 through H-CLAUDE-CODE-04 (all validated)

**Documentation**: [Subagent Orchestration](./subagent-orchestration.md)

---

### GSD Orchestration

**When to use**: Complex, multi-session projects requiring continuity

**Key Innovation**: Fresh context per executor prevents quality degradation

```
Traditional: Context accumulates → Quality degrades
GSD: Each executor gets fresh 200K → Consistent quality
```

**Best for**:
- Multi-day features spanning sessions
- Team handoffs (STATE.md provides complete context)
- Projects with complex dependencies
- When you notice quality degrading in long sessions

**Key Artifacts**:
- `STATE.md` - Current position, decisions, blockers
- `.planning/` - Research, plans, summaries
- XML task specifications with embedded verification

**Documentation**: [GSD Orchestration](./gsd-orchestration.md)

---

### CAII Cognitive Agents

**When to use**: Building scalable, maintainable agent architectures

**Key Innovation**: 7 fixed agents by cognitive function, not domain

```
Domain-specific: N agents (grows with scope) → Maintenance nightmare
CAII: 7 agents (constant) → Sustainable architecture
```

**The 7 Cognitive Agents**:
1. **Clarification** - Transforms ambiguity into specs
2. **Research** - Gathers domain knowledge
3. **Analysis** - Decomposes problems
4. **Synthesis** - Integrates findings
5. **Generation** - Creates artifacts (TDD)
6. **Validation** - Verifies quality
7. **Memory** - Monitors progress, captures learnings

**Best for**:
- Teams building reusable agent systems
- Projects requiring deterministic orchestration
- Long-term systems that need to improve over time

**Bonus**: The [Johari Window](./johari-window-ambiguity.md) methodology (from CAII) is valuable for ANY framework

**Documentation**: [Cognitive Agent Infrastructure](./cognitive-agent-infrastructure.md)

---

### Claude-Flow (Reference Only)

**When to use**: Almost never directly—reference for enterprise patterns

**Why reference only**:
- 60+ agents is extreme complexity
- Performance claims unverified (250% extension)
- Vector memory and swarm topologies are advanced
- No production validation data

**When to reference**:
- Designing enterprise-scale agent systems
- Researching advanced orchestration patterns
- Evaluating swarm topology options

**Documentation**: SOURCES.md (no dedicated pattern file—intentionally)

---

## How Frameworks Map to SDD Phases

All orchestration frameworks implement the SDD 4-phase model differently:

| SDD Phase | Native Subagent | GSD | CAII |
|-----------|-----------------|-----|------|
| **Specify** | CLAUDE.md, skills | STATE.md, .planning/ | Clarification agent |
| **Plan** | Plan subagent | Research + PLAN.md | Research + Analysis agents |
| **Tasks** | TodoWrite, JSON files | XML task specs | Synthesis agent |
| **Implement** | Explore/general-purpose | Fresh executors | Generation + Validation agents |

---

## Common Mistakes

### ❌ Choosing Framework Before Understanding Problem

**Mistake**: "I'll use GSD because it sounds powerful"
**Reality**: Native subagents handle 80% of work; GSD adds overhead
**Fix**: Start with native; upgrade when you hit specific friction

### ❌ Implementing Claude-Flow Patterns Directly

**Mistake**: "Let me build 60 specialized agents"
**Reality**: Enterprise complexity for most projects is overkill
**Fix**: Reference Claude-Flow for ideas; implement simpler frameworks

### ❌ Mixing Frameworks Arbitrarily

**Mistake**: Using CAII's 7 agents inside GSD's workflow phases
**Reality**: Frameworks have internal consistency; mixing creates confusion
**Fix**: Choose one orchestration approach; extract universally useful patterns (like Johari Window)

### ❌ Ignoring the Default

**Mistake**: Always reaching for complex orchestration
**Reality**: Native subagent + good CLAUDE.md handles most needs
**Fix**: Prove you need more before adding complexity

---

## Universally Useful Patterns

Some patterns extracted from these frameworks work with ANY orchestration:

| Pattern | Origin | Universal Value |
|---------|--------|-----------------|
| [Johari Window](./johari-window-ambiguity.md) | CAII | Surface unknowns before implementation |
| [STATE.md](./gsd-orchestration.md#the-statemd-pattern) | GSD | Cross-session memory (even without full GSD) |
| [Progressive Disclosure](./progressive-disclosure.md) | Production | Token efficiency for all frameworks |
| [Atomic Commits](./gsd-orchestration.md#atomic-commits-pattern) | GSD | One task = one commit (good practice anyway) |

---

## Framework Selection by Project Type

| Project Type | Recommended | Why |
|--------------|-------------|-----|
| **Bug fix** | Native Subagent | Simple, low overhead |
| **Small feature (<1 day)** | Native Subagent | No session continuity needed |
| **Medium feature (1-3 days)** | Native or GSD | GSD if quality degradation noticed |
| **Large feature (1+ week)** | GSD | STATE.md essential for continuity |
| **Building agent tools** | CAII | Scalable architecture matters |
| **Research project** | Native + Johari | Johari for ambiguity; native for execution |
| **Team collaboration** | GSD | STATE.md enables handoffs |

---

## Related Patterns

- [Spec-Driven Development](./spec-driven-development.md) - The foundational methodology (always use)
- [Subagent Orchestration](./subagent-orchestration.md) - Default orchestration patterns
- [GSD Orchestration](./gsd-orchestration.md) - Multi-session, fresh context patterns
- [Cognitive Agent Infrastructure](./cognitive-agent-infrastructure.md) - Scalable agent architecture
- [Context Engineering](./context-engineering.md) - Context strategies for all frameworks
- [MCP vs Skills Economics](./mcp-vs-skills-economics.md) - Execution layer decisions

---

## Summary

1. **SDD is always foundational** - All frameworks implement its 4 phases
2. **Native Subagent is the default** - Zero setup, handles 80% of work
3. **GSD for session continuity** - STATE.md when projects span sessions
4. **CAII for agent architecture** - When building reusable agent systems
5. **Claude-Flow for reference only** - Enterprise patterns, don't implement directly

**When in doubt**: Start with Native Subagent. Add complexity only when you feel specific friction.

---

*Last updated: January 2026*

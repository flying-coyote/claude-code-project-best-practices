# Cognitive Agent Infrastructure (CAII)

**Source**: [skribblez2718/caii](https://github.com/skribblez2718/caii) (Kristoffer Sketch)
**Evidence Tier**: B (Production implementation, documented methodology)

## Overview

CAII (Cognitive Agent Infrastructure Implementation) organizes agents by **cognitive function** rather than domain specialization. Instead of proliferating domain-specific agents, it uses **7 fixed cognitive agents** that receive context on-the-fly, adapting to any domain without modification.

**SDD Phase**: Cross-phase orchestration (alternative to domain-specific agent proliferation)

> "As the system grows, so would the number of task-specific agents, and so would the overhead in maintaining them."
> — CAII Documentation

---

## The Core Problem

### Domain-Specific Agent Proliferation

Traditional approach: Create specialized agents for each domain.

```
Traditional Architecture (Domain-Specific):
├── TQL Developer Agent
├── Documentation Agent
├── Test Writer Agent
├── Security Auditor Agent
├── Code Reviewer Agent
├── Deploy Agent
└── ... (N grows with project scope)
```

**Problems**:
- Agent count grows with project scope
- Maintenance overhead scales linearly
- Overlapping capabilities between agents
- Inconsistent interfaces and behaviors

### CAII's Alternative: Cognitive Functions

CAII approach: Fixed agents organized by **how** they think, not **what** they work on.

```
CAII Architecture (Cognitive Functions):
├── Clarification Agent    → Transforms ambiguity into specs
├── Research Agent         → Gathers domain knowledge
├── Analysis Agent         → Decomposes problems
├── Synthesis Agent        → Integrates findings
├── Generation Agent       → Creates artifacts
├── Validation Agent       → Verifies quality
└── Memory/Metacognition   → Monitors progress

Total: 7 agents (constant, regardless of domain)
```

---

## The Seven Cognitive Agents

### 1. Clarification Agent

**Purpose**: Transform ambiguous inputs into actionable specifications

**When Active**: Task begins, requirements unclear

**Outputs**:
- Refined task specification
- Success criteria
- Constraints and assumptions

**Integration**: Uses [Johari Window](./johari-window-ambiguity.md) methodology for surfacing unknowns.

### 2. Research Agent

**Purpose**: Investigate options and gather domain knowledge

**When Active**: Domain knowledge needed, options to evaluate

**Outputs**:
- Domain context
- Available options with trade-offs
- Relevant prior work

### 3. Analysis Agent

**Purpose**: Decompose problems and assess complexity

**When Active**: Problem understood, need implementation approach

**Outputs**:
- Problem decomposition
- Complexity assessment
- Dependency mapping
- Risk identification

### 4. Synthesis Agent

**Purpose**: Integrate findings into coherent recommendations

**When Active**: Multiple inputs need integration

**Outputs**:
- Integrated recommendations
- Reconciled conflicts
- Prioritized approach

### 5. Generation Agent

**Purpose**: Create artifacts using test-driven development

**When Active**: Specifications complete, ready to implement

**Outputs**:
- Code, documentation, or other artifacts
- Tests (written before implementation)
- Atomic, verifiable changes

### 6. Validation Agent

**Purpose**: Verify artifacts against quality criteria

**When Active**: Artifacts created, need verification

**Outputs**:
- Test results
- Quality assessment
- Issues and remediation steps

### 7. Memory/Metacognition Agent

**Purpose**: Monitor progress and detect impasses

**When Active**: Continuously during workflow

**Outputs**:
- Progress tracking
- Impasse detection
- Learning capture
- Context management

---

## Deterministic Orchestration

CAII uses **Python orchestration** to enforce protocol adherence, not LLM prompting alone.

### The Problem with Pure LLM Orchestration

```
Prompt-Based Orchestration:
"Follow these steps: 1, 2, 3, 4..."

Reality: LLM may skip steps, reorder, or interpret differently each run
```

### CAII's Solution: State Machine Enforcement

```python
# Simplified CAII orchestration concept
class CognitiveWorkflow:
    states = [
        "clarification",
        "research",
        "analysis",
        "synthesis",
        "generation",
        "validation"
    ]

    def execute(self, task):
        for state in self.states:
            agent = self.get_agent(state)
            result = agent.process(task, self.context)
            self.context.update(result)

            # Deterministic: MUST complete state before advancing
            if not result.complete:
                return self.handle_impasse(state, result)

        return self.context.final_output
```

**Key Principle**: "Uses Python to prompt the LLM one step at a time, strictly following a given protocol."

**Benefit**: "The non-deterministic nature of AI will execute a given step slightly differently each time, but by enforcing the same process we gain more consistency and transparency."

---

## Learning & Memory System

### Task-Specific Memories

Each task generates memory files organized by cognitive function:

```
.claude/memory/
├── task-001-clarification-memory.md
├── task-001-research-memory.md
├── task-001-analysis-memory.md
└── ...
```

### The `/learn` Command

After workflow completion, `/learn` transforms experiences into reusable learnings:

```markdown
## Learning Entry: TQL Pipeline Pattern

### Cognitive Function: Generation

### Context
Task: Create data transformation pipeline
Domain: TQL (Tenzir Query Language)

### Learning
When generating TQL pipelines:
1. Start with source → sink skeleton
2. Add transformations incrementally
3. Validate each stage before adding next
4. Use `test_pipeline` after each transformation

### Applicability
- TQL development
- Similar: SQL pipelines, data transformations
```

### Increasing Autonomy Over Time

CAII demonstrates progressive learning through two mechanisms:

**1. Chunking** (Inspired by Soar architecture):
- Complex multi-step reasoning patterns
- Convert to automatic/reactive processing over time
- Reduce cognitive load for repeated patterns

**2. Learnings Integration**:
- Captured insights reference automatically
- Less instruction needed for similar tasks
- System "requires less instruction over time"

---

## Comparison: CAII vs GSD vs Domain-Specific

| Aspect | Domain-Specific | GSD | CAII |
|--------|-----------------|-----|------|
| **Agent Count** | N (grows) | ~5 | 7 (fixed) |
| **Organization** | By domain | By workflow phase | By cognitive function |
| **Maintenance** | High (grows) | Medium | Low (constant) |
| **Context Strategy** | Specialized | Fresh per subagent | On-the-fly injection |
| **Learning** | Per-agent | STATE.md | Task-specific memories |
| **Orchestration** | Various | Human checkpoints | Deterministic state machine |

### When to Choose Each

| Scenario | Recommended Approach |
|----------|---------------------|
| **Deep domain specialization needed** | Domain-Specific |
| **Multi-phase projects with sessions** | GSD |
| **Scalable, maintainable architecture** | CAII |
| **Rapid prototyping** | GSD or Domain-Specific |
| **Long-term autonomous operation** | CAII |

---

## Implementation in Claude Code

### Mapping Cognitive Agents to Subagent Types

| Cognitive Agent | Claude Code Mapping |
|-----------------|---------------------|
| Clarification | Custom skill + AskUserQuestion |
| Research | `Explore` subagent |
| Analysis | `Plan` subagent |
| Synthesis | `general-purpose` subagent |
| Generation | `general-purpose` subagent |
| Validation | `Explore` subagent (verification focus) |
| Memory | Hooks + external files |

### Orchestration via Skills

Create a CAII orchestrator skill:

```yaml
---
name: caii-orchestrator
description: Cognitive Agent Infrastructure workflow orchestration
trigger: Complex multi-step tasks requiring systematic approach
---

# CAII Orchestrator

## When to Use
- Tasks with unclear requirements (need Clarification)
- Tasks requiring research (need Research)
- Tasks with multiple approaches (need Analysis + Synthesis)
- Tasks requiring artifacts (need Generation + Validation)

## Workflow

### Phase 1: Clarification
Apply Johari Window methodology:
- Map Arena (shared understanding)
- Surface Hidden (user context)
- Share Blind Spots (technical considerations)
- Identify Unknown (uncertainties)

### Phase 2: Research
Spawn Explore subagent:
- Gather domain context
- Identify options and trade-offs
- Find relevant prior work

### Phase 3: Analysis
Spawn Plan subagent:
- Decompose problem
- Assess complexity
- Map dependencies
- Identify risks

### Phase 4: Synthesis
Integrate findings:
- Reconcile conflicts between research and analysis
- Prioritize approach
- Create recommendations

### Phase 5: Generation
Create artifacts:
- Write tests first (TDD)
- Implement incrementally
- Atomic commits

### Phase 6: Validation
Verify quality:
- Run tests
- Check against success criteria
- Document issues

### Memory Capture
After completion:
- Capture learnings per cognitive function
- Update memory files
- Reference in future similar tasks
```

---

## Anti-Patterns

### ❌ Skipping Cognitive Phases

**Problem**: Jumping from clarification directly to generation
**Symptom**: Rework, missed requirements, quality issues
**Solution**: Trust the sequence—each phase builds on previous

### ❌ Domain-Specific Agent Creep

**Problem**: Adding agents for each new domain
**Symptom**: Growing maintenance burden, inconsistent behavior
**Solution**: Inject domain context, don't create new agents

### ❌ Pure LLM Orchestration

**Problem**: Relying only on prompts to enforce workflow
**Symptom**: Inconsistent step execution, skipped phases
**Solution**: Deterministic state machine with explicit transitions

### ❌ Ignoring Memory Capture

**Problem**: Not capturing learnings after workflows
**Symptom**: Same mistakes repeated, no improvement over time
**Solution**: Always run learning capture after significant tasks

---

## Integration with Other Patterns

| Pattern | Integration |
|---------|-------------|
| **Johari Window** | Clarification agent uses SAAE protocol |
| **GSD Orchestration** | Complementary: GSD for session structure, CAII for cognitive workflow |
| **Session Learning** | Memory/Metacognition agent implements session learning |
| **Subagent Orchestration** | Maps cognitive agents to subagent types |

---

## When NOT to Use CAII

| Scenario | Why Skip CAII |
|----------|---------------|
| **Simple, well-defined tasks** | Overhead exceeds benefit |
| **Single-step operations** | No cognitive decomposition needed |
| **Time-critical tasks** | Multi-phase workflow adds latency |
| **Already have working domain agents** | Don't fix what works |

---

## Summary

CAII offers an alternative to domain-specific agent proliferation:

| Benefit | Description |
|---------|-------------|
| **Constant complexity** | 7 agents regardless of domain scope |
| **Maintainability** | Update cognitive functions, not domain agents |
| **Consistency** | Deterministic orchestration ensures process fidelity |
| **Learning** | System improves over time with memory capture |
| **Adaptability** | Inject domain context without creating new agents |

**Rule of Thumb**: Use CAII when you need scalable, maintainable multi-agent architecture that improves over time.

---

## Related Patterns

- [Johari Window](./johari-window-ambiguity.md) - Used by Clarification agent
- [GSD Orchestration](./gsd-orchestration.md) - Complementary orchestration approach
- [Subagent Orchestration](./subagent-orchestration.md) - Foundation for agent mapping
- [Session Learning](./session-learning.md) - Memory/Metacognition implementation

---

## Sources

**Primary (Tier B)**:
- [skribblez2718/caii](https://github.com/skribblez2718/caii) - Cognitive Agent Infrastructure Implementation

**Theoretical Foundation**:
- Soar Cognitive Architecture (chunking mechanism)
- Johari Window (Luft & Ingham, 1955)

*Last updated: January 2026*

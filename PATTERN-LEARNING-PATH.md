# Pattern Learning Path

**Purpose**: Guided reading sequence for 34 patterns to reduce overwhelm and provide clear learning progression

---

## Overview

This repository documents 34 implementation patterns. **You don't need all of them.** This guide helps you:

1. Start with essential foundations (everyone)
2. Choose a path based on your role/goals
3. Add patterns as you encounter specific problems

**Estimated reading times**:
- **Start Here** (Everyone): 45 minutes
- **Role-Specific Paths**: 1-2 hours each
- **Complete catalog**: 6-8 hours

---

## Start Here (Everyone)

Read these 3 patterns first. They're foundational - everything else builds on them.

### 1. [FOUNDATIONAL-PRINCIPLES.md](FOUNDATIONAL-PRINCIPLES.md)
**The Big 3 principles: Keep CLAUDE.md minimal (~60 lines), Plan first (always), Context engineering > Prompt engineering**

**Why first**: These are non-negotiable. Violating these causes most problems.

**Time**: 15 minutes

**Key takeaway**: "Would removing this cause mistakes? If not, cut it."

---

### 2. [Context Engineering](patterns/context-engineering.md)
**Specs as deterministic context; external artifacts as agent memory**

**Why second**: Foundation for how Claude Code works. Context over prompts.

**Time**: 15 minutes

**Key takeaway**: Correctness trumps compression. Use external artifacts (specs, docs, git) as persistent context.

---

### 3. [Spec-Driven Development](patterns/spec-driven-development.md)
**4-phase model: Specify → Plan → Tasks → Implement**

**Why third**: The methodology that organizes all other patterns.

**Time**: 15 minutes

**Key takeaway**: Planning effort directly improves output quality (2-3x).

---

**After reading these 3**: You understand the principles. Now choose your path based on role or need.

---

## Learning Paths by Role

### Path A: Solo Developer

**Goal**: Maximize personal productivity with Claude Code

**Sequence** (1-2 hours):
1. ✅ **Foundation**: Complete "Start Here" section above
2. [Project Infrastructure](patterns/project-infrastructure.md) - Tiered setup (5/15/30 min)
3. [Long-Running Agent](patterns/long-running-agent.md) - Work across sessions
4. [Progressive Disclosure](patterns/progressive-disclosure.md) - Skill architecture (73% token savings)
5. [Advanced Hooks](patterns/advanced-hooks.md) - Quality gates (formatting, linting)
6. [Parallel Sessions](patterns/parallel-sessions.md) - 5+ sessions for parallel work

**Optional additions**:
- [Agentic Retrieval](patterns/agentic-retrieval.md) - Better code navigation
- [Confidence Scoring](patterns/confidence-scoring.md) - Assess AI outputs
- [Tool Ecosystem](patterns/tool-ecosystem.md) - When to use Claude Code vs alternatives

**Outcome**: Productive solo workflow with quality infrastructure

---

### Path B: Team Lead / Engineering Manager

**Goal**: Establish team standards and best practices

**Sequence** (1-2 hours):
1. ✅ **Foundation**: Complete "Start Here" section above
2. [Project Infrastructure](patterns/project-infrastructure.md) - Team standardization approach
3. [Evidence Tiers](patterns/evidence-tiers.md) - Dual tier system for claims (A-D + 1-5)
4. [Documentation Maintenance](patterns/documentation-maintenance.md) - ARCH/PLAN/INDEX trio
5. [Architecture Decision Records](patterns/architecture-decision-records.md) - Document why
6. [Agent Evaluation](patterns/agent-evaluation.md) - Measure what you're improving

**Optional additions**:
- [Plugins and Extensions](patterns/plugins-and-extensions.md) - When Skills vs MCP vs Hooks
- [Framework Selection Guide](patterns/framework-selection-guide.md) - Choose orchestration
- [MCP vs Skills Economics](patterns/mcp-vs-skills-economics.md) - Cost tradeoffs

**Outcome**: Evidence-based team standards with clear documentation

---

### Path C: Production / Security Focus

**Goal**: Deploy AI coding tools safely at scale

**Sequence** (1-2 hours):
1. ✅ **Foundation**: Complete "Start Here" section above
2. [Safety and Sandboxing](patterns/safety-and-sandboxing.md) - OS-level isolation
3. [MCP Patterns](patterns/mcp-patterns.md) - 7 failure modes + OWASP security
4. [Agent Principles](patterns/agent-principles.md) - 6 principles for reliability
5. [Agent Evaluation](patterns/agent-evaluation.md) - Testing and validation
6. [Advanced Hooks](patterns/advanced-hooks.md) - Pre/PostToolUse quality gates

**Optional additions**:
- [Secure Code Generation](patterns/secure-code-generation.md) - Prevent vulnerabilities
- [Memory Architecture](patterns/memory-architecture.md) - Information lifecycle
- [Session Learning](patterns/session-learning.md) - Improve over time

**Outcome**: Secure, reliable AI coding infrastructure

---

### Path D: Researcher / Experimenter

**Goal**: Understand cutting-edge patterns and orchestration

**Sequence** (2-3 hours):
1. ✅ **Foundation**: Complete "Start Here" section above
2. [Framework Selection Guide](patterns/framework-selection-guide.md) - Native vs GSD vs CAII
3. [GSD Orchestration](patterns/gsd-orchestration.md) - Fresh context per subagent
4. [Cognitive Agent Infrastructure](patterns/cognitive-agent-infrastructure.md) - 7 cognitive agents
5. [Recursive Context Management](patterns/recursive-context-management.md) - Programmatic self-examination
6. [Recursive Evolution](patterns/recursive-evolution.md) - Self-Evolution Algorithm

**Optional additions**:
- [Johari Window Ambiguity](patterns/johari-window-ambiguity.md) - Surface hidden assumptions
- [Advanced Tool Use](patterns/advanced-tool-use.md) - Tool search, programmatic calling
- [AI Image Generation](patterns/ai-image-generation.md) - Visual asset pipelines

**Outcome**: Deep understanding of orchestration approaches

---

## Learning Paths by Use Case

### Use Case 1: "I'm setting up a new project"

**Quick path** (30 minutes):
1. [FOUNDATIONAL-PRINCIPLES.md](FOUNDATIONAL-PRINCIPLES.md) - The Big 3
2. [Project Infrastructure](patterns/project-infrastructure.md) - Tiered setup
3. Use [BOOTSTRAP-NEW-PROJECT.md](prompts/BOOTSTRAP-NEW-PROJECT.md) with preset

**Then add as needed**:
- [Context Engineering](patterns/context-engineering.md) - If CLAUDE.md grows
- [Documentation Maintenance](patterns/documentation-maintenance.md) - For ARCH/PLAN/INDEX

---

### Use Case 2: "I want to improve my existing Claude Code setup"

**Quick path** (45 minutes):
1. [FOUNDATIONAL-PRINCIPLES.md](FOUNDATIONAL-PRINCIPLES.md) - Audit against The Big 3
2. [Project Infrastructure](patterns/project-infrastructure.md) - Compare to Tier 1/2/3
3. Use [AUDIT-EXISTING-PROJECT.md](prompts/AUDIT-EXISTING-PROJECT.md)
4. [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - Address specific issues

**Then add gaps**:
- Missing hooks → [Advanced Hooks](patterns/advanced-hooks.md)
- Bloated CLAUDE.md → [Context Engineering](patterns/context-engineering.md)
- No planning process → [Spec-Driven Development](patterns/spec-driven-development.md)

---

### Use Case 3: "I'm working on complex multi-session features"

**Quick path** (1 hour):
1. [Long-Running Agent](patterns/long-running-agent.md) - External artifacts as memory
2. [Spec-Driven Development](patterns/spec-driven-development.md) - Specify → Plan → Tasks → Implement
3. [Documentation Maintenance](patterns/documentation-maintenance.md) - ARCH/PLAN/INDEX
4. [Progressive Disclosure](patterns/progressive-disclosure.md) - Manage large skills

**Then optimize**:
- [Memory Architecture](patterns/memory-architecture.md) - 4-tier lifecycle
- [Session Learning](patterns/session-learning.md) - Capture corrections

---

### Use Case 4: "I need to choose between MCP, Skills, or Hooks"

**Quick path** (45 minutes):
1. [Plugins and Extensions](patterns/plugins-and-extensions.md) - Decision framework
2. [MCP vs Skills Economics](patterns/mcp-vs-skills-economics.md) - Cost/performance tradeoffs
3. [MCP Patterns](patterns/mcp-patterns.md) - Failure modes + security
4. [Progressive Disclosure](patterns/progressive-disclosure.md) - Skill architecture
5. [Advanced Hooks](patterns/advanced-hooks.md) - Quality gates

**Outcome**: Clear decision on extension approach

---

### Use Case 5: "I'm building custom AI workflows"

**Deep path** (2-3 hours):
1. [Framework Selection Guide](patterns/framework-selection-guide.md) - Choose orchestration
2. [GSD Orchestration](patterns/gsd-orchestration.md) OR [Cognitive Agent Infrastructure](patterns/cognitive-agent-infrastructure.md)
3. [Agent Principles](patterns/agent-principles.md) - Reliability principles
4. [Agent Evaluation](patterns/agent-evaluation.md) - Testing patterns
5. [Advanced Tool Use](patterns/advanced-tool-use.md) - Programmatic calling

**Advanced**:
- [Recursive Evolution](patterns/recursive-evolution.md) - Self-improvement
- [Recursive Context Management](patterns/recursive-context-management.md) - Advanced inference

---

## Complete Pattern Catalog (By Phase)

Once you've completed a learning path, you can explore the full catalog organized by SDD phase:

### Foundational (2 patterns)
- [Spec-Driven Development](patterns/spec-driven-development.md) ✅ Start Here
- [Framework Selection Guide](patterns/framework-selection-guide.md)

### Specify Phase (4 patterns)
- [Context Engineering](patterns/context-engineering.md) ✅ Start Here
- [Memory Architecture](patterns/memory-architecture.md)
- [Johari Window Ambiguity](patterns/johari-window-ambiguity.md)
- [Project Infrastructure](patterns/project-infrastructure.md)

### Plan Phase (3 patterns)
- [Documentation Maintenance](patterns/documentation-maintenance.md)
- [Architecture Decision Records](patterns/architecture-decision-records.md)
- [Evidence Tiers](patterns/evidence-tiers.md)

### Tasks + Implement Phase (7 patterns)
- [Long-Running Agent](patterns/long-running-agent.md)
- [Progressive Disclosure](patterns/progressive-disclosure.md)
- [Advanced Hooks](patterns/advanced-hooks.md)
- [Advanced Tool Use](patterns/advanced-tool-use.md)
- [Agentic Retrieval](patterns/agentic-retrieval.md)
- [Parallel Sessions](patterns/parallel-sessions.md)
- [AI Image Generation](patterns/ai-image-generation.md)

### Cross-Phase (18 patterns)
- [Agent Principles](patterns/agent-principles.md)
- [Agent Evaluation](patterns/agent-evaluation.md)
- [MCP Patterns](patterns/mcp-patterns.md)
- [MCP vs Skills Economics](patterns/mcp-vs-skills-economics.md)
- [Plugins and Extensions](patterns/plugins-and-extensions.md)
- [Safety and Sandboxing](patterns/safety-and-sandboxing.md)
- [GSD Orchestration](patterns/gsd-orchestration.md)
- [Cognitive Agent Infrastructure](patterns/cognitive-agent-infrastructure.md)
- [Recursive Context Management](patterns/recursive-context-management.md)
- [Session Learning](patterns/session-learning.md)
- [Confidence Scoring](patterns/confidence-scoring.md)
- [Recursive Evolution](patterns/recursive-evolution.md)
- [Tool Ecosystem](patterns/tool-ecosystem.md)
- [Secure Code Generation](patterns/secure-code-generation.md)
- [Subagent Orchestration](patterns/subagent-orchestration.md)
- [Execution Management](patterns/execution-management.md)
- [Verification and Testing](patterns/verification-and-testing.md)
- [Quality Metrics](patterns/quality-metrics.md)

---

## How to Use This Guide

### For Quick Reference
1. Identify your situation (role or use case)
2. Follow the recommended sequence
3. Add optional patterns as problems arise

### For Comprehensive Learning
1. Complete "Start Here" (3 patterns)
2. Read all patterns in your primary path
3. Skim patterns from other paths
4. Deep-dive when you encounter specific needs

### For Team Onboarding
1. Share "Start Here" (required reading)
2. Assign role-specific paths
3. Meet to discuss FOUNDATIONAL-PRINCIPLES.md
4. Reference other patterns as needed

---

## Pattern Dependencies

Some patterns reference others. This diagram shows major dependencies:

```
FOUNDATIONAL-PRINCIPLES (The Big 3)
    ↓
Context Engineering
    ↓
Spec-Driven Development
    ↓
    ├─→ Project Infrastructure → Advanced Hooks
    ├─→ Long-Running Agent → Documentation Maintenance
    ├─→ Progressive Disclosure → Plugins and Extensions
    └─→ Agent Principles → Agent Evaluation

Framework Selection Guide
    ↓
    ├─→ GSD Orchestration
    ├─→ Cognitive Agent Infrastructure
    └─→ (Native Claude Code patterns)
```

**Reading tip**: If a pattern references another, read the referenced pattern first.

---

## Maintenance Note

This learning path is a guide, not a mandate. Patterns are:
- **Descriptive** (what works), not prescriptive (what you must do)
- **Evidence-based** (see SOURCES.md for attribution)
- **Evolvable** (new patterns added as practices emerge)

Start with foundations, add as needed, adapt to your context.

---

**Last Updated**: February 2026
**Pattern Count**: 34
**See Also**: [INDEX.md](INDEX.md) (complete file listing), [TROUBLESHOOTING.md](TROUBLESHOOTING.md) (common issues)

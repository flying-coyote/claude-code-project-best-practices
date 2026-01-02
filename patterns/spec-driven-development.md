# Spec-Driven Development: The Foundational Methodology

**Source**: [GitHub Spec Kit](https://github.com/github/spec-kit) (59K+ stars), [agentskills.io](https://agentskills.io) (open standard)
**Evidence Tier**: A (Industry standard - major vendor adoption, cross-platform specification)

## Overview

Spec-driven development (SDD) is the foundational methodology for AI-assisted development. This repository adopts SDD principles, with Claude Code as the primary implementation context.

> "Spec-driven development uses well-crafted software requirement specifications as prompts, aided by AI coding agents, to generate executable code."
> — ThoughtWorks

**This is not an external framework we reference—it's the methodology we implement.**

---

## The 4-Phase Model

All significant work follows this structure (aligned with GitHub Spec Kit):

### Phase 1: Specify
Define **what** to build—requirements and user stories focusing on the "what" and "why."

**Claude Code Implementation:**
- CLAUDE.md for project context
- `specs/` directory for feature requirements
- Slash command: `/specify` to gather requirements

### Phase 2: Plan
Create technical strategy—technology stack, architecture decisions, engineering constraints.

**Claude Code Implementation:**
- ARCHITECTURE.md for system design
- DECISIONS.md for trade-off rationale
- Slash command: `/plan` to create technical design

### Phase 3: Tasks
Generate actionable task lists from the implementation plan.

**Claude Code Implementation:**
- TodoWrite tool for structured task management
- JSON task files for complex features
- PLAN.md for current priorities

### Phase 4: Implement
Execute tasks according to established plan and specifications.

**Claude Code Implementation:**
- Skills for repeatable methodologies
- Hooks for quality gates
- One feature at a time (long-running agent pattern)
- Git commits as checkpoints

---

## How Existing Patterns Implement SDD

| Pattern | SDD Phase | What It Implements |
|---------|-----------|-------------------|
| [Planning-First Development](./planning-first-development.md) | Specify + Plan | "Great Planning is Great Prompting" principle |
| [Context Engineering](./context-engineering.md) | Specify | Specs as deterministic context |
| [Documentation Maintenance](./documentation-maintenance.md) | Plan | ARCH/PLAN/INDEX as spec artifacts |
| [Long-Running Agent](./long-running-agent.md) | Tasks + Implement | External artifacts, one feature at a time |
| [Memory Architecture](./memory-architecture.md) | All phases | Lifecycle-based information management |
| [Progressive Disclosure](./progressive-disclosure.md) | Implement | Token-efficient methodology loading |

---

## Reference Implementations

These frameworks represent proven implementations of SDD:

| Framework | Strength | Use As Reference For |
|-----------|----------|---------------------|
| **[GitHub Spec Kit](https://github.com/github/spec-kit)** | Tool-agnostic 4-phase model | Phase structure, slash commands |
| **[BMAD Method](https://github.com/bmad-code-org/BMAD-METHOD)** | Multi-agent architecture | Agent-as-code, document sharding |
| **[Kiro (AWS)](https://kiro.dev/)** | IDE integration | Agent hooks, spec file structure |
| **[Agent OS](https://github.com/buildermethods/agent-os)** | Customizable workflows | Phase customization |

---

## When to Apply Full SDD Rigor

### Full 4-Phase (Complex Work)

| Scenario | Why |
|----------|-----|
| Features touching multiple files/systems | Specs prevent scope creep |
| Team projects | Shared specifications enable coordination |
| Work spanning multiple sessions | Specs bridge context loss |
| Regulated environments | Specs provide audit trail |

### Lightweight SDD (Simple Work)

| Scenario | Approach |
|----------|----------|
| Bug fixes | Skip to Tasks phase, brief spec in commit message |
| Small features (<1 day) | Combine Specify+Plan, then implement |
| Exploratory prototyping | "Vibe code" first, retrofit specs if keeping |

**Principle**: Scale rigor to complexity. Don't over-specify simple work.

---

## Known Limitations

### Documented Challenges (Be Aware)

1. **Waterfall Risk**: Over-specifying before learning through implementation
2. **Context Window Limits**: Large specs can fragment agent understanding
3. **Natural Language Ambiguity**: AI may interpret specs differently than intended
4. **Instruction Following**: Agents don't always follow all spec details

### Mitigations

| Challenge | Mitigation |
|-----------|------------|
| Waterfall risk | Iterate specs during implementation, not just before |
| Context limits | Progressive disclosure, document sharding (BMAD pattern) |
| Ambiguity | Acceptance criteria, examples, test cases in specs |
| Instruction following | Hooks for enforcement, verification steps |

---

## Implementing SDD in Claude Code

### Option 1: Use Existing Framework

Install a framework like Agent OS or Spec Kit alongside Claude Code:

```bash
# Agent OS
curl -sSL https://buildermethods.com/agent-os/install.sh | bash

# Spec Kit
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

### Option 2: Lightweight Spec Pattern

Create a minimal spec-driven workflow using Claude Code native features:

```
.claude/
├── commands/
│   ├── specify.md      # "/specify" - gather requirements
│   ├── plan.md         # "/plan" - create implementation plan
│   └── implement.md    # "/implement" - execute with context
└── CLAUDE.md           # Reference spec files
```

### Option 3: Skill-Based Spec Workflow

Create a skill that implements spec-driven methodology:

```markdown
---
name: spec-workflow
description: Guides spec-driven development for complex features
---

# Spec-Driven Development Workflow

## When to Activate
Use this workflow when implementing features that:
- Touch multiple files or systems
- Require architectural decisions
- Need team coordination

## Phases

### 1. Specify
Before any code, create `specs/<feature>/requirements.md`:
- User stories with acceptance criteria
- Non-functional requirements
- Out of scope items

### 2. Plan
Create `specs/<feature>/design.md`:
- Technical approach
- File changes needed
- Dependencies and risks

### 3. Implement
Follow the plan, updating specs as needed.
```

---

## Recommendations

### For Simple Projects
Skip formal SDD. Use Claude Code's native patterns:
- CLAUDE.md for context
- One feature at a time
- Git commits as checkpoints

### For Complex Projects
Consider lightweight spec integration:
- Create `/specs` directory
- Require specs for features >1 day effort
- Use specs as session handoff artifacts

### For Enterprise/Team Projects
Evaluate full SDD frameworks:
- BMAD for full lifecycle management
- Spec Kit for GitHub-integrated workflows
- Agent OS for customizable processes

---

## Related Patterns

- [Long-Running Agent](./long-running-agent.md) - External artifacts as memory
- [Context Engineering](./context-engineering.md) - Deterministic vs probabilistic context
- [Documentation Maintenance](./documentation-maintenance.md) - Living documentation patterns

---

## Sources

- [GitHub Spec Kit](https://github.com/github/spec-kit) - 59K+ stars
- [BMAD Method](https://github.com/bmad-code-org/BMAD-METHOD) - MIT licensed
- [Kiro by AWS](https://kiro.dev/) - Spec-driven IDE
- [Agent OS](https://github.com/buildermethods/agent-os) - Spec-driven system
- [ThoughtWorks: Spec-Driven Development](https://www.thoughtworks.com/en-us/insights/blog/agile-engineering-practices/spec-driven-development-unpacking-2025-new-engineering-practices)
- [InfoQ: AWS Kiro](https://www.infoq.com/news/2025/08/aws-kiro-spec-driven-agent/)

*Last updated: January 2026*

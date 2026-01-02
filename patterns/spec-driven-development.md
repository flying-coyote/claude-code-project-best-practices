# Spec-Driven Development for AI Coding Agents

**Source**: [GitHub Spec Kit](https://github.com/github/spec-kit), [ThoughtWorks Analysis](https://www.thoughtworks.com/en-us/insights/blog/agile-engineering-practices/spec-driven-development-unpacking-2025-new-engineering-practices)
**Evidence Tier**: B (Validated secondary - major vendor implementations)

## Overview

Spec-driven development (SDD) emerged in 2025 as one of the most significant AI-assisted engineering practices. It addresses the limitations of "vibe coding" by requiring structured specifications before AI-generated implementation.

> "Spec-driven development uses well-crafted software requirement specifications as prompts, aided by AI coding agents, to generate executable code."
> — ThoughtWorks

---

## The Problem SDD Solves

### Vibe Coding Limitations

When using AI coding agents without structure:
- Inconsistent results across sessions
- Context loss in complex features
- "Works but wrong" implementations
- Difficult to maintain or extend
- Poor team coordination

### SDD Solution

Specifications become the **source of truth**:
- Shared understanding between human and AI
- Reproducible outcomes
- Living documentation that evolves with code
- Team coordination artifact

---

## Major Frameworks (2025)

| Framework | Approach | Best For | Link |
|-----------|----------|----------|------|
| **GitHub Spec Kit** | 4-phase workflow (Specify→Plan→Tasks→Implement) | Individual developers, feature-level | [github/spec-kit](https://github.com/github/spec-kit) |
| **BMAD Method** | Multi-agent team (19+ specialized agents) | Large projects, full lifecycle | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) |
| **Kiro (AWS)** | IDE with specs built-in (requirements.md, design.md, tasks.md) | Greenfield projects | [kiro.dev](https://kiro.dev/) |
| **Agent OS** | Spec-driven system for any AI coding tool | Customizable workflows | [buildermethods/agent-os](https://github.com/buildermethods/agent-os) |

---

## GitHub Spec Kit: The 4-Phase Model

### Phase 1: Specify (`/speckit.specify`)
Define **what** to build—requirements and user stories focusing on the "what" and "why."

### Phase 2: Plan (`/speckit.plan`)
Create technical strategy—technology stack, architecture decisions, engineering constraints.

### Phase 3: Tasks (`/speckit.tasks`)
Generate actionable task lists from the implementation plan.

### Phase 4: Implement (`/speckit.implement`)
Execute tasks according to established plan and specifications.

### Supporting Commands
- **Constitution**: Establish project governing principles
- **Clarify**: Resolve underspecified areas before planning
- **Analyze**: Verify cross-artifact consistency

---

## BMAD Method: Multi-Agent Architecture

### Core Concept
A complete AI "project team" with specialized agents:
- **Analyst Agent**: Research and requirements gathering
- **PM Agent**: Product requirements documents
- **Architect Agent**: System design and tech choices
- **Developer Agent**: Implementation
- **Scrum Master Agent**: Story breakdown and coordination

### Two-Phase Approach
1. **Agentic Planning**: Agents collaborate on PRDs and architecture
2. **Context-Engineered Development**: Hyper-detailed stories with complete context

### Agent-as-Code
Each agent is a self-contained markdown file with embedded YAML configuration—version-controllable and shareable.

---

## When to Use Spec-Driven Development

### Good Fit ✓

| Scenario | Why SDD Helps |
|----------|---------------|
| Complex features | Specs prevent scope creep and context loss |
| Team projects | Shared specifications enable coordination |
| Greenfield development | Clean start benefits from upfront planning |
| Regulated environments | Specs provide audit trail |
| Long-running implementations | External artifacts bridge sessions |

### Poor Fit ✗

| Scenario | Why SDD Struggles |
|----------|-------------------|
| Rapid prototyping | Overhead slows exploration |
| Highly exploratory work | Requirements unknown upfront |
| Small bug fixes | Overkill for simple changes |
| Performance-critical code | Requires human expertise |
| Existing codebases | Retrofitting specs is difficult |

---

## Criticisms and Limitations

### Documented Challenges

1. **Waterfall Concerns**
   > "SDD reminds some of the Waterfall model, which required massive documentation before coding."
   > — [Marmelab Analysis](https://marmelab.com/blog/2025/11/12/spec-driven-development-waterfall-strikes-back.html)

2. **Context Window Limits**
   Large specifications hit context window limits, fragmenting agent understanding.

3. **Natural Language Ambiguity**
   Specs written in natural language face inherent ambiguity—AI may interpret differently than intended.

4. **Instruction Following**
   > "Even with all of these files and templates... agents frequently don't follow all the instructions."
   > — ThoughtWorks

5. **Code Bloat**
   Martin Fowler's experiments: Kiro generated 5,000 lines for a tool that should have been 800 lines.

6. **Team Adoption**
   67% of teams report extra debugging time during learning phase.

---

## Integration with Claude Code Patterns

### Complementary Relationship

SDD frameworks can **use Claude Code as an execution engine**. This repository focuses on Claude Code-native patterns that work within or alongside SDD:

```
┌─────────────────────────────────────────────────────────┐
│           SDD Framework (BMAD, Spec Kit, etc.)          │
│                    Specification Layer                   │
├─────────────────────────────────────────────────────────┤
│                    Claude Code                           │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐    │
│  │ Skills  │  │  Hooks  │  │   MCP   │  │Subagents│    │
│  └─────────┘  └─────────┘  └─────────┘  └─────────┘    │
│                    Execution Layer                       │
└─────────────────────────────────────────────────────────┘
```

### Pattern Alignment

| This Repo's Pattern | SDD Parallel | Integration Point |
|---------------------|--------------|-------------------|
| [Long-Running Agent](./long-running-agent.md) | External artifacts | Specs as persistent memory |
| [Context Engineering](./context-engineering.md) | Deterministic context | Specs as semantic highways |
| [Documentation Maintenance](./documentation-maintenance.md) | Living documentation | Specs as living docs |
| [Memory Architecture](./memory-architecture.md) | Project-scoped memory | Specs define project context |

### Key Difference

| Claude Code Native | SDD Frameworks |
|--------------------|----------------|
| Progressive disclosure (load on demand) | Full spec upfront |
| Token efficiency prioritized | Comprehensive documentation first |
| Incremental, one-feature-at-a-time | Multi-agent parallel planning |
| Skills for methodology | Agents for roles |

---

## Implementing Spec-Driven Workflows in Claude Code

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

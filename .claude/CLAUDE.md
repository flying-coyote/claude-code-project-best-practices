# AI-Driven Development Best Practices

## Project Purpose

Document and validate best practices for AI-driven software development, using Claude Code as the primary implementation context. This repository:
- **Adopts spec-driven development (SDD)** as the foundational methodology
- **Implements patterns** with Claude Code (skills, hooks, MCP, CLAUDE.md)
- **Aligns with industry standards** (GitHub Spec Kit, agentskills.io)
- **Validates through production use** before documenting

## Core Methodology

We follow the **4-phase SDD model** (aligned with GitHub Spec Kit):

| Phase | Purpose | Claude Code Implementation |
|-------|---------|---------------------------|
| **Specify** | Define what to build | CLAUDE.md, specs/ directory |
| **Plan** | Technical design | ARCHITECTURE.md, DECISIONS.md |
| **Tasks** | Break down work | TodoWrite, JSON task files |
| **Implement** | Execute with context | Skills, hooks, one feature at a time |

## Current Phase

**Status**: Post-v1.0 (Maintenance + SDD Alignment)
**Focus**: Aligning patterns with industry-standard SDD methodology

## Recent Learnings (Team Memory)

Capture mistakes and insights as they happen. Update 2-3x per week.

### 2026-01-10 - Self-compliance audit
**What happened**: Documented Boris Cherny's best practices but didn't apply them to this project
**Prevention**: Always run self-compliance audit after documenting new patterns

### 2026-01-10 - Settings schema change
**What happened**: Used `allowedTools` which is now `permissions.allow`
**Prevention**: Check schema errors carefully - Claude Code validates settings.json

### 2026-01-09 - Missing pattern cross-references
**What happened**: New patterns (parallel-sessions, github-actions) created without updating related patterns
**Prevention**: Update "Related Patterns" section in all affected files

## Quality Standards

All content must:
- Align with SDD principles (specify before implement)
- Reference which SDD phase it supports
- Be backed by authoritative sources (see SOURCES.md)
- Acknowledge when patterns work across AI coding tools
- Be validated in production before documenting

## Key Files

| File | Purpose |
|------|---------|
| README.md | Project overview and getting started |
| SOURCES.md | All sources with evidence tiers |
| DECISIONS.md | Design rationale and trade-offs |
| patterns/ | Core implementation patterns |
| skills/ | Skill documentation and examples |
| templates/ | Ready-to-use configuration templates |
| examples/ | Complete project examples |
| presets/ | Quick-start configurations by project type |

## Patterns Directory (by SDD Phase)

### Foundational
- `spec-driven-development.md` - **Core methodology** (4-phase model, reference implementations)

### Specify Phase
- `context-engineering.md` - Specs as deterministic context
- `memory-architecture.md` - Lifecycle-based information management

### Plan Phase
- `documentation-maintenance.md` - ARCH/PLAN/INDEX as spec artifacts
- `evidence-tiers.md` - Citation quality classification

### Tasks + Implement Phase
- `long-running-agent.md` - External artifacts, one feature at a time
- `progressive-disclosure.md` - Token-efficient methodology loading
- `advanced-hooks.md` - Quality gates, PostToolUse, Stop hooks
- `advanced-tool-use.md` - Tool search and programmatic calling

### Cross-Phase
- `agent-principles.md` - 6 production AI principles
- `mcp-patterns.md` - Failure modes + positive patterns + security
- `plugins-and-extensions.md` - Plugin vs skill vs MCP decision framework
- `recursive-evolution.md` - Self-Evolution Algorithm (multi-candidate, judge loop, crossover)
- `session-learning.md` - Cross-session preference capture from corrections (Claude Diary, /reflect)

## Skills Directory

- `README.md` - Comprehensive skills guide
- `SKILL-TEMPLATE.md` - Template for creating skills
- `examples/` - 10 production-validated example skills

## Development Guidelines

When adding new patterns:
1. Identify authoritative source (Tier A or B required)
2. Document in patterns/ with source attribution
3. Create example in examples/ if applicable
4. Update SOURCES.md with new reference
5. Test in at least one production project

## Git Workflow

Commit message prefixes:
- `📚` - Documentation and patterns
- `🔧` - Configuration and infrastructure
- `✅` - Validation and testing
- `📊` - Research and analysis

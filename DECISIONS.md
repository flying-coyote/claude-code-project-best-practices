# Design Decisions

This document explains the reasoning behind key design choices and alternatives that were considered.

## Decision 1: Prompt-Based Setup vs. Template Repository

### Alternatives Considered

| Approach | Pros | Cons |
|----------|------|------|
| **Template repo** (`gh repo create --template`) | Version-controlled, one command | Rigid structure, hard to customize, requires GitHub |
| **Shell script** (bash bootstrap) | Automated, consistent | Not interactive, can't adapt to project context |
| **Copy-paste files** | Simple, portable | Manual, error-prone, no guidance |
| **AI-guided prompt** | Interactive, adaptive, explains choices | Requires Claude Code, slightly longer |

### Decision: AI-Guided Prompt

**Why**: The prompt approach lets Claude:
1. Assess your project's characteristics before setup
2. Ask relevant questions about your needs
3. Explain what each component does as it creates them
4. Adapt to edge cases (existing files, unusual structures)

**Trade-off accepted**: Requires Claude Code to run. But if you're setting up Claude Code infrastructure, you already have Claude Code.

---

## Decision 2: Four Presets vs. Single Template

### Alternatives Considered

| Approach | Pros | Cons |
|----------|------|------|
| **Single template** | Simple, one-size-fits-all | Doesn't fit diverse project types |
| **Many presets** (10+) | Very specific configurations | Overwhelming choice, maintenance burden |
| **No presets** (fully custom) | Maximum flexibility | Requires too many decisions upfront |
| **Four presets** | Covers major categories, manageable | Some projects don't fit cleanly |

### Decision: Four Presets (coding, writing, research, hybrid)

**Why**: These four categories cover the vast majority of projects:
- **coding**: Software development, libraries, tools
- **writing**: Books, blogs, documentation
- **research**: Analysis, literature reviews, studies
- **hybrid**: Mixed-purpose (most real projects)

**Trade-off accepted**: Some projects don't fit neatly. That's what `hybrid` is for, and users can always customize after setup.

---

## Decision 3: What to Include by Default

### Components Evaluated

| Component | Included by Default? | Reasoning |
|-----------|---------------------|-----------|
| **CLAUDE.md** | Yes (always) | Core value - project context |
| **Session hook** | Optional (asked) | Useful but adds complexity |
| **Post-tool hook** | No | Only useful for specific workflows |
| **Stop hook** | No | Rarely needed |
| **Slash commands** | No | Project-specific, add later |
| **Custom skills** | No | Advanced feature, add later |

### Decision: Minimal by Default

**Why**: Start with just what's needed:
1. **CLAUDE.md** - Always created (the core value)
2. **Session hook** - Asked about (useful context display)
3. Everything else - Add later if needed

**Philosophy**: It's easier to add components than remove them. Over-engineering at setup leads to unused complexity.

---

## Decision 4: Hook Complexity

### Alternatives Considered

| Approach | What it shows | Complexity |
|----------|--------------|------------|
| **No hooks** | Nothing | None |
| **Simple hook** | Branch + uncommitted count | Low |
| **Medium hook** | + Recent commits + phase | Medium |
| **Complex hook** | + In-progress tasks + cross-repo status | High |

### Decision: Medium Complexity Hook (Opt-in)

**Why**: The session-start hook shows:
- Current branch
- Uncommitted changes count
- Recent commits (last 3)
- Current phase (if ARCHITECTURE.md exists)

This implements Anthropic's "verify before work" pattern without requiring additional tracking files.

**Not included**: Cross-repo progress tracking, JSON task files. These are powerful but add maintenance overhead.

---

## Decision 5: Quality Standards by Preset

### How Standards Differ

| Preset | Primary Standards |
|--------|------------------|
| **coding** | Clean code, TDD, conventional commits, no over-engineering |
| **writing** | Evidence-based, balanced perspective, voice consistency |
| **research** | Evidence tiers, hypothesis tracking, source attribution |
| **hybrid** | Combined subset of all three |

### Decision: Preset-Specific Standards

**Why**: Different project types have different quality concerns:
- A library doesn't need citation standards
- A book doesn't need TDD enforcement
- Research needs rigorous evidence tracking

**Trade-off**: The `hybrid` preset has broader standards, which means more to follow. This is intentional for mixed-purpose projects.

---

## Decision 6: Audit vs. Bootstrap Separation

### Alternatives Considered

| Approach | Behavior |
|----------|----------|
| **Single prompt** | Detects state, either bootstraps or audits |
| **Two prompts** | Separate prompts for new vs. existing |

### Decision: Two Separate Prompts

**Why**: Different mental models and workflows:
- **Bootstrap**: "I'm starting fresh, set me up"
- **Audit**: "I have something, how can I improve it?"

Combining them adds complexity and makes each less focused.

---

## Decision 7: Where to Store This Repository

### Alternatives Considered

| Location | Pros | Cons |
|----------|------|------|
| **GitHub Gist** | Simple, single file | Can't have directory structure |
| **Personal repo** | Full control | Less discoverable |
| **Organization repo** | Team access | Requires org setup |
| **Public repo** | Maximum reach, community | Maintenance responsibility |

### Decision: Public GitHub Repository

**Why**: The goal is to share these patterns widely. A public repo:
- Is easily referenced in prompts via raw URLs
- Can accept community contributions
- Establishes credibility through transparency
- Allows versioning and improvement over time

---

## Anti-Patterns Avoided

### 1. Over-Specification
**Avoided**: Detailed templates for every possible project type.
**Why**: Creates maintenance burden and decision paralysis.

### 2. Mandatory Components
**Avoided**: Forcing all hooks and features on every project.
**Why**: Not every project needs automation. Start minimal.

### 3. External Dependencies
**Avoided**: Requiring specific tools beyond Claude Code.
**Why**: Maximum portability and simplicity.

### 4. Complex Scripting
**Avoided**: Bash scripts with many options and flags.
**Why**: AI-guided setup is more flexible and self-documenting.

---

## Future Considerations

These were considered but deferred:

1. **MCP Server Integration**: Could provide tools for project management. Deferred until clearer use case emerges.

2. **Cross-Project Sync**: Keeping multiple projects' patterns in sync. Complex coordination problem.

3. **Version Migration**: Updating projects when best practices change. Need real usage patterns first.

4. **Team Features**: Shared conventions across team members. Scope creep for v1.

---

## Decision 8: Adopting Spec-Driven Development as Foundational Methodology

### Context

Spec-driven development (SDD) has emerged as an industry standard for AI-assisted development in 2025:
- GitHub Spec Kit: 59K+ stars, tool-agnostic 4-phase workflow
- Kiro (AWS): IDE with specs built-in
- BMAD Method: Multi-agent lifecycle management
- Agent Skills: Now an open standard (agentskills.io), adopted by OpenAI

The question: Should this project remain narrowly "Claude Code-specific" or align with industry best practices?

### Alternatives Considered

| Approach | Pros | Cons |
|----------|------|------|
| **Stay Claude Code-specific** | Deep expertise, clear scope | May age poorly, fights standardization |
| **Become tool-agnostic SDD resource** | Broader audience | Loses depth, duplicates Spec Kit |
| **Adopt SDD methodology, Claude Code implementation** | Industry-aligned, maintains depth | Requires reframing existing content |

### Decision: Adopt SDD as Methodology, Claude Code as Primary Implementation

**This repository documents AI-driven development best practices**, using Claude Code as the primary implementation context. We adopt industry-standard SDD principles rather than treating them as external.

### Core Methodology (Aligned with Spec Kit)

The 4-phase model applies to all significant work:

| Phase | Purpose | Claude Code Implementation |
|-------|---------|---------------------------|
| **Specify** | Define what to build | CLAUDE.md, requirements in specs/ |
| **Plan** | Technical design | Architecture docs, design decisions |
| **Tasks** | Break down work | Structured task lists, TodoWrite |
| **Implement** | Execute with context | Skills, hooks, one feature at a time |

### What This Means for Content

**Reframe existing patterns as SDD implementations:**
- `long-running-agent.md` → SDD's external artifacts pattern in Claude Code
- `context-engineering.md` → How specs become deterministic context
- `memory-architecture.md` → Living documentation pattern
- `documentation-maintenance.md` → ARCH/PLAN/INDEX as spec artifacts

**Elevate Spec Kit, BMAD, Kiro from "sources to monitor" to "aligned standards":**
- GitHub Spec Kit: Reference implementation of 4-phase model
- BMAD: Reference for multi-agent patterns
- Kiro: Reference for IDE-integrated specs

### Evidence Tier Alignment

| Source | Previous Tier | New Tier | Rationale |
|--------|---------------|----------|-----------|
| GitHub Spec Kit | B (secondary) | A (standard) | 59K stars, industry adoption |
| Kiro (AWS) | B (secondary) | B (major vendor) | AWS official, emerging |
| BMAD Method | C (community) | B (validated) | Production use, MIT licensed |
| agentskills.io | - | A (specification) | Open standard, multi-vendor |

### Staying Current: Review Cadence

| Source Type | Frequency | Action |
|-------------|-----------|--------|
| Anthropic Engineering Blog | Weekly | Incorporate immediately |
| Spec Kit / agentskills.io | Weekly | Align with spec changes |
| SDD frameworks (BMAD, Kiro) | Monthly | Adopt proven patterns |
| Community resources | Monthly | Validate and incorporate |

### Trade-offs Accepted

1. **Broader scope** requires more maintenance, but aligns with industry direction
2. **Less Claude Code-specific** but patterns still use Claude Code as primary example
3. **Adopting external methodology** rather than inventing our own, but standing on proven foundations

### Migration Path

Existing patterns remain valid—they implement SDD principles. New content should:
1. Reference the phase it supports (Specify/Plan/Tasks/Implement)
2. Show Claude Code implementation of cross-platform patterns
3. Acknowledge when patterns work across tools

---

*Last updated: January 2026*

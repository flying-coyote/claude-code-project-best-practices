# Claude Code Project Best Practices

A curated collection of patterns and prompts for building excellent Claude Code projects.

## The Problem

When you start a new project with Claude Code, or work on an existing one, Claude has no memory of:
- What this project is about
- Your quality standards and conventions
- The current state of work
- What happened in previous sessions

Each session starts fresh. This leads to:
- Repeated explanations of project context
- Inconsistent code quality and conventions
- Lost context between sessions
- Wasted time re-establishing understanding

## The Solution

A **project foundation** that gives Claude persistent context through a `.claude/` directory containing:

```
your-project/
└── .claude/
    ├── CLAUDE.md           # Project context Claude reads every session
    ├── settings.json       # Hook configurations (optional)
    ├── hooks/              # Automation scripts (optional)
    │   └── session-start.sh
    └── skills/             # Project-specific skills (optional)
        └── my-skill/
            └── SKILL.md
```

This approach is based on Anthropic's own engineering patterns for long-running agents.

## Quick Start

### For a New Project

Copy this prompt into Claude Code:

```
Fetch https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/refs/heads/master/prompts/BOOTSTRAP-NEW-PROJECT.md and follow its instructions to set up Claude infrastructure for this project.
```

### For an Existing Project

Copy this prompt into Claude Code:

```
Fetch https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/refs/heads/master/prompts/AUDIT-EXISTING-PROJECT.md and follow its instructions to review this project against best practices.
```

## What's Included

### Prompts
- **[BOOTSTRAP-NEW-PROJECT.md](prompts/BOOTSTRAP-NEW-PROJECT.md)** - Interactive setup for new projects
- **[AUDIT-EXISTING-PROJECT.md](prompts/AUDIT-EXISTING-PROJECT.md)** - Review and improve existing projects

### Templates
- **[CLAUDE.md.template](templates/CLAUDE.md.template)** - Project context template
- **[settings.json.template](templates/settings.json.template)** - Hook configuration
- **[session-start.sh](templates/session-start.sh)** - Session initialization script

### Presets
Project-type configurations with appropriate defaults:
- **[coding.md](presets/coding.md)** - Software development (TDD, debugging, git workflow)
- **[writing.md](presets/writing.md)** - Content creation (voice consistency, citations)
- **[research.md](presets/research.md)** - Analysis projects (evidence tiers, hypotheses)
- **[hybrid.md](presets/hybrid.md)** - Mixed-purpose projects

### Patterns

Core implementation patterns documented with evidence tiers:

| Pattern | Use When | Key Insight | Source |
|---------|----------|-------------|--------|
| [Long-Running Agent](patterns/long-running-agent.md) | Starting project | External artifacts as memory | Anthropic |
| [Context Engineering](patterns/context-engineering.md) | Structuring context | Correctness > compression | Nate B. Jones |
| [Agent Principles](patterns/agent-principles.md) | Building production AI | 6 principles for reliability | Nate B. Jones |
| [MCP Failure Modes](patterns/mcp-failure-modes.md) | Integrating MCP servers | 7 failure modes + 3 patterns | Nate B. Jones |
| [Advanced Tool Use](patterns/advanced-tool-use.md) | Optimizing token usage | Tool search, programmatic calling | Anthropic |
| [Evidence Tiers](patterns/evidence-tiers.md) | Managing citations | Dual tier system (A-D + 1-5) | Production |
| [Confidence Scoring](patterns/confidence-scoring.md) | Hypothesis validation | HIGH/MEDIUM/LOW with evidence mapping | Production |
| [Progressive Disclosure](patterns/progressive-disclosure.md) | Large skills (200+ lines) | 3-tier architecture, 73% token savings | Production |
| [Advanced Hooks](patterns/advanced-hooks.md) | Automating workflows | PostToolUse, Stop hooks | Production |
| [Documentation Maintenance](patterns/documentation-maintenance.md) | Keeping docs current | ARCH/PLAN/INDEX trio | Production |
| [Memory Architecture](patterns/memory-architecture.md) | Context lifecycle | 4-tier memory model | Nate B. Jones |
| [Architecture Decision Records](patterns/architecture-decision-records.md) | Documenting decisions | Why decisions were made, not just what | Software Eng |

### Skills
Reusable AI behavior patterns:
- **[skills/README.md](skills/README.md)** - Comprehensive skills guide
- **[skills/QUICK-REFERENCE.md](skills/QUICK-REFERENCE.md)** - Fast skill lookup and integration patterns
- **[skills/SKILL-TEMPLATE.md](skills/SKILL-TEMPLATE.md)** - Template for new skills
- **[skills/SECURITY-GUIDELINES.md](skills/SECURITY-GUIDELINES.md)** - Security framework with MITRE ATLAS mapping
- **[skills/examples/](skills/examples/)** - 9 production-validated example skills:
  - `systematic-debugger` - 4-phase debugging methodology (REPRODUCE-ISOLATE-UNDERSTAND-FIX)
  - `tdd-enforcer` - Test-driven development enforcement (RED-GREEN-REFACTOR)
  - `git-workflow-helper` - Git best practices and safe operations
  - `ultrathink-analyst` - Deep analysis (FRAME-ANALYZE-SYNTHESIZE)
  - `content-reviewer` - Publication quality (evidence tiers, voice, balance)
  - `research-extractor` - Systematic research synthesis (HIGH RISK - 5-layer defense)
  - `hypothesis-validator` - Research hypothesis validation with confidence scoring
  - `threat-model-reviewer` - Security threat modeling (STRIDE)
  - `detection-rule-reviewer` - SIEM/detection engineering quality

### Examples
Complete `.claude/` directories you can reference:
- **[examples/coding-project/](examples/coding-project/)** - Software development setup
- **[examples/writing-project/](examples/writing-project/)** - Content creation setup

## Core Principles

### 1. Context is King
Claude works better when it understands your project. A good `CLAUDE.md` file provides:
- Project purpose (what and why)
- Current phase (where we are)
- Quality standards (how we work)
- Conventions (consistency rules)

### 2. External Artifacts as Memory
From Anthropic's engineering blog:
> "External artifacts become the agent's memory. Progress files, git history, and structured feature lists persist across sessions."

### 3. Verify Before Work
The session-start hook implements Anthropic's "verify before work" pattern:
- Check for uncommitted changes
- Show recent commits for context
- Surface any in-progress work
- Prevent starting with broken state

### 4. Minimal by Default
Start with just `CLAUDE.md`. Add hooks only if you need them. Don't over-engineer.

## Why This Approach?

See **[DECISIONS.md](DECISIONS.md)** for detailed reasoning on:
- Why prompts instead of template repos
- Why four presets instead of one or many
- Why AI-guided setup instead of scripts
- What to include vs. exclude

## Sources & Acknowledgments

See **[SOURCES.md](SOURCES.md)** for all references, including:
- Anthropic Engineering Blog posts
- Claude Code documentation
- Production validation from real projects

**Foundational influences on this repo's design:**
- **[Daniel Miessler's Fabric](https://github.com/danielmiessler/fabric)** - The IDENTITY/GOAL/STEPS/OUTPUT pattern structure and "scaffolding > models" philosophy
- **[Nate B. Jones's Memory Prompts](https://natesnewsletter.substack.com)** - Context lifecycle management and retrieval strategy patterns

## Contributing

Contributions welcome! Please:
1. Open an issue to discuss changes
2. Follow existing patterns and style
3. Update documentation as needed

## License

MIT License - Use freely, attribution appreciated.

---

*Built from patterns validated across 12+ production projects.*

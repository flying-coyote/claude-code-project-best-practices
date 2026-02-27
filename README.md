# AI-Driven Development Best Practices

A **meta-guide** curating community Claude Code resources with unique contributions: evidence assessment, SDD methodology, context engineering, security frameworks, and measurement discipline.

**Philosophy**: We defer to community consensus where it exists (tool discovery, implementation guides) and focus on what we uniquely provide (architectural analysis, integration guidance, evidence validation).

**Methodology**: We adopt [spec-driven development (SDD)](patterns/spec-driven-development.md) as our foundational approach, aligned with industry standards like [GitHub Spec Kit](https://github.com/github/spec-kit) and [agentskills.io](https://agentskills.io).

> 🔗 **Looking for tool recommendations?** See [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) (5.6k+ stars) for community-curated MCPs, plugins, and productivity tips. See [COMMUNITY-RESOURCES.md](COMMUNITY-RESOURCES.md) for our complete community directory.

## The Problem

When you use AI coding agents without structure:
- Inconsistent results across sessions
- Context loss in complex features
- "Works but wrong" implementations
- Difficult to maintain or extend
- Poor team coordination

## The Solution

A **spec-driven approach** that gives AI agents persistent context through structured artifacts:

```
your-project/
├── specs/                  # Feature specifications (Specify phase)
├── ARCHITECTURE.md         # System design (Plan phase)
├── PLAN.md                 # Current priorities (Tasks phase)
└── .claude/                # Claude Code implementation
    ├── CLAUDE.md           # Project context
    ├── settings.json       # Hook configurations
    ├── hooks/              # Automation scripts
    ├── commands/           # Slash commands
    └── skills/             # Reusable methodologies
```

This approach implements the **4-phase SDD model**:
1. **Specify** → Define what to build (CLAUDE.md, specs/)
2. **Plan** → Technical design (ARCHITECTURE.md, DECISIONS.md)
3. **Tasks** → Break down work (PLAN.md, TodoWrite)
4. **Implement** → Execute with context (skills, hooks, one feature at a time)

## Quick Start

### The Three Tiers

Every project uses the same infrastructure pattern - just choose your tier:

| Tier | When | Time | What You Get |
|------|------|------|--------------|
| **Tier 1: Baseline** | All projects | 5 min | Stop hook + permissions |
| **Tier 2: Active** | Weekly work | 15 min | + CLAUDE.md + SessionStart |
| **Tier 3: Team** | Collaborators | 30 min | + GitHub Actions + /commit-push-pr |

**There's no difference between "new" and "existing" projects** - both follow the same tiered approach.

### Apply Tier 1 Now (5 minutes)

Run this in your project to get baseline protection:

```bash
mkdir -p .claude && cat > .claude/settings.json << 'EOF'
{
  "permissions": {
    "allow": ["Bash(git status*)", "Bash(git diff*)", "Bash(git log*)"]
  },
  "hooks": {
    "Stop": [{
      "matcher": "",
      "hooks": [{
        "type": "command",
        "command": "bash -c 'if ! git diff --quiet 2>/dev/null; then echo \"⚠️ Uncommitted changes\"; fi'"
      }]
    }]
  }
}
EOF
```

### Full Setup (Interactive)

For Tier 2/3 setup with CLAUDE.md, hooks, and GitHub Actions:

```
Fetch https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/refs/heads/master/prompts/SETUP-PROJECT.md and follow its instructions.
```

See **[Project Infrastructure Pattern](patterns/project-infrastructure.md)** for the complete tiered approach.

## Which Entry Point Should I Use?

This repository provides multiple entry points for different scenarios:

| Your Situation | Use This | Why |
|----------------|----------|-----|
| I have 5 minutes, want quick value | README Tier 1 Quick Start (above) | Immediate uncommitted/unpushed warnings with 4 lines in settings.json |
| Setting up new project from scratch | [BOOTSTRAP-NEW-PROJECT.md](prompts/BOOTSTRAP-NEW-PROJECT.md) | Full interactive setup with preset selection and best practices |
| Setting up infrastructure for any project | [SETUP-PROJECT.md](prompts/SETUP-PROJECT.md) | Unified tiered approach (5/15/30 min) for new or existing projects |
| Auditing existing Claude Code setup | [AUDIT-EXISTING-PROJECT.md](prompts/AUDIT-EXISTING-PROJECT.md) | Comprehensive compliance check against best practices |
| Learning the methodology | [FOUNDATIONAL-PRINCIPLES.md](FOUNDATIONAL-PRINCIPLES.md) | Read The Big 3 principles first |
| Finding a specific pattern | Pattern tables below | Jump directly to implementation guidance |

**Not sure?** Start with the Tier 1 Quick Start above, then explore SETUP-PROJECT.md when you want more.

## Pattern Decision Matrix

Quick reference: Which pattern solves which problem?

| I Need To... | Use This Pattern | Alternative/Related |
|--------------|------------------|---------------------|
| **Getting Started** |
| Set up project infrastructure | [project-infrastructure.md](patterns/project-infrastructure.md) | [SETUP-PROJECT.md](prompts/SETUP-PROJECT.md) |
| Understand core principles | [FOUNDATIONAL-PRINCIPLES.md](FOUNDATIONAL-PRINCIPLES.md) | [spec-driven-development.md](patterns/spec-driven-development.md) |
| Learn patterns progressively | [PATTERN-LEARNING-PATH.md](PATTERN-LEARNING-PATH.md) | Pattern tables below |
| Migrate from Cursor or other tools | [MIGRATION-GUIDE.md](MIGRATION-GUIDE.md) | [TROUBLESHOOTING.md](TROUBLESHOOTING.md) |
| **Context & Planning** |
| Keep CLAUDE.md minimal | [context-engineering.md](patterns/context-engineering.md) | [FOUNDATIONAL-PRINCIPLES.md](FOUNDATIONAL-PRINCIPLES.md) |
| Plan before implementing | [spec-driven-development.md](patterns/spec-driven-development.md) | [planning-first-development.md](patterns/planning-first-development.md) |
| Manage information lifecycle | [memory-architecture.md](patterns/memory-architecture.md) | [context-engineering.md](patterns/context-engineering.md) |
| Surface hidden assumptions | [johari-window-ambiguity.md](patterns/johari-window-ambiguity.md) | - |
| Document architecture decisions | [architecture-decision-records.md](patterns/architecture-decision-records.md) | [documentation-maintenance.md](patterns/documentation-maintenance.md) |
| **Implementation** |
| Work across multiple sessions | [long-running-agent.md](patterns/long-running-agent.md) | [session-learning.md](patterns/session-learning.md) |
| Add quality gates (hooks) | [advanced-hooks.md](patterns/advanced-hooks.md) | [project-infrastructure.md](patterns/project-infrastructure.md) |
| Use advanced tool features | [advanced-tool-use.md](patterns/advanced-tool-use.md) | - |
| Run parallel work streams | [parallel-sessions.md](patterns/parallel-sessions.md) | - |
| Navigate code dynamically | [agentic-retrieval.md](patterns/agentic-retrieval.md) | - |
| Generate images in pipeline | [ai-image-generation.md](patterns/ai-image-generation.md) | - |
| **Extensions** |
| Choose MCP vs Skills vs Hooks | [plugins-and-extensions.md](patterns/plugins-and-extensions.md) | [mcp-vs-skills-economics.md](patterns/mcp-vs-skills-economics.md) |
| Design large skills efficiently | [progressive-disclosure.md](patterns/progressive-disclosure.md) | [skills-domain-knowledge.md](patterns/skills-domain-knowledge.md) |
| Understand MCP failure modes | [mcp-patterns.md](patterns/mcp-patterns.md) | [safety-and-sandboxing.md](patterns/safety-and-sandboxing.md) |
| Evaluate cost vs performance | [mcp-vs-skills-economics.md](patterns/mcp-vs-skills-economics.md) | [plugins-and-extensions.md](patterns/plugins-and-extensions.md) |
| Add domain knowledge to skills | [skills-domain-knowledge.md](patterns/skills-domain-knowledge.md) | [progressive-disclosure.md](patterns/progressive-disclosure.md) |
| **Orchestration** |
| Choose orchestration framework | [framework-selection-guide.md](patterns/framework-selection-guide.md) | - |
| Use GSD pattern | [gsd-orchestration.md](patterns/gsd-orchestration.md) | [subagent-orchestration.md](patterns/subagent-orchestration.md) |
| Implement cognitive agents | [cognitive-agent-infrastructure.md](patterns/cognitive-agent-infrastructure.md) | [framework-selection-guide.md](patterns/framework-selection-guide.md) |
| Orchestrate subagents | [subagent-orchestration.md](patterns/subagent-orchestration.md) | [gsd-orchestration.md](patterns/gsd-orchestration.md) |
| Manage recursive context | [recursive-context-management.md](patterns/recursive-context-management.md) | [memory-architecture.md](patterns/memory-architecture.md) |
| **Quality & Security** |
| Ensure security and isolation | [safety-and-sandboxing.md](patterns/safety-and-sandboxing.md) | [mcp-patterns.md](patterns/mcp-patterns.md) |
| Generate secure code | [secure-code-generation.md](patterns/secure-code-generation.md) | [safety-and-sandboxing.md](patterns/safety-and-sandboxing.md) |
| Assess output confidence | [confidence-scoring.md](patterns/confidence-scoring.md) | - |
| Apply production AI principles | [agent-principles.md](patterns/agent-principles.md) | [safety-and-sandboxing.md](patterns/safety-and-sandboxing.md) |
| Evaluate agent performance | [agent-evaluation.md](patterns/agent-evaluation.md) | [confidence-scoring.md](patterns/confidence-scoring.md) |
| Implement self-improvement | [recursive-evolution.md](patterns/recursive-evolution.md) | [session-learning.md](patterns/session-learning.md) |
| **Research & Documentation** |
| Classify evidence quality | [evidence-tiers.md](patterns/evidence-tiers.md) | [confidence-scoring.md](patterns/confidence-scoring.md) |
| Maintain documentation | [documentation-maintenance.md](patterns/documentation-maintenance.md) | [architecture-decision-records.md](patterns/architecture-decision-records.md) |
| Learn from session corrections | [session-learning.md](patterns/session-learning.md) | [long-running-agent.md](patterns/long-running-agent.md) |
| Integrate with CI/CD | [github-actions-integration.md](patterns/github-actions-integration.md) | [advanced-hooks.md](patterns/advanced-hooks.md) |
| **Tool Selection** |
| Choose Claude Code vs alternatives | [tool-ecosystem.md](patterns/tool-ecosystem.md) | [framework-selection-guide.md](patterns/framework-selection-guide.md) |

**Can't find what you need?** See [PATTERN-LEARNING-PATH.md](PATTERN-LEARNING-PATH.md) for guided learning by role or [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for common issues.

## What's Included

### Prompts
- **[SETUP-PROJECT.md](prompts/SETUP-PROJECT.md)** - Unified tiered setup for any project (replaces separate new/existing prompts)

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

### Patterns (by SDD Phase)

Core implementation patterns organized by the spec-driven development phase they support:

#### Foundational
| Pattern | Key Insight | Source |
|---------|-------------|--------|
| [Spec-Driven Development](patterns/spec-driven-development.md) | 4-phase model: Specify→Plan→Tasks→Implement | GitHub Spec Kit |
| [Framework Selection Guide](patterns/framework-selection-guide.md) | Choose orchestration: Native (default) vs GSD vs CAII | Synthesis |

#### Specify Phase
| Pattern | Key Insight | Source |
|---------|-------------|--------|
| [Context Engineering](patterns/context-engineering.md) | Specs as deterministic context; correctness > compression | Nate B. Jones |
| [Memory Architecture](patterns/memory-architecture.md) | 4-tier lifecycle model for information management | Nate B. Jones |
| [Johari Window Ambiguity](patterns/johari-window-ambiguity.md) | Surface hidden assumptions before task execution | CAII |

#### Plan Phase
| Pattern | Key Insight | Source |
|---------|-------------|--------|
| [Documentation Maintenance](patterns/documentation-maintenance.md) | ARCH/PLAN/INDEX trio as spec artifacts | Production |
| [Architecture Decision Records](patterns/architecture-decision-records.md) | Document why, not just what | Software Eng |
| [Evidence Tiers](patterns/evidence-tiers.md) | Dual tier system (A-D + 1-5) for claims | Production |

#### Tasks + Implement Phase
| Pattern | Key Insight | Source |
|---------|-------------|--------|
| [Long-Running Agent](patterns/long-running-agent.md) | External artifacts as memory; one feature at a time | Anthropic |
| [Progressive Disclosure](patterns/progressive-disclosure.md) | 3-tier architecture; 73% token savings | Production |
| [Advanced Hooks](patterns/advanced-hooks.md) | PreToolUse, PostToolUse, Stop hooks for quality gates | Production |
| [Advanced Tool Use](patterns/advanced-tool-use.md) | Tool search, programmatic calling | Anthropic |
| [Agentic Retrieval](patterns/agentic-retrieval.md) | Dynamic navigation vs pre-computed embeddings | LlamaIndex |
| [Parallel Sessions](patterns/parallel-sessions.md) | 5+ terminal + 5-10 web sessions for parallel work streams | Boris Cherny |
| [AI Image Generation](patterns/ai-image-generation.md) | Automated visual assets in development pipelines | Community |

#### Cross-Phase
| Pattern | Key Insight | Source |
|---------|-------------|--------|
| [Agent Principles](patterns/agent-principles.md) | 6 principles for production AI reliability | Nate B. Jones |
| [Agent Evaluation](patterns/agent-evaluation.md) | Evals as tests; task-based, LLM-as-judge, infrastructure noise | Anthropic |
| [MCP Patterns](patterns/mcp-patterns.md) | 7 failure modes + positive patterns + OWASP security | Nate B. Jones + OWASP |
| [MCP vs Skills Economics](patterns/mcp-vs-skills-economics.md) | Skills 50% cheaper than MCP; tradeoffs on speed vs cost | Tenzir |
| [Plugins and Extensions](patterns/plugins-and-extensions.md) | When to use Skills vs MCP vs Hooks vs Commands | Production |
| [Safety and Sandboxing](patterns/safety-and-sandboxing.md) | OS-level isolation over permission prompts | Anthropic + OWASP |
| [GSD Orchestration](patterns/gsd-orchestration.md) | Fresh context per subagent; state externalization | glittercowboy |
| [Cognitive Agent Infrastructure](patterns/cognitive-agent-infrastructure.md) | 7 fixed cognitive agents vs domain-specific proliferation | CAII |
| [Recursive Context Management](patterns/recursive-context-management.md) | Programmatic self-examination vs single forward pass | MIT CSAIL |
| [Session Learning](patterns/session-learning.md) | Capture corrections to update persistent config | Lance Martin |
| [Confidence Scoring](patterns/confidence-scoring.md) | HIGH/MEDIUM/LOW assessment framework | Production |
| [Recursive Evolution](patterns/recursive-evolution.md) | Self-Evolution Algorithm: multi-candidate, judge loop, crossover | Google TTD-DR |
| [Tool Ecosystem](patterns/tool-ecosystem.md) | When Claude Code vs alternatives (Aider, Cursor, OpenHands) | Community |

### Skills
Reusable AI behavior patterns:
- **[skills/README.md](skills/README.md)** - Comprehensive skills guide
- **[skills/QUICK-REFERENCE.md](skills/QUICK-REFERENCE.md)** - Fast skill lookup and integration patterns
- **[skills/SKILL-TEMPLATE.md](skills/SKILL-TEMPLATE.md)** - Template for new skills
- **[skills/SECURITY-GUIDELINES.md](skills/SECURITY-GUIDELINES.md)** - Security framework with MITRE ATLAS mapping
- **[skills/examples/](skills/examples/)** - 10 production-validated example skills:
  - `systematic-debugger` - 4-phase debugging methodology (REPRODUCE-ISOLATE-UNDERSTAND-FIX)
  - `tdd-enforcer` - Test-driven development enforcement (RED-GREEN-REFACTOR)
  - `git-workflow-helper` - Git best practices and safe operations
  - `ultrathink-analyst` - Deep analysis (FRAME-ANALYZE-SYNTHESIZE)
  - `recursive-analyst` - Self-Evolution Algorithm (multi-candidate, judge loop, crossover)
  - `content-reviewer` - Publication quality (evidence tiers, voice, balance)
  - `research-extractor` - Systematic research synthesis (HIGH RISK - 5-layer defense)
  - `hypothesis-validator` - Research hypothesis validation with confidence scoring
  - `threat-model-reviewer` - Security threat modeling (STRIDE)
  - `detection-rule-reviewer` - SIEM/detection engineering quality

### Examples
Complete `.claude/` directories you can reference:
- **[examples/coding-project/](examples/coding-project/)** - Software development setup
- **[examples/writing-project/](examples/writing-project/)** - Content creation setup
- **[examples/research-project/](examples/research-project/)** - Research and analysis setup

## Core Principles

### 1. Specify Before Implement
The SDD 4-phase model ensures clarity before code:
- **Specify**: What are we building and why?
- **Plan**: How will we build it?
- **Tasks**: What are the concrete steps?
- **Implement**: Execute with full context

### 2. External Artifacts as Memory
From Anthropic's engineering blog:
> "External artifacts become the agent's memory. Progress files, git history, and structured feature lists persist across sessions."

Specs, architecture docs, and task files bridge session boundaries.

### 3. Scale Rigor to Complexity
- **Simple bug fix**: Skip to Tasks phase, brief spec in commit message
- **Small feature (<1 day)**: Combine Specify+Plan, then implement
- **Complex feature**: Full 4-phase workflow with specs/
- **Exploratory work**: "Vibe code" first, retrofit specs if keeping

### 4. Cross-Platform Awareness
These patterns work across AI coding tools:
- Skills follow [agentskills.io](https://agentskills.io) open standard (Claude, Codex, Cursor, etc.)
- SDD methodology applies to any AI coding agent
- Claude Code is our implementation context, not the only option

## Why This Approach?

See **[DECISIONS.md](DECISIONS.md)** for detailed reasoning on:
- Why prompts instead of template repos
- Why four presets instead of one or many
- Why AI-guided setup instead of scripts
- What to include vs. exclude

## Sources & Acknowledgments

See **[SOURCES-QUICK-REFERENCE.md](SOURCES-QUICK-REFERENCE.md)** for top 20 Tier A/B sources or **[SOURCES.md](SOURCES.md)** for comprehensive database, including:
- Anthropic Engineering Blog posts
- Industry standards (GitHub Spec Kit, agentskills.io, OWASP MCP Guide)
- Production validation from real projects

**Aligned standards:**
- **[GitHub Spec Kit](https://github.com/github/spec-kit)** - 4-phase SDD model (59K+ stars)
- **[agentskills.io](https://agentskills.io)** - Open standard for cross-platform skills
- **[OWASP MCP Security Guide](https://genai.owasp.org)** - MCP security best practices

**Foundational influences:**
- **[Daniel Miessler's Fabric](https://github.com/danielmiessler/fabric)** - Pattern structure and "scaffolding > models" philosophy
- **[Nate B. Jones's Memory Prompts](https://natesnewsletter.substack.com)** - Context lifecycle management
- **[BMAD Method](https://github.com/bmad-code-org/BMAD-METHOD)** - Multi-agent architecture patterns

## Contributing

Contributions welcome! Please:
1. Open an issue to discuss changes
2. Follow existing patterns and style
3. Update documentation as needed

## License

MIT License - Use freely, attribution appreciated.

---

*Built from patterns validated across 12+ production projects.*

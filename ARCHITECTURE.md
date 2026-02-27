# Architecture

**Purpose**: System design, directory structure, and current phase status
**Last Updated**: January 2, 2026

---

## Project Purpose

This repository documents and validates patterns for Claude Code projects. It serves as:
- **Reference implementation** - Practices what it preaches
- **Teaching resource** - Examples and templates for users
- **Validation testbed** - Patterns tested in production before documenting

---

## Current Phase

**Phase**: Post-v1.0 Maintenance + Pattern Expansion
**Status**: Active development

**Recent Milestones**:
- v1.0: Initial patterns from Anthropic (Nov 2025)
- v1.1: Nate B. Jones patterns added (Dec 8, 2025)
- v1.2: Self-compliance - repo follows its own patterns (Dec 8, 2025)
- v1.3: Production patterns from second-brain integration (Dec 13, 2025)

---

## Directory Structure

```
claude-code-project-best-practices/
├── .claude/                    # Meta-project infrastructure
│   ├── CLAUDE.md              # Project context
│   ├── settings.json          # Hooks configuration
│   ├── hooks/                 # Hook scripts
│   │   ├── session-start.sh   # Context loading
│   │   ├── post-tool-use.sh   # INDEX.md regeneration
│   │   └── stop-doc-check.sh  # Documentation currency
│   └── claude-tasks.json      # Task tracking
│
├── patterns/                   # Core implementation patterns (20 total)
│   ├── advanced-hooks.md      # PostToolUse, Stop hooks
│   ├── advanced-tool-use.md   # Tool search, programmatic calling
│   ├── agent-principles.md    # 6 production principles
│   ├── ai-image-generation.md # AI asset generation for development
│   ├── architecture-decision-records.md  # ADR framework
│   ├── confidence-scoring.md  # HIGH/MEDIUM/LOW hypothesis confidence
│   ├── context-engineering.md # Deterministic vs probabilistic
│   ├── documentation-maintenance.md  # ARCH/PLAN/INDEX trio
│   ├── evidence-tiers.md      # Dual tier system (A-D + 1-5)
│   ├── long-running-agent.md  # Anthropic harness patterns
│   ├── mcp-patterns.md        # Failure modes + positive patterns
│   ├── memory-architecture.md # Lifecycle-based memory
│   ├── planning-first-development.md  # "Great Planning is Great Prompting"
│   ├── plugins-and-extensions.md  # Skills vs MCP vs Hooks decision
│   ├── progressive-disclosure.md  # 3-tier skill architecture (73% reduction)
│   ├── recursive-evolution.md # Self-Evolution Algorithm
│   ├── skills-domain-knowledge.md  # Domain expertise as persistent context
│   ├── spec-driven-development.md  # 4-phase SDD model (foundational)
│   ├── subagent-orchestration.md  # Multi-agent patterns
│   └── tool-ecosystem.md          # Claude Code vs alternatives
│
├── skills/                     # Skill documentation
│   ├── README.md              # Skills guide
│   ├── QUICK-REFERENCE.md     # Fast lookup
│   ├── SKILL-TEMPLATE.md      # Template with all sections
│   ├── SECURITY-GUIDELINES.md # Risk classification
│   └── examples/              # 10 example skills
│       ├── content-reviewer/
│       ├── detection-rule-reviewer/
│       ├── git-workflow-helper/
│       ├── hypothesis-validator/
│       ├── recursive-analyst/
│       ├── research-extractor/
│       ├── systematic-debugger/
│       ├── tdd-enforcer/
│       ├── threat-model-reviewer/
│       └── ultrathink-analyst/ (with 3 workflows)
│
├── templates/                  # Ready-to-use templates
│   ├── CLAUDE.md.template     # Handlebars template
│   ├── settings.json.template # Hook configuration
│   └── session-start.sh       # Session hook script
│
├── examples/                   # Complete project examples
│   ├── coding-project/        # Software development setup
│   ├── research-project/      # Research and analysis setup
│   └── writing-project/       # Content creation setup
│
├── presets/                    # Quick-start configurations
│   ├── coding.md
│   ├── writing.md
│   ├── research.md
│   └── hybrid.md
│
├── prompts/                    # Interactive setup guides
│   ├── BOOTSTRAP-NEW-PROJECT.md
│   └── AUDIT-EXISTING-PROJECT.md
│
├── automation/                 # Scripts
│   └── generate_index.py      # INDEX.md generator
│
├── research/                   # Research and analysis
│   └── ai-creators-analysis.md # Tier A source analysis
│
├── ARCHITECTURE.md            # This file (strategic)
├── ARCHIVE.md                 # Completed work and milestones
├── CONTRIBUTING.md            # Contribution guidelines
├── DECISIONS.md               # Design rationale
├── INDEX.md                   # Auto-generated inventory
├── PLAN.md                    # Current priorities (tactical)
├── README.md                  # Project overview
└── SOURCES.md                 # All sources with evidence tiers
```

---

## Project Philosophy (Updated February 2026)

### Meta-Guide Approach

This project is a **meta-guide** that curates and enhances community Claude Code resources rather than duplicating them. We follow a three-layer strategy:

#### Layer 1: Pointer Patterns (~12 patterns, 33%)
- Point to best community resource with evidence tier assessment
- Add integration guidance and decision matrices
- Track deprecations and provide migration paths
- **Examples**: [mcp-daily-essentials.md](patterns/mcp-daily-essentials.md) → shanraisshan, [advanced-tool-use.md](patterns/advanced-tool-use.md) → Anthropic blog

#### Layer 2: Deep Methodology (~18 patterns, 50%)
- Unique architectural analysis not found in community
- SDD methodology, context engineering, evidence tiers
- Security frameworks, orchestration patterns
- Measurement discipline with revalidation
- **Examples**: [spec-driven-development.md](patterns/spec-driven-development.md), [context-engineering.md](patterns/context-engineering.md), [evidence-tiers.md](patterns/evidence-tiers.md)

#### Layer 3: Synthesis & Integration (~6 patterns, 17%)
- Comparative frameworks (tool ecosystem, framework selection)
- Integration patterns between resources
- Decision trees and trade-off analysis
- **Examples**: [framework-selection-guide.md](patterns/framework-selection-guide.md), [mcp-vs-skills-economics.md](patterns/mcp-vs-skills-economics.md)

### Why This Approach?

**Problem identified (February 2026)**:
- 15 of 36 patterns (42%) had 50%+ overlap with community projects
- Maintaining tool lists that community projects maintain better
- Duplication created maintenance burden and slower-than-community updates
- Our unique value (SDD, evidence tiers, measurements) was getting diluted

**Solution**:
- **Curate** community resources with evidence tier assessment
- **Integrate** resources through decision matrices
- **Fill gaps** not covered by community
- **Track** deprecations and coordination issues
- **Defer to community consensus** where it exists

**Result**: Focus on 18 unique patterns (evidence tiers, SDD, context engineering, security frameworks, measurement discipline) while pointing to community leaders for tool discovery and implementation details.

See: [COMMUNITY-RESOURCES.md](COMMUNITY-RESOURCES.md) for complete directory of community projects we curate and enhance.

---

## Key Design Decisions

### 1. Self-Compliance
The repository follows the patterns it documents. This provides:
- Credibility (practices what it preaches)
- Validation (patterns tested on this repo)
- Example (users can see patterns in action)

### 2. Evidence-Based Documentation
All patterns must be backed by:
- Tier A: Anthropic official sources
- Tier B: Production-validated implementations
- Tier C: Community best practices

### 3. Progressive Disclosure
Documentation is layered:
- README.md: Quick start
- patterns/: Deep dives
- examples/: Complete implementations

---

## Integration Points

### Sources
- Anthropic Engineering Blog
- Nate B. Jones (Memory Prompts, MCP Guide)
- Daniel Miessler (Fabric framework)
- Production validation (12+ projects)

### Validation
Patterns are validated in production before documenting:
- project1 (second-brain): 21 skills, 50 hypotheses
- 8 independent repositories

---

## Maintenance

| Document | Update Trigger | Owner |
|----------|---------------|-------|
| ARCHITECTURE.md | Major milestones, structure changes | Manual |
| PLAN.md | Weekly, priority shifts | Manual |
| INDEX.md | File changes | Automated |

See [PLAN.md](PLAN.md) for current priorities.

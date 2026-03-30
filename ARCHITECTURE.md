# Architecture

**Purpose**: System design, directory structure, and current phase status
**Last Updated**: March 26, 2026

---

## Project Purpose

This repository provides an **evidence-based analytical layer** for Claude Code. It evaluates claims, compares approaches, and surfaces quantified behavioral insights — the "Consumer Reports" for Claude Code tooling.

**What we are**:
- Evidence assessor (dual-tier system for claims)
- Comparative analyst (tools, frameworks, approaches)
- Behavioral insight aggregator (quantified observations from expert practitioners)

**What we are NOT**:
- Implementation guide (see [everything-claude-code](https://github.com/anthropics-solutions/everything-claude-code))
- Methodology framework (see [superpowers](https://github.com/obraun-cl/superpowers))
- Tool catalog (see community repos in SOURCES.md)

---

## Current Phase

**Phase**: v2.0 — Analytical Layer Repositioning
**Status**: Active

**Milestones**:
- v1.0: Initial patterns from Anthropic (Nov 2025)
- v1.1-v1.4: Pattern expansion to 36 patterns (Nov 2025 - Mar 2026)
- v2.0: Repositioned as analytical layer; 36 patterns → 14 analysis documents (Mar 2026)

---

## Directory Structure

```
claude-code-project-best-practices/
├── .claude/                    # Meta-project infrastructure
│   ├── CLAUDE.md              # Project context
│   ├── settings.json          # Hooks configuration
│   └── hooks/                 # Hook scripts
│
├── analysis/                   # Core content (16 documents)
│   ├── evidence-tiers.md      # Dual tier system (A-D + 1-5)
│   ├── behavioral-insights.md # Quantified Claude Code behavior
│   ├── orchestration-comparison.md  # Orchestration approach comparison
│   ├── mcp-vs-skills-economics.md   # Cost/performance analysis
│   ├── mcp-patterns.md        # Failure modes + OWASP mapping
│   ├── mcp-daily-essentials.md      # Optimal plugin configuration
│   ├── plugins-and-extensions.md    # Skills vs MCP vs Hooks decision
│   ├── safety-and-sandboxing.md     # 4-layer security stack
│   ├── secure-code-generation.md    # OWASP-aware code generation
│   ├── tool-ecosystem.md           # Claude Code vs alternatives
│   ├── framework-selection-guide.md # Framework decision matrix
│   ├── harness-engineering.md       # Harness philosophy + diagnostics
│   ├── domain-knowledge-architecture.md # Domain knowledge for LLMs
│   ├── agent-evaluation.md         # Eval methodology
│   ├── agent-principles.md         # 6 production principles
│   └── confidence-scoring.md       # Assessment framework
│
├── archive/                    # Prior v1 content (preserved)
│   ├── patterns-v1/           # 24 archived patterns
│   ├── skills-v1/             # Archived skills + examples
│   ├── templates-v1/          # Archived templates
│   ├── presets-v1/            # Archived presets
│   ├── prompts-v1/            # Archived prompts
│   ├── examples-v1/           # Archived project examples
│   ├── mcp-server-v1/         # Archived MCP server
│   └── specs-v1/              # Archived specs
│
├── automation/                 # Scripts
│   └── generate_index.py      # INDEX.md generator
│
├── research/                   # Research and analysis
│
├── ARCHITECTURE.md            # This file
├── DECISIONS.md               # Design rationale
├── INDEX.md                   # Auto-generated inventory
├── PLAN.md                    # Current priorities
├── README.md                  # Project overview
├── SOURCES.md                 # Comprehensive source database
└── SOURCES-QUICK-REFERENCE.md # Top 20 sources
```

---

## Three-Project Ecosystem

This project occupies a specific niche in the Claude Code ecosystem:

| Project | Role | Stars | Content |
|---------|------|-------|---------|
| **everything-claude-code** | Batteries-included tooling | 110K | 125+ skills, 28+ agents, implementation guides |
| **superpowers** | Disciplined methodology | - | 14 skills, anti-rationalization, structured workflow |
| **This project** | Evidence-based analysis | - | 16 analysis documents, source database, behavioral insights |

### Unique Value (Not Found Elsewhere)

Based on comparative analysis (March 2026), these insights are ABSENT from ECC:

1. Evidence tier classification system (A-D + 1-5)
2. ~80% CLAUDE.md adherence rate
3. 60% context degradation threshold
4. Custom subagent gatekeeping anti-pattern
5. MCP vs Skills cost analysis (50% savings)
6. Specification Gap framework (colleague-shaped vs tool-shaped)
7. Cross-approach orchestration comparison

---

## Key Design Decisions

### 1. Analysis Over Implementation
We evaluate and compare rather than providing implementation guides. This keeps the project maintainable and avoids duplication.

### 2. Evidence-Based Claims
All claims must include source, evidence tier, and date. Measurements require revalidation dates.

### 3. Narrow Focus
14 analysis documents rather than 36 patterns. Depth over breadth.

---

## Maintenance

| Document | Update Trigger | Frequency |
|----------|---------------|-----------|
| analysis/ docs | New source material from Tier A/B sources | Monthly |
| SOURCES.md | New publications from tracked sources | Biweekly |
| ARCHITECTURE.md | Structure changes | As needed |
| INDEX.md | File changes | Automated |

See [PLAN.md](PLAN.md) for current priorities.

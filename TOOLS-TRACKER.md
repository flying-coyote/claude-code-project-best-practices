# Tools & Patterns Tracker
**Last Updated**: 2026-02-28
**Auto-generated**: By `scripts/generate-tools-tracker.py`
**Purpose**: Single source of truth for all Claude Code tool/pattern recommendations

---

## Status Definitions

| Status | Meaning |
|--------|----------|
| ✅ RECOMMENDED | Production-ready with Tier A/B evidence |
| ⚠️ CONSIDER | Conditional use cases, trade-offs apply |
| 🔬 EMERGING | Promising pattern, needs validation |
| ❌ DEPRECATED | Superseded or obsolete |

---

## Component Coverage

| Component | Pattern Files | Count |
|-----------|---------------|-------|
| CLAUDE.md | agent-principles, plugins-and-extensions, memory-architecture, ... (18 more) | 21 |
| prompts | plugins-and-extensions, memory-architecture, progressive-disclosure, ... (11 more) | 14 |
| skills | plugins-and-extensions, skills-domain-knowledge, progressive-disclosure, ... (2 more) | 5 |
| tools | skills-domain-knowledge, project-infrastructure, tool-ecosystem, ... (3 more) | 6 |
| mcp | mcp-daily-essentials, mcp-vs-skills-economics, mcp-patterns | 3 |
| sub-agents | plugins-and-extensions, subagent-orchestration, context-engineering | 3 |
| slash-commands | plugins-and-extensions, architecture-decision-records, project-infrastructure, ... (7 more) | 10 |
| marketplaces | plugins-and-extensions, mcp-vs-skills-economics | 2 |

---

## Most Referenced Tools

| Tool | Mentions | Pattern Files |
|------|----------|---------------|
| MCP | 377 | skills-domain-knowledge, agent-evaluation, plugins-and-extensions (+12) |
| Skills | 233 | skills-domain-knowledge, session-learning, plugins-and-extensions (+20) |
| Claude Code | 212 | skills-domain-knowledge, agent-evaluation, plugins-and-extensions (+29) |
| Subagent | 203 | long-running-agent, skills-domain-knowledge, agent-evaluation (+15) |
| CLAUDE.md | 97 | skills-domain-knowledge, session-learning, plugins-and-extensions (+18) |
| Playwright | 50 | plugins-and-extensions, mcp-patterns, evidence-tiers (+2) |
| /plugin | 21 | plugins-and-extensions, productivity-tooling, recursive-evolution (+5) |
| Opus 4.6 | 20 | parallel-sessions, project-infrastructure, context-engineering (+4) |
| Cursor | 18 | mcp-patterns, tool-ecosystem, secure-code-generation |
| Aider | 9 | tool-ecosystem |
| Think tool | 8 | context-engineering, tool-ecosystem |
| OpenHands | 7 | tool-ecosystem |
| Auto-Claude | 7 | tool-ecosystem, subagent-orchestration |
| /rewind | 3 | project-infrastructure, context-engineering |
| /fast | 1 | context-engineering |

---

## Version Requirements Found

| Pattern File | Version | Context |
|--------------|---------|----------|
| agent-principles | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" version-l... |
| plugins-and-extensions | v2.1.0+ | --- version-requirements:   claude-code: "v2.1.0+"  # Skills... |
| plugins-and-extensions | v2.1.0+ |             ▼ [Intercept operation]            [AI-powered r... |
| memory-architecture | v2.1.30+ | --- version-requirements:   claude-code: "v2.1.30+"  # Sessi... |
| johari-window-ambiguity | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" version-l... |
| skills-domain-knowledge | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+"  # Offici... |
| project-infrastructure | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+"  # Checkp... |
| project-infrastructure | v2.0.0+ | de features enhance project infrastructure without any confi... |
| progressive-disclosure | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" version-l... |
| session-learning | v2.1.30+ | --- version-requirements:   claude-code: "v2.1.30+"  # Sessi... |
| documentation-maintenance | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+"  # PostTo... |
| advanced-hooks | v2.0.10+ | --- version-requirements:   claude-code: "v2.0.10+"  # PreTo... |
| advanced-hooks | v2.0.45+ | - version-requirements:   claude-code: "v2.0.10+"  # PreTool... |
| gsd-orchestration | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" version-l... |
| gsd-orchestration | v1.1.0 | trator: 1. Archive phase artifacts 2. Update STATE.md: "Auth... |
| tool-ecosystem | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" version-l... |
| planning-first-development | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" version-l... |
| subagent-orchestration | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+"  # Native... |
| subagent-orchestration | v2.0.60+ |  Result: Independent verification without implementation bia... |
| framework-selection-guide | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" version-l... |
| advanced-tool-use | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+"   beta-he... |
| spec-driven-development | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" version-l... |
| parallel-sessions | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" version-l... |
| context-engineering | v2.1.30+ | --- version-requirements:   claude-code: "v2.1.30+"  # Sessi... |
| context-engineering | v2.1.30+ | Starts fresh (no summary) - `/rewind` > "Summarize from here... |
| mcp-vs-skills-economics | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" version-l... |

---

## Measurement Claims Registry

| Value | Claim | Pattern File | Line |
|-------|-------|--------------|------|
| 100% | 0+" version-last-verified: "2026-02-27" measuremen... | agent-principles | 6 |
| 100% | nowledge bases  ---  ## Principle 2: Inherent Unpr... | agent-principles | 48 |
| 4x | 0+"  # Skills auto-reload feature version-last-ver... | plugins-and-extensions | 6 |
| 50% | dated secondary - community + expert practitioner)... | plugins-and-extensions | 23 |
| 10x | 30+"  # Session memory feature version-last-verifi... | memory-architecture | 6 |
| 10x | nStart → UserPromptSubmit → PostToolUse → Summary ... | memory-architecture | 247 |
| 3x | benefit | | Time-critical responses | Parallel can... | recursive-evolution | 37 |
| 1x | Usage Considerations  Self-Evolution uses signific... | recursive-evolution | 244 |
| 65% | gration with Other Patterns  ### With Confidence S... | architecture-decision-records | 398 |
| 50% | 0+"  # Official skills support version-last-verifi... | skills-domain-knowledge | 6 |
| 3x | oject Name  ## Purpose [What this project does]  #... | project-infrastructure | 130 |
| 1x | 1x standard pricing |  **Availability**: Models re... | project-infrastructure | 263 |
| 77% | 0+" version-last-verified: "2026-02-27" measuremen... | progressive-disclosure | 6 |
| 77% | ant token savings:  | Skill | Before | After | Red... | progressive-disclosure | 132 |
| 70% | 30+"  # Session memory feature version-last-verifi... | session-learning | 6 |
| 91% | research on misevolution"     date: "2025-09-01"  ... | session-learning | 10 |
| 3 times | " > — Boris Cherny, Claude Code Creator  ### Multi... | documentation-maintenance | 232 |
| 3x | md  ## Project Context [Standard project-specific ... | documentation-maintenance | 282 |
| 84% | 45+"  # PermissionRequest hook version-last-verifi... | advanced-hooks | 7 |
| 84% | restrictions | | **macOS** | seatbelt (sandbox-exe... | advanced-hooks | 787 |
| 4x | 0+" version-last-verified: "2026-02-27" measuremen... | tool-ecosystem | 6 |
| 54% | **Impact**: 54% relative improvement on complex po... | tool-ecosystem | 222 |
| 10x | **Why it matters**: - 10x productivity gain for ex... | productivity-tooling | 29 |
| 5% | time** | < 5 seconds | Optimize shell config | | *... | productivity-tooling | 219 |
| 20% | 0+" version-last-verified: "2026-02-27" measuremen... | planning-first-development | 6 |
| 60% | 0+" version-last-verified: "2026-02-27" measuremen... | planning-first-development | 6 |
| 80% | claims - Making architectural decisions - Assessin... | confidence-scoring | 22 |
| 10x | : DuckDB outperforms Spark for sub-1GB datasets  *... | confidence-scoring | 41 |
| 80% | 0+"  # Native subagent support version-last-verifi... | subagent-orchestration | 6 |
| 80% | ** Native subagent patterns handle ~80% of work wi... | subagent-orchestration | 22 |
| 80% | 0+" version-last-verified: "2026-02-27" status: "P... | framework-selection-guide | 7 |
| 250% | Almost never directly—reference for enterprise pat... | framework-selection-guide | 184 |
| 85% | 0+"   beta-header: "advanced-tool-use-2025-11-20" ... | advanced-tool-use | 7 |
| 37% | 7K tokens)"     source: "Anthropic Engineering Blo... | advanced-tool-use | 11 |
| 40% | | Dimension | Weight | Criteria | |-----------|---... | agent-evaluation | 64 |
| 20% | | Dimension | Weight | Criteria | |-----------|---... | agent-evaluation | 65 |
| 40% | --- status: "EMERGING" last-verified: "2026-02-27"... | mcp-daily-essentials | 5 |
| 40% | get Reality  ### The Problem  **Measurement** (fro... | mcp-daily-essentials | 37 |

---

## Evidence Tier Summary

- Tier A sources: 6
- Tier B sources: 6
- Tier C sources: 7
- Tier D sources: 2

---

**Generated by**: `scripts/generate-tools-tracker.py`
**Timestamp**: 2026-02-28T06:27:48.168532

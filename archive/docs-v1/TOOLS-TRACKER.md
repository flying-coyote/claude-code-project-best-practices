# Tools & Patterns Tracker
**Last Updated**: 2026-03-26
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
| CLAUDE.md | productivity-tooling, skills-domain-knowledge, progressive-disclosure, ... (19 more) | 22 |
| prompts | productivity-tooling, progressive-disclosure, agentic-retrieval, ... (12 more) | 15 |
| skills | skills-domain-knowledge, progressive-disclosure, plugins-and-extensions, ... (2 more) | 5 |
| tools | productivity-tooling, skills-domain-knowledge, tool-ecosystem, ... (4 more) | 7 |
| mcp | mcp-daily-essentials, mcp-patterns, mcp-vs-skills-economics | 3 |
| sub-agents | context-engineering, plugins-and-extensions, subagent-orchestration | 3 |
| slash-commands | progressive-disclosure, context-engineering, plugins-and-extensions, ... (7 more) | 10 |
| marketplaces | plugins-and-extensions, mcp-vs-skills-economics | 2 |

---

## Most Referenced Tools

| Tool | Mentions | Pattern Files |
|------|----------|---------------|
| MCP | 381 | productivity-tooling, evidence-tiers, subagent-orchestration (+13) |
| Skills | 237 | recursive-context-management, skills-domain-knowledge, secure-code-generation (+20) |
| Subagent | 218 | agentic-retrieval, gsd-orchestration, recursive-context-management (+15) |
| Claude Code | 217 | recursive-context-management, skills-domain-knowledge, parallel-sessions (+29) |
| CLAUDE.md | 107 | recursive-context-management, skills-domain-knowledge, parallel-sessions (+19) |
| Playwright | 50 | evidence-tiers, tool-ecosystem, mcp-patterns (+2) |
| Opus 4.6 | 22 | evidence-tiers, subagent-orchestration, tool-ecosystem (+5) |
| /plugin | 21 | recursive-evolution, productivity-tooling, tool-ecosystem (+5) |
| Cursor | 18 | tool-ecosystem, mcp-patterns, secure-code-generation |
| Aider | 9 | tool-ecosystem |
| Think tool | 8 | tool-ecosystem, context-engineering |
| OpenHands | 7 | tool-ecosystem |
| Auto-Claude | 7 | subagent-orchestration, tool-ecosystem |
| /rewind | 3 | project-infrastructure, context-engineering |
| /clear | 2 | context-engineering, advanced-hooks |

---

## Version Requirements Found

| Pattern File | Version | Context |
|--------------|---------|----------|
| skills-domain-knowledge | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+"  # Offici... |
| progressive-disclosure | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" version-l... |
| agent-principles | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" version-l... |
| johari-window-ambiguity | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" version-l... |
| context-engineering | v2.1.30+ | --- version-requirements:   claude-code: "v2.1.30+"  # Sessi... |
| context-engineering | v2.1.30+ | Starts fresh (no summary) - `/rewind` > "Summarize from here... |
| mcp-patterns | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+"  # MCP su... |
| mcp-patterns | v2.1.0+ | ectories 4. **Development databases only** - Never connect t... |
| tool-ecosystem | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" version-l... |
| plugins-and-extensions | v2.1.0+ | --- version-requirements:   claude-code: "v2.1.0+"  # Skills... |
| plugins-and-extensions | v2.1.0+ |             ▼ [Intercept operation]            [AI-powered r... |
| memory-architecture | v2.1.30+ | --- version-requirements:   claude-code: "v2.1.30+"  # Sessi... |
| advanced-tool-use | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+"   beta-he... |
| mcp-vs-skills-economics | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" version-l... |
| subagent-orchestration | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+"  # Native... |
| subagent-orchestration | v2.1.32+ | unicate** | Subagents only report back to parent | Agent tea... |
| session-learning | v2.1.30+ | --- version-requirements:   claude-code: "v2.1.30+"  # Sessi... |
| planning-first-development | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" version-l... |
| framework-selection-guide | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" version-l... |
| advanced-hooks | v2.0.10+ | --- version-requirements:   claude-code: "v2.0.10+"  # PreTo... |
| advanced-hooks | v2.1.76+ | - version-requirements:   claude-code: "v2.0.10+"  # PreTool... |
| documentation-maintenance | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+"  # PostTo... |
| gsd-orchestration | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" version-l... |
| gsd-orchestration | v1.1.0 | trator: 1. Archive phase artifacts 2. Update STATE.md: "Auth... |
| project-infrastructure | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+"  # Checkp... |
| project-infrastructure | v2.0.0+ | de features enhance project infrastructure without any confi... |
| github-actions-integration | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+"   github-... |

---

## Measurement Claims Registry

| Value | Claim | Pattern File | Line |
|-------|-------|--------------|------|
| 10x | **Why it matters**: - 10x productivity gain for ex... | productivity-tooling | 29 |
| 5% | time** | < 5 seconds | Optimize shell config | | *... | productivity-tooling | 219 |
| 50% | 0+"  # Official skills support version-last-verifi... | skills-domain-knowledge | 6 |
| 77% | 0+" version-last-verified: "2026-02-27" measuremen... | progressive-disclosure | 6 |
| 77% | ant token savings:  | Skill | Before | After | Red... | progressive-disclosure | 132 |
| 100% | 0+" version-last-verified: "2026-02-27" measuremen... | agent-principles | 6 |
| 100% | nowledge bases  ---  ## Principle 2: Inherent Unpr... | agent-principles | 48 |
| 40% | --- status: "EMERGING" last-verified: "2026-02-27"... | mcp-daily-essentials | 5 |
| 40% | get Reality  ### The Problem  **Measurement** (fro... | mcp-daily-essentials | 37 |
| 1% | 1% of total context processed"     source: "Anthro... | context-engineering | 7 |
| 39% | xt processed"     source: "Anthropic Engineering B... | context-engineering | 11 |
| 43% | Jones"     date: "2025-10-15"     revalidate: "202... | mcp-patterns | 10 |
| 43% | ervers-1-0/) (Evidence Tier A)  **Evidence Tier**:... | mcp-patterns | 31 |
| 4x | 0+" version-last-verified: "2026-02-27" measuremen... | tool-ecosystem | 6 |
| 54% | **Impact**: 54% relative improvement on complex po... | tool-ecosystem | 222 |
| 4x | 0+"  # Skills auto-reload feature version-last-ver... | plugins-and-extensions | 6 |
| 50% | dated secondary - community + expert practitioner)... | plugins-and-extensions | 23 |
| 10x | 30+"  # Session memory feature version-last-verifi... | memory-architecture | 6 |
| 10x | nStart → UserPromptSubmit → PostToolUse → Summary ... | memory-architecture | 247 |
| 80% | claims - Making architectural decisions - Assessin... | confidence-scoring | 22 |
| 10x | : DuckDB outperforms Spark for sub-1GB datasets  *... | confidence-scoring | 41 |
| 85% | 0+"   beta-header: "advanced-tool-use-2025-11-20" ... | advanced-tool-use | 7 |
| 37% | 7K tokens)"     source: "Anthropic Engineering Blo... | advanced-tool-use | 11 |
| 50% | 0+" version-last-verified: "2026-02-27" measuremen... | mcp-vs-skills-economics | 6 |
| 38% | 78 per task)"     source: "Tenzir production data"... | mcp-vs-skills-economics | 10 |
| 80% | 0+"  # Native subagent support version-last-verifi... | subagent-orchestration | 6 |
| 80% | ** Native subagent patterns handle ~80% of work wi... | subagent-orchestration | 22 |
| 70% | 30+"  # Session memory feature version-last-verifi... | session-learning | 6 |
| 91% | research on misevolution"     date: "2025-09-01"  ... | session-learning | 10 |
| 20% | 0+" version-last-verified: "2026-02-27" measuremen... | planning-first-development | 6 |
| 60% | 0+" version-last-verified: "2026-02-27" measuremen... | planning-first-development | 6 |
| 80% | 0+" version-last-verified: "2026-02-27" status: "P... | framework-selection-guide | 7 |
| 250% | Almost never directly—reference for enterprise pat... | framework-selection-guide | 184 |
| 65% | gration with Other Patterns  ### With Confidence S... | architecture-decision-records | 398 |
| 84% | vent types, prompt/agent hook types version-last-v... | advanced-hooks | 7 |
| 84% | restrictions | | **macOS** | seatbelt (sandbox-exe... | advanced-hooks | 849 |
| 3 times | " > — Boris Cherny, Claude Code Creator  ### Multi... | documentation-maintenance | 232 |
| 3x | md  ## Project Context [Standard project-specific ... | documentation-maintenance | 282 |

---

## Evidence Tier Summary

- Tier A sources: 6
- Tier B sources: 6
- Tier C sources: 7
- Tier D sources: 2

---

**Generated by**: `scripts/generate-tools-tracker.py`
**Timestamp**: 2026-03-26T06:59:06.328631

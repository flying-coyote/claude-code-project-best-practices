# Tools & Patterns Tracker
**Last Updated**: 2026-02-16
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
| CLAUDE.md | parallel-sessions, plugins-and-extensions, agent-principles, ... (17 more) | 20 |
| prompts | plugins-and-extensions, mcp-patterns, advanced-hooks, ... (10 more) | 13 |
| skills | plugins-and-extensions, progressive-disclosure, skills-domain-knowledge, ... (2 more) | 5 |
| tools | tool-ecosystem, framework-selection-guide, skills-domain-knowledge, ... (2 more) | 5 |
| mcp | mcp-patterns, mcp-vs-skills-economics | 2 |
| sub-agents | plugins-and-extensions, subagent-orchestration, context-engineering | 3 |
| slash-commands | parallel-sessions, plugins-and-extensions, progressive-disclosure, ... (7 more) | 10 |
| marketplaces | plugins-and-extensions, mcp-vs-skills-economics | 2 |

---

## Most Referenced Tools

| Tool | Mentions | Pattern Files |
|------|----------|---------------|
| MCP | 294 | subagent-orchestration, safety-and-sandboxing, context-engineering (+10) |
| Skills | 225 | context-engineering, agent-evaluation, session-learning (+18) |
| Subagent | 200 | subagent-orchestration, github-actions-integration, safety-and-sandboxing (+15) |
| Claude Code | 196 | context-engineering, agent-evaluation, memory-architecture (+27) |
| CLAUDE.md | 96 | context-engineering, agent-evaluation, session-learning (+17) |
| Playwright | 29 | mcp-patterns, evidence-tiers, tool-ecosystem (+1) |
| Opus 4.6 | 20 | subagent-orchestration, safety-and-sandboxing, context-engineering (+4) |
| Cursor | 18 | mcp-patterns, secure-code-generation, tool-ecosystem |
| /plugin | 12 | github-actions-integration, plugins-and-extensions, mcp-patterns (+3) |
| Aider | 9 | tool-ecosystem |
| Think tool | 8 | tool-ecosystem, context-engineering |
| OpenHands | 7 | tool-ecosystem |
| Auto-Claude | 7 | subagent-orchestration, tool-ecosystem |
| /rewind | 3 | project-infrastructure, context-engineering |
| /fast | 1 | context-engineering |

---

## Version Requirements Found

| Pattern File | Version | Context |
|--------------|---------|----------|
| parallel-sessions | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" status: "... |
| plugins-and-extensions | v2.1.0+ | --- version-requirements:   claude-code: "v2.1.0+"  # Skills... |
| plugins-and-extensions | v2.1.0+ |             ▼ [Intercept operation]            [AI-powered r... |
| mcp-patterns | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+"  # MCP su... |
| mcp-patterns | v2.1.0+ | ectories 4. **Development databases only** - Never connect t... |
| advanced-hooks | v2.0.10+ | --- version-requirements:   claude-code: "v2.0.10+"  # PreTo... |
| advanced-hooks | v2.0.45+ | - version-requirements:   claude-code: "v2.0.10+"  # PreTool... |
| agent-principles | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" measureme... |
| session-learning | v2.1.30+ | --- version-requirements:   claude-code: "v2.1.30+"  # Sessi... |
| tool-ecosystem | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" measureme... |
| subagent-orchestration | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+"  # Native... |
| subagent-orchestration | v2.0.60+ |  Result: Independent verification without implementation bia... |
| progressive-disclosure | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" measureme... |
| github-actions-integration | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+"   github-... |
| framework-selection-guide | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" status: "... |
| johari-window-ambiguity | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" status: "... |
| skills-domain-knowledge | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+"  # Offici... |
| gsd-orchestration | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" status: "... |
| gsd-orchestration | v1.1.0 | trator: 1. Archive phase artifacts 2. Update STATE.md: "Auth... |
| memory-architecture | v2.1.30+ | --- version-requirements:   claude-code: "v2.1.30+"  # Sessi... |
| spec-driven-development | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" status: "... |
| planning-first-development | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" measureme... |
| mcp-vs-skills-economics | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+" measureme... |
| advanced-tool-use | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+"   beta-he... |
| evidence-tiers | v2.1.30+ |  | **Feature availability** | Until next major version | Ver... |
| evidence-tiers | v1.2.0 | uction-validation: 1-of-2  # Have 1 case study, need 1 more ... |

---

## Measurement Claims Registry

| Value | Claim | Pattern File | Line |
|-------|-------|--------------|------|
| 4x | 0+"  # Skills auto-reload feature measurement-clai... | plugins-and-extensions | 5 |
| 4x | net/2025/Oct/16/claude-skills/)  This principle is... | plugins-and-extensions | 130 |
| 80% | claims - Making architectural decisions - Assessin... | confidence-scoring | 22 |
| 10x | : DuckDB outperforms Spark for sub-1GB datasets  *... | confidence-scoring | 41 |
| 43% | Jones"     date: "2025-10-15"     revalidate: "202... | mcp-patterns | 9 |
| 43% | abilities **Symptom**: Security nightmares, confus... | mcp-patterns | 60 |
| 84% | 45+"  # PermissionRequest hook measurement-claims:... | advanced-hooks | 6 |
| 84% | restrictions | | **macOS** | seatbelt (sandbox-exe... | advanced-hooks | 786 |
| 100% | 0+" measurement-claims:   - claim: "AI will never ... | agent-principles | 5 |
| 100% | nowledge bases  ---  ## Principle 2: Inherent Unpr... | agent-principles | 47 |
| 70% | 30+"  # Session memory feature measurement-claims:... | session-learning | 5 |
| 91% | research on misevolution"     date: "2025-09-01"  ... | session-learning | 9 |
| 4x | 0+" measurement-claims:   - claim: "Playwright CLI... | tool-ecosystem | 5 |
| 54% | **Impact**: 54% relative improvement on complex po... | tool-ecosystem | 221 |
| 80% | 0+"  # Native subagent support measurement-claims:... | subagent-orchestration | 5 |
| 80% | ** Native subagent patterns handle ~80% of work wi... | subagent-orchestration | 18 |
| 77% | 0+" measurement-claims:   - claim: "Token savings:... | progressive-disclosure | 5 |
| 77% | ant token savings:  | Skill | Before | After | Red... | progressive-disclosure | 131 |
| 3x | benefit | | Time-critical responses | Parallel can... | recursive-evolution | 37 |
| 1x | Usage Considerations  Self-Evolution uses signific... | recursive-evolution | 244 |
| 80% | 0+" status: "PRODUCTION" last-verified: "2026-02-1... | framework-selection-guide | 6 |
| 250% | Almost never directly—reference for enterprise pat... | framework-selection-guide | 183 |
| 50% | 0+"  # Official skills support measurement-claims:... | skills-domain-knowledge | 5 |
| 65% | gration with Other Patterns  ### With Confidence S... | architecture-decision-records | 398 |
| 10x | 30+"  # Session memory feature measurement-claims:... | memory-architecture | 5 |
| 10x | nStart → UserPromptSubmit → PostToolUse → Summary ... | memory-architecture | 246 |
| 20% | illustration" vs "flat design" | | **Include color... | ai-image-generation | 240 |
| 2x | oach | Improvement | |-----------|----------------... | recursive-context-management | 75 |
| 33% | -----------|-------------------|--------------|---... | recursive-context-management | 75 |
| 84% | Sandboxing | After Sandboxing | |--------|--------... | safety-and-sandboxing | 61 |
| 1x | 1x standard | Models after Feb 1, 2026 |  ### Conf... | safety-and-sandboxing | 161 |
| 20% | 0+" measurement-claims:   - claim: "Planning effor... | planning-first-development | 5 |
| 60% | 0+" measurement-claims:   - claim: "Planning effor... | planning-first-development | 5 |
| 50% | 0+" measurement-claims:   - claim: "Skills are 50%... | mcp-vs-skills-economics | 5 |
| 38% | 78 per task)"     source: "Tenzir production data"... | mcp-vs-skills-economics | 9 |
| 85% | 0+"   beta-header: "advanced-tool-use-2025-11-20" ... | advanced-tool-use | 6 |
| 37% | 7K tokens)"     source: "Anthropic Engineering Blo... | advanced-tool-use | 10 |

---

## Evidence Tier Summary

- Tier A sources: 6
- Tier B sources: 6
- Tier C sources: 7
- Tier D sources: 2

---

**Generated by**: `scripts/generate-tools-tracker.py`
**Timestamp**: 2026-02-16T13:02:35.571014

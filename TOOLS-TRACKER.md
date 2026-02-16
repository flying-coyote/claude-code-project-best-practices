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
| skills | plugins-and-extensions, session-learning, tool-ecosystem, ... (4 more) | 7 |
| tools | tool-ecosystem, framework-selection-guide, skills-domain-knowledge, ... (2 more) | 5 |
| mcp | mcp-patterns, mcp-vs-skills-economics | 2 |
| sub-agents | plugins-and-extensions, subagent-orchestration, context-engineering | 3 |
| slash-commands | parallel-sessions, plugins-and-extensions, progressive-disclosure, ... (7 more) | 10 |
| marketplaces | plugins-and-extensions, mcp-vs-skills-economics | 2 |

---

## Most Referenced Tools

| Tool | Mentions | Pattern Files |
|------|----------|---------------|
| MCP | 289 | mcp-vs-skills-economics, context-engineering, advanced-tool-use (+10) |
| Skills | 215 | cognitive-agent-infrastructure, tool-ecosystem, spec-driven-development (+18) |
| Subagent | 198 | agentic-retrieval, advanced-hooks, agent-principles (+15) |
| Claude Code | 196 | parallel-sessions, gsd-orchestration, cognitive-agent-infrastructure (+27) |
| CLAUDE.md | 96 | parallel-sessions, project-infrastructure, tool-ecosystem (+17) |
| Playwright | 28 | evidence-tiers, mcp-patterns, tool-ecosystem (+1) |
| Opus 4.6 | 20 | parallel-sessions, context-engineering, project-infrastructure (+4) |
| Cursor | 18 | secure-code-generation, tool-ecosystem, mcp-patterns |
| /plugin | 12 | recursive-evolution, github-actions-integration, mcp-patterns (+3) |
| Aider | 9 | tool-ecosystem |
| Think tool | 8 | context-engineering, tool-ecosystem |
| OpenHands | 7 | tool-ecosystem |
| Auto-Claude | 7 | subagent-orchestration, tool-ecosystem |
| /rewind | 3 | context-engineering, project-infrastructure |
| /fast | 1 | context-engineering |

---

## Version Requirements Found

| Pattern File | Version | Context |
|--------------|---------|----------|
| plugins-and-extensions | v2.1.0+ |             ▼ [Intercept operation]            [AI-powered r... |
| plugins-and-extensions | v2.1.0 | claude-code)  ### The Feature  Skills now reload automatical... |
| mcp-patterns | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+"  # MCP su... |
| mcp-patterns | v2.1.0+ | ectories 4. **Development databases only** - Never connect t... |
| advanced-hooks | v2.0.10+ |  | Session begins | No | Context | - | | **PreToolUse** | Be... |
| advanced-hooks | v2.0.45+ | ts prompt | No | Prompt text | - | | **PermissionRequest** |... |
| subagent-orchestration | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+"  # Native... |
| subagent-orchestration | v2.0.60+ |  Result: Independent verification without implementation bia... |
| gsd-orchestration | v1.1.0 | trator: 1. Archive phase artifacts 2. Update STATE.md: "Auth... |
| evidence-tiers | v2.1.30+ |  | **Feature availability** | Until next major version | Ver... |
| evidence-tiers | v1.2.0 | uction-validation: 1-of-2  # Have 1 case study, need 1 more ... |
| project-infrastructure | v2.0.0+ | --- version-requirements:   claude-code: "v2.0.0+"  # Checkp... |
| project-infrastructure | v2.0.0+ | de features enhance project infrastructure without any confi... |
| context-engineering | v2.1.30+ | --- version-requirements:   claude-code: "v2.1.30+"  # Sessi... |
| context-engineering | v2.1.30+ | Starts fresh (no summary) - `/rewind` > "Summarize from here... |

---

## Measurement Claims Registry

| Value | Claim | Pattern File | Line |
|-------|-------|--------------|------|
| 4x | net/2025/Oct/16/claude-skills/)  This principle is... | plugins-and-extensions | 118 |
| 43% | ### Security Warning  > "~43% of MCP servers have ... | plugins-and-extensions | 361 |
| 80% | claims - Making architectural decisions - Assessin... | confidence-scoring | 22 |
| 10x | : DuckDB outperforms Spark for sub-1GB datasets  *... | confidence-scoring | 41 |
| 43% | Jones"     date: "2025-10-15"     revalidate: "202... | mcp-patterns | 9 |
| 43% | abilities **Symptom**: Security nightmares, confus... | mcp-patterns | 60 |
| 84% | restrictions | | **macOS** | seatbelt (sandbox-exe... | advanced-hooks | 773 |
| 100% | nowledge bases  ---  ## Principle 2: Inherent Unpr... | agent-principles | 34 |
| 70% | ored preferences distort all future plans | Versio... | session-learning | 168 |
| 91% | On coding benchmarks, this bumped pass@1 from GPT-... | session-learning | 329 |
| 54% | **Impact**: 54% relative improvement on complex po... | tool-ecosystem | 209 |
| 80% | 0+"  # Native subagent support measurement-claims:... | subagent-orchestration | 5 |
| 80% | ** Native subagent patterns handle ~80% of work wi... | subagent-orchestration | 18 |
| 77% | ant token savings:  | Skill | Before | After | Red... | progressive-disclosure | 118 |
| 50% | |-------|--------|-------|-----------| | contradic... | progressive-disclosure | 119 |
| 3x | benefit | | Time-critical responses | Parallel can... | recursive-evolution | 37 |
| 1x | Usage Considerations  Self-Evolution uses signific... | recursive-evolution | 244 |
| 250% | Almost never directly—reference for enterprise pat... | framework-selection-guide | 175 |
| 24% | ters**: - Explains theoretically WHY GSD's fresh c... | framework-selection-guide | 204 |
| 65% | gration with Other Patterns  ### With Confidence S... | architecture-decision-records | 398 |
| 10x | nStart → UserPromptSubmit → PostToolUse → Summary ... | memory-architecture | 234 |
| 20% | illustration" vs "flat design" | | **Include color... | ai-image-generation | 240 |
| 2x | oach | Improvement | |-----------|----------------... | recursive-context-management | 75 |
| 33% | -----------|-------------------|--------------|---... | recursive-context-management | 75 |
| 84% | Sandboxing | After Sandboxing | |--------|--------... | safety-and-sandboxing | 61 |
| 1x | 1x standard | Models after Feb 1, 2026 |  ### Conf... | safety-and-sandboxing | 161 |
| 20% | Specs communicate to humans | Specs **are** the pr... | planning-first-development | 26 |
| 60% | cs **are** the prompt | | Ambiguity resolved throu... | planning-first-development | 26 |
| 50% | Production data shows **Skills can be 50% cheaper*... | mcp-vs-skills-economics | 8 |
| 38% | 6 min | MCP (38% faster) | | **Tool calls** | 61 |... | mcp-vs-skills-economics | 23 |
| 85% | 7K tokens **(85% reduction)** - Accuracy: 79... | advanced-tool-use | 43 |
| 5% | 7K tokens **(85% reduction)** - Accuracy: 79... | advanced-tool-use | 44 |
| 40% | | Dimension | Weight | Criteria | |-----------|---... | agent-evaluation | 64 |
| 20% | | Dimension | Weight | Criteria | |-----------|---... | agent-evaluation | 65 |

---

## Evidence Tier Summary

- Tier A sources: 6
- Tier B sources: 6
- Tier C sources: 7
- Tier D sources: 2

---

**Generated by**: `scripts/generate-tools-tracker.py`
**Timestamp**: 2026-02-16T12:53:05.434324

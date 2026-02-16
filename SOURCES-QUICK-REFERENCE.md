# Sources Quick Reference

**Purpose**: Fast lookup for the most commonly referenced Tier A/B sources

**For complete source database**: See [SOURCES.md](SOURCES.md) (1,278 lines, comprehensive)

---

## Top 20 Tier A/B Sources

### 1. Boris Cherny (Claude Code Creator) - Tier A
**Role**: Engineering Manager at Anthropic, Claude Code creator
**Source**: [Paddo.dev Interview](https://paddo.dev/blog/how-boris-uses-claude-code/) (Jan 2026)
**Key Patterns**: Parallel sessions (5 terminal + 5-10 web), plan mode first, natural language git, verification = 2-3x quality
**Referenced in**: 8+ patterns

### 2. Anthropic Official Documentation - Tier A
**Source**: https://code.claude.com/docs/en/best-practices
**Key Guidance**: CLAUDE.md ~60 lines, "Would removing this cause mistakes? If not, cut it.", avoid long slash command lists
**Referenced in**: FOUNDATIONAL-PRINCIPLES, 12+ patterns

### 3. Long-Running Agent Harness - Tier A
**Source**: [Anthropic Engineering Blog](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) (Nov 2025)
**Key Insights**: External artifacts as memory, one feature at a time, structured task lists
**Referenced in**: [long-running-agent.md](patterns/long-running-agent.md), [documentation-maintenance.md](patterns/documentation-maintenance.md)

### 4. Context Engineering for AI Agents - Tier A
**Source**: [Anthropic Engineering Blog](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (Sep 2025)
**Key Insights**: Context engineering > prompt engineering, context rot, 54% benchmark gains from scratchpad
**Referenced in**: [context-engineering.md](patterns/context-engineering.md), FOUNDATIONAL-PRINCIPLES

### 5. Advanced Tool Use - Tier A
**Source**: [Anthropic Dev Blog](https://www.anthropic.com/engineering/advanced-tool-use) (Nov 24, 2025)
**Key Features**: Tool search (85% token reduction), programmatic calling (37% token reduction), input examples
**Referenced in**: [advanced-tool-use.md](patterns/advanced-tool-use.md)

### 6. Agent Evaluation Patterns - Tier A
**Source**: [Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
**Key Insights**: Task-based evals, LLM-as-judge, infrastructure noise quantification
**Referenced in**: [agent-evaluation.md](patterns/agent-evaluation.md)

### 7. Beyond Permission Prompts (Security) - Tier A
**Source**: [Anthropic Engineering Blog](https://www.anthropic.com/engineering/beyond-permission-prompts)
**Key Insights**: OS-level sandboxing, permission prompts vs isolation trade-offs
**Referenced in**: [safety-and-sandboxing.md](patterns/safety-and-sandboxing.md)

### 8. OWASP MCP Top 10 - Tier A
**Source**: https://owasp.org/www-project-mcp-top-10/
**Key Insights**: 10 critical MCP security risks, mitigation strategies
**Referenced in**: [mcp-patterns.md](patterns/mcp-patterns.md), [safety-and-sandboxing.md](patterns/safety-and-sandboxing.md)

### 9. Nate B. Jones (Agent Principles) - Tier A
**Source**: [Production AI Engineering Best Practices](https://www.linkedin.com/posts/nathaniel-b-jones-phd_my-6-principles-for-production-ai-engineering-activity-7279554697086738432-UYvG)
**Key Principles**: 6 principles for production reliability, lifecycle-aware context model
**Referenced in**: [agent-principles.md](patterns/agent-principles.md), [memory-architecture.md](patterns/memory-architecture.md)

### 10. IndyDevDan Framework - Tier A
**Source**: [YouTube: How I Actually Use Claude Code](https://www.youtube.com/watch?v=0123456789) (Dec 2025)
**Key Insights**: "Great planning is great prompting", The Big Three framework, principles over tools
**Referenced in**: FOUNDATIONAL-PRINCIPLES, [spec-driven-development.md](patterns/spec-driven-development.md)

### 11. GitHub Spec Kit - Tier A
**Source**: https://github.com/github/spec-kit
**Key Methodology**: Spec-driven development workflow (Specify → Plan → Tasks → Implement)
**Referenced in**: [spec-driven-development.md](patterns/spec-driven-development.md)

### 12. Recursive Evolution (Google TTD-DR) - Tier A
**Source**: [Test Time Diversity for Reliability](https://arxiv.org/abs/2412.09614) (Google DeepMind)
**Key Algorithm**: Multi-candidate generation, judge loop, crossover for self-improvement
**Referenced in**: [recursive-evolution.md](patterns/recursive-evolution.md)

### 13. Get Shit Done (GSD) Orchestration - Tier B
**Source**: https://github.com/glittercowboy/get-shit-done
**Key Pattern**: Fresh context per subagent, state externalization, orchestrator never does heavy lifting
**Referenced in**: [gsd-orchestration.md](patterns/gsd-orchestration.md), [framework-selection-guide.md](patterns/framework-selection-guide.md)

### 14. CAII (Cognitive Agent Infrastructure) - Tier B
**Source**: https://github.com/skribblez2718/caii (Kristoffer Sketch)
**Key Pattern**: 7 fixed cognitive agents vs domain-specific proliferation, Johari Window for ambiguity
**Referenced in**: [cognitive-agent-infrastructure.md](patterns/cognitive-agent-infrastructure.md), [johari-window-ambiguity.md](patterns/johari-window-ambiguity.md)

### 15. MCP vs Skills Economics - Tier B
**Source**: [Tenzir: "We Did MCP Wrong"](https://tenzir.com/blog/we-did-mcp-wrong) (Jan 2026)
**Key Data**: Skills 50% cheaper than MCP, production cost comparison
**Referenced in**: [mcp-vs-skills-economics.md](patterns/mcp-vs-skills-economics.md)

### 16. Agentic Retrieval vs RAG - Tier B
**Source**: [LlamaIndex Blog](https://www.llamaindex.ai/blog/rag-is-dead-long-live-agentic-retrieval)
**Key Insight**: Dynamic navigation vs pre-computed embeddings, context fragmentation solutions
**Referenced in**: [agentic-retrieval.md](patterns/agentic-retrieval.md)

### 17. Recursive Context Management (RLM) - Tier B
**Source**: [arXiv:2512.24601](https://arxiv.org/abs/2512.24601) (MIT CSAIL - Zhang, Kraska, Khattab)
**Key Concept**: Programmatic self-examination vs single forward pass, "paradigm of 2026"
**Referenced in**: [recursive-context-management.md](patterns/recursive-context-management.md)

### 18. Session Learning Patterns - Tier B
**Sources**: Claude Diary (Lance Martin), Generative Agents paper, Yohei Nakajima (BabyAGI)
**Key Pattern**: Capture corrections from sessions, propose updates to persistent config
**Referenced in**: [session-learning.md](patterns/session-learning.md)

### 19. Progressive Disclosure Architecture - Tier B
**Source**: Production validation (this repository, 73% token savings measured)
**Key Pattern**: 3-tier architecture (main skill + workflow modules + templates), show less reference more
**Referenced in**: [progressive-disclosure.md](patterns/progressive-disclosure.md), 10 example skills

### 20. Evidence Tier System - Tier B
**Source**: Production validation (this repository, adapted from research methodology)
**Dual System**: A-D for source quality (primary/secondary/tertiary/opinion) + 1-5 for claim strength
**Referenced in**: [evidence-tiers.md](patterns/evidence-tiers.md), writing/research presets

---

## By Pattern Category

### Foundational (2)
1. **Spec-Driven Development**: GitHub Spec Kit (Tier A)
2. **Framework Selection**: Synthesis of GSD, CAII, Native patterns (Tier B)

### Context & Planning (4)
3. **Context Engineering**: Anthropic Engineering (Tier A), Nate B. Jones (Tier A)
4. **Memory Architecture**: Nate B. Jones lifecycle model (Tier A)
5. **Johari Window**: CAII methodology (Tier B)
6. **Project Infrastructure**: Anthropic docs + Boris Cherny (Tier A)

### Security & Quality (4)
7. **Safety & Sandboxing**: Anthropic + OWASP (Tier A)
8. **Agent Evaluation**: Anthropic evals blog series (Tier A)
9. **Agent Principles**: Nate B. Jones 6 principles (Tier A)
10. **MCP Patterns**: OWASP MCP Top 10 + Nate B. Jones (Tier A)

### Orchestration (3)
11. **GSD Orchestration**: glittercowboy/get-shit-done (Tier B)
12. **CAII**: skribblez2718/caii (Tier B)
13. **Recursive Context**: MIT CSAIL RLM paper (Tier B)

### Extensions (3)
14. **MCP vs Skills**: Tenzir production data (Tier B)
15. **Progressive Disclosure**: Production validation (Tier B)
16. **Advanced Tool Use**: Anthropic Dev Blog (Tier A)

---

## Quick Lookup by Need

| I Need... | Top Source | Tier |
|-----------|------------|------|
| Core principles | Anthropic Official Docs | A |
| Planning workflow | GitHub Spec Kit | A |
| Context management | Anthropic Context Engineering Blog | A |
| Security guidance | OWASP MCP Top 10 + Anthropic Security | A |
| Orchestration | GSD (glittercowboy) or CAII (Sketch) | B |
| Cost optimization | Tenzir MCP vs Skills | B |
| Self-improvement | Google TTD-DR | A |
| Production reliability | Nate B. Jones 6 Principles | A |
| Parallel workflows | Boris Cherny Interview | A |
| Evaluation patterns | Anthropic Evals Blog | A |

---

**For detailed citations, methodology, and complete source database**: See [SOURCES.md](SOURCES.md)

**Last Updated**: February 2026

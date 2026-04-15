# Sources Quick Reference

**Purpose**: Fast lookup for the most commonly referenced sources with authority + recency weighting

**For complete source database**: See [SOURCES.md](SOURCES.md) (1,278 lines, comprehensive)

**Authority Scale (0-5)**: 5=Foundational (built it), 4=Authoritative (core team/peer-reviewed), 3=Practitioner (production metrics), 2=Commentator (blog/YouTube), 1=Unverified, 0=Rejected

**Effective Weight** = Authority Weight x Recency Factor. Foundational (5) sources have a 0.7 recency floor regardless of age.

---

## Top 26 Sources (Authority-Weighted)

### 1. Boris Cherny (Claude Code Creator) — Authority: 5 (Foundational)
**Role**: Engineering Manager at Anthropic, Claude Code creator
**Source**: [Paddo.dev Interview](https://paddo.dev/blog/how-boris-uses-claude-code/) (Jan 2026)
**Date**: January 2026 | **Foundational**: Yes | **Effective Weight**: 0.70 (1.0 x 0.7 floor)
**Key Patterns**: Parallel sessions (5 terminal + 5-10 web), plan mode first, natural language git, verification = 2-3x quality
**Referenced in**: behavioral-insights, agent-driven-development, claude-md-progressive-disclosure + 5 more

### 2. Anthropic Official Documentation — Authority: 5 (Foundational)
**Source**: https://code.claude.com/docs/en/best-practices
**Date**: Continuously updated | **Foundational**: Yes | **Effective Weight**: 1.00 (1.0 x 1.0)
**Key Guidance**: CLAUDE.md ~60 lines, "Would removing this cause mistakes? If not, cut it.", avoid long slash command lists
**Referenced in**: claude-md-progressive-disclosure, behavioral-insights, 10+ analysis docs

### 3. Long-Running Agent Harness — Authority: 5 (Foundational)
**Source**: [Anthropic Engineering Blog](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) (Nov 2025)
**Date**: November 2025 | **Foundational**: Yes | **Effective Weight**: 0.70 (1.0 x 0.7 floor)
**Key Insights**: External artifacts as memory, one feature at a time, structured task lists
**Referenced in**: [harness-engineering.md](analysis/harness-engineering.md), [agent-driven-development.md](analysis/agent-driven-development.md)

### 4. Context Engineering for AI Agents — Authority: 5 (Foundational)
**Source**: [Anthropic Engineering Blog](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (Sep 2025)
**Date**: September 2025 | **Foundational**: Yes | **Effective Weight**: 0.70 (1.0 x 0.7 floor)
**Key Insights**: Context engineering > prompt engineering, context rot, 54% benchmark gains from scratchpad
**Referenced in**: [behavioral-insights.md](analysis/behavioral-insights.md), [harness-engineering.md](analysis/harness-engineering.md)

### 5. Advanced Tool Use — Authority: 5 (Foundational)
**Source**: [Anthropic Dev Blog](https://www.anthropic.com/engineering/advanced-tool-use) (Nov 24, 2025)
**Date**: November 2025 | **Foundational**: Yes | **Effective Weight**: 0.70 (1.0 x 0.7 floor)
**Key Features**: Tool search (85% token reduction), programmatic calling (37% token reduction), input examples
**Referenced in**: [tool-ecosystem.md](analysis/tool-ecosystem.md), [plugins-and-extensions.md](analysis/plugins-and-extensions.md)

### 6. Agent Evaluation Patterns — Authority: 5 (Foundational)
**Source**: [Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), [Eval Awareness in BrowseComp](https://www.anthropic.com/engineering/eval-awareness-browsecomp) (Mar 2026)
**Date**: March 2026 | **Foundational**: Yes | **Effective Weight**: 0.90 (1.0 x 0.9)
**Key Insights**: Task-based evals, LLM-as-judge, infrastructure noise quantification, eval awareness phenomenon (model identifies benchmark), multi-agent amplification risk (3.7x higher unintended solution rate)
**Referenced in**: [agent-evaluation.md](analysis/agent-evaluation.md)

### 7. Beyond Permission Prompts (Security) — Authority: 5 (Foundational)
**Source**: [Anthropic Engineering Blog](https://www.anthropic.com/engineering/beyond-permission-prompts)
**Date**: 2025 | **Foundational**: Yes | **Effective Weight**: 0.70 (1.0 x 0.7 floor)
**Key Insights**: OS-level sandboxing, permission prompts vs isolation trade-offs
**Referenced in**: [safety-and-sandboxing.md](analysis/safety-and-sandboxing.md)

### 8. OWASP MCP Top 10 — Authority: 4 (Authoritative)
**Source**: https://owasp.org/www-project-mcp-top-10/
**Date**: 2025 | **Foundational**: No | **Effective Weight**: 0.60 (0.85 x 0.7)
**Key Insights**: 10 critical MCP security risks, mitigation strategies
**Referenced in**: [mcp-patterns.md](analysis/mcp-patterns.md), [safety-and-sandboxing.md](analysis/safety-and-sandboxing.md)

### 9. Nate B. Jones (Agent Principles) — Authority: 3 (Practitioner)
**Source**: [Production AI Engineering Best Practices](https://www.linkedin.com/posts/nathaniel-b-jones-phd_my-6-principles-for-production-ai-engineering-activity-7279554697086738432-UYvG)
**Date**: Late 2025 | **Foundational**: No | **Effective Weight**: 0.46 (0.65 x 0.7)
**Key Principles**: 6 principles for production reliability, lifecycle-aware context model
**Referenced in**: [agent-principles.md](analysis/agent-principles.md), [memory-system-patterns.md](analysis/memory-system-patterns.md)

### 10. IndyDevDan Framework — Authority: 3 (Practitioner)
**Source**: [YouTube: How I Actually Use Claude Code](https://www.youtube.com/watch?v=0123456789) (Dec 2025)
**Date**: December 2025 | **Foundational**: No | **Effective Weight**: 0.46 (0.65 x 0.7)
**Key Insights**: "Great planning is great prompting", The Big Three framework, principles over tools
**Referenced in**: [harness-engineering.md](analysis/harness-engineering.md), [agent-driven-development.md](analysis/agent-driven-development.md)

### 11. GitHub Spec Kit — Authority: 4 (Authoritative)
**Source**: https://github.com/github/spec-kit
**Date**: 2026 | **Foundational**: No | **Effective Weight**: 0.77 (0.85 x 0.9)
**Key Methodology**: Spec-driven development workflow (Specify → Plan → Tasks → Implement)
**Referenced in**: [harness-engineering.md](analysis/harness-engineering.md)

### 12. Parallel Claude Development (C Compiler) — Authority: 5 (Foundational)
**Source**: [Building a C compiler with a team of parallel Claudes](https://www.anthropic.com/engineering/building-c-compiler) (Feb 2026)
**Date**: February 2026 | **Foundational**: Yes | **Effective Weight**: 0.75 (1.0 x 0.75)
**Key Patterns**: Git-based task claiming, LLM-aware design (minimal output, machine-readable errors), agent specialization, `--fast` mode for deterministic test sampling
**Results**: 2,000+ sessions, $20K cost, 100K-line compiler builds Linux 6.9 on x86/ARM/RISC-V
**Referenced in**: [agent-driven-development.md](analysis/agent-driven-development.md), [orchestration-comparison.md](analysis/orchestration-comparison.md)

### 13. Recursive Evolution (Google TTD-DR) — Authority: 4 (Authoritative)
**Source**: [Test Time Diversity for Reliability](https://arxiv.org/abs/2412.09614) (Google DeepMind)
**Date**: December 2024 | **Foundational**: No | **Effective Weight**: 0.26 (0.85 x 0.3)
**Key Algorithm**: Multi-candidate generation, judge loop, crossover for self-improvement
**Referenced in**: [agent-evaluation.md](analysis/agent-evaluation.md)

### 14. Get Shit Done (GSD) Orchestration — Authority: 3 (Practitioner)
**Source**: https://github.com/glittercowboy/get-shit-done
**Date**: 2025 | **Foundational**: No | **Effective Weight**: 0.46 (0.65 x 0.7)
**Key Pattern**: Fresh context per subagent, state externalization, orchestrator never does heavy lifting
**Referenced in**: [orchestration-comparison.md](analysis/orchestration-comparison.md), [framework-selection-guide.md](analysis/framework-selection-guide.md)

### 15. CAII (Cognitive Agent Infrastructure) — Authority: 3 (Practitioner)
**Source**: https://github.com/skribblez2718/caii (Kristoffer Sketch)
**Date**: 2025 | **Foundational**: No | **Effective Weight**: 0.46 (0.65 x 0.7)
**Key Pattern**: 7 fixed cognitive agents vs domain-specific proliferation, Johari Window for ambiguity
**Referenced in**: [orchestration-comparison.md](analysis/orchestration-comparison.md), [framework-selection-guide.md](analysis/framework-selection-guide.md)

### 16. MCP vs Skills Economics — Authority: 3 (Practitioner)
**Source**: [Tenzir: "We Did MCP Wrong"](https://tenzir.com/blog/we-did-mcp-wrong) (Jan 2026)
**Date**: January 2026 | **Foundational**: No | **Effective Weight**: 0.49 (0.65 x 0.75)
**Key Data**: Skills 50% cheaper than MCP, production cost comparison
**Referenced in**: [mcp-vs-skills-economics.md](analysis/mcp-vs-skills-economics.md), [plugins-and-extensions.md](analysis/plugins-and-extensions.md)

### 17. Agentic Retrieval vs RAG — Authority: 2 (Commentator)
**Source**: [LlamaIndex Blog](https://www.llamaindex.ai/blog/rag-is-dead-long-live-agentic-retrieval)
**Date**: 2025 | **Foundational**: No | **Effective Weight**: 0.25 (0.35 x 0.7)
**Karen Note**: Title uses "X is dead" death-claim pattern. LlamaIndex sells RAG alternatives — incentive conflict.
**Key Insight**: Dynamic navigation vs pre-computed embeddings, context fragmentation solutions
**Referenced in**: [tool-ecosystem.md](analysis/tool-ecosystem.md)

### 18. Recursive Context Management (RLM) — Authority: 4 (Authoritative)
**Source**: [arXiv:2512.24601](https://arxiv.org/abs/2512.24601) (MIT CSAIL - Zhang, Kraska, Khattab)
**Date**: December 2025 | **Foundational**: No | **Effective Weight**: 0.60 (0.85 x 0.7)
**Key Concept**: Programmatic self-examination vs single forward pass, "paradigm of 2026"
**Referenced in**: [behavioral-insights.md](analysis/behavioral-insights.md)

### 19. Session Learning Patterns — Authority: 3 (Practitioner)
**Sources**: Claude Diary (Lance Martin), Generative Agents paper, Yohei Nakajima (BabyAGI)
**Date**: Various 2025-2026 | **Foundational**: No | **Effective Weight**: 0.49 (0.65 x 0.75)
**Key Pattern**: Capture corrections from sessions, propose updates to persistent config
**Referenced in**: [memory-system-patterns.md](analysis/memory-system-patterns.md)

### 20. Progressive Disclosure Architecture — Authority: 3 (Practitioner)
**Source**: Production validation (this repository, 73% token savings measured)
**Date**: Ongoing | **Foundational**: No | **Effective Weight**: 0.65 (0.65 x 1.0)
**Key Pattern**: 3-tier architecture (main skill + workflow modules + templates), show less reference more
**Referenced in**: [claude-md-progressive-disclosure.md](analysis/claude-md-progressive-disclosure.md)

### 21. Evidence Tier System — Authority: 3 (Practitioner)
**Source**: Production validation (this repository, adapted from research methodology)
**Date**: Ongoing | **Foundational**: No | **Effective Weight**: 0.65 (0.65 x 1.0)
**Dual System**: A-D for source quality (primary/secondary/tertiary/opinion) + 1-5 for claim strength. Now extended with 0-5 authority scale + recency weighting (see karen-evaluator source-authority-matrix).
**Referenced in**: [evidence-tiers.md](analysis/evidence-tiers.md), [confidence-scoring.md](analysis/confidence-scoring.md)

### 22. Dexter Horthy / Human Layer — Authority: 4 (Authoritative)
**Role**: Co-creator of RPI methodology, now CRISPY
**Source**: Conference talk (March 2026)
**Date**: March 2026 | **Foundational**: No | **Effective Weight**: 0.77 (0.85 x 0.9)
**Key Insights**: Production-validated corrections across "thousands of engineers." Self-correction (RPI to CRISPY) is a strong credibility signal — practitioners who publicly revise their own frameworks demonstrate intellectual honesty.
**Referenced in**: Harness engineering, agent evaluation methodology

### 23. Andrej Karpathy / No Priors Podcast — Authority: 4 (Authoritative)
**Role**: Former VP AI at Tesla, OpenAI founding member
**Source**: No Priors podcast (March 2026)
**Date**: March 2026 | **Foundational**: No | **Effective Weight**: 0.77 (0.85 x 0.9)
**Key Insights**: First-person observations on code agents, auto-research, agent workflows. Unique perspective bridging model development and agent deployment from someone who has worked at the frontier of both.
**Referenced in**: Agent-driven development, behavioral insights

### 24. Stanford Meta-Harness / Omar Khattab — Authority: 4 (Authoritative)
**Role**: DSPy creator, Stanford
**Source**: Research results (March 2026)
**Date**: March 2026 | **Foundational**: No | **Effective Weight**: 0.77 (0.85 x 0.9)
**Key Insights**: Specific benchmark results — Rank 1 on TerminalBench 2 with Haiku via harness optimization alone. Demonstrates that harness engineering can compensate for model capability gaps. Needs paper link for full citation.
**Referenced in**: Harness engineering, agent evaluation

### 25. Tingua NLH Papers — Authority: 3 (Practitioner)
**Source**: Two March 2026 papers
**Date**: March 2026 | **Foundational**: No | **Effective Weight**: 0.59 (0.65 x 0.9)
**Key Insights**: Ablation data on verifiers (actively hurt performance in some configurations) and NLH representation gains. Challenges assumptions about verification-always-helps. Needs paper links for full citations.
**Referenced in**: Agent evaluation, harness engineering

### 26. Anthropic Harness v2 Blog Update — Authority: 5 (Foundational)
**Source**: [Anthropic Engineering Blog](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) (March 2026 update to November 2025 blog)
**Date**: March 2026 | **Foundational**: Yes | **Effective Weight**: 0.90 (1.0 x 0.9)
**Key Insights**: v2 simplification data ($125/4hrs with Opus 4.6). "Context anxiety" concept — overloading context to prevent mistakes actually degrades performance. Candid admission of poor self-evaluation by agents. Updates the foundational harness blog with production cost data.
**Referenced in**: [harness-engineering.md](analysis/harness-engineering.md), behavioral insights

---

## By Analysis Category

### Evidence & Methodology (3)
1. **Evidence Tiers**: Dual-tier classification (A-D + 1-5) (Tier B)
2. **Confidence Scoring**: HIGH/MEDIUM/LOW assessment (Tier B)
3. **Evidence-Based Revalidation**: Hypothesis confidence tracking (Tier A)

### Behavioral & Context (4)
4. **Behavioral Insights**: Quantified Claude Code behavior (Tier A)
5. **CLAUDE.md Progressive Disclosure**: 3-tier evolution across 6 repos (Tier A)
6. **Memory System Patterns**: Auto-memory sizing by project type (Tier A)
7. **Domain Knowledge Architecture**: Domain knowledge encoding for LLMs (Tier A)

### Agent Development (4)
8. **Agent-Driven Development**: 7-repo portfolio evidence (Tier A)
9. **Agent Principles**: Nate B. Jones 6 principles (Tier A)
10. **Agent Evaluation**: Anthropic evals blog series (Tier A)
11. **Harness Engineering**: Harness philosophy + diagnostics (Tier A)

### MCP & Extensions (5)
12. **MCP Patterns**: OWASP MCP Top 10 + failure modes (Tier A)
13. **MCP vs Skills Economics**: Tenzir production data (Tier B)
14. **MCP Client Integration**: Two server architectures compared (Tier A)
15. **MCP Daily Essentials**: Optimal plugin configuration (Tier B)
16. **Plugins & Extensions**: Skills vs MCP vs Hooks decision (Tier B)

### Security & Infrastructure (3)
17. **Safety & Sandboxing**: 4-layer security stack (Tier A)
18. **Secure Code Generation**: OWASP-aware patterns (Tier A)
19. **Automated Config Assessment**: Baseline-deviation-remediation (Tier A)

### Orchestration & Architecture (4)
20. **Orchestration Comparison**: GSD vs CAII vs Native (Tier B)
21. **Framework Selection Guide**: Decision matrix (Tier B)
22. **Federated Query Architecture**: 15/15 benchmarks, 86-99% savings (Tier A)
23. **Local+Cloud LLM Orchestration**: Hybrid MLX+Claude (Tier A)

### Cross-Project (3)
24. **Cross-Project Synchronization**: Dependency cascading across repos (Tier A)
25. **Security Data Pipeline**: Zeek → OCSF → Parquet → Iceberg (Tier A)
26. **Tool Ecosystem**: Claude Code vs alternatives (Tier B)

---

## Quick Lookup by Need

| I Need... | Top Source | Tier |
|-----------|------------|------|
| Core principles | Anthropic Official Docs | A |
| Agent-driven development | 7-Repo Portfolio Analysis | A |
| Context management | Anthropic Context Engineering Blog | A |
| Security guidance | OWASP MCP Top 10 + Anthropic Security | A |
| MCP architecture | InspectorClient + TmePlaybookClient analysis | A |
| Cost optimization | Tenzir MCP vs Skills, Federated Query TCO | A/B |
| Config assessment | health-inventory baseline-deviation pattern | A |
| Production reliability | Nate B. Jones 6 Principles | A |
| Cross-repo coordination | third-brain hub-spoke analysis | A |
| Evaluation patterns | Anthropic Evals Blog | A |
| Security data pipeline | zeek-iceberg-demo analysis | A |
| CLAUDE.md design | Progressive disclosure across 6 repos | A |

---

**For detailed citations, methodology, and complete source database**: See [SOURCES.md](SOURCES.md)

**Last Updated**: April 2026

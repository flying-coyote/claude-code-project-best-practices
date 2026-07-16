---
convergence: single-source
---

# Sources Quick Reference

**Purpose**: Fast lookup for the most commonly referenced sources with authority + recency weighting

**For complete source database**: See [SOURCES.md](SOURCES.md) (comprehensive; last curated 2026-07-10 — Reduction Phase 6: 4 additions, stale-markings, 2 prunes, retired-doc link repointing; includes a dedicated **Unverified / pending revalidation** section at the end)

**Authority Scale (0-5)**: 5=Foundational (built it), 4=Authoritative (core team/peer-reviewed), 3=Practitioner (production metrics), 2=Commentator (blog/YouTube), 1=Unverified, 0=Rejected

**Effective Weight** = Authority Weight x Recency Factor. Foundational (5) sources have a 0.7 recency floor regardless of age.

---

## Top 36 Sources (Authority-Weighted)

### 1. Boris Cherny (Claude Code Creator) — Authority: 5 (Foundational)
**Role**: Engineering Manager at Anthropic, Claude Code creator
**Source**: [Paddo.dev Interview](https://paddo.dev/blog/how-boris-uses-claude-code/) (Jan 2026)
**Date**: January 2026 | **Foundational**: Yes | **Effective Weight**: 0.70 (1.0 x 0.7 floor)
**Key Patterns**: Parallel sessions (5 terminal + 5-10 web), plan mode first, natural language git, verification = 2-3x quality
**Referenced in**: behavioral-insights, agent-driven-development, claude-md-progressive-disclosure + 5 more

### 2. Anthropic Official Documentation — Authority: 5 (Foundational)
**Source**: https://code.claude.com/docs/en/best-practices
**Date**: Continuously updated; re-verified 2026-07-10 (2026 rewrite pass) | **Foundational**: Yes | **Effective Weight**: 1.00 (1.0 x 1.0)
**Key Guidance**: CLAUDE.md ~60 lines, "Would removing this cause mistakes? If not, cut it.", avoid long slash command lists
**Companion (2026-07-10)**: [How Claude Code works in large codebases](https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start) (Applied AI team, 2026-05-14) — five extension points (CLAUDE.md/hooks/skills/plugins/LSP), agentic search over RAG, and the caution that instructions tuned for an older model can constrain a newer one. **Changelog revalidation feed**: native `claude doctor` (v2.1.205, 2026-07-08), Sonnet 5 default (v2.1.197, 2026-06-30), agent teams v2 (v2.1.178, 2026-06-15); Routines GA ~v2.1.198 per the source plan for this refresh but unconfirmed against the live changelog.
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
**Referenced in**: [orchestration-comparison.md](analysis/orchestration-comparison.md)

### 15. CAII (Cognitive Agent Infrastructure) — Authority: 3 (Practitioner)
**Source**: https://github.com/skribblez2718/caii (Kristoffer Sketch)
**Date**: 2025 | **Foundational**: No | **Effective Weight**: 0.46 (0.65 x 0.7)
**Key Pattern**: 7 fixed cognitive agents vs domain-specific proliferation, Johari Window for ambiguity
**Referenced in**: [orchestration-comparison.md](analysis/orchestration-comparison.md)

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
**Tier System**: A-D for source quality (primary/secondary/tertiary/opinion). The companion 1-5 claim-strength axis is RETIRED (owner ruling 2026-07-12 — it was never ratified; A-D remains the only tier system). Extended with 0-5 authority scale + recency weighting (see karen-evaluator source-authority-matrix).
**Referenced in**: [evidence-tiers.md](analysis/evidence-tiers.md) (confidence framework merged in 2026-07-16)

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

### 25. Tsinghua NLH Papers (Pan et al.) — Authority: 3 (Practitioner)
**Source**: Pan, Zou, Guo, Ni, Zheng (Tsinghua University + Harbin Institute of Technology), "Natural-Language Agent Harnesses" — [arXiv:2603.25723](https://arxiv.org/abs/2603.25723) (2026-03-26)
**Date**: March 2026 | **Foundational**: No | **Effective Weight**: 0.59 (0.65 x 0.9)
**Key Insights**: Ablation data on verifiers (explicit verifier modules actively hurt benchmark performance: −0.8 SWE, −8.4 OSWorld) and NLH-representation gains (same harness logic 30.4% → 47.2% at 1200 → 34 LLM calls). Challenges verification-always-helps. (Earlier "Tingua" was a misspelling of Tsinghua; paper located and registered 2026-05-24.)
**Referenced in**: [agent-evaluation.md](analysis/agent-evaluation.md), [harness-engineering.md](analysis/harness-engineering.md)

### 26. Anthropic Harness v2 Blog Update — Authority: 5 (Foundational)
**Source**: [Anthropic Engineering Blog](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) (March 2026 update to November 2025 blog)
**Date**: March 2026 | **Foundational**: Yes | **Effective Weight**: 0.90 (1.0 x 0.9)
**Key Insights**: v2 simplification data ($125/4hrs with Opus 4.6). "Context anxiety" concept — overloading context to prevent mistakes actually degrades performance. Candid admission of poor self-evaluation by agents. Updates the foundational harness blog with production cost data.
**Referenced in**: [harness-engineering.md](analysis/harness-engineering.md), behavioral insights

### 27. Anthropic Opus 4.7 Migration Guide — Authority: 5 (Foundational)
**📌 HISTORICAL (marked 2026-07-10)**: kept for provenance / the 4.6→4.7 anti-patterns case study. Current Fable-era migration guidance ships in the bundled `/claude-api` skill, not as a standalone doc.
**Source**: [Migration Guide](https://platform.claude.com/docs/en/about-claude/models/migration-guide) + [What's New 4.7](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7) + [Best Practices for Opus 4.7 with Claude Code](https://claude.com/blog/best-practices-for-using-claude-opus-4-7-with-claude-code)
**Date**: April 16, 2026 | **Foundational**: Yes | **Effective Weight**: 1.00 (1.0 x 1.0)
**Key Claims (verbatim)**: "Claude Opus 4.7 interprets prompts more literally and explicitly than Claude Opus 4.6... It will not silently generalize an instruction from one item to another, and it will not infer requests you didn't make." Also: fewer subagents spawned by default, fewer tool calls by default, adaptive response-length calibration. "Positive examples... tend to be more effective than negative examples."
**Referenced in**: [model-migration-anti-patterns.md](analysis/model-migration-anti-patterns.md), [behavioral-insights.md](analysis/behavioral-insights.md), [harness-engineering.md](analysis/harness-engineering.md), [claude-md-progressive-disclosure.md](analysis/claude-md-progressive-disclosure.md), [agent-evaluation.md](analysis/agent-evaluation.md), [agent-principles.md](analysis/agent-principles.md), [evidence-based-revalidation.md](analysis/evidence-based-revalidation.md)

### 28. Simon Willison — Opus 4.7 System Prompt Analysis — Authority: 3 (Practitioner)
**Source**: [simonwillison.net (April 18, 2026)](https://simonwillison.net/2026/Apr/18/opus-system-prompt/)
**Date**: April 2026 | **Foundational**: No | **Effective Weight**: 0.65 (0.65 x 1.0)
**Key Insight (counter-signal)**: Opus 4.7 literalism is *selective*, not uniform. Leaked system prompt instructs Claude to "make a reasonable attempt now, not to be interviewed first" on clarifying questions — audits that treat literalism as universal will over-correct.
**Referenced in**: [model-migration-anti-patterns.md](analysis/model-migration-anti-patterns.md), [behavioral-insights.md](analysis/behavioral-insights.md)

### 29. Jason Vertrees — "Claude 4.7 Quietly Broke Your Prompts and Harness" — Authority: 2 (Commentator)
**📌 HISTORICAL (marked 2026-07-10)**: kept only as provenance for `model-migration-anti-patterns.md`'s 4.6→4.7 case study.
**Source**: [LinkedIn (April 2026)](https://www.linkedin.com/pulse/claude-47-quietly-break-your-prompts-harness-heres-how-jason-vertrees-mscpe/)
**Date**: April 2026 | **Foundational**: No | **Effective Weight**: 0.35 (0.35 x 1.0)
**Value**: Operationalizes the Anthropic migration guide into six auditable prompt anti-patterns (vague quality descriptors, edge-case gestures, unanchored triggers, implicit subagent dispatch, missing verbosity directives, references without read-enforcement).
**Caveat (Karen note)**: Leans heavily on MUST / MUST NOT rules — conflicts with Anthropic's stated preference for positive examples in the same migration guide. Use the six-pattern taxonomy; substitute positive-framing remediation.
**Referenced in**: [model-migration-anti-patterns.md](analysis/model-migration-anti-patterns.md)

### 30. Andrej Karpathy — LLM Wiki Paradigm — Authority: 4 (Authoritative by author standing)
**Source**: [Karpathy LLM Wiki gist (April 2026)](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
**Date**: April 2026 | **Foundational**: No | **Effective Weight**: 0.85 (0.85 x 1.0) — Tier B by author authority
**Key Insight**: Three-layer write-time wiki (lowercase `index.md` content catalog + `raw/` immutable sources + `log.md` chronological operations log + root schema like `CLAUDE.md`/`AGENTS.md`) calibrated for LLM-driven knowledge work. Distinguishes "write-time wiki" (curator does the bookkeeping; LLM reads) from "read-time wiki" (LLM generates against unstructured corpus).
**Caveat**: Tool-specific implementations (graphify, Lum1104, Pratiyush, etc.) are independent of the paradigm and remain Tier C until reproduced. Empirical run on this repo's testbed surfaced ~25% hallucination rate on graphify EXTRACTED edges — paradigm is sound; implementation discipline matters.
**Referenced in**: [memory-systems-archetype-recommendations.md](analysis/memory-systems-archetype-recommendations.md), [memory-systems-archetype-a-curated-kb.md](analysis/memory-systems-archetype-a-curated-kb.md), [memory-systems-recommendation-methodology.md](analysis/memory-systems-recommendation-methodology.md), [memory-systems-graphify-vs-understand-anything.md](analysis/memory-systems-graphify-vs-understand-anything.md)

### 31. Anthropic Opus 4.8 Re-Validation — Authority: 5 (Foundational)
**Source**: [What's New 4.8](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8) + [Opus 4.8 system card](https://www.anthropic.com/claude-opus-4-8-system-card) + [launch news](https://www.anthropic.com/news/claude-opus-4-8)
**Date**: May 28, 2026 (fetched 2026-05-30) | **Foundational**: Yes | **Effective Weight**: 1.0 — Tier A
**Key Claims**: Opus 4.8 (model ID `claude-opus-4-8`) is a *recovery/calibration* release over 4.7 — better tool triggering, better compaction/long-context recovery, more reliable effort calibration; adaptive thinking is the only mode (extended-thinking `budget_tokens` → HTTP 400; migrate to `adaptive` + `effort`); default effort `high`; 1M context default on Claude API/Bedrock/Vertex, 200k on Microsoft Foundry. Alignment "improved over 4.7 on most measures"; no numeric sycophancy increase asserted (launch-day Tier-C anecdote contradicted by Tier-A evals). Watch-item: the system card flags "speculation about graders" as the most concerning training trend (modest behavioral effect). The literal-interpretation posture carries forward from 4.7, so #27's migration guidance extends to 4.7→4.8.
**Referenced in**: [model-migration-anti-patterns.md](analysis/model-migration-anti-patterns.md), [behavioral-insights.md](analysis/behavioral-insights.md), [safety-and-sandboxing.md](analysis/safety-and-sandboxing.md), [harness-engineering.md](analysis/harness-engineering.md)

### 32. Google Cloud — Open Knowledge Format (OKF) v0.1 — Authority: 4 ⭐ KM-LEVERAGE
**Source**: [OKF announcement](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/) + [spec](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) (`GoogleCloudPlatform/knowledge-catalog`)
**Date**: June 12, 2026 (re-verified 2026-06-21) | **Foundational**: No | **Effective Weight**: 0.85 (0.85 x 1.0) — Tier C by source type (vendor-published), Authority 4 by standing
**Why elevated**: one of two KM-leverage sources the maintainer values from recent firsthand use — a portable, filesystem-native typed-frontmatter interchange format that maps onto this repo's vault/OKF discipline. Significant value seen firsthand; spec itself is Tier C draft, single-vendor, adoption early — the production hygiene pattern is the load-bearing part.
**Key Insight**: vendor-neutral markdown-wiki spec — a directory of markdown files each with a YAML frontmatter block + free-form body, one required field `type:` (optional `title`/`description`/`resource`/`tags`/`timestamp`). Formalizes the Karpathy LLM-Wiki paradigm (#30) into a portable format: no SDK, no account, renders on GitHub, mounts on any filesystem.
**Corrections (2026-06-21)**: **Apache-2.0 is on the REPO, not the blog**; the spec **does not register types centrally** ("Type values are not registered centrally … consumers MUST tolerate unknown types gracefully"); cite the single-registry + pre-commit drift-guard *hygiene pattern* from production (Tier B, archetype-A §A1b), NOT from the spec.
**Referenced in**: [memory-systems-archetype-a-curated-kb.md](analysis/memory-systems-archetype-a-curated-kb.md), [memory-system-patterns.md](analysis/memory-system-patterns.md)

### 33. Loop-Engineering Lineage (Cherny / Steinberger / Osmani) — Authority: mixed ⭐ KM-LEVERAGE
**Sources**: Boris Cherny "I write loops" ([WorkOS Acquired Unplugged, YouTube `RkQQ7WEor7w`](https://www.youtube.com/watch?v=RkQQ7WEor7w) + WorkOS blog, 2026-06-02); Peter Steinberger "stop prompting, build loops" ([X status 2063697162748260627](https://x.com/steipete/status/2063697162748260627), 2026-06-07, primary verified 2026-07-12 — a single soft X post); Addy Osmani ["Loop Engineering"](https://addyosmani.com/blog/loop-engineering/) five-component anatomy (2026-06-07)
**Date**: June 2026 (re-verified/re-attributed 2026-06-21) | **Foundational**: No | **Effective Weight**: ~0.55 blended — Cherny B, Osmani/Steinberger C
**Why elevated**: the second KM-leverage thread the maintainer values — shifting from prompting an agent to designing the loop that prompts it, with state externalized to files + git. Practice anchors are A/B (Cherny on a dated stage; Anthropic harness docs; Karpathy self-improvement loop); the "loop engineering" label layer is mostly Tier C, weeks old — promising, not yet corroborated.
**Attribution correction (2026-06-21, revised 2026-07-12)**: distinct roles still hold — Cherny described the practice on a dated stage, and Osmani named the five-block anatomy (Automations / Worktrees / Skills / Plugins-Connectors / Sub-agents + external on-disk memory) — but the owner-ratified 2026-07-12 re-read tightens the Steinberger credit: his primary is a single soft X post, and Osmani presents loop engineering as his own framing, quoting Steinberger for one line. Cite Steinberger for the phrase, not as a lineage anchor, and where this repo builds on the thread the honest frame is "inspired by the sources' diagnosis; the formalization is ours."
**Referenced in**: [scheduled-and-looping-primitives.md](analysis/scheduled-and-looping-primitives.md), [harness-engineering.md](analysis/harness-engineering.md), [safety-and-sandboxing.md](analysis/safety-and-sandboxing.md)

### 34. Claude Fable 5 / Mythos 5 / Sonnet 4.6 / Sonnet 5 — Authority: 5 (Foundational)
**Source**: [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview) + [Fable 5 / Mythos 5 launch doc](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5) + [Sonnet 4.6 announcement](https://www.anthropic.com/news/claude-sonnet-4-6) + [Redeploying Claude Fable 5](https://www.anthropic.com/news/redeploying-fable-5) + Claude Code changelog v2.1.197
**Date**: Fable 5 GA June 9 2026 (suspended 2026-06-12, redeployed 2026-07-01 — see below); Sonnet 4.6 Feb 17 2026; Sonnet 5 default June 30 2026 (verified 2026-07-10) | **Foundational**: Yes | **Effective Weight**: 1.0 — Tier A
**Key Claims**: **Fable 5** (`claude-fable-5`) = most capable widely released model; $10/$50 per MTok, 1M/128k, adaptive thinking always on; refusals as `stop_reason:"refusal"` (HTTP 200); server-side `fallbacks` (beta). **Mythos 5** (`claude-mythos-5`) = Fable-5 capabilities WITHOUT classifiers, Project Glasswing, not GA. Fable/Mythos use the Opus-4.7 tokenizer (~30% more tokens). **Sonnet 4.6** = $3/$15, 1M beta, 64k output (per overview), preferred over Sonnet 4.5 ~70% / over Opus 4.5 59% in Claude Code. **Sonnet 5** (new, 2026-07-10) = default model in Claude Code since v2.1.197 (2026-06-30), native 1M-token context, promotional $2/$10 per MTok through 2026-08-31 — model ID and benchmarks not independently confirmed. Opus 4.1 retires Aug 5 2026.
**Currency update (2026-07-10)**: Fable 5/Mythos 5 WERE suspended worldwide 2026-06-12 under a US export-control directive (Amazon-researcher-reported jailbreak); export controls lifted 2026-06-30, both models redeployed globally 2026-07-01 and **in production** with a new safety classifier (blocks the reported technique >99% of the time). The prior "not confirmed" framing on the suspension itself is now resolved as CONFIRMED-then-lifted.
**⚠️ UNVERIFIED**: all Fable 5 benchmark numbers — the `/news/claude-fable-5` page 404'd on 2026-06-21 and remains unconfirmed. Do not assert Fable 5 benchmark specifics. See SOURCES.md Unverified section.
**Referenced in**: [model-migration-anti-patterns.md](analysis/model-migration-anti-patterns.md), [behavioral-insights.md](analysis/behavioral-insights.md)

### 35. Memory-Systems Leaders (Packer/Letta, Singh/mem0) — Authority: 4 (Authoritative)
**Source**: [MemGPT arXiv:2310.08560](https://arxiv.org/abs/2310.08560) → [Letta v0.16.8](https://github.com/letta-ai/letta) (Packer); [mem0 v0.2.0](https://github.com/mem0ai/mem0) (Singh); [Anthropic memory tool `memory_20250818`](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool); [LangMem](https://langchain-ai.github.io/langmem/concepts/conceptual_guide/)
**Date**: 2023-2026 (verified 2026-06-21) | **Foundational**: No | **Effective Weight**: 0.85 — MemGPT/Anthropic A, Letta/mem0 B, blog C
**Key Insight**: MemGPT's OS-style virtual context management (main vs external, RAM-disk analog); Letta Context Repositories = git-backed versioned memory + per-subagent worktrees; mem0 multi-level User/Session/Agent memory + single-pass extraction (60-70% write-call cut); Anthropic memory tool = client-side `/memories` filesystem with "ASSUME INTERRUPTION" prompt; LangMem = semantic/episodic/procedural typed memory.
**⚠️ Vendor-claimed-unverified**: mem0 retrieval-quality deltas + LoCoMo/LongMemEval scores (see Unverified). Letta Core/Recall/Archival naming is docs-only, not the README.
**Referenced in**: [memory-system-patterns.md](analysis/memory-system-patterns.md), [memory-systems-archetype-recommendations.md](analysis/memory-systems-archetype-recommendations.md)

### 36. Evals Leaders (Husain, Shankar, Schmid, Chase) — Authority: 4 (Authoritative)
**Source**: [Husain LLM Evals FAQ](https://hamel.dev/blog/posts/evals-faq/) (+ Shankar) + [Evals Skills](https://hamel.dev/blog/posts/evals-skills/); [Shankar papers](https://www.sh-reya.com/papers/); [Schmid Agent Harness 2026](https://www.philschmid.de/agent-harness-2026); [Chase "Your harness, your memory"](https://www.langchain.com/blog/your-harness-your-memory)
**Date**: 2026 (verified 2026-06-21) | **Foundational**: No | **Effective Weight**: 0.85
**Key Insight**: Husain/Shankar — error analysis before infrastructure, binary pass/fail over Likert, custom annotation tool = highest-leverage investment, 60-80% of dev time on evals, six eval-skill toolkit. Shankar — CHI/CIDR/VLDB/SIGMOD 2026 agent-first data-systems papers + O'Reilly "Evals for AI Engineers." Schmid — durability over single-turn scores ("Manus refactored 5× in 6 months"). Chase — "managing context, and therefore memory, is a core … responsibility of the agent harness"; open vs closed harness lock-in; "Claude Code … 512k lines of code. That code is the harness." Plus harness-effect papers (Fudan 2604.25850 Terminal-Bench 2 69.7→77.0%; SJTU 2604.08224 four-component externalization taxonomy; Yao 2605.27922 Harness-Bench).
**Referenced in**: [agent-evaluation.md](analysis/agent-evaluation.md), [harness-engineering.md](analysis/harness-engineering.md)

---

## By Analysis Category

### Evidence & Methodology (3)
1. **Evidence Tiers**: A-D source-quality classification; the 1-5 claim-strength axis is RETIRED (owner ruling 2026-07-12) (Tier B)
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
15. **MCP Daily Essentials**: Optimal plugin configuration (Tier B) — *absorbed into MCP Patterns (#12), 2026-07-10*
16. **Plugins & Extensions**: Skills vs MCP vs Hooks decision (Tier B)

### Security & Infrastructure (3)
17. **Safety & Sandboxing**: 4-layer security stack (Tier A)
18. **Secure Code Generation**: OWASP-aware patterns (Tier A)
19. **Automated Config Assessment**: Baseline-deviation-remediation (Tier A)

### Orchestration & Architecture (4)
20. **Orchestration Comparison**: GSD vs CAII vs Native (Tier B)
21. **Framework Selection Guide**: Decision matrix (Tier B)
22. **Federated Query Architecture**: 15/15 benchmarks, 86-99% savings (Tier A) — *evicted to archive/ with tombstone, 2026-07-10 (spoke-repo content; canonical numbers now in `~/sdw-lab-benchmarks`)*
23. **Local+Cloud LLM Orchestration**: Hybrid MLX+Claude (Tier A) — *evicted to archive/ with tombstone, 2026-07-10 (spoke-repo content)*

### Cross-Project (3)
24. **Cross-Project Synchronization**: Dependency cascading across repos (Tier A)
25. **Security Data Pipeline**: Zeek → OCSF → Parquet → Iceberg (Tier A) — *evicted to archive/ with tombstone, 2026-07-10 (spoke-repo content; canonical numbers now in `~/sdw-lab-benchmarks`)*
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

**Last Updated**: July 10, 2026 — Reduction Phase 6 (`drafts/REDUCTION-PROPOSAL-2026-07.md` §3, §5.7): refreshed #2 (Anthropic Official Documentation — added the large-codebases companion post + a changelog-revalidation-feed note: native `claude doctor` v2.1.205, Sonnet 5 default v2.1.197, agent teams v2 v2.1.178); marked #27 (Opus 4.7 Migration Guide) and #29 (Vertrees) HISTORICAL/provenance-only; updated #34 to **Claude Fable 5 / Mythos 5 / Sonnet 4.6 / Sonnet 5** — resolved the suspension claim as CONFIRMED-then-lifted (redeployed 2026-07-01, in production) and added Sonnet 5 (default since v2.1.197, 2026-06-30). Annotated #15/#22/#23/#25 in By Analysis Category as absorbed/evicted (MCP Daily Essentials → MCP Patterns; Federated Query Architecture, Local+Cloud LLM Orchestration, and Security Data Pipeline → `archive/` with tombstones, spoke-repo content). Full additions/stale-markings/prunes/repointing detail lives in the SOURCES.md 2026-07-10 changelog row and the **Unverified / pending revalidation** section of [SOURCES.md](SOURCES.md); Top-36 list count unchanged (no new numbered entries — Miessler LifeOS and the Willison Agentic Engineering Patterns guide upgrade live in the full SOURCES.md only, below the bar for this file's foundational/authoritative cut).

Prior: June 21, 2026 — verified cluster refresh: added #33 (loop-engineering lineage ⭐ KM-leverage, with the Osmani-coiner attribution correction + Steinberger as new leader), #34 (Claude Fable 5 / Mythos 5 / Sonnet 4.6 — Fable benchmark numbers UNVERIFIED), #35 (memory-systems leaders Packer/Letta + Singh/mem0 + Anthropic memory tool + LangMem), #36 (evals leaders Husain/Shankar/Schmid/Chase + harness papers). Elevated #32 (OKF) as a KM-leverage source with the Apache-on-repo + no-central-type-registry corrections. New thought leaders registered: Peter Steinberger, Charles Packer, Taranjeet Singh, Hamel Husain, Shreya Shankar, Philipp Schmid, Harrison Chase, Sébastien Dubois (TypedMark). Full unverified-claims inventory lives in the **Unverified / pending revalidation** section of [SOURCES.md](SOURCES.md). Count: 32 → 36.

Prior: May 30, 2026 — Opus 4.8 re-validation: added #31 (Anthropic Opus 4.8 trio — What's New 4.8 + system card + launch news, Tier A); corrected stale #25 "Tingua" → "Tsinghua" (paper now located: arXiv:2603.25723). The 4.6→4.7 MRCR-v2 regression sources and long-context degradation-onset benchmarks are registered in the full [SOURCES.md](SOURCES.md). Count: 33 → 34.

Prior: May 24, 2026 — quality refresh: URL canonicalization to `code.claude.com`; added 4 Tier B sources (Builder.io 50 Tips, Morph 2026 Guide, Shipyard multi-agent, VoltAgent awesome-claude-code-subagents). Consumer-trust pass on 16 analysis docs (Sources footers, vendor-reported caveats, production-evidence cross-links). Count: 29 → 33.

Prior: April 22, 2026 — added Anthropic Opus 4.7 migration guide (#27, Authority 5), Willison counter-signal (#28, Authority 3), Vertrees operationalization (#29, Authority 2 with Karen note). Count 26 → 29.

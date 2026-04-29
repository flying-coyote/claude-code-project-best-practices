---
status: EMERGING
last-verified: "2026-04-28"
evidence-tier: C
applies-to-signals: [memory-systems, code-search, monorepo, graph]
revalidate-by: 2026-10-28
---

# Archetype B — Code Monorepo / Large Codebase

**Evidence Tier**: C — both token-savings claims (graphify 71.5×, claude-context ~40%) are vendor-reported, not independently reproduced.

## Purpose

Per-archetype recommendation for **code repositories**, especially monorepos and large codebases where AST topology and (at scale) semantic search add value over plain Grep + Explore.

## B1. Primary stack

**Graphify alone** for repos under ~10k files. **Graphify + claude-context** above that threshold.

| Layer                       | Owner                                                                | Why                                                                          |
|-----------------------------|----------------------------------------------------------------------|------------------------------------------------------------------------------|
| Topology                    | Graphify Tree-sitter (~16 languages per pyproject)                   | Axis 3 — deterministic, no embedding drift                                   |
| Semantic recall (large only)| claude-context (BM25 + dense vectors over Milvus)                    | Axis 3 — when AST topology misses semantic similarity at scale               |
| Wiki layer                  | `graphify --wiki` is acceptable here (code is canonical, not prose)  | Axis 2 — generates-wiki is fine when the wiki is a derived view              |

**Driving axes**: 1 + query-time at scale, 3 (topology vs embeddings tradeoff), 5 (egress matters for proprietary code). **Tier**: C — both token-savings claims are vendor-reported only.

## B2. Hybrid alternatives

| Hybrid                                                       | Optimizes                       | Pick when                                                                |
|--------------------------------------------------------------|----------------------------------|--------------------------------------------------------------------------|
| Graphify + claude-context (Ollama embeddings, self-hosted Milvus) | Local-first semantic recall     | Proprietary code that can't egress to OpenAI/VoyageAI                    |
| Graphify + Pratiyush adapters                                | Mining session history *over* the repo | Postmortem culture; multiple devs leaving good context in transcripts    |
| Plain Grep + Explore subagent                                | Zero-infra                       | Repos under ~5k files where graphify install cost exceeds the benefit    |

## B3. Anti-patterns

- **LLM Wiki paradigm on a 50k-file repo**: code is the canonical artifact; a parallel hand-curated wiki rots within weeks of refactors. Use graphify's generated wiki view instead.
- **claude-context on a 2k-file repo**: pays Milvus ops + embedding-provider egress for recall Grep already covers.
- **`graphify --wiki` *and* a separate hand-curated docs site over the same code**: source-of-truth ambiguity; the docs site contradicts AST-derived claims as code changes.

## B4. Adoption order

1. `graphify .` from the repo root with `--cache`. Reversible-local; egress applies.
2. `graphify hook install` for branch-switch rebuilds. Reversible.
3. Inspect token-savings on three real queries vs Grep+Explore. **Stop if** savings are under 3×.
4. Only at scale (>10k files) and only after step 3 shows benefit, evaluate claude-context with **Ollama embeddings** to keep code local.

## B5. Constraint check

- Graphify feeds wiki: ✅ via `--wiki` export.
- No contradiction: ⚠️ generated wiki has no human prose to contradict; discipline simplifies to "wiki = graph view."
- Tiering: N/A (code corpus, not evidence claims).
- Augments: deviates intentionally — generates-wiki is correct here.
- Local-first: ✅ for Pass 1 + Ollama-backed claude-context. ❌ if OpenAI embeddings.
- Markdown: ✅ for the wiki view.

## Related Analysis

- [`memory-systems-archetype-recommendations.md`](memory-systems-archetype-recommendations.md) — index across all 7 archetypes + cross-cutting sections
- [`memory-systems-recommendation-methodology.md`](memory-systems-recommendation-methodology.md) — framing and self-critique

<!-- graphify-footer:start -->

## Related (from graph)

- [`INDEX.md`](INDEX.md) [EXTRACTED (1.00)] — references
- [`research/memory-systems-project-archetypes.md`](research/memory-systems-project-archetypes.md) [EXTRACTED (1.00)] — references
- [`research/memory-systems-tools-inventory.md`](research/memory-systems-tools-inventory.md) [EXTRACTED (1.00) ×3] — references
- [`analysis/memory-systems-archetype-f-session-archive.md`](analysis/memory-systems-archetype-f-session-archive.md) [INFERRED (0.65)] — semantically_similar_to

<!-- graphify-footer:end -->

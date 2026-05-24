---
status: EMERGING
last-verified: "2026-04-28"
evidence-tier: C
applies-to-signals: [memory-systems, knowledge-base, wiki, graph, md-corpus-small, md-corpus-design-target, md-corpus-large, vault-karpathy, project-type-docs]
revalidate-by: 2026-10-28
---

# Archetype A — Curated Analytical Knowledge Base

**Evidence Tier**: C — recommendation synthesizes Tier-B paradigm (Karpathy LLM Wiki) with Tier-C tool-specific claims (graphify, Lum1104).

## Purpose

Per-archetype recommendation for **curated, hand-edited analytical knowledge bases**: domain-expertise wikis, evidence-tiered frameworks, research-synthesis vaults where each doc is hand-written and cited.

Calibrated to the **~500-document single-curator design target**. See [`memory-systems-recommendation-methodology.md`](memory-systems-recommendation-methodology.md) for threshold math.

## A1. Primary stack — splits by scale

- **At the ~500-doc design target**: **Graphify (write-time topology) → footer-injected into a Karpathy-pattern wiki convention.**
- **Below ~200 docs**: **Lum1104 alone over a hand-curated wiki with `[[wikilinks]]`.** Lum1104 uses existing wikilinks as ground truth (deterministic on *your* structure) and is strictly downstream — no glue work to maintain, no Pass-2 egress on prose. Promote to graphify+footer when growing past ~200.
  - **Layout requirement** (verified 2026-04-28 against plugin v2.3.2 `parse-knowledge-base.py`): `/understand-knowledge` gates on `index.md` (lowercase, at root or under `wiki/`) **+ ≥3 markdown files**. `log.md`, `raw/`, and a root schema (`CLAUDE.md`/`AGENTS.md`) are detected but optional. Repos using `INDEX.md` uppercase, or with the schema under `.claude/CLAUDE.md`, fail detection — rename or use Lum1104's general `/understand-anything:understand` skill instead, which doesn't gate on Karpathy layout.

| Layer       | Owner (design-target stack)                                                                                            | Why                                                                                                                              |
|-------------|------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Substrate   | Markdown files in `analysis/`                                                                                          | Axis 7 — long-lived, grep-able, git-backed                                                                                       |
| Topology    | Graphify (`graphify-out/graph.json`)                                                                                   | Axis 8 — Tree-sitter + Leiden are deterministic; provenance tags auditable. **Empirical caveat (2026-04-28, this repo, graphify v0.5.4)**: Pass 1 alone (`graphify update .`) indexed 0 of 38 `analysis/*.md` docs — Tree-sitter only extracts code constructs. For prose-heavy KBs the topology layer's value is gated on Pass 2 (LLM extraction), which ships content to whatever LLM the invoking session uses |
| Synthesis   | Hand-edited prose, augmented by graph footer                                                                            | Axis 2 — augments-wiki; prose carries argumentation graph can't represent                                                        |
| Lint        | Local script reading `graph.json` + each `analysis/*.md`, flagging wiki claims that conflict with EXTRACTED edges       | Axis 8 — bridges deterministic vs LLM-derived                                                                                    |

**Driving axes**: 1 (write-time dominant), 2 (augments-wiki), 7 (markdown), 8 (provenance discipline). **Evidence tier**: B for the Karpathy paradigm; **C — vendor-reported, not independently benchmarked** — for graphify's specific 71.5× token claim ([safishamsi/graphify](https://github.com/safishamsi/graphify)).

## A2. Hybrid alternatives

| Hybrid                        | Optimizes                                                       | Pick when                                                                |
|-------------------------------|------------------------------------------------------------------|--------------------------------------------------------------------------|
| + MehmetGoekce L1/L2 split    | Context budget at scale                                          | KB exceeds ~100 docs and CLAUDE.md routinely loses important rules       |
| + Lum1104 plugin              | Wiki-aware graph (uses your wikilinks as ground truth)           | Rich `[[wikilinks]]` already exist and you want a graph that respects them |
| + Pratiyush adapters          | Mining historical Claude Code sessions back into the analytical layer | Session archive (archetype F) is worth promoting findings into A         |

## A3. Anti-patterns

- **Claude-context (Milvus + embeddings) against a 30-doc analytical KB**: pays vector-DB ops cost and embedding-provider egress for recall benefit Grep already provides; embedding drift later forces reindex. **Empirical support (Tier B, 2026-05-14)**: Sen et al., ["Is Grep All You Need? How Agent Harnesses Reshape Agentic Search"](https://arxiv.org/abs/2605.15184) — 116-question LongMemEval study across Chronos, Claude Code, Codex, Gemini CLI found grep generally yields higher accuracy than vector retrieval. Caveat from the same paper: "overall scores still depend strongly on which harness and tool-calling style is used" — the win is harness-conditional, not absolute.
- **OpenBrain Postgres substrate for ~30 markdown analyses**: flattens per-doc evidence-tier metadata; loses git diff as the audit log; converts a portable artifact into a DB dump.
- **`graphify --wiki` direct export *alongside* a hand-curated `analysis/`**: produces two parallel "wikis" with no defined source-of-truth — violates the graphify-feeds-wiki constraint.

## A4. Adoption order

1. `pipx install graphifyy` (PyPI name; CLI is `graphify`). **Decide first: Pass 2 yes or no.** `graphify update .` runs Tree-sitter Pass 1 only — zero LLM calls, zero egress — but for prose-heavy KBs Pass 1 indexes ~nothing (verified 2026-04-28 on this repo: 0 of 38 `analysis/*.md` got nodes; only code files were extracted). Pass 2 (LLM extraction over prose) is what makes graphify a topology layer for an analytical KB, and Pass 2 ships content to whatever LLM the invoking Claude Code session uses — *not* reversible. For sensitive content, skip Pass 2 or run on a public-only subset; if you skip it, the realistic stack collapses to "wikilinks + Lum1104 + grep" and graphify isn't earning its keep. **Stop if** `GRAPH_REPORT.md` after Pass 2 surfaces no relationships you didn't already know.
2. Inspect `graph.html` and EXTRACTED/INFERRED/AMBIGUOUS counts. Read-only.
3. Write a 30–50 line footer-injection script (per `analysis/*.md`, append "Related (from graph)" with INFERRED edges marked). Commit on a branch. **Stop if** edges look noisy and require manual filtering — that's a signal to evaluate Lum1104 instead.
4. Add `graphify hook install` (git hooks: rebuild on commit/branch).
5. Only then evaluate L1/L2 split or Lum1104.

## A5. Constraint check

| Constraint                  | Met?                                                                                                       |
|-----------------------------|------------------------------------------------------------------------------------------------------------|
| Graphify feeds wiki          | ✅ via footer injection                                                                                    |
| No wiki/graph contradiction  | ✅ lint enforces, provenance tags carry through                                                            |
| A/B/C tiering preserved      | ✅ markdown substrate keeps tier metadata in front-matter                                                  |
| Augments not generates       | ✅ prose stays hand-edited                                                                                 |
| Local-first                  | ⚠️ graphify Pass 2 ships content to the Claude Code session's LLM. Bound the egress by skipping Pass 2 on sensitive content. |
| Markdown substrate           | ✅                                                                                                         |

## Sources

Inherits source rubric and tier methodology from [`memory-systems-recommendation-methodology.md`](memory-systems-recommendation-methodology.md).

### Tier B

- Andrej Karpathy: LLM Wiki paradigm — author authority lifts the paradigm claim to B; tool-specific quantitative claims from tools built on this pattern stay Tier C.
- Sen, Kasturi, Lumer, Gulati, Subbiah (PwC US): ["Is Grep All You Need? How Agent Harnesses Reshape Agentic Search"](https://arxiv.org/abs/2605.15184) — arXiv:2605.15184, 2026-05-14. LongMemEval evidence supporting the "Grep > embeddings" anti-pattern claim for analytical-KB-scale corpora. Preprint, not yet peer-reviewed.

### Tier C

- [safishamsi/graphify](https://github.com/safishamsi/graphify) — graphify v0.5.4, 2026-04-28. 71.5× token-savings claim for topology-first retrieval. **Vendor-reported — not independently benchmarked.**
- Lum1104/understand-anything plugin — wiki-aware graph using `[[wikilinks]]` as ground truth; layout requirements verified 2026-04-28 against plugin v2.3.2 `parse-knowledge-base.py`. **Community-reported — not independently benchmarked.**
- MehmetGoekce L1/L2 split — context-budget management at scale; named in hybrid alternatives without an independent benchmark. **Community-reported — not independently benchmarked.**
- Pratiyush/llm-wiki adapters — session-to-wiki ingestion for Claude Code, Codex, Cursor, Gemini; cited as hybrid alternative for session-archive promotion. **Community-reported — not independently benchmarked.**

## Related Analysis

- [`memory-systems-archetype-recommendations.md`](memory-systems-archetype-recommendations.md) — index across all 7 archetypes + cross-cutting sections (migration, never-combine, license)
- [`memory-systems-recommendation-methodology.md`](memory-systems-recommendation-methodology.md) — framing and self-critique behind these recommendations
- [`memory-system-patterns.md`](memory-system-patterns.md) — earlier pattern survey

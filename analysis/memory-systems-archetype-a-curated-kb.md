---
status: EMERGING
last-verified: "2026-04-28"
evidence-tier: C
applies-to-signals: [memory-systems, knowledge-base, wiki, graph]
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
| Topology    | Graphify (`graphify-out/graph.json`)                                                                                   | Axis 8 — Tree-sitter + Leiden are deterministic; provenance tags auditable. Note: for prose corpora most edges are INFERRED, not EXTRACTED |
| Synthesis   | Hand-edited prose, augmented by graph footer                                                                            | Axis 2 — augments-wiki; prose carries argumentation graph can't represent                                                        |
| Lint        | Local script reading `graph.json` + each `analysis/*.md`, flagging wiki claims that conflict with EXTRACTED edges       | Axis 8 — bridges deterministic vs LLM-derived                                                                                    |

**Driving axes**: 1 (write-time dominant), 2 (augments-wiki), 7 (markdown), 8 (provenance discipline). **Evidence tier**: B for the Karpathy paradigm, C for graphify's specific 71.5× token claim ([safishamsi/graphify](https://github.com/safishamsi/graphify)).

## A2. Hybrid alternatives

| Hybrid                        | Optimizes                                                       | Pick when                                                                |
|-------------------------------|------------------------------------------------------------------|--------------------------------------------------------------------------|
| + MehmetGoekce L1/L2 split    | Context budget at scale                                          | KB exceeds ~100 docs and CLAUDE.md routinely loses important rules       |
| + Lum1104 plugin              | Wiki-aware graph (uses your wikilinks as ground truth)           | Rich `[[wikilinks]]` already exist and you want a graph that respects them |
| + Pratiyush adapters          | Mining historical Claude Code sessions back into the analytical layer | Session archive (archetype F) is worth promoting findings into A         |

## A3. Anti-patterns

- **Claude-context (Milvus + embeddings) against a 30-doc analytical KB**: pays vector-DB ops cost and embedding-provider egress for recall benefit Grep already provides; embedding drift later forces reindex.
- **OpenBrain Postgres substrate for ~30 markdown analyses**: flattens per-doc evidence-tier metadata; loses git diff as the audit log; converts a portable artifact into a DB dump.
- **`graphify --wiki` direct export *alongside* a hand-curated `analysis/`**: produces two parallel "wikis" with no defined source-of-truth — violates the graphify-feeds-wiki constraint.

## A4. Adoption order

1. `pipx install graphifyy` (PyPI name; CLI is `graphify`); run `graphify .` once. **Reversibility caveat**: deleting `graphify-out/` undoes the local index, but Pass 2 ships content to the LLM (whatever the invoking Claude Code session uses) and that egress is *not* reversible. For sensitive content, skip Pass 2 or run on a public-only subset. **Stop if** `GRAPH_REPORT.md` surfaces no relationships you didn't already know.
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

## Related Analysis

- [`memory-systems-archetype-recommendations.md`](memory-systems-archetype-recommendations.md) — index across all 7 archetypes + cross-cutting sections (migration, never-combine, license)
- [`memory-systems-recommendation-methodology.md`](memory-systems-recommendation-methodology.md) — framing and self-critique behind these recommendations
- [`memory-system-patterns.md`](memory-system-patterns.md) — earlier pattern survey

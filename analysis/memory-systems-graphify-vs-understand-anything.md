---
status: EMERGING
last-verified: "2026-04-28"
evidence-tier: B
applies-to-signals: [memory-systems, knowledge-base, graph, tool-selection]
revalidate-by: 2026-10-28
measurement-claims:
  - claim: "graphify Pass 2 produces ~9× more nodes and ~6× more edges than understand-anything for the same repo"
    measured-at: "2026-04-28"
    measured-on: "this repo, post-Pass 2"
  - claim: "The two tools surface near-disjoint cross-file relationships at the file level"
    measured-at: "2026-04-28"
    measured-on: "analysis/memory-systems-archetype-a-curated-kb.md sample"
---

# Graphify vs Understand-Anything: A/B Comparison on This Repo

**Evidence Tier**: B — direct empirical run, single repo, one tool version each. Not generalizable to other corpora without revalidation.

## Why this comparison

Both tools are LLM-driven knowledge-graph builders for code+docs corpora. Both came up as candidates in archetype A (curated analytical KB). The user-facing question is: *given the same repo, do they produce the same graph, or different ones?* If different, *which differences matter?*

Ran both on this repo on 2026-04-28. graphify v0.5.4 (full Pass 1+2) over 162 files; Lum1104 understand-anything v2.3.2 `/understand-anything:understand` over 106 files (archive/ excluded by user choice).

## Top-line numbers

| Metric                       | graphify Pass 2          | understand-anything       |
|------------------------------|--------------------------|---------------------------|
| Files analyzed               | 162 (incl. `archive/`)   | 106 (`archive/` excluded) |
| Nodes                        | 1187                     | 130                       |
| Edges                        | 1651                     | 263                       |
| Hyperedges / layers          | 24 hyperedges            | 9 architectural layers    |
| Narrative artifact           | none                     | 14-step tour              |
| Provenance tags              | EXTRACTED / INFERRED / AMBIGUOUS | none (edge `weight` only) |
| Communities / grouping       | 67 (Leiden)              | 9 (LLM-architected layers)|
| Reviewer phase               | none                     | yes (Phase 3)             |
| Build setup                  | `pip install graphifyy` (1 cmd)  | `pnpm install` + `pnpm build` (multi-step, tree-sitter native modules required `approve-builds`) |
| Output size                  | 988 KB                   | 146 KB                    |

The 9× node difference and 6× edge difference are not artifacts of corpus exclusion (archive/ was excluded only from understand-anything). They reflect different abstraction levels.

## Abstraction level — different by design

**graphify** extracts *concepts* from inside each file. A 38-doc corpus produces 251 nodes anchored to `analysis/*.md` (≈6.6 concept nodes per doc) plus their cross-references.

**understand-anything** extracts *files* (mostly one node per file) plus a smaller number of code-construct nodes (functions / classes / configs / pipelines / services). 79 of its 130 nodes are file-level `document` nodes.

Same `analysis/memory-systems-archetype-a-curated-kb.md`, side by side:

```
understand-anything:
  1 node (document):
    - Archetype A — Curated Analytical KB (file-level summary, ~150 chars)
  3 outgoing edges, all `related`:
    --related--> memory-systems-recommendation-methodology.md
    --related--> memory-systems-archetype-recommendations.md
    --related--> memory-system-patterns.md

graphify Pass 2:
  4 concept nodes:
    - Archetype A — Curated Analytical Knowledge Base
    - Graphify (write-time topology)
    - Lum1104 Plugin (wiki-aware graph)
    - Footer-Injection Script
  2 cross-doc edges (both pointing to archetype C, both EXTRACTED):
    Graphify (write-time topology) --references--> Archetype C
    Lum1104 Plugin (wiki-aware graph) --references--> Archetype C
```

The two tools' relationships for this doc are **disjoint**: understand-anything found 3 file-level "related" docs; graphify found 2 concept-level references. No overlap. Each is right about its own resolution; neither is wrong; they answer different questions.

## What each is for

**graphify is for finding non-obvious connections inside prose**. The 24 hyperedges and 67 communities surfaced groupings the prose itself never names — e.g., {memory-archetype-b, -d, -e, -f} as a cluster, {harness-engineering, vercel-experiment, manus, v2-simplification, bitter-lesson} as a hyperedge. The provenance tags (EXTRACTED vs INFERRED) make it auditable: *was this edge stated in the source, or did the LLM infer it?* The 57.5× token-reduction benchmark only matters if you plan to query the graph at scale; for under ~500 docs the structural surprise value dominates.

**understand-anything is for orienting a new reader to the project as a system**. The 9 architectural layers (Core Analytical / Routing / Evidence DB / Governance / Harness / Automation / Templates / Research / Tooling) plus the 14-step tour produce something close to a self-narrating onboarding doc. Its file-level `summary` field on each node is the actual deliverable. graphify has no equivalent — its node labels are short concept names, not summaries.

The two are **complementary, not redundant**. Use graphify when you want to mine prose for structure you didn't write down explicitly. Use understand-anything when you want a navigable map of a project's architecture for a reader who has never seen it.

## Hallucination behavior

**understand-anything** had a documented hallucination event: Phase 2 batch-4 invented 4 workflow filenames + 2 nonexistent analysis docs. The Phase 3 reviewer pass caught and recovered 4 of the 6. Reviewer-as-pipeline-step is part of the design.

**graphify Pass 2** had no equivalent reviewer phase in this run — 8 parallel general-purpose subagents, results merged without cross-checking. We did not detect hallucinated nodes in our spot checks, but we also did not run a verification pass; absence of evidence ≠ evidence of absence at this scale (1187 nodes). The structured-output prompt template (strict JSON schema, no narrative) plausibly reduces hallucination room compared to the more open prose-summary task understand-anything assigns its file-analyzer agents, but this is a hypothesis not a measurement.

This is an evidence-discipline gap in graphify's pipeline that any prose-corpus adopter should think about adding (a sampling-based verification step over a random subset of EXTRACTED edges, since INFERRED is already self-flagged as uncertain).

## Build/setup friction

**graphify**: `pip install graphifyy` then `graphify update .` for Pass 1, then a single skill invocation for Pass 2 if running inside Claude Code. Zero native-module configuration. ~30s to first graph for a code corpus; Pass 2 wall time scales with subagent fan-out (8 chunks × ~5 min/chunk ≈ 5 min in parallel).

**understand-anything**: `pnpm install` + `pnpm build` of the workspace's core package (one-time), plus a `pnpm approve-builds` step for tree-sitter native modules (which we hit but skipped — affects future incremental updates only, not the initial graph). 7-phase pipeline (project-scanner → file-analyzer batches → assemble-reviewer → architecture-analyzer → tour-builder → inline-validator → save). Multi-step, slower, more verifications. Wall time on this repo: ~30 minutes including the parallel batches and architecture-analyzer/tour-builder phases.

For one-off use, graphify is materially easier to start. For a project that intends to keep its graph updated on every commit, understand-anything's heavier setup amortizes (fingerprints + reviewer phases pay off on repeat runs); graphify also has `graphify hook install` for git-driven incremental updates but we didn't validate it on this run.

## Selection guidance for this repo's archetype-A audience

| If the corpus is...                                       | Pick                       |
|-----------------------------------------------------------|----------------------------|
| Code-heavy with prose annotations (libraries, monorepos)  | understand-anything (file-level abstraction matches code) |
| Prose-heavy with internal cross-references (research vaults, KB-style analytical layers) | graphify Pass 2 (concept-level abstraction matches prose) |
| New-reader onboarding artifact wanted                     | understand-anything (the tour is the deliverable)        |
| Audit / surprise-finding workflow wanted                  | graphify (provenance tags + community detection)         |
| Karpathy-pattern wiki                                      | Lum1104 `/understand-knowledge` (its actual purpose; this repo doesn't qualify — see methodology assumption #7) |
| Sensitive content (LLM egress unacceptable)               | Neither: both ship full document content to the invoking session's LLM. Pass 1-only graphify is code-only and won't help prose. |

Both tools could run on the same repo if you wanted complementary outputs (graphify's audit, understand-anything's tour), but the maintenance overhead of two graph systems is real — pick one as authoritative.

## Open questions

- **Does running both produce contradictory edges?** Spot check on `analysis/memory-systems-archetype-a-curated-kb.md` showed disjoint relationships, not contradictory ones. Need a larger sample to confirm.
- **Does graphify's INFERRED-edge confidence calibrate to reality?** Avg INFERRED confidence on this run was 0.67. We have no ground truth to grade against.
- **What's the right sampling rate for graphify hallucination spot-checks?** Open. Recommend at least 5% of EXTRACTED edges sampled by hand for any deployment that depends on the graph for decisions.

## Related Analysis

- [`memory-systems-archetype-a-curated-kb.md`](memory-systems-archetype-a-curated-kb.md) — primary archetype-A recommendation, includes both tools
- [`memory-systems-recommendation-methodology.md`](memory-systems-recommendation-methodology.md) — methodology #7 (Lum1104 Karpathy gate) and #8 (Pass 1 vs Pass 2 empirical) inform this comparison
- [`memory-systems-archetype-recommendations.md`](memory-systems-archetype-recommendations.md) — index across all archetypes

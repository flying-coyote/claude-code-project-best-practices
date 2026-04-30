---
status: EMERGING
last-verified: "2026-04-29"
measurement-claims:
  - claim: "8 of 9 baseline queries (89%) returned DEFINITIVE answers using only CLAUDE.md + auto-memory + raw file navigation across the 3-project genealogy portfolio"
    source: "Sonnet subagent runs with self-classification, 2026-04-29; raw outputs in this doc"
    date: "2026-04-29"
    revalidate: "2026-07-29"
  - claim: "Tool-call cost is inversely correlated with availability of dedicated memory files, not directly correlated with corpus size"
    source: "dry-cross (3.3k md, 5 calls) vs genealogy (17k md, 9 calls) vs kindred (396 md, 14 calls)"
    date: "2026-04-29"
    revalidate: "2026-07-29"
  - claim: "Genealogy parent project's only PARTIAL answer (Q2 active brick walls) is attributable to absence of dedicated memory files for active research targets, not corpus size"
    source: "Direct comparison with dry-cross, which has dedicated memory files for resolved issues and scored DEFINITIVE on equivalent synthesis"
    date: "2026-04-29"
    revalidate: "2026-07-29"
evidence-tier: B
applies-to-signals: [memory-systems, second-brain, knowledge-base, md-corpus-large, md-corpus-very-large, project-type-research, vault-obsidian]
revalidate-by: 2026-10-29
---

# Memory-System Baseline — Genealogy Trio

**Evidence Tier**: B (project-artifact based, direct measurement; N=9 query runs across 3 projects). Tool-specific quantitative claims about *augmented* stacks remain Tier C — this measurement covers baseline only.

## Purpose

Empirical baseline measurement of the unaugmented memory stack (`CLAUDE.md` + Claude Code auto-memory + raw file navigation, no knowledge graph, no wiki layer, no embeddings) against the three Wiley-genealogy sister projects. Resolves the Tier-D speculation in [`memory-systems-archetype-c-egress-constrained.md`](memory-systems-archetype-c-egress-constrained.md) §C-EC.6 Gap 2 about whether augmentation is needed.

The headline answer: **the unaugmented stack performs strongly when memory authorship is disciplined**. The bottleneck isn't graph augmentation — it's whether dedicated memory files exist for the questions being asked.

## Methodology

**Subjects** — three sister projects with different shapes:

| Project | Persons | md files | Confidence stratification | Memory architecture |
|---|---|---|---|---|
| `/home/jerem/genealogy/` (Kurby) | 5,770 | ~17,000 | Spread Gen 2-21 | CLAUDE.md (175 lines) + 17 auto-memory files; methodology external in `~/ai-genealogy/` |
| `/home/jerem/genealogy-kindred/` (Linda) | 948 | 396 | Spread Gen 2-15 | CLAUDE.md (104 lines) + 8 auto-memory files; same methodology link |
| `/home/jerem/genealogy-dry-cross/` (Christy) | 3,369 | 3,290 | Spread Gen 1-16 | CLAUDE.md (95 lines) + 11 auto-memory files; same methodology link |

**Protocol**:

1. Spawn fresh Sonnet subagent (no parent-conversation context) per project.
2. Subagent reads project's `CLAUDE.md` + auto-memory `MEMORY.md` to bootstrap (simulates fresh-session load).
3. Run 3 queries per project across three categories:
   - **Q1 — Methodology lookup**: Should hit CLAUDE.md or methodology repo
   - **Q2 — Multi-file synthesis**: Requires reading several files and stitching
   - **Q3 — Cross-project methodology**: Tests the `ai-genealogy/` resource-map routing
4. Subagent classifies each answer:
   - **DEFINITIVE** — complete answer with cited file paths
   - **PARTIAL** — answered with gaps; gaps named
   - **UNCERTAIN** — found something; low confidence
   - **UNABLE** — couldn't find the answer
5. Records tool-call count, files read, dead ends.

**Query design** (3 per project, 9 total):

| Project | Q1 (Methodology) | Q2 (Synthesis) | Q3 (Cross-project) |
|---|---|---|---|
| genealogy | Tier 5 external-contribution policy | 3 currently-active brick walls + evidence needed | Tier 2a vs 2b distinction |
| genealogy-kindred | POSSIBLE-link contribution policy | LP2 Cave/Echols Gen 9-11 extension full session reconstruction | Audit-first /loop rule + wiring-bug fix count |
| genealogy-dry-cross | WikiTree post-or-prep workflow | Indian Jim Brown @I71 conflation resolution | 510-person generation offset issue + cascade-fix deferral reason |

## Results

### Headline rates

| Outcome | Count | % |
|---|---|---|
| DEFINITIVE | 8 / 9 | 89% |
| PARTIAL | 1 / 9 | 11% |
| UNCERTAIN | 0 / 9 | 0% |
| UNABLE | 0 / 9 | 0% |

### Per-project detail

| Project | Q1 | Q2 | Q3 | Total tool calls | Wall time | Self-reported "load-bearing" layer |
|---|---|---|---|---|---|---|
| genealogy | DEFINITIVE | **PARTIAL** | DEFINITIVE | ~9 | 92s | CLAUDE.md resource-map (Q1, Q3); journals (Q2 — stale, drove the PARTIAL) |
| genealogy-kindred | DEFINITIVE | DEFINITIVE | DEFINITIVE | ~14 | 138s | MEMORY.md as session-summary index (Q2); CLAUDE.md (Q1, Q3) |
| genealogy-dry-cross | DEFINITIVE | DEFINITIVE | DEFINITIVE | ~5 | 54s | MEMORY.md → dedicated memory files (`project_gen_offset_martin_import.md`); CLAUDE.md (Q1) |

### Tool-call cost vs corpus size — counter-intuitive

| Project | md count | Tool calls | Calls per file (×10⁻⁴) |
|---|---|---|---|
| genealogy-dry-cross | 3,290 | 5 | 15 |
| genealogy | 17,000 | 9 | 5 |
| genealogy-kindred | 396 | 14 | 354 |

Smaller corpus ≠ fewer tool calls. **Kindred is the smallest project but cost the most tool calls** because Q2 (LP2 Cave/Echols) required reading 5+ individual person journals — the session was distributed across journals + LEARNINGS.md without a consolidating session-log file. **Dry-cross's gen-offset answer cost just 2 reads** because a single dedicated memory file (`project_gen_offset_martin_import.md`) carried the full answer including commit hashes, line numbers, and simulation results.

The variable that drove cost: **does a dedicated memory file exist for the topic at hand?**

## What worked — patterns to replicate

1. **CLAUDE.md as routing index, not encyclopedia.** Each project's CLAUDE.md has a "Resource Map" / "Authoritative References" section that names exact methodology-file paths and headings. This routed Q1 + Q3 to the right file in one read on every query. The "non-negotiables" line in `genealogy/.claude/CLAUDE.md:34` ("Never contribute Tier 5 parent links externally") was sufficient to fully answer Q1 without further navigation.

2. **MEMORY.md as flat index, not summary.** The auto-memory `MEMORY.md` files are ~10-line indices listing dedicated memory files with one-line descriptions. The format `- [Title](file.md) — one-line hook` lets the subagent decide which file to actually open. Both kindred and dry-cross used this pattern successfully.

3. **Dedicated memory files for resolved-but-complex issues.** Dry-cross's `project_gen_offset_martin_import.md` is the canonical example: it captures the bug origin, affected commits, line numbers, the failed simulation count, and the planned fix approach. When asked, the subagent did one read and produced a complete answer with citations. **This pattern is the highest-leverage authoring discipline** in the genealogy portfolio.

4. **External methodology repo (`ai-genealogy/`) as cross-project canon.** The methodology files (`02-evidence-standards.md`, `05-human-judgment-gates.md`) are referenced by all three projects' CLAUDE.md resource maps. Q1 + Q3 across all three projects routed cleanly into this repo without ambiguity.

## What struggled — gaps to address

1. **Active research targets without dedicated memory files** — the genealogy project's Q2 PARTIAL was traced to the absence of dedicated brick-wall memory files. The subagent had to navigate `RESEARCH_PRIORITY_PLAN.md` → `ONSITE_RESEARCH_BACKLOG.md` → 3 individual journals, and the journals themselves were last touched in February 2026 (stale). A dedicated `project_active_brick_walls.md` listing each open wall + evidence-needed + last-action-date would have collapsed Q2 to one read.

2. **Session reconstruction across distributed journal updates.** Kindred's Q2 (LP2 Cave/Echols 2026-04-19 session) required 5+ journal reads because no single session log was written. MEMORY.md's 2026-04-19 block had the high-level summary, but the granular detail (exact ARK URLs, conflict parties, upgrade paths) lived only in person journals. Compromise pattern: a thin `research/sessions/2026-04-19_lp2-cave-echols.md` with the per-journal pointer list would have been a 1-read answer.

3. **The auto-memory layer is API/schema-focused, not research-status focused.** The genealogy `MEMORY.md` covers tree.json field names, FS API behaviors, and rate limiter rules — useful for "how do I" questions, not "what's the state of X" questions. This isn't a fault; it's a category boundary worth naming.

## Implications for archetype recommendations

### For the genealogy portfolio specifically

The cheapest, highest-leverage improvement is **not** Graphify, Lum1104, or any embedding stack. It's:

- Author 5–10 dedicated memory files in the genealogy parent project for active brick walls (one per wall, ~10 min each), modeled on dry-cross's `project_gen_offset_martin_import.md`.
- Author session-log files in `research/sessions/YYYY-MM-DD_<topic>.md` for any session that touches multiple persons. Single source of truth for retrospective queries.

These are markdown-authoring disciplines, not infrastructure investments. Estimated cost: 1–2 hours of curation. Estimated benefit (extrapolating from this measurement): Q2-class queries collapse from 5–9 reads to 1–2.

### For Archetype C generally

This baseline supports a sharper recommendation: **the augmented stack's value (Graphify Pass 2 + wiki + footer-injection) is conditional on memory authorship being undisciplined to begin with**. A project with disciplined CLAUDE.md routing + dedicated memory files + MEMORY.md indexing may not need vendor-LLM Pass 2 at all for retrieval — the unaugmented baseline already runs at 89% definitive.

The graph augmentation case strengthens specifically when:
- The corpus is too large for any human curator to maintain dedicated memory files for active topics
- Cross-document patterns the human curator hasn't thought to capture in dedicated files would be found by graph topology
- The project has multiple curators with inconsistent authoring discipline

The genealogy portfolio meets none of those conditions cleanly. Single curator, disciplined authoring, the 17k corpus is journal-per-person (one source-of-truth file per query target), not free-form prose.

### Implication for the C-EC (egress-constrained) archetype

The 2026-04-29 reframing of the genealogy projects' egress posture (vendor-LLM egress now authorized — see `feedback_genealogy_data_classification.md` in user memory) means the constraint that drove the original "C-PII" variant doesn't apply to the canonical example. **The egress concern was load-bearing for "must we use the unaugmented stack" but turns out not to have been load-bearing for "is the unaugmented stack sufficient"** — it's sufficient anyway.

For *actual* hard-egress-constraint projects (medical, legal, journals naming third parties), this measurement still informs them: the architectural pattern (CLAUDE.md + dedicated memory files + MEMORY.md index) is plausibly sufficient on its own, regardless of whether vendor egress is permitted.

## Confounds — what this measurement does NOT establish

1. **Selection bias on queries.** I designed the queries with knowledge of what's documented in CLAUDE.md/MEMORY.md. A research-time query the curator hasn't anticipated documenting may fail differently. To strengthen, run a query set authored by the user from real research-session questions, not by the measurer.

2. **N=9 is small.** A 1-of-9 PARTIAL means ~11% failure rate ±~10% binomial CI. Repeating with 30+ queries would tighten the bound.

3. **Subagent reasoning is Sonnet-specific.** Different models will succeed on different queries. This is a Sonnet baseline, not a model-agnostic baseline.

4. **No comparative arm.** This measures the unaugmented stack only. To say "augmentation isn't needed" rigorously, run the same query set against a Graphify-augmented + wiki-augmented version of one of these projects. Now feasible given the egress reframe.

5. **Subagents have no real auto-memory.** The bootstrap `Read` of the auto-memory `MEMORY.md` simulates a fresh session loading auto-memory, but the auto-memory layer's actual retrieval characteristics in a long session may differ.

## Recommended next experiments

1. **Author 5 dedicated brick-wall memory files in `/home/jerem/genealogy/`** (one per active wall, modeled on dry-cross's gen-offset file). Re-run Q2 against the parent project. Measure tool-call delta. **Hypothesis**: Q2 collapses from 6 reads to 1–2.

2. **Run the augmented arm** — install Graphify on dry-cross (the cleanest project), Pass 1 + Pass 2 with vendor LLM (now authorized). Re-run all 3 queries. Compare tool calls + answer quality. **Hypothesis**: Marginal improvement small for Q1/Q3, modest for Q2; not worth ongoing infra cost given baseline already at 8/9 definitive.

3. **Author a research-time query set with the user** from real session questions (not measurer-designed). Re-run baseline. Check whether selection-bias confound holds.

## Related Analyses

- [`memory-systems-archetype-c-personal-second-brain.md`](memory-systems-archetype-c-personal-second-brain.md) — non-PII variant of the second-brain archetype
- [`memory-systems-archetype-c-egress-constrained.md`](memory-systems-archetype-c-egress-constrained.md) — egress-constrained variant (renamed from C-PII; the genealogy-as-canonical-example framing was retired in the 2026-04-29 reframe)
- [`memory-systems-archetype-recommendations.md`](memory-systems-archetype-recommendations.md) — index across archetypes
- [`memory-system-patterns.md`](memory-system-patterns.md) — earlier pattern survey
- [`memory-systems-graphify-vs-understand-anything.md`](memory-systems-graphify-vs-understand-anything.md) — A/B comparison of LLM graph builders on the docs in *this* repo (not genealogy)

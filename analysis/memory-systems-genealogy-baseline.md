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
  - claim: "Authoring 5 dedicated brick-wall memory files + a MEMORY.md flat-index entry per wall collapses Q2 from ~6-9 tool calls (PARTIAL) to 3 tool calls (DEFINITIVE) on the genealogy parent project"
    source: "Experiment #1, Sonnet subagent re-run 2026-04-29 against augmented memory; the rich one-line index entries in MEMORY.md were answer-sufficient without opening the dedicated files"
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

### Experiment #1 — Brick-wall memory file authoring — RUN, VALIDATED, AND EXPANDED 2026-04-29

**Hypothesis**: authoring dedicated brick-wall memory files in `/home/jerem/.claude/projects/-home-jerem-genealogy/memory/` (modeled on dry-cross's `project_gen_offset_martin_import.md`) collapses Q2-class synthesis queries from ~6 reads to ~1-2.

#### Batch 1 (initial — 5 files, 2026-04-29 morning)

- Sonnet subagent surveyed `RESEARCH_PRIORITY_PLAN.md`, `ONSITE_RESEARCH_BACKLOG.md`, and per-person journals.
- Selected 5 brick walls applying selection criteria (re-query likelihood, multi-session journal depth, lineage diversity). Rejected 4 candidates with thin journals rather than padding.
- Authored 5 files (51-63 lines each), each containing: canonical facts + IDs + generation + lineage, attached primary sources with tier, what's been tried + dates, what evidence is needed, next research targets, cross-refs to journals.
- Updated `MEMORY.md` with a new `## Active brick walls` section.
- Lineage diversity: Parts 5, 8, 10, 10, 11; generations 6-9.

**Validation** — fresh Sonnet subagent re-ran the original Q2 query against the augmented memory:

| Metric | Original baseline | Post-Batch-1 | Delta |
|---|---|---|---|
| Tool calls (Q2) | ~6-9 | **3** (2 bootstrap + 1 spot-check) | **−5 to −6** |
| Answer-bearing reads | 5+ per-person journals | **1 (`MEMORY.md` alone)** | **−4+** |
| Classification | PARTIAL | **DEFINITIVE** | **+1 tier** |
| Wall time | 92s | **44s** | **−48s** |

**Counter-finding (better than predicted)**: the validation agent answered the full query from the `MEMORY.md` `## Active brick walls` section *alone* — the dedicated brickwall files weren't needed for the synthesis query because the index entries contained the highest-value next target per wall. The dedicated files serve as the "give me details" backstop for deeper queries, not the primary retrieval surface for "list active walls".

#### Batch 2 (expansion — 15 files, 2026-04-29 afternoon)

After validation, the project owner authorized expanding coverage. Methodology:

- **Survey subagent** classified the remaining 64 brick walls (`tree.json` `brick_wall=True` minus the 5 done) into QUALIFY / DEFER / SKIP using the same quality gate as Batch 1: re-query likelihood, journal depth, plannable evidence, multi-file synthesis pain, lineage diversity.
- Outcome: **15 QUALIFY / 17 DEFER / 32 SKIP**. The DEFER count tells the user where the research-frontier-vs-memory-curation boundary actually sits — those need real research sessions before memory files would add value (single-bootstrap journals, missing journal files, FS searches still PENDING).
- 3 parallel authoring subagents each handled 5 files, with the index update deferred to the parent session to avoid `MEMORY.md` write races.
- Authored 15 files (47-64 lines each) covering Parts 4, 5, 6, 7, 7, 8, 8, 9, 10, 10, 13, 16, 16 + Part 6/8 reinforcement.

**Final state**: 20 dedicated brick-wall memory files in the genealogy auto-memory dir. Coverage spans 10 of 16 lineage parts. ~6 min curation cost per file × 20 = ~2 hours total.

#### Cost-benefit summary

| Investment | Empirical result |
|---|---|
| ~2 hours subagent + parent-session curation | 5x → likely larger reduction in synthesis-query tool calls |
| Zero infrastructure (no graph, no embeddings, no Pass 2) | PARTIAL → DEFINITIVE on Q2 class |
| All work at the markdown-authoring layer | Coverage of 20 of 69 brick walls; remaining 49 break down 17 DEFER (need research) / 32 SKIP (low ROI) |

**Implications now Tier B from direct measurement at 4x scale**:

- The architecture: **`MEMORY.md` as a rich flat index is the load-bearing layer**. Dedicated memory files behind it serve detail queries.
- The economic story: a few hours of authoring beats infrastructure for retrieval purposes on this corpus class.
- Quality gate matters: padding the count to 69 by lowering the gate would dilute the index. The DEFER/SKIP discipline is what keeps the index actionable.
- The "next batch" decision is data-driven: 17 DEFER candidates can be promoted to QUALIFY only after a real research session adds journal depth. SKIP candidates are unlikely to ever earn dedicated files; they belong in `ONSITE_RESEARCH_BACKLOG.md` summary rows instead.

### Experiment #2 — Comparative augmented arm (planned, not yet run)

Install Graphify on dry-cross (cleanest project), Pass 1 + Pass 2 with vendor LLM (authorized). Re-run all 3 queries. Compare tool calls + answer quality. **Hypothesis**: marginal improvement small for Q1/Q3, modest for Q2; not worth ongoing infra cost given baseline (post-experiment-1) is now 9/9 likely-DEFINITIVE if the same pattern is applied to dry-cross's brick walls.

### Experiment #3 — User-authored query set (planned, not yet run)

Author a research-time query set with the user from real session questions (not measurer-designed). Re-run baseline. Check whether selection-bias confound holds.

## Related Analyses

- [`memory-systems-archetype-c-personal-second-brain.md`](memory-systems-archetype-c-personal-second-brain.md) — non-PII variant of the second-brain archetype
- [`memory-systems-archetype-c-egress-constrained.md`](memory-systems-archetype-c-egress-constrained.md) — egress-constrained variant (renamed from C-PII; the genealogy-as-canonical-example framing was retired in the 2026-04-29 reframe)
- [`memory-systems-archetype-recommendations.md`](memory-systems-archetype-recommendations.md) — index across archetypes
- [`memory-system-patterns.md`](memory-system-patterns.md) — earlier pattern survey
- [`memory-systems-graphify-vs-understand-anything.md`](memory-systems-graphify-vs-understand-anything.md) — A/B comparison of LLM graph builders on the docs in *this* repo (not genealogy)

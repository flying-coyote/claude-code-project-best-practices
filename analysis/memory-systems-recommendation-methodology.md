---
status: EMERGING
last-verified: "2026-04-28"
measurement-claims:
  - claim: "Karpathy's LLM Wiki paradigm rates Tier B by author authority, not Tier C, despite April 2026 publication date"
    source: "Author authority on par with Boris Cherny on Claude Code; user-stated criterion 2026-04-28"
    date: "2026-04-28"
    revalidate: "2026-10-28"
  - claim: "Wiki+graph+contradiction-lint discipline starts paying back at ~500 docs for single-curator hand-curated KBs (rough working-memory math, not measured)"
    source: "Working-memory ~50-100 docs × cross-ref density K=3-5 → ~1,500-2,500 relations beyond mental tracking at 500 docs"
    date: "2026-04-28"
    revalidate: "2026-10-28"
  - claim: "Graphify Pass 2 LLM work happens via the invoking Claude Code session, not via direct LLM SDK calls — confirmed by zero LLM SDK deps in pyproject.toml"
    source: "Direct read of safishamsi/graphify pyproject.toml v1 branch"
    date: "2026-04-28"
    revalidate: "2026-07-28"
evidence-tier: C
applies-to-signals: [memory-systems, methodology, evidence-tiering]
revalidate-by: 2026-10-28
---

# Memory & Knowledge Recommendations: Methodology and Self-Critique

This is the methodology and self-critique companion to `analysis/memory-systems-archetype-recommendations.md`. It captures *why* the recommendations were calibrated to ~500-document curated KBs, what assumptions in the underlying user constraints are weaker than they look, where the analysis itself is structurally weak, and what corrections were applied during iteration.

> **Companion docs**:
> - `analysis/memory-systems-archetype-recommendations.md` — the per-archetype recommendations themselves
> - `research/memory-systems-tools-inventory.md` — factual catalog of 8 tools with verified licenses
> - `research/memory-systems-architecture-axes.md` — 8 architectural axes
> - `research/memory-systems-project-archetypes.md` — 7 project archetypes A–G

---

## What this analysis is FOR

The recommendations target **~500-document curated knowledge bases** — the scale at which the wiki + graph + contradiction-lint discipline starts paying back for a single curator without active automated ingestion. This is the design target, not the only valid scale.

### Why ~500?

A single curator can hold ~50–100 docs in active mental review. With average cross-reference density K=3–5 per doc, 500 docs implies 1,500–2,500 relations to keep coherent — beyond mental tracking. The lint goes from "nice-to-have" at 28 to "load-bearing" at 500 over roughly an order of magnitude.

| Scale | Lint discipline | Recommendation |
|---|---|---|
| ≤ 50 docs | Excess | Plain markdown + manual cross-refs |
| 50–200 docs | Optional | Wikilinks + Lum1104 plugin (if you want a graph view) |
| 200–500 docs (single curator) | Increasingly load-bearing | Add graphify + footer-injection + contradiction lint |
| ≥ 500 docs (single curator) | Load-bearing | Full design-target stack |
| Multi-author or active automated ingestion | Threshold compresses to ~100–200 | Adopt earlier |

**Caveat on the ~500 number**: this is rough working-memory-vs-relation-count math, not measured studies. Treat with ±50% confidence interval. An earlier draft of this methodology cited "200+ docs"; ~500 is more defensible as the *single-curator* threshold, while 200 is closer for multi-author or active-ingestion projects.

### Far-larger projects

Projects 12×–40× the design target (6k–20k+ markdown vaults with active ingestion and federation) run on heavily customized stacks tailored to their specifics. The archetype recommendations here are useful as upper-bound sanity checks but are not the calibration scale.

---

## Tier discipline

| Source class | Tier | Examples |
|---|---|---|
| Recognized thought leaders, paradigm-level claims | **B** by author authority | Karpathy LLM Wiki paradigm; Boris Cherny on Claude Code |
| Tool-specific quantitative benchmarks (vendor-reported) | **C** until reproduced | Graphify's 71.5× token claim; claude-context's ~40% reduction; OpenBrain's $0.10–0.30/month |
| Roadmap claims (not shipped) | **D** | OpenBrain's compilation agent |
| Verified factual claims (e.g., licenses) | **A** when directly verified | Pratiyush MIT, MehmetGoekce MIT, Lum1104 MIT, Rowboat Apache 2.0 (all dated 2026-04-28) |

**Important**: this corrects an earlier draft that downgraded Karpathy's paradigm to Tier C purely on recency. Recency does not auto-downgrade an author-authority source. The paradigm claim ("write-time wiki + ingest/query/lint workflows + bookkeeping-not-reading insight") is Tier B from publication; only the tool-specific implementations need independent reproduction to move from C to B.

---

## Eight assumptions worth challenging before adopting

These are pushbacks on the user-stated constraints and on my own framing — surfaced upfront so a reader can apply judgment rather than treating the recommendations as decided.

### 1. "Graphify feeds wiki" is a feature you have to build, not one graphify ships

Graphify offers `--wiki` *export* (graph **generates** a wiki) and a hook system that fires on Glob/Grep. Neither of these is "feed findings into your existing markdown." The promotion path is custom glue (the footer-injection script in adoption step A4-3). If you don't write and maintain that script, you'll get the parallel-artifact failure your constraint is supposed to prevent.

**Implication**: scope the footer-injection script as load-bearing infrastructure. If you don't have appetite to maintain it, prefer Lum1104 (which works *over* your existing wiki and wikilinks) over graphify (which assumes you'll write the bridge).

### 2. For prose-heavy corpora, graphify's "deterministic" pitch mostly evaporates

Tree-sitter Pass 1 (the deterministic, EXTRACTED-tag pass) returns ~nothing useful from `.md` files containing argumentation. The provenance discipline collapses to mostly INFERRED for an analytical-prose KB. The contradiction lint then has very little EXTRACTED bedrock to anchor against. **Determinism is for code corpora, not for prose corpora.** The inventory and axes docs don't make this distinction sharply enough.

### 3. The contradiction discipline scales sharply — calibrate to ~500 docs, not your local scale

At 28 docs (this repo's scale), a contradiction-lint is excess. At ~500 docs (the design target), the math flips: 1,500–2,500 relations, beyond mental tracking, silent drift inevitable. Multi-author or active automated ingestion compresses the threshold to ~100–200.

**Implication**: write recommendations for the ~500-doc design target, not for whatever scale you happen to be testing at. The lint is correct at 500 even where it's over-engineered at 28.

### 4. Karpathy's paradigm is Tier B by author authority

(See "Tier discipline" above.) An earlier draft downgraded it to Tier C on recency grounds. That was wrong — Karpathy is a recognized authority and his paradigm carries author-weight. Tool-specific quantitative claims still stay Tier C until independently reproduced; the paradigm itself does not.

### 5. "Local-first" for graphify is a half-truth on prose

Pass 1 (Tree-sitter) is local. Pass 2 (LLM concept extraction) is **not** — content goes to whatever LLM the invoking Claude Code session is using. On a prose KB, Pass 2 is *most of the signal*. So "graphify is local" reads as a privacy claim it doesn't make for prose.

**Sub-finding from a 2026-04-28 source check**: graphify's `pyproject.toml` lists zero LLM SDK dependencies (no `anthropic`, `openai`, `litellm`). The README confirms it's "A Claude Code skill" — meaning LLM passes happen via the Claude Code session, not via graphify-internal API keys. **Pointing graphify at a local model (e.g., Gemma 4) is not a documented configuration**; it would require either skipping Pass 2 entirely (Tree-sitter only) or forking graphify to replace Claude-Code-skill calls with direct local-LLM calls.

### 6. Archetype purity is a useful frame but a misleading recommendation surface

Most real projects mix archetypes (e.g., A+F, C+E, A+D+F). Recommending one primary stack per archetype is useful for *framing*; real adoption needs to layer two archetypes' stacks selectively. Treat the per-archetype primaries in the companion doc as orthogonal building blocks, not committed package deals.

### 7. Lum1104's "wiki-aware" framing requires Karpathy filename conventions, not just `[[wikilinks]]` (added 2026-04-28)

Verified 2026-04-28 against plugin v2.3.2: `/understand-knowledge`'s detector (`parse-knowledge-base.py`) gates on `index.md` (lowercase, at root or under `wiki/`) + ≥3 markdown files. `log.md`, `raw/`, and a root schema (`CLAUDE.md`/`AGENTS.md`) are detected but not required. Repos using `INDEX.md` uppercase, or routing schema to `.claude/CLAUDE.md` (this repo's case), fail detection.

**Implication**: the archetype-A "Lum1104 alone over a hand-curated wiki" recommendation is conditional on Karpathy filename discipline, not just on having wikilinks. Renaming `INDEX.md` → `index.md` is a small change but breaks tooling that hardcodes the uppercase form (`automation/generate_index.py` here). The general `/understand-anything:understand` skill is the fallback for repos that don't match — but that's a different code path with its own assumptions, not a drop-in. Document the layout requirement at recommend-time, not at adoption-time.

### 8. Graphify Pass 1 alone is not a topology layer for prose-heavy KBs (added 2026-04-28)

Empirical run, 2026-04-28, this repo at 38 analysis docs + supporting code, graphify v0.5.4. **Pass 1** (`graphify update .`, Tree-sitter only, zero LLM calls): 243 nodes / 427 edges / 73% EXTRACTED — but **0 of 38 `analysis/*.md` docs received nodes**. Pass 1's extraction model is code-only.

**Pass 2** run later the same day (8 parallel general-purpose subagents over 162 files, ~22 files/chunk): **1187 nodes / 1651 edges / 67 communities / 88% EXTRACTED / 24 hyperedges**. 251 nodes were anchored to `analysis/*.md` docs (≈6.6 concept nodes per analysis doc). Token-reduction benchmark on the resulting graph: **57.5× vs naive full-corpus** (graphify's marketing claim is 71×; this run hit 57.5× on the real corpus). Footer-injection re-run after Pass 2 found cross-file edges for **33 of 38 analysis docs** (file-level aggregation; node-level lookup returned zero — see implication below).

**Implications**:

1. **Pass-2-or-no-graphify is the primary decision**, not a footnote. Without Pass 2, graphify is a code-only AST tool with no awareness of prose; with it, graphify becomes a topology layer that captures explicit cross-references and surfaces non-obvious semantic similarities (e.g., the 24 hyperedges include a {memory-archetype-b, -d, -e, -f} grouping the prose itself never names as a set). Update archetype-A's adoption-order step 1 to make this decision explicit before any tooling install.

2. **Egress framing was correct**. Pass 2 ships document content to whatever LLM the invoking session uses. The earlier reversibility-except-egress framing applies in full and is the gate that determines whether graphify is even a viable topology layer for sensitive prose corpora.

3. **File-level aggregation matters for prose footers**. Each markdown file produces many concept nodes (mean 6.6, max 28 in this run), not one. Footer-injection scripts that look up edges by *file-path-as-node-id* return zero edges; they have to aggregate node-level edges by `source_file` to produce a "Related" footer. The script in `scripts/graphify_footer_inject.py` was updated 2026-04-28 to do this; the original node-keyed lookup was a code-corpus assumption that doesn't survive contact with prose.

4. **Subagent model selection is a real cost lever**. The 8 Pass 2 subagents each consumed 80k–190k tokens on the parent's Opus 4.7. Subagent extraction is mechanical structured output; pass `model: "sonnet"` to graphify-style fan-outs (or run graphify under a Sonnet-default Claude Code session) and the run is 4–8× cheaper with no quality difference observed.

---

## Three places the analysis is structurally weak

- **Reversibility framing on adoption-order step 1s**: deleting a graphify output folder undoes the local index, but Pass 2 has already shipped content to whatever LLM the invoking session uses, and that egress is not reversible. The companion doc now distinguishes "reversible-local" from "reversible-except-egress" but the broader pattern — that any LLM-touching tool's first run is egress-irreversible — applies across many recommendations and is not consistently flagged.

- **The "never combine graphify + Lum1104" rule was overstated initially**. They're architecturally different: Lum1104 uses your `[[wikilinks]]` as ground truth; graphify discovers structure via AST + LLM passes. Running both *can* be coherent if one is explicitly authoritative and the other is read-only. The companion doc's never-combine entry has been softened to reflect this; the absolute version was wrong.

- **Evidence-gap list misses the foundational experiment**. The deepest unknown isn't graphify's 71× token claim — it's whether wiki + graph beats plain markdown + good cross-refs at 30-doc scale, at 500-doc scale, and at 5,000-doc scale. That requires 3+ months of A/B on real query patterns at each scale. Without it, every recommendation is sophisticated guessing about the payoff curve.

---

## Two reframings worth considering

- **Archetype A's right answer splits by scale.** Below ~200 docs: "good wikilinks + Lum1104, defer everything else" — Lum1104 respects existing wikilinks and is strictly downstream; manual cross-referencing is tractable. At ~500 docs: automated graphify becomes necessary, footer-injection glue is worth maintaining, contradiction-lint earns its keep. Don't over-generalize a small-scale recommendation to design-target projects, or vice versa.

- **OpenBrain as the archetype-G primary is contingent on a feature that hasn't shipped.** Recommending OpenBrain *now* treats Tier D speculation as Tier C evidence. The honest archetype-G primary today is "wait for the compilation agent to ship and reproduce its claims, OR roll a minimal Postgres + pgvector + tiny MCP shim yourself." OpenBrain's full stack is recorded in the companion doc as a forward-planning state, not a current adoption.

---

## Applied corrections during iteration

The companion recommendations doc reflects these corrections from earlier drafts:

| Correction | What changed |
|---|---|
| Archetype A primary stack split by scale | Lum1104-only added as the explicit primary at <~200 docs; graphify+footer-injection remains the primary at ~500-doc design target |
| Archetype G flagged as roadmap-contingent | "Wait or roll your own Postgres+pgvector+MCP" is the recommendation today; full OpenBrain stack captured as future state |
| Adoption-order step 1s distinguish reversibility classes | Reversible-local vs reversible-except-egress; LLM Pass 2 = irreversible egress |
| Never-combine graphify+Lum1104 softened | Allowed if one is explicitly authoritative |
| Karpathy paradigm Tier B by author authority | Corrected from prior Tier C downgrade |
| Threshold calibrated to ~500 docs | Earlier "200+" replaced with the more defensible single-curator threshold; 100–200 noted for multi-author or active-ingestion |
| All four "check repo" licenses verified 2026-04-28 | Pratiyush, MehmetGoekce, Lum1104 = MIT; Rowboat = Apache 2.0 (rowboatlabs/rowboat) |
| Rowboat description corrected | README lists Google Gmail/Calendar/Drive + optional Composio MCP (not Granola/Fireflies as the inventory had) |
| InfraNodus added to license/cost table | Acknowledged as paradigm alternative (text network analysis) but doesn't fit local-first + markdown-substrate constraints |

---

## What I shouldn't have shortcut

- "(analyses are public)" was used to justify graphify Pass 2 egress on this repo. Public-on-GitHub bounds external-disclosure harm; it does not address vendor retention, what bulk-indexers actually ship (the whole working tree, not just the public-by-intent subset), or future drift. The honest framing is: "the action is reversible-bounded-not-undoable; even public content's egress is one-way; verify what would ship before running."

- Treating every April-2026 tool as Tier C uniformly. Author authority distinguishes paradigm claims from tool implementations. Karpathy's paradigm carries weight; a specific implementation's benchmark does not, until reproduced.

---

## Related analyses

- `analysis/memory-systems-archetype-recommendations.md` — the recommendations themselves
- `analysis/evidence-tiers.md` — evidence-tier framework used here
- `analysis/evidence-based-revalidation.md` — how to keep recommendations current
- `analysis/confidence-scoring.md` — adjacent practice for tracking claim confidence

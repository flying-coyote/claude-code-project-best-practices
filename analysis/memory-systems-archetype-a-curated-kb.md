---
status: EMERGING
follows: "Karpathy LLM-wiki paradigm (write-time vs read-time wiki; Tier B by author authority, verified 2026-07-16) — the curated-KB paradigm layer this archetype implements. Bar status: fails Supported (blog/talk-form canon). Delta kept here: working implementation evidence — the graphify+footer pipeline and the typed-registry remediation. Advance trigger: the paradigm productized by a Supported tool covering the curated-KB archetype."
last-verified: "2026-08-13"
evidence-tier: C
convergence: emerging  # AI-PKM caveat (B-F1 seed): emerging WITH license risk — Obsidian Smart Connections ~786K downloads but Jan-2026 proprietary switch (DR-6 verified)
applies-to-signals: [memory-systems, knowledge-base, wiki, graph, md-corpus-small, md-corpus-design-target, md-corpus-large, vault-karpathy, project-type-docs, typed-memory-no-registry]
revalidate-by: 2026-10-28
---

# Archetype A — Curated Analytical Knowledge Base

**Evidence Tier**: C — recommendation synthesizes Tier-B paradigm (Karpathy LLM Wiki) with Tier-C tool-specific claims (graphify, Understand-Anything).

> **Following the Karpathy LLM-wiki paradigm since 2026-07-16.** New coverage effort on the paradigm layer goes to tracking the canon, not growing this doc. Delta kept: the implementation evidence (graphify+footer, typed-registry remediation).
>
> **Citation note.** Paths under `project1/` name files on the author's machine, not in this repository. They are recorded as **provenance for a single-practitioner production deployment** — enough to identify what was inspected and when — and are deliberately not hyperlinks, because no reader of this repository can follow them. Treat every `project1/` claim at the Tier-B bar this repo gives uncorroborated single-project evidence.

## Canon liveness check — 2026-08-13: STABLE

The followed canon is unchanged. The [Karpathy LLM-wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) (created 2026-04-04) shows **exactly one revision** — no updates through 2026-08-13 (fetch-verified 2026-08-13). The write-time-vs-read-time wiki paradigm this archetype implements therefore stands as originally published; no advance-trigger movement, and nothing in the canon layer requires a change to A1–A5 below.

Karpathy's in-window public activity has moved to **model-capability commentary rather than knowledge-architecture**: a Fable 5 launch reaction (~2026-06-09, X post — search-snippet only, X unfetchable: "this is a major-version-bump-deserving step change forward… peaking especially for long problem-solving sessions on very difficult problems"), and a ~2026-07-05 warning about "focusing on agents before models" (snippet-only). **Tier C for both** — search snippets, primary source unfetchable. Neither revises the wiki paradigm, and neither is load-bearing for any recommendation here; they are recorded only to show the canon author was active and did *not* update the pattern.

Next liveness check rides with this doc's `revalidate-by` (2026-10-28).

## Purpose

Per-archetype recommendation for **curated, hand-edited analytical knowledge bases**: domain-expertise wikis, evidence-tiered frameworks, research-synthesis vaults where each doc is hand-written and cited.

Calibrated to the **~500-document single-curator design target**. See [`memory-systems-recommendation-methodology.md`](memory-systems-recommendation-methodology.md) for threshold math.

## A1. Primary stack — splits by scale

- **At the ~500-doc design target**: **Graphify (write-time topology) → footer-injected into a Karpathy-pattern wiki convention.**
- **Below ~200 docs**: **Understand-Anything alone over a hand-curated wiki with `[[wikilinks]]`.** Understand-Anything uses existing wikilinks as ground truth (deterministic on *your* structure) and is strictly downstream — no glue work to maintain, no Pass-2 egress on prose. Promote to graphify+footer when growing past ~200.
  - **Layout requirement** (verified 2026-04-28 against plugin v2.3.2 `parse-knowledge-base.py`): `/understand-knowledge` gates on `index.md` (lowercase, at root or under `wiki/`) **+ ≥3 markdown files**. `log.md`, `raw/`, and a root schema (`CLAUDE.md`/`AGENTS.md`) are detected but optional. Repos using `INDEX.md` uppercase, or with the schema under `.claude/CLAUDE.md`, fail detection — rename or use Understand-Anything's general `/understand-anything:understand` skill instead, which doesn't gate on Karpathy layout.

| Layer       | Owner (design-target stack)                                                                                            | Why                                                                                                                              |
|-------------|------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Substrate   | Markdown files in `analysis/`                                                                                          | Axis 7 — long-lived, grep-able, git-backed                                                                                       |
| Topology    | Graphify (`graphify-out/graph.json`)                                                                                   | Axis 8 — Tree-sitter + Leiden are deterministic; provenance tags auditable. **Empirical caveat (2026-04-28, this repo, graphify v0.5.4)**: Pass 1 alone (`graphify update .`) indexed 0 of 38 `analysis/*.md` docs — Tree-sitter only extracts code constructs. For prose-heavy KBs the topology layer's value is gated on Pass 2 (LLM extraction), which ships content to whatever LLM the invoking session uses |
| Synthesis   | Hand-edited prose, augmented by graph footer                                                                            | Axis 2 — augments-wiki; prose carries argumentation graph can't represent                                                        |
| Lint        | Local script reading `graph.json` + each `analysis/*.md`, flagging wiki claims that conflict with EXTRACTED edges       | Axis 8 — bridges deterministic vs LLM-derived                                                                                    |

**Driving axes**: 1 (write-time dominant), 2 (augments-wiki), 7 (markdown), 8 (provenance discipline). **Evidence tier**: B for the Karpathy paradigm; **C — vendor-reported, not independently benchmarked** — for graphify's specific 71.5× token claim ([Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)).

## A1b. Typed-frontmatter hygiene — OKF as the KM-leverage pattern

This is the highest-leverage hygiene layer in the whole archetype, so treat it as a named pattern, not a footnote. A curated KB whose notes carry a `type:` in frontmatter is no longer just grep-able prose — it is a *typed knowledge graph* an agent, a generated index, or an MCP can query by kind ("every `Assumption` due for review," "every `MDR` still `Proposed`"). That queryability is the leverage. It only holds, though, while the type vocabulary stays small and canonical. Left ungoverned it drifts: one production second-brain reached **127 distinct `type:` values, 86 of them used exactly once**, which made type-based retrieval (a Tolaria MCP, generated indexes, queries) close to useless until the vocabulary was consolidated back to ~30 canonical types. The transferable discipline has four parts:

1. **Every note carries a `type:`** in YAML frontmatter — the one field [Google's Open Knowledge Format (OKF) v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) also makes its *sole* requirement. The spec's own words: "OKF requires exactly one thing of every concept: a `type` field. Everything else … is left to the producer."
2. **A single canonical type-registry doc is the source of truth** — ~30 canonical types plus a few intentional singletons, with a merge-map that keeps retired type names greppable in git history.
3. **A pre-commit guard that *parses* the registry** (does not hard-code the list) and flags any commit whose `type:` is non-canonical — so the guard can never disagree with the human-readable registry.
4. **A coverage/drift health check** — an untyped-node gap report (nav/status/front-door files excluded by a stem regex) plus a distinct-type count that catches fragmentation before it makes retrieval useless.

Federation: have the registry loader take multiple repo roots, so the same coverage/drift checks run across a hub plus its spokes (see [archetype-D](memory-systems-archetype-recommendations.md#archetype-d-cross-project-portfolio)).

### OKF stores what we know; RETHINK re-asks whether it is still right

The four-part hygiene above keeps the typed store *clean*, but a clean store still only answers *what do we know*. It says nothing about whether what we know is still true — a hand-cited analytical note ages, an assumption's review comes due, a contradiction stays unresolved. So the typed substrate pairs with the **RETHINK** limb of the loop (the intent-alignment "why" pass — see [harness-engineering.md](harness-engineering.md)): OKF stores what we know; RETHINK re-asks, on a cadence, whether it is still the right thing to know. The types are what make that re-asking cheap — the loop filters to the kinds most likely to have gone stale rather than re-reading the corpus. In the worked deployment this is a real script (`okf_signals.py`, below) that derives next-work *from the types themselves*, so the graph is the backlog and there is nothing separate to keep in sync.

### The worked deployment (the §A1b source, with real files)

The single production second-brain this pattern is drawn from is project1, a ~500-doc cross-repo security-research vault. The four parts above map to real files — cite these, not a paraphrase:

| Part | File |
|---|---|
| Registry (source of truth) + merge map | `01-knowledge-base/_type-registry.md` — 30 canonical + 9 singletons; records the 127→~30 (2026-06-09) and 51→canonical (2026-06-18) consolidations |
| Per-type field conventions | `AGENTS.md` — the Tolaria-loaded conventions file (registry owns the *list*; AGENTS.md owns the *fields per type*) |
| Parsed-registry helpers (single source of truth, federation-ready) | `automation/lib/okf.py` — `load_canonical_types()` parses the registry region; `load_notes()` takes a list of roots |
| Pre-commit drift guard | `automation/orchestrator/quality_gates.py` `validate_okf_type` — **warns, does not hard-block** (a loud per-commit warning is what keeps the set from re-drifting; the registry rule is "register the new type first") |
| Coverage / drift / gap health check | `automation/okf_health.py` — signal not gate; `--federated` adds spokes (reading ~0% today by design), `--brief` feeds the daily brief |
| Next-work from the graph (RETHINK) | `automation/okf_signals.py` — overdue assumptions, undecided MDRs, unresolved contradictions, weak hypotheses, thin components |

One honest note on the guard: the live deployment makes the canonical-type check a **warning, not a blocking gate**, which is softer than this section's part 3 ("flags any commit") implies and deliberately so — the hard blocks in that pre-commit hook are reserved for invariants (matrix-decision validity, retired-claim drift), while type-drift is a loud warning so the registry-first rule stays a discipline rather than a wall. Adopt blocking or warning per how much you trust contributors to register types first.

**Anti-pattern**: hard-coding the type list inside the guard (it drifts from the human registry the moment someone edits one and not the other); or adding a `type:` field with no registry and no guard at all (you get the 127-types / 86-singletons sprawl, and typed retrieval degrades to plain grep). This second anti-pattern is exactly the `typed-memory-no-registry` signal that routes a project to adopt OKF.

**Scale**: like the lint in A1, this earns its keep at the ~500-doc / multi-spoke design target. Below ~100 docs a fixed handful of types needs neither a registry nor a guard.

**Evidence tier**: B for the pattern — a single production deployment (project1, running the parsed-registry pre-commit guard, with the measured 127→~30 then 51→canonical consolidations and the graph-derived next-work signal). **Flagged: significant value seen recently, but one practitioner, one project, not independently corroborated.** The external OKF spec it conforms to (Google Cloud, Apache-2.0, [announced 2026-06-12](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing), v0.1 "Draft") is a Tier-C vendor-published standard — date, license, and the single-required-`type`-field claim verified against the primary spec + blog on 2026-06-21. Cite the *pattern* from production, the *spec* as the conformance target.

## A2. Hybrid alternatives

| Hybrid                        | Optimizes                                                       | Pick when                                                                |
|-------------------------------|------------------------------------------------------------------|--------------------------------------------------------------------------|
| + MehmetGoekce L1/L2 split    | Context budget at scale                                          | KB exceeds ~100 docs and CLAUDE.md routinely loses important rules       |
| + Understand-Anything plugin              | Wiki-aware graph (uses your wikilinks as ground truth)           | Rich `[[wikilinks]]` already exist and you want a graph that respects them |
| + Pratiyush adapters          | Mining historical Claude Code sessions back into the analytical layer | Session archive (archetype F) is worth promoting findings into A         |

## A3. Anti-patterns

- **Claude-context (Milvus + embeddings) against a 30-doc analytical KB**: pays vector-DB ops cost and embedding-provider egress for recall benefit Grep already provides; embedding drift later forces reindex. **Empirical support (Tier B, 2026-05-14)**: Sen et al., ["Is Grep All You Need? How Agent Harnesses Reshape Agentic Search"](https://arxiv.org/abs/2605.15184) — 116-question LongMemEval study across Chronos, Claude Code, Codex, Gemini CLI found grep generally yields higher accuracy than vector retrieval. Further support (Tier B, 2026-05-12): Wu et al., ["LongMemEval-V2"](https://arxiv.org/abs/2605.12493) — "AgentRunbook-C" (store trajectories as files; coding agent greps/reads at query time) reaches 72.5% on environment-specific tasks, beating retrieval-augmented baselines. Caveat from Sen et al.: "overall scores still depend strongly on which harness and tool-calling style is used" — the win is harness-conditional, not absolute.
- **Scope boundary — counter-signal at long-horizon scale (Tier B, 2026-04-23)**: Abtahi et al., ["Memanto: Typed Semantic Memory with Information-Theoretic Retrieval"](https://arxiv.org/abs/2604.22085) reaches SOTA 89.8% / 87.1% on long-horizon agent benchmarks with **vector-only retrieval** (no graph, no LLM-mediated ingestion). The "grep beats embeddings" claim above is scoped to small-KB / short-task regimes (which is the Archetype A design target). At long-horizon agent-memory scale — i.e., Archetype F territory, not Archetype A — well-designed vector retrieval can dominate. Do not extrapolate this archetype's anti-pattern to that scope.
- **OpenBrain Postgres substrate for ~30 markdown analyses**: flattens per-doc evidence-tier metadata; loses git diff as the audit log; converts a portable artifact into a DB dump.
- **`graphify --wiki` direct export *alongside* a hand-curated `analysis/`**: produces two parallel "wikis" with no defined source-of-truth — violates the graphify-feeds-wiki constraint.

## A4. Adoption order

**Adoption gate**: this archetype's function (AI-PKM) carries `convergence: emerging` in the frontmatter, and the binding rule is that infrastructure adoption requires converged status or an explicit owner exception, so treat the steps below as an evaluation path rather than a sanctioned default.

1. `pipx install graphifyy` (PyPI name; CLI is `graphify`). **Decide first: Pass 2 yes or no.** `graphify update .` runs Tree-sitter Pass 1 only — zero LLM calls, zero egress — but for prose-heavy KBs Pass 1 indexes ~nothing (verified 2026-04-28 on this repo: 0 of 38 `analysis/*.md` got nodes; only code files were extracted). Pass 2 (LLM extraction over prose) is what makes graphify a topology layer for an analytical KB, and **Pass 2 egress is not reversible** — decide before you run it, not after.

   > **Corrected 2026-08-28 — where Pass 2 sends content depends on how you invoke it.** This step used to say flatly that Pass 2 "ships content to whatever LLM the invoking Claude Code session uses" and that the only options for sensitive content were to skip it or run a public-only subset. Both halves need qualifying. Session routing is a property of the **`/graphify` skill path**; headless `graphify extract` has its own provider chain and egresses directly. And current graphify documents `--backend ollama` (plus `OPENAI_BASE_URL` for llama.cpp / vLLM / LM Studio), so a **local Pass 2** is now a documented configuration — sensitive content is no longer a categorical disqualification.
   >
   > The catch is that local is **opt-in and last in line**: the auto-detection chain runs Gemini → Kimi → Claude → OpenAI → DeepSeek → Azure → Bedrock → **Ollama**, so any provider credential in the environment wins silently, and an empty key list is not sufficient either (`--backend claude-cli` rides the Claude subscription; Bedrock uses the ambient AWS IAM chain). Pin the backend explicitly and audit the environment. Untested here — quality against a local model is unmeasured.

   If you skip Pass 2 entirely, the realistic stack collapses to "wikilinks + Understand-Anything + grep" and graphify isn't earning its keep. **Stop if** `GRAPH_REPORT.md` after Pass 2 surfaces no relationships you didn't already know.
2. Inspect `graph.html` and EXTRACTED/INFERRED/AMBIGUOUS counts. Read-only.
3. Write a 30–50 line footer-injection script (per `analysis/*.md`, append "Related (from graph)" with INFERRED edges marked). Commit on a branch. **Stop if** edges look noisy and require manual filtering — that's a signal to evaluate Understand-Anything instead.
4. Add `graphify hook install` (git hooks: rebuild on commit/branch).
5. Only then evaluate L1/L2 split or Understand-Anything.

## A5. Constraint check

| Constraint                  | Met?                                                                                                       |
|-----------------------------|------------------------------------------------------------------------------------------------------------|
| Graphify feeds wiki          | ✅ via footer injection                                                                                    |
| No wiki/graph contradiction  | ✅ lint enforces, provenance tags carry through                                                            |
| A/B/C tiering preserved      | ✅ markdown substrate keeps tier metadata in front-matter                                                  |
| Augments not generates       | ✅ prose stays hand-edited                                                                                 |
| Local-first                  | ⚠️ graphify Pass 2 egresses by default. On the `/graphify` skill path it goes to the Claude Code session's LLM; headless `graphify extract` goes to whichever provider it auto-detects. Bound it with an explicit `--code-only` or `--backend ollama` plus an environment audit — not by assuming no session or no API key means no egress (corrected 2026-08-28). |
| Markdown substrate           | ✅                                                                                                         |

## Sources

Inherits source rubric and tier methodology from [`memory-systems-recommendation-methodology.md`](memory-systems-recommendation-methodology.md).

### Tier B

- Andrej Karpathy: LLM Wiki paradigm — author authority lifts the paradigm claim to B; tool-specific quantitative claims from tools built on this pattern stay Tier C.
- Sen, Kasturi, Lumer, Gulati, Subbiah (PwC US): ["Is Grep All You Need? How Agent Harnesses Reshape Agentic Search"](https://arxiv.org/abs/2605.15184) — arXiv:2605.15184, 2026-05-14. LongMemEval evidence supporting the "Grep > embeddings" anti-pattern claim for analytical-KB-scale corpora. Preprint, not yet peer-reviewed.
- Wu, Ji, Kawatkar, Kwan, Gu, Peng, Chang: ["LongMemEval-V2: Evaluating Long-Term Agent Memory"](https://arxiv.org/abs/2605.12493) — arXiv:2605.12493, 2026-05-12. AgentRunbook-C pattern (file-as-memory + coding agent retrieval) hits 72.5% on environment tasks, beating RAG baselines. Successor to LongMemEval; complementary to Sen et al. above. Preprint, not yet peer-reviewed.
- Abtahi, Rahnema, H. Patel, N. Patel, Fekri, Khani: ["Memanto: Typed Semantic Memory with Information-Theoretic Retrieval"](https://arxiv.org/abs/2604.22085) — arXiv:2604.22085, 2026-04-23. **Counter-signal**, registered as a scope boundary: vector-only retrieval reaches SOTA 89.8% / 87.1% at long-horizon scale. Used in this archetype's anti-pattern section to prevent over-extrapolation of "grep beats embeddings" outside the small-KB / short-task regime. Preprint, not yet peer-reviewed.

### Tier B (added)

- Typed-frontmatter hygiene pattern (§A1b) — single production second-brain (project1), firsthand. Real implementation: `01-knowledge-base/_type-registry.md` (the registry + merge map, 30 canonical types), `automation/lib/okf.py` (parses the registry — single source of truth — and is federation-ready via a roots list), `automation/orchestrator/quality_gates.py:validate_okf_type` (the pre-commit drift guard, warn-not-block), `automation/okf_health.py` (coverage/drift/gap health signal), and `automation/okf_signals.py` (graph-derived next-work — the RETHINK operationalization). Measured 127-distinct-types/86-singletons → ~30 (2026-06-09), then 51 → canonical (2026-06-18). **Expert-practitioner, production-validated on one project, not independently corroborated (Tier B by this repo's definition).**

### Tier C

- [Google Cloud — Open Knowledge Format (OKF) v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) — Apache-2.0; [announced 2026-06-12](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing) (Google Cloud blog). v0.1 marked "Draft." Vendor-neutral markdown-wiki spec for agent context; its sole required frontmatter field is `type:` (recommended-but-optional: `title`, `description`, `resource`, `tags`, `timestamp`; consumers MUST NOT reject a bundle for unknown types or missing optional fields). Version, license, date, and the single-required-field claim verified against the primary spec + blog on 2026-06-21. The §A1b registry+guard is a conformance/hygiene layer on top of that one required field. **Vendor-published open standard — cite the pattern from production, not the spec.**
- [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) *(was `safishamsi/graphify`, which no longer resolves — repo re-homed; verified 2026-08-28)* — graphify v0.5.4, 2026-04-28. 71.5× token-savings claim for topology-first retrieval. **Vendor-reported — not independently benchmarked.**
- [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) *(formerly `Lum1104/Understand-Anything`; transfer verified 2026-08-28)* — wiki-aware graph using `[[wikilinks]]` as ground truth; layout requirements verified 2026-04-28 against plugin **v2.3.2**. Upstream is now v2.9.4 and its default state directory moved to `.ua/`, so re-verify the detector before relying on it. **Community-reported — not independently benchmarked.**
- MehmetGoekce L1/L2 split — context-budget management at scale; named in hybrid alternatives without an independent benchmark. **Community-reported — not independently benchmarked.**
- Pratiyush/llm-wiki adapters — session-to-wiki ingestion for Claude Code, Codex, Cursor, Gemini; cited as hybrid alternative for session-archive promotion. **Community-reported — not independently benchmarked.**

## Related Analysis

- [`memory-systems-archetype-recommendations.md`](memory-systems-archetype-recommendations.md) — index across all 7 archetypes + cross-cutting sections (migration, never-combine, license)
- [`memory-systems-recommendation-methodology.md`](memory-systems-recommendation-methodology.md) — framing and self-critique behind these recommendations
- [`memory-system-patterns.md`](memory-system-patterns.md) — earlier pattern survey

---

*Last updated: 2026-08-13 (canon-liveness check — Karpathy LLM-wiki gist fetch-verified unchanged at one revision since 2026-04-04; canon verdict STABLE; author's in-window commentary noted as model-capability topics, not paradigm revision; `last-verified` → 2026-08-13. The `follows:` frontmatter verified date is deliberately left at 2026-07-16 for the next consolidation pass). Prior: 2026-07-16 (follow-lane wiring — `follows:` frontmatter + body banner for the Karpathy LLM-wiki paradigm canon). Prior: 2026-04-28 (layout-requirement verification against plugin v2.3.2; A1b typed-frontmatter hygiene pattern added).*

<!-- graphify-footer:start -->

## Related (from graph)

- [`analysis/memory-systems-archetype-recommendations.md`](memory-systems-archetype-recommendations.md) [EXTRACTED (1.00) ×2] — references

<!-- graphify-footer:end -->

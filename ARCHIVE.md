# Archive

**Purpose**: Completed work items and historical milestones
**Note**: Active work is tracked in [PLAN.md](PLAN.md)

---

## Completed Milestones

### Reduction 2026-07, Phase 3 — memory-cluster fold, 12 docs → 5 (July 10, 2026)

- Folded the seven index-internal archetype docs (B code-monorepo, C personal-second-brain, C-EC egress-constrained, D cross-project-portfolio, E work-state-tracker, F session-archive, G team-shared-memory) into `analysis/memory-systems-archetype-recommendations.md` as in-document sections; archetype A keeps its own file as the heavily-routed primary. All substantive content survived the fold (stack tables, hybrids, anti-patterns, adoption orders, constraint checks, the C-EC safety content nearly whole); what dropped was per-file boilerplate, duplicated source blocks, and stale graphify footers.
- The owner-authorized-egress deciding rule (the C-EC constraint is policy, not data category; user reframe 2026-04-29) moved into `analysis/memory-systems-recommendation-methodology.md` with its measurement claim and the sensitivity-tag vocabulary.
- Archived `memory-systems-genealogy-baseline.md` → `archive/` as a dated measurement (claims stamped 2026-04-29, revalidate ~2026-07-29); the 8/9-DEFINITIVE finding and its implications survive in the consolidated doc's §C-EC.6.
- Routing rows `vault-obsidian` and `md-corpus-very-large` repointed at the consolidated doc in the same commit; AUDIT-CONTEXT's two-level-routing note and signal-vocabulary invariant rewritten to match. Analysis corpus 39 → 31; fleet-audit raw-URL regression re-run after push.

### Reduction 2026-07, Phase 0 — husk removal (July 10, 2026)

- Deleted untracked residue: `mcp-server/` (73 MB of .venv/pycache left behind after the server's source was archived to `archive/mcp-server-v1/`), `examples/` (archived at `archive/examples-v1/`), `.graphify-venv/`, `graphify-out/`, `.understand-anything/` (graphify measurements are recorded in `analysis/memory-systems-graphify-vs-understand-anything.md`).
- Removed the orphaned tracker pair: `scripts/generate-tools-tracker.py` + `.github/workflows/tools-evolution-tracker.yml` (served only the archived docs-v1 TOOLS-TRACKER); `analysis/evidence-tiers.md` repointed at the live `check-measurement-expiry.py` mechanism.
- Fixed `scripts/check-measurement-expiry.py` default scan dir (`patterns/` → `analysis/`): it had been scanning a nonexistent directory and exiting green having checked nothing; it now finds 44 docs and currently flags 2 expired claims (both in `mcp-patterns.md`, a staged collapse target) + 11 expiring within 30 days.
- Archived `V2-COMPLIANCE-MATRIX.md` → `archive/` with a staleness banner (2026-03-31 snapshot asserting since-archived projects as active; live successor = project1 fleet-audit outputs).
- Full plan: `drafts/REDUCTION-PROPOSAL-2026-07.md` (KEEP 12 / COLLAPSE 18 / DELETE 14; Phases 1–3 execution continues, Phases 4–6 gated on Jeremy's sign-off).

### v2.1 - Production Evidence Integration (April–May 2026)

- **Memory & knowledge stack archetypes** (April 28, 2026): split omnibus recommendations into 7 per-archetype docs (`memory-systems-archetype-{a..g}-*.md`) + methodology + graphify vs. understand-anything A/B testbed. Doc count 28 → 38. Empirical findings on Pass 2 LLM extraction (1187 nodes, 67 communities, ~25% hallucination spot-check on EXTRACTED edges).
- **Egress-constrained archetype reframe + genealogy baseline** (April 29, 2026): renamed Archetype C-PII → C-Egress-Constrained after reframing genealogy projects' egress posture. New empirical doc `memory-systems-genealogy-baseline.md` — 3 subagents × 3 queries × 3 projects, 8/9 DEFINITIVE on the unaugmented stack.
- **Memory testbed experiments** (May 2026): Experiment #1 expanded to 20 brick-wall memory files; dedicated brick-wall files collapsed Q2 from 6–9 reads to 3.
- **Quality refresh + consumer-trust pass** (May 24, 2026): URL canonicalization to `code.claude.com`; +4 verified Tier B sources (Builder.io, Morph, Shipyard, VoltAgent); backfilled `## Sources` footers across 16 analysis docs; inlined vendor-reported caveats on Tier C metrics; cross-linked 7-repo portfolio evidence into framework-selection and orchestration-comparison docs.
- **Cross-brain integration from project1 ingest** (May 24, 2026): Surveyed 6k-doc second brain for cross-pollination; 2 of 9 reviewed items passed evidence-tier + scope filters. Added Vallentin CLI+Skill LinkedIn (Tier B with vendor-incentive caveat) — new "CLI + Skill Pattern" section in `mcp-vs-skills-economics.md` documenting the 4-step OpenAPI → typed SDK → CLI → skill recipe. Added H-HARNESS-01 "Hypothesis Status and Falsifiability" section in `harness-engineering.md` with explicit `>6× from model-only swap would invalidate` criterion and outstanding-provenance log. Added arXiv:2605.15184 "Is Grep All You Need? How Agent Harnesses Reshape Agentic Search" (Sen/Kasturi/Lumer/Gulati/Subbiah, PwC US) as Tier B preprint backing the grep-vs-embeddings anti-pattern in `archetype-a-curated-kb.md`. 6 other candidates deferred with documented reasons.
- **Tier A sweep + academic provenance closure** (May 24, 2026): Closed the biweekly Tier A sweep gap (2026-04-22 → 2026-05-24, ~4 weeks). Registered 9 new sources: 6 academic preprints (Meta-Harness arXiv:2603.28052 closing the Stanford 6× gap; Pan et al./Tsinghua arXiv:2603.25723 correcting "Tingua" misspelling; Agentic Context Engineering arXiv:2510.04618 — first ICLR-class Tier A; SWE-Bench Mobile arXiv:2602.09540 — independent 6× corroboration; Memanto arXiv:2604.22085 — counter-signal at long-horizon scale; LongMemEval-V2 arXiv:2605.12493) + Anthropic Research "Teaching Claude why" (Tier A, alignment training reduces blackmail rate 22% → 3%) + Claude Code doc URLs for agent-view / ultrareview / `/goal` (covering 33 changelog versions v2.1.117 → v2.1.150). All three H-HARNESS-01 outstanding-provenance gaps closed; YAML frontmatter and narrative attributions in `harness-engineering.md` corrected. One unverified Anthropic Engineering Blog post (claude-code-quality-reports) returned 404 on three URL variants — flagged, not registered.

### v2.0 - Adaptive Routing + Opus 4.7 Integration (April 2026)

- **Adaptive routing protocol** (April 22, 2026): `AUDIT-CONTEXT.md` routing map from project signals to applicable analysis docs. Typical audit now fetches 4–8 of 28 docs, not the source index alone. `ONE-LINE-PROMPT.md` rewritten as 4-step flow; every recommendation cites the analysis doc + evidence tier.
- **Opus 4.7 migration evidence** (April 22, 2026): `analysis/model-migration-anti-patterns.md` cross-version anti-pattern matrix (4.5 → 4.6 → 4.7); six Vertrees anti-patterns mapped to Anthropic migration guide; behavioral-insights, harness-engineering, claude-md-progressive-disclosure, agent-evaluation, evidence-based-revalidation updated for 4.7.
- **7-repo portfolio analysis** (April 2026): added `analysis/agent-driven-development.md` with quantified evidence from 7 production repos (infrastructure maturity model, cross-repo coordination, security boundaries, velocity data — Nick Schrock's 1000+ PRs/3 weeks, Tenzir's 3x velocity claim).
- **9 new analysis docs covering identified gaps** (April 2026): local-cloud-llm-orchestration, mcp-client-integration, federated-query-architecture, automated-config-assessment, claude-md-progressive-disclosure, memory-system-patterns, evidence-based-revalidation, security-data-pipeline, cross-project-synchronization.

### v1.3 - Production Patterns Integration (December 13, 2025)
- Added production patterns from second-brain integration
- Completed multi-workflow refactoring documentation
- Added 5 new patterns:
  - planning-first-development.md
  - plugins-and-extensions.md
  - skills-domain-knowledge.md
  - spec-driven-development.md
  - subagent-orchestration.md
- Added hypothesis-validator skill example

### v1.2 - Self-Compliance (December 8, 2025)
- Repository now follows its own documented patterns
- Created meta-project infrastructure (.claude/)
- Added PostToolUse and Stop hooks
- Created INDEX.md automation
- Added security guidelines for skills
- Updated SKILL-TEMPLATE.md with Workflow Routing + Security
- Created ARCHITECTURE.md and PLAN.md
- Added 4 new patterns:
  - progressive-disclosure.md
  - advanced-hooks.md
  - documentation-maintenance.md
  - memory-architecture.md

### v1.1 - Nate B. Jones Patterns (December 7-8, 2025)
- Added Nate B. Jones patterns:
  - context-engineering.md
  - agent-principles.md
  - mcp-patterns.md
- Fixed broken URL in SOURCES.md
- Expanded SOURCES.md with article mapping

### v1.0 - Initial Release (November 2025)
- Initial patterns from Anthropic Engineering Blog
- Core skill structure and examples
- Basic template system
- 4 presets (coding, writing, research, hybrid)

---

## Detailed Activity Log

Granular dated entries for each milestone above. Summary bullets in `## Completed Milestones` are the "what"; this section is the "how / why / what changed in which files."

### May 24, 2026 — Tier A sweep + academic provenance closure

- **Biweekly Tier A sweep**: Closed the gap from 2026-04-22 (last refresh) to 2026-05-24 (~4 weeks). Anthropic changelog covered: 33 versions v2.1.117 → v2.1.150. Biggest architectural additions registered as new Claude Code doc URLs: **Agent view** (`claude agents` TUI, supervisor process, git-worktree session isolation), **Ultrareview** (cloud bug-hunting agent fleet with CI integration), **`/goal` command** (completion-condition loop), **hooks invoking MCP tools directly** via `type: "mcp_tool"`, **`hard_deny` auto-mode rules**, **`continueOnBlock` PostToolUse**. One unverified Anthropic Engineering Blog post (claude-code-quality-reports, 2026-04-23) returned 404 on three URL variants — flagged, not registered. Anthropic Research: **["Teaching Claude why"](https://www.anthropic.com/research/teaching-claude-why)** (2026-05-08) registered as Tier A — principle-teaching reduces agentic-misalignment blackmail rate 22% → 3% at 28× token efficiency vs honeypot data; integrated into [`behavioral-insights.md`](analysis/behavioral-insights.md) with explicit harness-design caveat (training-time effect is the lever; `MUST NOT` rules in CLAUDE.md are backstop, not substitute).
- **Academic sweep closed all three outstanding-provenance gaps in H-HARNESS-01** (previously tracked in [`harness-engineering.md`](analysis/harness-engineering.md) as "needs primary source verification"):
  - **Stanford 6× orchestration figure** = headline quote of the **Meta-Harness paper** (Lee/Nair/Zhang/Lee/Khattab/Finn, Stanford+MIT, [arXiv:2603.28052](https://arxiv.org/abs/2603.28052), 2026-03-30). Both gaps resolve to the same single source.
  - **"Tingua NLH ablation"** was a misspelling of **Tsinghua**. Corrected attribution: Pan, Zou, Guo, Ni, Zheng (Tsinghua University + Harbin Institute of Technology). [arXiv:2603.25723](https://arxiv.org/abs/2603.25723), 2026-03-26. All ablation numbers in the repo match the paper exactly.
  - **Meta-Harness paper** now has formal SOURCES.md entry with arXiv ID; result numbers tightened (76.4% Opus 4.6 / 37.6% Haiku 4.5 on TerminalBench-2, rank 1 among Haiku agents).
- **Independent corroboration of the 6× figure**: Tian et al., **SWE-Bench Mobile** ([arXiv:2602.09540](https://arxiv.org/abs/2602.09540), 2026-02-10) — same Opus 4.5 model scores 12% on Cursor vs 2% on OpenCode (exactly 6×, scaffold-only) across 22 configurations. The headline figure is now replicated, not just cited.
- **First peer-reviewed top-venue addition**: **Agentic Context Engineering** (Zhang/Hu/Upasani et al., [arXiv:2510.04618](https://arxiv.org/abs/2510.04618), ICLR 2026) — validates context-as-multiplier with +10.6% on agent tasks / +8.6% on finance. First ICLR-class paper directly supporting the Document & Clear pattern at venue tier A.
- **Counter-signal registered** to scope the "grep > embeddings" claim: **Memanto** (Abtahi et al., [arXiv:2604.22085](https://arxiv.org/abs/2604.22085), 2026-04-23) — vector-only retrieval reaches SOTA 89.8% / 87.1% at long-horizon scale. Added to [`memory-systems-archetype-a-curated-kb.md`](analysis/memory-systems-archetype-a-curated-kb.md) anti-pattern section as explicit scope boundary (small-KB regime only — do not extrapolate to long-horizon agent memory).
- **Memory-systems supporting evidence extended**: **LongMemEval-V2** (Wu et al., [arXiv:2605.12493](https://arxiv.org/abs/2605.12493), 2026-05-12) registered as successor benchmark — "AgentRunbook-C" file-as-memory pattern reaches 72.5% on environment tasks, beating RAG baselines. Cross-referenced from archetype A.

### May 24, 2026 — Cross-brain integration from project1 ingest

- Surveyed project1 (6k-doc second brain) for cross-pollination candidates; 2 of 9 reviewed items passed the evidence-tier and scope filters.
- **Vallentin CLI+Skill LinkedIn (2026-03-17)** added as Tier B source with vendor-incentive caveat. New "CLI + Skill Pattern" section in [`mcp-vs-skills-economics.md`](analysis/mcp-vs-skills-economics.md) documents the 4-step recipe (`OpenAPI → @hey-api/openapi-ts → commander → skill`), decision flow for when to apply, and which parts of the categorical "MCP is a solution in search of a problem" framing to discount.
- **H-HARNESS-01 cross-brain tracking** added to [`harness-engineering.md`](analysis/harness-engineering.md): new "Hypothesis Status and Falsifiability" section consolidating the existing scattered Stanford/Tingua/Karpathy evidence under a single hypothesis claim with explicit falsifiability criterion (`>6× from model-only swap would invalidate`) and an outstanding-provenance log (Stanford 6× orchestration figure, Meta-Harness paper, Tingua NLH ablation — all still need primary-source verification at the time of writing; subsequently closed by the May 24 academic sweep above). Cross-repo pointer to project1's hypothesis tracker without duplicating its tangential cross-brain evidence (Splunk benchmark, CAII Johari Window).
- **arXiv:2605.15184 "Is Grep All You Need? How Agent Harnesses Reshape Agentic Search"** (Sen/Kasturi/Lumer/Gulati/Subbiah, PwC US, 2026-05-14) added as Tier B preprint. 116-question LongMemEval study across Chronos, Claude Code, Codex, Gemini CLI finds grep generally beats vector retrieval with harness having measurable effect independent of retrieval choice. Cross-referenced in `harness-engineering.md` supporting-evidence table + Sources, and in `memory-systems-archetype-a-curated-kb.md` as empirical backing for the claude-context-against-small-KB anti-pattern. Discovered via Elvis S. LinkedIn pointer; only the paper is registered (the LinkedIn post adds no claim beyond the paper).
- 6 other project1 candidates deferred with documented reasons: H-CONTEXT-ROT-01 (already covered in 5 docs), H-CONTEXT-FILE-SYSTEM-01 (single-source 2/5 confidence), H-BOUNDED-AGENCY-01 (governance scope), H-FASTMCP-01 (MCP-server-developer audience, wrong consumer), Lindenberg LinkedIn (derivative pointer with provenance issues), Hoyt Emerson LinkedIn (single-practitioner observation pending corroboration). Elvis post moved from "defer" to "complete" once the underlying paper was located.

### May 24, 2026 — Sources quality refresh + consumer-trust pass

- SOURCES.md: URL canonicalization to `code.claude.com` (3 entries); added "Last curated" header
- Added 4 verified Tier B sources: Builder.io 50 Tips (Gopinath, 2026-03-20), Morph 2026 Guide (2026-02-15), Shipyard Multi-Agent Orchestration (2026-03-18), VoltAgent awesome-claude-code-subagents (20.4k stars). All WebFetch-verified 2026-05-24.
- Backfilled `## Sources` footers across 16 analysis docs that previously relied on inline YAML attribution only. No sources invented; tier subsections populated from existing inline citations and YAML `measurement-claims`.
- Inlined "vendor-reported — not independently benchmarked" caveats on Graphify 71.5× and claude-context ~40% claims at the spots that lacked them (archetype-recommendations evidence-gap table; archetype-a driving-axes line).
- Threaded 7-repo portfolio evidence into `framework-selection-guide.md` and `orchestration-comparison.md` via "Production Evidence" subsections that cross-link the existing portfolio docs.

### April 28, 2026 — Memory & knowledge stack archetype split + Pass-2 testbed

- Split `analysis/memory-systems-archetype-recommendations.md` into 7 per-archetype docs (`memory-systems-archetype-{a..g}-*.md`) following the project's one-pattern-per-file convention
- Added `analysis/memory-systems-recommendation-methodology.md` with the 200/500/6k scale-band math, 8 challengeable assumptions, and applied corrections
- Added `analysis/memory-systems-graphify-vs-understand-anything.md` — direct A/B comparison after running both LLM-driven graph builders on this repo as testbed
- Empirical findings folded back into the recommendations:
  - Graphify Pass 1 (Tree-sitter) indexed 0 of 38 prose docs; Pass 2 (LLM extraction) produced 1187 nodes / 1651 edges / 67 communities / 88% EXTRACTED but with a measured ~25% hallucination rate on EXTRACTED edges (n=8 spot-check)
  - Lum1104 `/understand-knowledge` skill gates on lowercase `index.md` + `raw/` + `log.md` Karpathy layout — falls back to `/understand-anything:understand` for repos that don't match
- Wired up the audit's signal vocabulary: added `md-corpus-{small,design-target,large,very-large}`, `vault-obsidian`, `vault-karpathy`, `corpus-sensitive` to `AUDIT-CONTEXT.md`. Without these, the new archetype docs were unreachable from the audit
- Added helper scripts as documented patterns for downstream consumers: `scripts/graphify_footer_inject.py` (file-level edge aggregation, schema-tolerant), `scripts/graphify_contradiction_lint.py`
- Doc count: 28 → 38; SOURCES.md changelog updated

### April 22, 2026 — One-Prompt Realignment: Routing-Based Advisory Fetch

- Added `AUDIT-CONTEXT.md`: routing map from observed project signals (CLAUDE.md state, harness layout, commit patterns, session diagnostics, model version, project type) to the specific analysis docs that apply. Typical audit now fetches 4–8 docs, not 28, and not the source index alone.
- Rewrote `ONE-LINE-PROMPT.md` as a 4-step flow (collect signals → fetch routing map → conditionally fetch advisories → produce audit). Every recommendation in the structured output must cite the analysis doc and its evidence tier.
- Updated README Quick Start with the new prompt and the "4–8 of 28 docs" framing.
- Added Anthropic Opus 4.7 migration guide (#27, Authority 5), Willison counter-signal (#28, Authority 3), Vertrees operationalization (#29, Authority 2 with Karen note) to `SOURCES-QUICK-REFERENCE.md`. Count bumped 26 → 29.
- Design rationale: prior prompt was blind to applicability (library projects got federated-query advice because the source was high-authority), blind to model version (no 4.7 migration signal), and lacked audit trail (recommendations did not carry doc+tier citations). Routing via `AUDIT-CONTEXT.md` fixes all three.

### April 22, 2026 — Opus 4.7 Migration Integration

- Added `analysis/model-migration-anti-patterns.md`: cross-version anti-pattern matrix (4.5 → 4.6 → 4.7), six Vertrees anti-patterns mapped to Anthropic migration guide, documented MUST-vs-positive-examples tension
- Updated `behavioral-insights.md`: prompt sensitivity table across model versions; Willison and HN counter-signals
- Updated `harness-engineering.md`: 4.7 counter-signal — harness simplifies while prompts need more explicit wording
- Updated `claude-md-progressive-disclosure.md`: references-without-read-enforcement is a 4.7 failure mode; enforcement options (PreToolUse hook, explicit Read, required-reading block)
- Updated `agent-evaluation.md` + `agent-principles.md`: implicit subagent dispatch anti-pattern, single-model eval baselines
- Updated `evidence-based-revalidation.md`: 4.6 → 4.7 as canonical revalidation trigger case study
- Updated SOURCES.md: registered Anthropic migration guide, What's New 4.7, Best Practices 4.7 blog (Tier A); Vertrees, Willison (Tier B); HN 47793411/47814832 (Tier C)
- Internal consistency fixes: added evidence-tier declaration to `evidence-tiers.md` meta-doc; updated `evidence-tiers.md` pedagogical examples to reference 4.7 shift; added explicit "Gap:" statements to `session-quality-tools.md`
- Bumped doc count 27 → 28 across README, PLAN, CLAUDE.md

### April 2026 Review

- Added production-scale agent-driven development evidence to `analysis/harness-engineering.md`:
  - Nick Schrock (Dagster): 1,000+ PRs merged in 3 weeks with Claude Code
  - Matthias Vallentin (Tenzir): 3x development velocity claim
- Updated SOURCES.md with Schrock and Vallentin agent-driven development entries
- Cross-referenced from third-brain concept imports (agent-driven-development-patterns)
- Added `analysis/agent-driven-development.md`: Agent-driven development patterns with quantified evidence from 7 production repos (infrastructure maturity model, cross-repo coordination, security boundaries, velocity data)
- Updated cross-references in 5 existing analysis docs
- Updated SOURCES.md with 7-repo portfolio analysis evidence (Tier A)
- Added 9 additional analysis documents covering all 10 identified gaps:
  - `local-cloud-llm-orchestration.md`: Hybrid MLX+Claude architecture from mndr-review-automation
  - `mcp-client-integration.md`: MCP client patterns from InspectorClient + TmePlaybookClient
  - `federated-query-architecture.md`: 15/15 benchmarks, 86-99% cost savings, TCO calculator
  - `automated-config-assessment.md`: Baseline-deviation-remediation, 3,816+ sensors, 100% detection
  - `claude-md-progressive-disclosure.md`: 3-tier CLAUDE.md evolution across 6 repos
  - `memory-system-patterns.md`: Auto-memory sizing by project type across 5 projects
  - `evidence-based-revalidation.md`: Hypothesis confidence tracking and demo prep
  - `security-data-pipeline.md`: Zeek → OCSF → Parquet → Iceberg pipeline case study
  - `cross-project-synchronization.md`: Dependency cascading across 7 repos
- Synced SOURCES.md: added Internal Methodology section for 3 meta-framework docs (behavioral-insights, confidence-scoring, evidence-tiers)
- Fixed stale line count references in SOURCES.md and SOURCES-QUICK-REFERENCE.md (1,278 → 1,579)
- Committed auto-regenerated INDEX.md (115 → 123 documents, added templates section)

---

## Completed Goals

### High Priority (All Complete)
- ✅ Validation: Test patterns on this repo itself
- ✅ Documentation: Ensure all patterns have examples
- ✅ Self-compliance: Repository follows its own patterns

### Medium Priority (Mostly Complete)
- ✅ Community: Accept contributions (CONTRIBUTING.md created)
- ⚠️ Examples: Update example projects (partially complete)

### Low Priority (Addressed)
- ✅ Automation: Hook patterns documented (3 hooks)

---

## Metrics at Archive Time

**v2.1 snapshot (May 24, 2026)**:

| Metric | v1 Target | v1 Achieved | v2.1 Current |
|--------|-----------|-------------|---------------|
| Analysis documents | — | — | **41** |
| Patterns documented (v1) | 10+ | **17** | (archived to `archive/patterns-v1/`) |
| Source database entries | — | — | **141+** |
| Source attribution | 100% | **100%** | **100%** (Sources footers across all 41 docs) |
| Self-compliance | 100% | **100%** | **100%** |
| Total documents (repo-wide) | — | **48** | tracked in INDEX.md |

---

## Deferred Items

These items were evaluated and consciously deferred:

| Item | Reason | Revisit When |
|------|--------|--------------|
| MCP server for pattern lookup | Requires design decisions (transport, operations, hosting) | When design is clarified |
| Video walkthrough | External infrastructure required | Out of scope |
| Fabric integration guide | Low priority (Tier C source) | Community demand |
| Cross-project skill sync | Needs real use cases first | Community feedback |

---

*This file is updated when work items are completed or milestones are reached.*

---
convergence: single-source
---

# Plan

**Purpose**: Current priorities, immediate next actions
**Last Updated**: August 28, 2026 (prose-corpus discoverability: new analysis doc + instrument + self-audit — `analysis/prose-corpus-discoverability.md` (EMERGING, Mixed A-B, single-source) names the assumption first-party guidance makes about the *unloaded remainder* (*anything Claude can figure out by reading code*, *let Claude fetch what it needs*) and the class of project where it fails: for prose, the discriminating property is authority/currency, which retrieval cannot see. Ships `scripts/measure-link-reachability.py` (reachability from session-loaded entry points + a three-way currency classifier) and `research/corpus-reachability-2026-08-28.md`. **Self-audit result**: reachability passes (**171/181, 94.5%** under E1/refs — INDEX.md + AUDIT-CONTEXT.md + ABSORPTION-MAP.md do that work), currency fails — of 96 `archive/` files only 12 correctly declared themselves superseded, **17 asserted `status: PRODUCTION`/`EMERGING` in their own frontmatter**, and 67 said nothing; every automated check (`markdownlint` `'!archive'`, `check-measurement-expiry.py` default `analysis`) is scoped to the live lane. The 17 are corrected here in a separable commit (`status: ARCHIVED` + tombstone banner, matching the 2026-07 eviction convention); the 67 silent files stay open — see Priorities. Second-order finding: the one check that *does* cover the whole corpus, the daily link-checker workflow, has filed 916 open `documentation` issues that nobody has triaged — a firing check is not a working check, and it is the same pathology that retired the RSS watchers. n=2 corpora, so the doc ships EMERGING not PRODUCTION.) Prior: August 13, 2026 (Claude 5-family + thought-leader content refresh: Opus 5 (2026-07-24) and verified Sonnet 5 integrated across 8 analysis docs — matrix column, net-deltas section, dispatch/verification reversals, tokenizer confound; all seven follow-lane canons liveness-checked (Willison per-release canon spans the full 5 family; Ronacher schema-non-neutrality counter-signal hosted in harness-engineering; Ng/Osmani primaries resolved; Husain/Shankar agentic two-phase eval update; Karpathy stable; ClaudeLog not re-swept); two absorption-lane flags for the ~2026-10 sweep — model-migration follow-lane candidacy (first-party `prompt-audit` + Opus 5 prompting guide, trigger partially fired) and progressive-disclosure partial absorption (first-party adopts the term); new `model-version-opus-5`/`model-version-sonnet-5` routing signals wired end-to-end). Prior: July 18, 2026 (measurement session `research/probe-session-2026-07-18.md`: token-economics re-measure cluster executed, both lapsed OWASP rows reverified, Playwright 4x attribution corrected, MRCR carried item closed as superseded-by-GraphWalks, academic follow-ups checked post-ICML, realistic-prose adherence ladder executed — Fable descriptive ceiling through 200 rules, first same-instrument between-model score difference). Prior: July 16, 2026 (third-party absorption wave: instrument + first sweep + seven-lane repositioning; see `drafts/ABSORPTION-SCAN-2026-07.md` + DECISIONS.md Decision 12), 2026-07-12 (intake-alignment wave), 2026-07-09/10 (Reduction Phases 0–6, Decision 11), June 15, 2026 (loop-engineering + unattended-execution update)

---

## Current Focus

**Phase**: v2.1 — the evidence-graded-audit lane (README § Where This Sits)
**Goal**: Carry the measurements and instruments no other lane publishes, and prune into the other six lanes as they mature — the absorption map (ABSORPTION-MAP.md) is the standing per-doc answer to "who covers what, and what hands off when."

---

## Current Status

| Metric | Status |
|--------|--------|
| Analysis files | 26 (25 routable + template; 44→27 Reduction 2026-07-10, 27→25 absorption wave 2026-07-16, +1 2026-08-28 `prose-corpus-discoverability`) |
| Absorption lanes | 16 none-found (KEEP-SOLE) / 5 follow / 1 retire-toward (mcp-vs-skills-economics → `/usage`) / 2 merged / 1 staged (plugins-and-extensions) |
| Archived v1 patterns | 24 |
| Source database | Last curated 2026-07-16 (absorption-wave sweep: superpowers/ECC re-verified, AGENTS.md-LF + ClaudeLog + CodeGuard-integration + Ronacher/Ng added, negative dossiers for frozen/stale/abandoned absorbers) |

---

## Current Priorities

### High Priority

| Item | Effort | Status |
|------|--------|--------|
| Complete mcp-vs-skills-economics retirement (RETIRING → RETIRED + archive) | Low | Due at the 2026-09-30 review — retained A/B-instrument note relocates or archives with it |
| plugins-and-extensions staged retirement | Medium | Ruled 2026-07-16: **approved as staged**. Due 2026-09-30 revalidate — migrate residual first (community-marketplace table → accept link-rot loss; 300–800ms figure → mcp-patterns), per the substance check in ABSORPTION-SCAN §2.2. 2026-08-19: the DeepSeek Harness refresh recorded counter-evidence to the retirement premise (the cross-runtime plugin-evaluation residual may grow; SOURCE-REFRESH-2026-08-19-deepseek-harness.md §3), so re-examine at the revalidate rather than silently execute |
| September revalidation batch | Medium | 2026-09-21: intent-alignment-audit + scheduled-and-looping-primitives; 2026-09-30: domain-knowledge-architecture (Smart Connections license-risk re-verify) + plugins-and-extensions (above) + memory-systems-recommendation-methodology fold-in into archetype-recommendations (ruled 2026-07-16) |
| behavioral-insights Fable-era re-measure | Medium | Partially executed 2026-07-16 (64-agent probe session, `research/fable-probe-session-2026-07-16.md`): synthetic adherence ladder hit ceiling at every rung (1.0 at 10–150 rules) — Opus-era figures now flagged stale for Fable; Fable-window program CLOSED 2026-07-16 (all gated items run): heterogeneous ladder clean 12/12 through 250 checkable rules (descriptive — no positive control); unread-references and unanchored-triggers re-instrumented, instruments work, descriptive-only under adversarial review (graded re-runs need: <4/4-expected condition; applicability-heterogeneous fixture + second behavior); context-fill (60%-threshold): post-close follow-up executed 2026-07-17 in a fresh session — classifier void SUPERSEDED (instrument executes end-to-end; de-blocking unattributable between session and filler), a silent workflow-path model fallback was caught by adversarial verification (Opus-served readers under a Fable request; new rule: gate probe scoring on per-turn served model) and the gated main-loop re-run produced first Fable rows, descriptive ceiling 10/10 through ~140k tokens on the salient-needle instrument; Gap 317 (fill-vs-quality correlation on realistic material) stays open. **Realistic-prose-rule ladder executed 2026-07-18** (raw record `research/probe-session-2026-07-18.md` Part 3, two-lens verified, instrument archived at `research/artifacts/2026-07-18-realistic-ladder/`): 200-rule realistic-diversity fixture with baseline positive control + golden fixture + same-instrument Opus 4.8 arm — Fable 12/12 gated reps at 1.0 through 200 rules (descriptive ceiling, cap still unlocated); Opus at full n=3/rung after same-day evening replacement reps: 1.0 everywhere except two morning K100 reps at 46/47 on one ambiguously-worded verbatim-phrase rule (fable 6/6 literal vs opus 4/6 — interpretation-dependent literalization-propensity difference, checker-artifact-robust; the program's first same-instrument between-model score difference; not a cap, not a ranking). New residual open item: a Fable-failure-capable design (conflicting/semantic rules, one-pass low-effort regime, distractor load, multiple renderings per rung) |
| v2.1.121 token-economics re-measure cluster | Medium | **Executed 2026-07-18** (raw record `research/probe-session-2026-07-18.md`, two-lens verified): 81,986 figure demoted to historical with a wire re-measure (workspace-mcp 51 tools ~28.8k est. tokens static vs ~0.9k names-only deferred; @playwright/mcp ~4.9k vs the stale ~20K row); both lapsed OWASP-survey rows reverified (42%-of-12,000+ re-cited to BlueRock Tier C; trustworthy-count row withdrawn as never-a-measurement); Playwright 114K/27K "4x" attribution corrected to community benchmarks ~2-3.7x (misapplied stale flag removed); tool-search version pegs corrected repo-wide (default-on v2.1.7, `alwaysLoad` v2.1.121). Residual: none — future re-measures ride the normal revalidate dates (2027-01-18) |
| Backfill supersession markers on the 67 unmarked `archive/` files | Medium | **Opened 2026-08-28** by `analysis/prose-corpus-discoverability.md`. The 17 files that *falsely asserted* a live status were corrected in the same change; these 67 assert nothing, so retrieval still returns them indistinguishable from live prose. Re-measure with `python3 scripts/measure-link-reachability.py --currency` (target: `WRONG=0, absent=0`). Owner call on whether every v1 file earns a banner or whether a lane-level `archive/README.md` plus a `status: ARCHIVED` default suffices. |
| Triage or retire the daily link-checker issue stream | Medium | **Opened 2026-08-28.** `.github/workflows/link-checker.yml` files one "🔗 Broken links detected" issue per day on the cron path; the repo now carries **916 open `documentation`-labelled issues**, the recent ones all that issue, all zero-comment and unedited since creation, while 214 internal links stay dangling. This is the same pathology that got the RSS + source-monitoring watchers deleted in Reduction Phase 6 ("their GitHub issues sat unread — hundreds open, zero triage") — the link checker survived that cull and reproduced it. Options: aggregate into one standing issue that is updated rather than re-filed; make it block the PR path (currently `continue-on-error: true`); split internal-link failures (actionable, 214 of them) from external link rot (mostly not); or retire it on the same reasoning as the watchers. Owner call. |
| Extend the currency check to the lanes no instrument reads | Low | **Opened 2026-08-28.** `markdownlint` excludes `archive` by glob and `check-measurement-expiry.py` defaults to `analysis` — individually reasonable, jointly the reason the dead lane rotted unobserved. Proposal: keep the *style* exclusions, add a *currency* pass over `archive/` (and `research/`, `drafts/`) to `weekly-review` step 5b. |
| Fix `graphify_footer_inject.py` path emission | Low | **Opened 2026-08-28.** Line 114 renders repo-root-relative targets into files under `analysis/`, so 54 generated "Related (from graph)" links across 19 of 26 docs do not resolve from their containing file (`analysis/analysis/…`). One `os.path.relpath` call. The mechanism built to enrich the pointer graph is currently degrading it. |
| Quarterly absorption sweep (emerging-pattern-monitor Phase F) | Low | Next due ~2026-10 — check follow-lane advance triggers + canon liveness; weekly-review 5b trips DRIFT if the map's sweep date exceeds 100 days |

### Owner rulings (all five staged items ruled 2026-07-16)

| Item | Ruling |
|------|--------|
| model-migration-anti-patterns convergence single-source → emerging | **Approved** — flipped in-doc with both exemplars recorded (Willison per-release analyses + Vertrees audit framework, Vertrees provenance-only caveat explicit); map row updated |
| automated-config-assessment candidate-emerging note | **Declined** — stays single-source: doctor/checkup are install-health tooling, not baseline→deviation→remediation assessment substance; advance trigger unchanged on the map row |
| Wire-or-retire `best_practices_reviewer.py` | **Retire** — existence-check-only coupling is the same no-bite defect that killed the RSS watchers; removal executes project1-side (`automation/orchestrator/`), nothing further in this repo |
| memory-systems-recommendation-methodology fold-in | **Approved, batched** — executes in the 2026-09-30 session (fold into archetype-recommendations), not now |

The fifth staged item — plugins-and-extensions final retirement — was ruled the same day: **approved as staged** for the 2026-09-30 revalidate, residual migration first (see High Priority row above).

### Carried research items

| Item | Notes |
|------|-------|
| MRCR-v2 multi-needle retrieval benchmark on Opus 4.8 | **Closed as superseded 2026-07-18**: Anthropic dropped MRCR after the 4.7 card; GraphWalks 256K/1M figures from the 4.8 and Fable/Mythos system cards now recorded in SOURCES.md (Mythos 5 Parents 99.96→97.5; Opus 4.8 BFS 85.9→68.1). Residual open item: no independent third-party long-context coverage of 4.8/Claude 5 found as of 2026-07-18 (re-checked 2026-08-13: still none for Opus 5/Sonnet 5 either) — recheck at the quarterly sweep |
| 4.7-era claims side-by-side re-validation on 4.8 | Open — see model-migration-anti-patterns.md |
| Track ICLR/ICML 2026 follow-ups (Agentic Context Engineering, Meta-Harness) + peer-reviewed publication of the four 2026 arXiv preprints | Checked 2026-07-18 (post-ICML): ACE = ICLR 2026 poster (camera-ready retitled; 226 S2-floor citations); Meta-Harness still preprint (no ICML entry; watch NeurIPS 2026 Dec); MCE (arXiv:2601.21557) registered as first ACE follow-up found — authors claim ICML 2026, proceedings entry unverified, recheck at the quarterly sweep; the other three preprints remain unvenued |

---

## Review Cadence

| Source Type | Frequency | Mechanism |
|-------------|-----------|-----------|
| Anthropic engineering blog + changelog | Weekly | `weekly-review` step 4 (the RSS watcher was deleted in Reduction Phase 6 — manual, in-loop) |
| Absorption-map consistency | Weekly | `weekly-review` step 5b (mechanical greps + self-test line) |
| Follow-lane canons (Willison, Osmani, Ronacher, Ng, Karpathy, Husain/Shankar, ClaudeLog, Miessler) | Quarterly | `emerging-pattern-monitor` Phase F — advance triggers + liveness |
| ECC / superpowers / AGENTS.md / CodeGuard releases | Quarterly | Same Phase F sweep (retire-toward + standards lanes) |
| DeepSeek Harness (deepseek-ai/deepseek-harness) releases | Quarterly, or on release | Same Phase F sweep. Added 2026-08-19 (SOURCE-REFRESH-2026-08-19-deepseek-harness.md): v0.1 developer preview that disclaims stability, so expect breaking changes and re-verify the CC-consumption surfaces (AGENTS.md/CLAUDE.md reader, SKILL.md, hooks bridge, subagent provider) at each check |

---

## Completed Work

Dated activity log lives in [ARCHIVE.md](ARCHIVE.md) — "Detailed Activity Log". Wave summaries live in DECISIONS.md (Decision 11: the 2026-07 reduction; Decision 12: the absorption instrument + first third-party sweep).

## Next Review

**When**: weekly cadence (`/weekly-review`); next judgment sweep ~2026-09-30 (September revalidation batch + the two staged retirements) and the quarterly Phase F pass ~2026-10.
**Focus**: complete the economics-doc retirement; execute the plugins staged retirement after residual migration; run the Fable re-measure and the v2.1.121 token-economics session; put the four staged owner rulings in front of the owner; watch the AGENTS.md ecosystem for data-backed sizing guidance (the advance trigger on claude-md-progressive-disclosure's absorption row) and mem0/Letta docs for archetype-style guidance (the flip trigger on memory-systems-archetype-recommendations).

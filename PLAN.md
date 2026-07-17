---
convergence: single-source
---

# Plan

**Purpose**: Current priorities, immediate next actions
**Last Updated**: July 16, 2026 (third-party absorption wave: instrument + first sweep + seven-lane repositioning; see `drafts/ABSORPTION-SCAN-2026-07.md` + DECISIONS.md Decision 12). Prior: 2026-07-12 (intake-alignment wave), 2026-07-09/10 (Reduction Phases 0–6, Decision 11), June 15, 2026 (loop-engineering + unattended-execution update)

---

## Current Focus

**Phase**: v2.1 — the evidence-graded-audit lane (README § Where This Sits)
**Goal**: Carry the measurements and instruments no other lane publishes, and prune into the other six lanes as they mature — the absorption map (ABSORPTION-MAP.md) is the standing per-doc answer to "who covers what, and what hands off when."

---

## Current Status

| Metric | Status |
|--------|--------|
| Analysis files | 25 (24 routable + template; 44→27 Reduction 2026-07-10, 27→25 absorption wave 2026-07-16) |
| Absorption lanes | 15 none-found (KEEP-SOLE) / 5 follow / 1 retire-toward (mcp-vs-skills-economics → `/usage`) / 2 merged / 1 staged (plugins-and-extensions) |
| Archived v1 patterns | 24 |
| Source database | Last curated 2026-07-16 (absorption-wave sweep: superpowers/ECC re-verified, AGENTS.md-LF + ClaudeLog + CodeGuard-integration + Ronacher/Ng added, negative dossiers for frozen/stale/abandoned absorbers) |

---

## Current Priorities

### High Priority

| Item | Effort | Status |
|------|--------|--------|
| Complete mcp-vs-skills-economics retirement (RETIRING → RETIRED + archive) | Low | Due at the 2026-09-30 review — retained A/B-instrument note relocates or archives with it |
| plugins-and-extensions staged retirement | Medium | Ruled 2026-07-16: **approved as staged**. Due 2026-09-30 revalidate — migrate residual first (community-marketplace table → accept link-rot loss; 300–800ms figure → mcp-patterns), per the substance check in ABSORPTION-SCAN §2.2 |
| September revalidation batch | Medium | 2026-09-21: intent-alignment-audit + scheduled-and-looping-primitives; 2026-09-30: domain-knowledge-architecture (Smart Connections license-risk re-verify) + plugins-and-extensions (above) + memory-systems-recommendation-methodology fold-in into archetype-recommendations (ruled 2026-07-16) |
| behavioral-insights Fable-era re-measure | Medium | Partially executed 2026-07-16 (64-agent probe session, `research/fable-probe-session-2026-07-16.md`): synthetic adherence ladder hit ceiling at every rung (1.0 at 10–150 rules) — Opus-era figures now flagged stale for Fable; Fable-window program CLOSED 2026-07-16 (all gated items run): heterogeneous ladder clean 12/12 through 250 checkable rules (descriptive — no positive control); unread-references and unanchored-triggers re-instrumented, instruments work, descriptive-only under adversarial review (graded re-runs need: <4/4-expected condition; applicability-heterogeneous fixture + second behavior); context-fill (60%-threshold) void on a harness classifier block — needs a fresh session, Gap 317 open. Realistic-prose-rule ladder remains the durable open item |
| v2.1.121 token-economics re-measure cluster | Medium | Open — mcp-patterns (81,986-token figure + two lapsed OWASP reverifies) and plugins-and-extensions (4x claims); one measurement session clears the cluster |
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
| MRCR-v2 multi-needle retrieval benchmark on Opus 4.8 | Open — "better long-context" remains directional (Tier A), not quantified |
| 4.7-era claims side-by-side re-validation on 4.8 | Open — see model-migration-anti-patterns.md |
| Track ICLR/ICML 2026 follow-ups (Agentic Context Engineering, Meta-Harness) + peer-reviewed publication of the four 2026 arXiv preprints | Ongoing |

---

## Review Cadence

| Source Type | Frequency | Mechanism |
|-------------|-----------|-----------|
| Anthropic engineering blog + changelog | Weekly | `weekly-review` step 4 (the RSS watcher was deleted in Reduction Phase 6 — manual, in-loop) |
| Absorption-map consistency | Weekly | `weekly-review` step 5b (mechanical greps + self-test line) |
| Follow-lane canons (Willison, Osmani, Ronacher, Ng, Karpathy, Husain/Shankar, ClaudeLog, Miessler) | Quarterly | `emerging-pattern-monitor` Phase F — advance triggers + liveness |
| ECC / superpowers / AGENTS.md / CodeGuard releases | Quarterly | Same Phase F sweep (retire-toward + standards lanes) |

---

## Completed Work

Dated activity log lives in [ARCHIVE.md](ARCHIVE.md) — "Detailed Activity Log". Wave summaries live in DECISIONS.md (Decision 11: the 2026-07 reduction; Decision 12: the absorption instrument + first third-party sweep).

## Next Review

**When**: weekly cadence (`/weekly-review`); next judgment sweep ~2026-09-30 (September revalidation batch + the two staged retirements) and the quarterly Phase F pass ~2026-10.
**Focus**: complete the economics-doc retirement; execute the plugins staged retirement after residual migration; run the Fable re-measure and the v2.1.121 token-economics session; put the four staged owner rulings in front of the owner; watch the AGENTS.md ecosystem for data-backed sizing guidance (the advance trigger on claude-md-progressive-disclosure's absorption row) and mem0/Letta docs for archetype-style guidance (the flip trigger on memory-systems-archetype-recommendations).

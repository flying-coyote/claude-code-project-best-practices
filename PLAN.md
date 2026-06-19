# Plan

**Purpose**: Current priorities, immediate next actions
**Last Updated**: June 15, 2026 (loop-engineering + unattended-execution update: new EMERGING doc, 7 audit signals, routing-invariant fix, volatile Fable 5 / Mythos 5 currency note). Prior: June 4, 2026 (first-party introspection; session-quality-tools.md → RETIRING via /insights)

---

## Current Focus

**Phase**: v2.1 — Production Evidence Integration
**Goal**: Maintain focused, evidence-based analysis that complements ECC and superpowers

---

## Current Status

| Metric | Status |
|--------|--------|
| Analysis documents | 42 |
| Archived v1 patterns | 24 |
| Source database entries | 141+ (Tier A sweep 2026-05-24 added: Meta-Harness arXiv:2603.28052, Pan et al./Tsinghua arXiv:2603.25723 — attribution corrected from "Tingua", Agentic Context Engineering arXiv:2510.04618 ICLR 2026, SWE-Bench Mobile arXiv:2602.09540, Memanto arXiv:2604.22085, LongMemEval-V2 arXiv:2605.12493, Teaching Claude why, agent-view/ultrareview/`/goal` Anthropic docs) |
| Source attribution | 100% (16 docs backfilled with `## Sources` footers on 2026-05-24) |

---

## Current Priorities

### High Priority

| Item | Effort | Status |
|------|--------|--------|
| Monitor Tier A sources for new insights | Low | Ongoing |
| Keep SOURCES.md current (biweekly) | Low | Ongoing |
| Update analysis docs when new evidence emerges | Medium | Ongoing |
| Opus 4.8 release re-validation (model-coupled docs) | Medium | **Done 2026-05-30** — 4.8 deltas, sycophancy nuance, injection regression §5.2, 60%-threshold revalidation, MRCR case study, soft-guideline anti-pattern, `model-version-4-8` routing. See model-migration-anti-patterns / behavioral-insights / safety-and-sandboxing / harness-engineering |
| Benchmark multi-needle long-context retrieval (MRCR-v2) on Opus 4.8 | Medium | Open — no public 4.8 MRCR transcription yet; "better long-context" 4.8 claim is directional (Tier A), not quantified |
| Revalidate 4.7-era claims on Opus 4.8 (side-by-side output diff) | Medium | Open — see [model-migration-anti-patterns.md](analysis/model-migration-anti-patterns.md) |
| CI regression tests for prompt anti-patterns (Vertrees proposal) | Medium | Deferred — out of scope until Anthropic publishes guidance |
| Monitor first-party feature convergence for retirement (replacement-readiness) | Low | **Ongoing** — obsolescence sweep 2026-06-04 registered `/insights`, `/usage`, `/doctor` (Tier A). `session-quality-tools.md` → RETIRING (defers to `/insights`). Watch list: MCP/skills economics ← `/usage` per-category; install-health ← `/doctor`. Tracked via `emerging-pattern-monitor` retirement lane + CONTRIBUTING § Retiring a doc |
| Obsolescence sweep + routing/count hygiene | Low | **Done 2026-06-04** — core (static evidence-tiered routing, model-migration detection, memory archetypes) has no first-party equivalent as of June 2026; only session-diagnostics commoditized (→ `/insights`). Wired previously-unreachable `dapr-durable-agents.md` into routing (`project-type-agent-infra`); reconciled stale doc counts (28/38 → 41) and backfilled 3 missing docs in the README Core Analysis table |
| Loop-engineering + unattended-execution update | Medium | **Done 2026-06-15** — new EMERGING [`scheduled-and-looping-primitives.md`](analysis/scheduled-and-looping-primitives.md); 7 audit signals under AUDIT-CONTEXT "Unattended / Long-Running Execution" (`harness-loop-config`, `harness-scheduled-agent`, `ci-scheduled-agent`, `harness-background-tasks`, `harness-dynamic-workflows`, `harness-goal-completion-loop`, `cron-disabled`); `ONE-LINE-PROMPT.md` "Unattended Execution Exposure" output section; loop-engineering fold-in + `/goal` version/claim fixes + Rajasekaran/Managed-Agents/Karpathy citations in `harness-engineering.md`; routing-invariant fix (two-level memory-index sub-route documented); volatile Fable 5 / Mythos 5 currency note + `model-version-fable-mythos` row. See Decision 10 |

### Medium Priority

| Item | Effort | Notes |
|------|--------|-------|
| Update internal cross-references in analysis/ docs | Low | Completed April 2026 |
| Review CONTRIBUTING.md for v2.1 alignment | Low | Completed April 2026 |

### Low Priority

| Item | Effort | Notes |
|------|--------|-------|
| Consider consolidated "key findings" summary page | Medium | Single-page executive summary |

---

## Review Cadence

| Source Type | Frequency | Automation |
|-------------|-----------|------------|
| Anthropic Engineering Blog | Weekly | anthropic-blog-rss.yml |
| Boris Cherny interviews/posts | Monthly | Manual |
| Nate B. Jones publications | Monthly | Manual |
| IndyDevDan repos/content | Monthly | Manual |
| ECC major releases | Monthly | Manual |

---

## Completed Work

Dated activity log for all completed work has moved to [ARCHIVE.md](ARCHIVE.md) — see "Detailed Activity Log" section.

## Next Review

**When**: Late June 2026 (next biweekly cadence, ~2 weeks from 2026-06-15)
**Focus**: Re-verify the **volatile Fable 5 / Mythos 5 suspension** and update the currency notes + `model-version-fable-mythos` row when access is restored or the suspension is made permanent; **transcribe Boris Cherny's WorkOS *Acquired Unplugged* recording (2026-06-02)** for the verbatim "write loops" quote currently resting on secondaries; watch whether "loop engineering" accumulates production evidence (graduate `scheduled-and-looping-primitives.md` EMERGING → PRODUCTION) or whether first-party tooling absorbs the audit value (retirement lane); **`harness-goal-completion-loop` validated + graduated 2026-06-19** (anchored user-turn-head predicate, measured 80%→0% false-positive; now triggers) and **dynamic-workflow caps re-confirmed** (per-run 1,000 / up to 16 concurrent; the `cores−2` formula and 4096 item-cap are NOT in the docs — the live docs were already clean) and **`CronList` confirmed not to enumerate cloud Routines**; still owed: testbed-confirm `harness-scheduled-agent`'s `SKILL.md` leaf via a real Desktop scheduled task. Carry-forward: biweekly Tier A sweep; benchmark MRCR-v2 multi-needle retrieval on Opus 4.8; watch for a 4.7→4.8 migration-guide expansion and Petri 3.0 / injection-robustness follow-ups; track ICLR/ICML 2026 papers building on Agentic Context Engineering and Meta-Harness; watch for primary peer-reviewed publication of the four 2026 arXiv preprints.

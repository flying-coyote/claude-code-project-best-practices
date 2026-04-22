---
version-requirements:
  claude-code: "v2.1.0+"
version-last-verified: "2026-04-06"
measurement-claims:
  - claim: "H-CONFIG-01 confidence advanced from 3.0/5 to 4.7/5 over 3 days through 5 explicit revalidation events"
    source: "Direct analysis — third-brain H-CONFIG-01-evidence.md confidence history"
    date: "2026-04-06"
    revalidate: "2026-10-06"
  - claim: "H-NDR-FEDERATION-01 confidence at 4.6/5 after 4 milestones (M1-M4) each with production-scale benchmarks"
    source: "Direct analysis — third-brain H-NDR-FEDERATION-01-evidence.md"
    date: "2026-04-06"
    revalidate: "2026-10-06"
status: "PRODUCTION"
last-verified: "2026-04-06"
---

# Evidence-Based Revalidation: Hypothesis-Driven Confidence Tracking

**Evidence Tier**: A — Direct observation of hypothesis validation across third-brain and spoke repos

## Purpose

This document analyzes the pattern of **re-running tests, benchmarks, and validations** before making claims or presenting results — specifically the hypothesis confidence scoring system used across the portfolio. The key insight: confidence scores are not opinions; they are **audit trails** tied to specific technical events, with explicit statements of what remains unvalidated.

---

## The Revalidation Pattern

### Hypothesis → Milestones → Confidence → Demo

```
Hypothesis formulated (confidence 0.5-1.0)
    │
    ▼
Milestone 1: Initial validation (confidence → 2.0-3.0)
    │
    ▼
Milestone N: Production-scale benchmark (confidence → 4.0-4.5)
    │
    ▼
Revalidation event: Re-run benchmarks with current code (confidence → 4.5-5.0)
    │
    ▼
Demo/presentation: Confidence scores cited as evidence with remaining gaps explicit
```

### Confidence as Audit Trail

Each confidence increment is tied to a specific technical event and explicitly states remaining gaps:

| Confidence | What It Means | Required Evidence |
|-----------|---------------|-------------------|
| 1.0-2.0 | Hypothesis plausible, no implementation | Literature review, competitor analysis |
| 2.0-3.0 | Initial validation against known data | Ground truth detection, POC working |
| 3.0-4.0 | Multi-milestone validation | Production-scale benchmarks passing |
| 4.0-4.5 | All dimensions validated | Automated end-to-end pipeline, LLM integration |
| 4.5-5.0 | External validation pending | Peer review, customer validation, blind assessment |

---

## Case Study: H-CONFIG-01 Confidence Progression

| Date | Confidence | Event | Remaining Gap |
|------|-----------|-------|---------------|
| 2026-04-04 | 3.0/5 | Hoosier ground truth: 12/12 known issues detected | Fleet Manager API access unknown |
| 2026-04-04 | 3.5/5 | Blocker resolved: health-inventory already collects config via LogScale | POC Phases 2-4 not yet run |
| 2026-04-04 | 4.0/5 | POC complete: adapter + engine + remediation validated | LLM remediation untested |
| 2026-04-04 | 4.5/5 | LLM remediation: 5 findings generated successfully (433.5s, Gemma 4 31B) | Suricata telemetry extraction missing |
| 2026-04-06 | 4.7/5 | Suricata YAML extraction: all 5 dimensions fully automated | PS engineer blind review pending |

**Critical property**: Each row explicitly states what was NOT validated ("Remaining Gap"). A confidence score of 4.7/5 does not mean "almost certain" — it means "all automated dimensions validated, external peer review outstanding."

---

## Case Study: H-NDR-FEDERATION-01

| Milestone | Confidence | Evidence | Method |
|-----------|-----------|---------|--------|
| M1: OCSF Pipeline | 3.5/5 | 20M events, 74 fields, 25 compliance checks | Production-scale data generation + validation |
| M2: Federation Benchmark | 4.0/5 | 15/15 queries pass, all < 10s | 15-query benchmark suite (`d2_benchmark_suite.py`) |
| M3: WAN Bandwidth | 4.3/5 | 93-99.9% reduction across all scenarios | Centralized vs. federated transfer measurement |
| M4: Competitive Parity | 4.6/5 | Path to match ExtraHop in 3.5-6.5 weeks | Competitive analysis + OCSF mapping assessment |

---

## Revalidation Before Demo

The AI Stakeholder Forum Meeting 2 demo script shows how revalidation works in practice. Before presenting results, each deliverable is re-verified:

1. **TME MCP**: 33 patterns, 26 playbooks, 67 tests — re-run test suite before demo
2. **Config Assessment**: Confidence 4.7/5, all 5 dimensions — re-run against current fleet data
3. **MNDR + TME Integration**: 3-phase enrichment — validate Inspector + Investigator + TME Playbook all responding
4. **Federated Query**: 15/15 queries — re-run benchmark suite against current data

**Why revalidate**: Code changes between validation and presentation can break previously-passing results. A benchmark that passed on 2026-04-04 may fail on 2026-04-07 if a dependency updated. The revalidation step catches regressions before they become false claims in a presentation.

---

## Scheduled Revalidation

Cross-repo dependency monitoring (from third-brain `scheduled_tasks.json`) runs weekday mornings:

- Checks corelight-inspector for upstream changes
- Alerts if tool signatures or schemas changed
- Prevents silent integration failures between revalidation events

This is **continuous revalidation** — not triggered by milestones, but by the passage of time and upstream changes.

---

## Case Study: Model Migration as Revalidation Trigger (Opus 4.6 → 4.7, April 2026)

The Opus 4.7 release on 2026-04-16 is a canonical revalidation trigger that does **not** fit the usual milestone pattern. No code changed; no benchmark ran; the only change was the underlying model's prompt-interpretation behavior. Yet claims validated on 4.6 can no longer be cited without re-verification.

### Why This Is a Revalidation Event

The [Anthropic migration guide](https://platform.claude.com/docs/en/about-claude/models/migration-guide) states: "Claude Opus 4.7 interprets prompts more literally and explicitly than Claude Opus 4.6... It will not silently generalize an instruction from one item to another." This means any prompt, skill, or CLAUDE.md instruction that depended on 4.6's willingness to infer intent may now produce a silent no-op on 4.7 — the output looks plausible, but the actual work was never performed.

Silent no-ops are the worst class of regression: no exception, no failed assertion, no visible symptom. Only revalidation catches them.

### Revalidation Table (this repo's own claims)

| Claim | 4.6 status | 4.7 revalidation approach | Gap |
|---|---|---|---|
| CLAUDE.md instructions followed ~80% of the time | Validated (Boris Cherny, March 2026) | Re-run sample on 4.7 with same CLAUDE.md; measure whether literal interpretation raises or lowers rate | Not yet measured |
| References in CLAUDE.md trigger file reads | Advisory loading worked on 4.6 | Mechanical enforcement required on 4.7 (PreToolUse hook, explicit Read step) | See [progressive-disclosure](claude-md-progressive-disclosure.md) |
| Implicit subagent dispatch ("execute in parallel") spawns subagents | Validated on 4.6 | Migration guide confirms 4.7 spawns fewer by default — explicit dispatch required | See [Model Migration Anti-Patterns](model-migration-anti-patterns.md) |
| 16 occurrences of "Opus 4.5/4.6" across analysis/ | Current as of prior release | Each needs either revalidation on 4.7 or explicit historical framing | Tracked in [PLAN.md](../PLAN.md) |

### Pattern Generalization

Any model release is a revalidation trigger for:

1. **Prompt-sensitivity claims** — literal vs. inferred interpretation can shift
2. **Subagent-dispatch claims** — default spawning behavior can shift
3. **Verbosity claims** — response-length calibration can shift
4. **Tool-use frequency claims** — default tool-call behavior can shift

Unlike code-driven revalidation (a benchmark script you can re-run), model-driven revalidation requires side-by-side behavior comparison: run the same prompt on the old and new version, diff outputs, flag divergences. This is a new revalidation method worth formalizing.

---

## Integration with Evidence Tiers

The revalidation pattern connects to the [Evidence Tiers](./evidence-tiers.md) system:

| Evidence Tier | Revalidation Requirement |
|--------------|-------------------------|
| Tier A (primary observation) | Re-run benchmark/test with current code before citing |
| Tier B (expert practitioner) | Verify claim still holds for current version |
| Tier C (industry report) | Check publication date; flag if > 6 months old |
| Tier D (opinion/anecdote) | Do not cite without corroborating evidence |

The `measurement-claims` frontmatter in each analysis document includes `revalidate` dates — explicit expiration timestamps for claims. This is revalidation built into the document format.

---

## Anti-Patterns

| Anti-Pattern | Symptom | Fix |
|-------------|---------|-----|
| Citing stale benchmarks | "15/15 pass" from last month, but code changed since | Re-run benchmark suite before citing; include revalidation date |
| Confidence without remaining gaps | "4.7/5 confidence" with no mention of what's unvalidated | Every confidence score must state what remains |
| Demo without revalidation | Presenter discovers failures live | Revalidation step in demo prep checklist |
| One-time validation | "It worked in March" as permanent proof | Scheduled revalidation or `revalidate` dates in frontmatter |
| Model version drift | Claim validated on 4.6 cited after 4.7 release | Re-verify on new model; prompt behavior changes silently |

---

## Sources

### Tier A (Direct Production Observation)

- H-CONFIG-01 confidence history (April 2026) — 5 revalidation events over 3 days, 3.0→4.7/5
- H-NDR-FEDERATION-01 milestone validation (April 2026) — 4 milestones with production-scale benchmarks
- AI Stakeholder Forum Meeting 2 demo script (April 2026) — 4 deliverables with pre-demo revalidation

### Related Analysis

- [Evidence Tiers](./evidence-tiers.md) — Dual-tier classification system for claims
- [Confidence Scoring](./confidence-scoring.md) — Assessment framework for research hypotheses
- [Automated Config Assessment](./automated-config-assessment.md) — H-CONFIG-01 as primary revalidation case study
- [Federated Query Architecture](./federated-query-architecture.md) — H-NDR-FEDERATION-01 as milestone revalidation case study
- [Model Migration Anti-Patterns](./model-migration-anti-patterns.md) — Opus 4.6 → 4.7 as a revalidation trigger; six prompt anti-patterns to audit on each release

---

*Last updated: April 2026*

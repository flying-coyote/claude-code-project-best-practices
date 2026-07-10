---
measurement-claims:
  - claim: "12/12 known configuration issues detected in Hoosier Energy ground truth (100% detection rate, target >=80%)"
    source: "Direct analysis — health-inventory tests/test_engine.py"
    date: "2026-04-06"
    revalidate: "2026-10-06"
status: PRODUCTION
last-verified: "2026-07-10"
evidence-tier: A
applies-to-signals: [project-type-config-assessment]
revalidate-by: 2026-10-06
---

# Automated Config Assessment: Baseline-Deviation-Remediation Pattern

> **Collapsed 2026-07-10 (Reduction Phase 4).** The config-assessment slice went native (claude doctor + /checkup v2.1.205; fewer-permission-prompts + update-config skills). Kept delta: the baseline-deviation-remediation pattern and the Hoosier 12/12 ground-truth measurement.

**Evidence Tier**: A — Direct production analysis of the health-inventory deviation engine + third-brain hypothesis validation.

## Purpose

This document keeps two things out of a longer prior analysis: a reusable assessment pattern (baseline → deviation → remediation) for domains that still lack a native config-assessment tool, and the ground-truth measurement that validated it. The full walkthrough of the pattern's NDR implementation — YAML baseline schema, deviation engine internals, template/LLM remediation paths — is cut, because `claude doctor` and `/checkup` (v2.1.205) now cover that mechanism for Claude Code's own configuration.

## The Pattern: Baseline → Deviation → Remediation

Three layers, in sequence: a baseline specification (e.g., YAML) formalizes expected state, per-check severity, and remediation guidance; a deviation engine compares live telemetry against those thresholds and emits scored, structured findings; a remediation generator turns findings into a prioritized action plan (template-based and deterministic, optionally LLM-enhanced for richer context).

The pattern generalizes beyond NDR sensor configuration to any domain where compliance must be assessed at scale against a formalized baseline — cloud infrastructure compliance (CIS benchmarks), database configuration audit, network device hardening, application security posture. For Claude Code's own configuration, the pattern is now native: `claude doctor` / `/checkup` run the deviation-detection layer, and the bundled `fewer-permission-prompts` and `update-config` skills run the remediation layer.

## Hoosier Energy Ground Truth (Measurement Note)

The Hoosier Energy MNDR review identified 12 specific configuration issues across 16 sensors. The health-inventory deviation engine (`lib/config_assessment/`, validated via `tests/test_engine.py`) detected all 12. Five of the findings carry a measured value beyond the issue label itself:

- **Missed bytes**: Bartholomew sensor at 54.84% average — more than half of TCP streams incomplete
- **No-three-way**: fleet at 98.81% peak — cannot determine connection initiator
- **Missing local_nets**: WIN-Sensor — 263K connections misclassified as external-to-external
- **Undefined VULN_SCANNERS**: 5,990 false Log4j RCE alerts from an internal Nessus scanner
- **Export lag**: Owen County — 81 days behind on exports (silent data loss)

Full table, all 12:

| Known Issue | Severity | Detected? |
|-------------|----------|-----------|
| Owen County 81-day export lag | Critical | Yes |
| Wayne-White 6+ day export lag | Critical | Yes |
| Zero exporters (offline sensor) | Critical | Yes |
| Bartholomew 54.84% missed bytes | Critical | Yes |
| Bartholomew 98.81% no-three-way | Critical | Yes |
| Fleet-wide missing community_id | High | Yes |
| Fleet-wide missing hassh | High | Yes |
| Missing log filters (fleet) | High | Yes |
| WIN-Sensor missing local_nets | Critical | Yes |
| Undefined VULN_SCANNERS | High | Yes |
| Henry AP-200 0.19% packet drops | Medium | Yes |
| Decatur 19.1% checksum errors | Medium | Yes |

**Detection rate**: 100% (target was >= 80%). Evidence Tier A, dated 2026-04-06, revalidate by 2026-10-06 (see frontmatter `measurement-claims`).

## Sources

### Tier A (Direct Production Observation)

- health-inventory deviation engine (April 2026) — `lib/config_assessment/`, validated against `tests/test_engine.py`
- third-brain H-CONFIG-01 hypothesis (April 2026) — source of the Hoosier ground-truth dataset

### Tier B (Validated / Expert Practitioner)

- Hoosier Energy MNDR review findings — ground truth dataset for validation (12 known issues, 16 sensors)

## Related Analysis

- [Agent-Driven Development](./agent-driven-development.md) — health-inventory as a Level 2 (Standard Infrastructure) example
- [Harness Engineering](./harness-engineering.md) — diagnostic framework applied to config-assessment development

---

*Last updated: July 2026*

<!-- graphify-footer:start -->

## Related (from graph)

- [`AUDIT-CONTEXT.md`](AUDIT-CONTEXT.md) [EXTRACTED (1.00)] — references
- [`INDEX.md`](INDEX.md) [EXTRACTED (1.00)] — references

<!-- graphify-footer:end -->

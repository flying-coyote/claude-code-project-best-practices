---
version-requirements:
  claude-code: "v2.1.0+"
version-last-verified: "2026-04-06"
measurement-claims:
  - claim: "12/12 known configuration issues detected in Hoosier Energy ground truth (100% detection rate, target >=80%)"
    source: "Direct analysis — health-inventory tests/test_engine.py"
    date: "2026-04-06"
    revalidate: "2026-10-06"
  - claim: "3,816+ sensors assessed at fleet scale with zero processing errors"
    source: "Direct analysis — health-inventory unified_health_2026-04.csv"
    date: "2026-04-06"
    revalidate: "2026-10-06"
  - claim: "5-dimension baseline covering capture quality, detection coverage, network accuracy, Suricata tuning, and export health"
    source: "Direct analysis — health-inventory config/ndr-config-best-practices-baseline.yaml"
    date: "2026-04-06"
    revalidate: "2026-10-06"
  - claim: "Hypothesis confidence 4.7/5 after all 5 dimensions fully automated with Suricata telemetry extraction"
    source: "Direct analysis — third-brain H-CONFIG-01-evidence.md"
    date: "2026-04-06"
    revalidate: "2026-10-06"
status: "PRODUCTION"
last-verified: "2026-04-06"
---

# Automated Config Assessment: Baseline-Deviation-Remediation Pattern

**Evidence Tier**: A — Direct production analysis of health-inventory deviation engine + third-brain hypothesis validation

## Purpose

This document analyzes a **reusable assessment pattern**: YAML baseline specification defines expected state, a deviation engine compares actual sensor data against thresholds to produce scored findings, and a remediation generator creates actionable guidance (template-based or LLM-enhanced). The pattern was validated against 3,816+ NDR sensors with 100% detection rate on known ground truth issues.

The pattern applies beyond NDR: any domain where configuration compliance must be assessed at scale against a formalized baseline.

---

## Architecture: Three-Layer Pipeline

```
YAML Baseline Spec          Sensor Telemetry (CSV)
(thresholds, severity,      (43 config + 19 stats +
 attack impact, MITRE)       10 inventory fields)
        │                           │
        ▼                           ▼
┌──────────────────────────────────────────┐
│  Layer 1: Adapter                         │
│  CSV row → SensorProfile dataclass        │
│  (model capacity mapping, module          │
│   resolution, Suricata YAML decode)       │
└──────────────────┬───────────────────────┘
                   ▼
┌──────────────────────────────────────────┐
│  Layer 2: Deviation Engine                │
│  SensorProfile → AssessmentResult         │
│  (5 dimensions × N checks per dimension,  │
│   severity scoring, MITRE mapping)        │
└──────────────────┬───────────────────────┘
                   ▼
┌──────────────────────────────────────────┐
│  Layer 3: Remediation Generator           │
│  Findings → Prioritized Action Plan       │
│  (template path: deterministic, always    │
│   works; LLM path: richer context,        │
│   optional, MLX/Gemma local inference)    │
└──────────────────────────────────────────┘
```

---

## Layer 1: YAML Baseline Specification

The baseline YAML formalizes 5 configuration dimensions with thresholds, severity levels, attack impact descriptions, and remediation templates:

### Five Dimensions

| Dimension | What It Checks | Critical Threshold Example | Attack Impact |
|-----------|---------------|---------------------------|---------------|
| **Capture Quality** | missed_bytes_pct, no_three_way_pct, packet_drops_pct, checksum_error_pct | missed_bytes > 1.0% | Incomplete TCP stream reassembly |
| **Detection Coverage** | 90+ Zeek packages (community_id, hassh, ssh_bruteforce, smb_lateral, etc.) + log filters | community_id missing | No cross-log correlation capability |
| **Network Accuracy** | local_nets completeness, HOME_NET consistency, BPF filter review | local_nets incomplete | Traffic misclassified as external-to-external |
| **Suricata Tuning** | VULN_SCANNERS, infrastructure_ips, authorized_remote_tools variables | VULN_SCANNERS undefined | Thousands of false alerts from internal scanners |
| **Export Health** | export_lag_hours, zero_exporters, exporter_count | export_lag > 24 hours | Silent data loss — no alerts for missing data |

### Baseline Evidence (Ground Truth)

Each threshold is grounded in real findings from Hoosier Energy MNDR reviews:

- **Missed bytes**: Hoosier Bartholomew sensor at 54.84% average — more than half of TCP streams incomplete
- **No-three-way**: Hoosier fleet at 98.81% peak — cannot determine connection initiator
- **Missing local_nets**: Hoosier WIN-Sensor — 263K connections misclassified as external-to-external
- **Undefined VULN_SCANNERS**: Hoosier — 5,990 false Log4j RCE alerts from internal Nessus scanner
- **Export lag**: Hoosier Owen County — 81 days behind on exports (silent data loss)

---

## Layer 2: Deviation Engine

### Severity Scoring

```python
SEVERITY_SCORES = {"critical": 10, "high": 7, "medium": 4, "low": 1, "info": 0}
```

Each finding receives a severity from the baseline, mapped to a numeric score. The `AssessmentResult` aggregates:

- `total_checks`: All checks attempted
- `passed` / `failed` / `skipped`: Per-sensor breakdown
- `detection_rate`: Percentage of checks that found deviations
- `compliance_pct`: Percentage of checks that passed
- `total_score`: Sum of severity scores for all findings

### Finding Structure

Each finding includes everything needed for both human review and LLM processing:

| Field | Purpose |
|-------|---------|
| `dimension` | Which of 5 dimensions (e.g., "capture_quality") |
| `check_name` | Specific check (e.g., "missed_bytes_pct") |
| `severity` | critical/high/medium/low/info |
| `current_value` | What the sensor actually reports |
| `expected_value` | What the baseline defines as acceptable |
| `remediation_template` | Key into baseline YAML remediation section |
| `attack_impact` | What an attacker gains from this gap |
| `mitre_techniques` | Relevant ATT&CK technique IDs |
| `evidence` | Specific ground truth reference |
| `remediation_time` | Estimated fix time (e.g., "15 min") |

### Telemetry Gap Handling

Not all data is always available. The engine handles three gap patterns:

1. **Truncated data**: The `detection_modules_loaded` field caps at ~148 chars, causing 40K false "package not loaded" findings. **Fix**: Use `bp_failed_checks` as the authoritative source instead.
2. **Missing telemetry**: Suricata YAML blob requires base64 decode. Some sensors don't report it. **Fix**: Mark checks as `skipped` rather than `failed`.
3. **Model-dependent behavior**: AP-200 at 5K conn/s capacity behaves differently than AP-5000 at 100K. **Fix**: `MODEL_CAPACITY` mapping normalizes thresholds by sensor model.

---

## Layer 3: Remediation Generator

### Dual-Path Architecture

**Template path** (deterministic, always available):

```yaml
check_export_connectivity:
  title: "Resolve export lag or failed exports"
  steps:
    - "Check export target connectivity (S3 bucket, Kafka, syslog)"
    - "Verify IAM/credential permissions for export destination"
    - "Check export queue depth on sensor"
  risk: low
  typical_time: "1-2 hours"
```

**LLM path** (richer context, optional):

- Uses MLX/Gemma 4 31B locally (same local-only constraint as [Local+Cloud LLM Orchestration](./local-cloud-llm-orchestration.md))
- Prompt: "You are a Corelight PS engineer. Be concise and actionable."
- Temperature: 0.3, max 500 tokens
- Falls back to template-only if MLX unavailable
- Output structure: What/Why/Verify/Time/Risk

### Operational Impact Assessment

Each dimension maps to a remediation impact category:

| Dimension | Impact | Maintenance Window? |
|-----------|--------|-------------------|
| Capture Quality | Infrastructure change (SPAN/TAP reconfiguration) | Yes |
| Detection Coverage | Package enable/disable | No — immediate effect |
| Network Accuracy | Configuration via Fleet Manager | No — immediate effect |
| Suricata Tuning | Suricata configuration change | May require restart |
| Export Health | Investigate pipeline (network, credential, capacity) | Depends on root cause |

### Report Output

Prioritized action plan: quick wins (detection coverage, network accuracy) → config changes (Suricata tuning) → infrastructure changes (capture quality, export health).

---

## Validation Results

### Ground Truth: 12/12 Known Issues Detected

Hoosier Energy MNDR review identified 12 specific configuration issues across 16 sensors. The deviation engine detected all 12:

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

**Detection rate**: 100% (target was >= 80%)

### Fleet Scale: 3,816+ Sensors

- Zero processing errors across full fleet
- Compliance distribution: 85.8% in 70-89%, 14.2% in 50-69%
- Top fleet-wide gaps: log filters (100% missing), Suricata variables (100% missing), community_id (99.9% missing)

### LLM Remediation Quality

5 critical Hoosier findings tested with MLX/Gemma 4 31B:

- All 5 generated successfully (~87s per finding)
- Consistent output structure
- Sensor-model-aware Fleet Manager navigation paths
- Passed initial PS engineer review (no hallucinated commands)

---

## Reusability Beyond NDR

The three-layer pattern (baseline → deviation → remediation) applies wherever:

1. **A formalized baseline exists** (or can be created from expert knowledge)
2. **Telemetry is available** (CSV, API, structured data)
3. **Deviations have known impact** (security, compliance, performance)
4. **Remediation has operational context** (different fix paths by component type)

Potential domains: cloud infrastructure compliance (CIS benchmarks), database configuration audit, network device hardening, application security posture.

---

## Sources

### Tier A (Direct Production Observation)

- health-inventory deviation engine (April 2026) — `lib/config_assessment/` (adapter.py 345 lines, engine.py 425 lines, remediation.py 283 lines)
- YAML baseline specification (April 2026) — `config/ndr-config-best-practices-baseline.yaml` (5 dimensions, 30+ checks)
- Fleet-scale validation (April 2026) — 3,816+ sensors, zero processing errors
- third-brain H-CONFIG-01 hypothesis (April 2026) — Confidence 4.7/5, all milestones complete

### Tier B (Validated / Expert Practitioner)

- Hoosier Energy MNDR review findings — Ground truth dataset for validation (12 known issues)
- MITRE ATT&CK framework — Technique mapping for attack impact assessment

### Related Analysis

- [Local+Cloud LLM Orchestration](./local-cloud-llm-orchestration.md) — Same local MLX inference pattern used for LLM remediation path
- [Agent-Driven Development](./agent-driven-development.md) — health-inventory as Level 2 (Standard Infrastructure) example
- [Harness Engineering](./harness-engineering.md) — Diagnostic framework applied to config assessment development

---

*Last updated: April 2026*

---
version-requirements:
  claude-code: "v2.1.0+"
version-last-verified: "2026-04-06"
measurement-claims:
  - claim: "15/15 federation benchmark queries pass, all under 10 seconds (cross-site JOIN avg 9.3s)"
    source: "Direct analysis — zeek-iceberg-demo d2_benchmark_suite.py + third-brain M2 results"
    date: "2026-04-06"
    revalidate: "2026-10-06"
  - claim: "93-99.9% WAN bandwidth reduction across all federated query scenarios vs centralized"
    source: "Direct analysis — third-brain M3 bandwidth measurements"
    date: "2026-04-06"
    revalidate: "2026-10-06"
  - claim: "86-99% annual cost savings vs centralized SIEM across 3 enterprise scenarios"
    source: "Direct analysis — third-brain federated_query_tco.py calculator"
    date: "2026-04-06"
    revalidate: "2026-10-06"
  - claim: "20M OCSF v1.8 events across 2 distributed sites with 74 fields and 25 compliance checks passing"
    source: "Direct analysis — zeek-iceberg-demo + third-brain M1 milestone"
    date: "2026-04-06"
    revalidate: "2026-10-06"
status: PRODUCTION
last-verified: "2026-04-06"
evidence-tier: A
applies-to-signals: [project-type-data-pipeline]
revalidate-by: 2026-10-06
---

# Federated Query Architecture: Claude Code as Design and Benchmarking Tool

**Evidence Tier**: A — Direct production observation across zeek-iceberg-demo (implementation) and third-brain (hypothesis validation, TCO analysis)

## Purpose

This document analyzes how **Claude Code was used to design, implement, benchmark, and validate** a federated query architecture for security data — Zeek network logs transformed to OCSF, stored in Parquet/Iceberg, queried across distributed sites via Dremio/Trino/ClickHouse. The focus is on the **development methodology** (how agent-driven development produced a validated architecture with quantified results), not the architecture itself.

This is a case study in using Claude Code for complex systems engineering: hypothesis formulation, multi-milestone validation, competitive analysis, and business case construction.

---

## Architecture Summary

```
Edge Site 1 (HQ)              Edge Site 2 (Branch)
┌──────────────────┐          ┌──────────────────┐
│ Zeek Logs        │          │ Zeek Logs        │
│ → OCSF Transform │          │ → OCSF Transform │
│ → Parquet/Iceberg│          │ → Parquet/Iceberg│
│ → MinIO (S3)     │          │ → MinIO-edge2    │
│ → DuckDB (local) │          │ → DuckDB (local) │
└────────┬─────────┘          └────────┬─────────┘
         │                             │
         └──────────┬──────────────────┘
                    │ Federated queries only
                    │ (no raw data movement)
              ┌─────┴─────┐
              │  Central   │
              │  Dremio    │ Federated SQL
              │  Trino     │ Cross-site JOINs
              │  ClickHouse│ Hot tier (0.15s)
              └────────────┘
```

**Stack**: Zeek JSON → Python OCSF transformer (30K records/sec) → Parquet (Snappy, 75% compression) → MinIO → Iceberg catalog (Hive Metastore) → Dremio/Trino/ClickHouse

---

## Development Methodology: Hypothesis-Driven with Milestones

The architecture was developed using an explicit hypothesis validation framework tracked in third-brain:

**Hypothesis H-NDR-FEDERATION-01**: "Federated Search Architecture Determines NDR Platform Stickiness"

- **Confidence**: 4.6/5 (after all milestones passed)
- **Evidence Level**: A (systematic review + 12-service federation POC with production-scale benchmarks)

### Four Validation Milestones

| Milestone | Target | Result | Date |
|-----------|--------|--------|------|
| M1: OCSF Pipeline | 20M events, OCSF v1.8, cross-site JOINs | 20M events, 74 fields, 25 compliance checks | 2026-04-04 |
| M2: Federation Benchmark | 15/15 queries < 10s | All pass. Single-edge 4.6s, UNION 7.3s, JOIN 9.3s | 2026-04-04 |
| M3: WAN Bandwidth Reduction | >90% reduction | 93-99.9% across all scenarios | 2026-04-04 |
| M4: Competitive Parity | Path to match/exceed ExtraHop | 3.5-6.5 eng-weeks to minimum viable | 2026-04-04 |

**How Claude Code contributed**: Each milestone was an agent-driven development cycle — explore existing codebase → plan benchmark approach → execute implementation → validate results. The 15-query benchmark suite, OCSF transformer, multi-site data generator, and TCO calculator were all agent-co-authored.

---

## Benchmark Results: 15-Query Federation Suite

### Query Categories and Performance

| Category | Queries | Avg Latency | What They Test |
|----------|---------|------------|----------------|
| Single-edge (Q01-Q07) | 7 | 4.6s | Baseline: row counts, distributions, top talkers, lateral movement |
| Cross-site UNION (Q08-Q10) | 3 | 7.3s | UNION ALL across both edges: combined counts, distributions, top talkers |
| Cross-site JOIN (Q11-Q13) | 3 | 9.3s | JOINs: IPs on both edges, denied IPs on both, common destinations |
| Partition pruning (Q14-Q15) | 2 | 1.3s | Date range scan + point partition filter |

### Cross-Engine Comparison (10M events, identical dataset)

| Engine | Format | Avg Latency | vs Splunk |
|--------|--------|------------|-----------|
| ClickHouse | Native MergeTree | 0.19s | 145x faster |
| Dremio | Iceberg | 1.00s | 28x faster |
| StarRocks | Iceberg | 1.50s | 18x faster |
| Trino | Iceberg | 2.67s | 10x faster |
| Splunk | SPL | 27.52s | Baseline |

**Source**: Splunk DB Connect Benchmark — same 10M-event dataset across all engines.

---

## WAN Bandwidth Reduction (M3)

### Raw Dataset

- Edge-1: 10M rows, 874.4 MB Parquet
- Edge-2: 10M rows, 874.6 MB Parquet
- Total: 20M rows, 1,748.9 MB

### Federated vs Centralized Transfer

| Scenario | Centralized | Federated | Reduction |
|----------|------------|-----------|-----------|
| Single-edge GROUP BY (1 col) | 1,748.9 MB | 76.8 MB | **95.6%** |
| Cross-edge JOIN (1 col, both edges) | 1,748.9 MB | 120.7 MB | **93.1%** |
| Partition-pruned (1 day, 2 cols) | 1,748.9 MB | 1.7 MB | **99.9%** |
| Time-filtered analytical (3 days, 5 cols) | 1,748.9 MB | 12.2 MB | **99.3%** |

**Key finding**: Column pruning alone (Parquet columnar reads) reduces physical I/O by 91% per edge. Partition pruning adds another order of magnitude for time-bounded queries.

---

## TCO Analysis: 86-99% Cost Savings

### Validated Cost Constants

| Constant | Value | Source |
|----------|-------|--------|
| Splunk ingestion | $150/GB/month | Industry standard |
| AWS S3 Standard | $23/TB/month | us-east-1 pricing |
| Parquet compression | 4x | Validated in POC |
| ZSTD compression | 8.2x | ClickHouse validated |
| Column I/O reduction | 91% | M3 measurement |

### Annual Cost Comparison

| Scenario | Daily Volume | Sites | Centralized SIEM | Federated Lakehouse | Savings |
|----------|-------------|-------|-----------------|-------------------|---------|
| Small Enterprise | 10 GB/day | 5 | $541.6K | $76.2K | **85.9%** |
| Mid-Size Enterprise | 100 GB/day | 20 | $5.47M | $229.7K | **95.8%** |
| Large Enterprise | 1 TB/day | 100 | $57.28M | $822.8K | **98.6%** |

### Cost Breakdown Example (Mid-Size Enterprise)

**Centralized SIEM**: Ingestion/License $5.40M + WAN bandwidth $65.7K = **$5.47M/year**

**Federated Lakehouse**: Storage $3.3K + Compute $22.8K + Edge infra $48K + Catalog $3.6K + WAN $2K + Operations $150K = **$229.7K/year**

**Primary cost driver eliminated**: The $150/GB/month ingestion tax. Open table formats (Iceberg) have no per-GB licensing.

---

## Agent-Driven Development Patterns in This Project

### Infrastructure Progression

zeek-iceberg-demo demonstrates the Level 1→2 maturity progression from [Agent-Driven Development](./agent-driven-development.md):

- **Phase 1**: Basic CLAUDE.md + manual demo workflow
- **Phase 2**: Added `.claude/` infrastructure — SessionStart hook, 4 slash commands (`/demo`, `/status`, `/setup-minio`, `/reflections`), settings.json permissions
- **Phase 3**: Full SDD artifacts — ARCHITECTURE.md (12 ADRs), PROJECT-STATUS-CURRENT.md, audit report

### Commit Pattern Evidence

The git history shows characteristic agent-driven development:

- Infrastructure commits: `🏗️ Add Claude Code infrastructure and SDD artifacts`
- Feature branches: `flying-coyote/claude/audit-best-practices-nWE7b`
- Phase markers: `📁 Organize documentation into docs/ structure - Phase 2`
- Benchmark commits: `Add multi-site federation data generator and cross-site query demo`

### Cross-Repo Coordination

The architecture spans two repos:

- **zeek-iceberg-demo**: Implementation (Docker Compose, transformers, benchmarks, demo scripts)
- **third-brain**: Strategy (hypothesis tracking, TCO calculator, business case, competitive analysis)

This hub-spoke pattern (documented in [Agent-Driven Development](./agent-driven-development.md)) enables the implementation repo to stay focused on code while the knowledge hub maintains strategic context.

---

## Diagnostic: When This Architecture Applies

```
Is your data distributed across multiple sites?
├── No → Single-site query engine (ClickHouse/DuckDB) is sufficient
└── Yes → Can all raw data be centralized?
    ├── Yes, no constraints → Centralized SIEM (simpler, higher cost)
    └── No (cost, bandwidth, sovereignty) → Federated architecture
        ├── Query latency < 10s acceptable? → Iceberg + Dremio/Trino
        ├── Sub-second needed? → ClickHouse hot tier + materialized views
        └── Both? → Hybrid: Iceberg for warm, ClickHouse for hot
```

---

## Sources

### Tier A (Direct Production Observation)

- zeek-iceberg-demo implementation (April 2026) — Docker Compose federation overlay, 15-query benchmark suite, OCSF transformers, multi-site data generator
- third-brain hypothesis validation (April 2026) — H-NDR-FEDERATION-01 evidence document, M1-M4 milestones, TCO calculator (`automation/federated_query_tco.py`, 460 lines)
- Splunk DB Connect Benchmark (April 2026) — Cross-engine performance comparison on identical 10M-event dataset

### Tier B (Validated / Expert Practitioner)

- OCSF v1.8 specification — 25 event classes mapped for Corelight Zeek log types
- Apache Iceberg table format — Open table format enabling federated catalog queries

### Related Analysis

- [Agent-Driven Development](./agent-driven-development.md) — Development methodology used to build and validate this architecture
- [Harness Engineering](./harness-engineering.md) — Infrastructure maturity progression observed in zeek-iceberg-demo

---

*Last updated: April 2026*

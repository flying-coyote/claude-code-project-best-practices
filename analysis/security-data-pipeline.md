---
version-requirements:
  claude-code: "v2.1.0+"
version-last-verified: "2026-04-06"
measurement-claims:
  - claim: "Zeek → OCSF transformation at 30,000 records/second with 74 OCSF-compliant fields per record"
    source: "Direct analysis — zeek-iceberg-demo transform scripts + ARCHITECTURE.md"
    date: "2026-04-06"
    revalidate: "2026-10-06"
  - claim: "75% compression ratio with Snappy-compressed Parquet (1M records = 89.6MB)"
    source: "Direct analysis — zeek-iceberg-demo ARCHITECTURE.md"
    date: "2026-04-06"
    revalidate: "2026-10-06"
  - claim: "3 OCSF event classes implemented: Network Activity (4001), HTTP Activity (4002), DNS Activity (4003)"
    source: "Direct analysis — zeek-iceberg-demo transformation scripts"
    date: "2026-04-06"
    revalidate: "2026-10-06"
status: PRODUCTION
last-verified: "2026-04-06"
evidence-tier: A
applies-to-signals: [project-type-data-pipeline]
revalidate-by: 2026-10-06
---

# Security Data Pipeline: Zeek to Lakehouse as a Claude Code Case Study

**Evidence Tier**: A — Direct production analysis of zeek-iceberg-demo implementation

## Purpose

This document analyzes the **Zeek → OCSF → Parquet → Iceberg → Query Engine** pipeline as a case study in using Claude Code for security data engineering. The focus is on the development patterns — how agent-driven development produced a validated data pipeline with standard-compliant transformations, Docker-based infrastructure, and benchmark-validated query performance.

For the federated query results built on top of this pipeline, see [Federated Query Architecture](./federated-query-architecture.md).

---

## Pipeline Architecture

```
Zeek Sensor              Transformation           Storage              Query
┌──────────┐    ┌─────────────────────┐    ┌──────────────┐    ┌──────────────┐
│ conn.log │───▶│ transform_zeek_to_  │───▶│ Parquet      │───▶│ Dremio       │
│ dns.log  │    │ ocsf_flat.py        │    │ (Snappy)     │    │ Trino        │
│ http.log │    │                     │    │              │    │ ClickHouse   │
│          │    │ OCSF v1.8 mapping   │    │ MinIO (S3)   │    │ DuckDB       │
│          │    │ 74 fields/record    │    │              │    │              │
│          │    │ 30K records/sec     │    │ Iceberg      │    │ Spark        │
└──────────┘    └─────────────────────┘    │ catalog      │    └──────────────┘
                                            └──────────────┘
```

## Transformation Layer

### Three OCSF Event Classes

| Zeek Log | OCSF Class | Script | Fields |
|----------|-----------|--------|--------|
| conn.log | 4001 (Network Activity) | `transform_zeek_to_ocsf_flat.py` | 74 |
| dns.log | 4003 (DNS Activity) | `transform_zeek_dns_to_ocsf.py` | Class-specific |
| http.log | 4002 (HTTP Activity) | `transform_zeek_http_to_ocsf.py` | Class-specific |

### Key Design Decision: Flat OCSF Schema

OCSF defines nested objects (`src_endpoint.ip`, `dst_endpoint.ip`). The pipeline uses flat column names (`src_endpoint_ip`, `dst_endpoint_ip`) for:

- **Query simplicity**: `WHERE src_endpoint_ip = '10.0.0.1'` vs nested object access
- **Engine compatibility**: All query engines handle flat columns; nested struct support varies
- **Parquet performance**: Flat columns enable better columnar compression and predicate pushdown

This is documented as ADR-005 in the project's DECISIONS.md.

### Compliance Validation

Each transformation includes inline validation:

```python
compliance = validate_ocsf_compliance(df)
# 25 compliance checks per event class
# Validates: required fields, data types, enum values, timestamp formats
```

The validation runs as part of the pipeline, not as a separate step. Failed compliance aborts the transformation rather than producing non-compliant Parquet files.

---

## Infrastructure Layer (Docker Compose)

### 7-Service Stack

| Service | Purpose | Port |
|---------|---------|------|
| MinIO | S3-compatible object storage | 9000 (S3), 9001 (console) |
| PostgreSQL | Hive Metastore backend | 5432 |
| Hive Metastore | Iceberg catalog | 9083 |
| Spark | Processing engine | 8080, 10000 |
| Dremio | Query acceleration (reflections) | 9047 (UI), 31010 (JDBC) |
| Jupyter | Interactive notebooks | 8888 |
| minio-init | Bucket creation (one-shot) | — |

### Federation Overlay

A separate `docker-compose.federation.yml` adds multi-site infrastructure:

- **Edge Site 2**: MinIO-edge2 (port 9010) + DuckDB edge compute
- **Central hot tier**: ClickHouse (port 8123) for sub-second aggregations
- **Trino**: Cross-site federation engine

---

## Storage Layer: Parquet + Iceberg

### Why Parquet

- **Columnar**: Query engines read only needed columns (91% I/O reduction measured)
- **Compression**: Snappy at 75% ratio (1M records = 89.6MB)
- **Ecosystem**: Every query engine supports Parquet natively
- **Predicate pushdown**: Filters applied at storage level, not after full scan

### Why Iceberg

- **Table format**: Schema evolution, time travel, partition evolution without rewriting data
- **Catalog**: Hive Metastore provides unified table registry across engines
- **Federation**: Multiple engines (Dremio, Trino, Spark, DuckDB) access the same tables
- **Open**: No vendor lock-in; any engine that speaks Iceberg can query the data

### Partitioning Strategy

Data partitioned by `year/month/day` — enabling partition pruning for time-bounded queries. The benchmark results show partition-pruned queries at 1.3s average vs 4.6s for full table scans.

---

## Agent-Driven Development in This Pipeline

### Slash Commands as Operational Interface

The project uses 4 custom commands that demonstrate how Claude Code operates complex infrastructure:

| Command | Purpose | What It Does |
|---------|---------|-------------|
| `/demo` | Run 20-minute demo | Pre-demo checklist, 5-section walkthrough, teardown |
| `/status` | Check environment health | Docker services, MinIO data, git status, env vars |
| `/setup-minio` | Configure object storage | Bucket creation, IAM setup, Iceberg warehouse init |
| `/reflections` | Configure Dremio reflections | Materialized view setup for query acceleration |

### Development Progression

The git history shows phased development:

1. **Phase 1**: Basic pipeline — Zeek JSON → OCSF → Parquet → MinIO
2. **Phase 2**: Federation overlay — Multi-site, DuckDB edge, ClickHouse hot tier, Trino
3. **Phase 3**: Claude Code infrastructure — Hooks, commands, SDD artifacts, audit report

This matches the infrastructure maturity model in [Agent-Driven Development](./agent-driven-development.md): the pipeline was built first, then the agent infrastructure was added to make it operational.

### Multi-Site Data Generation

The `generate_federation_data.py` script demonstrates agent-driven data engineering — generating realistic multi-site network traffic with distinct profiles:

- **Edge 1 (HQ)**: 50 hosts, 60% external traffic, diverse services (HTTP, DNS, SSL, SSH, SMTP)
- **Edge 2 (Branch)**: 15 hosts, 80% external traffic, limited services (web + DNS + SSL)

These profiles create realistic federation scenarios where cross-site JOINs find shared IPs, merged traffic patterns, and site-specific anomalies.

---

## Applicability

This pipeline pattern applies to any security data engineering task where:

1. **Raw security logs** need standardization (OCSF, ECS, CIM)
2. **Cost reduction** requires moving from ingestion-priced SIEM to open storage
3. **Multi-engine query** is needed (investigation + analytics + reporting on same data)
4. **Distributed deployment** requires federation rather than centralization

The key reusable components: OCSF transformer pattern, Parquet + Iceberg storage, Docker Compose infrastructure, benchmark validation suite.

---

## Sources

### Tier A (Direct Production Observation)

- zeek-iceberg-demo pipeline analysis (April 2026) — 3 OCSF transformers, Docker Compose 7-service stack, federation overlay, 15-query benchmark suite
- ARCHITECTURE.md (April 2026) — 12 ADRs including flat OCSF schema decision
- OCSF compliance validation (April 2026) — 25 checks per event class, inline validation

### Tier B (Validated / Expert Practitioner)

- OCSF v1.8 specification — Event class definitions and field requirements
- Apache Iceberg documentation — Table format capabilities and federation patterns

### Related Analysis

- [Federated Query Architecture](./federated-query-architecture.md) — Query performance and TCO analysis built on this pipeline
- [Agent-Driven Development](./agent-driven-development.md) — Development methodology used for this pipeline

---

*Last updated: April 2026*

---
version-requirements:
  claude-code: "v2.1.0+"
version-last-verified: "2026-04-06"
measurement-claims:
  - claim: "1,216 tests across 57 suites validating hybrid local+cloud LLM pipeline with zero PII leakage"
    source: "Direct analysis — mndr-review-automation test suite"
    date: "2026-04-06"
    revalidate: "2026-10-06"
  - claim: "10 entity types tokenized with deterministic SHA-256 hashing before any cloud transmission"
    source: "Direct analysis — mndr-review-automation lib/tokenizer.py"
    date: "2026-04-06"
    revalidate: "2026-10-06"
  - claim: "7 hallucination scrubbers applied in sequence to every local LLM output before assembly"
    source: "Direct analysis — mndr-review-automation lib/llm_pipeline.py"
    date: "2026-04-06"
    revalidate: "2026-10-06"
  - claim: "Supply chain attack surface eliminated by rejecting litellm, openai, anthropic, langchain packages"
    source: "Direct analysis — mndr-review-automation lib conventions + scripts/verify_deps.py"
    date: "2026-04-06"
    revalidate: "2026-10-06"
status: PRODUCTION
last-verified: "2026-04-06"
evidence-tier: A
applies-to-signals: [project-type-hybrid-llm]
revalidate-by: 2026-10-06
---

# Local+Cloud LLM Orchestration: Hybrid Architecture for Sensitive Data

**Evidence Tier**: A — Direct production analysis of mndr-review-automation pipeline

## Purpose

This document analyzes the **hybrid local+cloud LLM architecture** used in mndr-review-automation — a production pipeline that processes customer security data through a local LLM (MLX/Gemma on Apple Silicon) while using a cloud LLM (Claude) for coaching and quality review. The key insight: the boundary between local and cloud is not a technical limitation — it's a **data classification decision** enforced through tokenization, hooks, and architectural separation.

This pattern is reusable beyond NDR: any domain where sensitive data must be analyzed by LLMs but cannot leave the local environment.

---

## Architecture Overview

```
Customer Data (PII: IPs, hostnames, domains)
    │
    ▼
┌─────────────────────────────────────────┐
│  LOCAL MACHINE (Apple Silicon + MLX)     │
│                                          │
│  ingest → tables → queries → findings    │
│  → enrich → llm (Gemma 4 31B)           │
│       │                                  │
│       ├─ classify_finding()              │
│       ├─ classify_severity()             │
│       ├─ assess_root_cause()             │
│       └─ synthesize_finding()            │
│                                          │
│  7 hallucination scrubbers               │
│  12 universal + 6 category validators    │
│                                          │
│  Tokenizer: 10 entity types → tokens     │
│       │                                  │
└───────┼──────────────────────────────────┘
        │ tokenized content only
        ▼
┌─────────────────────────────────────────┐
│  CLOUD (Claude Sonnet via CLI/API)       │
│                                          │
│  cloud-coach: coaching for escalated     │
│               findings                   │
│  revise: iterative quality review loop   │
│       │                                  │
└───────┼──────────────────────────────────┘
        │ coaching feedback (no PII)
        ▼
┌─────────────────────────────────────────┐
│  LOCAL MACHINE (retry with coaching)     │
│                                          │
│  llm-retry → assemble → export           │
│                                          │
│  Token map stays local (never shared)    │
│  Final output: detokenized for customer  │
└─────────────────────────────────────────┘
```

---

## The Tokenization Boundary

The critical architectural decision: **where does local processing stop and cloud processing start?** The answer is the tokenizer.

### 10 Entity Types Tokenized

| Entity | Token Format | Example |
|--------|-------------|---------|
| IPv4 | `IP-{sha256[:8]}` | `IP-a1b2c3d4` |
| IPv6 | `IPV6-{sha256[:8]}` | `IPV6-e5f6a7b8` |
| MAC address | `MAC-{sha256[:8]}` | `MAC-c9d0e1f2` |
| Hostname | `HOST-{sha256[:8]}` | `HOST-3a4b5c6d` |
| Domain | `DOMAIN-{sha256[:8]}` | `DOMAIN-7e8f9a0b` |
| UID/Serial | `UID-{sha256[:8]}` | `UID-1c2d3e4f` |
| CIDR | `CIDR-{sha256[:8]}` | `CIDR-5a6b7c8d` |
| Email | `EMAIL-{sha256[:8]}` | `EMAIL-9e0f1a2b` |
| Service account | `ACCT-{sha256[:8]}` | `ACCT-3c4d5e6f` |
| Customer name | `CUSTOMER-{sha256[:8]}` | `CUSTOMER-7a8b9c0d` |

**Design properties**:

- **Deterministic**: Same input always produces the same token (SHA-256 based), so cross-references within the document remain consistent
- **Not reversible**: Cannot recover the original value from the token alone
- **Collision-handled**: Hash extended to 12 chars if collision detected
- **Auditable**: `Tokenizer.audit(text)` scans for remaining leaks and returns `(pattern_type, match, line_number)` tuples

### Pre-Cloud Validation Gate

Every cloud transmission passes through `validate_pre_cloud()`:

```python
def validate_pre_cloud(text, known_hostnames, known_domains, customer_name) -> List:
    # Returns empty list if clean, else list of (type, value, line) leaks
    # Pipeline ABORTS if any leaks detected
```

This function is called before `step_cloud_coach()` and `step_cloud_review()`. It is not advisory — a non-empty return aborts the pipeline. Combined with the PreToolUse hook (which blocks Claude Code from reading raw customer data), this creates **three independent layers** preventing PII leakage:

| Layer | Mechanism | Failure Mode It Prevents |
|-------|-----------|-------------------------|
| Instruction | CLAUDE.md "Security Boundaries" section | Agent reads raw data by accident (~80% reliable) |
| Hook enforcement | PreToolUse blocks `data/staging/`, `token_map.json`, `.env` | Agent reads raw data despite instructions (~100% reliable) |
| Tokenization gate | `validate_pre_cloud()` aborts pipeline if PII detected | Tokenizer miss or novel entity pattern (~100% reliable) |

---

## Local LLM: MLX In-Process

### Runtime Architecture

- **Model**: `mlx-community/gemma-4-31b-it-5bit` (configurable via `MLX_MODEL` env)
- **Runtime**: MLX on Apple Silicon unified memory — no network calls, no API server, fully in-process
- **Fallback**: Tries `mlx_vlm` first (VLM architectures), falls back to `mlx_lm`

### Model Alternatives: Gemma 4 26B MoE (April 2026)

Google's Gemma 4 family (released April 2, 2026) includes a 26B Mixture of Experts model with properties relevant to local inference:

| Property | Gemma 4 31B (current) | Gemma 4 26B MoE |
|----------|----------------------|------------------|
| Total parameters | 30.7B (dense) | 26B (MoE) |
| Active parameters | 30.7B | 3.8B per token |
| Context window | 256K | 256K |
| Function calling | Prompt-injected | Native (built-in) |
| Inference speed | Baseline | Potentially faster (fewer active params) |
| Agentic benchmark (tau2) | — | 86.4% |

**Native function calling** is the key differentiator — the 26B MoE model supports tool use natively rather than through prompt templates. For pipelines with many structured LLM calls (like the ~200 per MNDR review), this could improve both accuracy and latency.

**Decision pending**: Benchmarking 26B MoE vs 31B dense on domain-specific tasks is required before switching production pipelines. Available via Ollama: `ollama run gemma4:26b`.

### Ollama v0.19 MLX Backend (March 2026)

Ollama v0.19 (released March 27, 2026) introduced native Apple MLX framework integration. The original decision to use direct MLX-LM over Ollama was driven by eliminating HTTP overhead and network listeners. With Ollama now using MLX natively on Apple Silicon, the gap has narrowed:

| Factor | Direct MLX-LM (current) | Ollama v0.19 + MLX |
|--------|------------------------|---------------------|
| Inference engine | MLX (in-process) | MLX (via Ollama) |
| Network calls | None | Localhost HTTP (minimal overhead) |
| Model management | Manual (`mlx-lm` downloads) | `ollama pull` (managed) |
| Multi-model switching | Code change required | Config/runtime switch |
| Security surface | `mlx-lm` package only | `ollama` binary + HTTP listener |

**Assessment**: For single-model pipelines with security constraints (like MNDR), direct MLX remains simpler. For development workflows needing quick model switching, Ollama v0.19 is now a viable alternative. Benchmarking is needed to quantify the actual latency difference.

### Four Core Functions

| Function | Purpose | Temperature | Max Tokens |
|----------|---------|------------|------------|
| `classify_finding(title, evidence)` | Categorize into 7 known types + unknown | 0.1 | 256 |
| `classify_severity(finding_context)` | HIGH/MEDIUM/LOW with justification | 0.1 | 256 |
| `assess_root_cause(anomaly_context)` | 2-3 paragraph root cause analysis | 0.3 | 2048 |
| `synthesize_finding(data_points)` | Narrative from correlated data points | 0.3 | 2048 |

**Design principle**: Classification tasks use low temperature (0.1) for deterministic output. Generation tasks use moderate temperature (0.3) for natural prose. Neither uses high temperature — hallucination risk outweighs creativity benefit in security reporting.

### Heuristic Fast Path

Before invoking the LLM, `_classify_category_heuristic()` attempts keyword-based classification. If a finding's title contains "sensor health" or "export lag", it's classified without LLM inference. This reduces latency for common categories and reserves LLM capacity for ambiguous cases.

---

## Cloud LLM: Claude for Coaching and Review

### Two Cloud Interaction Patterns

**1. Escalation Coaching (`step_cloud_coach`)**

Escalation triggers — any ONE condition sends a finding to cloud review:

- **Novel category**: Not one of 7 known types (the local LLM flagged uncertainty)
- **Validation failure**: Output quality checks failed (too short, generic filler, hallucinated data)
- **Multi-source correlation**: Evidence from multiple detection layers (Notice + Suricata)
- **HIGH severity**: All critical findings get coaching review regardless of quality

The cloud receives `escalation_requests.md` (tokenized) containing:

- Escalation reasons
- Evidence table (tokenized)
- The local LLM's failed attempt
- Auto-generated coaching question (contextual to failure mode)

The cloud returns `coaching.md` — structured coaching per finding that the local LLM uses on retry.

**2. Iterative Revision Loop (`step_revise`, max 3 iterations)**

```
tokenized_draft.md → Cloud review → PASS/WARN/FAIL per section
    → Parse actionable feedback
    → Local LLM rewrites WARN/FAIL sections with feedback context
    → Re-tokenize → Re-submit
    → Repeat until "Ready" or max iterations
```

### Cloud API Pattern

```python
# Primary: claude CLI (inherits Claude Code auth)
# Fallback: ANTHROPIC_API_KEY via anthropic SDK
# Model: claude-sonnet-4-6 (hardcoded)
# Timeout: 600 seconds
```

The CLI-first approach means no separate API key management for the primary path — the pipeline inherits Claude Code's authentication context.

---

## Output Quality: 7 Scrubbers + 18 Validators

### Hallucination Scrubbing Pipeline

Every local LLM output passes through 7 scrubbers in sequence before assembly:

| Scrubber | What It Removes | Why |
|----------|----------------|-----|
| `scrub_hallucinated_ips(text, evidence)` | IPs not present in evidence table | LLMs fabricate plausible-looking IPs |
| `scrub_hallucinated_code(text)` | Zeek scripts, iptables rules, ACL patterns | LLMs generate "helpful" code that doesn't exist |
| `scrub_hallucinated_macs(text, evidence)` | MAC addresses not in evidence | Same fabrication pattern as IPs |
| `scrub_hallucinated_hostnames(text, evidence)` | Internal hostnames not in evidence | Fabricated hostnames could mislead investigation |
| `scrub_hallucinated_ipv6(text, evidence)` | IPv6 addresses not in evidence | Less common but same risk |
| `scrub_hallucinated_emails(text, evidence)` | Email addresses not in evidence | Could implicate wrong individuals |
| `scrub_hallucinated_cves(text, evidence)` | CVEs not in evidence or known list | Fabricated CVEs waste investigation time |

Plus two post-scrubbers: `scrub_coaching_leak(text)` removes echoed coaching instructions, and `fix_scrubber_artifacts(text)` cleans mid-word truncation from replacements.

### Validation Dimensions (5 scores)

```
completeness   = length + evidence_reference + no_placeholders
accuracy       = no_hallucinated_ips + no_code + no_fabricated_certs
actionability  = category_specific_checks + no_generic_filler
evidence_citation = evidence_reference + not_evidence_echo
clarity        = complete_sentences + english + no_internal_markers
overall        = mean of 5 dimensions
```

**Pass threshold**: `score >= 0.6` AND no hard-fail conditions (fabricated IP/code/cert, empty output, internal markers).

**12 universal checks** apply to all findings. **6 category-specific checks** add domain requirements (e.g., compliance findings must cite RFC/CVE/standard; OT/ICS findings must reference industrial protocol).

---

## Supply Chain Security Decision

### Why litellm Was Rejected

The pipeline explicitly forbids litellm, openai, anthropic, langchain, and llama-index packages. This is enforced at multiple levels:

- **CLAUDE.md rule**: "No LLM proxy libraries — MLX in-process only"
- **Rules file** (`lib-conventions.md`): "No litellm, openai, anthropic, langchain, or llama-index packages allowed (supply chain risk)"
- **Runtime check**: `scripts/verify_deps.py` scans installed packages against a forbidden list

**Rationale**: LLM proxy libraries are high-value supply chain targets. The litellm v1.82.8 compromise (March 2026) validated this decision — a single dependency compromise could exfiltrate customer data through the proxy layer. By using MLX directly (in-process, no network) and the Claude CLI (inherits OS-level auth), the attack surface is minimized to the runtime itself.

**Trade-off accepted**: No multi-model abstraction. Switching models requires code changes to `local_llm.py` rather than config changes. This is acceptable because model switching is infrequent and the security benefit outweighs the convenience cost.

---

## Context Injection Strategy

Each finding generation receives layered context, injected in priority order:

| Layer | Source | Purpose |
|-------|--------|---------|
| 1. Preamble | `config/llm_prompts.yaml` | Anti-hallucination constraints (universal) |
| 2. Category prompt | `config/llm_prompts.yaml` | Detection-specific guidance (per finding type) |
| 3. PS Knowledge | `config/ps_knowledge.yaml` | Cross-customer best practices |
| 4. Customer Context | Work order metadata | Industry, OT environment, authorized tools |
| 5. Enrichment | Inspector MCP + Investigator API | Entity profiles, alert context |
| 6. Trend Context | `review_history.json` | Historical finding recurrence |
| 7. Review Feedback | Previous review notes | Customer-specific priorities |
| 8. Playbook Context | Matched investigation playbooks | Domain investigation steps |

For coaching retries, coaching context is appended: `"COACHING FROM SENIOR ANALYST:\n" + coaching`

---

## Coaching Quality Measurement

The `CoachingScorer` tracks whether cloud coaching actually improves local LLM output:

```python
class CoachingScorer:
    def score_revision(finding_id, title, category, escalation_reasons,
                       old_analysis, new_analysis, evidence, coaching_passed)
        -> FindingRevision
```

Each revision computes per-dimension deltas (completeness, accuracy, actionability, evidence citation, clarity) before vs. after coaching. Results are saved to `coaching_quality_metrics.json` with effectiveness breakdowns by escalation reason and finding category.

**Diagnostic**: If coaching effectiveness drops for a specific category, it indicates either the coaching prompts need updating or the local LLM's baseline has improved enough that coaching adds noise rather than signal.

---

## Anti-Patterns

| Anti-Pattern | Symptom | Fix |
|-------------|---------|-----|
| Cloud-first for all inference | PII in cloud API calls; compliance violation | Local-first; cloud only for tokenized content |
| LLM proxy library as abstraction | Supply chain vulnerability; data exfiltration risk | Direct runtime integration (MLX in-process, CLI for cloud) |
| Tokenization as afterthought | PII leaks discovered in production | Tokenization as architectural boundary with pre-cloud validation gate |
| Single validation layer | Hallucinated data in customer reports | 7 scrubbers + 18 validators + pre-cloud gate (defense in depth) |
| No coaching quality tracking | Degrading revision loop effectiveness | CoachingScorer with per-dimension delta tracking |
| Same temperature for all tasks | Classification inconsistency OR generation blandness | 0.1 for classification, 0.3 for generation |

---

## Applicability Beyond NDR

This architecture applies wherever:

1. **Sensitive data must be processed by LLM** but cannot leave the local environment
2. **Cloud LLM quality** is needed for specific tasks (review, coaching, complex reasoning)
3. **Tokenization** can preserve analytical value while stripping identifying information
4. **Supply chain risk** makes proxy libraries unacceptable

Examples: medical record summarization, legal document review, financial analysis with PII, HR assessment generation.

---

## Sources

### Tier A (Direct Production Observation)

- mndr-review-automation pipeline analysis (April 2026) — `lib/local_llm.py`, `lib/tokenizer.py`, `lib/llm_pipeline.py`, `lib/output_validator.py`, `scripts/run_review.py`, `config/llm_prompts.yaml`
- 1,216 tests across 57 suites validating the hybrid pipeline end-to-end
- PreToolUse hook enforcement (`/.claude/hooks/pre-tool-use.sh`, 72 lines)

### Tier B (Validated / Expert Practitioner)

- litellm v1.82.8 supply chain compromise (March 2026) — Validates rejection of proxy libraries
- Boris Cherny (March 2026) — ~80% CLAUDE.md adherence rate motivating hook-based enforcement

### Related Analysis

- [Agent-Driven Development](./agent-driven-development.md) — Infrastructure maturity model; mndr-review-automation as Level 3 (Full Harness) example
- [Safety & Sandboxing](./safety-and-sandboxing.md) — 4-layer security stack that this document extends with tokenization boundary
- [Harness Engineering](./harness-engineering.md) — Diagnostic framework for agent infrastructure
- [MCP Patterns](./mcp-patterns.md) — MCP failure modes relevant to the Inspector enrichment integration

---

*Last updated: April 2026*

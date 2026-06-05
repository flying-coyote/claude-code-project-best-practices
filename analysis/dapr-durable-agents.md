---
version-requirements:
  dapr: "1.13+"
  python: "3.9+"
version-last-verified: "2026-05-25"
measurement-claims:
  - claim: "Production-ready durable agent in approximately 10 lines of Python"
    source: "Bilgin Ibryam (Diagrid, Dapr contributor) — LinkedIn demonstration, January 2026"
    date: "2026-01"
    revalidate: "2026-11-01"
  - claim: "Dapr provides ~30 state backend options and 10+ LLM provider abstractions via Conversation API"
    source: "Dapr documentation (docs.dapr.io)"
    date: "2026-05"
    revalidate: "2026-11-01"
status: REFERENCE
last-verified: "2026-05-25"
evidence-tier: B
applies-to-signals: [project-type-agent-infra]
revalidate-by: 2026-11-25
source-provenance: imported from ~/security-data-commons-blog/drafted/AGENT-03-dapr-durable-agents.md (SDC archive, 2026-05-25); SDC framing stripped, repo-format frontmatter added.
---

# Production AI Agents in ~10 Lines: Dapr's Infrastructure-as-Runtime Approach

**Evidence Tier**: B (open source project, high-credibility author; CNCF graduated project with production deployments).
**Author Provenance**: Bilgin Ibryam (Diagrid, Dapr contributor) for the 10-LOC demonstration; Dapr/SPIFFE/CNCF documentation for capability claims.

## Overview

Building production AI agents typically requires solving infrastructure concerns *before* writing agent logic: durability, state persistence, secrets management, workload identity, observability, LLM abstraction, resilience. Dapr (Distributed Application Runtime) provides these as a sidecar runtime, letting agent code focus on prompt engineering and decision flows. This document captures the architectural pattern and trade-offs for harness engineers evaluating agent-infrastructure choices.

## The Agent Infrastructure Problem

Building production AI agents typically requires:

- **Durability**: What happens when the agent crashes mid-task?
- **State persistence**: Where does conversation history live?
- **Secrets management**: How do you safely inject API keys?
- **Identity**: How do agents authenticate to services?
- **Observability**: How do you trace agent decisions for audit?
- **LLM abstraction**: How do you swap providers without rewrites?
- **Resilience**: Retries, timeouts, circuit breakers?

Most teams build custom solutions for each concern. The result: weeks of infrastructure engineering before writing agent logic.

## Dapr's Insight: Infrastructure as Runtime

Dapr is a CNCF graduated project that provides distributed systems primitives as a sidecar runtime. The key insight from Bilgin Ibryam: agent infrastructure concerns aren't new — they're the same distributed systems problems Dapr already solves, applied to AI workloads.

### The ~10-Line Agent

Ibryam demonstrated a production-ready durable agent in roughly 10 lines of Python:

```python
from dapr_agents import Agent

agent = Agent(
    name="investigator",
    model="gpt-4",
    workflow="investigate"
)

agent.run()
```

This minimal code gains access to the entire Dapr runtime infrastructure.

## What You Get for Free

| Capability | What It Provides | Dapr Building Block |
|------------|------------------|---------------------|
| **HTTP endpoint** | `/run` endpoint for agent invocation | Service Invocation |
| **Event triggers** | Pub/Sub from 10+ message brokers | Pub/Sub |
| **Durable execution** | Fault-tolerant, resumable workflows | Workflows |
| **State persistence** | ~30 backend options (Redis, PostgreSQL, etc.) | State Management |
| **Service discovery** | Agent registry for multi-agent systems | Service Discovery |
| **LLM abstraction** | 10+ providers through unified API | Conversation API |
| **Workload identity** | SPIFFE-based cryptographic identity | SPIFFE/SPIRE |
| **Secrets** | 10+ backends (Vault, K8s secrets, etc.) | Secrets Management |
| **Resiliency** | Retries, timeouts, circuit breakers | Resiliency |
| **Observability** | OpenTelemetry traces, metrics, logs | Observability |

These are runtime features activated by configuration — not capabilities you implement.

## Architecture Pattern

```
┌─────────────────────────────────────────────────────────────────┐
│                    Dapr Runtime (Sidecar)                        │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐    │
│  │ Pub/Sub │ │  State  │ │ Secrets │ │Workflow │ │   LLM   │    │
│  │ (Kafka, │ │ (Redis, │ │ (Vault, │ │(Durable │ │(OpenAI, │    │
│  │  NATS)  │ │Postgres)│ │  K8s)   │ │Executor)│ │ Claude) │    │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘    │
├─────────────────────────────────────────────────────────────────┤
│                    SPIFFE Identity Layer                         │
├─────────────────────────────────────────────────────────────────┤
│                   Observability (OpenTelemetry)                  │
└─────────────────────────────────────────────────────────────────┘
                             │
                             ▼
              ┌─────────────────────────┐
              │   Agent Code (~10 LOC)  │
              │   - Business logic      │
              │   - Prompt templates    │
              └─────────────────────────┘
```

Infrastructure concerns are handled by the sidecar; agent code focuses on prompt engineering, decision flows, tool invocations.

## Durable Workflows in Practice

Long-running agent tasks can take hours. What happens when the agent crashes mid-execution?

- **Without Dapr**: Custom checkpointing logic, retry handling, state recovery code.
- **With Dapr**: Workflow building block provides automatic durability. Agent resumes from last checkpoint.

```python
@workflow
async def investigate(ctx, input):
    enriched = await ctx.call_activity(enrich_input, input)
    analyzed = await ctx.call_activity(analyze_with_llm, enriched)
    response = await ctx.call_activity(generate_response, analyzed)
    return response
```

If the agent crashes after `enrich_input`, it resumes from that point — not from the beginning.

## SPIFFE Identity for Workload Authentication

When an agent queries a database, fetches data from an external service, or calls APIs — how does it authenticate?

SPIFFE (Secure Production Identity Framework for Everyone) provides cryptographic workload identity. Each agent gets a verifiable identity without manual certificate management.

```
Agent → SPIFFE Identity → Service
   │                         │
   └── Cryptographically ────┘
       verified (mTLS)
```

No static API keys in code. Identity tied to workload, not configuration files.

## Comparison: Dapr vs Other Agent Frameworks

| Approach | Infrastructure Code | Operational Readiness | Flexibility |
|----------|---------------------|----------------------|-------------|
| **Custom Agent** | High (weeks) | Varies (depends on team) | High |
| **LangChain** | Medium (days) | Medium (some patterns included) | Medium |
| **AutoGen** | Medium (days) | Medium (multi-agent focused) | Medium |
| **CrewAI** | Medium (days) | Medium (workflow-oriented) | Medium |
| **Dapr Agents** | Minimal (hours) | High (production primitives) | High |

### When Dapr fits

- Already running Kubernetes
- Multiple agents need coordination
- Production requirements (durability, audit, identity) are non-negotiable
- Team has distributed systems experience

### When alternatives fit better

- Prototyping/exploration phase
- Single-agent scenarios
- No Kubernetes environment
- Simpler operational requirements

## Dapr vs MCP: Complementary

A common question: how does Dapr relate to Model Context Protocol (MCP)?

| Concern | Dapr | MCP |
|---------|------|-----|
| **Primary Focus** | Agent infrastructure (durability, identity, observability) | Tool/capability exposure to LLMs |
| **Identity** | SPIFFE built-in | Not addressed |
| **Durability** | Workflow building block | Not addressed |
| **Observability** | OpenTelemetry built-in | Not addressed |
| **Tool Integration** | Not primary focus | Primary focus |

These are complementary layers: Dapr provides agent infrastructure (the plumbing), MCP provides tool integration (capability exposure), Skills/Prompts provide domain knowledge. An agent can use Dapr for infrastructure (durability, identity, secrets) + MCP for tool access (databases, APIs, files) + custom prompts for domain expertise.

See [`mcp-vs-skills-economics.md`](mcp-vs-skills-economics.md) for the related cost/latency analysis on MCP vs. Skills as the tool-exposure mechanism.

## Security Considerations

**Strengths**:
1. SPIFFE Identity eliminates static credentials.
2. Vault/K8s secrets integration without custom code.
3. mTLS encrypted communication between sidecars by default.
4. Fine-grained access control via Dapr access policies.

**Considerations**:
1. Sidecar attack surface — another component to patch and monitor.
2. Agent-to-agent communication needs explicit policy.
3. LLM API keys still need secure injection (but Dapr makes it easier).
4. Understand what data traverses the sidecar.

## Getting Started

```bash
# Install Dapr
dapr init

# Create agent project
dapr new --template agent my-agent

# Run locally
dapr run --app-id my-agent -- python agent.py
```

### Resources

- Dapr documentation: https://docs.dapr.io/
- Dapr Agents: https://github.com/dapr/dapr-agents
- SPIFFE: https://spiffe.io/

## Takeaway

Durability, identity, secrets, observability — these are solved problems in distributed systems. Every time a team builds custom agent infrastructure, they re-solve problems Dapr (and similar runtimes) already solved.

The question isn't Dapr specifically — it's whether to treat agent infrastructure as a runtime concern rather than application code. Write agent logic; let the runtime handle infrastructure.

## Footnotes / Sources

- **Dapr (Distributed Application Runtime)**: CNCF graduated project (graduated 2024, first released 2019). https://docs.dapr.io/ — Evidence Tier A.
- **Bilgin Ibryam**: Principal Product Manager at Diagrid (Dapr commercial support), CNCF contributor, author of *Kubernetes Patterns*. "10 lines of code" demonstration shared via LinkedIn, January 2026. Evidence Tier B.
- **SPIFFE (Secure Production Identity Framework for Everyone)**: CNCF graduated project providing a standard for workload identity. https://spiffe.io/ — Evidence Tier A.

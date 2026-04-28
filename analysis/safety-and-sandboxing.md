---
evidence-tier: A
applies-to-signals: [harness-hooks, commit-security-paths]
last-verified: 2026-04-15
revalidate-by: 2026-10-15
status: PRODUCTION
---

# Safety and Sandboxing

**Sources**:
- [Beyond Permission Prompts: Making Claude Code More Secure](https://www.anthropic.com/engineering/beyond-permission-prompts) (Evidence Tier A)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) (Evidence Tier A)
- [Claude Code Security Documentation](https://code.claude.com/docs/en/security) (Evidence Tier A)

**Evidence Tier**: A (Primary vendor + industry standard)

**SDD Phase**: Cross-phase (security applies to all phases)

## The Core Problem

Permission prompts are the primary mechanism for controlling what Claude Code can do. But frequent prompts create friction, leading developers to either:
1. Over-approve (reducing security) or
2. Avoid using AI tools (reducing productivity)

Sandboxing resolves this tension by providing OS-level isolation that makes most permission prompts unnecessary.

---

## Sandboxing Architecture

### How It Works

Claude Code's sandboxing restricts the agent's filesystem and network access at the OS level, regardless of what tools or commands it attempts to run.

| Platform | Technology | Mechanism |
|----------|-----------|-----------|
| **Linux** | bubblewrap (bwrap) | Filesystem namespaces, network isolation |
| **macOS** | seatbelt (sandbox-exec) | System call filtering, path restrictions |

### Isolation Layers

```
┌──────────────────────────────────────┐
│ Layer 1: Sandboxing (OS-level)       │
│ - Filesystem: project dir + temp     │
│ - Network: allowed/blocked domains   │
│ - Processes: restricted spawn        │
├──────────────────────────────────────┤
│ Layer 2: Permission Model            │
│ - PreToolUse hooks can block/modify  │
│ - settings.json allow/deny rules     │
│ - /permissions for interactive setup │
├──────────────────────────────────────┤
│ Layer 3: Hooks (Application-level)   │
│ - Custom validation logic            │
│ - Output formatting and logging      │
│ - Quality gates                      │
└──────────────────────────────────────┘
```

### Impact

From Anthropic's internal testing:

| Metric | Before Sandboxing | After Sandboxing |
|--------|------------------|-----------------|
| Permission prompts per session | ~25 | ~4 |
| **Reduction** | — | **84%** |
| Developer flow interruptions | Frequent | Rare |
| Security posture | User-dependent | Enforced by OS |

---

## Permission Model Design

### Pre-Approved Permissions

The most effective way to reduce permission prompts without sacrificing security:

```json
{
  "permissions": {
    "allow": [
      "Bash(git status*)",
      "Bash(git diff*)",
      "Bash(git log*)",
      "Bash(npm run *)",
      "Bash(python3 -m pytest*)",
      "Read(*)",
      "Glob(*)",
      "Grep(*)"
    ]
  }
}
```

**Principle**: Pre-approve read operations and known-safe commands. Leave write operations and destructive commands for explicit approval.

### Permission Hierarchy

```
Enterprise Policy (Teams/Enterprise plans)
    ↓ overrides
Project settings (.claude/settings.json)
    ↓ overrides
User settings (~/.claude/settings.json)
    ↓ overrides
Local settings (.claude/settings.local.json)
```

More specific settings override broader ones on conflict.

### Interactive Setup

Use `/permissions` to interactively configure allowed commands during a session. Claude Code detects commonly-used patterns and suggests pre-approvals.

---

## Security Hooks

Hooks provide application-level security complementary to OS-level sandboxing.

### PreToolUse: Block Dangerous Operations

```bash
#!/bin/bash
read -r input
TOOL=$(echo "$input" | jq -r '.tool // "unknown"')

if [ "$TOOL" = "Bash" ]; then
    COMMAND=$(echo "$input" | jq -r '.parameters.command // ""')

    # Block destructive patterns
    if [[ "$COMMAND" =~ "rm -rf /" ]] || \
       [[ "$COMMAND" =~ "git push --force" ]] || \
       [[ "$COMMAND" =~ "DROP TABLE" ]]; then
        echo "Blocked dangerous command: $COMMAND"
        exit 2  # Block execution
    fi
fi

exit 0  # Allow
```

### PostToolUse: Audit Logging

```bash
#!/bin/bash
read -r input
TOOL=$(echo "$input" | jq -r '.tool // "unknown"')
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Log all tool executions for audit trail
echo "$TIMESTAMP|$TOOL|$(echo "$input" | jq -c '.parameters')" >> .claude/audit.log

exit 0
```

---

## Data Residency (Opus 4.6+)

For enterprise compliance, the `inference_geo` parameter controls where model inference runs.

| Setting | Behavior | Pricing | Available |
|---------|----------|---------|-----------|
| Default | Standard routing | Standard | All models |
| `"us"` | US-only inference | 1.1x standard | Models after Feb 1, 2026 |

### Configuration

```json
// Workspace-level (Teams/Enterprise)
{
  "allowed_inference_geos": ["us"],
  "default_inference_geo": "us"
}

// Per-request (API)
{
  "inference_geo": "us"
}
```

---

## MCP Security

MCP servers introduce additional attack surfaces. Key risks from [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/):

| Risk | Mitigation |
|------|------------|
| **Tool poisoning** | Pin server versions, verify checksums |
| **Rug pull attacks** | Monitor for tool description changes |
| **Schema poisoning** | Validate tool schemas before use |
| **Memory poisoning** | Audit agent memory writes |
| **Supply chain** | Use official servers, review dependencies |

**See**: [MCP Patterns](./mcp-patterns.md) for comprehensive MCP security guidance.

---

## Agent-Specific Attack Surface

**Source**: H-AGENT-SECURITY-01 hypothesis (4.8/5 confidence, settled)

The 4-layer security stack (Sandboxing, Auto Mode, Permissions, Hooks) is project-scoped -- it protects the local development environment. The attack surface for AI coding agents extends well beyond the project boundary into skill marketplaces, agent-to-agent communication, and social engineering vectors.

### Canonical Example: CVE-2026-25253 (OpenClaw)

CVE-2026-25253 (CVSS 8.8) demonstrated one-click RCE via an unvalidated WebSocket gateway combined with authentication token theft. This is the canonical example of why OS-level sandboxing exists -- without it, a compromised agent skill has direct access to the host system.

### Skill Marketplace Poisoning

The agent skill ecosystem is experiencing supply-chain attacks at scale:
- **15% of OpenClaw skills** contain harmful instructions (Jenova Research, March 2026)
- **230 malicious plugins** published on ClawHub in a single week using the ClickFix social engineering technique (Cisco/Kaspersky, February 2026)
- Attack vectors include agent self-destruction, identity spoofing, and semantic manipulation of agent behavior through crafted skill descriptions

### Agent-to-Agent Amplification

Multi-agent architectures introduce amplification risks not present in single-agent deployments:
- Infinite reply loops between agents can burn 60K+ tokens in 9 days without human intervention
- Compromised agents can propagate malicious instructions laterally to other agents in an orchestration chain

### Attack Taxonomy

| Category | Description | Mitigation Layer |
|----------|-------------|-----------------|
| **Social engineering** | Prompt injection via skill descriptions or tool outputs | Sandboxing + Hooks |
| **Agent self-destruction** | Malicious skill triggers agent to delete its own config | Sandboxing (filesystem) |
| **Identity spoofing** | Agent impersonates another agent or user in multi-agent flows | Permission model + auth |
| **Semantic attack surface** | Exploiting natural language ambiguity in agent instructions | Explicit rules in CLAUDE.md |
| **Skill marketplace poisoning** | Publishing malicious skills that pass superficial review | Supply chain verification |

### Enterprise Governance: Microsoft Agent 365 Model

For organizations deploying agents at scale, the Microsoft Agent 365 model provides a reference architecture:
- **Centralized registry** of all deployed agents with unique Agent IDs (Entra-based)
- **Designated human sponsor** required for each agent (accountability chain)
- **Shadow agent detection** to identify unauthorized agent deployments

### Managed Agents Security Model (Anthropic, April 2026)

Anthropic's Managed Agents introduce a structured security model for agent deployments:
- **Environment scoping** with explicit permission grants per agent instance
- **Vault-based OAuth credential management** -- agents never see raw credentials
- **Limited networking** -- agents can only access pre-approved endpoints

### OWASP AI Vulnerability Scoring System (AIVSS)

OWASP released the AI Vulnerability Scoring System (February 2026) providing use-case-aware risk quantification for agent deployments. Unlike traditional CVSS, AIVSS accounts for the non-deterministic nature of AI agents and the amplification potential of multi-agent systems.

---

## Defense-in-Depth Strategy

For production deployments, layer security mechanisms:

### Tier 1: All Projects (5 minutes)

- [ ] Enable sandboxing (default in recent versions)
- [ ] Configure pre-approved permissions in settings.json
- [ ] Add Stop hook for uncommitted changes reminder

### Tier 2: Active Development (15 minutes)

- [ ] Add PreToolUse hook for destructive command blocking
- [ ] Configure `disabledMcpServers` for unused MCP servers
- [ ] Set up audit logging via PostToolUse hook

### Tier 3: Enterprise/Compliance (30+ minutes)

- [ ] Configure data residency (`inference_geo`)
- [ ] Set up enterprise policy via Teams/Enterprise plan
- [ ] Implement OWASP MCP checklist for all MCP servers
- [ ] Enable Claude Code Analytics for usage monitoring
- [ ] Establish centralized agent registry with unique agent IDs and designated human sponsors (Microsoft Agent 365 model)
- [ ] Deploy shadow agent detection -- 50% of employees use non-company-issued AI tools, 53% hide AI usage, and only 18.5% are aware of company AI policy (H-AI-SHADOW-01, 4.5/5 confidence). Technical enforcement via sandboxing and hooks is more reliable than policy-based controls alone
- [ ] Apply OWASP AIVSS scoring to agent deployments for use-case-aware risk quantification

---

## Anti-Patterns

### ❌ Disabling Sandboxing
**Problem**: Turning off sandboxing because it blocks a needed operation
**Symptom**: Reduced security posture, back to frequent permission prompts
**Solution**: Configure sandbox exceptions for specific paths rather than disabling entirely

### ❌ Over-Approving Permissions
**Problem**: `"allow": ["Bash(*)"]` to avoid all permission prompts
**Symptom**: Claude can execute any command without restriction
**Solution**: Approve specific command patterns, not wildcards for destructive tools

### ❌ Security Hooks Without Sandboxing
**Problem**: Relying only on application-level hooks for security
**Symptom**: Hooks can be bypassed by bugs or unexpected tool behavior
**Solution**: Use sandboxing for hard boundaries, hooks for soft quality gates

### ❌ Ignoring MCP Security
**Problem**: Installing MCP servers without security review
**Symptom**: ~43% of community MCP servers have command injection vulnerabilities
**Solution**: Apply OWASP MCP checklist, prefer official servers, audit before use

---

## Auto Mode: Classifier-Based Permissions (March 2026)

**Source**: [Claude Code Auto Mode](https://www.anthropic.com/engineering/claude-code-auto-mode) (March 25, 2026)
**Evidence Tier**: A (Primary vendor)

Auto mode automates permission decisions using a two-stage classifier, reducing friction while maintaining security.

### How It Works

```
Permission Request
    │
    ├── Stage 1: Fast single-token filter (Sonnet 4.6)
    │   └── SAFE → Auto-approve
    │
    └── Stage 2: Chain-of-thought reasoning (if flagged)
        ├── SAFE → Auto-approve
        └── RISKY → Prompt user (interactive) or abort (non-interactive)
```

### Key Metrics

| Metric | Value |
|--------|-------|
| **User approval rate** | 93% of permission prompts are approved |
| **Classifier model** | Sonnet 4.6 |
| **Non-interactive behavior** | Aborts if classifier repeatedly blocks (no user fallback) |

### Enabling

```bash
# Via CLI flag
claude --permission-mode auto

# Via settings.json
{
  "permissions": {
    "mode": "auto"
  }
}
```

### New Sandbox Settings (v2.1.77-83)

| Setting | Purpose | Version |
|---------|---------|---------|
| `sandbox.failIfUnavailable` | Fail startup if sandbox unavailable (strict mode) | v2.1.83 |
| `sandbox.filesystem.allowRead` | Allow read within `denyRead` regions | v2.1.77 |
| `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1` | Strip Anthropic/cloud credentials from subprocesses | v2.1.83 |
| Silent sandbox disable warning | Visible startup warning if sandbox silently disabled | v2.1.78 |

### Recommendation Update

The permission/security stack is now four layers (up from three):

```
Layer 1: Sandboxing (OS-level)        — 84% permission reduction
Layer 2: Auto Mode (classifier)       — Automates 93% of remaining prompts
Layer 3: Permission Rules (settings)  — Pre-approve safe patterns
Layer 4: Hooks (application-level)    — Custom validation logic
```

---

## Related Patterns

- [Secure Code Generation](./secure-code-generation.md) - Securing the code Claude generates (output-level security)
- [Advanced Hooks](../archive/patterns-v1/advanced-hooks.md) - Hook patterns for security and quality gates
- [MCP Patterns](./mcp-patterns.md) - MCP security framework and OWASP compliance
- [Project Infrastructure](../archive/patterns-v1/project-infrastructure.md) - Infrastructure tiers including security
- [Subagent Orchestration](./orchestration-comparison.md) - Security for multi-agent execution
- [Agent-Driven Development](./agent-driven-development.md) - PreToolUse security hooks and permission matrices from production repos (mndr-review-automation case study)

---

## Sources

- [Beyond Permission Prompts](https://www.anthropic.com/engineering/beyond-permission-prompts) (October 2025)
- [Claude Code Auto Mode](https://www.anthropic.com/engineering/claude-code-auto-mode) (March 25, 2026)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- [Claude Code Security Documentation](https://code.claude.com/docs/en/security)
- [Data Residency Documentation](https://platform.claude.com/docs/en/build-with-claude/data-residency) (February 2026)
- H-AGENT-SECURITY-01 — Agent-specific attack surface analysis (4.8/5 confidence, settled)
- H-AI-SHADOW-01 — Shadow AI usage in enterprises (4.5/5 confidence)
- [OWASP AI Vulnerability Scoring System (AIVSS)](https://owasp.org/) (February 2026)
- Anthropic Managed Agents — Environment scoping and credential management (April 2026)

*Last updated: April 2026*

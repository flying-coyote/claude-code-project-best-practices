---
evidence-tier: A
applies-to-signals: [harness-hooks, commit-security-paths, model-version-4-8]
last-verified: 2026-05-30
revalidate-by: 2026-11-30
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

### `hard_deny`: Unconditional Blocks in Auto Mode (v2.1.128+)

Added in the v2.1.128 changelog (verified 2026-05-24 against [Anthropic Claude Code changelog](https://code.claude.com/docs/en/changelog), Tier A): a new `settings.autoMode.hard_deny` array that **takes precedence over all allow rules** — including project, user, and managed settings.

```json
{
  "autoMode": {
    "hard_deny": [
      "Bash(rm -rf /*)",
      "Bash(curl * | bash)",
      "Bash(* > /etc/*)",
      "Bash(git push --force origin master)"
    ]
  }
}
```

**What this changes**: Before v2.1.128, a permissive `allow` rule (e.g., `Bash(*)` in a dev environment) could be silently shadowed by overlapping rules but could not be unconditionally overridden. `hard_deny` provides a layer that *cannot* be allow-listed around, even by an auto-mode classifier approval.

**When to use**:
- Catastrophic-blast-radius commands that should never run regardless of context (`rm -rf /`, force-push to protected branches, secret-file overwrites)
- Org-mandated denylists that need to survive even broad project-level `allow` grants
- Environments where the auto-mode classifier itself shouldn't be trusted to refuse specific operations

**When `hard_deny` is the wrong tool**:
- Conditional restrictions ("block this except during deploys") — use scoped `allow` rules instead
- Per-user policy — `hard_deny` is global to the settings layer it's defined in, not per-identity
- Educational tripwires for normal mistakes — overusing `hard_deny` erodes its signal value

The `hard_deny` layer is a backstop, not a primary permission model. The primary defense remains the `allow` list + auto-mode classifier; `hard_deny` covers the failure mode where those fail open.

### Sandbox Path Overrides (v2.1.134+)

Two new settings to handle non-standard sandbox tool locations:

| Setting | What it overrides |
|---|---|
| `sandbox.bwrapPath` | Path to `bwrap` (bubblewrap) — for Linux setups where bubblewrap is not on `PATH` |
| `sandbox.socatPath` | Path to `socat` — for setups where socat is in a non-standard location |

Defaults remain auto-detection. Override only when the auto-detect path fails for your environment.

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

## Model-Level Prompt-Injection Robustness: Opus 4.8 Regressed vs 4.7 (system card §5.2)

**Source**: [Opus 4.8 system card](https://www.anthropic.com/claude-opus-4-8-system-card) §5.2 (Evidence Tier A). Released 2026-05-28; model ID `claude-opus-4-8`.

Opus 4.8 is an alignment *improvement* over 4.7 on most measures — but **prompt-injection robustness is the exception: 4.8 regressed vs 4.7**. This matters because injection robustness is a model property the sandboxing/permission/hook stack above does *not* replace — those layers constrain what a compromised agent can *do*; injection robustness governs how easily the agent is compromised in the first place.

The numbers below are easy to mis-cite. **Always state the safeguard / attempt-count / thinking conditions** — an unqualified headline percentage is meaningless here.

| Evaluation | Conditions | Opus 4.7 | Opus 4.8 |
|---|---|---|---|
| Gray Swan ART, tool-use | k=100 attempts, with thinking | 6.0% | **9.6%** |
| Shade adaptive attacker — coding / text injection | single attempt, **no safeguards**, with thinking | 2.34% | **7.03%** |
| Shade adaptive attacker — computer-use | single attempt, **no safeguards**, with thinking | 0.46% | **7.14%** |
| Shade adaptive attacker — computer-use | single attempt, **with safeguards**, with thinking | — | **5.11%** |

Reading the table: these are attack *success* rates (lower is better), so every 4.7→4.8 movement here is a regression. The computer-use single-attempt rate is the sharpest: 0.46% → 7.14% with no safeguards. **Safeguards materially reduce it** — the same computer-use single-attempt rate drops from 7.14% to 5.11% with safeguards enabled — but does not return it to the 4.7 level.

**What this does and does not mean:**

- It does **not** mean 4.8 is broadly less safe — Anthropic reports 4.8 as an improvement over 4.7 on most alignment measures (honesty in agentic settings "markedly improved"; Petri 3.0 "best-aligned publicly accessible model by nearly all these metrics"). Injection robustness is a specific, named exception.
- The widely-circulated **"0.07% → 0.26%" pair is wrong** — those are error-bar margins, not injection rates. Do not cite them.
- The single-attempt / k=100 distinction is load-bearing: a 7% single-attempt success rate compounds badly under repeated adversarial attempts (the Gray Swan k=100 column shows the multi-attempt regime).

**Defensive implication**: on 4.8, lean harder on the layers that don't depend on model injection-robustness — OS-level sandboxing (Layer 1), `hard_deny` for catastrophic-blast-radius commands (see above), and least-privilege networking — especially for **computer-use and tool-use agents handling untrusted content**, where the regression is largest. Enable injection safeguards where available; the system-card figures show they cut the computer-use single-attempt rate by roughly a third.

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
- [Opus 4.8 system card](https://www.anthropic.com/claude-opus-4-8-system-card) §5.2 (Tier A, released 2026-05-28) — prompt-injection robustness regressed 4.7→4.8: Gray Swan ART tool-use (k=100, thinking) 6.0%→9.6%; Shade coding/text injection (single attempt, no safeguards, thinking) 2.34%→7.03%; computer-use (single attempt, no safeguards, thinking) 0.46%→7.14%, dropping to 5.11% with safeguards. The "0.07%→0.26%" figure circulating elsewhere is error-bar margins, not injection rates — not used here.

*Last updated: May 2026 (Opus 4.8 prompt-injection regression, §5.2). Prior: April 2026.*

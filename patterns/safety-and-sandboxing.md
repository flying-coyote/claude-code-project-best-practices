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

## Related Patterns

- [Secure Code Generation](./secure-code-generation.md) - Securing the code Claude generates (output-level security)
- [Advanced Hooks](./advanced-hooks.md) - Hook patterns for security and quality gates
- [MCP Patterns](./mcp-patterns.md) - MCP security framework and OWASP compliance
- [Project Infrastructure](./project-infrastructure.md) - Infrastructure tiers including security
- [Subagent Orchestration](./subagent-orchestration.md) - Security for multi-agent execution

---

## Sources

- [Beyond Permission Prompts](https://www.anthropic.com/engineering/beyond-permission-prompts) (October 2025)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- [Claude Code Security Documentation](https://code.claude.com/docs/en/security)
- [Data Residency Documentation](https://platform.claude.com/docs/en/build-with-claude/data-residency) (February 2026)

*Last updated: February 2026*

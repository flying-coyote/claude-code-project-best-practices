---
evidence-tier: A
applies-to-signals: [harness-hooks, commit-security-paths, model-version-4-8, harness-loop-config, harness-scheduled-agent, ci-scheduled-agent]
last-verified: 2026-07-10
revalidate-by: 2026-11-30
status: PRODUCTION
---

# Safety and Sandboxing

> **Collapsed 2026-07-10 (Reduction Phase 4).** The sandboxing/permission/auto-mode mechanism half is now first-party (official sandboxing + permission-modes docs; autoMode.classifyAllShell v2.1.193). Kept delta: the OWASP mapping, the security-stack evaluation, unattended-execution controls, and the credential-boundary hook pattern absorbed from the retired templates/.

**Evidence Tier**: A (Primary vendor + industry standard) — full source list at the bottom of this doc

**SDD Phase**: Cross-phase (security applies to all phases)

---

## The Permission Stack, Evaluated

Official docs now own the mechanism for each layer — OS-level sandboxing, the auto-mode classifier, permission rules, hooks. What's kept here is what those docs don't cover: measured impact, where the stack fails, and how far a `hard_deny` override actually reaches.

### Measured impact

Anthropic's internal testing found permission prompts per session fell from roughly 25 to roughly 4 (an 84% reduction) once OS-level sandboxing removed the need to ask about most operations -- the security benefit comes from what the agent can't reach, not what it's told not to do.

### `hard_deny`: a backstop, not a primary control

`settings.autoMode.hard_deny` (v2.1.128+) takes precedence over every `allow` rule, including project, user, and managed settings — it's the one layer that can't be allow-listed around, even by an auto-mode classifier approval.

Use it for catastrophic-blast-radius commands that should never run regardless of context (`rm -rf /`, force-push to protected branches, secret-file overwrites), org-mandated denylists that need to survive broad `allow` grants, and cases where the auto-mode classifier itself shouldn't be trusted to refuse an operation. It's the wrong tool for conditional restrictions ("block this except during deploys" — use scoped `allow` rules instead), per-user policy (it's global to the settings layer it's defined in, not per-identity), or tripwires for normal mistakes, since overusing it erodes its signal value. The primary defense stays the `allow` list plus the classifier; `hard_deny` covers the failure mode where those fail open.

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

**Defensive implication**: on 4.8, lean harder on the layers that don't depend on model injection-robustness — OS-level sandboxing, `hard_deny` for catastrophic-blast-radius commands (see above), and least-privilege networking — especially for **computer-use and tool-use agents handling untrusted content**, where the regression is largest. Enable injection safeguards where available; the system-card figures show they cut the computer-use single-attempt rate by roughly a third.

---

## Agent-Specific Attack Surface

**Source**: H-AGENT-SECURITY-01 hypothesis (4.8/5 confidence, settled)

The 4-layer security stack (Sandboxing, Auto Mode, Permissions, Hooks) is project-scoped -- it protects the local development environment. The attack surface for AI coding agents extends well beyond the project boundary into skill marketplaces, agent-to-agent communication, and social engineering vectors, and the sandboxing case is not hypothetical: CVE-2026-25253 (OpenClaw, CVSS 8.8) demonstrated one-click RCE via an unvalidated WebSocket gateway combined with authentication token theft -- without OS-level sandboxing, a compromised agent skill has direct access to the host system.

The skill-marketplace supply chain is under attack at scale: 15% of OpenClaw skills contain harmful instructions (Jenova Research, March 2026), and 230 malicious plugins were published on ClawHub in a single week using the ClickFix social-engineering technique (Cisco/Kaspersky, February 2026), with vectors spanning agent self-destruction, identity spoofing, and semantic manipulation of agent behavior through crafted skill descriptions. Multi-agent architectures add a risk single-agent deployments don't have: infinite reply loops between agents have burned 60K+ tokens in 9 days without human intervention, and a compromised agent can propagate malicious instructions laterally through an orchestration chain.

### Unbounded & Unattended Loops

Scheduling and looping primitives (`/loop`, cloud Routines, Desktop scheduled tasks) move the blast radius from "what one approved tool call can do" to "what an autonomous loop can do before anyone looks." Filip Verloy (Rubrik, 2026-06-07, Tier C — vendor-adjacent, flag bias) names the failure modes even if the source is promotional: agentic overreach (the agent broadens its own permissions to fix a local problem), infinite hallucination loops that hammer APIs, and prompt injection executed at machine speed — "if a security engine discovers a violation after an agent has recursively run 500 loops, the damage is already done."

The defensible response leans on the concrete, auditable controls the primitives already ship rather than on the framing:

| Risk | Control (Tier A — Claude Code docs) |
|---|---|
| Forgotten recurring loop runs for a week | `/loop` recurring tasks auto-expire 7 days after creation |
| Scheduler running at all | `CLAUDE_CODE_DISABLE_CRON=1` disables `/loop`, the cron tools, and scheduled tasks |
| Cloud Routine acts with no approval | Cloud Routines run with **no permission prompts** — scope them deliberately and confirm with the operator; they may leave no on-disk footprint to audit |
| Desktop task touches uncommitted work | Runs against the working dir *including uncommitted changes* unless worktree isolation is on |
| Autonomous CI agent commits/PRs | Scope `GITHUB_TOKEN`/workflow permissions; require human review on agent-authored PRs |

See [Scheduled & Looping Primitives](scheduled-and-looping-primitives.md) for the full primitive surface and the audit signals that detect each.

### Governance and Credential Isolation at Scale

Two reference architectures address the fleet-scale version of this problem. Microsoft's Agent 365 model pairs a centralized, Entra-based agent registry (unique Agent IDs, one designated human sponsor per agent) with shadow-agent detection -- worth having, since 50% of employees already use non-company-issued AI tools, 53% hide that usage, and only 18.5% are aware of company AI policy (H-AI-SHADOW-01, 4.5/5 confidence); technical enforcement via sandboxing and hooks is more reliable than policy alone. Anthropic's Managed Agents take the credential-isolation route -- Lance Martin, Gabe Cemaj, Michael Cohen, ["Scaling Managed Agents"](https://www.anthropic.com/engineering/managed-agents) (2026-04-08, Tier A): a durable Session log outside the container, a stateless Harness "brain", and an isolated Sandbox for the "hands", with OAuth credentials in an external vault so a prompt-injected agent cannot exfiltrate them -- directly relevant to the unbounded-loop risks above. OWASP's AI Vulnerability Scoring System (February 2026) extends CVSS-style scoring for this non-determinism and multi-agent amplification.

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

## Credential-boundary enforcement (absorbed from templates/, 2026-07-10)

The retired templates/ directory shipped a generic `rules/security-boundaries.md` checklist for repos handling credentials or customer data:

- Never commit `.env` files, API keys, tokens, passwords, or certificates.
- Never hardcode credentials — use environment variables instead.
- Never log request bodies, prompts, or tool output that may contain credentials.

A checklist is only a reminder unless something enforces it. A `PreToolUse` hook can scan staged content for credential patterns before a commit-touching tool call is allowed to run:

`.claude/settings.json`:
```json
{
  "hooks": {
    "PreToolUse": [
      { "matcher": "Bash", "hooks": [{ "type": "command", "command": ".claude/hooks/scan-credentials.sh" }] }
    ]
  }
}
```

`.claude/hooks/scan-credentials.sh`:
```bash
#!/bin/bash
read -r input
cmd=$(echo "$input" | jq -r '.tool_input.command // ""')
[[ "$cmd" == *"git commit"* ]] || exit 0
git diff --cached | grep -EqI '(AKIA[0-9A-Z]{16}|-----BEGIN[A-Z ]*PRIVATE KEY-----|(api|secret)[_-]?key\s*=)' \
  && { echo "Blocked: staged diff matches a credential pattern." >&2; exit 2; }
exit 0
```

`/init` and the official hooks documentation ("Claude can write hooks for you") now generate project-specific versions of what the deleted tier templates did generically — this hook is one worked instance of that pattern, not a template to copy verbatim.

---

## Related Patterns

- [Secure Code Generation](./secure-code-generation.md) - Securing the code Claude generates (output-level security)
- [Advanced Hooks](../archive/patterns-v1/advanced-hooks.md) - Hook patterns for security and quality gates
- [MCP Patterns](./mcp-patterns.md) - MCP security framework and OWASP compliance
- [Agent-Driven Development](./agent-driven-development.md) - PreToolUse security hooks and permission matrices from production repos (mndr-review-automation case study)

---

## Sources

- [Beyond Permission Prompts: Making Claude Code More Secure](https://www.anthropic.com/engineering/beyond-permission-prompts) (October 2025, Tier A) — sandboxing impact measurement
- [Claude Code Auto Mode](https://www.anthropic.com/engineering/claude-code-auto-mode) (March 25, 2026, Tier A) — classifier cited in the `hard_deny` and attack-surface analysis above
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) (Tier A)
- [Claude Code Security Documentation](https://code.claude.com/docs/en/security) (Tier A)
- H-AGENT-SECURITY-01 — Agent-specific attack surface analysis (4.8/5 confidence, settled)
- H-AI-SHADOW-01 — Shadow AI usage in enterprises (4.5/5 confidence)
- [OWASP AI Vulnerability Scoring System (AIVSS)](https://owasp.org/) (February 2026)
- Anthropic Managed Agents — Environment scoping and credential management (April 2026)
- [Opus 4.8 system card](https://www.anthropic.com/claude-opus-4-8-system-card) §5.2 (Tier A, released 2026-05-28) — prompt-injection robustness regressed 4.7→4.8: Gray Swan ART tool-use (k=100, thinking) 6.0%→9.6%; Shade coding/text injection (single attempt, no safeguards, thinking) 2.34%→7.03%; computer-use (single attempt, no safeguards, thinking) 0.46%→7.14%, dropping to 5.11% with safeguards. The "0.07%→0.26%" figure circulating elsewhere is error-bar margins, not injection rates — not used here.
- templates/rules/security-boundaries.md, templates/settings.json, templates/hooks/{pre-commit-lint.sh, post-edit-test.sh} — retired 2026-07-10; credential-boundary rule set and hook pattern absorbed into this doc

*Last updated: 2026-07-10 (Reduction Phase 4 collapse: cut sandbox/permission/auto-mode mechanism now owned by official docs; absorbed templates/ credential-boundary material). Prior: 2026-06-15 (unbounded/unattended-loop blast radius + controls; Scaling Managed Agents citation; loop/schedule audit signals). Prior: May 2026 (Opus 4.8 prompt-injection regression, §5.2).*

<!-- graphify-footer:start -->

## Related (from graph)

- [`analysis/mcp-patterns.md`](analysis/mcp-patterns.md) [EXTRACTED (1.00) ×2] — references
- [`analysis/domain-knowledge-architecture.md`](analysis/domain-knowledge-architecture.md) [EXTRACTED (1.00)] — references
- [`AUDIT-CONTEXT.md`](AUDIT-CONTEXT.md) [EXTRACTED (1.00)] — references
- [`INDEX.md`](INDEX.md) [EXTRACTED (1.00)] — references

<!-- graphify-footer:end -->

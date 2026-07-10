---
version-requirements:
  claude-code: "v2.1.0+"  # Skills auto-reload feature
version-last-verified: "2026-03-23"
measurement-claims:
  - claim: "Skills are 4x more token-efficient than MCP for methodology (stale-pending-remeasure: tool search v2.1.121)"
    source: "Simon Willison analysis"
    date: "2025-10-16"
    revalidate: "2026-10-16"
status: PRODUCTION
last-verified: "2026-07-10"
evidence-tier: B
applies-to-signals: [harness-skills, harness-mcp]
revalidate-by: 2026-09-30
---

# Claude Code Plugins and Extension Mechanisms

> **Collapsed 2026-07-10 (Reduction Phase 4).** Mechanism documentation is now first-party (official plugins/skills docs, /plugin marketplace, nested skills v2.1.157). Kept delta: marketplace evaluation and the measured token economics.

**Evidence Tier**: B (Validated secondary — community + expert practitioner)

## Purpose

This document used to cover the full extension landscape: plugin structure, skills vs. MCP vs. hooks vs. slash commands, subagents, agent teams, permission configuration, the `.claude/rules/` directory, channels, and skill hot-reload mechanics. All of that is now native — the [official plugins docs](https://code.claude.com/docs/en/plugins), the `/plugin` marketplace, and nested skills (v2.1.157) document the mechanisms directly and stay current with the harness in a way a static analysis doc can't. What survives here is the two things those docs don't cover: how to evaluate a third-party plugin or skill before adopting it, and the measured token/context cost of each extension mechanism. The full walkthrough of each mechanism — plugin YAML structure, the skill/MCP/hook/command decision matrix, subagent design, the extended skill-frontmatter field table — is cut; a reader who needs that gets more accurate, more current information straight from the vendor than a snapshot analysis doc could offer.

## Evaluating Third-Party Plugins and Skills

### Official sources

1. **Claude Plugins Directory** ([claude.com/plugins](https://claude.com/plugins))
   - Official Anthropic plugin marketplace
   - Anthropic-verified and community-contributed plugins
   - Verified plugins: Frontend Design, Code Review, GitHub (official MCP)
   - High-installation plugins: Context7, Superpowers, Playwright
   - Installation statistics and compatibility information

2. **Anthropic Official Marketplace** (`claude-plugins-official`)
   - Automatically available in Claude Code
   - Run `/plugin` → Discover tab
   - **Keep updated**: run `/plugin marketplace update claude-plugins-official` periodically — the official marketplace receives new plugins and updates regularly, and running the update is what surfaces them when browsing

3. **Anthropic Demo Plugins** (`claude-code-plugins`)
   - Example plugins showing platform capabilities
   - Not auto-included; must add manually

```bash
# Update the official marketplace (recommended: weekly or before searching for new plugins)
/plugin marketplace update claude-plugins-official

# View available marketplaces
/plugin marketplace list
```

### Community marketplaces

Curated, but not Anthropic-vetted — apply the checklist below before installing from any of these:

| Source | Description | Link |
|--------|-------------|------|
| awesome-claude-code-plugins | Curated list + tools | [GitHub](https://github.com/ccplugins/awesome-claude-code-plugins) |
| Claude Code Plugins Hub | 243 plugins, Skills-compliant | [GitHub](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) |
| claude-plugins.dev | CLI manager | [Website](https://claude-plugins.dev/) |
| claudecodemarketplace.com | AI-curated marketplace | [Website](https://claudecodemarketplace.com/) |
| shanraisshan/claude-code-best-practice | Community workflow tips, top 4 MCP servers | [GitHub](https://github.com/shanraisshan/claude-code-best-practice) |

### Before installing

- [ ] Source reputation — known author or organization?
- [ ] Active maintenance — recent commits?
- [ ] Documentation — clear README with usage examples?
- [ ] Security review — no overly permissive capabilities?
- [ ] Minimal scope — does one thing well?
- [ ] Version pinned — can you lock to a specific version?

> "~43% of MCP servers have command injection vulnerabilities. Only ~10 of 5,960+ available servers are genuinely trustworthy."
> — [Nate B. Jones, MCP Implementation Guide](https://natesnewsletter.substack.com/p/the-mcp-implementation-guide-solving)

Apply the same skepticism to plugins: an unvetted community source can bundle arbitrary hooks, MCP servers, and shell access alongside whatever it's actually marketed for, so the checklist above is a gate, not a formality — run it before installing, not after something looks wrong.

### A worked example: Project CodeGuard

[CoSAI Project CodeGuard](https://github.com/cosai-oasis/project-codeguard) is an open-source security framework that embeds secure coding rules into AI agent workflows, with a `.claude-plugin/` directory for direct Claude Code integration. It provides 23 security rules covering cryptography, input validation, authentication, authorization, supply chain, cloud security, platform security, and data protection — worth naming here as a concrete pass against the checklist above (known author/organization, active maintenance, documented rules, minimal scope) rather than leaving that checklist abstract. Three integration depths, in increasing order of commitment: add 3 mandatory rules directly to CLAUDE.md (5 min), build a security skill with progressive disclosure (15 min), or install the full plugin (30 min). See [Secure Code Generation](./secure-code-generation.md) for the detailed integration instructions.

### Adoption anti-patterns

| Anti-Pattern | Problem | Fix |
|---|---|---|
| Plugin sprawl | Installing more plugins than you use, bloating context | Enable only what you need; disable when done |
| Kitchen sink plugin | One plugin trying to do everything | Prefer small, focused plugins that compose |
| Skipping security review | Trusting community plugins blindly | Run the checklist above before installing, every time |
| Version drift | Different team members on different plugin versions | Pin versions in shared `settings.json`; review plugin updates like any other dependency |

### Team governance

Once a plugin clears the checklist and is adopted, treat it as a dependency, not a one-time install:

1. **Pin versions** in `settings.json`, subject to the same change control as code.
2. **Review changes** before upgrading, the same way you'd review a library bump.
3. **Test in staging** before a team-wide rollout.
4. **Document exceptions** for configurations that diverge from the team default.

```json
{
  "plugins": {
    "marketplaces": ["claude-plugins-official"],
    "installed": {
      "team-standards": "1.2.0",
      "security-gates": "2.0.1"
    }
  }
}
```

## Token Economics

The choice between MCP and Skills is a cost decision as much as a capability one: whichever mechanism reaches the same outcome with fewer tokens per call compounds across a session, especially for agents that make many tool calls in a row. Measured context costs of the extension mechanisms follow (Evidence Tier B). Two of the numbers below predate tool search (v2.1.121), which changed how tool schemas load into context — treat those as directional until re-measured against the new baseline, not as current fact:

- **MCP servers** are an open protocol adopted by every major model provider, which is exactly why they carry more overhead than a Claude-specific mechanism: they can consume thousands of tokens per server just loading tool-schema definitions — the protocol transmits a JSON schema for every registered tool up front, whether that call gets used in the session or not *(stale-pending-remeasure: tool search v2.1.121)* — plus a 300-800ms baseline latency that makes them unsuitable for transaction paths.
- **Skills** are token-efficient by design: metadata loads first, at roughly dozens of tokens, with the full SKILL.md body loading only on invocation. Skill description budget scales dynamically at 2% of the context window, with a 16KB fallback; keep SKILL.md itself under 500 lines and move reference material into a `references/` subdirectory. — [Agent Skills Engineering Blog](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) (March 19, 2026)
- **Measured comparison**: Microsoft's Playwright CLI achieves a 4x token reduction (114K → 27K) over the equivalent MCP server by saving data to disk instead of streaming it into context *(stale-pending-remeasure: tool search v2.1.121)*. See [MCP Patterns — CLI vs MCP](./mcp-patterns.md#cli-vs-mcp-the-token-efficiency-case) for the full comparison.
- Simon Willison draws the same conclusion from the CLI-tool angle: "Almost everything achievable with an MCP can be handled by a CLI tool instead. LLMs know how to call `cli-tool --help`... Skills have exactly the same advantage, only now you don't even need to implement a new CLI tool — you can just drop a Markdown file describing how to do a task instead." — [Simon Willison](https://simonwillison.net/2025/Oct/16/claude-skills/), also the source behind this doc's frontmatter measurement-claim.

For the fuller MCP-vs-Skills cost comparison — Tenzir's production numbers ($10.27 vs $20.78 per task, 50% cheaper, 38% slower, 55% less cached tokens) — see [MCP vs Skills Economics](./mcp-vs-skills-economics.md); that's a dedicated measurement doc, not duplicated here. Both documents converge on the same directional finding from independent evidence (Willison's practitioner analysis here, Tenzir's production telemetry there): Skills win on token cost, MCP sometimes wins on wall-clock speed, and the right choice depends on which one you're optimizing for.

## Related Patterns

For the mechanism documentation itself, start with the official docs linked in Purpose above. These are the companion analysis docs for what isn't first-party yet:

- [MCP Patterns](./mcp-patterns.md) — Failure modes + positive patterns + security
- [MCP vs Skills Economics](./mcp-vs-skills-economics.md) — The fuller measured cost comparison referenced above
- [Secure Code Generation](./secure-code-generation.md) — CodeGuard integration for secure AI-generated code
- [Harness Engineering](./harness-engineering.md) — Diagnostic framework for choosing the right extension mechanism
- [Domain Knowledge Architecture](./domain-knowledge-architecture.md) — How to structure domain knowledge using these extension mechanisms without overwhelming context

## Sources

- [Claude Plugins Directory](https://claude.com/plugins) — Official Anthropic plugin marketplace
- [Anthropic Claude Code Plugins Documentation](https://code.claude.com/docs/en/plugins) — Official mechanism docs (plugin structure, skills, MCP, hooks, commands)
- [Simon Willison: Claude Skills are awesome, maybe a bigger deal than MCP](https://simonwillison.net/2025/Oct/16/claude-skills/) — Token-economics source
- [awesome-claude-code-plugins](https://github.com/ccplugins/awesome-claude-code-plugins) — Community marketplace
- [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) — Community-driven best practices (5.6k+ stars)

---

*Last updated: 2026-07-10*

<!-- graphify-footer:start -->

## Related (from graph)

- [`analysis/mcp-patterns.md`](analysis/mcp-patterns.md) [EXTRACTED (1.00)] — references
- [`analysis/domain-knowledge-architecture.md`](analysis/domain-knowledge-architecture.md) [EXTRACTED (1.00)] — references
- [`analysis/mcp-vs-skills-economics.md`](analysis/mcp-vs-skills-economics.md) [EXTRACTED (1.00) ×2] — references
- [`AUDIT-CONTEXT.md`](AUDIT-CONTEXT.md) [EXTRACTED (1.00)] — references
- [`INDEX.md`](INDEX.md) [EXTRACTED (1.00)] — references

<!-- graphify-footer:end -->

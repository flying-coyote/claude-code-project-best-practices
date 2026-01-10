# Claude Code Plugins and Extension Mechanisms

**Source**: [Anthropic Claude Code Documentation](https://code.claude.com/docs/en/plugins), [Simon Willison Analysis](https://simonwillison.net/2025/Oct/16/claude-skills/)
**Evidence Tier**: B (Validated secondary - community + expert practitioner)

## Overview

Claude Code provides multiple extension mechanisms, each designed for different use cases. Understanding when to use each is critical for maintainable, effective Claude Code projects.

---

## The Extension Landscape

### Quick Decision Matrix

| Mechanism | Invocation | Scope | Best For |
|-----------|-----------|-------|----------|
| **Plugins** | `/plugin` command | Distribution | Team standardization, bundled configurations |
| **Skills** | Auto-detected | Context-aware | Repeatable methodologies, workflows |
| **MCP Servers** | Configured | External access | Database, API, third-party integrations |
| **Slash Commands** | Manual (`/cmd`) | Explicit | User-initiated repeatable actions |
| **Subagents** | Delegated | Parallel | Context isolation, deep dives |
| **Hooks** | Automatic | Events | Quality gates, enforcement |

---

## Plugins

### What Are Plugins?

Plugins are lightweight packages that bundle any combination of:
- Slash commands
- Subagents
- MCP servers
- Hooks
- Skills

They install with a single command and can be toggled on/off as needed.

### Plugin Structure

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json        # Only plugin.json goes here
├── commands/              # Slash commands
├── agents/                # Subagents
├── skills/                # Claude skills
└── hooks/                 # Event hooks
```

**Common Mistake**: Don't put `commands/`, `agents/`, `skills/`, or `hooks/` inside `.claude-plugin/`. Only `plugin.json` goes there.

### When to Use Plugins

**Use plugins when:**
- Distributing configurations across a team
- Standardizing workflows across projects
- Bundling multiple related customizations
- Sharing opinionated setups publicly

**Don't use plugins when:**
- Single-use project configurations (use `.claude/` directly)
- Personal customizations (use `~/.claude/`)
- Simple one-file commands (use slash commands)

### Best Practices

1. **Version your plugins** - Pin versions to prevent drift
2. **Treat as dependencies** - Subject to same change control as code
3. **Start minimal** - Add capabilities gradually
4. **Document clearly** - Include README with usage examples

---

## Skills vs MCP: The Core Distinction

> "MCP provides connectivity; Skills provide methodology."
> — [IntuitionLabs Technical Comparison](https://intuitionlabs.ai/articles/claude-skills-vs-mcp)

### MCP Servers

**Purpose**: Connect Claude TO external systems

**Use when you need:**
- Access to databases (PostgreSQL, MongoDB)
- API integrations (GitHub, Slack, Stripe)
- External data sources (Google Drive, file systems)
- Business tool connections (CRM, project management)

**Characteristics:**
- Open protocol adopted by all major model providers
- Higher complexity (protocol specification, transports)
- Can consume thousands of tokens per server
- 300-800ms baseline latency (unsuitable for transaction paths)

### Skills

**Purpose**: Teach Claude HOW to perform tasks

**Use when you need:**
- Repeatable workflows (debugging, TDD, code review)
- Domain-specific methodologies
- Structured output patterns
- Team coding standards

**Characteristics:**
- Markdown files with YAML frontmatter
- Token-efficient (metadata loads first, ~dozens of tokens)
- Claude-specific (not portable to other models)
- Easy to create (if you can write docs, you can write skills)

### Expert Perspective: Simon Willison

> "Almost everything achievable with an MCP can be handled by a CLI tool instead. LLMs know how to call `cli-tool --help`... Skills have exactly the same advantage, only now you don't even need to implement a new CLI tool—you can just drop a Markdown file describing how to do a task instead."
> — [Simon Willison](https://simonwillison.net/2025/Oct/16/claude-skills/)

### Complementary Use

Skills and MCP are partners, not competitors:

```
┌─────────────────────────────────────────────────┐
│                    SKILL                         │
│  "How to analyze repository activity"            │
│                     │                            │
│         Uses multiple MCP servers:               │
│    ┌────────────────┼────────────────┐          │
│    ▼                ▼                ▼          │
│ [GitHub MCP]   [Database MCP]   [Slack MCP]     │
│                                                  │
│  Result: Coordinated analysis + notification    │
└─────────────────────────────────────────────────┘
```

---

## Slash Commands vs Skills

| Aspect | Slash Commands | Skills |
|--------|---------------|--------|
| **Trigger** | Explicit (`/command`) | Auto-detected by context |
| **Discovery** | Terminal autocomplete | Claude decides relevance |
| **Packaging** | Single file | Directory with supporting files |
| **Best for** | User-initiated actions | AI-initiated methodologies |

**Use slash commands for:** Explicit, repeatable terminal entry points
**Use skills for:** Context-aware methodologies Claude applies automatically

---

## Subagents

Custom subagents are specialized AI assistants with:
- Task-specific system prompts
- Customized tool access
- Separate context windows

### When to Use Subagents

1. **Parallel execution** - Multiple independent investigations
2. **Context isolation** - Prevent pollution of main context
3. **Deep dives** - Specialized analysis without losing main thread
4. **Early investigation** - Verify details before committing main context

> "Telling Claude to use subagents to verify details or investigate particular questions, especially early in a conversation, tends to preserve context availability without much downside."
> — [Anthropic Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)

---

## Hooks

Hooks are shell scripts that intercept Claude Code operations.

### Hook Events

| Event | Trigger | Use Case |
|-------|---------|----------|
| `UserPromptSubmit` | Message sent | Validation, preprocessing |
| `PreToolUse` | Before tool runs | Approval gates, blocking |
| `PostToolUse` | After tool runs | Verification, logging |
| `SessionStart` | Claude Code starts | Environment setup |
| `Stop` | Session ends | Cleanup, summarization |

### Hooks + Subagents Pattern

```
Hook (deterministic) ──triggers──▶ Subagent (intelligent)
     │                                    │
     │ "File edited"                      │ "Analyze for security issues"
     │                                    │
     ▼                                    ▼
[Intercept operation]            [AI-powered response]
```

---

## Finding High-Quality Plugins

### Official Sources

1. **Anthropic Official Marketplace** (`claude-plugins-official`)
   - Automatically available in Claude Code
   - Run `/plugin` → Discover tab
   - **Keep updated**: Run `/plugin marketplace update claude-plugins-official` periodically

2. **Anthropic Demo Plugins** (`claude-code-plugins`)
   - Example plugins showing capabilities
   - Must add manually

### Marketplace Maintenance

Keep your plugin sources current:

```bash
# Update the official marketplace (recommended: weekly or before searching for new plugins)
/plugin marketplace update claude-plugins-official

# View available marketplaces
/plugin marketplace list
```

**Why this matters**: The official marketplace receives new plugins and updates regularly. Running the update ensures you see the latest vetted plugins when browsing.

### Community Marketplaces

| Source | Description | Link |
|--------|-------------|------|
| **awesome-claude-code-plugins** | Curated list + tools | [GitHub](https://github.com/ccplugins/awesome-claude-code-plugins) |
| **Claude Code Plugins Hub** | 243 plugins, Skills-compliant | [GitHub](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) |
| **claude-plugins.dev** | CLI manager | [Website](https://claude-plugins.dev/) |
| **claudecodemarketplace.com** | AI-curated marketplace | [Website](https://claudecodemarketplace.com/) |

### Quality Checklist

Before installing a plugin:

- [ ] **Source reputation** - Known author or organization?
- [ ] **Active maintenance** - Recent commits?
- [ ] **Documentation** - Clear README with usage examples?
- [ ] **Security review** - No overly permissive capabilities?
- [ ] **Minimal scope** - Does one thing well?
- [ ] **Version pinned** - Can you lock to specific version?

### Security Warning

> "~43% of MCP servers have command injection vulnerabilities. Only ~10 of 5,960+ available servers are genuinely trustworthy."
> — [Nate B. Jones MCP Implementation Guide](https://natesnewsletter.substack.com/p/the-mcp-implementation-guide-solving)

**Apply this skepticism to plugins too.** Review before trusting.

---

## Decision Framework

```
Need to extend Claude Code?
│
├─► Need external data/API access?
│   └─► Use MCP Server
│
├─► Need repeatable methodology?
│   ├─► User-initiated? → Slash Command
│   └─► Context-aware? → Skill
│
├─► Need parallel/isolated work?
│   └─► Use Subagent
│
├─► Need automatic enforcement?
│   └─► Use Hook
│
└─► Need to distribute/share?
    └─► Package as Plugin
```

---

## Permission Configuration

### Settings Hierarchy

Claude Code settings follow a specific precedence order:

```
CLI Arguments (highest priority)
    ↓
Project Settings (.claude/settings.json)
    ↓
Global Settings (~/.claude/settings.json, lowest priority)
```

**Implication**: Project settings override global, CLI overrides both.

### Wildcard Permissions (v2.1.0+)

Permission rules now support wildcard patterns for flexible tool access control.

#### Bash Wildcards

```json
{
  "allowedTools": [
    "Bash(npm *)",           // Any npm command
    "Bash(* install)",       // Any install command
    "Bash(git * main)",      // Git commands targeting main
    "Bash(*-h)",             // Any help flag
    "Bash(* --help)",        // Any help command
    "Bash(python -m *)"      // Any Python module
  ]
}
```

#### Pattern Syntax

| Pattern | Matches | Example |
|---------|---------|---------|
| `Bash(npm *)` | npm followed by anything | `npm install`, `npm run build` |
| `Bash(* install)` | Anything ending in install | `pip install`, `brew install` |
| `Bash(git * main)` | Git commands with main | `git push origin main` |
| `Bash(*-h)` | Short help flags | `python -h`, `docker -h` |

#### MCP Server Wildcards

```json
{
  "allowedTools": [
    "mcp__github__*",        // All tools from GitHub MCP server
    "mcp__postgres__*",      // All tools from Postgres MCP server
    "mcp__*__read*"          // All read operations from any MCP
  ]
}
```

#### Disabling Specific Agents

```json
{
  "disallowedTools": [
    "Task(general-purpose)", // Disable general-purpose subagent
    "Task(Explore)"          // Disable Explore subagent
  ]
}
```

### Permission Detection (/doctor)

As of v2.1.3, the `/doctor` command detects and warns about:
- Unreachable permission rules (e.g., rules shadowed by broader patterns)
- Source tracking for each permission rule
- Conflicting allow/disallow entries

Run `/doctor` periodically to validate your permission configuration.

### Best Practices

1. **Start restrictive** - Allow specific commands, not `Bash(*)`
2. **Use wildcards for families** - `npm *` instead of listing every npm command
3. **Document intent** - Add comments explaining why permissions exist
4. **Review with /doctor** - Check for shadowed or conflicting rules

---

## Team Standardization

### Plugin Governance

1. **Pin versions** in `settings.json`
2. **Review changes** like any dependency
3. **Test in staging** before team rollout
4. **Document exceptions** for custom configurations

### Recommended Team Setup

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

---

## Anti-Patterns

### 1. Plugin Sprawl
**Problem**: Installing too many plugins, bloating context
**Fix**: Enable only what you need; disable when done

### 2. Kitchen Sink Plugin
**Problem**: One plugin trying to do everything
**Fix**: Small, focused plugins that compose

### 3. Skipping Security Review
**Problem**: Trusting community plugins blindly
**Fix**: Review capabilities before installing

### 4. Version Drift
**Problem**: Different team members on different versions
**Fix**: Pin versions in shared configuration

---

## Related Patterns

- [MCP Patterns](./mcp-patterns.md) - Failure modes + positive patterns + security
- [Skills README](../skills/README.md) - Comprehensive skills guide
- [Progressive Disclosure](./progressive-disclosure.md) - Token-efficient skill architecture

---

## Sources

- [Anthropic Claude Code Plugins Documentation](https://code.claude.com/docs/en/plugins)
- [Simon Willison: Claude Skills are awesome, maybe a bigger deal than MCP](https://simonwillison.net/2025/Oct/16/claude-skills/)
- [IntuitionLabs: Claude Skills vs MCP Technical Comparison](https://intuitionlabs.ai/articles/claude-skills-vs-mcp)
- [alexop.dev: Understanding Claude Code's Full Stack](https://alexop.dev/posts/understanding-claude-code-full-stack/)
- [Composio: Improving your coding workflow with Claude Code Plugins](https://composio.dev/blog/claude-code-plugin)
- [awesome-claude-code-plugins](https://github.com/ccplugins/awesome-claude-code-plugins)

*Last updated: January 2026*

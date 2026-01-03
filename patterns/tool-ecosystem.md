# AI Coding Tool Ecosystem

**Source**: Community observations, production experience
**Evidence Tier**: C (Community-driven, production-validated)

## Overview

This pattern helps developers choose the right AI coding tool for their context. While this repository focuses on Claude Code, the underlying principles (SDD, skills, context engineering) apply across tools.

> "Yesterday it was Cursor, today it's Windsurf, tomorrow it'll be something else... learn to endure change with principle."
> — IndyDevDan

**Core Insight**: Principles are durable; tools are ephemeral. Learn patterns that transfer.

---

## Tool Selection Framework

### When to Use Claude Code

| Scenario | Why Claude Code |
|----------|-----------------|
| **Anthropic ecosystem** | Native Claude integration, latest model access |
| **Terminal-first workflow** | CLI-native, git-centric by design |
| **Complex reasoning tasks** | Claude's strength in multi-step reasoning |
| **Skill-based methodology** | Official skills support (agentskills.io) |
| **Hooks and automation** | PreToolUse, PostToolUse, Stop hooks for quality gates |
| **Subagent orchestration** | Built-in parallel task delegation |

### When to Consider Alternatives

| Scenario | Alternative | Why |
|----------|-------------|-----|
| **Local model requirements** | Aider + Ollama | Privacy, offline, cost optimization |
| **IDE-native workflow** | Cursor, Windsurf | Tight editor integration, visual diff |
| **Containerized agents** | OpenHands | Sandboxed execution, reproducibility |
| **Multi-model orchestration** | Goose | Extensible local agent framework |
| **GitHub Copilot investment** | Copilot Chat | Existing enterprise licenses |

---

## Tool Comparison Matrix

| Capability | Claude Code | Aider | Cursor | OpenHands |
|------------|-------------|-------|--------|-----------|
| **Model** | Claude (cloud) | Any (local/cloud) | Various | Any |
| **Interface** | CLI | CLI | IDE | Web/Docker |
| **Local models** | No | Yes (Ollama) | Limited | Yes |
| **Git integration** | Manual | Automatic commits | Manual | Automatic |
| **Skills/Rules** | Skills (.md) | - | .cursorrules | - |
| **MCP support** | Yes | No | Limited | No |
| **Subagents** | Yes | No | No | Yes |
| **Hooks** | Yes | No | No | No |
| **Cost** | API usage | API/free (local) | Subscription | Free |

---

## Decision Tree

```
START: What's your primary constraint?

├─ Privacy/Compliance (data can't leave network)
│  └─ Use: Aider + Ollama (local models)
│
├─ IDE-native experience required
│  ├─ VS Code → Cursor or GitHub Copilot
│  └─ JetBrains → GitHub Copilot or AI Assistant
│
├─ Containerized/sandboxed execution
│  └─ Use: OpenHands (Docker-based)
│
├─ Best reasoning quality (cloud OK)
│  └─ Use: Claude Code (Claude models)
│
├─ Git-first workflow with auto-commits
│  └─ Use: Aider
│
└─ Flexible/extensible local agent
   └─ Use: Goose
```

---

## Pattern Portability

Many patterns in this repository transfer across tools:

### Fully Portable (Principles)

| Pattern | Applicability |
|---------|--------------|
| **Spec-Driven Development** | Any tool - it's methodology, not implementation |
| **Planning-First Development** | Any tool - "Great Planning is Great Prompting" |
| **Context Engineering** | Any tool - deterministic vs probabilistic context |
| **One Feature at a Time** | Any tool - prevents context exhaustion |
| **Evidence Tiers** | Any tool - intellectual rigor is tool-agnostic |

### Partially Portable (Need Adaptation)

| Pattern | Claude Code | Other Tools |
|---------|-------------|-------------|
| **Skills** | Native `.md` format | Cursor: `.cursorrules`; Others: system prompts |
| **Hooks** | PreToolUse/PostToolUse | Manual or tool-specific automation |
| **Subagents** | Task tool with types | Custom orchestration required |
| **MCP** | Native support | Limited or no support |

### Claude Code Specific

| Pattern | Portability |
|---------|------------|
| **Advanced Hooks** | Claude Code only |
| **Subagent Orchestration** | Claude Code only (others have different approaches) |
| **MCP Integration** | Primarily Claude Code (Cursor has limited support) |

---

## Hybrid Workflow Considerations

Some developers use multiple tools strategically:

### Example: Planning + Execution Split

```
1. PLANNING: Claude Code (superior reasoning)
   - Architecture decisions
   - Spec writing
   - Complex problem decomposition

2. EXECUTION: Aider + Local Model (privacy/cost)
   - Routine code generation
   - Refactoring tasks
   - Test writing
```

### Example: IDE + CLI Split

```
1. EXPLORATION: Cursor (visual, IDE-native)
   - Code navigation
   - Quick edits
   - Visual diff review

2. AUTOMATION: Claude Code (CLI-native)
   - Multi-file refactoring
   - Automated workflows
   - Skill-based methodologies
```

---

## Tool-Specific Resources

### Claude Code (This Repository)
- [Patterns](../patterns/) - Core implementation patterns
- [Skills](../skills/) - Reusable AI behavior patterns
- [Templates](../templates/) - Ready-to-use configurations

### Aider
- **Repository**: https://github.com/paul-gauthier/aider
- **Key Feature**: Treats LLM as a "git user" with automatic commits
- **Local Models**: Full Ollama support
- **Best For**: Git-centric workflows, local model usage

### Cursor
- **Website**: https://cursor.sh
- **Key Feature**: VS Code fork with native AI integration
- **Rules**: `.cursorrules` file (similar to CLAUDE.md)
- **Best For**: IDE-native experience, visual workflows

### OpenHands
- **Repository**: https://github.com/All-Hands-AI/OpenHands
- **Key Feature**: Dockerized autonomous agents
- **Best For**: Sandboxed execution, reproducible environments

### Goose
- **Repository**: https://github.com/block/goose
- **Key Feature**: Extensible local agent framework
- **Best For**: Custom agent development, local-first workflows

---

## Maintaining Tool Independence

### Recommendations

1. **Document in Markdown**: Works everywhere, not tool-specific
2. **Use Standard Formats**: Skills (agentskills.io) work in multiple tools
3. **Version Control Everything**: CLAUDE.md, .cursorrules, prompts - all in git
4. **Separate Concerns**: Architecture docs vs tool configuration
5. **Invest in Principles**: SDD, context engineering, evidence tiers transfer

### Anti-Patterns

- Assuming one tool will "win" - the landscape changes rapidly
- Deep vendor lock-in to tool-specific features
- Ignoring local model options for privacy-sensitive work
- Dismissing tools without understanding their strengths

---

## Related Patterns

- [Plugins and Extensions](./plugins-and-extensions.md) - Claude Code extension mechanisms
- [Context Engineering](./context-engineering.md) - Applies to all tools
- [Spec-Driven Development](./spec-driven-development.md) - Tool-agnostic methodology

---

## Sources

- [Aider](https://github.com/paul-gauthier/aider) - Git-centric AI coding
- [OpenHands](https://github.com/All-Hands-AI/OpenHands) - Dockerized agents
- [Goose](https://github.com/block/goose) - Extensible local agent
- [Cursor](https://cursor.sh) - AI-native IDE
- [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)

*Last updated: January 2026*

---
version-requirements:
  claude-code: "v2.0.0+"
measurement-claims:
  - claim: "Playwright CLI: 4x more token-efficient than Claude in Chrome extension"
    source: "Community benchmarking"
    date: "2025-12-15"
    revalidate: "2026-12-15"
status: "PRODUCTION"
last-verified: "2026-02-16"
---

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
| **Anthropic ecosystem** | Native Claude integration, Opus 4.6 with 1M context |
| **Terminal-first workflow** | CLI-native, git-centric by design |
| **Complex reasoning tasks** | Claude's strength in multi-step reasoning + think tool |
| **Skill-based methodology** | Official skills support (agentskills.io) |
| **Hooks and automation** | PreToolUse, PostToolUse, Stop hooks for quality gates |
| **Subagent orchestration** | Built-in parallel task delegation + agent teams |
| **Web-based workflow** | Claude Code on Web (VS Code in browser) |

### When to Consider Alternatives

| Scenario | Alternative | Why |
|----------|-------------|-----|
| **Local model requirements** | Aider + Ollama | Privacy, offline, cost optimization |
| **IDE-native workflow** | Cursor, Windsurf | Tight editor integration, visual diff |
| **Containerized agents** | OpenHands | Sandboxed execution, reproducibility |
| **Multi-model orchestration** | Goose | Extensible local agent framework |
| **GitHub Copilot investment** | Copilot Chat | Existing enterprise licenses |
| **Multi-agent orchestration** | Auto-Claude | Parallel agents, worktree isolation, autonomous workflows |
| **Browser automation** | Playwright | Mature, battle-tested, production-ready |

---

## Tool Comparison Matrix

| Capability | Claude Code | Aider | Cursor | OpenHands |
|------------|-------------|-------|--------|-----------|
| **Model** | Claude Opus 4.6 (cloud) | Any (local/cloud) | Various | Any |
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

### Auto-Claude
- **Repository**: https://github.com/AndyMik90/Auto-Claude
- **Key Feature**: Multi-agent orchestration with git worktree isolation
- **Best For**: Autonomous parallel development, safe experimentation

---

## Claude Code Deployment Options

Claude Code is available in multiple form factors:

| Deployment | Interface | Best For |
|-----------|-----------|----------|
| **Terminal CLI** | `claude` command | Primary development, full control |
| **VS Code Extension** | IDE panel | Inline diffs, visual workflows |
| **JetBrains Plugin** | IDE panel | IDE diff viewer, JetBrains AI subscription |
| **Claude Code on Web** | Browser-based VS Code | No local install, remote development |
| **GitHub Actions** | CI/CD | Automated PR reviews, issue handling |

### The Think Tool

**Source**: [The Think Tool: Enabling Claude to Stop and Think](https://www.anthropic.com/engineering/claude-think-tool) (March 2025)

The think tool enables Claude to pause mid-response to verify information before proceeding. Unlike extended thinking (which happens before response generation), the think tool acts as a deliberate checkpoint during complex multi-step tool chains.

**Impact**: 54% relative improvement on complex policy-following tasks.

**When it helps most**:
- Multi-step tool chains where each step depends on verifying previous results
- Complex policy compliance (checking multiple conditions before acting)
- Tasks requiring cross-referencing information from multiple sources

**For tool designers**: When building MCP servers or skills, design tool descriptions that encourage Claude to use the think tool between critical steps. See [Writing Effective Tools for Agents](https://www.anthropic.com/engineering/writing-effective-tools-for-agents).

---

## Complementary Tools

Beyond AI coding agents, these tools integrate with development workflows for specific tasks:

### Browser Automation

#### Claude in Chrome (Beta) vs Playwright

Claude Code offers a "Claude in Chrome" feature (via Chrome extension) that enables browser control directly from the CLI. However, **this feature is still in Beta** and not recommended for production workflows.

| Aspect | Claude in Chrome | Playwright |
|--------|-----------------|------------|
| **Maturity** | Beta (December 2025) | Production-ready (5+ years) |
| **Reliability** | Experimental, evolving | Battle-tested, stable APIs |
| **Documentation** | Limited | Comprehensive |
| **Community** | Emerging | Large, established |
| **CI/CD Integration** | Not designed for | First-class support |
| **Cross-browser** | Chrome only | Chrome, Firefox, Safari, Edge |
| **Debugging** | Limited tooling | Trace viewer, codegen, inspector |

**Recommendation**: Use **Playwright** for browser automation until Claude in Chrome matures and thought leaders in the AI coding space validate it for production use.

#### Playwright Integration

```bash
# Install
npm init playwright@latest

# Or with Python
pip install playwright
playwright install
```

**Use Cases with Claude Code**:
- Web scraping for research tasks
- E2E testing automation
- Screenshot capture for documentation
- Form filling and data entry automation

**Pattern**: Claude Code generates Playwright scripts, which execute in a controlled browser context:

```python
# Claude Code can generate and execute this
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://example.com")
    # Automated interactions...
    browser.close()
```

**Why This Works Better**:
1. **Separation of concerns** - Claude reasons, Playwright executes
2. **Reproducibility** - Scripts can be version-controlled and rerun
3. **Debugging** - Playwright's tooling helps diagnose failures
4. **No beta dependencies** - Production reliability from day one

### AI Image Generation

#### google-image-gen-api-starter
- **Repository**: https://github.com/AI-Engineer-Skool/google-image-gen-api-starter
- **Key Feature**: CLI for Gemini image generation with style templates
- **API**: Google Gemini (gemini-3-pro-image-preview)
- **Best For**: Documentation assets, visual prototypes, automated asset pipelines

**Quick Start**:
```bash
# Install
git clone https://github.com/AI-Engineer-Skool/google-image-gen-api-starter
cd google-image-gen-api-starter
uv sync

# Configure
cp .env.example .env
# Add GOOGLE_AI_API_KEY from https://aistudio.google.com/apikey

# Generate
uv run python main.py output.png "A 3D diagram of microservices architecture"
```

**Style Templates**: Reusable prompt templates in `styles/*.md` ensure visual consistency across generated assets.

**Pattern**: See [AI Image Generation](./ai-image-generation.md) for comprehensive integration guidance.

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
- [Safety and Sandboxing](./safety-and-sandboxing.md) - Security across tools
- [Agent Evaluation](./agent-evaluation.md) - Evaluating AI coding tool effectiveness

---

## Sources

- [Aider](https://github.com/paul-gauthier/aider) - Git-centric AI coding
- [OpenHands](https://github.com/All-Hands-AI/OpenHands) - Dockerized agents
- [Goose](https://github.com/block/goose) - Extensible local agent
- [Cursor](https://cursor.sh) - AI-native IDE
- [Playwright](https://playwright.dev) - Browser automation (recommended over Claude in Chrome Beta)
- [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)
- [The Think Tool](https://www.anthropic.com/engineering/claude-think-tool) (March 2025)
- [Writing Effective Tools for Agents](https://www.anthropic.com/engineering/writing-effective-tools-for-agents) (September 2025)

*Last updated: February 2026*

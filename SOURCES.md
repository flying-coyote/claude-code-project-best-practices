# Sources and References

All patterns in this repository are derived from authoritative sources and production-validated implementations.

## Primary Sources (Tier A)

### Anthropic Engineering Blog

#### Long-Running Agent Harness Patterns
- **Title**: "Effective harnesses for long-running agents"
- **Source**: Anthropic Engineering Blog
- **Date**: November 2025
- **URL**: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- **Key Insights**:
  - External artifacts become the agent's memory
  - "Verify before work" startup protocol
  - One feature at a time to prevent context exhaustion
  - Git as recovery mechanism
  - Structured task lists (JSON over markdown)

#### Advanced Tool Use Patterns
- **Title**: "Introducing advanced tool use on the Claude Developer Platform"
- **Source**: Anthropic Developer Blog
- **Date**: November 24, 2025
- **URL**: https://www.anthropic.com/engineering/advanced-tool-use
- **Beta Header**: `advanced-tool-use-2025-11-20`
- **Key Insights**:
  - Tool Search Tool: 85% token reduction
  - Programmatic Tool Calling: 37% token reduction
  - Input examples: 72% → 90% accuracy improvement

### Claude Code Documentation
- **Source**: Anthropic Official Documentation
- **URL**: https://docs.anthropic.com/en/docs/claude-code
- **Topics Used**:
  - CLAUDE.md file format
  - Settings and hooks configuration
  - Slash commands structure
  - Skills system

---

## Secondary Sources (Tier B)

### Claude Code Best Practices
- **Title**: "Claude Code: Best practices for agentic coding"
- **Source**: Anthropic Engineering
- **URL**: https://www.anthropic.com/engineering/claude-code-best-practices
- **Key Insights**:
  - Project context importance
  - Effective prompting patterns
  - Common pitfalls to avoid

### Community Skills and Patterns
- **Source**: Claude Code community discussions
- **Topics**:
  - Skill organization patterns
  - Hook implementation strategies
  - Cross-project consistency approaches

### Agent Skills Open Standard
- **Title**: "Equipping agents for the real world with Agent Skills"
- **Source**: Anthropic Engineering
- **Date**: December 2025
- **URL**: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- **Specification**: https://agentskills.io
- **Key Insights**:
  - Agent Skills released as open standard
  - Adopted by OpenAI for Codex CLI and ChatGPT
  - Cross-platform portability for skills

---

## Spec-Driven Development Frameworks (Tier B)

These frameworks represent the emerging discipline of spec-driven development for AI coding agents:

### GitHub Spec Kit
- **Author**: GitHub
- **URL**: https://github.com/github/spec-kit
- **Stars**: 59,000+ (as of Jan 2026)
- **License**: MIT
- **Description**: Tool-agnostic toolkit for spec-driven development with AI coding agents
- **Key Concepts**:
  - 4-phase workflow: Specify → Plan → Tasks → Implement
  - Constitution command for project governing principles
  - Supports 16+ coding agents including Claude Code
- **Pattern**: [Spec-Driven Development](patterns/spec-driven-development.md)
- **Evidence Tier**: B (Major vendor, widely adopted)

### BMAD Method
- **Author**: Brian (BMad) Madison
- **URL**: https://github.com/bmad-code-org/BMAD-METHOD
- **License**: MIT
- **Description**: Multi-agent methodology with 19+ specialized AI agents for full project lifecycle
- **Key Concepts**:
  - Agent-as-Code paradigm (agents as markdown files)
  - Two-phase approach: Agentic Planning + Context-Engineered Development
  - Scale-Adaptive Intelligence
  - Document Sharding for token optimization
- **Claude Code Port**: https://github.com/24601/BMAD-AT-CLAUDE
- **Pattern**: [Spec-Driven Development](patterns/spec-driven-development.md)
- **Evidence Tier**: C (Community-driven, MIT licensed)

### Kiro (AWS)
- **Author**: Amazon Web Services
- **URL**: https://kiro.dev
- **Launch**: July 2025 (AWS Summit NYC)
- **Description**: VS Code-based IDE with spec-driven development built-in
- **Key Concepts**:
  - Three spec files: requirements.md, design.md, tasks.md
  - Agent Hooks for event-driven automation
  - MCP integration for multimodal context
- **Analysis**: [InfoQ Coverage](https://www.infoq.com/news/2025/08/aws-kiro-spec-driven-agent/)
- **Pattern**: [Spec-Driven Development](patterns/spec-driven-development.md)
- **Evidence Tier**: B (Major vendor implementation)

### ThoughtWorks Analysis
- **Title**: "Spec-driven development: Unpacking one of 2025's key new AI-assisted engineering practices"
- **Source**: ThoughtWorks Insights
- **URL**: https://www.thoughtworks.com/en-us/insights/blog/agile-engineering-practices/spec-driven-development-unpacking-2025-new-engineering-practices
- **Key Insights**:
  - SDD as one of 2025's most significant practices
  - Challenges with agent instruction following
  - Balance between structure and agility
- **Evidence Tier**: B (Industry analyst)

---

## Foundational Influences (Tier B)

These sources directly influenced the design of the skill structure and project scaffolding patterns in this repository:

### Nate B. Jones - AI Implementation Patterns
- **Author**: Nate B. Jones
- **Substack**: https://natesnewsletter.substack.com
- **Website**: https://www.natebjones.com/
- **Description**: AI strategist and former Head of Product at Amazon Prime Video. Created the "Memory Prompts" methodology and extensive documentation of AI implementation patterns from 100+ production builds.

#### Key Articles (used in this repo)

| Article | Pattern | Key Insights |
|---------|---------|--------------|
| [Beyond the Perfect Prompt](https://natesnewsletter.substack.com/p/beyond-the-perfect-prompt-the-definitive) | [Context Engineering](../patterns/context-engineering.md) | Deterministic vs probabilistic context, correctness over compression |
| [2025 Agent Build Bible](https://natesnewsletter.substack.com/p/why-your-ai-breaks-in-production) | [Agent Principles](../patterns/agent-principles.md) | 6 principles for production AI, semantic validation |
| [MCP Implementation Guide](https://natesnewsletter.substack.com/p/the-mcp-implementation-guide-solving) | [MCP Failure Modes](../patterns/mcp-failure-modes.md) | 7 failure modes, Intelligence Layer/Sidecar/Batch patterns |
| Million-Dollar Workflows in 10 Minutes | Skills structure | IDENTITY/GOAL/STEPS/OUTPUT skill format |

#### Core Concepts

- **Memory Prompts Methodology**
  - 4-Prompt System: Memory Architecture Designer, Context Library Builder, Project Brief Compiler, Retrieval Strategy Planner
  - Lifecycle-Aware Context: PERMANENT/EVERGREEN/PROJECT-SCOPED/SESSION-SCOPED information types
  - Retrieval Strategy: Task-type-based patterns (planning/execution/review modes)
  - Fact vs Assumption Separation: Distinguishing confirmed facts from working assumptions

- **Context Engineering**
  - Two-layer architecture: deterministic (user-controlled) vs probabilistic (AI-discovered)
  - "Correctness trumps compression" - semantic relevance over token efficiency
  - Semantic highway design for guided AI discovery

- **Production AI Principles**
  - AI violates assumptions so fundamental we don't realize we're making them
  - Hybrid architecture: traditional systems for trust, AI for intelligence
  - Monitoring lies: traditional metrics miss semantic failures

- **MCP Integration**
  - 300-800ms baseline latency makes MCP unsuitable for transaction paths
  - Intelligence Layer pattern: background analysis, not real-time execution
  - ~43% of MCP servers have security vulnerabilities

- **Influence on This Repo**: Skill structure, context patterns, and three pattern files derive from Nate B. Jones' work

### Daniel Miessler - Fabric Framework & PAI (Personal AI Infrastructure)
- **Author**: Daniel Miessler
- **GitHub**: https://github.com/danielmiessler/fabric
- **Website**: https://danielmiessler.com
- **Description**: Security professional and creator of Fabric, an open-source framework for augmenting humans using AI with 200+ reusable patterns
- **Key Concepts**:
  - **"Solve Once, Reuse Forever"**: Modular, reusable prompt patterns
  - **Scaffolding > Models**: "The scaffolding matters more. Building great scaffolding requires tons of user empathy."
  - **Spec-Driven Development**: Structured project evolution with clear specifications
  - **Pattern Structure**: IDENTITY/GOAL/STEPS/OUTPUT format for systematic prompt engineering
  - **PAI (Personal AI Infrastructure)**: Multi-workflow architecture for complex skills
    - Kebab-case naming convention for workflows
    - Routing document pattern (SKILL.md as dispatcher)
    - Progressive disclosure through conditional workflow loading
    - Workflow size guidelines (200-500 lines optimal)
- **Influence on This Repo**:
  - Skill template structure directly adapted from Fabric patterns
  - Philosophy of modular, composable AI behaviors
  - Evidence-based approach to AI augmentation
  - Multi-workflow pattern for complex skills (ultrathink-analyst, git-workflow-helper examples)
  - Kebab-case naming standard for workflow files

---

## Community Skill Sources (Tier C)

These community repositories provide additional examples and inspiration for Claude skills:

### Fabric Framework (Implementation Reference)
- **URL**: https://github.com/danielmiessler/fabric
- **Description**: 200+ battle-tested patterns from 300+ contributors
- **Relevance**: Reference implementation for pattern structure and composability

### Agent OS (Spec-Driven Framework)
- **Author**: Brian Casel (BuilderMethods)
- **URL**: https://github.com/buildermethods/agent-os
- **Description**: Spec-driven development framework that "transforms AI coding agents from confused interns into productive developers"
- **Key Concepts**:
  - Specification-driven methodology for AI agents
  - Structured project configuration (YAML-based)
  - Technology choices and codebase-specific standards
  - Works with Claude Code, Cursor, and other AI assistants
- **Relevance**: Influenced project scaffolding approach and spec-driven philosophy

### obra/superpowers
- **URL**: https://github.com/obra/superpowers
- **Description**: Curated collection of AI-assisted development patterns
- **Relevance**: Examples of skill-like behaviors for coding workflows

### awesome-claude-skills
- **Author**: BehiSecc
- **URL**: https://github.com/BehiSecc/awesome-claude-skills
- **Description**: Curated list of 40+ Claude skills across 10 categories
- **Categories**: Document skills, Development tools, Data analysis, Scientific research, Writing, Learning, Media, Collaboration, Security, Automation
- **Relevance**: Community skill discovery and categorization reference

### Cybersecurity AI (CAI)
- **Author**: Alias Robotics
- **URL**: https://github.com/aliasrobotics/cai
- **Description**: Open-source framework for AI-powered security automation with 300+ model integrations
- **Key Features**:
  - Agent-based architecture for security tasks
  - Built-in reconnaissance, exploitation, and privilege escalation tools
  - Guardrails against prompt injection
  - Battle-tested in CTFs and bug bounties
- **Relevance**: Reference for security-focused AI agent patterns and guardrails

### RAPTOR (Recursive Autonomous Penetration Testing and Observation Robot)
- **Author**: gadievron
- **URL**: https://github.com/gadievron/raptor
- **Description**: AI-powered security testing platform built on Claude Code that automates offensive and defensive security research
- **Key Features**:
  - Static analysis with Semgrep and CodeQL (dataflow validation)
  - Binary fuzzing with AFL++
  - LLM-driven vulnerability analysis and exploit generation
  - Automated patch development for identified vulnerabilities
  - GitHub forensics for evidence-backed repository investigations
  - Multi-LLM support (Claude, GPT-4, Gemini)
- **Relevance**: Reference implementation for Claude Code in security automation, demonstrates modular security tool integration with AI reasoning

### Claude Code Templates (aitmpl.com)
- **Author**: Daniel Avila (davila7)
- **URL**: https://github.com/davila7/claude-code-templates
- **Website**: https://www.aitmpl.com
- **NPM**: https://www.npmjs.com/package/claude-code-templates
- **Description**: CLI tool providing 400+ ready-to-use components for Claude Code including 100+ agents, 159+ commands, hooks, MCPs, and project templates
- **Key Features**:
  - Pre-built agents for common workflows (frontend-developer, code-reviewer, security-auditor)
  - MCP integrations for GitHub, PostgreSQL, Stripe, AWS
  - Progressive disclosure skills for PDF/Excel workflows
  - Analytics dashboard and conversation monitoring tools
  - Component attribution from wshobson/agents (48 agents, MIT) and awesome-claude-code (21 commands)
- **Installation**: `npx claude-code-templates@latest`
- **Stars**: 12.6k+ (as of Dec 2025)
- **Relevance**: Ready-to-use implementations of patterns documented in this repository; complementary resource for users who want pre-built components rather than building from scratch

### Anthropic Official Skills Examples
- **URL**: https://github.com/anthropics/skills
- **Description**: Official skill examples from Anthropic
- **Relevance**: Reference implementation patterns

### Simon Willison's Analysis
- **URL**: https://simonwillison.net/2025/Oct/16/claude-skills/
- **Description**: Technical analysis of Claude skills system
- **Relevance**: Deep dive into how skills work and best practices; key insight that skills may be bigger than MCP due to simplicity

### Plugins and Extensions Comparison Sources
- **IntuitionLabs**: https://intuitionlabs.ai/articles/claude-skills-vs-mcp
  - Technical comparison of Skills vs MCP
  - Key insight: "MCP provides connectivity; Skills provide methodology"
- **alexop.dev**: https://alexop.dev/posts/understanding-claude-code-full-stack/
  - Full stack explanation: MCP, Skills, Subagents, Hooks
  - Decision framework for when to use each extension mechanism
- **Composio**: https://composio.dev/blog/claude-code-plugin
  - Practical guide to Claude Code plugins
  - Plugin structure and best practices
- **awesome-claude-code-plugins**: https://github.com/ccplugins/awesome-claude-code-plugins
  - Curated list of community plugins, slash commands, subagents, MCP servers, hooks

### Security-Specific Sources
- **MITRE ATT&CK**: https://attack.mitre.org/
  - Foundation for threat-model-reviewer and detection-rule-reviewer skills
- **Sigma Rules Project**: https://github.com/SigmaHQ/sigma
  - Reference for detection rule patterns
- **OWASP Threat Modeling**: https://owasp.org/www-community/Threat_Modeling
  - Methodology basis for threat modeling skills

---

## Claude Code Best Practices Repositories (Tier C)

These repositories provide community-maintained best practices and should be periodically reviewed to ensure this project remains current:

### Curated Lists (Primary Review Sources)

| Repository | Stars | Focus | Review Priority |
|------------|-------|-------|-----------------|
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | 18k+ | Commands, workflows, patterns | HIGH |
| [jqueryscript/awesome-claude-code](https://github.com/jqueryscript/awesome-claude-code) | - | Tools, IDE integrations, frameworks | HIGH |
| [josix/awesome-claude-md](https://github.com/josix/awesome-claude-md) | - | CLAUDE.md examples and patterns | HIGH |
| [ccplugins/awesome-claude-code-plugins](https://github.com/ccplugins/awesome-claude-code-plugins) | - | Plugins, commands, hooks | MEDIUM |
| [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | - | Skills resources and tools | MEDIUM |

### Best Practices Repositories

| Repository | Author | Description |
|------------|--------|-------------|
| [awattar/claude-code-best-practices](https://github.com/awattar/claude-code-best-practices) | awattar | Patterns and examples for Claude Code integration |
| [anuraag2601/claude-code-best-practices](https://github.com/anuraag2601/claude-code-best-practices) | anuraag2601 | Battle-tested practices from real projects |
| [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | ykdojo | 40+ tips including status line, system prompt optimization |
| [Cranot/claude-code-guide](https://github.com/Cranot/claude-code-guide) | Cranot | Comprehensive guide to Claude Code features |
| [zebbern/claude-code-guide](https://github.com/zebbern/claude-code-guide) | zebbern | Tips, tricks, optimization, hidden commands |
| [jmckinley/claude-code-resources](https://github.com/jmckinley/claude-code-resources) | jmckinley | Production agents, templates, 100+ workflows |

### Template and Configuration Repositories

| Repository | Description |
|------------|-------------|
| [centminmod/my-claude-code-setup](https://github.com/centminmod/my-claude-code-setup) | Starter template with memory bank system |
| [ruvnet/claude-flow](https://github.com/ruvnet/claude-flow/wiki/CLAUDE-MD-Templates) | CLAUDE.md templates for different project types |
| [ArthurClune/claude-md-examples](https://github.com/ArthurClune/claude-md-examples) | Sample CLAUDE.md files |

### Cross-Platform AI Coding Resources

| Repository | Description |
|------------|-------------|
| [instructa/ai-prompts](https://github.com/instructa/ai-prompts) | Prompts for Cursor, CLINE, Windsurf, Copilot |
| [Bhartendu-Kumar/rules_template](https://github.com/Bhartendu-Kumar/rules_template) | Cross-platform rules for multiple AI assistants |
| [obviousworks/vibe-coding-ai-rules](https://github.com/obviousworks/vibe-coding-ai-rules) | AI-optimized rules for Windsurf, Cursor |
| [nibzard/awesome-agentic-patterns](https://github.com/nibzard/awesome-agentic-patterns) | Curated catalogue of agentic AI patterns |

### Agentic Development Frameworks

| Repository | Description |
|------------|-------------|
| [microsoft/autogen](https://github.com/microsoft/autogen) | Programming framework for agentic AI |
| [e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) | List of AI autonomous agents |
| [panaversity/learn-agentic-ai](https://github.com/panaversity/learn-agentic-ai) | Agentic AI learning with DACA design pattern |

### Review Cadence

| Source Type | Review Frequency |
|-------------|------------------|
| Anthropic Engineering Blog | Weekly |
| awesome-claude-code lists | Monthly |
| Best practices repositories | Monthly |
| SDD frameworks (Spec Kit, BMAD) | Quarterly |
| Cross-platform resources | Quarterly |

---

## Production Validation (Tier B)

These patterns have been validated across 12+ production projects:

### flying-coyote/second-brain
- **Author**: Jeremy (flying-coyote)
- **Repository**: https://github.com/flying-coyote/second-brain
- **Description**: Production cybersecurity research knowledge management system with advanced Claude Code infrastructure
- **Key Contributions to This Repo**:
  - **Progressive Disclosure Pattern**: 73% average token reduction across 4 production skills
  - **Multi-Workflow Refactoring**: 3 large skills refactored to multi-workflow structure (Dec 2025)
    - ultrathink-analyst: 748 lines → 957 lines (4 files, 3 workflows)
    - git-workflow-helper: 587 lines → 2,216 lines (6 files, 5 workflows)
    - academic-citation-manager: 534 lines → 1,503 lines (5 files, 4 workflows)
    - Benefit: Conditional workflow loading (only load relevant operation)
  - **Dual Evidence Tier System**: Tier 1-5 (research evidence) + Tier A-D (source quality)
  - **MITRE ATLAS Security Mapping**: Adversarial ML technique mapping for skills security
  - **Confidence Scoring Methodology**: HIGH/MEDIUM/LOW assessment framework
  - **ADR Framework for Research**: Architecture Decision Records adapted for hypothesis-driven work
- **Production Metrics**:
  - 21 Claude skills across 9 repositories (6 personal + 15 project-specific)
  - 12 new workflow files created in multi-workflow refactoring
  - 46 hypotheses tracked with confidence scoring
  - 25+ documented contradictions resolved via ADRs
  - 70+ pre-approved tool patterns for friction reduction
  - 5-layer defense for HIGH RISK skills (external document processing)
  - Average workflow size: ~300 lines (optimal maintainability)
- **Validation Scope**:
  - Software development projects (4)
  - Content creation (blog, book manuscript)
  - Research projects (literature review, hypothesis validation)
  - Government partnership (CISA collaboration)
- **Evidence Tier**: B (Production-validated implementations with measured outcomes)
- **Relevance**: Primary source for progressive disclosure, multi-workflow pattern, confidence scoring, and security patterns in this repository

---

### Project Categories Tested
1. **Software Development** (4 projects)
   - Python libraries
   - TypeScript applications
   - Docker-based tools
   - MCP servers

2. **Content Creation** (3 projects)
   - Technical book (115,500 words)
   - Blog platform
   - Documentation sites

3. **Research Projects** (3 projects)
   - Literature reviews
   - Hypothesis tracking systems
   - Standards development (ITU-T)

4. **Government/Enterprise** (2 projects)
   - CISA collaboration (government partnership)
   - Enterprise security analysis

### Validation Metrics
- **Setup time**: Reduced from 2+ hours to ~15 minutes
- **Context retention**: Improved across session boundaries
- **Consistency**: 90%+ adherence to project standards
- **Maintenance**: Minimal ongoing overhead

---

## Evidence Tier Definitions

This repository uses a tiered evidence system:

### Tier A: Primary Sources
- Direct from Anthropic (engineering blog, documentation)
- Official specifications and standards
- First-party production data

### Tier B: Validated Secondary
- Peer-reviewed or expert-validated
- Production-tested implementations
- Industry-accepted practices

### Tier C: Industry Knowledge
- Vendor documentation
- Community best practices
- Analyst reports

### Tier D: Opinions/Speculation
- Personal experience
- Theoretical projections
- Unvalidated claims

**This repository primarily uses Tier A and B sources.**

---

## How to Verify Sources

All URLs in this document are publicly accessible. To verify:

1. **Anthropic Blog Posts**: Visit the URL directly
2. **Documentation**: Check docs.anthropic.com
3. **Production Validation**: Patterns derived from private repositories, methodology documented

---

## Citing This Repository

If you reference these patterns:

```
Claude Code Project Best Practices
https://github.com/flying-coyote/claude-code-project-best-practices
Based on Anthropic Engineering patterns (November 2025)
```

---

## Updates

This sources document is updated when:
- New Anthropic patterns are released
- Additional production validation is completed
- Community contributions add new references

*Last updated: January 2026*

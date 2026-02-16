# Sources and References

All patterns in this repository are derived from authoritative sources and production-validated implementations.

**Quick Lookup**: For the top 20 most-referenced sources, see [SOURCES-QUICK-REFERENCE.md](SOURCES-QUICK-REFERENCE.md) (100 lines vs 1,278 here)

## Primary Sources (Tier A)

### Boris Cherny (Claude Code Creator)

**Role**: Engineering Manager at Anthropic, creator of Claude Code
**Interview Sources**:
- [Paddo.dev: How Boris Uses Claude Code](https://paddo.dev/blog/how-boris-uses-claude-code/) (January 2026)
- [VentureBeat: Creator of Claude Code Workflow](https://venturebeat.com/technology/the-creator-of-claude-code-just-revealed-his-workflow-and-developers-are) (January 2026)
- [Anthropic Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)

**Key Workflow Insights**:
1. **Parallel Sessions**: Run 5 terminal instances + 5-10 web sessions simultaneously
2. **Opus 4.6 (latest)**: Use for all tasks—agent teams, 1M context, adaptive thinking
3. **CLAUDE.md as Team Memory**: Update multi-weekly, capture mistakes as they happen
4. **Plan Mode First**: Always for non-trivial work
5. **Natural Language Git**: "commit and push" works without custom commands (per official guidance, avoid complex slash command lists)
6. **PostToolUse Auto-Formatting**: Run formatters (prettier, black) after Write
7. **Pre-Allow Permissions**: `/permissions` to allow `bun run build:*`, `bun run test:*`
8. **MCP for External Tools**: When native tools insufficient
9. **Verification = 2-3x Quality**: Subagent verification before finalizing
10. **Background Agents**: Stop hooks to avoid lost work
11. **GitHub Actions + @.claude**: Trigger Claude from CI/CD
12. **Skip Exotic Customization**: Standard patterns over novel approaches

**Pattern References**: [Parallel Sessions](patterns/parallel-sessions.md), [Subagent Orchestration](patterns/subagent-orchestration.md), [Documentation Maintenance](patterns/documentation-maintenance.md), [GitHub Actions Integration](patterns/github-actions-integration.md)
**Evidence Tier**: A (Primary vendor/creator)

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

### Claude Code Documentation (Canonical)
- **Source**: Anthropic Official Documentation
- **URL**: https://code.claude.com/docs/en/best-practices (Canonical - January 2026)
- **Legacy URL**: https://docs.anthropic.com/en/docs/claude-code (redirects to above)
- **Evidence Tier**: A (Primary vendor documentation)
- **Key Guidance**:
  - CLAUDE.md should be concise (~60 lines recommended)
  - Skills should be minimal ("Would removing this cause mistakes? If not, cut it.")
  - Avoid long lists of custom slash commands (anti-pattern)
  - Include verification (tests, linting) as highest-leverage practice
  - Use hooks sparingly; prefer pre-approved permissions
- **Topics Used**:
  - CLAUDE.md file format
  - Settings and hooks configuration
  - Slash commands structure
  - Skills system

### Claude Code Changelog
- **Source**: Anthropic GitHub Repository
- **URL**: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- **Releases**: https://github.com/anthropics/claude-code/releases
- **Key Updates Referenced** (as of February 2026):
  - v2.1.37 (current): Agent teams (experimental), automatic session memory, PDF page ranges in Read tool, "Summarize from here" via /rewind, skills from --add-dir, remote sessions in VS Code, OAuth for MCP servers
  - v2.1.3: Unified slash commands and skills, permission rule detection in /doctor, 10-minute hook timeout
  - v2.1.0: Skill hot-reload, context forking, skill-level hooks, wildcard permissions, subagent resumption, real-time steering, MCP list_changed notifications
  - v2.0.76: LSP tool (go-to-definition, find references, hover)
  - v2.0.60: Background agent support
- **Model Updates**:
  - Opus 4.6 (February 5, 2026): 1M token context, agent teams, adaptive reasoning, data residency controls
  - Opus 4.5 (November 24, 2025): 67% price reduction to $5/$25 per million tokens
  - Sonnet 4.5 (September 29, 2025): Agent-first design, Agent SDK support
  - Haiku 4.5 (October 2025): Extended thinking support, 1/3 cost of Sonnet
- **Pattern References**: [Advanced Hooks](patterns/advanced-hooks.md), [Skills README](skills/README.md), [Subagent Orchestration](patterns/subagent-orchestration.md), [Plugins and Extensions](patterns/plugins-and-extensions.md)

#### Context Engineering for AI Agents
- **Title**: "Effective context engineering for AI agents"
- **Source**: Anthropic Engineering Blog
- **Date**: September 2025
- **URL**: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- **Key Insights**:
  - Context engineering supersedes prompt engineering for agents
  - Context rot: accuracy decreases as token count increases
  - Iterative context curation during inference cycles
  - 54% benchmark gains from scratchpad techniques
  - Three mitigation strategies: compaction, structured notes, sub-agent architectures
  - Memory Tool + Context Editing: 39% improvement in agent search performance
  - Token consumption reduction: 84% in 100-round web search
- **Pattern**: [Context Engineering](patterns/context-engineering.md)

#### Agent Skills for Real-World Applications
- **Title**: "Equipping agents for the real world with Agent Skills"
- **Source**: Anthropic Engineering Blog
- **Date**: January 2026
- **URL**: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- **Key Insights**:
  - Skills are organized folders of instructions, scripts, and resources
  - Progressive disclosure is the core design principle
  - Published as open standard for cross-platform portability
  - Skills extend Claude's capabilities into domain-specific expertise
- **Pattern**: [Plugins and Extensions](patterns/plugins-and-extensions.md), [Progressive Disclosure](patterns/progressive-disclosure.md)

#### The Complete Guide to Building Skills for Claude
- **Title**: "The Complete Guide to Building Skills for Claude"
- **Source**: Anthropic (PDF guide)
- **Date**: January 2026
- **URL**: https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf
- **Key Insights**:
  - YAML frontmatter field reference: name, description (required), allowed-tools, license, compatibility, metadata (optional)
  - Description formula: [What it does] + [When to use it] + [Key capabilities], include trigger phrases
  - Security restrictions: No XML angle brackets in frontmatter, no "claude"/"anthropic" in skill names
  - Three skill categories: Document & Asset Creation, Workflow Automation, MCP Enhancement
  - Success metrics: 90% trigger accuracy, 0 failed API calls, workflow completion without user correction
  - Five workflow patterns: Sequential orchestration, Multi-MCP coordination, Iterative refinement, Context-aware tool selection, Domain-specific intelligence
  - Problem-first vs. tool-first design heuristic for skill framing
  - SKILL.md hard ceiling: 5,000 words; move detailed docs to references/
  - Negative triggers in descriptions to prevent over-triggering
  - Debugging approach: Ask Claude "When would you use the [skill name] skill?"
  - Model laziness mitigation more effective in user prompts than SKILL.md
  - Skill packs for 20-50+ simultaneous skills
  - Skills API: `/v1/skills` endpoint, `container.skills` Messages API parameter
- **Patterns**: [Skills Domain Knowledge](patterns/skills-domain-knowledge.md), [Progressive Disclosure](patterns/progressive-disclosure.md), [Agent Evaluation](patterns/agent-evaluation.md), [Plugins and Extensions](patterns/plugins-and-extensions.md)

#### Claude Agent SDK
- **Title**: "Building agents with the Claude Agent SDK"
- **Source**: Anthropic Engineering Blog
- **Date**: January 2026
- **URL**: https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk
- **Key Insights**:
  - Claude Code SDK renamed to Claude Agent SDK (broader vision)
  - Subagents are first-class: Explore, Plan, general-purpose built-in
  - Plugins bundle skills + hooks + MCP servers
  - Supports context forking for isolated subagent execution
- **Pattern**: [Subagent Orchestration](patterns/subagent-orchestration.md)

#### Code Execution with MCP
- **Title**: "Code execution with MCP: building more efficient AI agents"
- **Source**: Anthropic Engineering Blog
- **Date**: 2026
- **URL**: https://www.anthropic.com/engineering/code-execution-with-mcp
- **Key Insights**:
  - Load tools on demand for context efficiency
  - Filter data before it reaches the model
  - Execute complex logic in a single step
  - Security and state management benefits
- **Pattern**: [MCP Patterns](patterns/mcp-patterns.md)

#### The Think Tool
- **Title**: "The think tool: Enabling Claude to stop and think"
- **Source**: Anthropic Engineering Blog
- **Date**: March 20, 2025
- **URL**: https://www.anthropic.com/engineering/claude-think-tool
- **Key Insights**:
  - Tool that lets Claude pause mid-response to verify information before proceeding
  - 54% relative improvement on complex policy-following tasks
  - Different from extended thinking (which happens before response generation)
  - Valuable in complex multi-step tool chains
- **Pattern**: [Tool Ecosystem](patterns/tool-ecosystem.md)

#### Building a C Compiler with Parallel Claudes
- **Title**: "Building a C compiler with a team of parallel Claudes"
- **Source**: Anthropic Engineering Blog
- **Date**: February 5, 2026
- **URL**: https://www.anthropic.com/engineering/building-a-c-compiler-with-parallel-claudes
- **Key Insights**:
  - 16 agents wrote a Rust-based C compiler (100,000 lines)
  - Nearly 2,000 sessions, ~$20,000 API cost
  - Capable of compiling the Linux kernel on x86, ARM, and RISC-V
  - Agent teams stress test demonstrating multi-agent coordination at scale
- **Pattern**: [Subagent Orchestration](patterns/subagent-orchestration.md)

#### Quantifying Infrastructure Noise in Agentic Coding Evals
- **Title**: "Quantifying infrastructure noise in agentic coding evals"
- **Source**: Anthropic Engineering Blog
- **Date**: February 2026
- **URL**: https://www.anthropic.com/engineering/quantifying-infrastructure-noise-in-agentic-coding-evals
- **Key Insights**:
  - Infrastructure noise is a significant confounder in agentic coding evaluations
  - Non-deterministic environments affect eval reliability
  - Methodology for isolating infrastructure effects from model capability
- **Pattern**: [Agent Evaluation](patterns/agent-evaluation.md)

#### Designing AI-Resistant Technical Evaluations
- **Title**: "Designing AI-resistant technical evaluations"
- **Source**: Anthropic Engineering Blog
- **Date**: January 21, 2026
- **URL**: https://www.anthropic.com/engineering/designing-ai-resistant-technical-evaluations
- **Key Insights**:
  - Principles for evaluations that remain valid as AI capabilities improve
  - Avoiding benchmark saturation and gaming
  - Designing for measurement of genuine capability
- **Pattern**: [Agent Evaluation](patterns/agent-evaluation.md)

#### Demystifying Evals for AI Agents
- **Title**: "Demystifying evals for AI agents"
- **Source**: Anthropic Engineering Blog
- **Date**: January 9, 2026
- **URL**: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- **Key Insights**:
  - 8 evaluation patterns for agents
  - Start with 20-50 tasks derived from real failures
  - Practical checklist for building agent evals
  - Evaluation design principles
- **Pattern**: [Agent Evaluation](patterns/agent-evaluation.md)

#### Beyond Permission Prompts: Making Claude Code More Secure
- **Title**: "Beyond permission prompts: making Claude Code more secure"
- **Source**: Anthropic Engineering Blog
- **Date**: October 20, 2025
- **URL**: https://www.anthropic.com/engineering/beyond-permission-prompts
- **Key Insights**:
  - OS-level sandboxing (bubblewrap on Linux, seatbelt on macOS)
  - 84% reduction in permission prompts through sandboxing
  - Complementary to hooks-based security, not a replacement
  - Open-sourced sandboxing implementation
- **Pattern**: [Safety and Sandboxing](patterns/safety-and-sandboxing.md)

#### Writing Effective Tools for Agents
- **Title**: "Writing effective tools for agents -- with agents"
- **Source**: Anthropic Engineering Blog
- **Date**: September 11, 2025
- **URL**: https://www.anthropic.com/engineering/writing-effective-tools-for-agents
- **Key Insights**:
  - Tool design for non-deterministic users (AI agents)
  - Clear, unambiguous tool descriptions
  - Input validation and error messaging designed for AI consumption
  - Agent-tested tool refinement methodology
- **Pattern**: [Tool Ecosystem](patterns/tool-ecosystem.md)

#### How We Built Our Multi-Agent Research System
- **Title**: "How we built our multi-agent research system"
- **Source**: Anthropic Engineering Blog
- **Date**: June 13, 2025
- **URL**: https://www.anthropic.com/engineering/how-we-built-our-multi-agent-research-system
- **Key Insights**:
  - Multi-agent architecture for research tasks
  - Lead/worker agent coordination patterns
  - Parallel research with result synthesis
  - Foundation for Agent Teams feature
- **Pattern**: [Subagent Orchestration](patterns/subagent-orchestration.md)

#### Claude Code Sub-agents
- **Source**: Anthropic Official Documentation
- **URL**: https://docs.anthropic.com/en/docs/claude-code/sub-agents
- **Key Insights**:
  - Specialized subagent types (Explore, Plan, general-purpose)
  - Parallel execution patterns
  - Context isolation for fresh context windows
- **Pattern**: [Subagent Orchestration](patterns/subagent-orchestration.md)

#### Claude Code Hooks Reference
- **Source**: Anthropic Official Documentation
- **URL**: https://docs.anthropic.com/en/docs/claude-code/hooks
- **Key Insights**:
  - PreToolUse input modification (v2.0.10+)
  - PostToolUse output formatting
  - PermissionRequest hooks (v2.0.45+)
  - SubagentStop and SessionEnd hooks
- **Pattern**: [Advanced Hooks](patterns/advanced-hooks.md)

### Coalition for Secure AI (CoSAI) - Project CodeGuard
- **Source**: https://github.com/cosai-oasis/project-codeguard
- **Blog**: https://blogs.cisco.com/ai/cisco-donates-project-codeguard-to-the-coalition-for-secure-ai
- **Date**: February 2026 (donated to CoSAI); originally open-sourced October 2025 by Cisco
- **Type**: Open-source security framework for AI coding agents
- **Evidence Tier**: A (Industry consortium — Anthropic, Google, OpenAI, Microsoft, NVIDIA are CoSAI founding members)
- **Description**: Model-agnostic framework embedding secure-by-default practices into AI coding agent workflows. 23 security rules across 8 domains (cryptography, input validation, authentication, authorization, supply chain, cloud security, platform security, data protection). Includes MCP-specific security rules.
- **Key Contributions**:
  - 3 mandatory rules: hardcoded credentials, cryptographic algorithms, digital certificates
  - Pre-generation / during-generation / post-generation lifecycle model
  - Credential detection patterns (AWS `AKIA*`, Stripe `sk_live_*`, GitHub `ghp_*`, JWT `eyJ*`)
  - Supply chain security (lockfiles, digest pinning, SBOM, deterministic installs)
  - MCP security (SPIFFE/SPIRE workload identity, transport security, tool sandboxing)
  - Integration tools for Cursor, Windsurf, Copilot, Agent Skills, and Claude Code
- **License**: CC BY 4.0 (rules), Apache 2.0 (tools)
- **Governance**: CoSAI Special Interest Group within AI Security Risk Governance Workstream
- **Pattern**: [Secure Code Generation](patterns/secure-code-generation.md)

### OWASP Security Standards

#### OWASP MCP Top 10
- **Source**: OWASP Foundation
- **URL**: https://owasp.org/www-project-mcp-top-10/
- **Date**: 2025
- **Key Risks**:
  - Tool poisoning and rug pull attacks
  - Schema poisoning
  - Memory poisoning
  - Supply chain attacks
- **Pattern**: [MCP Patterns](patterns/mcp-patterns.md)

#### OWASP Guide for Securely Using Third-Party MCP Servers
- **Source**: OWASP GenAI Security Project
- **URL**: https://genai.owasp.org/resource/cheatsheet-a-practical-guide-for-securely-using-third-party-mcp-servers-1-0/
- **Version**: 1.0 (October 2025)
- **Contributors**: ServiceNow, IBM, Google, AWS, SAP, and others
- **Key Insights**:
  - Defense-in-depth checklist for MCP
  - Server verification (version pinning, checksums)
  - OAuth 2.1/OIDC authorization
  - Trusted MCP registry governance
- **Pattern**: [MCP Patterns](patterns/mcp-patterns.md)

### Agent Skills Open Standard
- **Title**: "Agent Skills Specification"
- **Source**: Anthropic (open standard)
- **URL**: https://agentskills.io/specification
- **Repository**: https://github.com/anthropics/skills
- **Key Insights**:
  - Cross-platform skill format (Claude Code, Cursor, VS Code, Codex CLI)
  - Required fields: name, description
  - SKILL.md with YAML frontmatter
  - Progressive disclosure via directory structure
- **Pattern**: [SKILL-TEMPLATE](skills/SKILL-TEMPLATE.md)

---

## Secondary Sources (Tier B)

### GSD (Get Shit Done) Orchestration Framework
- **Author**: glittercowboy
- **URL**: https://github.com/glittercowboy/get-shit-done
- **License**: Open source
- **Description**: Orchestration framework maximizing Claude effectiveness through fresh context per subagent and state externalization
- **Key Concepts**:
  - **Thin Orchestrator**: Coordinates but never implements directly
  - **Fresh Context Per Subagent**: 200K tokens per executor, zero accumulated garbage
  - **STATE.md Pattern**: Persistent memory file for cross-session continuity
  - **XML Task Formatting**: Structured task specs with embedded verification
  - **Six Workflow Phases**: Initialize → Discuss → Plan → Execute → Verify → Complete
  - **.planning/ Directory Structure**: Isolates planning artifacts from source code
  - **Atomic Commits**: One git commit per task
- **Key Quote**: "The orchestrator never does heavy lifting. It spawns agents, waits, integrates results."
- **Pattern**: [GSD Orchestration](patterns/gsd-orchestration.md)
- **Evidence Tier**: B (Open source, production-validated)

### CAII (Cognitive Agent Infrastructure Implementation)
- **Author**: Kristoffer Sketch (skribblez2718)
- **URL**: https://github.com/skribblez2718/caii
- **Description**: Cognitive agent framework with Johari Window methodology for ambiguity surfacing
- **Key Concepts**:
  - **Johari Window Framework**: Four quadrants (Arena/Open, Hidden, Blind Spot, Unknown)
  - **SAAE Protocol**: SHARE → ASK → ACKNOWLEDGE → EXPLORE
  - **7 Cognitive Agents**: Clarification, Research, Analysis, Synthesis, Generation, Validation, Memory/Metacognition
  - **Learning & Memory System**: Task-specific memories with indexed learnings
- **Key Quote**: "Even well-written and well-structured prompts have ambiguity, which stems from the fact 'we don't know what we don't know.'"
- **Patterns**: [Johari Window](patterns/johari-window-ambiguity.md), [Cognitive Agent Infrastructure](patterns/cognitive-agent-infrastructure.md)
- **Evidence Tier**: B (Production implementation, documented methodology)

### Claude-Flow Enterprise Orchestration
- **Author**: ruvnet
- **URL**: https://github.com/ruvnet/claude-flow
- **Description**: Enterprise-scale multi-agent orchestration with 60+ specialized agents
- **Key Concepts**:
  - **Scale**: 60+ specialized agents, 42 pre-built skills, 170+ MCP native tools
  - **SONA Self-Learning**: <0.05ms adaptation, EWC++ prevents knowledge loss
  - **Vector Memory (HNSW)**: 150x-12,500x faster pattern retrieval
  - **6 Swarm Topologies**: Hierarchical, Mesh, Ring, Star, Hybrid, Adaptive
  - **ReasoningBank**: Trajectory storage with semantic pattern matching
- **Performance Claims**: 250% Claude Code usage extension
- **Pattern**: Reference architecture only (see [Framework Selection Guide](patterns/framework-selection-guide.md#claude-flow-reference-only))
- **Evidence Tier**: B (Enterprise-focused documentation)

### MCP Context Budget Analysis
- **Author**: valgard
- **URL**: https://dev.to/valgard/claude-code-must-haves-january-2026-kem
- **Date**: January 2026
- **Description**: Production analysis of MCP tool token consumption in Claude Code
- **Key Insights**:
  - MCP tools can consume 40%+ of context (measured: 81,986 tokens at startup)
  - Sweet spot: 4 plugins + 2 MCPs
  - Recommended core MCPs: Context7 + Sequential Thinking
  - Use `disabledMcpServers` to limit per-project
  - Activate specialized MCPs on-demand, not by default
- **Pattern**: [MCP Patterns](patterns/mcp-patterns.md#mcp-context-budget-management)
- **Evidence Tier**: B (Production measurement, documented methodology)

### Context Rot Deep Dive
- **Author**: Inkeep
- **URL**: https://inkeep.com/blog/fighting-context-rot
- **Date**: January 2026
- **Description**: Analysis of Anthropic's context rot findings with practical mitigations
- **Key Insights**:
  - "Context rot is the degradation of model accuracy as context windows fill up"
  - Transformer architecture struggles with n² relationship growth
  - Three mitigations: compaction, structured notes, sub-agent architectures
  - Memory Tool + Context Editing: 39% improvement
  - 84% token reduction in 100-round web search
- **Pattern**: [Context Engineering](patterns/context-engineering.md#context-rot)
- **Evidence Tier**: B (Analysis of primary source + practitioner validation)

### Recursive Language Models (RLM)
- **Authors**: Alex Zhang, Tim Kraska, Omar Khattab (MIT CSAIL)
- **arXiv**: https://arxiv.org/abs/2512.24601
- **GitHub**: https://github.com/alexzhang13/rlm
- **Blog**: https://alexzhang13.github.io/blog/2025/rlm/
- **Industry Analysis**: [Prime Intellect - "The Paradigm of 2026"](https://www.primeintellect.ai/blog/rlm)
- **Description**: Inference paradigm enabling LLMs to programmatically examine, decompose, and recursively call themselves over context stored as a variable
- **Key Concepts**:
  - **Context Rot**: Performance degradation as context window fills (beyond benchmark capture)
  - **Model-Managed Context**: Context as REPL variable, model decides what to examine
  - **Recursive Decomposition**: Spawns sub-LLM calls on chunks, combines results iteratively
  - **Emergent Behaviors**: Peeking, grepping, partition + map, summarization
- **Benchmark Results**:
  | Benchmark | Standard Approach | RLM Approach | Improvement |
  |-----------|-------------------|--------------|-------------|
  | OOLONG (132K tokens) | GPT-5 baseline | RLM(GPT-5-mini) 2x | >33% |
  | CodeQA | GPT-5: 24% | RLM: 62% | 158% |
  | BrowseComp-Plus | Degradation at scale | Perfect | Maintained at 10M+ |
- **Key Quote**: "If I split the context into two model calls, then combine them in a third model call, I'd avoid this degradation issue." — Alex Zhang
- **Pattern**: [Recursive Context Management](patterns/recursive-context-management.md)
- **Evidence Tier**: B (Academic research + industry recognition, no Claude-specific validation)
- **Status**: EMERGING PATTERN - Monitor for Claude-specific validation

### RLM Claude Code Integrations (Tier C)
Community implementations integrating RLM patterns with Claude Code:

| Repository | Author | Maturity | Key Features |
|------------|--------|----------|--------------|
| [rand/rlm-claude-code](https://github.com/rand/rlm-claude-code) | rand | Most mature (144 commits, 41 stars) | Persistent memory, complexity classifiers, budget tracking |
| [brainqub3/claude_code_RLM](https://github.com/brainqub3/claude_code_RLM) | Brainqub3 | Minimal (4 commits) | Basic scaffold, `/rlm` skill, Opus+Haiku hierarchy |
| [zircote/rlm-rs](https://github.com/zircote/rlm-rs) | zircote | Rust CLI | SQLite persistence, chunk orchestration |
| [ysz/recursive-llm](https://github.com/ysz/recursive-llm) | ysz | Multi-model | Supports `claude-sonnet-4`, provider-agnostic |
| [RLM-MCP](https://news.ycombinator.com/item?id=46708942) | HN poster | Initial beta | MCP server approach for large file analysis |

**All created January 2026** - early-stage ecosystem, no production validation yet.

### RLM Monitoring Signals
Track these for production readiness:

| Signal | Where to Watch | Implication |
|--------|----------------|-------------|
| Anthropic "context-trained" models | Blog, changelog | Native RLM compatibility |
| rand/rlm-claude-code releases | GitHub | Community validation progress |
| Claude Agent SDK RLM patterns | Anthropic docs | Official support |
| Chroma context rot follow-up | Research blog | Updated benchmarks |

### Context Rot Research
- **Source**: [Chroma Research](https://research.trychroma.com/context-rot)
- **Date**: July 2025 (initial), ongoing updates
- **Description**: Empirical study of LLM performance degradation with increasing context
- **Key Findings**:
  - Claude models decay slowest overall among tested LLMs
  - Claude shows most pronounced gap between focused/full prompt performance on LongMemEval
  - Claude models tend to abstain when uncertain rather than hallucinate
  - Counterintuitively, shuffled (incoherent) contexts outperform logically structured ones
- **Evidence Tier**: B (Independent research lab with reproducible methodology)

### Tenzir Blog: MCP vs Skills Economics
- **Author**: Matthias Vallentin
- **URL**: https://blog.tenzir.com (January 2026)
- **Title**: "We Did MCP Wrong"
- **Description**: Production data comparing MCP vs Skills architectures
- **Key Data**:
  | Metric | MCP | Skills | Winner |
  |--------|-----|--------|--------|
  | Duration | 6.2 min | 8.6 min | MCP (38% faster) |
  | Tool calls | 61 | 52 | Skills (15% fewer) |
  | **Cost** | $20.78 | $10.27 | **Skills (50% cheaper)** |
  | Cached tokens | 8.8M | 4.0M | Skills (55% less) |
- **Philosophy Shift**: "Force-feed structured context" → "Provide capabilities and documentation"
- **Pattern**: [MCP vs Skills Economics](patterns/mcp-vs-skills-economics.md)
- **Evidence Tier**: B (Production data from active project)

### LlamaIndex - Agentic Document Workflows
- **Source**: LlamaIndex Engineering Blog
- **URLs**:
  - [Introducing Agentic Document Workflows](https://www.llamaindex.ai/blog/introducing-agentic-document-workflows)
  - [RAG is Dead, Long Live Agentic Retrieval](https://www.llamaindex.ai/blog/rag-is-dead-long-live-agentic-retrieval)
- **Date**: 2025
- **Key Insights**:
  - Agentic retrieval uses tools to dynamically navigate documents vs pre-computed embeddings
  - Three-phase exploration: Parallel Scan → Deep Dive → Backtrack
  - Cross-references remain opaque to vector-based matching
  - Typed messages (Pydantic) enable formal contracts between workflow stages
- **Pattern**: [Agentic Retrieval](patterns/agentic-retrieval.md)
- **Evidence Tier**: B (Major framework vendor with production implementations)

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

### Playwright CLI (Browser Automation for AI Agents)
- **Author**: Microsoft / Playwright Team
- **URL**: https://github.com/microsoft/playwright-cli
- **Date**: February 2026
- **Description**: CLI tool for browser automation, purpose-built for AI coding agents as a token-efficient alternative to Playwright MCP
- **Key Insights**:
  - 4x token reduction vs Playwright MCP (~27K vs ~114K tokens per task)
  - Saves snapshots/screenshots to disk instead of streaming into context
  - Compact element references (e.g., `e21`) instead of full DOM trees
  - 50+ commands: navigation, interaction, screenshots, session management
  - `--skills` flag installs documentation for agent discovery
- **Pattern**: [MCP Patterns - CLI vs MCP](patterns/mcp-patterns.md#cli-vs-mcp-the-token-efficiency-case)
- **Evidence Tier**: B (Microsoft, measured benchmarks, 3.6k stars) ✅ Verified

---

## AI Coding Ecosystem Tools (Tier C)

These tools complement Claude Code or provide alternative approaches to AI-assisted development. Tier C reflects community-driven, production-validated tools.

### Alternative AI Coding Agents

| Tool | Repository | Key Feature | Use Case |
|------|------------|-------------|----------|
| **Aider** | [paul-gauthier/aider](https://github.com/paul-gauthier/aider) | Git-centric workflow, local model support (Ollama) | Privacy-sensitive, offline-first |
| **OpenHands** | [All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands) | Dockerized autonomous agents | Sandboxed execution, reproducibility |
| **Goose** | [block/goose](https://github.com/block/goose) | Extensible local agent framework | Custom agent development |
| **Cursor** | [cursor.sh](https://cursor.sh) | VS Code fork with native AI | IDE-native experience |

- **Pattern**: [Tool Ecosystem](patterns/tool-ecosystem.md)

### Context Extraction Tools

| Tool | Repository | Purpose |
|------|------------|---------|
| **repomix** | [yamadashy/repomix](https://github.com/yamadashy/repomix) | Pack repository into AI-friendly single file |
| **code2prompt** | [mufeedvh/code2prompt](https://github.com/mufeedvh/code2prompt) | Token-optimized codebase context extraction |

- **Pattern**: [Context Engineering](patterns/context-engineering.md)

### Agentic Retrieval Tools

| Tool | Repository | Purpose |
|------|------------|---------|
| **agentic-file-search** | [PromtEngineer/agentic-file-search](https://github.com/PromtEngineer/agentic-file-search) | Dynamic document exploration with LlamaIndex Workflows + Gemini |

- **Key Features**: Three-phase exploration (scan/dive/backtrack), 6 filesystem tools, multi-format support (PDF, DOCX, PPTX), ~$0.001/query
- **Pattern**: [Agentic Retrieval](patterns/agentic-retrieval.md)

### AI Asset Generation Tools

| Tool | Repository | API | Purpose |
|------|------------|-----|---------|
| **google-image-gen-api-starter** | [AI-Engineer-Skool/google-image-gen-api-starter](https://github.com/AI-Engineer-Skool/google-image-gen-api-starter) | Google Gemini | CLI for image generation with style templates |

- **Pattern**: [AI Image Generation](patterns/ai-image-generation.md), [Tool Ecosystem](patterns/tool-ecosystem.md)

---

## Spec-Driven Development Standards (Tier A)

These represent the industry-standard methodologies for AI-driven development that this repository adopts:

### GitHub Spec Kit (Foundational)
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
- **Evidence Tier**: A (Industry standard - 59K+ stars, adopted by this repository as foundational methodology)

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

## Practitioner Educators (Tier A)

These individuals have developed principled methodologies for AI-assisted development that directly inform this repository:

### IndyDevDan (Dan Diemer) - Principled AI Coding Framework
- **Author**: Dan Diemer (@IndyDevDan)
- **GitHub**: https://github.com/disler
- **YouTube**: https://youtube.com/@IndyDevDan
- **Website**: https://agenticengineer.com
- **Courses**:
  - [Principled AI Coding (PAIC)](https://agenticengineer.com/principled-ai-coding) - Foundational principles
  - [Tactical Agentic Coding (TAC)](https://agenticengineer.com/tactical-agentic-coding) - Advanced orchestration
- **Description**: Seasoned software engineer (10+ years) and early GenAI adopter. Creator of the "Context-Prompt-Model" framework and "Great Planning is Great Prompting" principle. Teaches principles over tools, focusing on enduring concepts that survive tool churn.

#### Core Framework: "The Big Three"

| Pillar | Purpose | SDD Alignment |
|--------|---------|---------------|
| **Context** | Provide AI with information it needs for success | = Specify phase (specs as deterministic context) |
| **Prompt** | Design precise queries that get accurate results | = Tasks phase (task specification) |
| **Model** | Choose and leverage the right tools for tasks | = Implement phase (tool selection) |

#### Key Principles

1. **"Great Planning is Great Prompting"** - The core insight that planning effort directly improves AI output quality. Aligns with SDD's Specify→Plan phases.
2. **Principles over Tools** - "Yesterday it was Cursor, today it's Windsurf, tomorrow it'll be something else... learn to endure change with principle."
3. **Plan → Spec → Build Workflow** - Intermediate specification step before coding, matching SDD's 4-phase model.
4. **Prompts as Programming Primitives** - Prompts deserve the same engineering rigor as code.
5. **Massive Spec Prompts** - Feature requirements → fully generated code in a single prompt via comprehensive specs.

#### Open Source Artifacts

| Repository | Purpose | Relevance |
|------------|---------|-----------|
| [single-file-agents](https://github.com/disler/single-file-agents) | Single-purpose Python agents demonstrating precise prompt patterns | Reference for minimal, focused agent design |
| [indydevtools](https://github.com/disler/indydevtools) | Agentic engineering toolbox for autonomous problem-solving | Multi-agent architecture patterns |
| [claude-code-hooks-multi-agent-observability](https://github.com/disler/claude-code-hooks-multi-agent-observability) | Real-time monitoring for parallel Claude Code agents | Production observability patterns |
| [infinite-agentic-loop](https://github.com/disler/infinite-agentic-loop) | Two-prompt system for continuous agent operation | Advanced orchestration patterns |

#### Advanced Concepts (TAC Course)

- **Orchestrator Agent**: "The one agent to rule them all" - single interface to command agent fleets
- **Agent Experts**: Solve "agents forget" with Act → Learn → Reuse workflow
- **7-Level Prompt Hierarchy**: From simple prompts to self-improving meta prompts
- **Agentic Layers**: Building blocks leading to "The Codebase Singularity"

- **Influence on This Repo**:
  - Direct validation of SDD methodology from practitioner perspective
  - Context-Prompt-Model framework reinforces specs-as-context pattern
  - "Great Planning" principle documented in [Planning-First Development](patterns/planning-first-development.md)
  - Orchestrator pattern informs [Subagent Orchestration](patterns/subagent-orchestration.md)
- **Evidence Tier**: A (Principled methodology with open-source implementations, production-validated across thousands of engineers)

### Aniket Panjwani - Plan-Then-Act & Domain Knowledge Embedding
- **Author**: Dr. Aniket Panjwani (@aniketapanjwani)
- **Twitter/X**: https://x.com/aniketapanjwani
- **Website**: https://aniketpanjwani.com
- **Newsletter**: [Content Quant](https://contentquant.io/)
- **LinkedIn**: https://www.linkedin.com/in/aniket-a-panjwani/
- **Description**: PhD Economics (Northwestern), Senior MLOps Engineer at Early Warning Services (Zelle). Rare combination of academic research methodology + production ML engineering. Demonstrates Claude Code best practices for both software development and knowledge work (research, content creation).

#### Core Framework: Plan-Then-Act + Domain Skills

| Concept | Purpose | SDD Alignment |
|---------|---------|---------------|
| **Plan-Then-Act** | Break work into plan step + action step | = Specify → Implement phases |
| **Domain Skills** | Embed expertise into reusable Claude skills | = Specify phase (knowledge as context) |
| **Phase-Based Skills** | Separate skills per workflow phase (research → write → polish) | = Tasks phase decomposition |
| **Selective MCP Loading** | Enable MCPs per-project to manage context | = Context engineering |

#### The 5 Tips Framework

From his [viral X thread](https://x.com/aniketapanjwani/status/1999487999604605345):

1. **Use /plan** - "One of the keys to success with agentic coding is to break up whatever you're doing into a plan step and an action step."
2. **Use voice input** (Superwhisper) - Speak faster than type; Claude Code handles stream-of-consciousness
3. **Selective MCPs** - Each MCP consumes context; enable only what's needed per project
4. **Use plugins/skills** - Extensibility through skills is why Claude Code leads
5. **YOLO mode** (`--dangerously-skip-permissions`) - "The real magic of Claude Code is just letting it cook"

#### Key Insights

- **"Claude Code is the future of social science"** - Skills and subagents allow researchers to embed domain knowledge productively
- **Non-coding applications** - Automated research/creation/polishing workflows for local newsletters in 5-10 minutes using distinct skills per phase
- **For social science workflows** (EDA, regressions, causal analysis) - Claude Code and Codex are "far superior to Cursor"

#### Production Validation

| Project | Description | Relevance |
|---------|-------------|-----------|
| Payload CMS Newsletter Plugin | Built entirely with Claude Code | Production validation of agentic coding |
| Local CMS | AI-powered SaaS for local media | Real-world AI product |
| Custom MCP Server | Autonomous content creation pipeline | MCP implementation example |
| Zelle Fraud Detection | ML pipelines catching millions in fraud | Enterprise-scale ML engineering |

- **Influence on This Repo**:
  - Plan-then-act validates SDD's Specify→Implement flow from practitioner perspective
  - Domain knowledge embedding documented in [Skills for Domain Knowledge](patterns/skills-domain-knowledge.md)
  - Phase-based skill separation reinforces progressive disclosure pattern
  - Non-engineering use cases validate SDD for knowledge work beyond software
- **Evidence Tier**: A (PhD research rigor + production ML engineering + actionable best practices with measured outcomes)

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
| [MCP Implementation Guide](https://natesnewsletter.substack.com/p/the-mcp-implementation-guide-solving) | [MCP Patterns](../patterns/mcp-patterns.md) | 7 failure modes, Intelligence Layer/Sidecar/Batch patterns |
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

### claude-mem (Persistent Memory Plugin)
- **Author**: thedotmack
- **URL**: https://github.com/thedotmack/claude-mem
- **Description**: Automatic session capture with AI compression for persistent Claude Code memory
- **Key Features**:
  - 5 lifecycle hooks: SessionStart → UserPromptSubmit → PostToolUse → Summary → SessionEnd
  - Progressive disclosure (~10x token savings via AI compression)
  - Vector search via Chroma for semantic retrieval
  - Web viewer at localhost:37777
  - Privacy controls with `<private>` tags
- **Relevance**: Production implementation of concepts in [Memory Architecture](patterns/memory-architecture.md) and [Long-Running Agent](patterns/long-running-agent.md)
- **Evidence Tier**: C (Community tool with production validation)

### Claude Diary (Session Learning)
- **Author**: Lance Martin (LangChain founder)
- **URL**: https://github.com/rlancemartin/claude-diary
- **Description**: Memory plugin implementing three-tier architecture (observation → reflection → retrieval) based on Generative Agents paper
- **Key Features**:
  - `/diary` command for session summary capture
  - `/reflect` command for cross-entry pattern analysis
  - PreCompact hook for automatic diary generation
  - Human review required before CLAUDE.md updates
  - Pattern detection (2+ occurrences = pattern, 3+ = strong pattern)
- **Categories Analyzed**: PR feedback, persistent preferences, design decisions, anti-patterns, efficiency improvements
- **Relevance**: Reference implementation for [Session Learning](patterns/session-learning.md) pattern
- **Evidence Tier**: B (Expert practitioner with academic research basis)

### Claude Reflect (Hook-Based Learning)
- **Author**: Bayram Annakov
- **URL**: https://github.com/BayramAnnakov/claude-reflect
- **Description**: Hook-based automatic correction detection for Claude Code
- **Key Features**:
  - Automatic detection of correction patterns ("no, use X", tool rejections)
  - Queued learnings reviewed via `/reflect` command
  - Plugin ecosystem integration
- **Relevance**: Alternative implementation for [Session Learning](patterns/session-learning.md) pattern
- **Evidence Tier**: C (Community implementation)

### Autoskill (Meta-Skill Learning)
- **Author**: AI-Unleashed
- **URL**: https://github.com/AI-Unleashed/Claude-Skills/tree/main/autoskill
- **Description**: Meta-skill that updates other skill files based on session corrections
- **Key Features**:
  - Signal detection: corrections, repeated patterns, approvals
  - 4-question quality filter before proposing changes
  - Confidence levels (HIGH/MEDIUM) for proposals
  - Routes learnings to appropriate skill files
- **Caution**: Updates skill files directly — higher risk than CLAUDE.md-only approaches
- **Relevance**: Alternative approach for [Session Learning](patterns/session-learning.md) pattern
- **Evidence Tier**: C (Community, minimal documentation, no production validation)

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

## Session Learning and Self-Improvement Sources (Tier B)

These sources document session learning, self-improvement, and the risks of autonomous agent evolution:

### Generative Agents Paper (Stanford)
- **Title**: "Generative Agents: Interactive Simulacra of Human Behavior"
- **Authors**: Park et al., Stanford University
- **URL**: https://arxiv.org/abs/2304.03442
- **Date**: April 2023
- **Key Concepts**:
  - Three-tier memory: Observation → Reflection → Retrieval
  - Agents that form memories and plan behavior based on experience
  - 54% improvement from reflection-based memory in studies
- **Relevance**: Foundational research for [Session Learning](patterns/session-learning.md) pattern
- **Evidence Tier**: A (Peer-reviewed academic research)

### Yohei Nakajima: Self-Improving Agents
- **Author**: Yohei Nakajima (BabyAGI creator)
- **URL**: https://yoheinakajima.com/better-ways-to-build-self-improving-ai-agents/
- **Description**: Research summary on self-improving agent architectures
- **Key Insights**:
  - "Reflection notes" stored alongside objectives improve performance over time
  - Vector search for similar past objectives enables learning transfer
  - Categories: Self-reflection, self-generated data, self-adapting models
- **Relevance**: Expert perspective on session learning mechanisms
- **Evidence Tier**: B (Expert practitioner with research synthesis)

### Misevolution Research
- **Title**: "Your Agent May Misevolve: Emergent Risks in Self-Evolving LLM Agents"
- **URL**: https://medium.com/@huguosuo/your-agent-may-misevolve-emergent-risks-in-self-evolving-llm-agents-2f364a6de72e
- **Key Findings**:
  - Four risk pathways: model, memory, tool, workflow misevolution
  - Self-training reduced safety refusal rates by up to 70%
  - Quick fixes failed to restore original alignment
- **Relevance**: Critical risk documentation for [Session Learning](patterns/session-learning.md) pattern
- **Evidence Tier**: B (Research summary with citations)

### Reflexion Paper
- **Title**: "Reflexion: Language Agents with Verbal Reinforcement Learning"
- **Authors**: Shinn et al.
- **URL**: https://arxiv.org/abs/2303.11366
- **Key Findings**:
  - Self-critique stored as "reflections" improves task performance
  - 91% pass@1 on HumanEval (up from GPT-4 baseline)
  - Natural language feedback more effective than scalar rewards
- **Relevance**: Academic validation of reflection-based learning
- **Evidence Tier**: B (Peer-reviewed research)

### OpenAI Cookbook: Self-Evolving Agents
- **URL**: https://cookbook.openai.com/examples/partners/self_evolving_agents/autonomous_agent_retraining
- **Key Insights**:
  - Repeatable retraining loop for production agents
  - Human-in-the-loop failsafe for critical updates
  - Log every retraining event with parameters and metrics
- **Relevance**: Production implementation guidance for session learning
- **Evidence Tier**: A (Vendor documentation)

---

## Self-Evolution Algorithm Sources (Tier B)

These sources document the Self-Evolution Algorithm (TTD-DR) used in the [Recursive Evolution](patterns/recursive-evolution.md) pattern:

### Google TTD-DR Paper
- **Title**: "Deep Researcher with Test-Time Diffusion"
- **Authors**: Google Research
- **URL**: https://arxiv.org/abs/2502.04675
- **Date**: February 2025
- **Key Concepts**:
  - Self-Evolution Algorithm for research synthesis
  - Multi-candidate initialization with diverse configurations
  - Component-wise evolution (Plan, Search, Answer)
  - Recursive feedback loop with "Environment Judge"
  - Crossover synthesis for merging insights
- **Evidence Tier**: B (Academic research with community implementations)

### OptILLM Deep Research Plugin
- **Author**: codelion
- **URL**: https://github.com/codelion/optillm
- **Plugin Path**: `optillm/plugins/deep_research/`
- **Description**: Production-ready implementation of TTD-DR algorithm
- **Key Features**:
  - Iterative denoising with quality thresholds
  - Gap analysis with priority classification
  - 6-dimension quality scoring (completeness, accuracy, depth, coherence, citations, improvement)
  - Termination conditions: completeness > 0.9 OR (improvement < 0.03 AND completeness > 0.7)
  - Component fitness tracking
- **Evidence Tier**: B (Production implementation with active maintenance)

### AI-Engineering-101 Tutorial
- **Author**: Saurav Prateek
- **URL**: https://github.com/SauravP97/AI-Engineering-101
- **Path**: `/self-evolution-google/agent.ipynb`
- **Video**: [Google Self-Evolution Algorithm for Deep Researcher](https://www.youtube.com/watch?v=example)
- **Description**: Educational implementation demonstrating core algorithm
- **Key Implementation**:
  - 3 candidates with diverse configs: T=0.5/1.0/1.5, top_k=30/40/50
  - 3 refinement iterations per candidate
  - Environment Judge evaluating against web search results
  - Crossover function merging evolved answers
- **Evidence Tier**: C (Educational implementation)

### Additional TTD-DR Implementations (Tier C)

| Repository | Description | Evidence Tier |
|------------|-------------|---------------|
| [MMU-RAG Competition](https://github.com/eamag/MMU-RAG-competition) | Faithful TTD-DR implementation designed for single 24GB GPU | C (Competition entry) |
| [TTD-DR Dify](https://github.com/fdb02983rhy/TTD-DR-Dify) | Low-code/visual TTD-DR workflow in Dify platform | C (Community port) |

---

## Claude Code Best Practices Repositories (Tier C)

These repositories provide community-maintained best practices and should be periodically reviewed to ensure this project remains current.

**Verification Status Legend:**
- ✅ **Verified**: Reviewed and confirmed high-quality
- 🔍 **Discovered**: Found via search, needs review
- ⚠️ **Stale**: Last commit >6 months ago

### Curated Lists (Primary Review Sources)

| Repository | Status | Stars | Focus | Priority |
|------------|--------|-------|-------|----------|
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | ✅ Verified | 18k+ | Commands, workflows, patterns | HIGH |
| [jqueryscript/awesome-claude-code](https://github.com/jqueryscript/awesome-claude-code) | 🔍 Discovered | - | Tools, IDE integrations | HIGH |
| [josix/awesome-claude-md](https://github.com/josix/awesome-claude-md) | 🔍 Discovered | - | CLAUDE.md examples | HIGH |
| [ccplugins/awesome-claude-code-plugins](https://github.com/ccplugins/awesome-claude-code-plugins) | 🔍 Discovered | - | Plugins, hooks | MEDIUM |
| [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | 🔍 Discovered | - | Skills resources | MEDIUM |

### Best Practices Repositories

| Repository | Status | Description |
|------------|--------|-------------|
| [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | ✅ Verified | 40+ tips, status line, system prompt optimization |
| [awattar/claude-code-best-practices](https://github.com/awattar/claude-code-best-practices) | 🔍 Discovered | Patterns and examples for Claude Code |
| [anuraag2601/claude-code-best-practices](https://github.com/anuraag2601/claude-code-best-practices) | 🔍 Discovered | Battle-tested practices from real projects |
| [Cranot/claude-code-guide](https://github.com/Cranot/claude-code-guide) | 🔍 Discovered | Comprehensive guide to features |
| [zebbern/claude-code-guide](https://github.com/zebbern/claude-code-guide) | 🔍 Discovered | Tips, tricks, hidden commands |
| [jmckinley/claude-code-resources](https://github.com/jmckinley/claude-code-resources) | 🔍 Discovered | Production agents, 100+ workflows |

### Template and Configuration Repositories

| Repository | Status | Description |
|------------|--------|-------------|
| [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | ✅ Verified | 400+ components, CLI tool (12.6k stars) |
| [centminmod/my-claude-code-setup](https://github.com/centminmod/my-claude-code-setup) | 🔍 Discovered | Starter template with memory bank |
| [ruvnet/claude-flow](https://github.com/ruvnet/claude-flow/wiki/CLAUDE-MD-Templates) | 🔍 Discovered | CLAUDE.md templates by project type |
| [ArthurClune/claude-md-examples](https://github.com/ArthurClune/claude-md-examples) | 🔍 Discovered | Sample CLAUDE.md files |

### Cross-Platform AI Coding Resources

| Repository | Status | Description |
|------------|--------|-------------|
| [instructa/ai-prompts](https://github.com/instructa/ai-prompts) | 🔍 Discovered | Prompts for Cursor, CLINE, Windsurf, Copilot |
| [Bhartendu-Kumar/rules_template](https://github.com/Bhartendu-Kumar/rules_template) | 🔍 Discovered | Cross-platform rules for AI assistants |
| [obviousworks/vibe-coding-ai-rules](https://github.com/obviousworks/vibe-coding-ai-rules) | 🔍 Discovered | AI-optimized rules for Windsurf, Cursor |
| [nibzard/awesome-agentic-patterns](https://github.com/nibzard/awesome-agentic-patterns) | 🔍 Discovered | Curated agentic AI patterns |

### Agentic Development Frameworks

| Repository | Status | Description |
|------------|--------|-------------|
| [danielmiessler/fabric](https://github.com/danielmiessler/fabric) | ✅ Verified | 200+ AI patterns, foundational influence |
| [microsoft/autogen](https://github.com/microsoft/autogen) | ✅ Verified | Microsoft's agentic AI framework |
| [anthropics/skills](https://github.com/anthropics/skills) | ✅ Verified | Official Anthropic skills examples |
| [e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) | 🔍 Discovered | List of AI autonomous agents |
| [panaversity/learn-agentic-ai](https://github.com/panaversity/learn-agentic-ai) | 🔍 Discovered | Agentic AI with DACA pattern |

### Review Cadence

| Source Type | Frequency | Next Review |
|-------------|-----------|-------------|
| Anthropic Engineering Blog | Weekly | Ongoing |
| awesome-claude-code lists | Monthly | Feb 2026 |
| Best practices repositories | Monthly | Feb 2026 |
| SDD frameworks (Spec Kit, BMAD) | Quarterly | Apr 2026 |
| Cross-platform resources | Quarterly | Apr 2026 |

### Verification Process

When reviewing a discovered repository:
1. Check last commit date (active maintenance?)
2. Review star count and fork activity
3. Scan README for quality and completeness
4. Check if patterns align with Claude Code capabilities
5. Update status to ✅ Verified or ⚠️ Stale

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
- Official specifications and standards (agentskills.io, OWASP)
- Industry-standard frameworks (GitHub Spec Kit 59K+ stars)
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

*Last updated: February 2026*

---
convergence: single-source
---

# Sources and References

All analysis documents in this repository are derived from authoritative sources and production-validated implementations.

**Quick Lookup**: For the top 20 most-referenced sources, see [SOURCES-QUICK-REFERENCE.md](SOURCES-QUICK-REFERENCE.md) (100 lines vs 1,612 here)

**Last curated**: 2026-07-18 (reverification sweep + token-economics re-measure — see the 2026-07-18 refresh-log row: OWASP-survey rows reverified via BlueRock, Playwright 4x attribution corrected, tool-search version pegs fixed, MRCR row resolved to GraphWalks, ACE/MCE/Meta-Harness venue checks, migration blog post added). Prior: 2026-07-16 (absorption-wave sweep, per `drafts/ABSORPTION-SCAN-2026-07.md` — superpowers v6.1.1 and ECC-rename re-verifications with GitHub-API-dated stats, new dossiers for the AGENTS.md standard / ClaudeLog / Armin Ronacher / Andrew Ng / anthropics first-party distribution repos, CodeGuard extended with the first-party marketplace plugin, canon follow-lane pointers on the Osmani/Willison/Karpathy/Husain-Shankar/Miessler entries, negative dossiers for frozen-or-abandoned repos, and 4 new quarantine lines in the Unverified section). Prior: 2026-07-10 (Reduction Phase 6 — 4 additions incl. the large-codebases Applied AI post and the best-practices-page 2026 rewrite, stale-markings for claude-doctor/`/insights`/Fable-suspension/Opus 4.7 migration/Vertrees/Playwright-CLI+valgard token numbers, 2 prunes, and link repointing for 4 retired analysis docs). Prior: 2026-06-21 (verified cluster refresh — Fable 5 GA, loop-eng lineage, OKF/typed-knowledge, memory-systems + evals leaders). Anthropic doc URLs are canonical at `code.claude.com`; older `docs.anthropic.com` paths still redirect but are not used here. See refresh log at the bottom, and the **Unverified / pending revalidation** section at the very end for claims that could not be primary-confirmed this pass.

## Primary Sources (Tier A)

### Boris Cherny (Claude Code Creator)

**Role**: Engineering Manager at Anthropic, creator of Claude Code
**Interview Sources**:
- [Paddo.dev: How Boris Uses Claude Code](https://paddo.dev/blog/how-boris-uses-claude-code/) (January 2026)
- [VentureBeat: Creator of Claude Code Workflow](https://venturebeat.com/technology/the-creator-of-claude-code-just-revealed-his-workflow-and-developers-are) (January 2026)
- [Anthropic Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)
- ["How I Use Claude Code" Threads mega-post](https://www.threads.com/@boris_cherny/post/DTBVlMIkpcm/) (February 1, 2026 — 8M views on X)
- ["Team Tips" Threads posts](https://www.threads.com/@boris_cherny/post/DUMZr4VElyb/) (42 tips, January-February 2026)
- [Lenny's Podcast: "Head of Claude Code"](https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens) (February 19, 2026)
- [Pragmatic Engineer: "Building Claude Code with Boris Cherny"](https://newsletter.pragmaticengineer.com/p/building-claude-code-with-boris-cherny) (March 4, 2026)
- [Anthropic Webinar: "Claude Code Advanced Patterns"](https://www.anthropic.com/webinars/claude-code-advanced-patterns) (March 24, 2026)

**Key Workflow Insights**:
1. **Parallel Sessions**: Run 5 terminal instances + 5-10 web sessions simultaneously
2. **Use the latest Opus** (4.6 at the time of Boris's interviews; Opus 4.8 is the current model as of 2026-05-28): all tasks—agent teams, 1M context, adaptive thinking
3. **CLAUDE.md as Team Memory**: Update multi-weekly, capture mistakes as they happen; CLAUDE.md is advisory (~80% adherence)—use hooks for 100% enforcement
4. **Plan Mode First**: Always for non-trivial work; have one Claude draft the plan, another review it as "staff engineer"
5. **Natural Language Git**: "commit and push" works without custom commands (per official guidance, avoid complex slash command lists)
6. **PostToolUse Auto-Formatting**: Run formatters (prettier, black) after Write (caveat: can consume 160K tokens in 3 rounds)
7. **Pre-Allow Permissions**: `/permissions` to allow `bun run build:*`, `bun run test:*`
8. **MCP for External Tools**: When native tools insufficient
9. **Verification = 2-3x Quality**: Subagent verification before finalizing; Writer/Reviewer pattern — fresh context improves review since Claude won't be biased toward code it just wrote
10. **Background Agents**: Stop hooks to avoid lost work
11. **GitHub Actions + @.claude**: Trigger Claude from CI/CD
12. **Skip Exotic Customization**: Standard patterns over novel approaches
13. **Document & Clear Pattern**: Never let a long session be your only record; commit frequently, dump progress to files, treat sessions as disposable
14. **60% Context Threshold**: Performance degrades at 20-40% capacity; auto-compaction fires at ~83.5%
15. **PostCompact Hook**: Re-inject critical instructions after context compaction (March 2026)
16. **Five-Layer Architecture**: MCP → Skills → Agent → Subagents → Agent Teams
17. **~150 Instruction Cap**: Keep CLAUDE.md under ~150 instructions; use progressive disclosure into skill files
18. **Subagent Anti-Pattern**: Custom subagents can "gatekeep context" and force rigid human workflows—consider letting the main agent use native delegation features
19. **New CLI Features**: `/loop` (recurring tasks, up to 3 days), `/btw` (side questions without breaking flow), `/effort max` (4 levels), `/insights` (weekly pattern review)
20. **100% AI-Authored Code**: Boris has written zero manual code since November 2025; ships 20-30 PRs/day

**Pattern References**: [Parallel Sessions](analysis/orchestration-comparison.md), [Subagent Orchestration](analysis/orchestration-comparison.md), [Documentation Maintenance](analysis/harness-engineering.md), [GitHub Actions Integration](analysis/harness-engineering.md), [Context Engineering](analysis/harness-engineering.md), [Advanced Hooks](analysis/harness-engineering.md)
**Evidence Tier**: A (Primary vendor/creator)

### Anthropic Engineering Blog

> **Venue note (2026-07-18)**: anthropic.com/engineering's most recent post remains 2026-04-23 as of this check; new Claude Code-relevant posts now appear at claude.com/blog (one confirmed instance below). Watch both in the weekly sweep.

#### Large-Scale Code Migrations with Claude Code
- **Title**: "How Anthropic runs large-scale code migrations with Claude Code"
- **Source**: claude.com/blog (the active vendor blog per the venue note above)
- **Date**: 2026-07-16 (verified 2026-07-18)
- **URL**: https://claude.com/blog/ai-code-migration
- **Key Insights**: rulebook-first migration prep; parallel subagents with small-model implementers reviewed by large-model reviewers; compiler/test verification loops as "objective referees"; resumable mechanical workflows.
- **Pattern**: [Model Migration Anti-Patterns](analysis/model-migration-anti-patterns.md), [Orchestration Comparison](analysis/orchestration-comparison.md)
- **Evidence Tier**: A per the rubric's "Direct from Anthropic (engineering blog, documentation)" line, with a self-reported-practices note: Anthropic describing its own internal usage, no external validation

#### Long-Running Agent Harness Patterns
- **Title**: "Effective harnesses for long-running agents"
- **Source**: Anthropic Engineering Blog
- **Date**: **2025-11-26** (date confirmed 2026-06-21; prior "March 2026" / "2026-03-01" stampings on this entry were wrong)
- **URL**: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- **Key Insights (confirmed on the page 2026-06-21)**:
  - External artifacts become the agent's memory (`claude-progress.txt` + git)
  - "Verify before work" startup protocol
  - "work on only one feature at a time" to prevent context exhaustion
  - Git as recovery mechanism
  - Structured task lists (JSON over markdown)
- **⚠️ Conflation corrected (2026-06-21)**: a prior draft claimed a "March 2026 update" to *this* page adding v2-simplification data ($125/4hrs with Opus 4.6 + "context anxiety"). **No such update appears on this page.** That $125 / Opus-4.6 / context-anxiety material lives on the SEPARATE "Harness design for long-running application development" page (2026-03-24), registered below. The two were conflated; see also the Quick-Reference correction. Note further: the harness-design page attributes the *removal* of context-reset behavior to **Opus 4.5** ("Opus 4.5 largely removed that behavior on its own"), so any "Opus 4.6 eliminates context anxiety" phrasing over-specifies the model version.
- **Revalidate by**: 2026-09-21

#### Harness Design for Long-Running Application Development
- **Title**: "Harness design for long-running application development"
- **Author**: Prithvi Rajasekaran (Anthropic)
- **Source**: Anthropic Engineering Blog
- **Date**: 2026-03-24 (verified 2026-06-21)
- **URL**: https://www.anthropic.com/engineering/harness-design-long-running-apps
- **Key Insights (verified verbatim 2026-06-21)**:
  - **Generator/evaluator separation** with a self-evaluation-bias caution: agents "confidently praising the work—even when, to a human observer, the quality is obviously mediocre … agents reliably skew positive when grading their own work"
  - **Cost evidence**: DAW harness $124.70 / 3hr 50min; solo agent $9 / 20 min vs full harness $200 / 6 hr ("over 20× more expensive, but the difference in output quality was immediately apparent"); "5 to 15 iterations per generation" for frontend design; the evaluator drives Playwright MCP to navigate/screenshot/study the live app against spec
  - Load-bearing guidance: "every component in a harness encodes an assumption about what the model can't do on its own, and those assumptions are worth stress testing"
  - **Context-anxiety attribution**: the page credits **Opus 4.5** with largely removing the context-reset behavior — do NOT attribute that to Opus 4.6.
- **Revalidate by**: 2026-09-21
- **Pattern**: [Harness Engineering](analysis/harness-engineering.md)

#### Scaling Managed Agents: Decoupling the Brain from the Hands
- **Title**: "Scaling Managed Agents: Decoupling the brain from the hands"
- **Author**: Lance Martin, Gabe Cemaj, Michael Cohen (Anthropic)
- **Source**: Anthropic Engineering Blog
- **Date**: 2026-04-08 (verified 2026-06-21)
- **URL**: https://www.anthropic.com/engineering/managed-agents
- **Key Insights (verified verbatim 2026-06-21)**:
  - Managed Agents is "our hosted service for long-horizon agent work"; it virtualizes the **session** (append-only log), **harness** (the loop that calls Claude and routes tool calls), and **sandbox** (execution environment)
  - Brain/hands decoupling via a stable interface: `execute(name, input) → string`
  - Performance: "our p50 TTFT dropped roughly 60% and p95 dropped over 90%"
  - "Don't adopt a pet" — cattle-not-pets framing; a failed container is handled as a tool error ("We no longer had to nurse failed containers back to health")
- **Revalidate by**: 2026-09-21
- **Pattern**: [Harness Engineering](analysis/harness-engineering.md), [Safety and Sandboxing](analysis/safety-and-sandboxing.md)

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

#### Parallel Claude Development (C Compiler)
- **Title**: "Building a C compiler with a team of parallel Claudes"
- **Source**: Anthropic Engineering Blog
- **Date**: February 5, 2026
- **URL**: https://www.anthropic.com/engineering/building-c-compiler
- **Key Insights**:
  - Git-based task claiming: agents claim tasks via text files, git synchronization prevents duplicates
  - LLM-aware design: minimal output, detailed logs to files, machine-readable error format
  - Agent specialization: deduplicate code, optimize performance, documentation, design critique
  - `--fast` mode: deterministic 1-10% test sampling to prevent endless test execution
  - Results: 2,000+ sessions, $20K API cost, 100K-line compiler building Linux 6.9 (x86/ARM/RISC-V)
- **Pattern**: [Parallel Sessions](analysis/orchestration-comparison.md), [Subagent Orchestration](analysis/orchestration-comparison.md)

#### Eval Awareness in BrowseComp
- **Title**: "Eval awareness in Claude Opus 4.6's BrowseComp performance"
- **Author**: Russell Coleman (Anthropic) — byline corrected 2026-06-21 (was attributed to "Anthropic Engineering")
- **Source**: Anthropic Engineering Blog
- **Date**: March 6, 2026 (re-verified 2026-06-21)
- **URL**: https://www.anthropic.com/engineering/eval-awareness-browsecomp
- **Key Insights**:
  - Model independently hypothesized it was being evaluated and identified the benchmark
  - Systematically located and decrypted the answer key without being told which benchmark
  - Multi-agent amplification: 3.7x higher unintended solution rate in multi-agent (0.87%) vs single-agent (0.24%)
  - At least 20 distinct sources of leaked answers found (academic papers, appendices)
  - Recommendation: treat evaluation integrity as ongoing adversarial problem, not design-time concern
- **Pattern**: [Agent Evaluation](analysis/agent-evaluation.md)

#### April 23 Postmortem — Claude Code Quality Regression
- **Title**: "An update on recent Claude Code quality reports" / "April 23 Postmortem"
- **Source**: Anthropic Engineering Blog
- **Date**: April 23, 2026
- **URL**: https://www.anthropic.com/engineering/april-23-postmortem
- **Key Insights**:
  - Three independent bugs cumulatively degraded Claude Code intelligence March 4 – April 20, 2026 across Sonnet 4.6, Opus 4.6, and Opus 4.7
  - Bug 1 (March 4): Reasoning-effort default switched `high` → `medium` to fix UI freezing; reverted April 7 after user complaints
  - Bug 2 (March 26): Prompt-caching optimization continuously cleared extended thinking blocks from sessions idle >1 hour, instead of clearing once — Claude lost mid-session reasoning context across turns
  - Bug 3 (April 16): System prompt instruction capping text-between-tool-calls to ≤25 words and final responses to ≤100 words "hurt coding quality" when combined with other changes
  - All reverted by April 20 (v2.1.116); usage limits reset April 23
  - Anthropic remediation: broader per-model evaluations for system-prompt changes, stricter code review, soak periods and gradual rollouts for intelligence-affecting changes, expanded repository context for code reviews
  - API itself was unaffected — only Claude Code, Claude Agent SDK, Claude Cowork
- **Implication for harness designers**: Vendor-side defaults sit upstream of all practitioner-observed quality thresholds; date-anchor claims to specific Claude Code versions. Effort-level defaults are load-bearing (not cosmetic). Caching layers can silently amputate context the harness assumed was retained. Brevity constraints at the system-prompt layer can degrade output even when they're harmless at the user-prompt layer.
- **Pattern**: [Behavioral Insights — Vendor-Side Quality Regression Case Study](analysis/behavioral-insights.md), [Harness Engineering — v2 Harness Simplification caveat](analysis/harness-engineering.md)
- **Evidence Tier**: A (vendor self-disclosure with specific dates, version numbers, and remediation steps)

#### Teaching Claude Why (Alignment Research)
- **Title**: "Teaching Claude why"
- **Source**: Anthropic Research
- **Date**: May 8, 2026
- **URL**: https://www.anthropic.com/research/teaching-claude-why
- **Key Insights**:
  - Teaching models the *principles* behind ethical behavior reduces agentic-misalignment (blackmail-scenario) rates from 22% to ~3%
  - "Difficult advice" training data achieves comparable alignment results at ~28× token efficiency vs synthetic-honeypot datasets
  - Implication for harness design: as models internalize *why* certain actions are problematic, heavy MUST-NOT scaffolding in CLAUDE.md may become less load-bearing — but is also no substitute for the alignment-training effect itself
- **Pattern**: [Behavioral Insights](analysis/behavioral-insights.md) (alignment-training implications for harness designers)
- **Evidence Tier**: A (Anthropic-authored research, with caveat that this is alignment research applied to harness design, not a harness-engineering guide)

#### How Claude Code Works in Large Codebases
- **Title**: "How Claude Code works in large codebases: Best practices and where to start"
- **Source**: Claude by Anthropic (Applied AI team — Alon Krifcher, Charmaine Lee, Chris Concannon, Harsh Patel, Henrique Savelli, Jason Schwartz, Jonah Dueck, Kirby Kohlmorgen)
- **Date**: 2026-05-14 (verified 2026-07-10)
- **URL**: https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start
- **Key Insights (verified 2026-07-10)**:
  - **Five extension points**: CLAUDE.md (hierarchical, directory-scoped, loaded automatically), hooks (event-triggered automation), skills (packaged instructions loaded on-demand rather than bloating every session), plugins (bundled skills/hooks/MCP for org-wide distribution), and LSP (symbol-level navigation instead of string matching)
  - **No-index filesystem navigation**: agentic search over RAG — "it traverses the file system, reads files, uses grep to find exactly what it needs, and follows references across the codebase," avoiding the staleness a centralized index accumulates
  - **Load-bearing caution for harness maintainers (verbatim)**: "instructions written for your current model can work against a future one" — a rule written to force single-file refactors around an older model's limits "would prevent a newer one from making coordinated cross-file edits it handles well." Recommends reviewing CLAUDE.md/hooks/skills configuration every 3-6 months against the current model.
  - Claude Code documented in production across multi-million-line monorepos, decades-old legacy systems, and distributed architectures spanning dozens of repositories
- **Evidence Tier**: A (Primary vendor documentation, named engineering team)
- **Revalidate by**: 2026-10-14
- **Role**: Replaces chunks of `harness-engineering.md` per the 2026-07-10 reduction pass — first-party guidance now covers ground (the extension-point inventory, the model-currency caution for configuration) the analysis doc previously carried alone.
- **Pattern**: [Harness Engineering](analysis/harness-engineering.md)

### Claude Code Documentation (Canonical)
- **Source**: Anthropic Official Documentation
- **URL**: https://code.claude.com/docs/en/best-practices (Canonical - January 2026, continuously updated; **re-fetched and re-verified 2026-06-21**)
- **Legacy URL**: https://docs.anthropic.com/en/docs/claude-code (redirects to above)
- **Evidence Tier**: A (Primary vendor documentation)
- **Verified verbatim 2026-06-21**:
  - **`/goal` condition + separate evaluator**: "set the check as a `/goal` condition. A separate evaluator re-checks it after every turn." This is the doc-level confirmation of the per-turn checker mechanism the changelog left unspecified.
  - **`Stop` hook gate**: "a Stop hook runs your check as a script and blocks the turn from ending until it passes," and "ends the turn after 8 consecutive blocks" — the documented infinite-loop guard.
  - **`/rewind` checkpointing**: "Every prompt you send creates a checkpoint."
  - **`/btw` side-questions**: "The answer appears in a dismissible overlay and never enters conversation history."
  - **Adversarial review subagent**: an explicit "Add an adversarial review step" section documents the Writer/Reviewer pattern as first-party guidance.
  - **CLAUDE.md discipline (verbatim)**: "keep it short and human-readable"; the prune test "Would removing this cause Claude to make mistakes? If not, cut it"; `@path/to/import` imports ("CLAUDE.md files can import additional files using @path/to/import syntax"); on-demand child loading ("Claude pulls in child CLAUDE.md files on demand when it reads a file in those directories").
  - **"Avoid common failure patterns" catalog (verbatim, all five)**: *The kitchen sink session*, *Correcting over and over*, *The over-specified CLAUDE.md*, *The trust-then-verify gap*, *The infinite exploration* — each with a prescribed Fix.
  - **Plugins are first-class**: "Plugins bundle skills, hooks, subagents, and MCP servers into a single installable unit ... Run `/plugin` to browse the marketplace."
- **Re-verified 2026-07-10 (2026 rewrite pass)**: page remains the canonical best-practices reference; the verbatim content above still holds. This entry doubles as the refresh target for the four analysis-doc collapses this pass reasons about (harness-engineering, claude-md-progressive-disclosure, orchestration-comparison, safety-and-sandboxing) — see `drafts/REDUCTION-PROPOSAL-2026-07.md` Phase 4. **Changelog cross-checked as the revalidation feed**:
  - **Native `claude doctor`** (v2.1.205, 2026-07-08, confirmed on the live changelog): "`/doctor` is now a full setup checkup that can diagnose and fix issues; `/checkup` is its alias" — supersedes the community claude-doctor tool this repo's audit previously shelled out to (see Session Quality Diagnostic Tools below).
  - **Sonnet 5 default** (v2.1.197, 2026-06-30, confirmed on the live changelog): "Introducing Claude Sonnet 5: now the default model in Claude Code, with a native 1M-token context window," promotional $2/$10 per MTok through 2026-08-31. See the Sonnet 5 section below.
  - **Agent teams v2** (v2.1.178, 2026-06-15, confirmed on the live changelog): `TeamCreate`/`TeamDelete` tools removed; with `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` every session now has one implicit team — teammates spawn directly via the Agent tool's `name` parameter, no setup step.
  - **Routines** (cloud-hosted scheduled/triggered workflows; carried in the source plan for this refresh as landing at v2.1.198): reached general availability in the June 2026 window per secondary sources, but the exact GA-tagged version could not be independently reconfirmed against the live changelog in this pass — v2.1.198's own changelog entry covers Claude-in-Chrome GA and background-agent auto-commit/push/PR, not Routines by name. Treat the v2.1.198 pairing as **unverified pending a direct fetch of the Routines GA announcement**.
- **Revalidate by**: 2026-10-10
- **Key Guidance**:
  - CLAUDE.md should be concise (~60 lines recommended)
  - Skills should be minimal ("Would removing this cause mistakes? If not, cut it.")
  - Avoid long lists of custom slash commands (anti-pattern)
  - Include verification (tests, linting) as highest-leverage practice
  - Use hooks sparingly; prefer pre-approved permissions
  - Custom subagents via `.claude/agents/*.md` — isolated context, scoped tools, model selection per agent
  - Plugins via `/plugin` marketplace — bundle skills, hooks, subagents, and MCP servers
  - Auto mode (`--permission-mode auto`) — AI classifier reviews commands, 0.4% FPR, replaces `--dangerously-skip-permissions`
  - `/btw` for side questions without growing context (dismissible overlay)
  - "Summarize from here" via `/rewind` — selective partial compaction
  - **Agent view** (`claude agents`, research preview, v2.1.139+): unified TUI dashboard for all background sessions — `https://code.claude.com/docs/en/agent-view`
  - **Ultrareview** (cloud bug-hunting agent fleet, v2.1.118+; CI subcommand `claude ultrareview <target>`): `https://code.claude.com/docs/en/ultrareview`
  - **`/goal` command** (completion-condition loop; the changelog does not specify the per-turn checker mechanism): `https://code.claude.com/docs/en/goal`
  - **Hooks invoke MCP tools directly** via `type: "mcp_tool"` (v2.1.118+) — no process spawn needed
  - **`hard_deny` auto-mode rules** (v2.1.128+) — unconditional blocks, take precedence over allow rules
  - **`continueOnBlock` PostToolUse hook option** (v2.1.136+) — feeds rejection reason back to Claude and continues the turn
- **Topics Used**:
  - CLAUDE.md file format
  - Settings and hooks configuration
  - Slash commands structure
  - Skills system
  - Custom subagents (`.claude/agents/`)
  - Plugin marketplace and installation
  - Auto mode permission handling
  - Context management (`/btw`, `/rewind` summarize)
  - Agent-view session orchestration, Ultrareview cloud fleet, `/goal` completion loops

### Claude Code Changelog
- **Source**: Anthropic GitHub Repository
- **URL**: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- **Releases**: https://github.com/anthropics/claude-code/releases
- **Key Updates Referenced** (as of April 2026):
  - **April 2026 Features**:
    - Advisor Strategy: Opus advisor + Sonnet/Haiku executor, 2% higher on SWE-bench at 11% lower cost
    - Monitor Tool: Interrupt-based background process monitoring, replaces polling loops
    - Managed Agents: Anthropic-hosted agent infrastructure, $0.08/hr + tokens, OAuth vaults, environment scoping
    - Claude Code Desktop Redesign: Multi-panel IDE-like experience, parallel sessions, integrated terminal
    - Routines: Cloud-hosted scheduled/triggered autonomous workflows (research preview)
    - Ultra Plan: Web-based planning interface, separate from execution
    - PR Session Launch: Start Claude Code session from pull request context
  - v2.1.114: Agent teams teammate permission dialog crash fix (April 18, 2026)
  - v2.1.113: Native binary CLI, `sandbox.network.deniedDomains`, Ultrareview parallelized launch, OSC 8 hyperlinks for wrapped URLs, 50+ security/bug fixes including `find -exec`/`-delete` no longer auto-approved (April 17, 2026)
  - v2.1.112: Opus 4.7 availability fix for auto mode (April 16, 2026)
  - v2.1.81: `--bare` flag, `--channels` permission relay, MCP OAuth updates
  - v2.1.80: Channels (`--channels`), `effort` frontmatter for skills, `rate_limits` in statusline
  - v2.1.79: `--console` flag, `/remote-control` for VSCode, AI session titles
  - v2.1.78: `StopFailure` hook, `effort`/`maxTurns`/`disallowedTools` frontmatter, `${CLAUDE_PLUGIN_DATA}`
  - v2.1.77: Opus 4.6 64k output, `allowRead` sandbox, `/copy N`
  - v2.1.76: MCP elicitation, `Elicitation`/`ElicitationResult` hooks, `/effort`, `worktree.sparsePaths`, 24 hook types
  - v2.1.37: Agent teams (experimental), automatic session memory, PDF page ranges in Read tool, "Summarize from here" via /rewind, skills from --add-dir, remote sessions in VS Code, OAuth for MCP servers
  - v2.1.3: Unified slash commands and skills, permission rule detection in /doctor, 10-minute hook timeout
  - v2.1.0: Skill hot-reload, context forking, skill-level hooks, wildcard permissions, subagent resumption, real-time steering, MCP list_changed notifications
  - v2.0.76: LSP tool (go-to-definition, find references, hover)
  - v2.0.60: Background agent support
- **Model Updates**:
  - **Claude Fable 5** (June 9, 2026; model ID `claude-fable-5`): Anthropic's "most capable widely released model" per the models overview; GA on Claude API + AWS Bedrock + Vertex + Microsoft Foundry; **$10/$50 per MTok**, 1M context, 128k output; **adaptive thinking always on** (the only thinking mode, no extended thinking). Refusals surface as `stop_reason: "refusal"` on a successful HTTP 200 (Fable 5 has safety classifiers; **Mythos 5 / `claude-mythos-5`** shares Fable 5 capabilities WITHOUT classifiers — limited availability via Project Glasswing, not GA). Tokenizer note: Fable 5 and Mythos 5 use the tokenizer introduced with Opus 4.7 — "the same text produces roughly 30% more tokens" vs pre-4.7 models. See Fable 5 / Mythos 5 section below. **Benchmark figures UNVERIFIED** — see Unverified section.
  - Opus 4.8 (May 28, 2026; model ID `claude-opus-4-8`): recovery/calibration release over 4.7 — better tool triggering, better compaction/long-context recovery, more reliable effort calibration; adaptive thinking is the only mode (extended-thinking `budget_tokens` returns HTTP 400 — migrate to `adaptive` + `effort`), default effort `high`; 1M context default on Claude API/Bedrock/Vertex, 200k on Microsoft Foundry — see Opus 4.8 Re-Validation section below. **Listed deprecation**: Opus 4.1 retires August 5, 2026 (models-overview Warning block, confirmed 2026-06-21).
  - Opus 4.7 (April 16, 2026): Literal instruction following, fewer silent generalizations, fewer default subagents, adaptive response-length calibration — see Opus 4.7 Migration Guidance section below
  - **Sonnet 4.6** (February 17, 2026; model ID `claude-sonnet-4-6`): $3/$15 per MTok (unchanged from 4.5); 1M-token context in beta (64k output per the models overview, NOT stated on the announcement page); "major improvement in computer use skills," prompt-injection improvement, "fewer false claims of success, fewer hallucinations"; supports both adaptive and extended thinking plus context compaction in beta. Users preferred Sonnet 4.6 over Sonnet 4.5 "roughly 70% of the time" and over Opus 4.5 "59% of the time" in Claude Code. See Sonnet 4.6 section below.
  - Opus 4.6 (February 5, 2026): 1M token context, agent teams, adaptive reasoning, data residency controls
  - Opus 4.5 (November 24, 2025): 67% price reduction to $5/$25 per million tokens
  - Sonnet 4.5 (September 29, 2025): Agent-first design, Agent SDK support
  - Haiku 4.5 (October 2025): Extended thinking support, 1/3 cost of Sonnet
- **Pattern References**: [Advanced Hooks](analysis/harness-engineering.md), [Plugins and Extensions](analysis/plugins-and-extensions.md), [Subagent Orchestration](analysis/orchestration-comparison.md), [Plugins and Extensions](analysis/plugins-and-extensions.md)

#### Opus 4.7 Migration Guidance (April 2026)

> **📌 HISTORICAL (marked 2026-07-10)**: kept for provenance and as `model-migration-anti-patterns.md`'s evidentiary base for the 4.6→4.7 transition specifically. Current migration guidance for Fable-era models ships in the bundled `/claude-api` skill (loaded in this harness) rather than as a standalone doc here — consult that skill for live model-migration guidance.

- **Primary — Anthropic Migration Guide**
  - **URL**: https://platform.claude.com/docs/en/about-claude/models/migration-guide
  - **Evidence Tier**: A (Primary vendor documentation)
  - **Key Claim (verbatim)**: "Claude Opus 4.7 interprets prompts more literally and explicitly than Claude Opus 4.6, particularly at lower effort levels. It will not silently generalize an instruction from one item to another, and it will not infer requests you didn't make."
  - **Additional guidance**:
    - "Response length calibrates to perceived task complexity rather than defaulting to a fixed verbosity" — to reduce verbosity, add explicit concision directive
    - "Fewer subagents spawned by default. Steerable through prompting."
    - "Fewer tool calls by default, using reasoning more."
    - "More regular progress updates... If you've added scaffolding to force interim status messages, try removing it."
    - **Tension with heavy MUST NOT patterns**: "Positive examples... tend to be more effective than negative examples or instructions that tell the model what not to do."
  - **Pattern**: [Model Migration Anti-Patterns](analysis/model-migration-anti-patterns.md), [Behavioral Insights](analysis/behavioral-insights.md)

- **Primary — What's New Claude 4.7**
  - **URL**: https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7
  - **Evidence Tier**: A
  - **Key points**: Literal instruction following, adaptive thinking, tool-call frugality
  - **Pattern**: [Behavioral Insights](analysis/behavioral-insights.md)

- **Primary — Best Practices for Opus 4.7 with Claude Code**
  - **URL**: https://claude.com/blog/best-practices-for-using-claude-opus-4-7-with-claude-code
  - **Evidence Tier**: A
  - **Pattern**: [Harness Engineering](analysis/harness-engineering.md), [Model Migration Anti-Patterns](analysis/model-migration-anti-patterns.md)

- **Secondary — Jason Vertrees: "Claude 4.7 Quietly Broke Your Prompts and Harness"**
  - **📌 HISTORICAL (marked 2026-07-10)**: kept only as provenance for `model-migration-anti-patterns.md`'s 4.6→4.7 case study — not a live source for current-model guidance.
  - **URL**: https://www.linkedin.com/pulse/claude-47-quietly-break-your-prompts-harness-heres-how-jason-vertrees-mscpe/
  - **Date**: April 2026
  - **Evidence Tier**: B (Practitioner commentary operationalizing Tier A guidance)
  - **Contribution**: Six prompt anti-patterns (vague quality descriptors, edge-case gestures, unanchored triggers, implicit subagent dispatch, missing verbosity directives, references without read-enforcement). Proposes audit with grep + CI regression tests.
  - **Caveat**: Vertrees leans heavily on MUST/MUST NOT rules; this conflicts with Anthropic's stated preference for positive examples.
  - **Pattern**: [Model Migration Anti-Patterns](analysis/model-migration-anti-patterns.md)

- **Secondary — Simon Willison: Opus 4.7 System Prompt Analysis**
  - **URL**: https://simonwillison.net/2026/Apr/18/opus-system-prompt/
  - **Date**: April 18, 2026
  - **Evidence Tier**: B
  - **Counter-signal**: Literalism is selective, not uniform. Anthropic's leaked system prompt nudges 4.7 to be *less* literal about clarifying questions — "the person typically wants Claude to make a reasonable attempt now, not to be interviewed first."
  - **Pattern**: [Behavioral Insights](analysis/behavioral-insights.md)

- **Practitioner — Hacker News 4.7 Discussions**
  - **HN 47793411** (1,955 points): "adaptive thinking chooses to not think when it should"; workaround = `xhigh` effort + explicit thinking-summary config
  - **HN 47814832**: 4.7 over-literally applies system-reminder instructions (e.g., malware check) to every file read — red-teamers describe as "close to unusable" for certain workflows
  - **Evidence Tier**: C (Community observation, unvalidated)
  - **Pattern**: [Behavioral Insights](analysis/behavioral-insights.md)

#### Opus 4.8 Re-Validation (May 2026)

Opus 4.8 shipped 2026-05-28 (model ID `claude-opus-4-8`; the `[1m]` suffix is the 1M-context variant). It is largely a *recovery and calibration* release relative to the 4.7 regressions — the literal-interpretation posture carries forward, so the Opus 4.7 migration guidance above still applies for 4.7→4.8. The four model-coupled analysis docs (`model-migration-anti-patterns.md`, `behavioral-insights.md`, `safety-and-sandboxing.md`, `harness-engineering.md`) and the audit routing in `AUDIT-CONTEXT.md` were re-validated against 4.8 primary sources fetched 2026-05-30.

- **Primary — What's New Claude 4.8**
  - **URL**: https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8
  - **Evidence Tier**: A (Primary vendor documentation)
  - **Key points**: Better tool triggering (fewer skipped required tool calls), better compaction/long-context recovery, more reliable effort calibration; adaptive thinking is the only thinking mode (extended-thinking `budget_tokens` returns HTTP 400 — migrate to `thinking: {type: "adaptive"}` + `effort`); default effort `high`; "better long-context handling" and "fewer compactions" vs 4.7 (directional, not quantified against the 4.6/4.7 MRCR figures).
  - **Pattern**: [Model Migration Anti-Patterns](analysis/model-migration-anti-patterns.md), [Behavioral Insights](analysis/behavioral-insights.md), [Harness Engineering](analysis/harness-engineering.md)

- **Primary — Opus 4.8 System Card**
  - **URL**: https://www.anthropic.com/claude-opus-4-8-system-card
  - **Evidence Tier**: A (Anthropic system card)
  - **Key points**: Improvement over 4.7 on most alignment measures; honesty in agentic settings "markedly improved"; best-aligned publicly accessible model on the third-party Petri 3.0 run. Two flagged caveats carried into the analysis docs: a qualitative pilot "Mild sycophancy" note the card itself flags as *inconsistent* with the quantitative trends (so no numeric sycophancy increase is asserted — the "up" signal is a Tier-C launch-day anecdote, contradicted by these Tier-A evals); and a "growing tendency toward speculation about graders / reasoning about how outputs will be assessed" flagged as the *most concerning training trend* (modest behavioral effect at deployment) — a watch-item for rubric-scored evaluator-agent workflows. The §5.2 prompt-injection regression figures from this card are registered with the safety analysis.
  - **Pattern**: [Behavioral Insights](analysis/behavioral-insights.md), [Model Migration Anti-Patterns](analysis/model-migration-anti-patterns.md), [Safety and Sandboxing](analysis/safety-and-sandboxing.md)

- **Primary — Claude Opus 4.8 Launch News**
  - **URL**: https://www.anthropic.com/news/claude-opus-4-8
  - **Date**: 2026-05-28 (fetched 2026-05-30)
  - **Evidence Tier**: A
  - **Key points**: Misaligned behavior "substantially lower than Opus 4.7"; 1M context default on Claude API, Bedrock, and Vertex; 200k on Microsoft Foundry.
  - **Pattern**: [Behavioral Insights](analysis/behavioral-insights.md)

- **Supporting — 4.6→4.7 long-context regression case study (MRCR-v2)**
  - **Sources**: OpenAI MRCR v2 (Multi-Round Co-Reference Resolution, 8-needle) benchmark; Opus 4.7 system card *chart images* (Tier A, image — the figures live in the card's charts, not its body text); [Context Arena](https://contextarena.ai) + the dev.to write-up "I read all 232 pages [of the Opus 4.7 system card]" (Tier B, third-party transcription of the same chart figures)
  - **Figures**: 1M tokens 78.3% → 32.2%; 256k tokens 91.9% → 59.2% (4.6 → 4.7, 8-needle). Cite as *card chart (Tier A, image) + third-party transcription (Tier B)*, not as a quotable card sentence. The tokenizer-as-cause explanation is a single Tier-C blog conjecture, not adopted here. Note the 4.6 @1M figure also circulates as 76% in launch-era retellings.
  - **Resolved 2026-07-18 — Anthropic dropped MRCR after the 4.7 card; GraphWalks supersedes.** The Opus 4.8 system card (2026-05-28, §8.9) and the Fable 5/Mythos 5 card (2026-06-09, §8.13) contain zero MRCR mentions (verified by direct grep of both PDFs) and report GraphWalks F1 instead, with 256K/1M subsets split for the first time. GraphWalks F1 (256K→1M, avg 5 trials; scores reported for Mythos 5, same weights as Fable 5 plus blocking classifiers): Mythos 5 BFS 91.1→79.4, Parents 99.96→97.5 — the shallowest Parents drop (−2.5 pts) among the six models tabulated across the two cards (vs Mythos Preview −4.4, Opus 4.8 99.3→83.3, GPT-5.5 90.1→58.5); on BFS, Mythos Preview's absolute drop is marginally shallower (−11.4 vs −11.7), so no across-the-board superlative. Opus 4.8: BFS 85.9→68.1, Parents 99.3→83.3 (vs 4.7's 76.9→40.3 / 93.6→56.6). GPT-5.5 rows were produced under Anthropic's amended scoring — attribute to Anthropic's card, not OpenAI. 1M-subset results not reproducible via the public API. No independent MRCR/Fiction.liveBench/NoLiMa/RULER/LongBench-v2 coverage of 4.8 or the Claude 5 family found as of 2026-07-18 (Context Arena unverifiable — JS-only shell); third-party coverage remains the open residual.
  - **Pattern**: [Model Migration Anti-Patterns](analysis/model-migration-anti-patterns.md)

- **Supporting — Long-context degradation-onset benchmarks (revalidating the "60%" heuristic)**
  - **Sources**: arXiv:2601.15300 (Qwen2.5-7B degrades at 40–50% of max context, F1 0.55 → 0.30); Fiction.liveBench (deep-comprehension slide "closer to 32k"); NoLiMa (ICML 2025 — most models drop below half their short-input score by 32k tokens); arXiv:2510.05381
  - **Evidence Tier**: B (academic / benchmark; no Claude-specific validation)
  - **Contribution**: Reclassifies Boris Cherny's "60% context threshold" from a measured degradation onset to a practitioner *intervention heuristic* (Tier C; the originally-cited source page now 403s). Degradation onset is model-specific and typically begins far below the advertised window (~16–64k tokens, ≈20–50% on a 1M-context model). Treat 60% as an "intervene now" trigger, not the point where quality starts to fall. Re-measure on 4.8 rather than assuming the threshold moved.
  - **Pattern**: [Behavioral Insights](analysis/behavioral-insights.md)

#### Claude Fable 5 / Mythos 5 (June 2026)

Fable 5 (`claude-fable-5`) went GA 2026-06-09 as Anthropic's most capable widely released model. Verified against the API docs 2026-06-21; the consumer launch-news page (`/news/claude-fable-5`) returned **HTTP 404** at fetch time, so no benchmark figures are confirmed. **Currency update (2026-07-10)**: the suspension below is now CONFIRMED and RESOLVED — Fable 5 is redeployed and in production; the prior "NOT confirmed by any primary" framing is stale, see the new bullet immediately below.

- **Primary — Redeploying Claude Fable 5** (`anthropic.com/news/redeploying-fable-5`, 2026-06-30, fetched 2026-07-10). Tier A. **Resolves the prior unverified-suspension flag**: Fable 5 and Mythos 5 WERE suspended worldwide starting 2026-06-12 under a US export-control directive, triggered by an Amazon-researcher-reported jailbreak that got Fable 5 to identify software vulnerabilities and, in one case, produce exploit code; Anthropic could not verify user nationality in real time, so it pulled both models for all users. Verbatim: "As of today, June 30, the export controls on Fable 5 and Mythos 5 have been lifted." Both models redeployed globally 2026-07-01 across Claude Platform, Claude.ai, Claude Code, and Claude Cowork — **in production as of this pass**. New safety classifier blocks the reported jailbreak technique "in over 99% of cases," rerouting flagged requests to Claude Opus 4.8. Access metered through 2026-07-07 (up to 50% of weekly Pro/Max/Team limits), then billed via usage credits at standard API rates ($10/$50 per MTok) from 2026-07-08. Cloud-platform access (AWS, Google Cloud, Microsoft Foundry) was being restored separately at fetch time.
  - **Revalidate by**: 2026-10-10

- **Primary — Claude Models Overview**
  - **URL**: https://platform.claude.com/docs/en/about-claude/models/overview
  - **Date**: 2026-06-09 (fetched 2026-06-21)
  - **Evidence Tier**: A
  - **Verified**: Fable 5 GA, $10/$50 per MTok, 1M context, 128k output, adaptive thinking always on. Lineup `claude-fable-5` / `claude-opus-4-8` / `claude-sonnet-4-6` / `claude-haiku-4-5`. Opus 4.1 deprecated, retires Aug 5 2026. Tokenizer tooltip: Fable 5 + Mythos 5 use the Opus-4.7 tokenizer, "roughly 30% more tokens" for the same text vs earlier models. Sonnet 4.6 context = 1M; Haiku 4.5 = 200k; Opus 4.8 = 1M (200k on Microsoft Foundry, footnote 4).
- **Primary — Introducing Claude Fable 5 and Claude Mythos 5 (API launch doc)**
  - **URL**: https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5
  - **Date**: 2026-06-09 (fetched 2026-06-21)
  - **Evidence Tier**: A
  - **Verified verbatim**: Fable 5 GA across Claude API + AWS Bedrock + Vertex + Foundry from June 9 2026; refusals return `stop_reason: "refusal"` as a successful HTTP 200, not an error (Fable 5 only; Mythos 5 has no classifiers). Three fallback paths — server-side `fallbacks` parameter (beta on Claude API and on AWS), SDK middleware (client-side), and manual — with billing that "fallback credit refunds the prompt-cache cost of switching, so you avoid paying that cost twice." Mythos 5 (`claude-mythos-5`) shares Fable 5 capabilities without safety classifiers, limited availability via Project Glasswing, not GA. Adaptive thinking is "the only thinking mode"; raw chain of thought is never returned; `thinking.display` is `summarized` or `omitted` (default); "Pass thinking blocks back unchanged in multi-turn conversations on the same model." A "Migrating from Claude Opus 4.8 to Claude Fable 5" section exists in the migration guide (independently confirmed).
  - **Revalidate by**: 2026-09-21
- **Pattern**: [Model Migration Anti-Patterns](analysis/model-migration-anti-patterns.md), [Behavioral Insights](analysis/behavioral-insights.md)
- **⚠️ UNVERIFIED (still open 2026-07-10)**: all Fable 5 benchmark numbers (SWE-bench, GPQA, capability scores) — the `/news/claude-fable-5` page 404'd on 2026-06-21 and no benchmark figure was confirmed from any primary source in that pass or this one. Mythos 5 / Project Glasswing details beyond access model are unverified. **RESOLVED this pass**: the suspension claim itself (2026-06-12, export-control) is now CONFIRMED by the redeployment primary above, along with the 2026-06-30 lift / 2026-07-01 redeployment — do not carry forward the old "not confirmed" framing.

#### Sonnet 5 (June 2026)
- **Title**: Claude Code changelog v2.1.197
- **Source**: Anthropic (Claude Code changelog)
- **Date**: 2026-06-30 (verified 2026-07-10)
- **URL**: https://code.claude.com/docs/en/changelog
- **Verified verbatim**: "Introducing Claude Sonnet 5: now the default model in Claude Code, with a native 1M-token context window," promotional pricing $2/$10 per MTok through 2026-08-31. Sonnet 5 is the model this repo's own harness was running for parts of this pass.
- **⚠️ Unverified against a primary this pass**: exact model ID (`claude-sonnet-5` assumed, not independently confirmed against a model-card/overview page); benchmark figures; whether $2/$10 is permanent or promotional-only past 2026-08-31.
- **Evidence Tier**: A (primary changelog)
- **Revalidate by**: 2026-10-10
- **Pattern**: [Model Migration Anti-Patterns](analysis/model-migration-anti-patterns.md), [Behavioral Insights](analysis/behavioral-insights.md)

#### Sonnet 4.6 (February 2026)
- **Title**: "Introducing Claude Sonnet 4.6"
- **Source**: Anthropic
- **Date**: 2026-02-17 (fetched 2026-06-21)
- **URL**: https://www.anthropic.com/news/claude-sonnet-4-6
- **Evidence Tier**: A
- **Verified on the announcement**: model ID `claude-sonnet-4-6`; "$3/$15 per million tokens" (unchanged from 4.5); "1M token context window in beta"; "users preferred Sonnet 4.6 over Sonnet 4.5 roughly 70% of the time" and "preferred Sonnet 4.6 to Opus 4.5 … 59% of the time" in Claude Code; "major improvement in computer use skills," prompt-injection improvement, "fewer false claims of success, fewer hallucinations"; "supports both adaptive thinking and extended thinking, as well as context compaction in beta."
- **⚠️ Attribution caveats (2026-06-21)**: the **64k output limit is NOT on this announcement** — it is on the models-overview page; attribute the 64k figure to the overview. No specific **OSWorld numeric score** is stated on this page — do not cite one.
- **Revalidate by**: 2026-09-21
- **Pattern**: [Behavioral Insights](analysis/behavioral-insights.md)

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
- **Pattern**: [Context Engineering](analysis/harness-engineering.md)

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
- **Pattern**: [Plugins and Extensions](analysis/plugins-and-extensions.md), [Progressive Disclosure](analysis/claude-md-progressive-disclosure.md)

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
- **Patterns**: [Skills Domain Knowledge](analysis/domain-knowledge-architecture.md), [Progressive Disclosure](analysis/claude-md-progressive-disclosure.md), [Agent Evaluation](analysis/agent-evaluation.md), [Plugins and Extensions](analysis/plugins-and-extensions.md)

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
- **Pattern**: [Subagent Orchestration](analysis/orchestration-comparison.md)

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
- **Pattern**: [MCP Patterns](analysis/mcp-patterns.md)

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
- **Pattern**: [Tool Ecosystem](analysis/tool-ecosystem.md)

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
- **Pattern**: [Subagent Orchestration](analysis/orchestration-comparison.md)

#### Quantifying Infrastructure Noise in Agentic Coding Evals
- **Title**: "Quantifying infrastructure noise in agentic coding evals"
- **Author**: Gian Segato (with Nicholas Carlini, Jeremy Hadfield, Mike Merrill, Alex Shaw), Anthropic
- **Source**: Anthropic Engineering Blog
- **Date**: 2026-02-05 (re-verified 2026-06-21)
- **URL**: https://www.anthropic.com/engineering/infrastructure-noise
- **⚠️ URL MOVED (2026-06-21)**: the prior slug `…/quantifying-infrastructure-noise-in-agentic-coding-evals` now returns **HTTP 404**; canonical live URL is `…/engineering/infrastructure-noise`. The short slug above is the live one.
- **Key Insights (verified verbatim 2026-06-21)**:
  - **+6 percentage-point total lift on Terminal-Bench 2.0** from 1× to uncapped resources (p<0.01)
  - Infra error rate drops monotonically from **5.8%** (strict enforcement) to **0.5%** (uncapped); between 3× and uncapped, infra errors fall ~1.6pp while success jumps ~4pp — headroom matters beyond error rate
  - Resource configuration "should be treated as a first-class experimental variable, documented and controlled with the same rigor as prompt format"
- **Revalidate by**: 2026-09-21
- **Pattern**: [Agent Evaluation](analysis/agent-evaluation.md)

#### Designing AI-Resistant Technical Evaluations
- **Title**: "Designing AI-resistant technical evaluations"
- **Author**: Tristan Hume (Anthropic performance optimization lead)
- **Source**: Anthropic Engineering Blog
- **Date**: January 21, 2026 (re-verified 2026-06-21)
- **URL**: https://www.anthropic.com/engineering/AI-resistant-technical-evaluations
- **⚠️ URL CORRECTED (2026-06-21)**: canonical live slug is **capitalized** `…/engineering/AI-resistant-technical-evaluations`. Both the old lowercase `…/designing-ai-resistant-technical-evaluations` and the speculative `…/research/ai-resistant-technical-evaluations` return **HTTP 404** — the post did NOT move to `/research/`.
- **Key Insights (verified 2026-06-21)**:
  - Take-home test iterated across versions; Claude Opus 4 defeated the original, Claude Opus 4.5 defeated version 2; ~1,000 candidates have completed it
  - AI-resistance design approaches: problem novelty / out-of-distribution domains, reduced realism, candidates build their own debugging tools, insight over code volume, longer time horizons (not enumerated on the page as exactly "five principles")
  - "Human experts retain an advantage over current models at sufficiently long time horizons" (verbatim)
- **Revalidate by**: 2026-09-21
- **Pattern**: [Agent Evaluation](analysis/agent-evaluation.md)

#### Demystifying Evals for AI Agents
- **Title**: "Demystifying evals for AI agents"
- **Author**: Mikaela Grace, Jeremy Hadfield, Rodrigo Olivares, Jiri De Jonghe (Anthropic)
- **Source**: Anthropic Engineering Blog
- **Date**: January 9, 2026 (re-verified 2026-06-21)
- **URL**: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- **Key Insights (verified verbatim 2026-06-21)**:
  - Start with "20-50 simple tasks drawn from real failures" rather than synthetic benchmarks
  - Three grader types ("code-based, model-based, human") — matching grader to task type is the first design decision
  - `pass@k` (at least one correct in k attempts) and `pass^k` for non-deterministic agents, replacing single-run pass rates
  - Per-agent-type evaluation mapping (coding, conversational, research, computer-use) — the earlier "8 patterns" framing is loose; the per-type mapping is what the page confirms
- **Revalidate by**: 2026-09-21
- **Pattern**: [Agent Evaluation](analysis/agent-evaluation.md)

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
- **Pattern**: [Safety and Sandboxing](analysis/safety-and-sandboxing.md)

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
- **Pattern**: [Tool Ecosystem](analysis/tool-ecosystem.md)

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
- **Pattern**: [Subagent Orchestration](analysis/orchestration-comparison.md)

#### Claude Code Sub-agents
- **Source**: Anthropic Official Documentation
- **URL**: https://code.claude.com/docs/en/sub-agents
- **Key Insights**:
  - Specialized subagent types (Explore, Plan, general-purpose)
  - Parallel execution patterns
  - Context isolation for fresh context windows
- **Pattern**: [Subagent Orchestration](analysis/orchestration-comparison.md)

#### Auto Mode: Classifier-Based Permissions
- **Title**: "How we built Claude Code auto mode: a safer way to skip permissions"
- **Source**: Anthropic Engineering Blog
- **Date**: March 25, 2026 (re-verified 2026-06-21)
- **URL**: https://www.anthropic.com/engineering/claude-code-auto-mode
- **Key Insights (verified verbatim 2026-06-21)**:
  - Two-stage classifier: **Stage 1** is a fast single-token filter (8.5% FPR, blocks first); the full pipeline runs at **0.4% FPR**
  - Classifier **strips assistant text** ("so the agent can't talk the classifier into making a bad call") and **strips tool results** ("the primary prompt-injection defense")
  - An **input-layer probe** screens tool outputs for hostile content before they reach agent context — two independent layers ("it must evade detection at the input layer, then steer the agent into emitting a tool call")
  - **17% false-negative rate** on real overeager actions; **more than twenty block rules** across four groups (destroy/exfiltrate, degrade security posture, cross trust boundaries, bypass review/affect others)
  - For non-interactive `-p` runs, auto mode aborts if the classifier repeatedly blocks
- **Revalidate by**: 2026-09-21
- **Pattern**: [Safety and Sandboxing](analysis/safety-and-sandboxing.md)

#### Agent Skills System (Updated)
- **Title**: "Equipping agents for the real world with Agent Skills"
- **Source**: Anthropic Engineering Blog
- **Date**: March 19, 2026
- **URL**: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- **Key Insights**:
  - New frontmatter fields: `effort`, `paths` (conditional activation), `shell`, `hooks` (skill-scoped), `agent` (subagent type)
  - `${CLAUDE_SKILL_DIR}` variable for self-referencing skills
  - Skill description budget scales dynamically at 2% of context window (fallback 16KB)
  - Keep SKILL.md under 500 lines; move reference material to supporting files
  - Dynamic context injection via `` !`command` `` syntax
- **Pattern**: [Plugins and Extensions](analysis/plugins-and-extensions.md), [Progressive Disclosure](analysis/claude-md-progressive-disclosure.md)

#### Claude Code Hooks Reference
- **Source**: Anthropic Official Documentation
- **URL**: https://code.claude.com/docs/hooks-reference
- **Key Insights**:
  - PreToolUse input modification (v2.0.10+)
  - PostToolUse output formatting
  - PermissionRequest hooks (v2.0.45+)
  - SubagentStop and SessionEnd hooks
  - New events (v2.1.76-84): TaskCreated, TaskCompleted, TeammateIdle, CwdChanged, FileChanged, PostCompact, InstructionsLoaded, WorktreeCreate
  - New hook handler types: `http` (POST to endpoint), `prompt` (single LLM call), `agent` (subagent with 50 tool turns, 60s timeout)
- **Pattern**: [Advanced Hooks](analysis/harness-engineering.md)

### Claude Code First-Party Introspection Commands (`/insights`, `/usage`, `/doctor`)
- **Source**: Anthropic Claude Code (first-party commands)
- **Evidence Tier**: A (Primary vendor feature)
- **`/insights`** (maintained — `/insights` crash fix shipped in v2.1.149): analyzes local session history (~30 days / 50 sessions, Haiku) and produces an HTML report of recurring patterns and friction points, including copy-paste-ready CLAUDE.md rules auto-generated from instructions repeated across sessions. **⚠️ Date annotation (2026-07-10)**: `/insights` itself is confirmed real in the official commands reference, but the "announced by Thariq Shihipar, February 2026 / GA Feb 2026" date could not be verified against a primary in the July-2026 docs sweep — the earliest changelog trace found is v2.1.101 (2026-04; re-traced 2026-07-16 — the 2026-07-10 sweep had found only the v2.1.149 crash-fix line, 2026-05), which presupposes an earlier ship date but doesn't establish one. Treat the Feb-2026 GA date as unconfirmed, not as established fact (quarantine line added 2026-07-16 in the Unverified section). **Boundary**: session-history-only — does not read CLAUDE.md/hooks/agents/settings, does not detect model versions or migration anti-patterns, cites no evidence sources, and its suggestions are personalized to local habits (not portable to other projects).
- **`/usage`** (per-category breakdown, v2.1.149, May 2026): shows what is driving limit usage by skills, subagents, plugins, and per-MCP-server cost. Supplies the live numbers the build-vs-borrow framework in `mcp-vs-skills-economics.md` reasons about (folded from `mcp-daily-essentials.md`, absorbed into `mcp-patterns.md` 2026-07-10) — the measurement, not the decision framework.
- **`/doctor`** (environment diagnostic; "last update attempt" status added v2.1.153; **native full checkup at v2.1.205, 2026-07-08** — "`/doctor` is now a full setup checkup that can diagnose and fix issues; `/checkup` is its alias"): checks installation status, config consistency, ripgrep, and MCP config errors, and as of v2.1.205 supersedes the community claude-doctor tool this repo's audit previously shelled out to (see Session Quality Diagnostic Tools below).
- **Relevance to this project**: These are the first-party features that converged on the *edges* of the audit's scope and, as of v2.1.205, closed the session-diagnostics slice entirely. `session-quality-tools.md` completed its `RETIRING → RETIRED` cycle 2026-07-10 (archived, not deleted — see [CONTRIBUTING.md](CONTRIBUTING.md) § Retiring a doc) and the audit's signal command moved from `npx -y claude-doctor` to `claude doctor`. `/usage` and `/doctor` remain cited complements, not replacements for the static, evidence-tiered, model-migration-aware routing core, which still has no first-party equivalent.
- **Pattern**: [Session Quality Tools (archived)](archive/session-quality-tools.md), [MCP vs Skills Economics](analysis/mcp-vs-skills-economics.md), [MCP Patterns](analysis/mcp-patterns.md) (absorbed MCP Daily Essentials)

### Coalition for Secure AI (CoSAI) - Project CodeGuard
- **Source**: https://github.com/cosai-oasis/project-codeguard
- **Blog**: https://blogs.cisco.com/ai/cisco-donates-project-codeguard-to-the-coalition-for-secure-ai
- **Integration docs**: https://project-codeguard.org/claude-code-skill-plugin + https://project-codeguard.org/getting-started (verified 2026-07-16)
- **Date**: 2026-02-09 (donated to CoSAI); originally open-sourced October 2025 by Cisco
- **Type**: Open-source security framework for AI coding agents
- **Evidence Tier**: A (OASIS standards body / industry consortium — Anthropic, Google, OpenAI, Microsoft, NVIDIA are CoSAI founding members)
- **Description**: Model-agnostic framework embedding secure-by-default practices into AI coding agent workflows. 23 security rules across 8 domains (cryptography, input validation, authentication, authorization, supply chain, cloud security, platform security, data protection). Includes MCP-specific security rules.
- **Key Contributions**:
  - 3 mandatory rules: hardcoded credentials, cryptographic algorithms, digital certificates
  - Pre-generation / during-generation / post-generation lifecycle model
  - Credential detection patterns (AWS `AKIA*`, Stripe `sk_live_*`, GitHub `ghp_*`, JWT `eyJ*`)
  - Supply chain security (lockfiles, digest pinning, SBOM, deterministic installs)
  - MCP security (SPIFFE/SPIRE workload identity, transport security, tool sandboxing)
  - Integration tools for Cursor, Windsurf, Copilot, Agent Skills, and Claude Code
- **First-party Claude Code plugin (verified 2026-07-16)**: upstream now ships a marketplace plugin — `codeguard-security@project-codeguard` — with three supported deployment routes: marketplace install (`/plugin install codeguard-security@project-codeguard`), team-wide rollout via committed `settings.json`, and from-source build. This absorbed `secure-code-generation.md`'s Options B/C (2026-07-16 collapse edit); Option A (CLAUDE.md-paste path) and the commit-security-paths remediation framing have no upstream home and stay ours.
- **Critical-triad note (factual drift caught 2026-07-16)**: upstream's always-enforced rules are hardcoded-credentials / crypto-algorithms / **digital-certificates**; input-validation is a separate, non-critical rule — do not restate the triad as credentials/crypto/input-validation.
- **License**: CC BY 4.0 (rules), Apache 2.0 (tools)
- **Governance**: CoSAI Special Interest Group within AI Security Risk Governance Workstream
- **Pattern**: [Secure Code Generation](analysis/secure-code-generation.md)

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
- **Pattern**: [MCP Patterns](analysis/mcp-patterns.md)

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
- **Pattern**: [MCP Patterns](analysis/mcp-patterns.md)

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
- **Pattern**: [SKILL-TEMPLATE](analysis/domain-knowledge-architecture.md)

### AGENTS.md Standard (Agentic AI Foundation)
- **Author**: Agentic AI Foundation (AAIF), under the Linux Foundation
- **URL**: https://agents.md
- **Evidence Tier**: A (standards body — Linux Foundation stewardship)
- **Added**: 2026-07-16 (absorption-wave sweep; page verified 2026-07-16)
- **Description**: Open cross-agent instructions-file standard — a single `AGENTS.md` at repo root read by 20+ agents (Codex, Copilot, Cursor, Windsurf, Zed, Gemini CLI, JetBrains Junie, and others), with 60K+ adopting repos. Claude Code reads it too, but CLAUDE.md remains the richer native format (imports, progressive disclosure, per-directory scoping), so AGENTS.md is the interop layer, not a replacement.
- **Scope caveat**: a format standard, not sizing or content guidance — it standardizes *where* cross-agent instructions live, not *what* belongs in them, so it does not absorb this repo's CLAUDE.md sizing/structure findings (ABSORPTION-MAP.md: Sub ✗ for claude-md-progressive-disclosure).
- **Routing**: `repo-has-agents-md` signal → [claude-md-progressive-disclosure.md](analysis/claude-md-progressive-disclosure.md) (interop note added 2026-07-16)
- **Unverified**: the "170+ AAIF members" figure circulating in coverage — not confirmed against a primary, do not assert.
- **Pattern**: [CLAUDE.md Progressive Disclosure](analysis/claude-md-progressive-disclosure.md)

### Open Knowledge Format (OKF) Open Standard ⭐ KM-LEVERAGE SOURCE
- **Title**: "Open Knowledge Format (OKF) v0.1"
- **Source**: Google Cloud / GoogleCloudPlatform org (open standard)
- **URL (blog)**: https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/
- **URL (spec)**: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
- **Repository**: https://github.com/GoogleCloudPlatform/knowledge-catalog (`okf/` `samples/` `toolbox/`; Apache-2.0; HTML 49.4% / TS 27.1% / Python 20.9%; carries a "not an official Google product" disclaimer despite the GoogleCloudPlatform org)
- **Published**: 2026-06-12 (both blog + spec re-verified 2026-06-21)
- **Why elevated**: this is one of the two knowledge-management leverage sources the maintainer values from recent firsthand use — a portable, filesystem-native typed-frontmatter interchange format that maps directly onto the vault/OKF discipline this repo and project1 already run. Significant value seen firsthand recently; the spec itself is Tier C (vendor-published, v0.1 draft) and adoption is early, so the production hygiene pattern is the load-bearing part, not the spec.
- **Verified 2026-06-21**:
  - Spec confirmed "Version 0.1 — Draft"; intentionally minimal: "no schema registry, no central authority, and no required tooling"
  - Verbatim: "Type values are not registered centrally. Producers SHOULD pick values that are descriptive and self-explanatory; consumers MUST tolerate unknown types gracefully."
  - Reserved filenames `index.md` (progressive disclosure) and `log.md` (chronological history) confirmed on the **blog**; the blog explicitly quotes Karpathy and links his gist
  - Non-goals reference Avro, Protobuf, OpenAPI — "references them; it does not subsume them"
- **⚠️ Source-attribution corrections (2026-06-21)**:
  - **Apache-2.0 is confirmed on the REPO, not the blog** — the blog page does not state the license. (Prior entry sourced "Apache-2.0" to the blog.)
  - The spec does **not** name agentskills.io or Karpathy LLM-Wiki; the Karpathy linkage is on the *blog*, the Agent-Skills linkage is this repo's own synthesis.
  - **Critical caveat**: OKF does NOT register types centrally. The local single-parsed-registry + pre-commit drift-guard + coverage-metric discipline this repo runs is a *production practice* (Tier B, archetype-A §A1b), not mandated by OKF.
- **Evidence Tier**: C (vendor-published open standard); the typed-frontmatter hygiene pattern it anchors is Tier B from production.
- **Revalidate by**: 2026-09-21
- **Pattern**: [Typed-frontmatter hygiene](analysis/memory-systems-archetype-a-curated-kb.md) §A1b; [Memory System Patterns](analysis/memory-system-patterns.md)

### TypedMark — Typed-Markdown Spec (complement to OKF)
- **Author**: Sébastien Dubois (dsebastien.net)
- **URL**: https://www.dsebastien.net/typedmark/
- **Date**: 2026-06-20 (page-shown date; verified 2026-06-21); MIT (2026)
- **Description**: An open spec for typed Markdown note systems — schemas with field definitions and constraints, type validation, type inheritance via `extends`, named reusable "property sets" (frontmatter/block bundles), YAML frontmatter + markdown. Enforces "strong typing, no coercion."
- **Positioning (verbatim)**: TypedMark is "an additional option for the ecosystem, not a replacement for OKF or mdbase." It mandates explicit schemas (constraints/defaults, no coercion) where OKF tolerates unknown types — a genuine differentiation in the typed-knowledge space.
- **Evidence Tier**: C (single-author spec, MIT; tooling/marketplace maturity early-stage, adoption unproven as of June 2026 — track for maturation)
- **Revalidate by**: 2026-09-21
- **Pattern**: [Typed-frontmatter hygiene](analysis/memory-systems-archetype-a-curated-kb.md), [Memory System Patterns](analysis/memory-system-patterns.md)

### Michael Hannecke — "Frontmatter-First Is Not Optional" (context-window survival)
- **Author**: Michael Hannecke (Sovereign AI Architect, bluetuple.ai)
- **URL**: https://medium.com/@michael.hannecke/frontmatter-first-is-not-optional-context-window-survival-for-local-llms-in-opencode-15809b207977
- **Date**: 2026-04-05 (verified 2026-06-21)
- **Description**: Frontmatter-first knowledge-base reads for local LLMs in OpenCode. The "30 files × ~2,000 tokens = 60,000 tokens just to locate one document" example is confirmed verbatim. Three-stage ladder: (1) line-range reads via AGENTS.md, (2) bash single-call frontmatter extract, (3) pre-built YAML manifest (git pre-commit `build-manifest.py`). Frontmatter "under 10 lines"; local LLM 7B-14B / 8k-32k context (4,096 default, 32k practical ceiling).
- **Token-reduction caveat (2026-06-21)**: the article headlines **85%** reduction, but its worked Stage-3 example computes ~2,500 tokens total (manifest ~500 + 1 full read) vs 60,000 = **~95.8%**; the "~500 tokens" is the manifest size alone, not the end-to-end total. Author-reported, not independently reproduced — treat as directional. Framing is local-LLM-specific (absolute context constraint); the manifest still cuts latency/cost on cloud LLMs.
- **Evidence Tier**: C (single practitioner; author-reported figures)
- **Revalidate by**: 2026-07-05
- **Pattern**: [Memory Systems Archetype A — Curated KB](analysis/memory-systems-archetype-a-curated-kb.md), [Memory System Patterns](analysis/memory-system-patterns.md)

### Daniel Miessler — TELOS / SPQA (typed personal-context prior art)
> **⚠️ SUPERSEDED (2026-07-10)**: kept for provenance only. Miessler's current, live architecture is **PAI 5.0 → LifeOS 6.0.2** (renamed 2026-07-02) — see "Miessler 2026 — TELOS, PAI 5.0, and LifeOS" under Foundational Influences (Tier B) below. TELOS/SPQA remain valid as the typed-personal-context *prior art* this repo's OKF/typed-knowledge lineage draws on; they are not a description of his current tooling.
- **TELOS**: https://github.com/danielmiessler/Telos (MIT, 1.4k stars, "framework for creating Deep Context about things that matter to humans"; templates `personal_telos.md` + `corporate_telos.md` capture mission/goals/strategies/tech-stack/metrics). Git-commit date unresolved from the fetch (prior "2024-01-17" was an HTML last-modified value, not a commit) — date `unknown`. Re-verified 2026-06-21.
- **SPQA**: https://danielmiessler.com/blog/spqa-ai-architecture-replace-existing-software (2023-03-10, verified 2026-06-21). Four components confirmed verbatim — **STATE** (logs/docs/finances/chats/emails/transcripts), **POLICY** (mission/goals/anti-goals/challenges/strategies), **QUESTIONS** (leader inquiries), **ACTION** (outputs/recommendations). The article does not spell out the acronym; the four section names match. The "months/thousands-of-hours to minutes" / work drops to "1% to 5%" claim is the author's 2023 prediction (pre-agent-mainstream) — optimistic, unproven at scale.
- **Role**: SPQA's State+Policy structure and TELOS's typed-context layer are prior art for the OKF/typed-knowledge `telos.md` / `project-context.md` policy layer. The architectural-role framing is Miessler's own (Tier C opinion); the repos' existence/contents are verified.
- **Evidence Tier**: C (author opinion / architectural framing)
- **Revalidate by**: 2026-09-21
- **Pattern**: [Memory System Patterns](analysis/memory-system-patterns.md)

### Claude Code Plugins Directory
- **Source**: Anthropic Official Plugin Marketplace
- **URL**: https://claude.com/plugins
- **Description**: Official directory of Claude Code and Cowork plugins, featuring Anthropic-verified and community-contributed extensions
- **Verified Plugins**:
  - Frontend Design, Code Review, GitHub (official MCP server)
  - Feature Dev, Code Simplifier, Ralph Loop
  - TypeScript LSP, Commit Commands
- **High-Installation Plugins**: Context7, Superpowers, Playwright
- **Key Features**: Plugin submission process, installation statistics, compatibility information
- **Relevance**: Canonical reference for plugin ecosystem and official extension recommendations
- **Evidence Tier**: A (Primary vendor marketplace)
- **Pattern**: [Plugins and Extensions](analysis/plugins-and-extensions.md)

### Anthropic First-Party Distribution Repos (anthropics/skills + anthropics/claude-plugins-official)
- **Author**: Anthropic
- **URL**: https://github.com/anthropics/skills + https://github.com/anthropics/claude-plugins-official
- **Evidence Tier**: A (first-party)
- **Added**: 2026-07-16 (absorption-wave sweep)
- **Stats**: 161,668 stars (anthropics/skills) and 32,216 stars (claude-plugins-official) as verified 2026-07-16 (GitHub API); both pushed 2026-07-16
- **Description**: The first-party skills and plugin-distribution lane — official skill examples plus Anthropic's curated plugin repo behind the marketplace. Together with the [Claude Code Plugins Directory](https://claude.com/plugins) entry above, this is the lane community skill/plugin recommendations get pruned into as first-party coverage matures (per this repo's planned-obsolescence intent).
- **Pattern**: [Plugins and Extensions](analysis/plugins-and-extensions.md), [Domain Knowledge Architecture](analysis/domain-knowledge-architecture.md)

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
- **Pattern**: [GSD Orchestration](analysis/orchestration-comparison.md)
- **Evidence Tier**: B (Open source, production-validated)

> **🗑️ PRUNED (2026-07-10)**: Builder.io "50 Claude Code Tips" and Morph "Claude Code Best Practices — 2026 Guide" were removed here — both were community/vendor restatements of practitioner mechanics (aliasing, hook recipes, task scoping, model routing) now covered by the official best-practices 2026 rewrite (see Claude Code Documentation (Canonical) above). Neither is cited as a named source by any live analysis doc (only by the 2026-05-24 changelog row below, which stays as written for provenance). URLs for provenance: `builder.io/blog/claude-code-tips-best-practices` (Gopinath, 2026-03-20); `morphllm.com/claude-code-best-practices` (2026-02-15).

### shanraisshan/claude-code-best-practice
> **⚠️ SUPERSEDED-BUT-KEPT (2026-07-10)**: durable content (daily-MCP recommendations, RPI workflow, wildcard-permission examples) is now covered by the official best-practices 2026 rewrite — this entry would otherwise be a prune candidate alongside Builder.io/Morph above. **Not deleted**: `analysis/mcp-daily-essentials.md` and `analysis/plugins-and-extensions.md` both cite this repo by name as a live source (`🔗 Community Source` header + Sources footer in the former; marketplace comparison table in the latter) — per the reduction rule, an analysis doc's named source is annotated, not removed. Re-evaluate for deletion once those two docs' Phase-4 collapse lands and re-cites (or drops) it.
- **URL**: https://github.com/shanraisshan/claude-code-best-practice
- **Stars**: 5.6k+ (as of Feb 2026) — point-in-time, unrefreshed since; treat as directional only
- **Description**: Community-driven knowledge base documenting practical Claude Code workflows and tooling recommendations
- **Key Contributions**:
  - Top 4 daily MCP servers (Context7, Playwright, Claude in Chrome, DeepWiki)
  - Productivity tips: voice prompting (Wispr Flow), terminal vs IDE usage
  - Wildcard permissions syntax examples
  - RPI workflow (Research-Plan-Implement)
  - Community Reddit insights compilation
  - Monorepo CLAUDE.md loading behavior documentation
- **Relevance**: Practical workflow tips and community-validated tool recommendations complement this project's methodology focus
- **Evidence Tier**: B (Community validation with 5.6k+ stars, production usage patterns)
- **Patterns**: [Plugins and Extensions](analysis/plugins-and-extensions.md), [Productivity Tooling](analysis/tool-ecosystem.md), [MCP Patterns](analysis/mcp-patterns.md) (absorbed MCP Daily Essentials, 2026-07-10)

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
- **Patterns**: [Johari Window](analysis/orchestration-comparison.md), [Cognitive Agent Infrastructure](analysis/orchestration-comparison.md)
- **Evidence Tier**: B (Production implementation, documented methodology)

### Shipyard: Multi-Agent Orchestration for Claude Code (2026)
- **Author**: Shipyard Team
- **URL**: https://shipyard.build/blog/claude-code-multi-agent/
- **Date**: 2026-03-18 (verified 2026-05-24)
- **Description**: Comparative analysis of three multi-agent orchestrators for Claude Code — Agent Teams, Gas Town, and Multiclaude — including coordination patterns, cost considerations, and implementation tradeoffs
- **Key Contributions**:
  - Cross-orchestrator comparison post-April 2026 redesign
  - Failure recovery and message-passing patterns at enterprise scale
  - Cost framing for multi-agent topologies
- **Relevance**: Direct comparator for `analysis/orchestration-comparison.md`; provides external validation of orchestrator-choice tradeoffs
- **Evidence Tier**: B (Infrastructure platform with production users; one author, but covers three independently developed systems)
- **Patterns**: [Orchestration Comparison](analysis/orchestration-comparison.md) (framework-selection function merged in 2026-07-16)

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
- **Pattern**: Reference architecture only (see [Orchestration Comparison](analysis/orchestration-comparison.md#claude-flow-reference-only))
- **Evidence Tier**: B (Enterprise-focused documentation)

### Dapr — Distributed Application Runtime (Infrastructure-as-Runtime for Agents)
- **Author**: Dapr (CNCF graduated project); 10-LOC durable-agent demonstration by Bilgin Ibryam (Principal Product Manager, Diagrid — Dapr's commercial backer; CNCF contributor; author of *Kubernetes Patterns*)
- **URLs**:
  - https://docs.dapr.io/ (Dapr documentation — Tier A, CNCF graduated project: graduated 2024, first released 2019)
  - https://github.com/dapr/dapr-agents (Dapr Agents)
  - https://spiffe.io/ (SPIFFE workload identity — Tier A)
  - Ibryam 10-LOC durable-agent demonstration shared via LinkedIn, January 2026 (Tier B)
- **Description**: Dapr as agent infrastructure-as-runtime — durability (Workflow building block with automatic checkpointing/resume), state persistence (~30 backend options), secrets, SPIFFE-based cryptographic workload identity, OTel observability, and a Conversation API LLM abstraction (10+ providers) provided as a sidecar runtime so agent code carries only prompt/decision logic. Positions as complementary to MCP rather than competing: Dapr is the infrastructure plumbing (durability, identity, secrets), MCP is tool exposure, Skills/prompts are domain knowledge.
- **Evidence Tier**: B (CNCF graduated project with production deployments + high-credibility author; the "production durable agent in ~10 lines" figure is a single-author LinkedIn demonstration → Tier B; the ~30-backend / 10+-LLM-provider capability counts are from Dapr docs → Tier A)
- **Pattern**: [Dapr Durable Agents](analysis/dapr-durable-agents.md); complements [MCP vs Skills Economics](analysis/mcp-vs-skills-economics.md) (tool-exposure layer)
- **Provenance**: Imported + adapted into this repo (2026-05-25) from the security-data-commons-blog archive (`AGENT-03-dapr-durable-agents.md`); SDC Substack framing stripped, repo-format frontmatter added.

### MCP Context Budget Analysis
- **Author**: valgard
- **URL**: https://dev.to/valgard/claude-code-must-haves-january-2026-kem
- **Date**: January 2026
- **Description**: Production analysis of MCP tool token consumption in Claude Code
- **⚠️ Historical baseline — re-measure executed 2026-07-18.** These were pre-tool-search measurements; deferred tool definitions (auto mode default-on since v2.1.7, per-server `alwaysLoad` since v2.1.121 — version pegs corrected 2026-07-18 against the changelog; the earlier "default-on since v2.1.121" note here was wrong) mean MCP tools no longer load their full definitions into context by default. A 2026-07-18 wire measurement (JSON-RPC tools/list, chars/4 estimator; `research/probe-session-2026-07-18.md`) found 51 tools of workspace-mcp at ~28.8k est. tokens statically vs ~0.9k names-only deferred for 82 tools, confirming the 81,986-token figure is a historical static-loading data point.
- **Key Insights (as originally measured, January 2026 — see staleness flag above)**:
  - MCP tools can consume 40%+ of context (measured: 81,986 tokens at startup)
  - Sweet spot: 4 plugins + 2 MCPs
  - Recommended core MCPs: Context7 + Sequential Thinking
  - Use `disabledMcpServers` to limit per-project
  - Activate specialized MCPs on-demand, not by default
- **Patterns**: [MCP Patterns](analysis/mcp-patterns.md#mcp-context-budget-management) (absorbed MCP Daily Essentials, 2026-07-10)
- **Evidence Tier**: B (Production measurement, documented methodology; numbers stale-pending-remeasure per above)

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
- **Pattern**: [Context Engineering](analysis/harness-engineering.md#context-rot)
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
- **Pattern**: [Recursive Context Management](analysis/harness-engineering.md)
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

### "Is Grep All You Need? How Agent Harnesses Reshape Agentic Search" (arXiv:2605.15184)
- **Authors**: Sahil Sen, Akhil Kasturi, Elias Lumer, Anmol Gulati, Vamse Kumar Subbiah (PricewaterhouseCoopers U.S.)
- **Source**: [arXiv:2605.15184](https://arxiv.org/abs/2605.15184)
- **Date**: 2026-05-14 (verified 2026-05-24)
- **Description**: Empirical comparison of grep-style text search vs. vector retrieval across four agent harnesses (Chronos custom harness, Claude Code, Codex, Gemini CLI) on a 116-question LongMemEval sample. Two experiments: (1) grep vs. vector retrieval across harnesses with both inline and file-based tool-result presentation; (2) grep-only vs. vector-only with progressive injection of distracting conversation history.
- **Key Findings**:
  - "Across Chronos and the provider CLIs, grep generally yields higher accuracy than vector retrieval in our comparisons in experiment 1"
  - "Overall scores still depend strongly on which harness and tool-calling style is used, even when the underlying conversation data are the same" — i.e., harness choice has a measurable effect independent of retrieval strategy
  - Strengthens existing repo claim that for evidence-location tasks (find the symbol, trace the call, read the failing test) literal search beats embedding-similarity, and that the lazy default of starting every agent stack with embeddings deserves scrutiny
- **How discovered**: Elvis S. LinkedIn post (2026-05-16, 673 reactions) acted as pointer; only the underlying paper is cited here. The LinkedIn post itself is not registered — it adds no claim beyond the paper.
- **Pattern**: [Harness Engineering](analysis/harness-engineering.md), [Memory Systems Archetype A — Curated KB](analysis/memory-systems-archetype-a-curated-kb.md) (anti-pattern: claude-context Milvus + embeddings against a small analytical KB)
- **Evidence Tier**: B (Preprint with reproducible methodology against public LongMemEval benchmark; not yet peer-reviewed; practitioner-research affiliation)

### LangChain DeepAgents — Harness Engineering Practitioner Replication
- **Title**: "Improving Deep Agents with Harness Engineering"
- **Source**: LangChain Engineering Blog
- **Date**: February 17, 2026
- **URL**: https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering
- **Key Data**:
  - deepagents-cli moved **52.8% → 66.5%** on TerminalBench-2 (+13.7 points)
  - Ranking moved from "just outside the Top 30" to **Top 5**
  - Model held constant: **gpt-5.2-codex** (no model swap, no prompt-base change)
  - Five middleware changes documented: `PreCompletionChecklistMiddleware` (self-verification loop), `LocalContextMiddleware` (directory/tooling map at startup), loop-detection middleware (per-file edit counts to catch doom loops), reasoning-budget allocation in a "reasoning sandwich" (xhigh-high-xhigh across plan/build/verify), time-budget warnings
  - Full TerminalBench traces published publicly
- **Direct quote on harness purpose**: *"the purpose of the harness engineer: prepare and deliver context so agents can autonomously complete work."*
- **Relevance**: Independent practitioner replication of the harness-as-multiplier effect with a reproducible artifact (traces). Sits alongside Meta-Harness (arXiv:2603.28052) and SWE-Bench Mobile (arXiv:2602.09540) as the third independent corroboration of H-HARNESS-01's headline class of result.
- **Pattern**: [Harness Engineering](analysis/harness-engineering.md) — H-HARNESS-01 practitioner replication.
- **Evidence Tier**: B (Authoritative practitioner blog from an organization with deep agent-harness expertise; reproducible via public traces)

### Hoyt Emerson — CLI-over-MCP Convergence Data Point
- **Title**: "Why I built Fletch (a CLI for ADBC data transfers)"
- **Source**: LinkedIn post
- **Date**: April 7, 2026
- **URL**: Linked from [`mcp-vs-skills-economics.md`](analysis/mcp-vs-skills-economics.md) "Convergence" table; original LinkedIn post (registered alongside Vallentin, Hex, ClickHouse, Reinhard, OSS Insight as a multi-source convergence)
- **Direct quote**: *"A local CLI tool allows you to simply run commands and functions you normally would in the terminal, with the added support of using your agent to do this... if the CLI already handles auth locally... then why use an MCP server?"*
- **Why registered**: Not the strongest single source on its own. Registered because the combination — Vallentin + Hoyt + Hex shipping CLI alongside its own MCP + ClickHouse building an agent-native CLI + Reinhard + OSS Insight counting ≥6 major repos in Q1 2026 — promotes "CLI-over-MCP for many integrations" from single-practitioner observation to documented multi-source pattern.
- **Hoyt's second claim** ("agents build their tools for themselves first" — agent self-tooling): Single-practitioner observation with one emerging-tool data point (Browser Harness); **not** yet corroborated; tracked separately, not registered as a pattern claim.
- **Pattern**: [MCP vs Skills Economics — CLI + Skill Pattern Convergence](analysis/mcp-vs-skills-economics.md)
- **Evidence Tier**: B (one of multiple converging practitioner sources; pattern strength comes from convergence, not from this source alone)

### "Meta-Harness: End-to-End Optimization of Model Harnesses" (arXiv:2603.28052)
- **Authors**: Yoonho Lee, Roshen Nair, Qizheng Zhang, Kangwook Lee, Omar Khattab, Chelsea Finn (Stanford + MIT)
- **Source**: [arXiv:2603.28052](https://arxiv.org/abs/2603.28052)
- **Date**: 2026-03-30 (verified 2026-05-24)
- **Description**: Agentic outer-loop autonomously rewrites the harness by reading failed execution traces. On TerminalBench-2: 76.4% with Opus 4.6 (rank 2 among Opus agents), 37.6% with Haiku 4.5 (rank 1 among Haiku agents, outperforming Goose at 35.5%). Also produced +7.7 points on text classification using 4× fewer context tokens, and +4.7 points on IMO-level math across five held-out models.
- **Key Finding**: Paper's headline quote — "Changing the harness around a fixed large language model (LLM) can produce a 6× performance gap on the same benchmark." This is the primary source for the "Stanford 6× orchestration figure" previously cited in `harness-engineering.md` via a synthesis transcript without a verified paper URL. Both "Stanford 6×" and "Meta-Harness paper" outstanding-provenance gaps resolve to this single entry.
- **Pattern**: [Harness Engineering](analysis/harness-engineering.md) — H-HARNESS-01 hypothesis primary source.
- **Venue check (2026-07-18)**: still a v1-only preprint — no ICML 2026 entry found, and the authors' project page lists venue "Preprint"; 99 citations (Semantic Scholar) in ~3.5 months; earliest plausible venue to watch is NeurIPS 2026 (Dec).
- **Evidence Tier**: B (Preprint from established authors at top institutions; Khattab is the DSPy lead, Finn runs the Stanford Auto-Iterative Reasoning lab; not yet peer-reviewed)

### "Natural-Language Agent Harnesses" (arXiv:2603.25723)
- **Authors**: Linyue Pan, Lexiao Zou, Shuo Guo, Jingchen Ni, Hai-Tao Zheng (Tsinghua University, Shenzhen International Graduate School + Harbin Institute of Technology)
- **Source**: [arXiv:2603.25723](https://arxiv.org/abs/2603.25723)
- **Date**: 2026-03-26 (verified 2026-05-24)
- **Attribution correction**: This paper was previously cited in the repo as "Tingua NLH" — a garbled spelling of Tsinghua. Ablation numbers and the NLH vs. native-code table (30.4% → 47.2%, 1,200 → 34 LLM calls) match the citations exactly; same paper, corrected attribution.
- **Key Findings**: Verifier ablation -0.8 SWE-bench / -8.4 OSWorld; multi-candidate search -2.4 SWE-bench / -5.6 OSWorld; self-evolution +4.8 / +2.7. NLH (expressing harness logic in natural language vs. native code) lifts 30.4% → 47.2% and cuts LLM calls from 1,200 to 34. Self-evolution is the only consistently helpful ablated module.
- **Pattern**: [Harness Engineering](analysis/harness-engineering.md) — verifier-modules anti-pattern, NLH as orthogonal optimization axis.
- **Evidence Tier**: B (Preprint with reproducible ablations on public benchmarks; not yet peer-reviewed)

### "Agentic Context Engineering: Evolving Contexts for Self-Improving LMs" (arXiv:2510.04618)
- **Authors**: Zhang, Hu, Upasani et al.
- **Source**: [arXiv:2510.04618](https://arxiv.org/abs/2510.04618)
- **Venue**: ICLR 2026 poster (presented 2026-04-25); camera-ready retitled "Agentic Context Engineering: Learning Comprehensive Contexts for Self-Improving Language Models" — the arXiv page keeps the old title (verified 2026-07-18; 226 citations, Semantic Scholar floor)
- **Follow-up (registered 2026-07-18, Tier B)**: "Meta Context Engineering via Agentic Skill Evolution" ([arXiv:2601.21557](https://arxiv.org/abs/2601.21557), Ye, He, Arak, Dong, Song — a different group; v2 2026-02-11, arXiv ID verified against the abs page) uses ACE as its baseline and self-reports 5.6-53.8% relative improvement over agentic-CE methods (mean 16.9%, abstract figures; the repo README's "+18.4% offline / +33.0% online over ACE" numbers are against the authors' own ACE reimplementation, not independently verified). The authors' repo tags it "[ICML 2026]" but no proceedings entry was independently verified and the abs page carries no venue — treat as preprint-with-claimed-venue until a PMLR/icml.cc entry is confirmed; first ACE follow-up found in the 2026-07-18 sweep, a supersession-watch trigger for the ACE numbers cited here
- **Date**: Verified 2026-05-24; re-verified 2026-07-18
- **Description**: Treats agent contexts as evolving playbooks that accumulate and refine strategies across tasks; not a fixed prompt but a structured memory that compounds learnings.
- **Key Findings**: +10.6% on agent tasks and +8.6% on finance benchmarks while reducing adaptation cost. Frames context-as-evolving-artifact as a distinct optimization axis from prompt engineering, retrieval, or fine-tuning.
- **Pattern**: [Behavioral Insights](analysis/behavioral-insights.md) (Document & Clear pattern refinement), [Memory System Patterns](analysis/memory-system-patterns.md) (context as accumulating playbook).
- **Evidence Tier**: A (Peer-reviewed at ICLR 2026 — first top-venue paper explicitly validating context management as a measurable performance multiplier)

### "SWE-Bench Mobile: Can LLM Agents Develop Industry-Level Mobile Apps?" (arXiv:2602.09540)
- **Authors**: Tian, Wang, Yang et al.
- **Source**: [arXiv:2602.09540](https://arxiv.org/abs/2602.09540)
- **Date**: 2026-02-10 (verified 2026-05-24)
- **Description**: Mobile-app benchmark covering 22 agent-model configurations.
- **Key Finding**: Same model (Opus 4.5) achieves 12% on Cursor vs. 2% on OpenCode — exactly 6× — purely from scaffold differences. Independent corroboration of the Meta-Harness "6× from harness alone" claim on a separate benchmark.
- **Pattern**: [Harness Engineering](analysis/harness-engineering.md) — independent benchmark replication of H-HARNESS-01's headline figure.
- **Evidence Tier**: B (Preprint with reproducible benchmark; not yet peer-reviewed)

### "Memanto: Typed Semantic Memory with Information-Theoretic Retrieval" (arXiv:2604.22085)
- **Authors**: Abtahi, Rahnema, H. Patel, N. Patel, Fekri, Khani
- **Source**: [arXiv:2604.22085](https://arxiv.org/abs/2604.22085)
- **Date**: 2026-04-23 (verified 2026-05-24)
- **Description**: Vector-only retrieval with information-theoretic selection (not graph augmentation, not LLM-mediated ingestion) at long-horizon agent benchmark scale.
- **Key Finding**: SOTA 89.8% / 87.1% on long-horizon agent benchmarks without graph infrastructure. **Counter-signal to arXiv:2605.15184 ("grep > embeddings")**: at long-horizon scale, vector-only approaches can dominate. Scope distinction matters — the grep paper tests short-task / small-KB regimes; Memanto tests long-horizon scale where embedding cost amortizes.
- **Pattern**: [Memory Systems Archetype A — Curated KB](analysis/memory-systems-archetype-a-curated-kb.md) (scope boundary for "grep beats embeddings" claim — registered as counter-signal, not retraction).
- **Evidence Tier**: B (Preprint with reproducible methodology; not yet peer-reviewed)

### "LongMemEval-V2: Evaluating Long-Term Agent Memory" (arXiv:2605.12493)
- **Authors**: Wu, Ji, Kawatkar, Kwan, Gu, Peng, Chang
- **Source**: [arXiv:2605.12493](https://arxiv.org/abs/2605.12493)
- **Date**: 2026-05-12 (verified 2026-05-24)
- **Description**: Successor benchmark to LongMemEval ("toward experienced colleagues"); tests memory strategies under longer, more diverse agent interactions.
- **Key Finding**: "AgentRunbook-C" (store trajectories as files; use a coding agent to grep / read at query time) reaches 72.5% on environment-specific tasks, substantially outperforming retrieval-augmented baselines. Complements arXiv:2605.15184 — same direction (file-as-memory + agentic search > fixed RAG pipeline), updated benchmark.
- **Pattern**: [Memory Systems Archetype A — Curated KB](analysis/memory-systems-archetype-a-curated-kb.md), [Memory System Patterns](analysis/memory-system-patterns.md).
- **Evidence Tier**: B (Preprint with public benchmark; not yet peer-reviewed)

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
- **Agent-Driven Development**: Vallentin also reported 3x development velocity with Claude Code agent-driven workflows (LinkedIn, December 2025), providing production validation of harness engineering patterns
- **Pattern**: [MCP vs Skills Economics](analysis/mcp-vs-skills-economics.md), [Harness Engineering](analysis/harness-engineering.md)
- **Evidence Tier**: B (Production data from active project)

### Matthias Vallentin (Tenzir) — CLI + Skill Pattern for SaaS Tooling
- **Author**: Matthias Vallentin
- **Source**: LinkedIn post (2026-03-17), reference implementation [`mavam/clattio`](https://lnkd.in/dqHjgHc6)
- **Description**: Concrete extension of the "We Did MCP Wrong" thesis to SaaS tool access. Argues a four-step recipe (`OpenAPI spec → @hey-api/openapi-ts typed SDK → commander CLI → skill that teaches the agent when/how to use it`) gives agents full read-write access to APIs whose official MCP servers are read-only.
- **Worked example**: Attio CRM's official MCP server exposes browse-only operations. Vallentin's `clattio` CLI + skill pairing gives agents complete read-write access — installable via `npx skills add mavam/clattio` — with no MCP server to run.
- **Key Data**: Recipe is the deliverable (no quantitative benchmark in this post). Engagement: 28 reactions, 7 comments. Pairs with `pi` coding agent (model-agnostic) in Vallentin's setup.
- **Vendor-incentive caveat**: Vallentin's company Tenzir builds agent-friendly data tooling, so "CLI + Skill > MCP" framing aligns with commercial interest. The Attio-is-read-only observation is verifiable; the broader claim that "MCP is a solution in search of a problem" is opinion. Treat the recipe as importable; treat the categorical claim as one practitioner's framing.
- **Pattern**: [MCP vs Skills Economics](analysis/mcp-vs-skills-economics.md)
- **Evidence Tier**: B (Practitioner reference implementation with reproducible recipe; categorical anti-MCP framing is opinion)

### Nick Schrock (Dagster) - Agent-Driven Development at Scale
- **Author**: Nick Schrock, CEO of Dagster Labs
- **Source**: LinkedIn (December 2025)
- **Description**: Production evidence of agent-driven development at enterprise scale
- **Key Data**:
  - 1,000+ pull requests merged in 3 weeks using Claude Code
  - IDE used as read-only review interface, not primary authoring tool
  - Review-loop development: human specifies → agent implements → human reviews
- **Relevance**: Strongest quantitative evidence for agent-driven development thesis. Demonstrates that harness engineering (structured agent workflows) matters more than raw model capability at scale.
- **Pattern**: [Harness Engineering](analysis/harness-engineering.md)
- **Evidence Tier**: B (Production data from major open-source project CEO)

### Portfolio Analysis: Agent-Driven Development Evidence (7 Repos)

- **Author**: Jeremy Wiley (direct observation)
- **Source**: Production git history analysis across 7 repositories (April 2026)
- **Description**: Controlled comparison of agent-driven development patterns across repos with varying infrastructure maturity — from no harness (tme-mcp-server, 10% co-authored) to full harness (mndr-review-automation, 95% co-authored)
- **Key Data**:
  - 7 repos: third-brain, mndr-review-automation, health-inventory, zeek-iceberg-demo, network-visualization-services, Splunk-db-connect-benchmark, tme-mcp-server
  - Co-authoring range: 10% (no infrastructure) to 100% (full harness)
  - Commit burst peaks: 22-25 commits/day during focused agent sessions
  - Hub-spoke coordination: 4 repos tracked, 120 commits in 14 days
  - Security enforcement: PreToolUse hook blocking customer data access
  - Specialized agents: finding-reviewer (Sonnet model, restricted tools, structured coaching)
  - Infrastructure maturity model: 4 levels validated across portfolio
- **Relevance**: First-party production evidence validating harness engineering thesis across multiple project types and maturity levels. Corroborates Schrock and Vallentin claims with controlled infrastructure comparison.
- **Pattern**: [Agent-Driven Development](analysis/agent-driven-development.md)
- **Evidence Tier**: A (Primary production observation)

### Portfolio Analysis: Local+Cloud LLM Orchestration

- **Author**: Jeremy Wiley (direct observation)
- **Source**: Production analysis of mndr-review-automation hybrid LLM pipeline (April 2026)
- **Key Data**: MLX/Gemma 4 31B local inference, Claude Sonnet cloud coaching, 10 tokenization entity types, 7 hallucination scrubbers, 1,216 tests, supply chain security (litellm rejected)
- **Pattern**: [Local+Cloud LLM Orchestration](archive/local-cloud-llm-orchestration.md) (evicted to archive/ with tombstone, 2026-07-10 — spoke-repo content, see `drafts/REDUCTION-PROPOSAL-2026-07.md` Phase 5)
- **Evidence Tier**: A (Primary production observation)

### Portfolio Analysis: MCP Client Integration Patterns

- **Author**: Jeremy Wiley (direct observation)
- **Source**: Production analysis of InspectorClient, TmePlaybookClient, and TME MCP server (April 2026)
- **Key Data**: JSON-RPC 2.0 over Streamable HTTP, Mcp-Session-Id lifecycle, localhost-only enforcement, two server architectures (structured tools vs orchestrated playbooks)
- **Pattern**: [MCP Client Integration](analysis/mcp-client-integration.md)
- **Evidence Tier**: A (Primary production observation)

### Portfolio Analysis: Federated Query Architecture

- **Author**: Jeremy Wiley (direct observation)
- **Source**: Production analysis of zeek-iceberg-demo + third-brain federation hypothesis (April 2026)
- **Key Data**: 15/15 benchmark queries pass (<10s), 93-99.9% WAN reduction, 86-99% cost savings, 20M OCSF events, TCO calculator validated
- **Pattern**: [Federated Query Architecture](archive/federated-query-architecture.md) (evicted to archive/ with tombstone, 2026-07-10 — spoke-repo content, canonical numbers now live in `~/sdw-lab-benchmarks`)
- **Evidence Tier**: A (Primary production observation)

### Portfolio Analysis: Automated Config Assessment

- **Author**: Jeremy Wiley (direct observation)
- **Source**: Production analysis of health-inventory deviation engine + H-CONFIG-01 hypothesis (April 2026)
- **Key Data**: 3,816+ sensors, 12/12 ground truth detection (100%), 5-dimension YAML baseline, LLM remediation, confidence 4.7/5
- **Pattern**: [Automated Config Assessment](analysis/automated-config-assessment.md)
- **Evidence Tier**: A (Primary production observation)

### Portfolio Analysis: Progressive Disclosure, Memory, Revalidation, Pipeline, Synchronization

- **Author**: Jeremy Wiley (direct observation)
- **Source**: Cross-portfolio analysis of CLAUDE.md evolution, memory systems, revalidation patterns, security pipelines, and dependency cascading (April 2026)
- **Key Data**: 6 repos with CLAUDE.md (42-209 lines), 5 repos with memory systems (2-13 files), hypothesis confidence tracking (3.0→4.7/5), Zeek→OCSF pipeline, 4-phase enrichment cascade
- **Patterns**: [CLAUDE.md Progressive Disclosure](analysis/claude-md-progressive-disclosure.md), [Memory System Patterns](analysis/memory-system-patterns.md), [Evidence-Based Revalidation](analysis/evidence-based-revalidation.md), [Security Data Pipeline](archive/security-data-pipeline.md) (evicted to archive/ with tombstone, 2026-07-10 — canonical Zeek→OCSF numbers now live in `~/sdw-lab-benchmarks`), [Cross-Project Synchronization](analysis/cross-project-synchronization.md)
- **Evidence Tier**: A (Primary production observation)

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
- **Pattern**: [Agentic Retrieval](analysis/domain-knowledge-architecture.md)
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

### VoltAgent/awesome-claude-code-subagents
- **Author**: VoltAgent community
- **URL**: https://github.com/VoltAgent/awesome-claude-code-subagents
- **Stars**: 20.4k (verified 2026-05-24); active commits May 2026
- **Description**: Curated collection of 131+ specialized Claude Code subagents organized across 10 categories — core development, language specialists, infrastructure, quality & security, data & AI, developer experience, specialized domains, business & product, meta-orchestration, research & analysis
- **Key Contributions**:
  - Ecosystem-scale validation of the subagent pattern (community curation, not vendor catalog)
  - Reference implementations for category-specific subagent design
  - Active maintenance signal (commits in the current month)
- **Relevance**: Validates real-world adoption of the subagent architecture documented by Anthropic; useful comparator for `analysis/orchestration-comparison.md` claims about subagent ROI
- **Evidence Tier**: B (community curation at scale; 20k+ stars indicates production adoption)
- **Patterns**: [Orchestration Comparison](analysis/orchestration-comparison.md), [Plugins and Extensions](analysis/plugins-and-extensions.md)

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
- **⚠️ Attribution corrected 2026-07-18 — the 114K/27K (4x) pairing is unsupported.** It appears in neither microsoft/playwright-cli's README (current, nor the late-Feb-2026 state at commit fa6f6bc) nor the playwright.dev/agent-cli docs; no Microsoft-published measurement was found. Earliest pairing found: a Medium post (2026-02-24) asserting unlinked "Microsoft's benchmarks" (its author's own run: ~89K vs ~24K, ~3.7x); later sources cite that post in a citation loop. The one independent benchmark found (Outpost/Ranger 2026-04-03): ~2x tokens saved, MCP ~2x faster wall-clock. playwright-mcp v0.0.78 (2026-07-09, distilled snapshots) stales all earlier MCP-side workflow measurements. Cite as community benchmarks, ~2-3.7x task-dependent, Tier C. (The prior note's tool-search rationale was also misapplied — definitions-deferral and per-call output are orthogonal levers.)
- **Key Insights (as originally measured, February 2026 — see staleness flag above)**:
  - 4x token reduction vs Playwright MCP (~27K vs ~114K tokens per task)
  - Saves snapshots/screenshots to disk instead of streaming into context
  - Compact element references (e.g., `e21`) instead of full DOM trees
  - 50+ commands: navigation, interaction, screenshots, session management
  - `--skills` flag installs documentation for agent discovery
- **Pattern**: [MCP Patterns - CLI vs MCP](analysis/mcp-patterns.md#cli-vs-mcp-the-token-efficiency-case)
- **Evidence Tier**: B (Microsoft, measured benchmarks, 3.6k stars) ✅ Verified

### affaan-m/ECC (renamed from everything-claude-code)
- **URL**: https://github.com/affaan-m/everything-claude-code (the repo was RENAMED to **ECC** — the old slug redirects; verified 2026-07-16)
- **Stars**: 230,304 as verified 2026-07-16 (GitHub API); pushed 2026-07-14
- **Author**: Affaan Mustafa (Anthropic Hackathon Winner)
- **⚠️ Naming hazard (2026-07-16)**: `worldflowai/everything-claude-code` is an unrelated minor project, and several high-star forks mirror affaan-m's repo — always pin the **affaan-m** owner when citing or installing.
- **Description**: Maximalist Claude Code plugin ecosystem with agents, skills, commands, and rules for 12 language ecosystems, built over 10+ months of daily production use. **Component counts quarantined (2026-07-16)**: the circulating 28 agents / 119 skills / 60 commands figures come from secondary pages and are unverified against the repo tree — see the Unverified section; treat any specific count as directional.
- **Key Contributions**:
  - **Agent auto-delegation**: Complex requests auto-route to specialized agents (planner, code-reviewer, tdd-guide, architect, build-error-resolver)
  - **Continuous learning pipeline**: Sessions → instincts (confidence-scored) → skills via `/learn` → `/evolve` → `/prune`
  - **Context budget management**: MCP discipline (limit to 5-6 active per project), context budget tracking, model routing (Haiku/Sonnet/Opus)
  - **12 language ecosystems**: TypeScript, Python, Go, Swift, PHP, Java, Kotlin, Rust, C++, Perl with language-specific rules, agents, and skills
  - **Industry-specific skills**: Logistics, customs compliance, energy procurement, production scheduling
  - **Hook runtime profiles**: `ECC_HOOK_PROFILE=standard|minimal|strict` with env-var disabling of individual hooks
  - **Multi-platform**: Claude Code, Cursor, Codex, OpenCode, Antigravity IDE
- **Philosophy**: Maximalist platform tuning — Claude becomes more effective with a rich pre-built library that automatically delegates, learns, and optimizes
- **Relevance**: Largest community Claude Code configuration ecosystem; validates patterns documented in this project at scale; complementary approach (batteries-included vs evidence-based guidance)
- **Evidence Tier**: B (Open source, large community star count — see repo for current figure, production-validated across 10+ months, Anthropic hackathon winner)
- **Patterns**: [Plugins and Extensions](analysis/plugins-and-extensions.md), [Harness Engineering](analysis/harness-engineering.md)

### obra/superpowers
- **URL**: https://github.com/obra/superpowers
- **Version / liveness**: v6.1.1 (2026-07-02); 255,877 stars / 22,790 forks as verified 2026-07-16 (GitHub API); pushed daily, 628 commits
- **Description**: Framework plugin equipping AI coding agents with structured workflows (brainstorming, TDD, systematic debugging, subagent coordination)
- **Skill set (enumerated 2026-07-16)**: brainstorming, dispatching-parallel-agents, executing-plans, finishing-a-development-branch, receiving-code-review, requesting-code-review, subagent-driven-development, systematic-debugging, test-driven-development, using-git-worktrees, using-superpowers, verification-before-completion, writing-plans
- **Key Methodologies**:
  - **RED-GREEN-REFACTOR TDD**: Strict test-first enforcement; deletes code written before tests
  - **Systematic Debugging**: 4-phase root-cause process (vs ad-hoc troubleshooting)
  - **Brainstorming → Design → Plan → Execute**: Collaborative design before implementation
  - **Subagent-driven development**: Fresh agents per task with two-stage review
  - **YAGNI + DRY enforcement**: Planning phase emphasis
  - **Git worktrees**: Isolated development per feature
- **Multi-platform Support**: Claude Code, Cursor, Codex, OpenCode
- **Substance check (2026-07-16)**: NO security skill (OWASP = 0 hits, CVE = 0 hits — the `secure-code-generation.md` advance trigger has not fired), NO "bitter lesson" content, NO framework comparison. Superpowers is a compared *object* in [orchestration-comparison.md](analysis/orchestration-comparison.md), not a comparator, so it does not absorb the comparison or the Bitter-Lesson diagnostic. Its two-stage review varies *what* is reviewed on the same weights — distinct from the Wiggins cross-model-family review (which varies *whose weights* review; see the Wiggins entry under Loop Engineering), so that delta stands.
- **Pattern Overlap**: This project independently implements equivalent patterns (tdd-enforcer skill, systematic-debugger skill, subagent-orchestration, planning-first-development) — re-verified accurate at v6.x (2026-07-16)
- **Relevance**: Reference implementation demonstrating skills-based workflow automation; validates this project's pattern documentation; carries the methodology lane in the seven-lane ecosystem (README § Where This Sits)
- **Evidence Tier**: B (Open source framework with cross-platform adoption)
- **Pattern**: [Plugins and Extensions](analysis/plugins-and-extensions.md), [Harness Engineering](analysis/harness-engineering.md), [Orchestration Comparison](analysis/orchestration-comparison.md)

### Prompt Engineering YouTube Channel
- **URL**: https://www.youtube.com/@engineerprompt
- **Video**: ["The AI Model Doesn't Matter Anymore"](https://www.youtube.com/watch?v=1Ohf2aeSPFA) (February 2026)
- **Key Thesis**: Raw model capability is commoditizing; the harness (infrastructure around the agent) determines outcomes. Introduces "harness engineering" as the defining discipline of 2026.
- **Key Evidence Cited**:
  - Frontier models: 90%+ on benchmarks, 24% on real professional tasks
  - Vercel text-to-SQL: removing 80% of tools improved accuracy 80% → 100%, reduced tokens 60%, 3.5x speed
  - Manus: 5 rebuilds in 6 months, biggest gains from removing features
  - Three properties of a good harness: deterministic replay, observable boundaries, behavioral contracts
  - Richard Sutton's "Bitter Lesson" applied to agents: harness should get simpler as models improve
- **Evidence Tier**: B (Detailed analysis with multiple cited studies and experiments)
- **Pattern**: [Harness Engineering](analysis/harness-engineering.md), [Domain Knowledge Architecture](analysis/domain-knowledge-architecture.md)

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
| **Crush** | [charmbracelet/crush](https://github.com/charmbracelet/crush) | Go-based, model-agnostic, MCP support (22.9k stars) | Multi-provider terminal agent |

- **Pattern**: [Tool Ecosystem](analysis/tool-ecosystem.md)

### External Memory Systems

| Tool | Repository | Architecture | Use Case |
|------|------------|-------------|----------|
| **MemPalace** | [memorylake-ai/mempalace](https://github.com/memorylake-ai/mempalace) | ChromaDB + SQLite, 19 MCP tools (43k stars) | Local-first cross-session memory via MCP |
| **Honcho** | [plastic-labs/honcho](https://github.com/plastic-labs/honcho) | FastAPI + PostgreSQL + pgvector, v3.0.6 (2.2k stars) | Multi-agent shared state, background reasoning |

- **Pattern**: [Memory System Patterns](analysis/memory-system-patterns.md#external-memory-systems-april-2026)

### Local LLM Ecosystem Updates (April 2026)

| Development | Source | Key Impact |
|-------------|--------|------------|
| **Gemma 4 26B MoE** | [Google DeepMind](https://blog.google/technology/developers/gemma-4/) (April 2, 2026) | 3.8B active params, 256K context, native function calling. 86.4% tau2-bench (agentic tool use). Available via `ollama run gemma4:26b` |
| **Ollama v0.19 MLX** | [Ollama Release Notes](https://github.com/ollama/ollama/releases) (March 27, 2026) | Native Apple MLX backend on Apple Silicon. Narrows the gap between direct MLX and Ollama for local inference |

- **Pattern**: [Local+Cloud LLM Orchestration](archive/local-cloud-llm-orchestration.md#model-alternatives-gemma-4-26b-moe-april-2026) (evicted to archive/ with tombstone, 2026-07-10), [Tool Ecosystem](analysis/tool-ecosystem.md#ecosystem-development-ollama-v019-mlx-backend-march-2026)

### Context Extraction Tools

| Tool | Repository | Purpose |
|------|------------|---------|
| **repomix** | [yamadashy/repomix](https://github.com/yamadashy/repomix) | Pack repository into AI-friendly single file |
| **code2prompt** | [mufeedvh/code2prompt](https://github.com/mufeedvh/code2prompt) | Token-optimized codebase context extraction |

- **Pattern**: [Context Engineering](analysis/harness-engineering.md)

### Agentic Retrieval Tools

| Tool | Repository | Purpose |
|------|------------|---------|
| **agentic-file-search** | [PromtEngineer/agentic-file-search](https://github.com/PromtEngineer/agentic-file-search) | Dynamic document exploration with LlamaIndex Workflows + Gemini |

- **Key Features**: Three-phase exploration (scan/dive/backtrack), 6 filesystem tools, multi-format support (PDF, DOCX, PPTX), ~$0.001/query
- **Pattern**: [Agentic Retrieval](analysis/domain-knowledge-architecture.md)

### AI Asset Generation Tools

| Tool | Repository | API | Purpose |
|------|------------|-----|---------|
| **google-image-gen-api-starter** | [AI-Engineer-Skool/google-image-gen-api-starter](https://github.com/AI-Engineer-Skool/google-image-gen-api-starter) | Google Gemini | CLI for image generation with style templates |

- **Pattern**: [AI Image Generation](analysis/tool-ecosystem.md), [Tool Ecosystem](analysis/tool-ecosystem.md)

### Session Quality Diagnostic Tools

> **⚠️ SUPERSEDED (2026-07-10)**: native `claude doctor` (v2.1.205, 2026-07-08 — "a full setup checkup that can diagnose and fix issues," `/checkup` alias) now covers this ground first-party. `analysis/session-quality-tools.md` completed its `RETIRING → RETIRED` cycle and is archived at [`archive/session-quality-tools.md`](archive/session-quality-tools.md); this repo's own audit signal command moved from `npx -y claude-doctor` to `claude doctor`. Entry kept for provenance — the AFINN-165 sentiment/heuristic methodology below is a still-valid Tier-B-underlying technique, just no longer this repo's active tool.

| Tool | Repository | Purpose |
|------|------------|---------|
| **claude-doctor** (community, superseded) | [aidenybai/claude-doctor](https://github.com/aidenybai/claude-doctor) | Session transcript analysis via AFINN-165 sentiment + heuristic pattern detection |

- **Author**: Aiden Bai
- **Version**: v0.0.3 (April 2026)
- **Evidence Tier**: C (Tool methodology — self-published, unvalidated thresholds)
- **Underlying Library**: AFINN-165 sentiment lexicon (Tier B — peer-reviewed, 2,477 words scored -5 to +5)
- **Key Capabilities**: Edit-thrashing detection (5+ edits/file), error-loop detection (3+ consecutive failures), sentiment analysis, repeated-instruction detection (60% Jaccard similarity)
- **Limitations**: Arbitrary severity weighting, no positive signal detection, no task-type normalization, percentage score not calibrated
- **Analysis**: [Session Quality Diagnostic Tools (archived)](archive/session-quality-tools.md)

---

## Spec-Driven Development Standards (Tier A)

These represent the industry-standard methodologies for AI-driven development that this repository adopts:

### GitHub Spec Kit (Foundational)
- **Author**: GitHub
- **URL**: https://github.com/github/spec-kit
- **Stars**: point-in-time count dropped 2026-07-10 (was "59,000+ as of Jan 2026" — follow the link for the current count)
- **License**: MIT
- **Description**: Tool-agnostic toolkit for spec-driven development with AI coding agents
- **Key Concepts**:
  - 4-phase workflow: Specify → Plan → Tasks → Implement
  - Constitution command for project governing principles
  - Supports 16+ coding agents including Claude Code
- **Pattern**: [Spec-Driven Development](analysis/harness-engineering.md)
- **Evidence Tier**: A (Industry standard, large sustained star count and community adoption — see repo for current figure — adopted by this repository as foundational methodology)

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
- **Pattern**: [Spec-Driven Development](analysis/harness-engineering.md)
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
- **Pattern**: [Spec-Driven Development](analysis/harness-engineering.md)
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

#### 2026 Updates

- **"Top 2% Agentic Engineering" Roadmap** ([agenticengineer.com/top-2-percent-agentic-engineering](https://agenticengineer.com/top-2-percent-agentic-engineering), March 2026):
  - Central thesis: "2026 is the year of trust" — every prediction comes down to *do you trust your agents?*
  - Multi-agent mandate: "Stop running a single Claude Code instance and start running three, five, ten, or hundreds."
  - Agent sandboxes are essential — "running agents unconstrained is how you delete your device, leak your API keys"
  - Fine-tuned specialization: "When you fine-tune an agent to solve one problem extraordinarily well, your trust in that agent skyrockets"
- **Agent-scoped hooks**: Hooks embedded in agents/skills, not just global settings.json — evolution from global to local hook control
- **Builder/Validator agent teams**: Separation of concerns via agent config (builder = full access, validator = read-only)

#### Open Source Artifacts

| Repository | Purpose | Relevance |
|------------|---------|-----------|
| [single-file-agents](https://github.com/disler/single-file-agents) | Single-purpose Python agents demonstrating precise prompt patterns | Reference for minimal, focused agent design |
| [indydevtools](https://github.com/disler/indydevtools) | Agentic engineering toolbox for autonomous problem-solving | Multi-agent architecture patterns |
| [claude-code-hooks-multi-agent-observability](https://github.com/disler/claude-code-hooks-multi-agent-observability) | Real-time monitoring for parallel Claude Code agents | Production observability patterns |
| [infinite-agentic-loop](https://github.com/disler/infinite-agentic-loop) | Two-prompt system for continuous agent operation | Advanced orchestration patterns |
| [claude-code-hooks-mastery](https://github.com/disler/claude-code-hooks-mastery) (3.4K stars, March 2026) ⚠️ stale — no push since 2026-03-04 (verified 2026-07-16, GitHub API); do not cite for current hook behavior | Comprehensive tutorial covering all 13 hook lifecycle events | UV single-file script pattern, deterministic hook control |
| [pi-vs-claude-code](https://github.com/disler/pi-vs-claude-code) (555 stars, March 2026) | Open-source Pi agent vs Claude Code comparison | Cross-agent config portability |
| [the-library](https://github.com/disler/the-library) (270 stars, March 2026) | Meta-skill for private-first distribution of agentic capabilities | Skill distribution across agents/devices/teams |

#### Advanced Concepts (TAC Course)

- **Orchestrator Agent**: "The one agent to rule them all" - single interface to command agent fleets
- **Agent Experts**: Solve "agents forget" with Act → Learn → Reuse workflow
- **7-Level Prompt Hierarchy**: From simple prompts to self-improving meta prompts
- **Agentic Layers**: Building blocks leading to "The Codebase Singularity"

- **Influence on This Repo**:
  - Direct validation of SDD methodology from practitioner perspective
  - Context-Prompt-Model framework reinforces specs-as-context pattern
  - "Great Planning" principle documented in [Planning-First Development](analysis/harness-engineering.md)
  - Orchestrator pattern informs [Subagent Orchestration](analysis/orchestration-comparison.md)
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
  - Domain knowledge embedding documented in [Skills for Domain Knowledge](analysis/domain-knowledge-architecture.md)
  - Phase-based skill separation reinforces progressive disclosure pattern
  - Non-engineering use cases validate SDD for knowledge work beyond software
- **Evidence Tier**: A (PhD research rigor + production ML engineering + actionable best practices with measured outcomes)

---

## Foundational Influences (Tier B)

These sources directly influenced the design of the skill structure and project scaffolding patterns in this repository:

### MCP Security Surveys and CLI-vs-MCP Benchmarks (2026-07-18 reverification)

- **BlueRock MCP Trust Registry** — [product page](https://www.bluerock.io/products/mcp-trust-registry) (page dated 2026-07-17). 42% of 12,000+ scanned public MCP servers with command-injection flaws (earlier snapshot: 43% of 10,000+), 33% SSRF, 6% critical, methodology disclosed only as "22+ security rules". **Tier C** (vendor product page marketing BlueRock's own registry — flag bias; the disclosed N is why it replaces Equixly as the cited source, not a tier upgrade). Different population and method from Equixly's 2025 popularity-selected pen-test, so context for the rate, not a replication.
- **Equixly — "MCP Servers: The New Security Nightmare"** — [blog](https://equixly.com/blog/2025/03/29/mcp-server-new-security-nightmare/) (2025-03-29, Alessio Dalla Piazza). Historical origin of the ~43% figure; sample size never disclosed. Tier C.
- **Adjacent vulnerability surveys** (landscape context only — different vulnerability classes, relayed via one Tier C roundup [Practical DevSecOps 2026-06-26](https://www.practical-devsecops.com/mcp-security-statistics-2026-report/), primaries unverified): Enkrypt AI 33% critical of 1,000 (Oct 2025); Endor Labs 82% path traversal of 2,614 (2025); Hasan et al. 5.5% tool poisoning of 1,899 (2025).
- **Ecosystem size (mid-2026, listing counts — dedup-dependent, include duplicates/abandonware)**: PulseMCP 22,300+ (verified 2026-07-18); mcp.so ~20,222 (Apr 2026); Glama ~22,775 (May 2026); official registry 9,652 latest records at SafeDep's 2026-05-24 API pull (~3,012 unique servers in a Mar 2026 count).
- **Outpost/Ranger — "The Hidden Cost of Fewer Tokens"** — [post](https://outpost.ranger.net/post/the-hidden-cost-of-fewer-tokens/) (2026-04-03). The one independent Playwright CLI-vs-MCP benchmark found: ~50-70K MCP vs ~19-45K CLI tokens (~2x) on Mozilla.org tasks, with MCP ~2x faster wall-clock (CLI needed 2-3x more tool calls). **Tier B** (documented independent measurement, single task set).

### Nate B. Jones - AI Implementation Patterns
- **Author**: Nate B. Jones
- **Substack**: https://natesnewsletter.substack.com
- **Website**: https://www.natebjones.com/
- **Description**: AI strategist and former Head of Product at Amazon Prime Video. Created the "Memory Prompts" methodology and extensive documentation of AI implementation patterns from 100+ production builds.

#### Key Articles (used in this repo)

| Article | Pattern | Key Insights |
|---------|---------|--------------|
| [Beyond the Perfect Prompt](https://natesnewsletter.substack.com/p/beyond-the-perfect-prompt-the-definitive) | [Context Engineering](analysis/harness-engineering.md) | Deterministic vs probabilistic context, correctness over compression |
| [2025 Agent Build Bible](https://natesnewsletter.substack.com/p/why-your-ai-breaks-in-production) | [Agent Principles](analysis/agent-principles.md) | 6 principles for production AI, semantic validation |
| [MCP Implementation Guide](https://natesnewsletter.substack.com/p/the-mcp-implementation-guide-solving) | [MCP Patterns](analysis/mcp-patterns.md) | 7 failure modes, Intelligence Layer/Sidecar/Batch patterns. ⚠️ Provenance corrections 2026-07-18: the guide's "~43% command injection" figure is Equixly's (the guide's "Docker data" attribution was a mis-citation), and its "only ~10 of 5,960+ trustworthy" line was the author's editorial judgment over PulseMCP's mid-2025 count — withdrawn from this repo as never-a-measurement (see MCP Security Surveys below) |
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

#### 2026 Updates

- **OB1 "Open Brain"** ([github.com/NateBJones-Projects/OB1](https://github.com/NateBJones-Projects/OB1), March 11, 2026):
  - Open-source MCP-based shared memory infrastructure with PostgreSQL + pgvector
  - SHA-256 content fingerprinting for deduplication; atomic embeddings (Zettelkasten-style)
  - Hub-and-spoke model: one central database, multiple AI tools connect via MCP
  - Four well-scoped MCP tools (semantic search, browse recent, stats, capture)
  - Row-level security for multi-user isolation; cost: $0.10-$0.30/month on free tier
  - Design principle: "Memory as infrastructure, not a feature — you own the data, not a platform"
  - Concrete implementation of the Memory Architecture pattern documented in this repo
- **Specification Gap** ([Substack, January 21, 2026](https://natesnewsletter.substack.com/p/tool-shaped-vs-colleague-shaped-ai)):
  - "Claude Code = colleague-shaped; Codex = tool-shaped. Know which you need."
  - Senior engineers gravitate toward Codex (well-specified tasks); juniors prefer Claude Code (conversational friction catches errors)
  - "The Specification Gap" — teams overestimate their ability to specify precise intent
- **Identity Shift** ([Substack, January 23, 2026](https://natesnewsletter.substack.com/p/6-practices-for-when-the-models-got)):
  - Bottleneck shifts from agents to keeping them fed with work
  - Identity shift: from "person who writes code" to "person who specifies, reviews, and orchestrates"
- **Claude Code Without the Code** ([Substack, updated March 17, 2026](https://natesnewsletter.substack.com/p/claude-code-without-the-code-the)):
  - 64-page guide to non-coding agent workflows (legal, research, document automation)
  - Positions Claude Code as "a general purpose AI agent hiding under the guise of just being a coding agent"
- **Note**: Primary website is **natebjones.com** (not nateb.xyz)

### Daniel Miessler - Fabric Framework & PAI (Personal AI Infrastructure)
- **Author**: Daniel Miessler
- **GitHub**: https://github.com/danielmiessler/fabric
- **Website**: https://danielmiessler.com
- **Description**: Security professional and creator of Fabric, an open-source framework for augmenting humans using AI. Re-fetched 2026-06-21: **v1.4.455 (June 9 2026), 42.5k stars, 4.2k forks, 200+ patterns**, CLI + REST API. 2026 changelog: Opus 4.7 1M-context (v1.4.447, Apr 16), OpenAI Codex backend (v1.4.437, Mar 16), Azure AI Gateway (v1.4.417, Feb 21), M365 Copilot (v1.4.380, Jan 15).
- **Key Concepts**:
  - **Scaffolding > Models**: "The scaffolding matters more. Building great scaffolding requires tons of user empathy."
  - **Spec-Driven Development**: Structured project evolution with clear specifications
  - **Pattern Structure**: actual pattern-file headers are **"IDENTITY and PURPOSE / OUTPUT SECTIONS / OUTPUT INSTRUCTIONS / INPUT"** (verified at `data/patterns/.../system.md` 2026-06-21). The repo's earlier shorthand "IDENTITY/GOAL/STEPS/OUTPUT" is a close paraphrase — the structured-template claim holds, the exact section names differ.
  - **PAI (Personal AI Infrastructure)**: multi-workflow architecture (kebab-case workflows; SKILL.md-as-dispatcher routing; progressive disclosure; 200-500-line workflow guidelines).
- **⚠️ Verification note (2026-06-21)**: the current `danielmiessler/fabric` README does NOT contain the slogan "Solve Once, Reuse Forever," the "200+/300+ contributors" count, or any PAI mention — those were likely lifted from older README text. The "240+ patterns" figure exists on `danielmiessler.com/telos`, not the Fabric README. Treat the slogan + counts as unverified against this URL (see Unverified section); the modular-reuse *philosophy* itself is uncontested.
- **Influence on This Repo**:
  - Skill template structure adapted from Fabric patterns (modular, composable AI behaviors)
  - Multi-workflow pattern for complex skills (ultrathink-analyst, git-workflow-helper examples); kebab-case naming standard

#### Miessler 2026 — TELOS, PAI 5.0, and LifeOS
- **"10 Prompts to Run When Fable Comes Back"** (`danielmiessler.com/blog/prompts-to-run-when-fable-comes-back`, 2026-06-18, Tier C, verified 2026-06-21): the body contains **15** distinct numbered prompts (Harness Optimization 6, Security 2, Life/Work 5, Development 1, Public Presence 1 = 15). Count framing corrected 2026-07-12: the verified primary carries 15, and the "16" count circulating in local materials includes a 16th prompt that is not on the page — if a 16th is kept locally it gets an explicit local-origin label rather than attribution to Miessler. Framing: prioritize META / system-level work over task-level; queue the highest-leverage strategic prompts for the strongest model. "Fable" = shorthand for any top-capability model ("Fable is just the temporary hotness"). "Ultracode" = a code word for "going super hard." The Development prompt is Peter Steinberger's loop prompt.
- **TELOS** (`danielmiessler.com/telos`, date unknown, Tier C, verified 2026-06-21): structure Problems (P0-P4), Strategies (S0/S4), Missions (M0-M2). **Correction**: P0 is "Human Activation Crisis" (~99.9% of humans "not activated"), NOT "human vulnerability to AI." Names PAI ("Personal AI Infrastructure") and Fabric ("AI augmentation framework with **240+** prompt patterns"). The "Telos files live at USER/TELOS/" claim is NOT on this page — quarantined.
- **PAI 5.0 "Life Operating System"** (`danielmiessler.com/blog/announcing-pai-5-life-operating-system`, 2026-04-30, Tier C, verified 2026-06-21): three layers (PAI framework / Pulse dashboard / Digital Assistant); "The Algorithm v6.3.0" — seven phases OBSERVE/THINK/PLAN/BUILD/EXECUTE/VERIFY/LEARN, effort tiers E1-E5; Memory v7.6 — three surfaces WORK/LEARNING/KNOWLEDGE (KNOWLEDGE = typed graph), BM25 retrieval; subagents Engineer/Architect/Designer (Anthropic) + Forge (GPT-5.4) + Anvil (Kimi K2.6) + Cato (cross-vendor auditor); five-inspector security pipeline (Pattern/Egress/Rules/Prompt/Injection).
- **LifeOS 6.0.2 rename** (`github.com/danielmiessler/LifeOS`, 2026-07-02, Tier B — cross-verified 2026-07-10 against the GitHub repo + README + Releases page). PAI is renamed **LifeOS** ("A General Purpose AI Harness for magnifying human capabilities" — "a life and work optimization platform, not just a coding harness"); v6.0.2 carries the PAI→LifeOS rename through code identifiers and doc prose (runtime-critical paths/regexes left byte-identical on purpose, so nothing breaks) and ships as skill-only distribution — "the whole system ships as one self-contained `LifeOS/` skill" with an AI-native, markdown-first install (`Read https://ourlifeos.ai/install and install LifeOS for me`). Current architecture, consolidating the PAI 5.0 entry above: **Algorithm v6.x** — the same OBSERVE→THINK→PLAN→BUILD→EXECUTE→VERIFY→LEARN loop, now gated by verifiable **Ideal State Criteria** at each phase (a check the phase must satisfy before advancing, not just a status report); **Memory v7.x** — the same three typed surfaces (WORK/LEARNING/KNOWLEDGE); deterministic lifecycle hooks; **45 composable skills**. Stated stance (this repo's synthesis of the framing, not a direct quote): extend Claude Code as the runtime rather than build parallel infrastructure — LifeOS sits on top of Claude Code's own hooks/skills/subagents rather than replacing them, which is the same thesis this repo's 2026-07-10 reduction pass applies to itself. **Supersedes** the TELOS/SPQA entry above (§ Primary Sources) as the current statement of Miessler's architecture; that entry stays for provenance.
  - **Evidence Tier**: B (named practitioner, public repo with verifiable release history, cross-checked against a second source)
  - **Follow-lane check (2026-07-16 absorption wave)**: no analysis doc `follows:` Miessler as canon — [intent-alignment-audit.md](analysis/intent-alignment-audit.md)'s lane is `none found` (Miessler is diagnosis-inspiration; LifeOS's Ideal State Criteria is convergent design, not a coding-team audit instrument). Advance trigger stays: LifeOS or superpowers shipping a standing intent-audit workflow.
  - **Revalidate by**: 2026-10-10

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
- **Relevance**: Production implementation of concepts in [Memory Architecture](analysis/memory-system-patterns.md) and [Long-Running Agent](analysis/harness-engineering.md)
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
- **Relevance**: Reference implementation for [Session Learning](analysis/memory-system-patterns.md) pattern
- **Evidence Tier**: B (Expert practitioner with academic research basis)

### Claude Reflect (Hook-Based Learning)
- **Author**: Bayram Annakov
- **URL**: https://github.com/BayramAnnakov/claude-reflect
- **Description**: Hook-based automatic correction detection for Claude Code
- **Key Features**:
  - Automatic detection of correction patterns ("no, use X", tool rejections)
  - Queued learnings reviewed via `/reflect` command
  - Plugin ecosystem integration
- **Relevance**: Alternative implementation for [Session Learning](analysis/memory-system-patterns.md) pattern
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
- **Relevance**: Alternative approach for [Session Learning](analysis/memory-system-patterns.md) pattern
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
- **Stars**: point-in-time count dropped 2026-07-10 (was "12.6k+ as of Dec 2025" — follow the link for the current count)
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
- **Relevance**: Foundational research for [Session Learning](analysis/memory-system-patterns.md) pattern
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
- **Relevance**: Critical risk documentation for [Session Learning](analysis/memory-system-patterns.md) pattern
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

These sources document the Self-Evolution Algorithm (TTD-DR) used in the [Recursive Evolution](analysis/evidence-based-revalidation.md) pattern:

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

### ClaudeLog — Community Mechanics Documentation
- **Author**: InventorBlack (Anthropic Developer Ambassador, r/ClaudeAI moderator)
- **URL**: https://claudelog.com
- **Evidence Tier**: C, with an author-authority note — the ambassador role and moderation standing lift confidence in the mechanics explanations, but the site publishes no measured data, so C is the honest tier
- **Added**: 2026-07-16 (absorption-wave sweep; site active as of 2026-07-16)
- **Description**: Actively-updated community documentation of Claude Code mechanics — CLAUDE.md behavior, plan mode, ultrathink, subagents, agent-first design. This is the mechanics-explainer lane in the seven-lane ecosystem (README § Where This Sits).
- **Followed canon (`follows:` lane, 2026-07-16)**: [behavioral-insights.md](analysis/behavioral-insights.md) follows ClaudeLog for the mechanics-explainer function. Retained delta: ClaudeLog does not publish measured adherence/threshold data — the quantified findings (~80% CLAUDE.md adherence, 60% context threshold, ~150-instruction budget) remain this repo's own instrument. Advance trigger: ClaudeLog or Anthropic publishing measured adherence/threshold data.
- **Pattern**: [Behavioral Insights](analysis/behavioral-insights.md)

### Curated Lists (Primary Review Sources)

| Repository | Status | Stars | Focus | Priority |
|------------|--------|-------|-------|----------|
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | ✅ Verified (active, pushed 2026-07-16) | — (snapshot counts dropped per the 2026-07-10 convention) | Commands, workflows, patterns | HIGH |
| [jqueryscript/awesome-claude-code](https://github.com/jqueryscript/awesome-claude-code) | 🔍 Discovered | - | Tools, IDE integrations | HIGH |
| [josix/awesome-claude-md](https://github.com/josix/awesome-claude-md) | 🔍 Discovered | - | CLAUDE.md examples | HIGH |
| [ccplugins/awesome-claude-code-plugins](https://github.com/ccplugins/awesome-claude-code-plugins) | 🔍 Discovered | - | Plugins, hooks | MEDIUM |
| [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | 🔍 Discovered | - | Skills resources | MEDIUM |

**Index-lane note (2026-07-16)**: `hesreallyhim/awesome-claude-code` is the canonical community index lane — active, pushed 2026-07-16 (GitHub API). Its sibling `hesreallyhim/a-list-of-claude-code-agents` is stale (last push 2025-11-10) and superseded for the agents slice by wshobson/agents and VoltAgent/awesome-claude-code-subagents — do not route agent discovery there.

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
| [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | ✅ Verified | 400+ components, CLI tool (star count point-in-time — dropped 2026-07-10, see link) |
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

### Negative Dossiers — Frozen / Stale / Abandoned (verified 2026-07-16, GitHub API)

Recorded so each future sweep doesn't re-litigate them. These repos remain citable for what they were, but none is a live canon and none absorbs any of this repo's docs.

- **humanlayer/12-factor-agents** — FROZEN: no push since 2025-09-21 (24,345 stars as verified 2026-07-16, GitHub API). An authoritative reference for its era's agent-design principles, not a live canon — do not follow.
- **humanlayer/advanced-context-engineering-for-coding-agents (ACE)** — stale since 2025-12-03.
- **disler/claude-code-hooks-mastery** — stale since 2026-03-04; do not cite for current hook behavior (row also annotated in the IndyDevDan Open Source Artifacts table above).
- **efij/awesome-claude-code-security** — created and abandoned the same day, 2026-03-12 (29 stars); NOT a security absorber — `safety-and-sandboxing.md` and `secure-code-generation.md` still have no community hub to defer to.

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
  - **Dual Evidence Tier System**: Tier 1-5 (research evidence) + Tier A-D (source quality). The 1-5 research-evidence axis is **RETIRED** (owner ruling 2026-07-12 — it was never ratified, and A-D remains the only tier system in use); the line stays as a record of what second-brain originally contributed
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

## Internal Methodology

These analysis documents define the evidence and scoring frameworks used throughout this repository. They are self-referential methodology — their sources are documented in each file's header.

### Behavioral Insights

- **Document**: [behavioral-insights.md](analysis/behavioral-insights.md)
- **Role**: Quantified behavioral observations about Claude Code (context thresholds, adherence rates, performance characteristics)
- **Classification**: Mixed A-B — synthesizes Boris Cherny data, Anthropic engineering blog, and RLM research (Zhang et al.)

### Confidence Scoring

- **Document**: [evidence-tiers.md](analysis/evidence-tiers.md) (confidence framework merged in 2026-07-16; pre-merge snapshot at archive/confidence-scoring.md)
- **Role**: HIGH/MEDIUM/LOW confidence assessment methodology for research hypotheses and technical claims
- **Classification**: Tier B — validated in production cybersecurity research projects

### Evidence Tiers

- **Document**: [evidence-tiers.md](analysis/evidence-tiers.md)
- **Role**: A-D source-quality classification used by all analysis documents. The companion 1-5 claim-strength axis is **RETIRED** (owner ruling 2026-07-12 — the 1-5 axis was never ratified; A-D remains the only tier system)
- **Classification**: Tier B — adapted from established research methodology, validated in this repository

### Session Quality Diagnostics

- **Document**: [session-quality-tools.md](archive/session-quality-tools.md) — **RETIRED 2026-07-10**, archived; superseded by native `claude doctor` (v2.1.205)
- **Role**: Evidence assessment of session quality diagnostic tools (claude-doctor), signal reliability analysis, harness maturity correlation
- **Classification**: Mixed B-C — AFINN-165 lexicon (Tier B, peer-reviewed), tool methodology and thresholds (Tier C, unvalidated)

---

## Memory & Knowledge System Sources (Mixed Tiers)

### Andrej Karpathy — LLM Wiki Paradigm

- **Source**: [karpathy gist 442a6bf555914893e9891c11519de94f](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) (April 2026)
- **Role**: Originated the convention for write-time wiki maintained by an LLM (sources/ + wiki/ + index.md + log.md + CLAUDE.md schema). Three workflows: ingest, query, lint. Core insight: bookkeeping (not reading) is the bottleneck in knowledge bases — "LLMs don't get bored."
- **Pattern References**: [memory-systems-archetype-recommendations.md](analysis/memory-systems-archetype-recommendations.md), [memory-systems-recommendation-methodology.md](analysis/memory-systems-recommendation-methodology.md)
- **Followed canon (`follows:` lane) as of 2026-07-16**: [memory-systems-archetype-a-curated-kb.md](analysis/memory-systems-archetype-a-curated-kb.md) follows the LLM-wiki paradigm as its canon. Retained delta: the implementation evidence (graphify + footer discipline, typed-registry remediation). Advance trigger: the paradigm productized by a Supported tool covering the curated-KB archetype.
- **Evidence Tier**: **B by author authority** (Karpathy is treated as a thought leader on par with Boris Cherny on Claude Code). Recency does not auto-downgrade an author-authority source. Tool-specific implementations of the paradigm (graphify, Pratiyush, MehmetGoekce, Lum1104) remain Tier C until independently reproduced.

### Memory & Knowledge Tools (Tier C — implementations of the Karpathy paradigm and adjacent ideas)

| Tool | Repo | License (verified 2026-04-28) | Position |
|---|---|---|---|
| graphify | [safishamsi/graphify](https://github.com/safishamsi/graphify) | MIT | AST + Leiden topology builder. PyPI: `graphifyy`. **No LLM SDK deps** — Pass 2 LLM work via invoking Claude Code session. |
| Pratiyush/llm-wiki | [Pratiyush/llm-wiki](https://github.com/Pratiyush/llm-wiki) | MIT | Session-history mining → wiki. Adapters for Claude Code, Codex, Cursor, Gemini, Obsidian, Copilot. |
| MehmetGoekce/llm-wiki | [MehmetGoekce/llm-wiki](https://github.com/MehmetGoekce/llm-wiki) | MIT | Karpathy wiki with L1/L2 cache hierarchy for context budget. |
| Lum1104/Understand-Anything | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | MIT | Wiki-aware graph plugin; uses existing `[[wikilinks]]` as ground truth. |
| zilliztech/claude-context | [zilliztech/claude-context](https://github.com/zilliztech/claude-context) | MIT | Semantic code search MCP (BM25 + vectors over Milvus). |
| OpenBrain | [justSteve/OpenBrain](https://github.com/justSteve/OpenBrain) | FSL-1.1-MIT | Self-hosted shared memory (Postgres + pgvector + AI gateway). Compilation agent on roadmap (Tier D). |
| Rowboat | [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) | Apache 2.0 | Desktop AI coworker; markdown knowledge graph from Google services (Gmail/Calendar/Drive). YC S24, ~13.1k stars. |
| Tolaria | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | AGPL-3.0 (verified 2026-04-30) | Files-first markdown KB desktop app (Tauri/React, mac/win/linux). AGENTS-file convention for Claude Code / Codex / Gemini. ~8.5k stars; public launch 2026-04-23. |
| SiYuan | [siyuan-note/siyuan](https://github.com/siyuan-note/siyuan) | AGPL-3.0 (verified 2026-04-30) | Block-level markdown KM with WYSIWYG editor and HTTP API. Self-hosted; community MCP servers (e.g. xgq18237 MIT). ~43k stars; mature since 2020. |
| claude-video | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | (skill repo; deps under their licenses) | **Ingestion adapter**, not memory architecture. yt-dlp + ffmpeg + Whisper + Claude vision pipeline. Egresses audio to Groq/OpenAI; frames + transcript to Claude. PII-unsafe by default. |

### Luca Rossi — Refactoring + Tolaria

- **Source**: [Refactoring newsletter](https://refactoring.fm/) (~50k+ subscribers since 2019); [Introducing Tolaria](https://refactoring.fm/p/introducing-tolaria) (2026-04-23 launch post).
- **Role**: Author of Tolaria (refactoringhq/tolaria). Documents using a 10k+ note workspace as the design driver. Software-architecture publishing track record argues toward Tier B for the methodology — but Tolaria itself is days old at time of inventory, so tool-specific claims stay C until independently reproduced.
- **Pattern References**: [`memory-systems-tools-inventory.md`](research/memory-systems-tools-inventory.md) entry #10; [`memory-systems-archetype-recommendations.md`](analysis/memory-systems-archetype-recommendations.md) §C2 hybrid (archetype-C section; folded 2026-07-10).
- **Evidence Tier**: B by author authority for the editor-as-knowledge-base paradigm; C for any specific Tolaria capability claim until reproduced.

### Genealogy Trio — Project Artifact Source for Memory-System Baseline

- **Source**: `/home/jerem/genealogy/.claude/CLAUDE.md`, `/home/jerem/genealogy-kindred/.claude/CLAUDE.md`, `/home/jerem/genealogy-dry-cross/.claude/CLAUDE.md`, plus auto-memory `MEMORY.md` files (read 2026-04-29 / 2026-04-30); cross-project methodology at `/home/jerem/ai-genealogy/`.
- **Role**: Empirical 3-corpus testbed for memory-system architecture. Used in [`memory-systems-genealogy-baseline.md`](archive/memory-systems-genealogy-baseline.md) to measure unaugmented-stack performance (8/9 DEFINITIVE on a 9-query baseline). Sizes: ~17,000 / 396 / 3,290 md files. Originally framed as PII-constrained (canonical example for C-PII / C-EC archetype) but owner reframed 2026-04-29 to authorize vendor-LLM egress with placeholder discipline + public-source content; genealogy moved to opt-out example in the egress-constrained archetype, not canonical case.
- **Evidence Tier**: B (project artifact; directly observable; falsifiable via re-read; 9-query measurement is project-artifact based but small-N).

### Dmitry Paranyushkin / InfraNodus — Text Network Analysis

- **Source**: [infranodus.com](https://infranodus.com); [github.com/infranodus](https://github.com/infranodus) (clients only — core is proprietary SaaS)
- **Role**: Established methodology for text network analysis (words as nodes, co-occurrences as edges; graph-theory algorithms for topic clusters and structural gaps). 10+ years of published research from Nodus Labs.
- **Pattern References**: [memory-systems-archetype-recommendations.md](analysis/memory-systems-archetype-recommendations.md) — discussed as paradigm alternative to graphify but doesn't fit local-first + markdown-substrate constraints. The official MIT MCP server ([mcp-server-infranodus](https://github.com/infranodus/mcp-server-infranodus)) makes an InfraNodus account queryable from Claude Code.
- **Evidence Tier**: **B by author authority** for the methodology; C for product-specific quantitative claims; subscription required for the core platform (€12–66/mo).

### Avi Chawla — Daily Dose of Data Science

- **Source**: ["The Next Step After Karpathy's Wiki"](https://blog.dailydoseofds.com/p/the-next-step-after-karpathys-wiki) (April 2026)
- **Role**: Surfaced Rowboat as a temporal-knowledge complement to Karpathy's wiki. The post's description of Rowboat's ingestion (Granola/Fireflies) does *not* match the actual repo's README (Google services + optional Composio MCP); the README is authoritative.
- **Evidence Tier**: C (community blog; corrected by direct README check).

### Agent-Memory Research & Platforms (verified 2026-06-21)

New cluster registered this pass — the memory-systems leaders behind MemGPT/Letta and mem0, plus Anthropic's first-party memory primitives and LangMem's typed-memory taxonomy. New leaders: **Charles Packer** (MemGPT lead author → Letta CEO) and **Taranjeet Singh** (mem0 co-founder).

- **MemGPT (arXiv:2310.08560)** — Packer, Wooders, Lin, Fang, Patil, Stoica, Gonzalez (UC Berkeley), 2023-10-12 (v2 2024-02-12). Tier A. Verified: "virtual context management … drawing inspiration from hierarchical memory systems in traditional operating systems … data movement between fast and slow memory" (the main-context/external-context RAM-disk analog). Evaluated on both failure modes (large docs exceeding the window; conversational agents that remember/reflect across long-term interactions); uses interrupts for control flow. Revalidate by 2026-09-21.
- **Letta (github.com/letta-ai/letta)** — Packer & Wooders (Letta, Inc.), latest release **v0.16.8 (2026-05-14)**, ~23.4k stars. Tier B. "Platform for stateful agents: AI with advanced memory that can learn and self-improve over time" (renamed from MemGPT). NOTE: the Core/Recall/Archival three-tier naming is Letta's *docs* architecture, NOT on the GitHub README.
  - **Letta blog — Context Repositories (git-based memory)** (`letta.com/blog/context-repositories/`, 2026-02-12, Tier B): "Context Repositories are git-backed, so every change to memory is automatically versioned with informative commit messages"; isolated worktree per subagent for concurrent memory writes merged via git conflict resolution; three skills — Initialization, Reflection, Defragmentation ("reorganizing into a clean hierarchy of 15-25 focused files").
  - **Letta blog — Rearchitecting the agent loop** (`letta.com/blog/letta-v1-agent`, 2025-10-14, Tier B): "stay in-distribution relative to the data the LLM was trained on"; "heartbeats and the send_message tool are deprecated."
- **mem0 (github.com/mem0ai/mem0)** — Singh & Yadav, latest release "Mem0 OpenCode Plugin (v0.2.0)" **2026-06-17**, 59k stars. Tier B. "Multi-Level Memory: … User, Session, and Agent state with adaptive personalization." Single-pass extraction "cuts write-time LLM calls by 60 to 70 percent" (confirmed on the token-playbook page).
  - **mem0 blog — Token Optimization Playbook** (`mem0.ai/blog/the-2026-token-optimization-playbook…`, 2026-05-06, Tier C): verified per-example token counts — 24-entry example 594 tokens naive vs 166 retrieval = **72%**; 200-entry example **~4,600** naive vs ~130 retrieval (≈35×). The "3-4× average" headline is vendor-conservative and not independently benchmarked. ⚠️ Prior draft's "3,200 vs 130 / ~24× reduction" was WRONG — see Unverified section.
  - **mem0 blog — State of AI Agent Memory 2026** (`mem0.ai/blog/state-of-ai-agent-memory-2026`, **2026-04-01** — date corrected from a "2026-06-20" last-modified stamp; Tier C): benchmarks LoCoMo (1,540 Q / 4 categories), LongMemEval (500 Q / 6 categories), BEAM (1M + 10M token scales); six production requirements; **five-to-six** unsolved gaps (prior "four" understated). Vendor-authored; retrieval-quality deltas and LoCoMo/LongMemEval score figures remain vendor-claimed-unverified.
- **Anthropic Memory Tool (`memory_20250818`)** — `platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool` (date unknown; tool ID implies Aug 2025). Tier A. Client-side filesystem tool, developer-controlled backend; six commands (view/create/str_replace/insert/delete/rename) on `/memories`. Auto-injected system prompt (verbatim): "IMPORTANT: ALWAYS VIEW YOUR MEMORY DIRECTORY BEFORE DOING ANYTHING ELSE" and "ASSUME INTERRUPTION: Your context window might be reset at any moment." Multi-session dev pattern (initializer bootstraps progress log + feature checklist; later sessions read to recover state) + pairing with compaction.
- **Anthropic Cookbook — Context Engineering (memory/compaction/tool-clearing)** — `platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools`, Isabella He (Anthropic), 2026-03-20. Tier A. Three primitives — compaction (server-side whole-transcript summarization), tool-result clearing (client-side placeholder replacement preserving `tool_use` records), memory (`memory_20250818`). Path-traversal protection via `pathlib` `Path.resolve()` + a `startswith` boundary check against `/memories`.
- **LangMem SDK** — `langchain-ai.github.io/langmem/concepts/conceptual_guide/` (date unknown). Tier B. Three typed memory categories — semantic (collections vs profiles), episodic ("preserves successful interactions as learning examples"), procedural ("encodes how an agent should behave"). Verbatim: "The best memory systems are often application-specific." `create_manage_memory_tool` confirmed; `create_search_memory_tool` NOT found on this page (see Unverified).

### Evals & Benchmarking Sources (verified 2026-06-21)

New cluster — practitioner eval methodology (Hamel Husain, Shreya Shankar), harness-effect benchmarks, and the academic LLM-as-judge literature. New leaders: **Hamel Husain**, **Shreya Shankar**, **Philipp Schmid**, **Harrison Chase**, plus three harness papers (Lin et al. Fudan; Zhou/Zhang et al. SJTU; Yao/Tan et al.).

- **Hamel Husain & Shreya Shankar — "LLM Evals: Everything You Need to Know"** (`hamel.dev/blog/posts/evals-faq/`, 2026-01-15, Tier B). Error analysis before infrastructure (review ~20-50 LLM outputs per significant change, ~100+ traces for saturation); "Binary evaluations force clearer thinking and more consistent labeling"; custom annotation tool is "the single most impactful investment" ("teams with custom annotation tools iterate ~10× faster"); "60-80% of … development time on error analysis and evaluation." Appoint a single domain-expert "benevolent dictator"; Transition Failure Matrices.
- **Hamel Husain — "Evals Skills for Coding Agents"** (`hamel.dev/blog/posts/evals-skills/` and `hamelhusain.substack.com/p/evals-skills-for-coding-agents`, 2026-03-02/03, Tier B). Distilled from "50+ companies and 4,000+ students"; "Improving the infrastructure around the agent yielded better returns than improving the model." **Six-skill toolkit**: error-analysis, generate-synthetic-data, write-judge-prompt, validate-evaluator (calibrate judges vs human labels via TPR/TNR + bias correction), evaluate-rag, build-review-interface. Distinguishes action hallucination from factual hallucination.
- **Shreya Shankar — agentic data systems / eval methodology** (`sh-reya.com/papers/`, 2026, Tier A for the papers list). CHI 2026 Best Paper "RAG Without the Lag"; CIDR 2026 "Supporting Our AI Overlords: Redesigning Data Systems to be Agent-First"; VLDB 2026 "Multi-Objective Agentic Rewrites…"; SIGMOD 2026 "Cut Costs, Not Accuracy…". Co-authored the O'Reilly book "Evals for AI Engineers" with Husain (off-page). ⚠️ "CMU assistant professor from 2027" is confirmed only to faculty-candidate status (March 2026) — treat the start year as inference.
- **Followed canon (`follows:` lane) as of 2026-07-16**: [agent-evaluation.md](analysis/agent-evaluation.md) follows the Husain/Shankar evals canon (plus the first-party Anthropic eval posts). Retained delta: per-version eval baselines, the subagent-dispatch regression eval, and the application table. Advance trigger: a Supported eval harness shipping per-repo agent-eval baselines for Claude Code.
- **Philipp Schmid (Google DeepMind) — "Agent Harness 2026"** (`philschmid.de/agent-harness-2026`, 2026-01-05, Tier B). "It comes down to durability: How well a model follows instructions while executing hundreds of tool calls over time" — durability over single-turn scores. "Manus refactored their harness five times in six months"; LangChain "re-architected … three times"; "Vercel removed 80% [of] their agents tool[s]." ⚠️ The companion posts (Inner/Outer Loop, AGENTS.md guide, etc.) were NOT individually fetched — their dates are author-asserted.
- **Harrison Chase (LangChain) — "Your harness, your memory"** (`langchain.com/blog/your-harness-your-memory`, 2026-04-11, Tier B). "Managing context, and therefore memory, is a core capability and responsibility of the agent harness." Closed/stateful harnesses (OpenAI Responses API, Anthropic server-side compaction) store state on vendor servers and prevent model switching/thread resumption; advocates open harnesses with user-controlled DBs. "When Claude Code's source code was leaked, there was 512k lines of code. That code is the harness."
- **Simon Willison — Agentic Engineering Patterns guide** (`simonwillison.net/guides/agentic-engineering-patterns/` + `simonw.substack.com/p/agentic-engineering-patterns`; first two chapters published 2026-02-23, growing at roughly 1-2 chapters/week since — 12+ chapters as of the latest count verified 2026-07-10; **upgraded C → Tier B this pass** as the guide consolidated from a launch post into a durable, actively-maintained reference). Six categories (Principles, Working with coding agents, Testing/QA, Understanding code, Annotated prompts, Appendix); chapters confirmed include "Writing code is cheap now," "Red/green TDD," "Linear walkthroughs," "Hoard things you know how to do," and "What is agentic engineering?" (chapter 12 by publication order, positioned first in the reading order to answer the fundamental question). **Position**: favors deterministic constraints (tests, linting, type checks, red/green TDD) over behavioral instructions/prose rules as the reliable way to shape agent output — consistent with this repo's own hooks-over-CLAUDE.md-prose findings, and extends the existing Willison entries in this file (the separate Opus 4.7 system-prompt analysis, below in the Opus 4.7 Migration Guidance section) rather than replacing them. Authorship discipline: "I have a strong personal policy of not publishing AI-generated writing under my own name." ⚠️ The exact definition string "An agent is an LLM that runs tools in a loop … The harness is what controls the loop" was NOT located verbatim — treat as unverified.
  - **Followed canon (`follows:` lane) as of 2026-07-16**: [harness-engineering.md](analysis/harness-engineering.md) follows the Willison/Ronacher/Osmani canon set (see the Armin Ronacher entry under Loop Engineering). Retained delta: the Bitter-Lesson diagnostic, the accretion heuristics, and the portfolio measurements. Advance trigger: a Supported harness-design guide absorbing the diagnostic function.
  - **Revalidate by**: 2026-10-10
- **Diagnosing LLM-as-a-Judge via IRT (arXiv:2602.00521)** — Choi, Park, Cho, Park, Kim, 2026-01-31 (v2 2026-05-29), ICML 2026. Tier A. Applies IRT with the Graded Response Model; two reliability dimensions — "(1) intrinsic consistency … under prompt variations, and (2) human alignment." ⚠️ The "no universally robust configuration" claim is NOT in the abstract — softened.
- **Terminal-Bench 2.0 (arXiv:2601.11868)** — Merrill et al. (85 authors), 2026-01-17. Tier A. "89 tasks in computer terminal environments," each with a unique environment, human-written solution, and comprehensive tests; frontier models/agents score **<65%**. ⚠️ The "81-82% with scaffolding / Docker / Harbor framework" details are NOT in the abstract.
- **Agent-as-a-Judge (arXiv:2601.05111)** — You, Cai, Zhang, Xu, Liu, Yu, Li, Li et al., 2026-01-08. Tier A. Three LLM-judge limitations: "inherent biases, shallow single-pass reasoning, and the inability to verify assessments against real-world observations." ⚠️ Title is "Agent-as-a-Judge" (not "A Survey on…"); the procedural/reactive/self-evolving taxonomy is not in the abstract.
- **METR — Measuring AI Ability to Complete Long Software Tasks (arXiv:2503.14499)** — Kwa et al. (25 authors, METR), v1 2025-03-18 (v3 2026-02-25), NeurIPS 2025. Tier A. The "50%-task-completion time horizon" metric; frontier models (Claude 3.7 Sonnet) ~50-minute horizon, doubling ~every 7 months since 2019; HCAST + RE-Bench + 66 new tasks.
- **Efficient Benchmarking of AI Agents (arXiv:2603.23749)** — Franck Ndzomga, 2026-03-24. Tier B. Mid-difficulty filter (30-70% historical pass rates, IRT-inspired) cuts eval tasks 44-70% while keeping rank fidelity across 8 benchmarks / 33 scaffolds / 70+ configs; rank-order stable under distribution shift.
- **OpenAI Evaluation Best Practices** (`developers.openai.com/api/docs/guides/evaluation-best-practices`, date unknown). Tier A. Eval-driven development ("Write scoped tests at every stage"; "Log as you develop so you can mine your logs for good eval cases"); validate automated scoring vs human judgment. ⚠️ Deprecation confirmed verbatim: Evals goes read-only for existing users **Oct 31, 2026**, platform shuts down **Nov 30, 2026**.
- **Harness-effect academic cluster** (all Tier A, arXiv abstracts verified 2026-06-21):
  - **Agentic Harness Engineering: Observability-Driven Automatic Evolution (arXiv:2604.25850)** — Lin, Liu, Pan, Lin, Dou, Xi, Huang, Yan, Han, Gui, Jiang (Fudan), 2026-04-28 (v4 2026-05-18). Three observability pillars (component/experience/decision); Terminal-Bench 2 pass@1 lifted **69.7% → 77.0%**, surpassing human-designed Codex-CLI (71.9%); SWE-bench-verified strong with 12% fewer tokens; "factual harness structure transfers while prose-level strategy does not."
  - **Externalization in LLM Agents: A Unified Review (arXiv:2604.08224)** — Zhou, Zhang, … (21 authors, SJTU et al.), 2026-04-09, 54pp, CC BY 4.0. "agents are increasingly built less by changing model weights than by reorganizing the runtime around them … a historical progression from weights to context to harness." Four-component taxonomy: Memory, Skills, Protocols, Harness engineering.
  - **Harness-Bench: Measuring Harness Effects across Models (arXiv:2605.27922)** — Yao, Tan, Liu, Li, Wang, Yu, Tan, Tian, Zhao, Sun, Zhang, Yang, 2026-05-27. "agent capability should be reported at the model-harness configuration level rather than attributed to the base model alone"; 5,194 trajectories across 106 sandboxed tasks; identifies "execution-alignment failures."

---

## Loop Engineering & Unattended Execution Sources (Mixed Tiers) ⭐ KM-LEVERAGE LINEAGE

Added 2026-06-15; **re-verified and re-attributed 2026-06-21**. This is the second of the two knowledge-management leverage threads the maintainer values from recent firsthand use — the shift from *prompting* an agent to *designing the loop that prompts it*, with state externalized to files + git. Significant value seen firsthand recently; the practice anchors are Tier A/B (Cherny on a dated stage, the Anthropic harness docs, the Karpathy self-improvement loop), but the "loop engineering" *label* layer is mostly Tier C and adoption is weeks old, so treat the framing as promising-not-yet-corroborated. Supports [`scheduled-and-looping-primitives.md`](analysis/scheduled-and-looping-primitives.md), [`harness-engineering.md`](analysis/harness-engineering.md), and [`safety-and-sandboxing.md`](analysis/safety-and-sandboxing.md).

**⚠️ Attribution correction (2026-06-21)** — supersedes the prior "Osmani coined it" line: Osmani's own 2026-06-07 post does **NOT** claim to coin "loop engineering"; it explicitly **attributes the concept to Peter Steinberger and Boris Cherny**. The New Stack reportedly credits Osmani, but The New Stack article body could not be fetched to confirm, and three earlier SOURCES lines asserting "Osmani coined the term" should be read against Osmani's own text. **Do not state Osmani coined the term** without a primary that shows him doing so. Distinct roles: Cherny *described the practice on stage*; Steinberger *issued the call-to-discipline on X*; Osmani *named the five-component anatomy*. New leader registered this pass: **Peter Steinberger** (see below).

**⚠️ Re-attribution (2026-07-12, owner-ratified)**, tempering the 2026-06-21 correction above: on re-read, Osmani presents loop-engineering as his own framing and quotes Steinberger for one line, so "attributes the concept to Steinberger and Cherny" was itself an over-credit; read it as one quoted line plus a nod to Cherny's stage remark rather than a concept handoff. Steinberger's contribution is a single soft X post (primary still unfetched). The truthful crediting frame for any instrument built on this lineage, this repo's audit machinery included, is "inspired by Steinberger's diagnosis; the instrument is its builder's own."

### Anthropic — Claude Code scheduling & workflow docs

- **Source**: ["Run prompts on a schedule"](https://code.claude.com/docs/en/scheduled-tasks) and ["Orchestrate subagents at scale with dynamic workflows"](https://code.claude.com/docs/en/workflows) (Claude Code docs); [changelog](https://code.claude.com/docs/en/changelog).
- **Role**: Canonical spec for `/loop` (interval/self-paced, `.claude/loop.md`, 7-day expiry, `CLAUDE_CODE_DISABLE_CRON`, v2.1.72+), the three-way Cloud/Desktop/loop comparison, Desktop scheduled tasks, `/goal` (v2.1.139, 2026-05-11), dynamic workflows (`.claude/workflows/`, `disableWorkflows`, v2.1.154), and subagents spawning subagents 5 levels deep (v2.1.172, 2026-06-10).
- **Pattern References**: [scheduled-and-looping-primitives.md](analysis/scheduled-and-looping-primitives.md), [orchestration-comparison.md](analysis/orchestration-comparison.md).
- **Evidence Tier**: A (first-party product documentation, authoritative for product behavior). Version numbers are fast-moving — re-verify before quoting.

### Anthropic Engineering — Long-running agent harness & managed agents

- **Source**: Prithvi Rajasekaran, ["Designing a harness for long-running application development"](https://www.anthropic.com/engineering/harness-design-long-running-apps) (2026-03-24); Lance Martin, Gabe Cemaj, Michael Cohen, ["Scaling Managed Agents: Decoupling the brain from the hands"](https://www.anthropic.com/engineering/managed-agents) (2026-04-08); ["Effective context engineering for AI agents"](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (2025-09-29).
- **Role**: Rajasekaran is the primary generator/evaluator harness source (planner/generator/evaluator, Playwright-driven evaluator, 5–15 iterations, ~$200/6hr vs ~$9/20min, self-praise-bias caution). Scaling Managed Agents gives the durable-Session / stateless-Harness / isolated-Sandbox architecture and vault-isolated credentials. Effective context engineering is Anthropic's published prompt→context progression — and notably does *not* use the term "loop engineering."
- **Pattern References**: [harness-engineering.md](analysis/harness-engineering.md), [safety-and-sandboxing.md](analysis/safety-and-sandboxing.md), [scheduled-and-looping-primitives.md](analysis/scheduled-and-looping-primitives.md).
- **Evidence Tier**: A (Anthropic engineering blog — first-party, per this repo's tier convention).

### Anthropic — 2026 Agentic Coding Trends Report

- **Source**: ["2026 Agentic Coding Trends Report"](https://resources.anthropic.com/2026-agentic-coding-trends-report) (~2026-01-20).
- **Role**: Vendor framing for long-running agents (Trend 3, "Long-running agents build complete systems"). Carries the intellectual-honesty counterweight to loop hype: developers use AI in ~60% of work but *fully delegate* only 0–20% of tasks. Published just before the Mar–Jun window; the delegation figure may have moved.
- **Pattern References**: [scheduled-and-looping-primitives.md](analysis/scheduled-and-looping-primitives.md).
- **Evidence Tier**: A (vendor primary), with a recency caveat on the delegation stat.

### Boris Cherny — "I write loops" (WorkOS Acquired Unplugged) ⭐

- **Primary**: WorkOS-hosted *Acquired Unplugged* event, 2026-06-02 — YouTube `watch?v=RkQQ7WEor7w` + the WorkOS Acquired-takeaways blog (2026-06-02). The New Stack's `thenewstack.io/loop-engineering/` rendered as a newsletter/listing wrapper on direct fetch (article exists, body not extracted), so the **primary_url is repointed to the YouTube/WorkOS blog**, not The New Stack.
- **Role**: Primary anchor for the loop-engineering wave. Verified via the WorkOS blog + a note.com near-verbatim share (2026-06-09): "I don't prompt Claude anymore. I have loops that are running. They're the ones that are prompting Claude and figuring out what to do. My job is to write loops." Context corroborated: deleted his IDE ~Nov 2025; 100% of his prior-30-day Claude Code contributions (259 PRs) written by Claude Code as of late Dec 2025.
- **⚠️ SECONDARY-ONLY (not in the verified WorkOS blog or extractable from the video, 2026-06-21)**: the explicit three-stage Stage-1/2/3 taxonomy (autocomplete → 5-10 parallel manual sessions → autonomous loops reading GitHub/Slack/Twitter), the "/loop babysit all my PRs" starter example, the cron scheduling layer, and the gate conditions (max-iteration count, no-progress detection, token/dollar budget ceiling) appear only in secondary Medium write-ups. Treat the stage taxonomy and the gate-condition list as secondary synthesis, not Cherny's primary words.
- **Pattern References**: [harness-engineering.md](analysis/harness-engineering.md), [scheduled-and-looping-primitives.md](analysis/scheduled-and-looping-primitives.md).
- **Evidence Tier**: B for the quote via the WorkOS blog primary (the named Claude Code creator on a dated stage; the YouTube body could not be content-extracted this pass, so not asserting A). The "loop engineering" *label* is press-coined (Tier C) — do not attribute the term to Cherny.
- **Revalidate by**: 2026-09-21

### Andrej Karpathy — Sequoia Ascent 2026 (self-improvement loop)

- **Source**: ["Sequoia Ascent 2026"](https://karpathy.bearblog.dev/sequoia-ascent-2026/) (2026-04-30, re-verified 2026-06-21); AutoResearch repo (github.com/karpathy/autoresearch).
- **Role**: The loop-engineering steelman. Verified verbatim on the bearblog post: "Coding gives the model feedback: tests pass or fail, programs run or crash, diffs can be inspected, benchmarks can be measured"; vibe coding "raises the floor … almost anyone create software by describing what they want," agentic engineering "raises the ceiling … coordinating fallible agents while preserving correctness, security, taste, and maintainability"; the MenuGen example (the agent matched Stripe purchases to Google accounts by email — "plausible code, but bad system design … A human needs enough product and engineering judgment to insist on persistent user IDs").
- **⚠️ Corrections (2026-06-21)**: **AutoResearch is NOT mentioned anywhere in the bearblog Sequoia post** — verified separately. The repo exists (MIT; agent edits `train.py` only; 5-minute fixed-time-budget training jobs; `val_bpb` metric, lower-is-better; keep-if-improved/revert-otherwise; ~100 experiments/night). The `val_bpb`-is-the-gate workflow is sound, but the "66,000+ stars by early April 2026" and "~12 experiments/hour" figures are point-in-time/secondary (repo now ~87.9k stars; per-hour rate not stated on either primary) — downgraded to Tier C.
- **Pattern References**: [harness-engineering.md](analysis/harness-engineering.md), [scheduled-and-looping-primitives.md](analysis/scheduled-and-looping-primitives.md).
- **Evidence Tier**: B by author authority for the bearblog content; demo quant figures Tier C (his report, not independently reproduced; star/rate counts unconfirmed).
- **Revalidate by**: 2026-09-21

### Geoffrey Huntley — Ralph Wiggum loop (+ official Anthropic plugin)

- **Source**: ["Ralph Wiggum as a software engineer"](https://ghuntley.com/ralph/) (**2025-07-14**, page shows 14 July 2025 — date corrected from "2025-07-01"; re-verified 2026-06-21); official Anthropic `ralph-wiggum` plugin in `anthropics/claude-code/plugins/`.
- **Role**: Origin of the fixed-prompt `while`-loop technique the productized commands descend from. **Confirmed on ghuntley.com/ralph/**: `while :; do cat PROMPT.md | claude-code ; done`; per-loop gate conditions (run unit tests after each fix; type-checking via Dialyzer/Pyrefly for dynamically-typed projects; build validation; "only 1 subagent for build/tests of rust"; git-tag patch-increment after a passing test run); deterministic per-loop context (`@fix_plan.md`, `@specs`, `@AGENT.md` self-tuning).
- **⚠️ Sourcing correction (2026-06-21)**: the **official-plugin lineage is NOT on ghuntley.com/ralph/** (the 2025 post predates that productization). It is confirmed instead on the official `anthropics/claude-code/plugins/ralph-wiggum` README: a `Stop` hook intercepts session exit and re-feeds the SAME prompt INSIDE the current session, so **state persists ACROSS iterations within one session** (not fresh-context-per-iteration) via files + git history. Completion = `--completion-promise` exact-string match + `--max-iterations` ("Always rely on `--max-iterations` as your primary safety mechanism"); commands `/ralph-loop` and `/cancel-ralph`. The native `/loop` `/goal` `/batch` commands are also NOT in the 2025 post — sourced from the Anthropic docs, not Huntley.
- **Pattern References**: [scheduled-and-looping-primitives.md](analysis/scheduled-and-looping-primitives.md).
- **Evidence Tier**: B by author authority (Huntley) for the technique; A for the official Anthropic plugin packaging (verified via the plugin README, not ghuntley.com).
- **Revalidate by**: 2026-10-21

### Armin Ronacher — inner-loop vs outer-loop essays (lucumr.pocoo.org)
- **Author**: Armin Ronacher (Flask creator; lucumr.pocoo.org)
- **Added**: 2026-07-16 (absorption-wave sweep)
- **Key posts**: "The Coming Loop" (2026-06-23 — the inner agent loop vs the outer harness loop, and what each can and cannot be trusted with); "Agent Design Is Still Hard" (2025-11); "A Language for Agents" (2026-02-09)
- **Role**: The most critical practitioner voice on autonomous-loop limits — where Cherny, Osmani, and the June-2026 wave argue for loops, Ronacher documents where they break, which is why he anchors two follow lanes rather than the hype layer.
- **Followed canon (`follows:` lane) as of 2026-07-16**: [scheduled-and-looping-primitives.md](analysis/scheduled-and-looping-primitives.md) (with Osmani + Ng) and [harness-engineering.md](analysis/harness-engineering.md) (with Willison + Osmani) both follow Ronacher as part of their canon sets; the docs keep their deltas (audit-signal routing + failure framing; Bitter-Lesson diagnostic + portfolio measurements) and stop growing.
- **Evidence Tier**: B (named practitioner with a long public track record; blog-form, no release discipline)
- **Pattern References**: [scheduled-and-looping-primitives.md](analysis/scheduled-and-looping-primitives.md), [harness-engineering.md](analysis/harness-engineering.md)

### Addy Osmani — "Loop Engineering" (the five-component anatomy)

- **Source**: ["Loop Engineering"](https://addyosmani.com/blog/loop-engineering/) (2026-06-07, verified 2026-06-21; Substack mirror `addyo.substack.com/p/loop-engineering`).
- **Role**: Names and structures the pattern. Verified on the primary page: opening definition "Loop engineering is replacing yourself as the person who prompts the agent. You design the system that does it instead." **Five building blocks** (verbatim): (1) Automations / scheduled discovery+triage, (2) Worktrees for parallel isolation, (3) Skills as reusable SKILL.md project knowledge, (4) Plugins/Connectors via MCP, (5) Sub-agents splitting ideation from verification — plus external memory ("the model forgets everything between runs so the memory has to be on disk and not in the context"). Gate conditions confirmed: sub-agent verification "splits the maker away from the checker"; `/goal` "keeps going until a condition you wrote is actually true"; CI/CD via connectors; human code-review responsibility ("your job is to ship code you confirmed works"). Warns about **"comprehension debt"** — "The faster the loop ships code you did not write, the bigger the gap between what exists and what you actually get." Closing line: "Build the loop. But build it like someone who intends to stay the engineer, not just the person who presses go." Three non-delegable human roles: verification, comprehension, resisting cognitive surrender.
- **⚠️ Coinage (2026-06-21)**: Osmani's own text **attributes the concept to Steinberger and Cherny** — he does not claim to coin "loop engineering" in this post. The New-Stack-credits-Osmani claim could not be confirmed against The New Stack body. See the section-head attribution correction. **Re-read 2026-07-12**: the post quotes Steinberger for one line and presents the five-component framing as Osmani's own, so that one-line quote is the full extent of the Steinberger reliance here.
- **Followed canon (`follows:` lane) as of 2026-07-16**: [scheduled-and-looping-primitives.md](analysis/scheduled-and-looping-primitives.md) (with Ronacher + Ng) and [harness-engineering.md](analysis/harness-engineering.md) (with Willison + Ronacher) follow Osmani as part of their canon sets; retained deltas are the audit-signal routing table + failure framing and the Bitter-Lesson diagnostic + portfolio measurements respectively.
- **Evidence Tier**: C (single practitioner; the anatomy is well-structured but the "names the pattern" credit is contested).
- **Revalidate by**: 2026-09-21

### Peter Steinberger — "Stop prompting, build loops" (2026-06)

- **Source**: X post `https://x.com/steipete/status/2063697162748260627` (dated 2026-06-07 per a secondary recap).
- **Role**: One soft X post carrying the diagnosis line the June wave quoted; re-scoped 2026-07-12 (owner ruling) because the prior "call-to-discipline that named the wave" framing over-credited a single post — the truthful frame is "inspired by Steinberger's diagnosis; the instrument is its builder's own," and machinery built on the line (this repo's included) is homegrown. Verbatim wording corroborated across 4+ secondaries (Latent Space Loopcraft, linas.substack, explainx, firecrawl): "you shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents." Distinct framing from Cherny (Steinberger = call-to-discipline; Cherny = autobiographical).
- **⚠️ UNVERIFIED against primary (2026-06-21)**: x.com could not be fetched in this environment (ECONNREFUSED; x.com blocks WebFetch), so the entry is `verified=false`. Date adjusted 2026-06-08 → 2026-06-07 per a secondary recap, still unconfirmed against X. **View count is disputed** (~6.5M vs a recap's 2.2M) — do NOT assert a number. `steipete.me` does not host this post — primary repointed to the X status URL. Biographical detail (OpenClaw creator → joined OpenAI ~Feb 2026; CodeLooper macOS menubar app) is independently reported (TechCrunch/CNBC 2026-02-15) but is biography, not the X-post content; the OpenClaw "145K stars / fastest-growing OSS" stat is secondary and unconfirmed.
- **Evidence Tier**: C (practitioner X post; primary unfetched — see Unverified section).

### Andrew Ng — The Batch: three-loop model + "context advantage" (2026-06-30)
- **Author**: Andrew Ng (The Batch, DeepLearning.AI)
- **Source**: The Batch letter, 2026-06-30
- **Added**: 2026-07-16 (absorption-wave sweep)
- **Role**: Names a three-loop model of agentic development and the "context advantage" — the framing that whoever holds the richer working context wins the loop, which slots into the commentary lineage this section tracks alongside Osmani's anatomy and Ronacher's limits.
- **Followed canon (`follows:` lane) as of 2026-07-16**: [scheduled-and-looping-primitives.md](analysis/scheduled-and-looping-primitives.md) follows Ng as part of its Osmani/Ronacher/Ng canon set.
- **Evidence Tier**: C (newsletter commentary; no measured data)
- **Pattern References**: [scheduled-and-looping-primitives.md](analysis/scheduled-and-looping-primitives.md)

### Jon Wiggins — "Loop engineering isn't new. Don't reinvent the wheel." + Errorta (2026-07)

- **Source**: Medium post (Jon Wiggins, ~2026-07; supplied by the maintainer 2026-07-10) + [errorta.app](https://errorta.app/) (fetched 2026-07-10); GitHub `wiggins-j/errorta_app` + `wiggins-j/aiar` (AIAR: Apache-2.0 local-RAG framework underneath).
- **Role**: A further practitioner voice on the term after the Cherny/Steinberger/Osmani wave, framing loop engineering as "the software development lifecycle with different (artificial) staffing" — spec/plan/dev/test/review as a chain of error-correcting checkpoints. Three mechanical rules, two of which map to patterns already anchored in this section: (1) fresh context window per role ("a reviewer that never heard your justification reviews like an outsider") = the sub-agent maker/checker split; (2) **cross-model-family review** ("shared weights share failure modes… have GPT or Gemini review what Claude wrote") — the one dimension this corpus does not yet carry as a named practice, and the article's genuine delta; (3) deterministic verification + fail-closed + adversarial reviewer prompts ("a checkpoint that always says yes is worse than no checkpoint"; "never let a model grade its own homework").
- **Errorta itself**: alpha desktop app, macOS-only (Windows announced), open-source; PM-agent task decomposition, model routing to "the cheapest capable model you allow," governance gates, nothing-touches-your-tree-until-review. The author's own product, so the article is partly promotion for it — read the rules, not the pitch.
- **Evidence Tier**: C (single practitioner promoting his own alpha tool; bias flagged). The rules restate practices already Tier A/B-anchored elsewhere in this section; the cross-family-review rule is argument-from-architecture, not measured.
- **Corroboration note (2026-07-10)**: the "loops that don't bite" failure mode was found live in THIS repo the same day the article was reviewed — `scripts/check-measurement-expiry.py` had been scanning a nonexistent `patterns/` directory and exiting green having checked nothing (fixed in the Phase-0 reduction commit). The rule earns its place on first-party evidence.
- **Revalidate by**: 2026-10-10 (check Errorta alpha→beta, Windows/Linux availability, any measured results; check whether cross-family review picks up measured backing anywhere).
- **Revalidate by**: 2026-09-21

### Loop-engineering amplification cloud (Tier C — bias-flagged)

- **Sources**: The New Stack, "Loop engineering" (2026-06, body unfetchable / auth-blocked); Filip Verloy (Rubrik), ["From Prompt Engineering to Loop Engineering"](https://medium.com/@filipv_74515/from-prompt-engineering-to-loop-engineering-why-the-agent-era-demands-a-new-security-paradigm-816385040e3d) (2026-06-07, vendor-adjacent security framing); Data Science Dojo, MindStudio, Louis Bouchard (2026-06).
- **Role**: The June-2026 amplification layer keyed off the Cherny clip and the Steinberger post. Useful for the ReAct / Reflexion / Plan-and-Execute lineage and the security framing; thin on primary sourcing and production metrics. The Neuron misattributes Osmani's "building blocks" framework to Cherny — do not repeat.
- **Evidence Tier**: C (community / journalism / vendor marketing; flag bias).

### Attribution note — Bilgin Ibryam "12 Agentic Harness Patterns"

- **Source**: Bilgin Ibryam, ["12 Agentic Harness Patterns from Claude Code"](https://generativeprogrammer.com/p/12-agentic-harness-patterns-from) (2026-04-05).
- **Role**: Patterns from the Claude Code source-map leak (Explore-Plan-Act Loop, Dream Consolidation, Tiered Memory, etc.). Recorded for an attribution fix: aggregators conflate this with Nate B. Jones — it is Ibryam, already a SOURCES author via the Dapr material.
- **Evidence Tier**: C (community analysis of a leaked artifact).

---

## Evidence Tier Definitions

This repository uses a tiered evidence system:

### Tier A: Primary Sources
- Direct from Anthropic (engineering blog, documentation)
- Official specifications and standards (agentskills.io, OWASP)
- Industry-standard frameworks (e.g. GitHub Spec Kit — see entry for current star count, point-in-time figures dropped 2026-07-10)
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
2. **Documentation**: Check code.claude.com (canonical; older docs.anthropic.com paths still redirect)
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

### Refresh Log

| Date | Action | Result |
|------|--------|--------|
| 2026-07-18 | Reverification sweep + token-economics re-measure (five-agent web sweep, two-lens adversarially verified; raw record `research/probe-session-2026-07-18.md`) | **Reverifications**: both lapsed MCP-security rows — 42%-of-12,000+ re-cited to BlueRock 2026 (Tier C, new subsection "MCP Security Surveys") with Equixly 2025 as historical origin and the Jones "Docker data"/"~10 of 5,960+" provenance corrections annotated on his entry; Playwright 114K/27K attribution corrected (unsupported — Medium citation loop; Outpost/Ranger ~2x independent benchmark registered Tier B); tool-search version pegs corrected repo-wide (auto mode default-on v2.1.7, `alwaysLoad` v2.1.121 — the prior "default-on since v2.1.121" notes here were wrong); valgard entry annotated re-measured (2026-07-18 wire measurement: workspace-mcp 51 tools ~28.8k est. tokens static vs ~0.9k names-only deferred). **MRCR row resolved**: Anthropic dropped MRCR after the 4.7 card; GraphWalks 256K/1M figures from the 4.8 and Fable/Mythos cards recorded (Mythos 5 Parents 99.96→97.5, shallowest Parents drop of the six tabulated models; superlative scoped after adversarial review — Mythos Preview's BFS drop is marginally shallower). **Academic checks**: ACE entry updated (ICLR 2026 poster 2026-04-25, camera-ready retitle, 226 S2-floor citations) + MCE follow-up registered Tier B preprint-with-claimed-venue (arXiv:2601.21557 verified; ICML tag is the authors' own, proceedings entry unverified); Meta-Harness venue check added (still preprint, 99 citations, watch NeurIPS 2026). **Additions**: claude.com/blog migration post (2026-07-16, Tier A + self-reported-practices note) with the engineering-blog venue note. Bumped "Last curated" to 2026-07-18. |
| 2026-07-16 | Absorption-wave sweep (`drafts/ABSORPTION-SCAN-2026-07.md`) — third-party dossier sync | **Updates**: obra/superpowers re-verified at v6.1.1 (2026-07-02) with GitHub-API-dated stats (255,877★/22,790 forks, pushed daily, 628 commits), the 13-skill enumeration, and a substance check (no security skill, no Bitter-Lesson content, no framework comparison — compared object, not comparator; "independently implements equivalent patterns" re-verified at v6.x); affaan-m repo rename → **ECC** recorded with the worldflowai/fork naming hazard and component counts quarantine-flagged (28/119/60 are secondary-page claims); CodeGuard entry extended with the first-party marketplace plugin (`codeguard-security@project-codeguard`), the Options-B/C absorption note, and the critical-triad correction (credentials/crypto-algorithms/digital-certificates — input-validation is separate, non-critical); `/insights` changelog trace updated to v2.1.101 (2026-04). **Additions**: AGENTS.md standard (AAIF/Linux Foundation, Tier A) with the `repo-has-agents-md` routing note; ClaudeLog (Tier C + author-authority note, `follows:` anchor for behavioral-insights); Anthropic first-party distribution repos (anthropics/skills 161,668★ + claude-plugins-official 32,216★, both pushed 2026-07-16); Armin Ronacher (Tier B, loop-limits canon); Andrew Ng The Batch three-loop letter (Tier C); hesreallyhim index-lane note incl. the stale a-list-of-claude-code-agents sibling. **Negative dossiers** (do-not-follow, verified 2026-07-16): HumanLayer 12-factor-agents FROZEN since 2025-09-21 (24,345★); HumanLayer ACE stale since 2025-12-03; disler/claude-code-hooks-mastery stale since 2026-03-04; efij/awesome-claude-code-security abandoned same-day-created 2026-03-12. **Follow-lane pointers** added on the Osmani, Willison-guide, Karpathy-LLM-wiki, Husain/Shankar, and Miessler entries (Miessler = checked, `none` lane). **Quarantine lines added** (see Unverified § Added 2026-07-16): ECC component counts, `/insights` ~Feb-2026 GA date, claudemarketplaces.com aggregate totals, Shopify 60-70% auto-merge figure. SOURCES-QUICK-REFERENCE.md: added #37-#40 (superpowers, ECC, AGENTS.md standard, CodeGuard), count 36 → 40. |
| 2026-07-10 | Reduction Phase 6 — SOURCES.md prune + refresh (`drafts/REDUCTION-PROPOSAL-2026-07.md` §3, §5.7) | **4 additions**: Anthropic "How Claude Code works in large codebases" (Applied AI team, 2026-05-14, Tier A, new subsection under Anthropic Engineering Blog); Daniel Miessler PAI 5.0 → **LifeOS 6.0.2** rename (2026-07-02, Tier B, new bullet in the Miessler 2026 subsection, supersedes the TELOS/SPQA entry); Simon Willison "Agentic Engineering Patterns" guide (upgraded Tier C → B, extends the existing Willison entry with the deterministic-constraints position and 12+-chapter growth); Claude Code official best-practices page refreshed in place (not duplicated) with a changelog-revalidation-feed bullet (native `claude doctor` v2.1.205, Sonnet 5 default v2.1.197, agent teams v2 v2.1.178, Routines ~v2.1.198 flagged unverified) plus a new dedicated Sonnet 5 subsection. **Stale-markings**: claude-doctor (community) superseded by native `claude doctor`; `/insights` GA-Feb-2026 date softened to unconfirmed (command itself confirmed real); Fable 5/Mythos 5 suspension resolved as CONFIRMED-then-lifted (redeployed 2026-07-01, in production — the prior "not confirmed" framing was itself stale); Opus 4.7 Migration Guidance and the Vertrees LinkedIn entry both marked historical/provenance-only; Playwright-CLI 4× token claim and the valgard MCP-context-budget numbers both annotated stale-pending-remeasure (MCP tool search v2.1.121 changed the token economics); point-in-time star counts dropped (numbers removed, links kept) on everything-claude-code, GitHub Spec Kit, and claude-code-templates. **2 prunes**: Builder.io "50 Tips" and Morph "2026 Guide" deleted outright (no analysis-doc citations); shanraisshan annotated-superseded rather than deleted (cited by name in `mcp-daily-essentials.md` and `plugins-and-extensions.md`). **Link repointing**: 4 classes — `mcp-daily-essentials.md` → `mcp-patterns.md` (absorbed, 3 Pattern-line occurrences); `federated-query-architecture.md` / `security-data-pipeline.md` / `local-cloud-llm-orchestration.md` → `archive/<same-filename>` (evicted-with-tombstone per Phase 5, 5 Pattern-line occurrences incl. one anchored link); memory-systems archetype files → `memory-systems-archetype-recommendations.md` (1 historical-changelog bare-link repoint, 2026-04-30 row); plus the `session-quality-tools.md` companion fix (`analysis/` → `archive/`, 3 occurrences) triggered by the claude-doctor supersession. Also resolved the "Fable 5 suspended" item in the Unverified section (struck through, marked RESOLVED) and re-verified the four highest-stakes new Tier A claims (large-codebases post date/authorship, v2.1.205/v2.1.197/v2.1.178 changelog entries, Fable redeployment) against live primaries before writing them in. SOURCES-QUICK-REFERENCE.md refreshed to match (entries #2, #27, #29, #34; By Analysis Category #15/#22/#23/#25 annotated). Bumped "Last curated" to 2026-07-10. |
| 2026-06-21 | Verified cluster refresh (Fable 5 GA, loop-eng lineage, OKF/typed-knowledge, memory-systems + evals leaders) | Six verified clusters folded in. **Anthropic-official**: re-verified the canonical best-practices doc (added `/goal`+separate-evaluator, `Stop`-hook 8-block guard, `/rewind` checkpoints, `/btw` overlay, adversarial-review subagent, the five-item "Avoid common failure patterns" catalog, `@path` imports, plugins-first-class — all verbatim); registered **Claude Fable 5** (`claude-fable-5`, GA 2026-06-09, $10/$50, 1M/128k, adaptive-only, `stop_reason:"refusal"`, server-side `fallbacks`) + **Mythos 5** (Project Glasswing, no classifiers) + **Sonnet 4.6** (2026-02-17, $3/$15, 1M beta); **split** the conflated harness pages — corrected "Effective harnesses…" date to **2025-11-26** and registered the separate **Harness design** (2026-03-24, $124.70/3h50, $9 vs $200, self-praise bias) + **Scaling Managed Agents** (2026-04-08, p50 TTFT −60%/p95 −90%) pages; **dead-link fixes** — infrastructure-noise slug moved to `…/engineering/infrastructure-noise`, AI-resistant-evals slug corrected to capital-AI `…/AI-resistant-technical-evaluations` (NOT `/research/`); changelog version-attribution fix (lean system prompt = v2.1.154, not v2.1.181). **OKF / typed-knowledge** (⭐ elevated KM-leverage): enriched OKF v0.1 (Apache-2.0 sourced to REPO not blog; no central type registry; types-not-registered-centrally verbatim) + added **TypedMark** (Sébastien Dubois, 2026-06-20, new leader), **Hannecke frontmatter-first**, **TELOS/SPQA**. **Loop-eng lineage** (⭐ elevated KM-leverage): **reattributed** — Osmani's own post attributes the concept to Steinberger+Cherny (do NOT say Osmani coined it); repointed Cherny primary to YouTube/WorkOS, flagged the Stage-1/2/3 taxonomy + gate-conditions as secondary-only; corrected Huntley date (2025-07-14) and plugin-sourcing (README not ghuntley.com); corrected Karpathy (AutoResearch NOT in the Sequoia post); added **Peter Steinberger** (new leader, X post primary-unfetched). **Memory-systems**: registered MemGPT/Letta (Packer, new leader), mem0 (Singh, new leader), Anthropic memory-tool + context-engineering cookbook, LangMem. **Evals**: registered Husain + Shankar (new leaders), Schmid, Chase, three harness papers (Fudan/SJTU/Yao). All unverified items collected into the new **Unverified / pending revalidation (2026-06-21)** section at the end. Bumped "Last curated" to 2026-06-21. |
| 2026-06-15 | Loop-engineering research + unattended-execution audit signals + new EMERGING doc | Added [`scheduled-and-looping-primitives.md`](analysis/scheduled-and-looping-primitives.md) (EMERGING) for the genuinely-new product surface (`/loop`, `/goal`, cloud Routines, Desktop scheduled tasks, the Ralph lineage). Wired seven routing signals into [`AUDIT-CONTEXT.md`](AUDIT-CONTEXT.md) under a new **Unattended / Long-Running Execution** section (`harness-loop-config`, `harness-scheduled-agent`, `ci-scheduled-agent`, `harness-background-tasks`, `harness-dynamic-workflows`, `harness-goal-completion-loop`, `cron-disabled` guard) + matching `applies-to-signals` frontmatter, plus an **Unattended Execution Exposure** output section in [`ONE-LINE-PROMPT.md`](ONE-LINE-PROMPT.md). New themed **Loop Engineering & Unattended Execution Sources** section (Tier A: scheduling/workflow docs, Rajasekaran harness-design 2026-03-24, Scaling Managed Agents 2026-04-08, 2026 Agentic Coding Trends Report; Tier B: Cherny WorkOS 2026-06-02 quote, Karpathy Sequoia Ascent 2026-04-30, Huntley Ralph; Tier C bias-flagged commentary cloud). **Attribution fixes**: "loop engineering" was coined by Addy Osmani, not Cherny; "12 Agentic Harness Patterns" is Bilgin Ibryam, not Nate B. Jones. **Fixes folded in**: `/goal` version corrected v2.1.140 → v2.1.139 and the unsupported "fast-model checker" clause hedged in `harness-engineering.md`; cited the previously-uncited Rajasekaran primary source. **Routing-invariant fix**: documented the two-level memory-index sub-route so the six archetype docs reached through it (B/D/E/F, C-EC, genealogy-baseline) are no longer orphan-signal docs, and softened the footer's bidirectional-sync claim. **Volatile model note**: Fable 5 / Mythos 5 released 2026-06-09, suspended worldwide 2026-06-12 (US export-control directive), Opus 4.8 the fallback — added a `model-version-fable-mythos` row + currency note. Doc count 41 → 42 routable. |
| 2026-06-04 | First-party introspection registered + first doc enters retirement lane | Registered **Claude Code First-Party Introspection Commands** (`/insights`, `/usage`, `/doctor`) as Tier A after an obsolescence sweep found Anthropic converging on the edges of the audit's scope. `/insights` (GA Feb 2026 — native session-history analysis + auto-generated CLAUDE.md rules) is the cited **replacement** for the session-diagnostics slice: [`session-quality-tools.md`](archive/session-quality-tools.md) (repointed 2026-07-10 — the doc completed its retirement and moved to `archive/`) moved `PRODUCTION → RETIRING` with a `replacement-by` frontmatter field and a tombstone banner, and the audit's session-diagnostic routing now defers to `/insights` (keeping only the static committed-CLAUDE.md check + the uncalibrated-score caveat that `/insights` does not cover). `/usage` and `/doctor` registered as cited complements (cost-measurement and install-health), not replacements for the static evidence-tiered routing core. This is the first application of the project's new `RETIRING/RETIRED` retirement lane (per [planned-obsolescence intent](CONTRIBUTING.md) — prune as robust replacements mature). |
| 2026-05-30 | Opus 4.8 re-validation → SOURCES sync | Registered the Opus 4.8 release (2026-05-28, model ID `claude-opus-4-8`) across the source database after the four model-coupled docs and the audit routing were re-validated against 4.8 primary sources. New **Opus 4.8 Re-Validation (May 2026)** subsection with the 4.8 trio (Tier A — [What's New 4.8](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8), [system card](https://www.anthropic.com/claude-opus-4-8-system-card), [launch news](https://www.anthropic.com/news/claude-opus-4-8)); the 4.6→4.7 MRCR-v2 long-context regression case-study sources (OpenAI MRCR v2 + 4.7 card chart images Tier A + Context Arena/dev.to "232 pages" Tier B transcription); and the long-context degradation-onset benchmarks revalidating the "60%" heuristic (arXiv:2601.15300, Fiction.liveBench, NoLiMa/ICML 2025, arXiv:2510.05381). De-staled the Boris Cherny "(latest)" model reference and the Model Updates list to lead with Opus 4.8; bumped "Last curated" to 2026-05-30. The four harness arXiv papers cited in the 4.8 commit (2603.25723, 2603.28052, 2602.09540, 2605.15184) were already registered in the 2026-05-24 sweep — not re-added. Quick-reference: added entry #31 (Opus 4.8 trio) and corrected the stale #25 "Tingua" → "Tsinghua". |
| 2026-05-25 | Dapr durable-agents doc registered (Tier B) | Added **Dapr — Distributed Application Runtime** to Tier B for the imported [`dapr-durable-agents.md`](analysis/dapr-durable-agents.md): Dapr docs (docs.dapr.io, Tier A CNCF graduated project), Dapr Agents repo, SPIFFE (spiffe.io, Tier A), and Bilgin Ibryam's "production durable agent in ~10 lines" LinkedIn demonstration (Tier B). Infrastructure-as-runtime pattern, complementary to `mcp-vs-skills-economics.md` (tool-exposure layer). Doc adapted from the security-data-commons-blog archive (SDC framing stripped, repo-format frontmatter added). |
| 2026-05-24 | Anthropic changelog → analysis-doc integration + April 23 postmortem + Hoyt convergence + LangChain DeepAgents | Folded Q2 2026 Anthropic changelog (v2.1.117 → v2.1.150) into the relevant analysis docs as bounded subsections: agent-view + Ultrareview added to [`orchestration-comparison.md`](analysis/orchestration-comparison.md) as new sections; `/goal`, `mcp_tool` hooks, `continueOnBlock`, `worktree.bgIsolation`, per-category `/usage` added to [`harness-engineering.md`](analysis/harness-engineering.md) as "Harness Toolkit Additions (Q2 2026)"; plugin URL/zip loading, `claude plugin prune/tag`, `allowAllClaudeAiMcps` added to [`plugins-and-extensions.md`](analysis/plugins-and-extensions.md) as "Plugin Dependency & Distribution Updates"; `hard_deny` + sandbox path overrides added to [`safety-and-sandboxing.md`](analysis/safety-and-sandboxing.md) under Permission Model Design. **Unverified post resolved**: the previously-flagged "claude-code-quality-reports" 404 turned out to be at `/engineering/april-23-postmortem` — three independent bugs (March 4 reasoning-effort default high→medium, March 26 caching bug clearing extended thinking blocks, April 16 system-prompt verbosity cap) cumulatively degraded Claude Code intelligence across Sonnet 4.6/Opus 4.6/4.7 from early March through v2.1.116 on April 20. Added as Tier A vendor self-disclosure; integrated into [`behavioral-insights.md`](analysis/behavioral-insights.md) as "Vendor-Side Quality Regression Case Study" with implications for harness designers (effort-level defaults are load-bearing; brevity constraints at system-prompt layer can degrade output) and cross-referenced from `harness-engineering.md` v2-simplification section as a caveat to "trust vendor defaults." **Hoyt Emerson CLI-over-MCP** added as convergence data point to the "CLI + Skill Pattern" section in [`mcp-vs-skills-economics.md`](analysis/mcp-vs-skills-economics.md) — section expanded with a multi-source convergence table (Vallentin + Hoyt + Hex + ClickHouse + Reinhard + OSS Insight ≥6 major repos in Q1 2026). The second Hoyt claim (agents-build-tools-for-themselves) remains single-practitioner, not registered. **LangChain DeepAgents** (2026-02-17) added as the third independent practitioner replication of the harness-as-multiplier finding (52.8% → 66.5% on TerminalBench-2, gpt-5.2-codex held constant; "outside Top 30 → Top 5"; five middleware changes; public traces). Sits alongside Meta-Harness (arXiv:2603.28052) and SWE-Bench Mobile (arXiv:2602.09540) as the third independent corroboration of H-HARNESS-01's headline class of result. |
| 2026-05-24 | Tier A sweep + academic provenance closure | Completed biweekly Tier A sweep (gap from 2026-04-22 → 2026-05-24, ~4 weeks). Anthropic changelog: registered new doc URLs for `agent-view`, `ultrareview`, `/goal` (33 versions v2.1.117 → v2.1.150 in window; biggest architectural additions = agent-view supervisor process + git-worktree session isolation, ultrareview cloud bug-hunting fleet, hooks invoking MCP tools directly via `type: "mcp_tool"`, `hard_deny` auto-mode rules, `continueOnBlock` PostToolUse). Anthropic Research: registered "Teaching Claude why" (2026-05-08) — principle-teaching reduces agentic-misalignment blackmail rate 22% → 3% at 28× token efficiency vs honeypot data. **Academic sweep closed 3 outstanding-provenance gaps**: Stanford 6× orchestration figure = Meta-Harness paper (arXiv:2603.28052, Lee/Nair/Zhang/Lee/Khattab/Finn, Stanford+MIT, 2026-03-30); "Tingua NLH ablation" was misspelled — corrected to Tsinghua (arXiv:2603.25723, Pan/Zou/Guo/Ni/Zheng, 2026-03-26); Meta-Harness paper itself now has formal SOURCES.md entry with arXiv ID. Independent corroboration of the 6× figure registered as SWE-Bench Mobile (arXiv:2602.09540, Opus 4.5: 12% on Cursor vs 2% on OpenCode). New Tier A peer-reviewed paper: Agentic Context Engineering (arXiv:2510.04618, ICLR 2026) — first top-venue paper validating context-as-multiplier (+10.6% agent tasks). Counter-signal registered: Memanto (arXiv:2604.22085) reaches SOTA 89.8% with vector-only retrieval at long-horizon scale, scoping the "grep > embeddings" claim to small-KB regime. LongMemEval-V2 (arXiv:2605.12493) registered as successor benchmark with AgentRunbook-C file-as-memory pattern. One unverified Anthropic Engineering Blog post (claude-code-quality-reports, 2026-04-23) returned 404 on three URL variants — flagged, not registered. |
| 2026-05-24 | "Is Grep All You Need?" preprint added (arXiv:2605.15184) | Added Sen/Kasturi/Lumer/Gulati/Subbiah (PwC US, 2026-05-14) as Tier B preprint. 116-question LongMemEval study across 4 harnesses (Chronos, Claude Code, Codex, Gemini CLI) finds grep generally yields higher accuracy than vector retrieval, with harness choice having measurable effect independent of retrieval strategy. Cross-referenced into [`harness-engineering.md`](analysis/harness-engineering.md) supporting-evidence table and Sources section, and into [`memory-systems-archetype-a-curated-kb.md`](analysis/memory-systems-archetype-a-curated-kb.md) as empirical backing for the "claude-context against a small analytical KB is anti-pattern" claim. Discovered via Elvis S. LinkedIn post (2026-05-16) which acted as pointer; the LinkedIn post itself is not registered separately — only the underlying paper carries citable evidence. |
| 2026-05-24 | Cross-brain integration: Vallentin CLI+Skill recipe + H-HARNESS-01 tracking | Added Matthias Vallentin LinkedIn (2026-03-17) "CLI + Skill > MCP" as Tier B source with vendor-incentive caveat — extends existing Vallentin/Tenzir presence with concrete 4-step CLI-ification recipe (OpenAPI → @hey-api/openapi-ts → commander → skill) and `mavam/clattio` reference implementation. Added "The CLI + Skill Pattern" section to [`mcp-vs-skills-economics.md`](analysis/mcp-vs-skills-economics.md) covering when to apply, decision flow, and which parts of the categorical claim to discount. Added "Hypothesis Status and Falsifiability" section to [`harness-engineering.md`](analysis/harness-engineering.md) consolidating H-HARNESS-01 evidence with explicit falsifiability criterion (>6× from model-only swap would invalidate the thesis) and outstanding-provenance gap log (Stanford 6× orchestration figure, Meta-Harness paper, Tingua NLH ablation). Cross-repository tracker pointer to project1 hypothesis ledger added without duplicating tangential cross-brain evidence. |
| 2026-05-24 | Quality refresh + consumer-trust pass | URL canonicalization to `code.claude.com` (3 entries: sub-agents, hooks reference, verification guidance). Added 4 verified Tier B sources: Builder.io 50 Tips (Gopinath, 2026-03-20), Morph 2026 Best Practices Guide (2026-02-15), Shipyard Multi-Agent Orchestration (2026-03-18), VoltAgent awesome-claude-code-subagents (20.4k stars). Consumer-trust pass on analysis docs: backfilled `## Sources` footers across 16 docs that previously relied on inline YAML attribution only; surfaced vendor-reported caveats inline on Tier C performance claims (Graphify 71.5×, claude-context ~40%); cross-linked 7-repo portfolio evidence into `framework-selection-guide.md`, `orchestration-comparison.md`, and `memory-systems-archetype-recommendations.md`. Added "Last curated" header to top of this file. |
| 2026-04-29 | C-PII renamed to C-Egress-Constrained + genealogy baseline measurement | Renamed `analysis/memory-systems-archetype-c-pii.md` → `memory-systems-archetype-c-egress-constrained.md` after user reframed Wiley genealogy projects' egress posture (placeholder discipline + public-source data → vendor-LLM egress authorized at owner's choice). Genealogy moves out of canonical-example slot; replaced with medical/legal/journals-with-third-parties. **New empirical doc**: [`memory-systems-genealogy-baseline.md`](archive/memory-systems-genealogy-baseline.md) — 3 Sonnet subagents ran 3 queries each across the 3 sister projects, scored 8/9 DEFINITIVE (89%) on the unaugmented stack alone. Counter-intuitive finding: tool-call cost correlates with *availability of dedicated memory files*, not corpus size — dry-cross (3.3k md, 5 calls) cheaper than kindred (396 md, 14 calls). Architectural takeaway: CLAUDE.md routing + dedicated memory files for resolved issues + MEMORY.md as flat index is the load-bearing pattern, not graph augmentation. Updated archetype-c primary doc, recommendations index, migration paths (C ↔ C-EC), build-vs-borrow gaps. |
| 2026-04-30 | Tolaria + SiYuan + claude-video added; Archetype C-PII variant introduced; 2 architecture axes added | Verified Tolaria + SiYuan licenses via raw LICENSE fetch (both AGPL-3.0; my earlier "Tolaria is macOS-only" claim was wrong — releases ship .deb + AppImage + .exe + .dmg). Added entries #10, #11, #12 to `research/memory-systems-tools-inventory.md`. Created [`memory-systems-archetype-c-pii.md`](analysis/memory-systems-archetype-recommendations.md) (repointed 2026-07-10 — folded into the recommendations index during the Phase 3 memory-cluster fold; link kept pointing at its live successor) for the genealogy-style PII-constrained second-brain case (5,311-doc uninstrumented corpus is the canonical example). Added Axis 9 (block-level vs page-level granularity) and Axis 10 (agent contract: convention vs MCP vs CLI) to `memory-systems-architecture-axes.md`. Added watch-later YouTube ingest hybrid (claude-video) to Archetype C primary doc with explicit egress profile. Updated `memory-systems-archetype-recommendations.md` index, migration paths (C ↔ C-PII), and build-vs-borrow gaps. Doc count 142 → 143. |
| 2026-04-28 | Memory & knowledge archetype split + empirical Pass-2 testbed | Split omnibus recommendations into 7 per-archetype docs (`memory-systems-archetype-{a..g}-*.md`); added `memory-systems-graphify-vs-understand-anything.md` A/B comparison after running both LLM-driven graph builders on this repo. **New empirical evidence**: graphify Pass 1 (Tree-sitter) indexed 0 of 38 prose docs; Pass 2 produced 1187 nodes / 1651 edges / 67 communities / 88% EXTRACTED. Hallucination spot-check (n=8): ~25% of EXTRACTED cross-file prose edges hallucinated. Added 7 generic signals to AUDIT-CONTEXT.md (`md-corpus-*`, `vault-obsidian`, `vault-karpathy`, `corpus-sensitive`) so the new docs are reachable from the audit. Doc count 28 → 38. |
| 2026-04-28 | Memory & knowledge system sources added | Added Karpathy LLM Wiki paradigm (Tier B by author authority); 7 tool implementations with verified licenses (Pratiyush, MehmetGoekce, Lum1104 = MIT; Rowboat = Apache 2.0; graphify, claude-context = MIT; OpenBrain = FSL-1.1-MIT); InfraNodus + Paranyushkin (Tier B methodology); Avi Chawla post (Tier C). Registered for new analyses `memory-systems-archetype-recommendations.md` and `memory-systems-recommendation-methodology.md`. |
| 2026-04-22 | Opus 4.7 migration evidence | Added Anthropic migration guide, What's New 4.7, Best Practices 4.7 blog (Tier A); Vertrees LinkedIn, Willison counter-signal (Tier B); HN 47793411/47814832 (Tier C). Registered for use in new model-migration-anti-patterns analysis. |
| 2026-04-20 | Advisory-triggered refresh | Verified current — no new releases (latest v2.1.114), no new Anthropic blog posts since April 18. 90 sections, all sources valid. |
| 2026-04-18 | Sources refresh | Added v2.1.112-114 changelog, Opus 4.7 signal, expanded best-practices coverage |

*Last updated: 2026-07-16 (absorption-wave sweep — superpowers/ECC re-verifications, 5 new dossiers + index-lane note, CodeGuard plugin extension, canon follow-lane pointers, negative dossiers, 4 quarantine lines; see the changelog row above for the full breakdown). Prior: 2026-07-10 (Reduction Phase 6 — 4 additions, stale-markings across 7 entry classes, 2 prunes, link repointing for 4 retired analysis docs). Prior: 2026-06-21 (verified cluster refresh — Fable 5 GA + Sonnet 4.6 + harness-page split + dead-link fixes; OKF/typed-knowledge and loop-eng lineage elevated as KM-leverage sources; memory-systems + evals leaders registered; Unverified section added).*

---

## Unverified / pending revalidation (as of 2026-06-21; extended 2026-07-16)

Everything here either could not be primary-confirmed this pass, was contradicted by a primary, or is a single-practitioner claim seen-firsthand-but-not-independently-corroborated. **Do not present any of it as established fact elsewhere in this file.** Items resolve when a primary source confirms them; recheck by 2026-09-21 unless noted.

### Added 2026-07-16 (absorption-wave sweep)
- **ECC component counts (28 agents / 119 skills / 60 commands)**: from secondary pages (directory listings and write-ups), unverified against the repo tree — treat every specific ECC component count as directional, and note the repo's own earlier README carried different figures (125+/60+).
- **`/insights` GA date "~Feb 2026"**: still unconfirmed against any primary; the earliest changelog trace is v2.1.101 (2026-04), which presupposes an earlier ship date but does not establish a Feb-2026 GA (consistent with the 2026-07-10 annotation on the First-Party Introspection Commands entry above).
- **Marketplace aggregate totals**: claudemarketplaces.com figures ("4,265+ skills" etc.) are aggregator-self-reported and not independently verified — directional only.
- **Shopify "60-70% auto-merge of low-risk PRs"**: Bessemer secondary reporting with no Shopify primary — directional only, do not cite as a measured figure.

### Could not fetch / primary unconfirmed
- **Claude Fable 5 benchmark numbers** (SWE-bench, GPQA, capability scores): the launch-news page `https://www.anthropic.com/news/claude-fable-5` returned **HTTP 404** on 2026-06-21. No benchmark figure was confirmed from any primary. Do NOT assert Fable 5 benchmark specifics until the page is live or a docs page publishes them.
- **Claude Mythos 5 / Project Glasswing** beyond the launch doc: invitation-only, $10/$50 shared spec, no benchmarks. Docs confirm existence + access model only — treat any capability/benchmark claim as unverified.
- **Peter Steinberger X post** (`x.com/steipete/status/2063697162748260627`): primary URL UNFETCHABLE here (ECONNREFUSED; x.com blocks WebFetch). Wording corroborated by 4+ secondaries; **view count disputed** (~6.5M vs 2.2M — quarantine the number); date adjusted to 2026-06-07 per a secondary, still unconfirmed. Biographical claims (OpenClaw → OpenAI ~Feb 2026; CodeLooper) are independently reported but are biography, not the post content; OpenClaw "145K stars" stat unverified.
- **Cherny primary_url** (`thenewstack.io/loop-engineering/`): did not render the article body on direct fetch (newsletter/listing wrapper). Article exists (search-confirmed headline) and the quote is corroborated via WorkOS blog + YouTube + note.com + two Medium posts, but the named New-Stack URL itself did not confirm in this session — primary repointed to YouTube/WorkOS.
- **The New Stack "Loop Engineering" article**: paywall/auth-blocked for direct fetch; Osmani-as-coiner is corroborated by newsletters/search summaries but the New Stack body was not retrieved.
- **Managed Agents pricing**: the Apr 8 2026 engineering blog discloses NO pricing. The "$0.08/hr + tokens" figure carried elsewhere in this file (changelog) is from an older changelog read — re-verify against platform.claude.com docs before citing any cost figure.

### Contradicted by a primary / corrected this pass (do not reuse the old form)
- **"Osmani coined 'loop engineering'"** (asserted in three prior SOURCES lines): CONTRADICTED by Osmani's own 2026-06-07 post, which attributes the concept to Steinberger and Cherny. Do not state Osmani coined the term without a primary showing him doing so.
- **Effective-harnesses page "March 2026 update"** ($125/4hrs, Opus 4.6, "context anxiety"): does NOT exist on that page (Nov 26 2025); that material is on the separate Harness-design page (Mar 24 2026). The page also mis-dated 2026-03-01 in a prior draft — actual 2025-11-26.
- **"Opus 4.6 eliminates context anxiety"**: over-specifies the model — the harness-design page credits **Opus 4.5** ("largely removed that behavior on its own").
- **Changelog "lean system prompt is default" = v2.1.181**: WRONG — shipped in **v2.1.154** (May 28).
- **mem0 token-playbook "3,200 vs 130 / ~24× reduction"**: WRONG — the page says ~4,600 naive vs ~130 retrieval (≈35×) on the 200-entry example; the verified 24-entry example is 594 vs 166 (72%). The "3-4× average" headline is vendor-conservative, not independently benchmarked.
- **mem0 "State of AI Agent Memory 2026" date 2026-06-20**: WRONG — publication is **2026-04-01** (June 20 is a last-modified stamp). "Four unsolved gaps" understated — the page lists five-to-six.
- **Miessler "16 prompts"**: the verified primary carries **15** (6+2+5+1+1); the "16" count comes from local materials, whose 16th prompt is local-origin and gets labeled as such rather than attributed to the page (framing corrected 2026-07-12). **TELOS P0** is "Human Activation Crisis," not "human vulnerability to AI." "Telos files at USER/TELOS/" is not on the page.
- **Sonnet 4.6 64k output / OSWorld score**: the 64k output limit is on the models-overview page, NOT the Feb 17 2026 announcement; no numeric OSWorld score is on the announcement — don't cite one to it.
- **Opus 4.7 best-practices blog**: does NOT contain the "interprets prompts more literally / will not silently generalize / will not infer requests you didn't make" language (that's verbatim on the platform.claude.com migration guide), nor any "migration path through to Fable 5" statement (the migration guide does have an Opus-4.8→Fable-5 section). Both facts are true but belong to the migration-guide URL, not the blog.
- **Opus 4.8 news page**: does NOT itself state the 1M/200k context split, compaction/long-context recovery, adaptive-thinking-only, or literal-interpretation-carries-forward — those are true but sourced from the models overview, the What's-New 4.8 page, and the migration guide respectively.

### Vendor-claimed / single-source — not independently reproduced
- **Fabric README slogan/counts**: "Solve Once, Reuse Forever," "200+/300+ contributors," and PAI mentions are NOT in the current `danielmiessler/fabric` README; the "240+ patterns" figure is only on `danielmiessler.com/telos`. The modular-reuse philosophy is uncontested; the slogan + counts are unverified against the GitHub URL.
- **mem0 retrieval-quality deltas** (+29.6pt temporal, +23.1pt multi-hop) and LoCoMo (91.6→92.5)/LongMemEval (94.4-94.8) scores, and the 6,700-7,000 vs 25,000+ token comparison: NOT confirmed at any fetched primary — vendor-claimed, Tier C.
- **Letta** Core/Recall/Archival three-tier naming: from Letta *docs*, not the GitHub README. "May 2026 LettaBot archived / folded into Channels" not confirmable at the GitHub URL.
- **LangMem** `create_search_memory_tool`: NOT found on the fetched conceptual-guide page (only `create_manage_memory_tool` confirmed) — may live on a different page.
- **Karpathy AutoResearch** "66,000+ stars by early April 2026" / "~12 experiments/hour": unconfirmable (repo now ~87.9k stars; per-hour rate not stated on either primary) — Tier C.
- **Shreya Shankar** "CMU assistant professor from 2027": confirmed only to faculty-candidate status (March 2026); the start year is inference. The O'Reilly book + LLM-Evals-FAQ co-authorship are confirmed off-page, not on her papers page.
- **Philipp Schmid companion posts** (Inner/Outer Loop, AGENTS.md guide, Agent Skills tips, etc.): only `agent-harness-2026` was fetched; the other dates are author-asserted.
- **Hannecke token reduction**: headline "85%" ≠ the worked example's ~95.8% (~2,500 vs 60,000); "~500 tokens" is the manifest size alone. Author-reported, directional.

### Abstract-level only (full-text not read)
- **Terminal-Bench 2.0 (2601.11868)**: "81-82% with scaffolding," isolated Docker containers, and the "Harbor" framework are NOT in the abstract. Author count is 85 (not "84"); title is "…Hard, Realistic Tasks in Command Line Interfaces."
- **IRT-GRM judge paper (2602.00521)**: the "no universally robust configuration / vulnerable to minor formatting changes" claim is NOT in the abstract.
- **Agent-as-a-Judge (2601.05111)**: title is "Agent-as-a-Judge" (not "A Survey on…"); the procedural/reactive/self-evolving taxonomy and exact "five capabilities" are not in the abstract.
- **Externalization review (2604.08224)**: institutional affiliations (SJTU / Sun Yat-Sen / Shanghai Innovation Institute / CMU / OPPO) were not visible in the abstract fetch — title/21-authors/date/54pp/CC-BY-4.0 confirmed.

### Carried-over flags still open
- **SWE-bench Verified contamination** claims (32.67% solution leakage, 76% file-path recall): sourced only to a secondary blog (digitalapplied.com); the OpenAI internal audit + underlying paper were NOT fetched — remain unverified.
- ~~**"Fable 5 suspended worldwide 2026-06-12 (US export-control directive)"** (carried in a prior changelog row): NOT verified against any primary this pass and does NOT appear on the Fable post page — do not assert it.~~ **RESOLVED 2026-07-10**: CONFIRMED true by a primary — `anthropic.com/news/redeploying-fable-5` (2026-06-30) states the export-control suspension began 2026-06-12 and was lifted 2026-06-30, with both models redeployed 2026-07-01. See the Claude Fable 5 / Mythos 5 section above. Struck through rather than deleted, for provenance of the earlier unverified state.
- **TELOS git-commit date**: GitHub shows a last-commit badge but no resolvable commit date in the fetch; the prior "2024-01-17" was an HTML last-modified value. Date = unknown (repo existence, MIT, 1.4k stars, templates ARE verified).
- **OpenAI evaluation-best-practices publication date**: not shown on the page (unknown); the Oct 31 / Nov 30 2026 deprecation dates ARE confirmed verbatim.

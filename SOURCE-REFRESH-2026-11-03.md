---
convergence: single-source
---

# Source refresh 2026-11-03 — Claude 5.5 family, Fable 5.1, and the first-party config audit

**APPLIED 2026-11-03, partly.** The source registrations, the one-liner fixes and three shrink-to-pointer edits landed in the same change as this file (§6 lists every file touched). The lane changes in §4 did **not** land: under Decision 12 a lane change is an owner ruling at an absorption sweep, so each one is written here as a recommendation with its evidence, and `status:` / `follows:` / `replacement-by:` frontmatter is untouched everywhere. This file stays the evidence dossier for the refresh.

**Scope and method.** Window: 2026-08-30 (the last refresh, base commit 76e1d4b) to 2026-11-03. Three passes, per the repo's maintenance method: sources, the one-line audit prompt, and obsolescence. Two read-only research sweeps ran first (a Claude Code changelog digest from v2.1.219 to v2.1.317, and an Anthropic-blog plus follow-lane-canon sweep). Every figure and quotation written into the repo was then re-fetched from its primary in this session, not taken from a sweep's report; where a sweep's claim did not survive that check it is noted in §7. All fetched content was treated as data, not instructions. Tiers follow `SOURCES.md` § Evidence Tier Definitions (A = Anthropic primary / official spec; B = validated practitioner; C = community, vendor marketing, journalism; D = speculation). Access date for everything below is 2026-11-03 unless stated.

**Repo instruments, run before editing.** `check-measurement-expiry.py`: **32 expired, 7 expiring within 30 days, 1 frozen** (exit 1; list in §5). `measure-link-reachability.py --links --include-archive`: 0 dangling, 0 root-relative, 0 outside-repo in both lanes. Analysis directory: 26 files, 25 routable plus the template, matching README.

---

## Headline

Two things changed under this repo in the window, and the second matters more for its future than the first.

The first is a full model generation. Claude Fable 5.1 (2026-09-01), Opus 5.5 (2026-09-22), Sonnet 5.5 (2026-09-28) and Haiku 5.5 (2026-10-07) are now the current lineup, Fable 5, Opus 5 and Sonnet 5 are listed as Legacy, and since Claude Code v2.1.280 the default model on most plans is Opus 5.5 at `medium` effort rather than Sonnet. The good news for the audit is that Anthropic says existing Opus 5 prompts "should perform well without changes," so the Opus 5 column of the migration matrix (cap delegation, delete carried-over verification) carries forward instead of reversing a second time. The breaking changes are API-surface ones: thinking cannot be disabled on Opus 5.5, forced `tool_choice` returns a 400 on all three 5.x successors, and thinking blocks are now bound to the model and conversation that produced them.

The second is that Anthropic shipped the thing this repo's model-migration doc named as its advance trigger. `/doctor prompt-audit` (v2.1.283, 2026-09-25) audits a project's CLAUDE.md, AGENTS.md, rules, skills, commands, subagents and output styles for "instructions written for older models, references to files or commands that don't exist, and files that contradict each other," and proposes edits without applying them. That covers the find-and-fix half of `model-migration-anti-patterns.md` and a slice of what the routing audit's `claude-md-*` rows send people to read. Per the charter, that is a pruning finding, and §4 recommends it as one.

---

## 1. Model facts (Tier A unless marked)

| Model | ID | Released | $/MTok in / out | Default effort | Claude Code alias default from |
|---|---|---|---|---|---|
| Claude Fable 5.1 | `claude-fable-5-1` | 2026-09-01 | $10 / $50, cache read $0.25 | `high` | v2.1.257 (Fable) |
| Claude Opus 5.5 | `claude-opus-5-5` | 2026-09-22 | $4 / $20, cache read $0.20 | `medium` | v2.1.280 (Opus; default model on most plans) |
| Claude Sonnet 5.5 | `claude-sonnet-5-5` | 2026-09-28 | $2 / $10, cache read $0.10 | `high`, levels recalibrated | v2.1.284 (Sonnet, Anthropic API) |
| Claude Haiku 5.5 | `claude-haiku-5-5` | 2026-10-07 | from $0.10 / $0.50 ($0.50 / $2.50 over 100K) | `medium` | v2.1.293 (Haiku, Anthropic API) |

Sources: [models overview](https://platform.claude.com/docs/en/about-claude/models/overview) (lineup, prices, default effort, Legacy list, "Every Claude model ID is a pinned snapshot"); [model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations) (all four Active, retirement not sooner than one year after release; Sonnet 4.5 retiring 2026-11-30); [Fable 5.1 model page](https://platform.claude.com/docs/en/models/fable-5-1/overview) ("Released September 1, 2026"); the Claude Code changelog for the alias-default versions; launch posts for [Opus 5.5](https://www.anthropic.com/news/claude-opus-5-5) (2026-09-22), [Sonnet 5.5](https://www.anthropic.com/news/claude-sonnet-5-5) (2026-09-28), [Haiku 5.5](https://www.anthropic.com/news/claude-haiku-5-5) (2026-10-07) and [Fable 5.1 / Mythos 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1) (page shows "September 2026"). All four share 1M context, 128K output, a June 2026 reliable knowledge cutoff, and the tokenizer introduced with Opus 4.7, so the tokenizer confound the 2026-08-30 probe measured between 4.x and the 5 family does not reopen within the 5 family.

What changes for a harness, by model:

- **Opus 5.5** ([migration guide](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide), [prompting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)). Thinking can't be disabled (400 at every effort level); forced `tool_choice` `any`/`tool` returns 400; text between tool calls comes back as `thinking` blocks that are empty unless `display: "updates"` is set; default effort `medium`, and in Anthropic's testing `medium` "matched or beat Claude Opus 5 at `high` effort" on agentic coding. The prompting guide makes no statement that reverses the Opus 5 delegation or self-verification posture. It adds unattended-run guidance that maps onto this repo's premature-done framing ("Treat a text-only end of turn as a report rather than as proof the task is done"; "stop after two or three automatic continuations on the same task").
- **Sonnet 5.5** ([migration guide](https://platform.claude.com/docs/en/models/sonnet-5-5/migration-guide)). `thinking: {type: "disabled"}` returns 400; `between_tools` is the thinking-off option at effort `high` or below; effort levels recalibrated; forced `tool_choice` 400.
- **Fable 5.1** (model page). Four breaking changes from Fable 5: forced tool use errors, only Fable 5.1 / Mythos 5.1 read its thinking blocks, editing earlier turns invalidates thinking blocks, and some advisor pairings are unsupported. Mythos 5.1 offers the same capabilities "only to organizations verified through Anthropic's verification programs," a change from Mythos 5's no-classifier framing.
- **Haiku 5.5** (launch post). The first 1M-context Haiku; Anthropic positions it as a subagent model: it "pairs well with Opus 5.5 and Sonnet 5.5 as a subagent on coding work," while "Sonnet 5.5 and Opus 5.5 remain better choices for complex agentic coding tasks."
- **Claude Code defaults** ([model config](https://code.claude.com/docs/en/model-config)). Pro, Max, Ultra, Team, Enterprise and Anthropic API default to Opus 5.5; the `opus` / `sonnet` / `haiku` aliases resolve to the 5.5 models on the Anthropic API but to older models on some providers (for example `sonnet` is Sonnet 4.5 on Bedrock and Google Cloud's Agent Platform); Opus 5.5, Sonnet 5.5 and Haiku 5.5 default to `medium` effort in Claude Code. A project that uses the `opus` alias got a new model at v2.1.280 with no edit in its repo.

---

## 2. Claude Code harness changes, v2.1.222 → v2.1.317 (Tier A, raw changelog)

Only the items that change what an audit should check. Versions are from the raw CHANGELOG.md; dates are from the docs changelog page.

| Area | Change | Version |
|---|---|---|
| Config audit | `/doctor prompt-audit` (alias `/checkup prompt-audit`) audits CLAUDE.md files, skills, agents and commands "for prompting patterns written for older models"; same release: "stale paths, stale commands and contradicting instruction files now lead the report" | v2.1.283 (2026-09-25) |
| Config audit | `/claude-api prompt-audit` added (the repo had this as v2.1.216; the changelog and the skills docs both say v2.1.221) | v2.1.221 |
| Config audit | `/doctor` checkup flags "checked-in CLAUDE.md content Claude could derive from the codebase" and offers to migrate always-loaded guidance into skills and nested CLAUDE.md files ([skills docs](https://code.claude.com/docs/en/skills#check-your-setup-with-/doctor)); `/skill-doctor` shows unused skills and their context cost (v2.1.261) | docs; v2.1.261 |
| Permissions | Interactive sessions start in **auto mode** when no permission mode is configured, every plan and provider (v2.1.284); `claude -p` / SDK on third-party providers, telemetry off or fresh install start in `default` (v2.1.302) | v2.1.284, v2.1.302 |
| Permissions | Containment Escape rule: cloud metadata-credential fetches, egress evasion and cross-tenant reach no longer auto-approved unless marked expected | v2.1.257 |
| Hooks | `onFailure: "block"` lets command and HTTP hooks fail closed | v2.1.295 |
| Subagents | Agent tool `effort` parameter | v2.1.292 (2026-10-06) |
| Subagents | `CLAUDE_CODE_SUBAGENT_MODEL` now a default, not an override (v2.1.251); `..._FORCE` restores override (v2.1.257); `CLAUDE_CODE_SUBAGENT_EFFORT` (v2.1.316) | v2.1.251–316 |
| Subagents | Fork subagents default-on (interactive v2.1.232; `claude -p` and SDK v2.1.302); `omitClaudeMd` frontmatter (v2.1.271); auto-mode hand-back reviewed by the classifier (v2.1.271); subagent results marked so they "cannot pass as the session's own instructions" (v2.1.277) | v2.1.232–302 |
| Memory | AGENTS.md read in a project with no CLAUDE.md | v2.1.277 |
| Memory | Large-CLAUDE.md notice counts instruction files together | v2.1.281 |
| Loops | Todo/task tools off on Opus 4.8, Sonnet 5, Fable 5, Mythos 5 and newer (`CLAUDE_CODE_ENABLE_TODO_TOOLS=1` restores) | v2.1.233 |
| Loops | `/loop` self-paced mode always available; ultraplan removed (v2.1.222); Ultracode a separate `/effort` toggle (v2.1.284) | v2.1.222–284 |
| Models | Opus 4.8 fast mode deprecated, removal 2026-11-30 | v2.1.316 |

The memory docs also now state three facts the repo had only by inference: "target under 200 lines per CLAUDE.md file"; "A path-scoped rule loads when Claude uses the Read, Write, or Edit tool on a matching file"; and auto memory loads "The first 200 lines of `MEMORY.md`, or the first 25KB, whichever comes first" ([memory docs](https://code.claude.com/docs/en/memory)).

---

## 3. Practitioner and practice sources

| # | Source | Author / org | Date | Tier | URL | What's new | Touches |
|---|---|---|---|---|---|---|---|
| 1 | How the Claude Code team does code review | Osmani, Westlee Lunt, Wang (Anthropic) | 2026-10-15 | A (vendor) | https://claude.dev/blog/solving-code-review-at-anthropic/ | Parallel bug-hunting agents, then "a separate group votes on each finding"; 16% → 54% of internal PRs got substantive comments | agent-evaluation, orchestration-comparison |
| 2 | Building agents: When to fold subagents into your main agent loop | Diane Sarkis (Anthropic) | 2026-10-22 | A (vendor) | https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop | Subagents "are effective at verification, parallel work, and modular permissioning"; otherwise one loop | orchestration-comparison § When Not to Orchestrate |
| 3 | Audit your Agent files | Addy Osmani | 2026-08-27 | B | https://addyosmani.com/blog/audit-your-agent-files/ | Audit agent config every few weeks; "instruction value can expire, so archive first" | intent-alignment-audit, evidence-based-revalidation (convergence) |
| 4 | Brownfield Agentic Engineering | Addy Osmani | 2026-09-14 | B | https://addyosmani.com/blog/brownfield-agentic-engineering/ | "Worktrees isolate changes, not behavior" | orchestration-comparison |
| 5 | Breaking Claude Code Opus 5 Auto Mode | Simon Willison on Johann Rehberger | 2026-08-27 | B | https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/ | Classifier allowed a malware process, then blocked the command to stop it | safety-and-sandboxing |
| 6 | Astra for Coding: Why Are We Doing This Again? | Armin Ronacher | 2026-09-07 | B | https://lucumr.pocoo.org/2026/9/7/astra-why/ | "I honestly do not need an agent to run for 35 hours on a single prompt" | scheduled-and-looping-primitives (counter-signal) |
| 7 | Per-release posts: Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5 | Simon Willison | 2026-09-01 → 10-07 | B | simonwillison.net (four URLs in SOURCES.md) | Follow-lane liveness; per-release dossier now spans 4.7 → 5.5 | model-migration-anti-patterns |
| 8 | anthropics/claude-code#90943 | GitHub user report | 2026-08-31 | C | https://github.com/anthropics/claude-code/issues/90943 | Shared index across concurrent sessions silently reverts committed work; worktrees are the fix git enforces | orchestration-comparison |
| 9 | Claude's new auto eval tool | Hamel Husain | 2026-09-30 | B | https://hamel.dev/blog/posts/claude-auto-evals/ | Canon liveness; skeptical of tools that do not center looking at data | agent-evaluation |
| 10 | The Batch, issue 372 | DeepLearning.AI | 2026-09-25 | C (reports Cognition's own figures) | https://www.deeplearning.ai/the-batch/issue-372/ | Lead model plans and reviews while a cheaper model writes code; 36% lower cost per task is the vendor's number | orchestration-comparison (advisor/executor) |

Canon liveness: Willison, Osmani, Ronacher, Ng and Husain published in window; Karpathy active on unrelated topics; Shankar's latest post is 2026-05-21; ClaudeLog shows an update date of 2026-10-30 but its mechanics pages were not re-opened. The engineering blog's one post in window ("Redesigning source control at Anthropic," 2026-10-13) is not about Claude Code practice; practice posts are on claude.com/blog, claude.dev/blog and claude.com/resources, a third venue the weekly sweep should add.

---

## 4. Obsolescence recommendations, per routable doc

Prune means retire and archive; shrink means keep a pointer plus the retained delta; keep means no change in lane. "Applied" marks the edits that landed with this file; everything else is a recommendation.

| Doc | Recommendation | Evidence | Applied |
|---|---|---|---|
| model-migration-anti-patterns | **Shrink, then RETIRING** toward `/doctor prompt-audit` + per-model prompting guides; retain the cross-version matrix and probe rows | `/doctor prompt-audit` v2.1.283 covers the find-and-fix audit (Supported, GA, Citeable; covers substance for the workflow, not for the matrix). The 2026-08-13 assessment was Partial; it is now Mostly | Banner, "Absorption Event 2" section, Audit Workflow now points at the first-party command first, version fix v2.1.216 → v2.1.221. Status flip **not** applied |
| claude-md-progressive-disclosure | **Shrink; move to `follow`** with first-party memory docs as canon; keep the 6-repo dataset | Memory docs give "target under 200 lines" and the path-scoped-rule mechanics; `/doctor` performs the always-loaded → on-demand migration | Currency section added (incl. when a path-scoped rule does not load). Lane **not** changed |
| scheduled-and-looping-primitives | **Keep** (follow lane); record partial trigger | Opus 5.5 prompting guide covers the premature-done limb; cost-runaway and weak-RETHINK limbs not covered | Short section added |
| mcp-vs-skills-economics | **Prune** (RETIRING → RETIRED + archive), overdue since 2026-09-30 | `/usage` gained a Loops breakdown (v2.1.243) and warnings for always-on context and large tool results (v2.1.299); `/doctor` folds in `/usage` recommendations (v2.1.305) | No |
| plugins-and-extensions | **Shrink to pointer**, overdue since 2026-09-30; re-examine the dsh counter-evidence first as PLAN.md asks | `/skill-doctor` (v2.1.261) and `/doctor` extension checks now report unused skills, MCP servers and plugins against context cost; `claude plugin eval` (v2.1.269) | No |
| memory-systems-recommendation-methodology | **Fold into archetype-recommendations** (ruled 2026-07-16, scheduled 2026-09-30, did not run) | Owner ruling already exists | No |
| orchestration-comparison | **Keep**; candidate for a partial follow on § When Not to Orchestrate | Anthropic's 2026-10-22 fold-subagents article restates that section's position first-party; per-subagent model/effort/scope mechanics are now configuration | Subsection added on per-subagent model, effort and scope and on concurrent sessions sharing one checkout |
| safety-and-sandboxing | **Keep** | No absorber; auto mode as the unconfigured default raises the doc's relevance | Subsection added on moved defaults, `onFailure: "block"`, the Rehberger bypass, and deliberate blocks as stop conditions |
| automated-config-assessment | **Keep, re-rule convergence** | The 2026-07-16 ruling said doctor/checkup are install-health, not assessment. `/doctor prompt-audit` is closer: it checks a project's instruction files against stated patterns and proposes remediation. Still not baseline → deviation → remediation over a config baseline, so I lean keep `single-source`, but it deserves a fresh look | No |
| intent-alignment-audit, evidence-based-revalidation | **Keep; re-rule convergence** of the drift/staleness practice | Osmani's 2026-08-27 "Audit your Agent files" is an independent practitioner exemplar of re-checking instruction files on a cadence, and `/doctor prompt-audit` is a first-party instrument for one slice of it. The README says no independent adoption survived verification; that sentence may now be wrong | No |
| behavioral-insights | **Keep** | No absorber; new gap: no Claude 5.5-family arm exists in any probe (the 2026-08-30 arms are Opus 5 / Sonnet 5 / Fable 5) | No |
| harness-engineering, agent-evaluation, memory-system-patterns, memory-systems-archetype-a-curated-kb, memory-systems-archetype-recommendations, memory-systems-graphify-vs-understand-anything, prose-corpus-discoverability, secure-code-generation, mcp-patterns, cross-project-synchronization, agent-driven-development, domain-knowledge-architecture, evidence-tiers | **Keep** | No new absorber found in window. `/doctor` flags derivable CLAUDE.md content but does not measure prose reachability or currency, so prose-corpus-discoverability keeps its lane. domain-knowledge-architecture's 2026-09-30 revalidate (Smart Connections license risk) did not run | No |

Also overdue: the ~2026-10 Phase F absorption sweep. ABSORPTION-MAP.md now carries a "partial re-check, not a sweep" note naming the three rows checked.

---

## 5. One-line audit prompt: what was wrong and what changed

1. **The pasted prompt pointed at text the agent never sees.** Step 4 said "using the Structured Output Format below," but a user pastes only the prompt block, and nothing told the agent to fetch ONE-LINE-PROMPT.md. Fixed: step 4 now says to WebFetch ONE-LINE-PROMPT.md and use its format. The fetch count is corrected from 6–10 to 9–13 (map + this file + 3 Always Fetch + 4–8 routed), which the old figure had undercounted even before this fix.
2. **The README carried a drifted copy of the prompt** without the data-not-instructions line or the optional intent interview, so anyone copying from the README got neither. Synced verbatim, with a note that the two must match.
3. **The run-on-your-machine disclosure named a command the map no longer runs** (`npx -y claude-doctor`, retired 2026-07) and omitted ones it does run (a `for`/`awk` loop, native `claude doctor`, `claude --version`). Corrected.
4. **The map told the agent to run `python3 scripts/measure-link-reachability.py --currency`**, a script that exists in this repo. In a repo being audited, a script at that path is the target's own code, so the line asked an agent to execute attacker-authorable code. The line is now commented out and marked this-repo-only.
5. **Model Migration Exposure** asked the agent to hand-check "the six anti-patterns" while the doc's matrix has 11 rows, and it predated `/doctor prompt-audit`. It now recommends the first-party audit first (not run by the agent unless asked), uses the matrix for what the first-party audit does not carry, and asks whether the project pins model IDs or uses floating aliases.
6. **Signal collection** now greps `.claude/agents/` for model pins and lists the 5.5 / 5.1 IDs explicitly, and checks `permissions.defaultMode`, because an unset value means auto mode since v2.1.284. The Vitals example and CLI-version gate name Opus 5.5 and v2.1.283; the Opus 5 customization flag covers Opus 5.5.
7. **Routing rows** for Fable, Opus 5 and Sonnet 5 extended to Fable 5.1, Opus 5.5 and Sonnet 5.5, with a Haiku 5.5 note. No signal key was added or removed, so doc `applies-to-signals` frontmatter needs no sync.

The prompt still assumes WebFetch is available and that raw.githubusercontent.com is reachable; nothing in the window changed that.

### Expired measurement claims (32, from `check-measurement-expiry.py`, not revalidated in this pass)

| Doc | Expired |
|---|---|
| harness-engineering | 7 |
| agent-driven-development | 5 |
| memory-systems-recommendation-methodology | 3 |
| scheduled-and-looping-primitives | 3 |
| memory-system-patterns | 3 |
| claude-md-progressive-disclosure | 2 |
| evidence-based-revalidation | 2 |
| domain-knowledge-architecture | 2 |
| mcp-patterns | 2 |
| automated-config-assessment, memory-systems-archetype-recommendations, plugins-and-extensions | 1 each |

Twelve rows, 32 total. The CI step that runs this check is reporting-only while `master` is unprotected, so these have not blocked anything.

---

## 6. Files changed with this refresh

- `SOURCE-REFRESH-2026-11-03.md` — this file.
- `SOURCES.md` — Claude 5.5 family + Fable 5.1 section; `/doctor prompt-audit` entry; changelog digest v2.1.222 → v2.1.317; lineup line; practice-posts block; refresh-log row; Unverified additions; `prompt-audit` version fix; both currency markers.
- `SOURCES-QUICK-REFERENCE.md` — the pointer's last-curated date (the top-30 list was not re-ranked).
- `AUDIT-CONTEXT.md` — model grep, `defaultMode` grep, CLI-version comment, Fable / Opus 5 / Sonnet 5 rows, `/doctor prompt-audit` deference note, this-repo-only caution on the reachability script, marker.
- `ONE-LINE-PROMPT.md` — step 4 fetch fix, fetch count, disclosure fix, Vitals and inventory rows, Session Quality line, Model Migration Exposure rewrite, customization flag.
- `README.md` — Quick Start prompt synced, fetch count, two doc-count fixes (27 → 25, 24 → 25), model-migration capability row.
- `ABSORPTION-MAP.md` — partial re-check note; trigger cells on three rows.
- `PLAN.md` — marker; the stale "Agent tool has no effort override" sentence annotated; a High Priority row listing the owner rulings in §4.
- `analysis/model-migration-anti-patterns.md`, `analysis/claude-md-progressive-disclosure.md`, `analysis/orchestration-comparison.md`, `analysis/safety-and-sandboxing.md`, `analysis/scheduled-and-looping-primitives.md` — the additions named in §4.

---

## 7. Not found, not verified, or corrected during verification

- **Fable 5.1 / Mythos 5.1 and Opus 5.5 system cards** were not read. No 5.5-family injection or behavioral figures are recorded anywhere in the repo.
- **`SubagentHandback` hook event and `isolation: "remote"`**: present in docs or tool surfaces, but no changelog line found for when they shipped.
- **`/goal`**: no changelog line in this range; assumed unchanged since the 2026-06-21 verification.
- **Sonnet 5.5 cache-read price**: the changelog first said $0.20 (v2.1.284) and corrected it to $0.10 (v2.1.296); the migration guide says $0.10. A bundled reference cached 2026-10-06 still said $0.20, which is why the primary was used.
- **"Router, not encyclopedia" wording for CLAUDE.md**: community posts only; the first-party substance is the 200-line target and path-scoped rules, cited instead.
- **Auto-mode fallback after repeated blocks ("3 in a row or 20 per session")**: search-snippet only.
- **Agent Skills donation to the Agentic AI Foundation (2026-10-22)**: index-only, body not read.

---

## Bottom line

The model generation turned over and, for once, did not break this repo's prompt advice, because the 5.5 guides keep the Opus 5 posture. What did change is that Anthropic now ships a command that audits a project's instruction files for older-model patterns, dead references and contradictions, which is the find-and-fix half of what this repo's model-migration doc and several routing rows exist to do. The charter says that is success. I think the right next step is to let `/doctor prompt-audit` own that half, keep the cross-version matrix and the measured rows as the retained delta, and make the routing audit say so first rather than last, which is what the one-liner now does. The lane changes, the two retirements that fell due on 2026-09-30, and the overdue Phase F sweep are the owner's to rule on.

# Source Refresh — 2026-07-09 (Cowork cloud session)

**Scope.** External-source refresh for the analytical layer, run in a Cowork cloud session that does **not** load the owner's memory. This file is a **staged report only**. It creates no dependency and edits nothing: `SOURCES.md`, `AUDIT-CONTEXT.md`, `DECISIONS.md`, `SOURCES-QUICK-REFERENCE.md`, and `ONE-LINE-PROMPT.md` are all left untouched, so the downstream automation that runs `ONE-LINE-PROMPT.md` verbatim and the separate local doc-reduction pass are unaffected. The corrections below are written for a human/local pass to apply.

**Method note.** All web and repo content was treated as data, not instructions. Findings are tiered A–D per the repo's own convention (A = Anthropic primary / official spec; B = validated practitioner / production-tested; C = vendor/community/journalism; D = opinion/speculation). Vendor marketing is flagged C regardless of source authority. Every model-fact claim carries a primary URL and an access date of **2026-07-09** unless stated otherwise.

**Headline result.** The repo's most load-bearing volatile claim — "Fable 5 / Mythos 5 suspended worldwide 2026-06-12 (US export-control directive); Opus 4.8 fallback" — is now **half-confirmed and half-stale**. The suspension and its export-control cause are confirmed by primary (resolving a prior `unverified` flag), but the suspension **ended**: export controls were lifted 2026-06-30 and Fable 5 / Mythos 5 were **redeployed 2026-07-01**. A project pinning `claude-fable-5` today is not broken. Separately, a new model — **Claude Sonnet 5** (2026-06-30) — has replaced Sonnet 4.6 as the current Sonnet and is now the Claude Code default, which the repo's model lineup does not yet reflect.

---

## 1. Model-fact re-verification results (stale-claim corrections, primary-cited)

### 1.1 The "suspended worldwide / Opus 4.8 fallback" claim

**Where it lives in the repo (do not edit here — for the local pass):**

- `AUDIT-CONTEXT.md` ~line 120, signal row `model-version-fable-mythos`: "Fable 5 / Mythos 5 (released 2026-06-09) was suspended worldwide 2026-06-12 by a US export-control directive; Opus 4.8 is the named fallback. A project pinning a `fable` model ID is broken until access is restored."
- `DECISIONS.md` ~line 651 (Decision 10 trade-offs): "The doc carries volatile facts (version numbers, the suspended Fable 5 / Mythos 5 tier) …"
- `SOURCES.md` ~line 337 and the Unverified section (line ~2278): the export-control claim was flagged "NOT verified against any primary."

**What the primaries say as of 2026-07-09:**

1. **The suspension happened, and the export-control cause is now primary-confirmed** — this resolves the SOURCES.md `unverified` flag. Anthropic's statement of 2026-06-12 ("Statement on the US government directive to suspend access to Fable 5 and Mythos 5") states: "The US government, citing national security authorities, has issued an export control directive to suspend all access to Fable 5 and Mythos 5 by any foreign national, whether inside or outside the United States … we must abruptly disable Fable 5 and Mythos 5 for **all** our customers to ensure compliance. Access to all other Anthropic models will not be affected." Source: https://www.anthropic.com/news/fable-mythos-access (accessed 2026-07-09).

2. **The mechanism was an export restriction on foreign nationals, not a blanket safety recall.** Because Anthropic "had no reliable way to verify nationality in real-time," it suspended access for everyone. The trigger was an Amazon report of a *narrow, non-universal* jailbreak (prompting Fable to identify — and in one case demonstrate exploitation of — software vulnerabilities). Anthropic's testing showed "many less capable models — including Claude Opus 4.8, GPT-5.5, and Kimi K2.7 — could identify the same vulnerabilities," and every model tested could reproduce the single exploit demonstration. Source: https://www.anthropic.com/news/redeploying-fable-5 (accessed 2026-07-09).

3. **The suspension ended. Access was restored.** "As of today, June 30, the export controls on Fable 5 and Mythos 5 have been lifted. Fable 5 will be available starting tomorrow, Wednesday, July 1, to users globally on the Claude Platform, Claude.ai, Claude Code, and Claude Cowork." Mythos 5 was restored for a set of approved US organizations following US-government approval on 2026-06-26. AWS, Google Cloud, and Microsoft Foundry re-enablement "as quickly as possible." Source: https://www.anthropic.com/news/redeploying-fable-5 (accessed 2026-07-09). The API launch doc now carries the banner "Access to Claude Fable 5 and Claude Mythos 5 has been restored." Source: https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (accessed 2026-07-09).

4. **"Opus 4.8 fallback" conflates two different things.** There are two distinct fallbacks, and the repo's currency note blurs them:
   - **Suspension-era fallback** ("use Opus 4.8 because Fable is disabled") — this was the operative advice for the 2026-06-12 → 2026-06-30 window only. It is now obsolete.
   - **Standing classifier fallback** (permanent design feature) — Fable 5 carries safety classifiers covering cybersecurity, biology/chemistry, and distillation; flagged requests are automatically served by Opus 4.8 and the user is notified. "More than 95% of Fable sessions involve no fallback at all." This is not a suspension artifact and remains true today. Sources: https://www.anthropic.com/news/claude-fable-5-mythos-5 and https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 (both accessed 2026-07-09).

**Recommended correction (for the local pass, not applied here):** Rewrite the `model-version-fable-mythos` signal row and the DECISIONS/SOURCES currency notes to read, in substance: *"Fable 5 / Mythos 5 (GA 2026-06-09) were suspended 2026-06-12 under a US export-control directive restricting access by foreign nationals, then redeployed 2026-07-01 after the controls were lifted 2026-06-30. As of 2026-07-09 both are available (Fable 5 GA globally; Mythos 5 limited to approved Glasswing partners). A pinned `claude-fable-5` ID works today. Note the standing classifier fallback: Fable routes cyber/bio-chem/distillation queries to Opus 4.8 (<5% of sessions)."* The audit-signal intent is unchanged — a `fable`/`mythos` pin is still worth flagging as volatile, but the reason is now "verify current availability and plan for the classifier-fallback refusal path," not "the model is unavailable."

### 1.2 The Fable 5 launch page and benchmark numbers

- **The 404 was a wrong slug, not a missing page.** The repo recorded that `https://www.anthropic.com/news/claude-fable-5` returned HTTP 404 on 2026-06-21. That short slug is still empty. The live launch page is at **`https://www.anthropic.com/news/claude-fable-5-mythos-5`** (accessed 2026-07-09, HTTP 200, full content). The API launch doc is at `https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5`.

- **Qualitative benchmark claims are now primary-attributable.** The launch page states Fable 5 "is state-of-the-art on nearly all tested benchmarks of AI capability" and that "the longer and more complex the task, the larger Fable 5's lead." Named, attributable customer results now exist as primary quotes, e.g.: Stripe reported a codebase-wide migration in a 50-million-line Ruby codebase "in a day that would otherwise have taken a whole team over two months by hand"; Cognition's FrontierCode eval — "Fable 5 scores highest among frontier models, even at medium effort"; on *Slay the Spire*, file-based memory "improved its performance three times more than for Opus 4.8"; Fable "beat FireRed with a minimal, vision-only harness."

- **The precise numeric scores remain image-locked.** The head-to-head benchmark table on the launch page is a PNG; SWE-bench / GPQA / capability numbers are not present as text and could not be transcribed from a primary this pass. **Recommendation:** downgrade the SOURCES.md "all Fable 5 benchmark numbers UNVERIFIED" flag to "qualitative SOTA claims and named customer results primary-confirmed; precise numeric scores remain image-only, not text-verified." Do not assert specific SWE-bench/GPQA integers.

### 1.3 New model — Claude Sonnet 5 (this is the biggest lineup gap)

The repo's lineup treats **Sonnet 4.6** as the current Sonnet. As of 2026-06-30 that is stale.

- **Claude Sonnet 5** (`claude-sonnet-5`), announced 2026-06-30. "Built to be the most agentic Sonnet model yet … its performance is close to that of Opus 4.8, but at lower prices." Source: https://www.anthropic.com/news/claude-sonnet-5 (accessed 2026-07-09).
- **Pricing:** introductory **$2 / $10 per MTok through 2026-08-31**, then standard **$3 / $15**. Uses an updated tokenizer (as with Opus 4.7); "the same input can map to more tokens: roughly 1.0–1.35× depending on the content type."
- **Availability / defaults:** default model for Free and Pro plans; available to Max/Team/Enterprise, in Claude Code, and on the Claude Platform. Per the Claude Code changelog (v2.1.197, 2026-06-30): "now the default model in Claude Code, with a native 1M-token context window."
- **Specs (models overview, accessed 2026-07-09):** 1M context, 128k max output, adaptive thinking, no extended thinking, reliable knowledge cutoff Jan 2026.
- **Safety:** launched with cyber safeguards on by default (same as Opus 4.7/4.8); lower hallucination and sycophancy than Sonnet 4.6; cannot develop a working Firefox exploit (0.0%), materially weaker cyber than Opus 4.8 / Mythos 5.
- **Consequence for the repo:** Sonnet 4.6 has dropped out of the "Latest models comparison" on the models-overview page (now Fable 5 / Opus 4.8 / Sonnet 5 / Haiku 4.5) and moves to legacy. Sources that say "current Sonnet = 4.6" or "Sonnet 4.6 preferred ~70% over 4.5" should be reframed as historical.
- **Numeric caveat:** Sonnet 5's own eval numbers are image-locked on the launch page. The page's changelog does restate two *Sonnet 4.6* figures under new methodology (Humanity's Last Exam 34.6% no-tools / 46.8% with-tools; OSWorld-Verified 78.5%) — these are 4.6 numbers, not 5.

### 1.4 Current model lineup and selection guidance (models overview, accessed 2026-07-09)

| Model | API ID | Price (in/out per MTok) | Context / max out | Thinking | Notes |
|---|---|---|---|---|---|
| Claude Fable 5 | `claude-fable-5` | $10 / $50 | 1M / 128k | Adaptive (always on) | Most capable widely released; classifier refusals → Opus 4.8 |
| Claude Opus 4.8 | `claude-opus-4-8` | $5 / $25 | 1M / 128k | Adaptive | Default effort `high`; recommended default for complex agentic coding |
| Claude Sonnet 5 | `claude-sonnet-5` | $3 / $15 ($2/$10 intro thru 2026-08-31) | 1M / 128k | Adaptive | New; Claude Code default; updated tokenizer |
| Claude Haiku 4.5 | `claude-haiku-4-5` | $1 / $5 | 200k / 64k | Extended thinking | Unchanged |

- **Selection guidance (verbatim):** "start with **Claude Opus 4.8** for complex agentic coding and enterprise work. For workloads that need the highest available capability, use **Claude Fable 5**."
- Fable 5 / Mythos 5 supported features at launch: effort, task budgets (beta header `task-budgets-2026-03-13`), memory tool, code execution, programmatic tool calling, context editing (beta `context-management-2025-06-27`), compaction, vision.
- Mythos 5 (`claude-mythos-5`): shares Fable 5 specs/pricing, no safety classifiers, invitation-only via Project Glasswing, not GA.

---

## 2. New / updated sources table

Tier per repo convention. "Touches" is pointer-level (which analysis docs or `AUDIT-CONTEXT` signals the source most affects). None of this is wired into routing here.

| # | Source (title) | Author / Org | Date | Tier | URL | What's new vs current SOURCES.md | Touches |
|---|---|---|---|---|---|---|---|
| 1 | Statement on the US directive to suspend Fable 5 / Mythos 5 | Anthropic | 2026-06-12 | A | https://www.anthropic.com/news/fable-mythos-access | Primary confirmation the 06-12 suspension was a US export-control directive (foreign-national restriction). Resolves the SOURCES.md "export-control claim unverified" flag. | `AUDIT-CONTEXT` `model-version-fable-mythos`; SOURCES Fable/Mythos + Unverified |
| 2 | Redeploying Fable 5 (with access-restored update) | Anthropic | 2026-06-30 (update 07-01) | A | https://www.anthropic.com/news/redeploying-fable-5 | Suspension ended: controls lifted 06-30, Fable/Mythos redeployed 07-01. Makes the repo's "broken until restored / Opus 4.8 fallback" note stale. Adds the cross-vendor jailbreak-severity framework (Capability gain / Breadth / Ease of weaponization / Discoverability) + govt-collaboration commitments. | `AUDIT-CONTEXT` `model-version-fable-mythos`; DECISIONS Decision 10; `safety-and-sandboxing.md` |
| 3 | Claude Fable 5 and Claude Mythos 5 (launch) | Anthropic | 2026-06-09 | A | https://www.anthropic.com/news/claude-fable-5-mythos-5 | The live launch page (the repo's tried `/news/claude-fable-5` was the wrong slug). Named customer capability claims (Stripe 50M-line Ruby migration in a day; Cognition FrontierCode highest even at medium effort; Slay the Spire memory 3× over Opus 4.8; FireRed vision-only). Standing classifier fallback: >95% of sessions no fallback. | SOURCES Fable/Mythos section; `behavioral-insights.md`; `model-migration-anti-patterns.md` |
| 4 | Introducing Claude Sonnet 5 | Anthropic | 2026-06-30 | A | https://www.anthropic.com/news/claude-sonnet-5 | Entirely new model absent from the repo. Replaces Sonnet 4.6 as current Sonnet; Claude Code default; $2/$10 intro → $3/$15; updated tokenizer (~1.0–1.35×); cyber safeguards default-on. | SOURCES Model Updates + QUICK-REF #34; `behavioral-insights.md`; `AUDIT-CONTEXT` model-version signals |
| 5 | Models overview (current lineup) | Anthropic (docs) | accessed 2026-07-09 | A | https://platform.claude.com/docs/en/about-claude/models/overview | Current lineup = Fable 5 / Opus 4.8 / Sonnet 5 / Haiku 4.5 (Sonnet 4.6 → legacy). Selection guidance: Opus 4.8 default, Fable 5 for highest capability. Knowledge cutoff Jan 2026. | SOURCES Model Updates; QUICK-REF #34 |
| 6 | Introducing Claude Fable 5 and Claude Mythos 5 (API/integration doc) | Anthropic (docs) | accessed 2026-07-09 | A | https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 | Now carries "access restored" banner. Confirms `stop_reason:"refusal"` (HTTP 200), three fallback paths, fallback-credit billing, adaptive-only, raw CoT never returned. Supported-features list (task budgets beta, memory tool, code execution, etc.). | SOURCES Fable/Mythos; `mcp-patterns.md` (fallback handling) |
| 7 | Claude Code changelog (v2.1.178 → v2.1.205) | Anthropic (docs) | 2026-06-15 → 2026-07-08 | A | https://code.claude.com/docs/en/changelog | Post-mid-June deltas: Sonnet 5 as CC default (v2.1.197); `/code-review <level>` multi-agent split from fast `/review` (v2.1.186/196/202); subagents background-by-default + `/agents` wizard removed (v2.1.198); subagents "less likely to re-delegate entire task" (v2.1.203); 5-level depth cap enforced foreground too (v2.1.181); MEMORY.md compaction reminder (v2.1.186); org default models + model restrictions (v2.1.187/196). | `orchestration-comparison.md`; `agent-principles.md`; `plugins-and-extensions.md`; `memory-system-patterns.md`; `AUDIT-CONTEXT` harness + model-version rows |
| 8 | Dynamic workflows / `ultracode` | Anthropic (docs + blog) | keyword rename v2.1.160, 2026-06-02 | A | https://code.claude.com/docs/en/workflows · https://claude.com/blog/introducing-dynamic-workflows-in-claude-code | Repo has `workflows` (v2.1.154) but not the `ultracode` framing. Trigger keyword renamed `workflow`→`ultracode`; `/effort ultracode` = xhigh effort + auto dynamic-workflow orchestration; in-window: "Dynamic workflow size" `/config` setting + workflow OTel attrs (v2.1.202). | `scheduled-and-looping-primitives.md`; `orchestration-comparison.md`; `harness-engineering.md` |
| 9 | Find bugs with ultrareview (`/code-review ultra`) | Anthropic (docs) | research preview since v2.1.86 | A | https://code.claude.com/docs/en/ultrareview | Repo has ultrareview, but the new bit is the `/code-review <level> <pr#>` restructure and that `/review <pr>` reverted to single-pass (v2.1.202). Cloud fleet, verified-only findings, $5–20/run after 3 free. | `orchestration-comparison.md`; `safety-and-sandboxing.md` |
| 10 | Claude Fable is relentlessly proactive | Simon Willison | 2026-06-11 | B | https://simonwillison.net/2026/jun/11/fable-is-relentlessly-proactive/ | New Willison piece (repo only has his Apr Opus-4.7 + Feb patterns work). Documents a real mid-session Fable→Opus-4.8 classifier downgrade ("hit some invisible guardrail and downgraded itself to Opus"; Opus inherited the full transcript and finished). Fable "relentlessly proactive" — behavioral counter-signal to the 4.7 "literal, won't infer" posture. Strong sandbox-necessity + prompt-injection-amplification argument. ~$12 session. | `behavioral-insights.md`; `safety-and-sandboxing.md`; `model-migration-anti-patterns.md` |
| 11 | Initial impressions of Claude Fable 5 | Simon Willison | 2026-06-09 | B | https://simonwillison.net/2026/Jun/9/claude-fable-5/ | Companion first-impressions piece (referenced, not fully fetched this pass). | `behavioral-insights.md` |
| 12 | Loop Engineering (O'Reilly Radar republication) | Addy Osmani / O'Reilly | 2026-06 | B (venue lift) / C (content) | https://www.oreilly.com/radar/loop-engineering/ | Same five-block anatomy the repo already cites from `addyosmani.com`, but republished on O'Reilly Radar — a more authoritative venue that partially lifts the loop-engineering label out of single-blog Tier C. | `scheduled-and-looping-primitives.md`; `harness-engineering.md` |

Notes on tiering: rows 1–9 are Anthropic primary (Tier A). The Fable launch page's *customer testimonial* quotes within row 3 are vendor-curated and should be read as C-grade marketing even though the page itself is A. Rows 10–11 are Tier B (named practitioner, production anecdote). Row 12 is a venue upgrade of existing repo content, not net-new substance.

---

## 3. Staged SOURCES.md entry text (ready for the local pass to paste)

The following blocks match the repo's existing entry style. They are **staged, not applied.** Paste into the indicated SOURCES.md sections during the local pass.

### 3a. Replace/annotate the Fable 5 / Mythos 5 subsection currency note (SOURCES.md ~line 321–337)

```markdown
#### Claude Fable 5 / Mythos 5 — availability update (2026-07-09 re-verification)

Fable 5 (`claude-fable-5`) and Mythos 5 (`claude-mythos-5`) went GA 2026-06-09, were
**suspended 2026-06-12** under a US-government export-control directive, and were
**redeployed 2026-07-01** after the controls were lifted 2026-06-30. As of 2026-07-09
both are available: Fable 5 GA globally on Claude API / Claude.ai / Claude Code / Cowork
(cloud providers re-enabling); Mythos 5 restored to approved US Glasswing partners
(US-govt approval 2026-06-26).

- **Primary — Suspension statement**: https://www.anthropic.com/news/fable-mythos-access
  (2026-06-12). Verbatim: "an export control directive to suspend all access to Fable 5
  and Mythos 5 by any foreign national … we must abruptly disable Fable 5 and Mythos 5 for
  all our customers … Access to all other Anthropic models will not be affected." Trigger:
  an Amazon report of a narrow, non-universal jailbreak (identify/demonstrate a software
  vulnerability); Anthropic confirmed Opus 4.8, GPT-5.5, Kimi K2.7 and others reproduce it.
  Tier A. Accessed 2026-07-09.
- **Primary — Redeployment**: https://www.anthropic.com/news/redeploying-fable-5 (2026-06-30,
  access-restored update 07-01). Verbatim: "As of today, June 30, the export controls on
  Fable 5 and Mythos 5 have been lifted. Fable 5 will be available starting tomorrow,
  Wednesday, July 1, to users globally." Adds the cross-vendor jailbreak-severity framework
  (capability gain / breadth / ease of weaponization / discoverability) with Amazon,
  Microsoft, Google. Tier A. Accessed 2026-07-09.
- **RESOLVED (was Unverified 2026-06-21)**: the "export-control directive" cause is now
  primary-confirmed. The prior "suspended worldwide / Opus 4.8 the fallback / broken until
  restored" framing is superseded — access is restored.
- **Standing classifier fallback (permanent, not a suspension artifact)**: Fable 5 routes
  cybersecurity / biology-chemistry / distillation queries to Opus 4.8; "more than 95% of
  Fable sessions involve no fallback." Source: https://www.anthropic.com/news/claude-fable-5-mythos-5.
- **Benchmark status**: the live launch page is
  https://www.anthropic.com/news/claude-fable-5-mythos-5 (the earlier `/news/claude-fable-5`
  slug was wrong). Qualitative SOTA + named customer results (Stripe 50M-line Ruby migration
  in a day; Cognition FrontierCode highest at medium effort; Slay the Spire memory 3× over
  Opus 4.8; FireRed vision-only) are primary-confirmed; precise numeric scores remain
  image-only and are NOT text-verified — do not assert specific SWE-bench/GPQA integers.
- **Revalidate by**: 2026-10-09 (availability + included-subscription window are volatile).
```

### 3b. New Model Update rows (SOURCES.md Model Updates list, ~line 230)

```markdown
- **Claude Sonnet 5** (2026-06-30; model ID `claude-sonnet-5`): "most agentic Sonnet yet,"
  performance "close to that of Opus 4.8, but at lower prices." Default model on Free/Pro and
  the Claude Code default (changelog v2.1.197). $2/$10 per MTok introductory through
  2026-08-31, then $3/$15. 1M context, 128k output, adaptive thinking, no extended thinking,
  knowledge cutoff Jan 2026. Updated tokenizer (as with Opus 4.7): "the same input can map to
  more tokens: roughly 1.0–1.35×." Cyber safeguards on by default (same as Opus 4.7/4.8);
  lower hallucination and sycophancy than Sonnet 4.6; cannot develop a working Firefox exploit
  (0.0%). Sonnet 4.6 drops to legacy. Sources:
  https://www.anthropic.com/news/claude-sonnet-5 ,
  https://platform.claude.com/docs/en/about-claude/models/whats-new-sonnet-5 ,
  https://platform.claude.com/docs/en/about-claude/models/overview . Tier A. Accessed 2026-07-09.
  ⚠️ Sonnet 5's own numeric eval scores are image-only on the launch page and NOT text-verified.
- **Current lineup (2026-07-09)**: Fable 5 / Opus 4.8 / Sonnet 5 / Haiku 4.5. Selection
  guidance (models overview, verbatim): "start with Claude Opus 4.8 for complex agentic coding
  and enterprise work. For workloads that need the highest available capability, use Claude
  Fable 5." Opus 4.1 retirement (Aug 5 2026) unchanged.
```

### 3c. New Claude Code feature rows (SOURCES.md Claude Code Documentation / Changelog section)

```markdown
- **`ultracode` / dynamic workflows** (keyword rename in changelog v2.1.160, 2026-06-02):
  the dynamic-workflow trigger keyword was renamed `workflow` → `ultracode`; `/effort ultracode`
  couples xhigh reasoning effort with automatic dynamic-workflow orchestration. Post-mid-June:
  a "Dynamic workflow size" `/config` setting (small/medium/large agent counts, advisory not a
  cap) and `workflow.run_id`/`workflow.name` OTel attributes (v2.1.202, 2026-07-06). Docs:
  https://code.claude.com/docs/en/workflows ; blog:
  https://claude.com/blog/introducing-dynamic-workflows-in-claude-code . Tier A (blog body
  corroborated via search, not fetched this pass — see Unverified). Accessed 2026-07-09.
- **`/code-review <level>` restructure** (changelog v2.1.186/196/202, 2026-06-22 → 07-06):
  `/review <pr>` reverted to a fast single-pass review; `/code-review <level> <pr#>` is the
  multi-agent review at a chosen effort level; five cleanup finders merged into one (~25% fewer
  tokens, v2.1.196). The cloud "ultra" tier is `/code-review ultra` / ultrareview (research
  preview since v2.1.86): https://code.claude.com/docs/en/ultrareview . Tier A. Accessed 2026-07-09.
- **Subagent defaults shift** (changelog v2.1.198, 2026-07-01): subagents now run in the
  background by default and inherit the session's extended-thinking config; the `/agents` wizard
  was removed ("ask Claude to create or manage subagents, or edit `.claude/agents/` directly").
  v2.1.203 (2026-07-07): "agents are now less likely to re-delegate their entire task to another
  subagent." Foreground subagents respect the same 5-level depth cap as background (v2.1.181).
  Source: https://code.claude.com/docs/en/changelog . Tier A. Accessed 2026-07-09.
- **Org model governance** (changelog v2.1.187/196, 2026-06-23/29): org-configured default
  models ("Org default"/"Role default" in `/model`) and org model restrictions applied to the
  model picker, `--model`, `/model`, and `ANTHROPIC_MODEL`. Candidate new audit signal (model
  governance). Tier A. Accessed 2026-07-09.
```

### 3d. Practitioner entries (SOURCES.md Tier B / Willison + loop-engineering sections)

```markdown
### Simon Willison — "Claude Fable is relentlessly proactive" (2026-06-11)
- **URL**: https://simonwillison.net/2026/jun/11/fable-is-relentlessly-proactive/
  (companion: https://simonwillison.net/2026/Jun/9/claude-fable-5/ , 2026-06-09)
- **Evidence Tier**: B (named practitioner; first-hand production anecdote)
- **Contribution**: Documents a real mid-session Fable→Opus-4.8 classifier downgrade
  ("Having figured out all of these tricks Fable … hit some invisible guardrail and downgraded
  itself to Opus. Thankfully Opus had access to the full transcript and could continue").
  Characterizes Fable 5 as "relentlessly proactive" — a behavioral counter-signal to the 4.7
  "interprets literally / won't infer" posture: Fable independently wrote a CORS capture server,
  injected JS into templates to trigger a modal, and used pyobjc/Quartz to screenshot native
  browser windows, from a one-line prompt. Reinforces the sandbox-necessity and
  prompt-injection-amplification argument ("frontier models know every trick in the book … if it
  does get subverted … the amount of damage it can do given its relentless proactivity is
  terrifying"). Session cost ~$12.11 (fable-5 + opus-4-8).
- **Touches**: behavioral-insights.md, safety-and-sandboxing.md, model-migration-anti-patterns.md
- **Revalidate by**: 2026-10-09
```

---

## 4. Not found / still unverified

1. **Precise Fable 5 benchmark integers** (SWE-bench Verified, GPQA, capability scores): the launch-page benchmark table is a PNG; no numeric score was text-verifiable from any primary this pass. Qualitative SOTA + named customer results are confirmed; specific integers are not.
2. **Sonnet 5 numeric eval scores**: image-locked on the Sonnet 5 launch page. Only relative statements ("close to Opus 4.8," "strict improvement over 4.6") and restated *Sonnet 4.6* figures (HLE 34.6%/46.8%, OSWorld-Verified 78.5%) are text-available. `whats-new-sonnet-5` docs page not fully fetched.
3. **Dynamic-workflows blog body** (`claude.com/blog/introducing-dynamic-workflows-in-claude-code`): the `ultracode` framing and `/effort ultracode` behavior are confirmed via the Claude Code changelog (v2.1.160) and `code.claude.com/docs/en/workflows` exists, but the dedicated blog post body was corroborated via web search only, not fetched. Treat the blog as pointer-level until fetched.
4. **Addy Osmani "Agentic Code Review"** (`addyosmani.com/blog/agentic-code-review/`) and the **O'Reilly Radar** loop-engineering republication: surfaced in search, not fetched. Dates and exact content unverified; the agentic-code-review post would bear directly on the new `/code-review` material if confirmed.
5. **Daniel Miessler PAI → LifeOS rename** (`github.com/danielmiessler/LifeOS`, "General-Purpose AI Harness … distributed as a Skill"; search snippet says "LifeOS 6.0.0"): plausible evolution of the repo's PAI 5.0 entry, but the repo/version was not fetched. Do not assert the "6.0.0" version or a hard PAI→LifeOS supersession without fetching the primary.
6. **Willison "route to a cheaper subagent" tip** (Fable-as-orchestrator delegating to Sonnet 5 workers via Managed Agents, worker-rate billing): summarized from a secondary aggregator (AI Weekly). The underlying Willison note/TIL was not fetched — verify before citing as his direct guidance.
7. **Included-subscription window for Fable 5** is volatile and secondary sources disagree. The primary redeployment post says Fable 5 is included "for up to 50% of weekly usage limits through July 7," then usage credits; Willison's 06-11 post (pre-redeployment) mentions a Max allowance "up until June 22nd"; a third-party guide says "free until July 12." Treat any included-window date as in-flux; rely on the redeployment post for the current window and re-check.
8. **Agent SDK**: no material named change appeared in the Claude Code changelog window (2026-06-15 → 2026-07-08). This is an observed absence, not a gap in coverage — the SDK sections of the repo do not appear to need a currency correction this pass.
9. **Cloud-provider (AWS / Vertex / Foundry) Fable 5 re-enablement timing**: the redeployment post says "as quickly as possible" without a date. A project deploying Fable 5 on Bedrock/Vertex/Foundry should verify current availability directly.

---

*Prepared 2026-07-09 in a Cowork cloud session (owner memory not loaded). One new file only; no existing repo file edited. Hand off to the local pass for SOURCES.md / AUDIT-CONTEXT.md / DECISIONS.md application and the separate doc-reduction workstream.*

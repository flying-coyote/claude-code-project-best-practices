---
evidence-tier: Mixed
applies-to-signals: [harness-loop-config, harness-scheduled-agent, ci-scheduled-agent, harness-background-tasks, harness-goal-completion-loop]
last-verified: 2026-06-15
revalidate-by: 2026-09-15
status: EMERGING
measurement-claims:
  - claim: "/loop runs interval or self-paced; minimum 1-minute interval; .claude/loop.md default prompt; recurring tasks auto-expire 7 days after creation; CLAUDE_CODE_DISABLE_CRON kill-switch; requires Claude Code v2.1.72+"
    source: "Claude Code docs — Run prompts on a schedule (code.claude.com/docs/en/scheduled-tasks)"
    date: "2026-06-15"
    revalidate: "2026-09-15"
  - claim: "/goal sets a completion condition and keeps working across turns until met; added v2.1.139 (2026-05-11)"
    source: "Anthropic Claude Code changelog"
    date: "2026-06-15"
    revalidate: "2026-09-15"
  - claim: "Cloud Routines run autonomously on Anthropic infrastructure with no permission prompts, 1-hour minimum interval"
    source: "Claude Code docs — Run prompts on a schedule (three-way Cloud/Desktop/loop comparison table)"
    date: "2026-06-15"
    revalidate: "2026-09-15"
---

# Scheduled & Looping Primitives: Unattended Execution in Claude Code

**Evidence Tier**: Mixed (A-B-C) — official Claude Code docs and changelog plus the Boris Cherny quote (Tier A, per this repo treating the Claude Code creator as Tier A), named-practitioner technique and analysis (Tier B: Huntley, Karpathy), and the June-2026 "loop engineering" commentary cloud (Tier C, bias-flagged).

## Purpose

This doc covers the first-party primitives that let Claude Code run **unattended, recurring, or until-done** — `/loop`, `/goal`, cloud Routines, Desktop scheduled tasks, and the Ralph-style continuous loop — and the audit signals that detect a project using them. It is deliberately lean: the scheduling surface is now first-party, so the job here is to point at the official controls and surface the operational risk an audit should flag, not to teach a discipline. For the in-run mechanics these primitives wrap (completion loops, self-verification, doom-loop detection, the reasoning-effort allocation across plan/build/verify), the researched anchor stays [`harness-engineering.md`](harness-engineering.md); this doc is its operational, scheduling-facing companion.

Status is **EMERGING**: the commands are real and documented (Tier A), but the surrounding "loop engineering" framing is two weeks old as of mid-June 2026 and mostly secondary-sourced, so the analytical claims here are held lightly pending production evidence.

---

## The Unattended-Execution Surface

Claude Code shipped a cluster of looping and scheduling primitives across Q2 2026. They differ on one axis that matters for an audit — **where the loop lives and who, if anyone, is watching**:

| Primitive | What it does | Where it persists | First shipped | Tier |
|---|---|---|---|---|
| `/loop` | Re-runs a prompt on an interval, or self-paced (Claude picks the cadence and stops when the task is provably complete) | In-session; optional `.claude/loop.md` (project) / `~/.claude/loop.md` (user) default prompt | v2.1.72+ | A — [scheduled-tasks docs](https://code.claude.com/docs/en/scheduled-tasks) |
| `/goal` | Sets a completion condition; Claude keeps working turn-after-turn until it holds, then stops | In-session; live overlay of elapsed/turns/tokens | v2.1.139 (2026-05-11) | A — [changelog](https://code.claude.com/docs/en/changelog) |
| Cloud Routines (`/schedule`) | Cron-style runs on Anthropic infrastructure, autonomously, **with no permission prompts** | Anthropic cloud (may leave no on-disk footprint in the repo) | Q2 2026 | A — [scheduled-tasks docs](https://code.claude.com/docs/en/scheduled-tasks) |
| Desktop scheduled tasks | Local cron that starts a fresh session able to edit/commit/PR | `~/.claude/scheduled-tasks/<name>/SKILL.md` (relocated under `CLAUDE_CONFIG_DIR` if set) | Q2 2026 | A — [desktop scheduled-tasks docs](https://code.claude.com/docs/en/scheduled-tasks) |
| Ralph-style continuous loop | A `while`-loop re-feeding a fixed prompt each iteration; state survives via files + git | A `Stop` hook (official plugin) or an external shell loop | plugin: 2026; technique: 2025-07 | A (Anthropic plugin) / B (Huntley origin) |
| Dynamic workflows | Claude writes a JS orchestration script the runtime executes in the background, fanning out subagents | `.claude/workflows/*.js` (project) / `~/.claude/workflows/` (user) | v2.1.154 (2026-05-28) | A — [workflows docs](https://code.claude.com/docs/en/workflows) |

Dynamic workflows are an orchestration primitive rather than a scheduling one, so the deeper treatment lives in [`orchestration-comparison.md`](orchestration-comparison.md); they appear here only because they share the same new detectable footprint an audit should learn to read.

### The three-way scheduling comparison

The official docs draw the distinction an audit should care about — autonomy and where the work runs:

| | Cloud Routines | Desktop scheduled tasks | In-session `/loop` |
|---|---|---|---|
| Runs on | Anthropic cloud | Your machine, fresh session | Your current session |
| Permission prompts | **None** | Per the session's settings | Per the session's settings |
| Minimum interval | 1 hour | per task | 1 minute |
| Survives the session? | Yes (cloud) | Yes (local store) | No (expires 7 days after creation) |
| On-disk footprint to audit | Often none | `~/.claude/scheduled-tasks/` | `.claude/loop.md` (if a default is set) |

The autonomy column is the operational risk. A cloud Routine running with no permission prompts, or a Desktop task that starts a fresh session against the working directory **including uncommitted changes**, is a different blast-radius than an interactive session a human approves call-by-call. Desktop tasks also fire one catch-up run on wake, so a 9 a.m. task can run at 11 p.m. against stale state.

---

## "Loop engineering": the orchestration face of harness engineering

In June 2026 a label — *loop engineering* — attached itself to a practice the repo already analyzes under [harness engineering](harness-engineering.md). The honest provenance matters, because the label is thinner than its volume suggests:

- The **practice** comes from Boris Cherny (Claude Code creator), at the WorkOS-hosted *Acquired Unplugged* event on 2026-06-02 (video: YouTube `RkQQ7WEor7w`). The four-word "My job is to write loops" is **host-anchored** — quoted directly by the event's host Michael Grinich (WorkOS) in his LinkedIn writeup (Tier A-minus: named host, dated event, presented as quotation). The fuller passage commonly cited — "I don't prompt Claude anymore. I have loops that are running... My job is to write loops." — is now rendered consistently across multiple independent published accounts: The New Stack's loop-engineering article, a note.com near-verbatim share (2026-06-09), and Medium write-ups by Njuguna and Flor (both 2026-06-08), all converging on the same wording. It remains video-derived — no published account gives a timestamp, and WorkOS's own event writeup paraphrases these sentences — so cite the short quote as host-attributed and the fuller passage as corroborated across independent published accounts, without attaching a timestamp.
- The **term** was coined by Addy Osmani (Google), not Cherny — The New Stack credits Osmani with naming it. Several aggregators conflate the two and attribute Osmani's "building blocks of a loop" enumeration to Cherny; that attribution is wrong and is not repeated here.
- Anthropic's own published progression stops at *prompt engineering → context engineering* ("we view context engineering as the natural progression of prompt engineering," [Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), 2025-09-29). The third rung is supplied by commentators. This repo named that rung *harness engineering* and backs it with research the loop-engineering cloud lacks ([Meta-Harness arXiv:2603.28052](https://arxiv.org/abs/2603.28052), [NLH arXiv:2603.25723](https://arxiv.org/abs/2603.25723)).

So "loop engineering" is the orchestration and iteration-cadence face of harness engineering, not a separate discipline. Andrej Karpathy's framing is the most useful steelman: coding is the ideal self-improvement loop precisely because it has built-in verification — "tests pass or fail, programs run or crash, diffs can be inspected" (Tier B — Karpathy, [Sequoia Ascent 2026](https://karpathy.bearblog.dev/sequoia-ascent-2026/), 2026-04-30). That verification property is what makes the unattended primitives above safe to leave running at all, and it is why the design question is never "loop or not" but "what closes the loop, and what bounds it."

The Ralph lineage is the concrete antecedent the productized commands descend from: Geoffrey Huntley's "Ralph Wiggum" technique (Tier B — [ghuntley.com/ralph](https://ghuntley.com/ralph/), 2025-07) is a `while` loop feeding a fixed prompt file to an agent each iteration, with state surviving through the codebase, a TODO/plan file, and per-iteration git commits. Anthropic packaged it as an official plugin (a `Stop` hook that blocks exit and re-feeds the prompt) and credits Huntley directly. One correction to common write-ups: the official plugin keeps state **across** iterations via files and git; the fresh-context-per-iteration variant is one design choice, not the default.

---

## Audit Signals (detection)

These map to the routing rows added to [`AUDIT-CONTEXT.md`](../AUDIT-CONTEXT.md). All detection is Tier A from the official docs; the analytical reading of what to do about a hit is the EMERGING part.

| Signal | Detection | Routes to | Why |
|---|---|---|---|
| `harness-loop-config` | `ls .claude/loop.md ~/.claude/loop.md` | this doc + safety-and-sandboxing | A `loop.md` defines what a bare `/loop` runs unattended; a forgotten recurring loop runs for up to 7 days. |
| `harness-scheduled-agent` | `find ~/.claude/scheduled-tasks -name SKILL.md` | this doc + safety-and-sandboxing | Desktop tasks start fresh sessions that can commit/PR against uncommitted state; host-level, optional like session diagnostics. |
| `ci-scheduled-agent` | `.github/workflows` with a `schedule:`/`cron:` trigger **and** a `claude`/`claude-code-action` invocation | this doc + safety-and-sandboxing | A cron-triggered agent that commits or opens PRs autonomously in CI — higher-stakes than `/loop`. |
| `harness-background-tasks` | `ls -d .claude/worktrees/` or `bgIsolation` in settings | orchestration-comparison + this doc | Background sessions auto-isolate into worktrees; confirms reliance on long-running background work. |
| `harness-goal-completion-loop` | `/goal` at a user-turn text head in `~/.claude/projects/` transcripts (anchored) | harness-engineering + this doc | Run-until-condition has a distinct failure surface (cost runaway, premature "done") from interval loops. Anchored match **triggers** — bare `grep "/goal"` was 80% FP (tested 2026-06-16), the user-turn-head anchor 0%. |
| `cron-disabled` *(negative guard)* | `CLAUDE_CODE_DISABLE_CRON=1` | suppress the **local** rows only; no fetch | If local cron is off, `/loop` and Desktop tasks can't fire; loop-hardening advice would be noise. **Does not clear the cloud-Routine concern** — a server-side Routine is unaffected by this local env var, so still emit the operator question. |

The unattended signals cluster deliberately: even when several trip at once, they dedupe to this doc plus `safety-and-sandboxing.md` (and at most `orchestration-comparison.md` / `harness-engineering.md`), so the cluster stays within the audit's [anti-bloat budget](../AUDIT-CONTEXT.md#anti-bloat-rule-deterministic) rather than firehosing.

---

## Counter-Evidence / What This Does *Not* Mean

The June-2026 enthusiasm runs ahead of the evidence in three ways worth holding onto:

- **Delegation is still narrow.** Anthropic's 2026 Agentic Coding Trends Report (Tier A) found developers use AI in roughly 60% of work but *fully delegate* only 0–20% of tasks. "I just write loops" is a leading-practitioner posture, not the median workflow. Treat the framing as aspirational signal, not a current baseline.
- **The term is press-coined and two weeks old.** Strip the commentary cloud (The New Stack, MindStudio, Data Science Dojo, Louis Bouchard, Verloy/Rubrik — all Tier C) and "loop engineering" reduces to one Cherny quote plus the productized commands. It does not yet clear the bar to enter this repo's voice as a paradigm; it enters as a named workflow with an attributed source.
- **A pure-cloud Routine may leave no on-disk footprint.** The detection signals catch `.claude/`-local and CI configurations; a project running cloud Routines on Anthropic infrastructure can be entirely invisible to a repo-local audit — and even the in-session `CronList` tool does not enumerate them (it lists only session `CronCreate` jobs, verified 2026-06-16), so a tool-assisted audit misses them too. The audit should say so rather than imply full coverage.

## Gaps

- **Gap: runaway-loop economics.** No published $/hour or token-burn figure for a 7-day `/loop` or a long-running cloud Routine left unattended (the nearest anchors are Managed Agents at ~$0.08/hr and the harness-design post's ~$200/6hr). A **Tier-D triangulation** on those anchors (2026-06-19): cost spans ~3 orders of magnitude by *activity rate*, not duration — a throttled/idle loop is single-digit dollars (cf. the safety doc's ~60K tokens over 9 days), while an active Opus loop at the ~$33/hr anchor (~$200/6hr) is ~$800/day → ~$5.6K over 7 days. The blast-radius control that matters is therefore a **token/$ budget ceiling**, not just a time bound. **Needs**: a real measured $/hr from a bounded `/loop` with cost telemetry to upgrade this from Tier D to Tier B.
- **Gap: detection reliability (closed 2026-06-19).** (a) `harness-goal-completion-loop` — **RESOLVED**: against a realistic transcript (a `src/goal/` path, "the /goal of…", a URL, "what is the /goal here?"), the bare `grep "/goal"` measured **80% false-positive**, while anchoring `/goal` to a user-turn text head gave **0 false positives, 1/1 true hit** (tested 2026-06-16). The signal now uses the anchored predicate and **triggers** rather than only informs. (b) `harness-scheduled-agent` — **CONFIRMED** from the official Desktop scheduled-tasks docs (2026-06-19): a local task is stored at `~/.claude/scheduled-tasks/<kebab-case-name>/SKILL.md` (or under `CLAUDE_CONFIG_DIR`), the file carrying YAML frontmatter `name`/`description` with the prompt as the body — so the `-name SKILL.md` predicate is correct and the signal graduates. One adjacent gap: a *durable* `/loop` cron persists separately to project-local `.claude/scheduled_tasks.json` (per the `CronCreate` tool's `durable` mode), a different artifact no current signal catches — candidate second predicate if durable `/loop` tasks become common.
- **Gap: cloud-Routine visibility (closure is structurally partial).** A pure-cloud Routine leaves no repo-local or host-local artifact, so the whole unattended-execution cluster is blind to it — and `cron-disabled` gives false reassurance, because a local env var does not disable a server-side Routine. Closure: (1) make "ask the operator to list cloud Routines + cadence" a **required output line**, not a caveat — the only reliable detector of a pure-cloud Routine; (2) `CronList` **confirmed NOT** to enumerate cloud Routines (verified 2026-06-16: it lists only `CronCreate` jobs created *in the session*, returning "No scheduled jobs" otherwise), so a tool-assisted audit misses pure-cloud Routines exactly as a disk-glob does — the operator question in (1) is the only reliable detector; (3) amend `cron-disabled` to suppress only local rows and still emit the operator question. **Needs**: a testbed Routine to verify the operator-question path and the guard fix.

## Related Analysis

- [`harness-engineering.md`](harness-engineering.md) — the researched anchor: completion loops, self-verification, doom-loop detection, reasoning-effort allocation; this doc is its scheduling-facing companion.
- [`safety-and-sandboxing.md`](safety-and-sandboxing.md) — the blast-radius of unattended loops and the concrete controls (7-day expiry, kill-switch, no-permission-prompts on cloud Routines, vault-isolated credentials).
- [`orchestration-comparison.md`](orchestration-comparison.md) — dynamic workflows, background sessions, agent teams, Routines as an orchestration layer.
- [`model-migration-anti-patterns.md`](model-migration-anti-patterns.md) — model-currency context for the harness the loop runs.

## Sources

### Tier A (Primary / Vendor)

- Anthropic Claude Code docs: ["Run prompts on a schedule"](https://code.claude.com/docs/en/scheduled-tasks) — `/loop` interval/self-paced, `.claude/loop.md`, 7-day expiry, `CLAUDE_CODE_DISABLE_CRON`, the three-way Cloud/Desktop/loop comparison, `CronCreate`/`CronList`/`CronDelete`, requires v2.1.72+.
- Anthropic [Claude Code changelog](https://code.claude.com/docs/en/changelog) — `/goal` v2.1.139 (2026-05-11); `/loop` fixes v2.1.140/147; `Stop`/`SubagentStop` hook inputs gain `background_tasks` and `session_crons` (v2.1.152); subagents spawn subagents up to 5 levels deep (v2.1.172, 2026-06-10).
- Anthropic Claude Code docs: ["Orchestrate subagents at scale with dynamic workflows"](https://code.claude.com/docs/en/workflows) — `.claude/workflows/` save location, `disableWorkflows`/`CLAUDE_CODE_DISABLE_WORKFLOWS`, concurrency and total-agent caps per run, `ultracode` trigger.
- Anthropic Engineering: ["Effective context engineering for AI agents"](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (2025-09-29) — the official prompt→context progression and the "LLMs autonomously using tools in a loop" agent definition; does not use the term "loop engineering."
- Anthropic Claude Code: official Ralph Wiggum plugin (`anthropics/claude-code`) — continuous loop via a `Stop` hook; credits Huntley; state persists across iterations via files/git.
- Boris Cherny (Claude Code creator) — WorkOS *Acquired Unplugged* event, 2026-06-02 (YouTube `RkQQ7WEor7w`): "My job is to write loops." Short quote host-anchored via Michael Grinich (WorkOS) LinkedIn (Tier A-minus); fuller passage corroborated across multiple independent published accounts — The New Stack ("loop engineering"), note.com near-verbatim share (2026-06-09), Njuguna and Flor (Medium, both 2026-06-08) — all converging on the same wording. Video-derived; no published account gives a timestamp, so cite the passage without one.

### Tier B (Validated / Expert Practitioner)

- Andrej Karpathy — ["Sequoia Ascent 2026"](https://karpathy.bearblog.dev/sequoia-ascent-2026/) (2026-04-30): coding's built-in verification makes it the ideal self-improvement loop; the human stays responsible for the software. AutoResearch as a concrete overnight self-improving loop (his own demo figures, not independently reproduced).
- Geoffrey Huntley — ["Ralph Wiggum as a software engineer"](https://ghuntley.com/ralph/) (2025-07): origin of the fixed-prompt `while`-loop technique the productized commands descend from.

### Tier C (Community — bias-flagged)

- The New Stack, "Loop engineering" (2026-06): establishes the term in connection with Cherny and credits Addy Osmani with naming it. Industry journalism.
- Addy Osmani, "Loop Engineering" (2026-06-07): the loop "building blocks" decomposition; conceptual, no production metrics.
- Filip Verloy (Rubrik), "From Prompt Engineering to Loop Engineering" (2026-06-07): security framing — agentic overreach, infinite hallucination loops, prompt injection at machine speed. Vendor-adjacent; flag bias.
- Data Science Dojo, MindStudio, Louis Bouchard (2026-06): explainer-tier coverage; useful for the ReAct/Reflexion/Plan-and-Execute lineage, thin on primary sourcing.

---

*Last updated: 2026-06-19 (#73 carry-forwards fully applied — `harness-goal-completion-loop` graduated to an anchored, triggering predicate after an 80%→0% false-positive measurement; `harness-scheduled-agent` graduated, its `~/.claude/scheduled-tasks/<name>/SKILL.md` path/leaf docs-confirmed; `CronList` confirmed not to enumerate cloud Routines; Cherny "write loops" quote re-cited to multiple published accounts; Tier-D runaway-cost estimate added, gap kept open). Prior: 2026-06-15 (new EMERGING doc — unattended-execution primitives and the loop-engineering framing).*

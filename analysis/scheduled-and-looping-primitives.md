---
evidence-tier: Mixed
applies-to-signals: [harness-loop-config, harness-scheduled-agent, ci-scheduled-agent, harness-background-tasks, harness-goal-completion-loop]
last-verified: 2026-07-16
revalidate-by: 2026-09-21
status: EMERGING
follows: "Osmani 'Loop Engineering' (addyosmani.com, 2026-06-07 — five-component anatomy; per the 2026-07-12 re-attribution he presents the framing as his own and quotes Steinberger for one line) + Ronacher 'The Coming Loop' (lucumr.pocoo.org, 2026-06-23) + Ng three-loop model (The Batch, 2026-06-30) (Tier B/C commentary canons, verified 2026-07-16) — the loop-engineering commentary layer; the primitive inventory itself is already first-party (collapsed 2026-07-10). Bar status: fails Supported (blog-form canons). Delta kept here: the audit-signal routing table, the failure framing (cost runaway, premature done, weak-RETHINK limb), and the loop-engineering provenance ledger. Advance trigger: first-party docs absorbing the failure-mode framing, or a Supported loop-engineering guide."
convergence: converged
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

> **Collapsed 2026-07-10 (Reduction Phase 4).** The primitive inventory is now first-party (official scheduled-tasks, /goal, and workflows docs; Routines GA v2.1.198). Kept delta: the audit-signal → routing table the fleet audit renders from, the unattended-execution failure framing (cost runaway, premature "done", self-verification gaps), the weak-RETHINK-limb analysis, and the loop-engineering provenance.

**Evidence Tier**: Mixed (A-B-C) — official Claude Code docs/changelog plus the Cherny quote (Tier A, per this repo's Claude-Code-creator rule), named-practitioner analysis (Tier B: Huntley, Karpathy), a single-practitioner case study (Tier B, single-source flagged — `project1`'s loop design + loop-state machines), and the June-2026 "loop engineering" commentary cloud (Tier C, bias-flagged).

> **Following the Osmani/Ronacher/Ng loop-commentary canons since 2026-07-16.** New coverage effort on loop-engineering commentary goes to tracking those canons, not growing this doc. Delta kept: the audit-signal routing table + failure framing + provenance ledger.

## Purpose

This doc covers the operational risk of running Claude Code **unattended, recurring, or until-done**, and the audit signals that detect it. The primitives (`/loop`, `/goal`, cloud Routines, Desktop scheduled tasks, dynamic workflows, the Ralph-style continuous loop) are documented first-party now ([scheduled-tasks](https://code.claude.com/docs/en/scheduled-tasks), [changelog](https://code.claude.com/docs/en/changelog), [workflows](https://code.claude.com/docs/en/workflows)). The researched anchor for in-run mechanics stays [`harness-engineering.md`](harness-engineering.md); this doc is its scheduling-facing companion. Status **EMERGING**: documented (Tier A), but the "loop engineering" framing remains secondary-sourced, so the analytical claims here are held lightly.

**Why unattended execution is a distinct failure surface**: the primitives differ from an interactive session on where the loop lives and who, if anyone, is watching. Cloud Routines run with no permission prompts; Desktop tasks start against the working directory, including uncommitted changes, firing a catch-up run on wake — a 9 a.m. task can run at 11 p.m. against stale state. That autonomy resolves into three failure modes: cost runaway (nothing bounds spend on an unwatched loop), premature "done" (`/goal` stops when its completion check is satisfied, not necessarily when the objective is met), and self-verification gaps (a loop grading its own work has no outside check). The Audit Signals table catches that one of these is running; the RETHINK section covers what closes the loop once caught.

---

## "Loop engineering": the orchestration face of harness engineering

In June 2026 a label — *loop engineering* — attached itself to a practice the repo already analyzes under [harness engineering](harness-engineering.md). The provenance is thinner than its volume suggests:

- The **practice** comes from Boris Cherny (Claude Code creator) at WorkOS's *Acquired Unplugged* event, 2026-06-02 (YouTube `RkQQ7WEor7w`): "My job is to write loops," host-anchored via Michael Grinich (WorkOS) LinkedIn (Tier A-minus); a fuller passage is corroborated across independent accounts (The New Stack, a note.com share 2026-06-09, Medium's Njuguna and Flor both 2026-06-08), video-derived with no published timestamp.
- The **term** was coined by Addy Osmani (Google), not Cherny — The New Stack credits Osmani; some aggregators wrongly attribute Osmani's "building blocks of a loop" enumeration to Cherny.
- Anthropic's own published progression stops at *prompt engineering → context engineering* ([Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), 2025-09-29); the third rung is supplied by commentators. This repo names it *harness engineering*, backed by research the loop-engineering cloud lacks ([Meta-Harness arXiv:2603.28052](https://arxiv.org/abs/2603.28052), [NLH arXiv:2603.25723](https://arxiv.org/abs/2603.25723)).

So "loop engineering" is the orchestration/iteration-cadence face of harness engineering, not a separate discipline. Karpathy's steelman: coding is the ideal self-improvement loop because it has built-in verification — "tests pass or fail, programs run or crash, diffs can be inspected" (Tier B — [Sequoia Ascent 2026](https://karpathy.bearblog.dev/sequoia-ascent-2026/), 2026-04-30) — making the unattended primitives safe to leave running, and why the design question is never "loop or not" but "what closes the loop, and what bounds it."

The Ralph lineage is the concrete antecedent: Geoffrey Huntley's "Ralph Wiggum" technique (Tier B — [ghuntley.com/ralph](https://ghuntley.com/ralph/), 2025-07) — a `while` loop feeding a fixed prompt each iteration, state surviving through the codebase, a TODO/plan file, and per-iteration git commits. Anthropic's official plugin (a `Stop` hook re-feeding the prompt) credits Huntley; state persists **across** iterations via files/git — fresh-context-per-iteration is a design choice, not the default.

---

## The weak RETHINK limb: where loop setups fail silently

Detecting that a project loops says nothing about *what closes the loop* — that's where the operational failure lives. The Cherny/Osmani lineage decomposes a working loop into stages (GENERATE → SELECT → EVALUATE → ACCUMULATE → PUBLISH → RETHINK), and most looping setups an audit encounters have a strong Act limb and a weak or absent RETHINK limb — the step that re-derives the question before the next iteration. A strong Act limb paired with a stale RETHINK limb produces confident motion toward the wrong target: Boyd's OODA reading applied to an agent loop, Act getting faster while Orient gets skipped. Karpathy's verification point above only keeps the Act limb *honest*; it never answers whether the thing being verified is still worth building.

The clearest worked example (Tier B, single-source flagged): `project1`'s [loop-engineering design](../../project1/02-projects/securitydataworks/LOOP-ENGINEERING-DESIGN-2026-06-15.md) scored its own loop stage-by-stage — GENERATE and EVALUATE (ground-truth benchmarks, not self-grading) strong, SELECT/ACCUMULATE/PUBLISH/RETHINK all leaked, RETHINK worst since "are these the right questions?" was answered only by one-shot human audits. Its summary travels beyond the one project: *the inner loop is a tight, gated, oracle-grounded controller; the outer loop is the human.* Two named gaps: **G1**, no loop-start cognition-store query; **G4**, no standing question-quality/drift instrument, so the human *is* the instrument — goal-drift is emergent with no error code (Arike et al., AIES 2025). The fix: two loop-state machines, [`BENCH-LOOP-STATE.md`](../../project1/02-projects/securitydataworks/BENCH-LOOP-STATE.md) and [`CONSOLE-LOOP-STATE.md`](../../project1/02-projects/securitydataworks/CONSOLE-LOOP-STATE.md), each opening every iteration with a step-0 ORIENT (restate the objective, check for drift), composed from existing instruments rather than an autonomous question-generator.

**When an audit fires an unattended-execution signal with no standing RETHINK/Orient instrument**: advise a loop-start Orient step, a question-quality instrument on a cadence kept separate from throughput dashboards, and treating any objective change as human-ratified, never auto-applied — soft and advisory, since no filesystem predicate exists for "this loop re-derives its own question." [`intent-alignment-audit.md`](intent-alignment-audit.md) is the forthcoming general RETHINK companion.

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

## Gaps & Counter-Evidence

What this doc does *not* establish, and what's still open:

- **Delegation is still narrow.** Anthropic's 2026 Agentic Coding Trends Report (Tier A): AI used in ~60% of work but *fully delegated* only 0–20% — "I just write loops" is a leading-practitioner posture, not the median.
- **The term is press-coined and recent.** Strip the Tier C commentary cloud (The New Stack, MindStudio, Data Science Dojo, Louis Bouchard, Verloy/Rubrik) and it reduces to one Cherny quote plus the productized commands — a named, attributed workflow, not a paradigm.
- **Runaway-loop economics.** No published $/hour or token-burn figure exists for an unattended `/loop` or cloud Routine. Tier-D triangulation (2026-06-19) — Managed Agents ~$0.08/hr, harness-design's ~$200/6hr, the safety doc's ~60K tokens/9 days idle — spans ~3 orders of magnitude by *activity rate*: an active Opus loop at ~$33/hr runs ~$800/day, ~$5.6K/7 days. The control that matters is a token/$ ceiling, not a time bound. **Needs**: a measured $/hr from a bounded `/loop`.
- **Detection reliability (closed 2026-06-19).** The `harness-goal-completion-loop` false-positive fix is in the Audit Signals table above (80%→0%, tested 2026-06-16). Also confirmed: `harness-scheduled-agent`'s `~/.claude/scheduled-tasks/<name>/SKILL.md` path is correct per the official docs. Open thread: a *durable* `/loop` cron persists separately to `.claude/scheduled_tasks.json`, uncaught by any current signal.
- **Absent RETHINK limb (soft signal only).** No filesystem predicate exists for "this loop re-derives its own question" — the recommendation above is a soft, advisory inference (loop signal + no Orient artifact). Evidence is single-practitioner (`project1`), so the prevalence claim is illustrative, not measured. **Needs**: a consistent heuristic and a second independent project.
- **Cloud-Routine visibility (structurally partial).** A pure-cloud Routine leaves no repo/host artifact and no on-disk footprint; `cron-disabled` gives false reassurance (a local env var doesn't touch a server-side Routine). Fix: make "ask the operator to list cloud Routines" a **required output line** — `CronList` confirmed not to enumerate them (verified 2026-06-16); `cron-disabled` suppresses local rows only. **Needs**: a testbed Routine.

## Related Analysis

- [`harness-engineering.md`](harness-engineering.md) — completion loops, self-verification, doom-loop detection, reasoning-effort allocation; this doc's scheduling-facing companion.
- [`intent-alignment-audit.md`](intent-alignment-audit.md) — forthcoming RETHINK companion: "does each mechanism still match its intent?"
- [`safety-and-sandboxing.md`](safety-and-sandboxing.md) — blast-radius controls (7-day expiry, kill-switch, no-permission-prompts, vault-isolated credentials).
- [`orchestration-comparison.md`](orchestration-comparison.md) — dynamic workflows, background sessions, agent teams, Routines as orchestration.
- [`model-migration-anti-patterns.md`](model-migration-anti-patterns.md) — model-currency context for the harness the loop runs.

## Sources

### Tier A (Primary / Vendor)

- Anthropic Claude Code docs: ["Run prompts on a schedule"](https://code.claude.com/docs/en/scheduled-tasks) (`/loop`, Desktop tasks, cloud Routines; v2.1.72+) and ["Orchestrate subagents with dynamic workflows"](https://code.claude.com/docs/en/workflows) (`.claude/workflows/`).
- Anthropic [Claude Code changelog](https://code.claude.com/docs/en/changelog) — `/goal` shipped v2.1.139 (2026-05-11).
- Anthropic Engineering: ["Effective context engineering for AI agents"](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (2025-09-29) — official prompt→context progression, doesn't use "loop engineering"; and the official Ralph Wiggum plugin (`anthropics/claude-code`) — `Stop`-hook loop, credits Huntley, state persists via files/git.
- Boris Cherny (Claude Code creator) — WorkOS *Acquired Unplugged*, 2026-06-02 (YouTube `RkQQ7WEor7w`): "My job is to write loops," host-anchored via Michael Grinich (WorkOS) LinkedIn (Tier A-minus); corroborated across The New Stack, note.com (2026-06-09), and Njuguna/Flor on Medium (both 2026-06-08). Video-derived, no timestamp given.

### Tier B (Validated / Expert Practitioner)

- Andrej Karpathy — ["Sequoia Ascent 2026"](https://karpathy.bearblog.dev/sequoia-ascent-2026/) (2026-04-30): coding's built-in verification makes it the ideal self-improvement loop.
- Geoffrey Huntley — ["Ralph Wiggum as a software engineer"](https://ghuntley.com/ralph/) (2025-07): origin of the fixed-prompt `while`-loop technique the productized commands descend from.
- Armin Ronacher — "The Coming Loop" (lucumr.pocoo.org, 2026-06-23): a second independent loop-engineering commentary voice outside the Cherny/Osmani line, corroborating the failure-mode framing (cost runaway, verification) this doc carries as delta.

### Tier B (Single-practitioner case study — flagged)

- `project1`: ["SDW Loop Engineering"](../../project1/02-projects/securitydataworks/LOOP-ENGINEERING-DESIGN-2026-06-15.md) (2026-06-15, self-scored GENERATE→RETHINK loop, gaps G1–G4, detailed in-body) and its two operationalized loop-state machines, [`BENCH-LOOP-STATE.md`](../../project1/02-projects/securitydataworks/BENCH-LOOP-STATE.md) / [`CONSOLE-LOOP-STATE.md`](../../project1/02-projects/securitydataworks/CONSOLE-LOOP-STATE.md) (2026-06-17/20). **Single-source — one practitioner's own project, illustrative pattern, bias-flagged.**

### Tier C (Community — bias-flagged)

- The New Stack, "Loop engineering" (2026-06), and Addy Osmani, "Loop Engineering" (2026-06-07): establish/name the term and the "building blocks" decomposition; conceptual, no production metrics.
- Filip Verloy (Rubrik), "From Prompt Engineering to Loop Engineering" (2026-06-07): security framing — agentic overreach, prompt injection at machine speed; vendor-adjacent, flag bias.
- Data Science Dojo, MindStudio, Louis Bouchard (2026-06): explainer-tier coverage, thin on primary sourcing.
- Andrew Ng — three-loop model, *The Batch* newsletter (2026-06-30): a third independent loop-engineering commentary voice; explainer-tier, no production metrics.

---

*Last updated: 2026-07-16 (follow-lane wiring — `follows:` frontmatter + body banner for the Osmani/Ronacher/Ng loop-commentary canons; Ronacher and Ng added to Sources; promotion check re-run, status held EMERGING). Prior: 2026-07-10 (Reduction Phase 4 — see banner; 33KB → 17KB). Prior: 2026-06-21 (added "The weak RETHINK limb" section — strong-Act/weak-RETHINK case study + advisory recommendation). Prior: 2026-06-19 (`harness-goal-completion-loop` graduated via the 80%→0% false-positive measurement; `harness-scheduled-agent` graduated; Tier-D cost estimate added). Prior: 2026-06-15 (new EMERGING doc).*

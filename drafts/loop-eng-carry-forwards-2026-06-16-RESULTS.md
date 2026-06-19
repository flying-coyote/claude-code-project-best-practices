# Loop-eng carry-forwards — results (2026-06-16)

Status: **APPLIED 2026-06-19.** CF2a (anchored `/goal` regex → graduated to triggering), CF3 (`CronList`
confirmed-no cloud caveat), and F (Tier-D runaway-cost estimate) folded into the live docs
(`AUDIT-CONTEXT.md`, `analysis/scheduled-and-looping-primitives.md`) on branch
`loop-engineering-unattended-execution-20260615`. Follow-up **A** (Fable/Mythos-suspended model note) was
already applied 2026-06-15 (`model-migration-anti-patterns.md` currency note + `AUDIT-CONTEXT.md` row); **D**
(workflow caps) needed no edit (the wrong values were never committed). **CF1/B and CF2b — RESOLVED 2026-06-19
via research** (the owner pointed at the now-published articles instead of the video): CF1's fuller passage is
corroborated across multiple independent published accounts (The New Stack, note.com near-verbatim share, Njuguna,
Flor — all 2026-06), so the "needs a human to transcribe the recording" hedge is retired (still video-derived, no
published timestamp); CF2b's `~/.claude/scheduled-tasks/<kebab-case-name>/SKILL.md` path/leaf is confirmed straight
from the official Desktop scheduled-tasks docs (YAML frontmatter `name`/`description` + prompt body), so the
`-name SKILL.md` predicate graduates. Bonus finding: a *durable* `/loop` cron persists to project-local
`.claude/scheduled_tasks.json` — a separate artifact no current signal catches.

---

## CF2a — `/goal` false-positive rate: MEASURED ✅ (ready to apply)

Ran the drafted test in a throwaway dir against a realistic 5-line transcript JSONL (1 true `/goal`
command at a user turn head + 4 false-positive contexts: a `src/goal/` path, "the /goal of this
project", a `https://example.com/goal/docs` URL, and "what is the /goal here?").

- **Bare `grep "/goal"` (the current `harness-goal-completion-loop` signal): 5/5 hits → 80% false-positive rate.** Every false-positive context tripped it.
- **Anchored to the command token at a user turn head: 1/1 hit, 0 false positives.** Working regex:
  `grep -E '"role":"user","content":\[\{"type":"text","text":"/goal( |")'`
  (i.e. `/goal` only when it is the head of a user message's text, followed by a space or the closing quote).

**Verdict:** the gap finding is confirmed empirically — the bare grep is unusable as a trigger (80% FP).
The anchored form isolates the true command. **Proposed edit** to `scheduled-and-looping-primitives.md`:
graduate `harness-goal-completion-loop` from "informing, not triggering" to **triggering with the
anchored regex above**, and replace the line-107 gap note's "(a) … false-positives on `src/goal/`…
anchor it to the command token at a turn head" with the measured result (80% FP on bare grep → 0 with
the turn-head anchor, tested 2026-06-16). Detection tier stays A (it's a grep precision fix, now testbed-validated).

## CF3 — does `CronList` enumerate cloud Routines? CONFIRMED: no ✅ (ready to apply)

Called the harness `CronList` tool directly: it returned "No scheduled jobs" and its contract is
"list all cron jobs scheduled **via CronCreate in this session**." So `CronList` surfaces only
session-created `CronCreate` jobs — it does **not** enumerate host-level cron, Desktop scheduled tasks,
or cloud Routines.

**Verdict:** `CronList` does **not** close the cloud-Routine blind spot. **Proposed edit** to the
line-102 caveat ("A pure-cloud Routine may leave no on-disk footprint"): add that *even the in-session
`CronList` tool does not enumerate cloud Routines* (it lists only `CronCreate` session jobs), so a
repo-local audit **and** a tool-assisted one both miss pure-cloud Routines — the audit must say so, not
imply coverage.

## CF2b — scheduled-task artifact path/leaf: RESOLVED 2026-06-19 (docs-confirmed) ✅

No `~/.claude/scheduled-tasks/` directory exists on this machine (no scheduled task has been created
here), so there is no live artifact to confirm the `<name>/SKILL.md` leaf against. The path rests on
the official docs (Tier A, line 43). **To truly confirm:** create one Desktop scheduled task and inspect
the on-disk artifact path + leaf filename. Until then, leave `harness-scheduled-agent`'s `-name SKILL.md`
predicate as doc-derived (don't graduate it on the strength of a testbed it hasn't actually seen).

## CF1 — Cherny "write loops" quote: RESOLVED 2026-06-19 (now-published accounts) ✅

The verbatim quote + timestamp from Boris Cherny's WorkOS *Acquired Unplugged* recording (2026-06-02)
is still resting on secondaries. `WebFetch` on the YouTube URL returns only page chrome (nav/footer),
no transcript text — YouTube transcripts aren't web-fetchable as text autonomously. **Action (you):**
open the recording, pull the verbatim "my job is to write loops" line + its timestamp, and replace the
secondary-sourced paraphrase in `DECISIONS.md` L635 / the citation with the primary quote.

## F — runaway-loop $/hr datapoint: CANNOT MEASURE autonomously; triangulated estimate (Tier D) ⚠️

I can't run a 7-day unbounded billed `/loop` and measure it. What I can do is make the blast-radius
argument quantitative from the doc's **own existing anchors**, clearly labeled as an estimate, not a
measurement:

- Active-agent rate anchor: the harness-design post's **~$200 / 6 hr ≈ ~$33/hr**.
- Infra floor: Managed Agents **$0.08 / session-hour** (infra only, not tokens).
- Near-idle case: the safety doc's **"60K+ tokens in 9 days"** inter-agent reply loop ≈ a few dollars total.

So an unbounded loop's 7-day cost spans **~3 orders of magnitude by activity rate**: a throttled/idle
loop is negligible (single-digit dollars), while an *active* Opus loop at the ~$33/hr anchor is **~$800/day
→ ~$5.6K over 7 days**. **The finding (Tier D, arithmetic on existing anchors): blast radius is dominated
by the loop's activity rate, not its duration** — which argues the control that matters is a **token/$
budget ceiling**, not just a time bound. The gap stays **open** for a real measured datapoint (run a
bounded `/loop` with cost telemetry on, capture actual $/hr, upgrade this to Tier B).

---

### Apply checklist
- [x] CF2a: graduated `harness-goal-completion-loop` to the anchored regex (AUDIT-CONTEXT Signal Collection + row, scheduled-and-looping-primitives signal table + gap note) — measured, applied 2026-06-19.
- [x] CF3: extended the cloud caveat + cloud-Routine gap to record `CronList`'s blind spot (confirmed-no) — applied 2026-06-19.
- [x] F: added the Tier-D triangulated estimate to the runaway-loop-economics gap; gap stays open for a measured run — applied 2026-06-19.
- [x] CF2b: `harness-scheduled-agent` graduated — `~/.claude/scheduled-tasks/<kebab-case-name>/SKILL.md` (YAML frontmatter `name`/`description` + prompt body) confirmed from the official Desktop scheduled-tasks docs 2026-06-19; noted the durable-`/loop` `.claude/scheduled_tasks.json` artifact as a separate uncaught gap.
- [x] CF1: fuller passage cited to the now-published accounts (The New Stack, note.com, Njuguna, Flor — all 2026-06); "needs human transcription" hedge retired across the docs + SOURCES; no published timestamp, so none asserted.

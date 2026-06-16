---
status: APPLIED 2026-06-16 (B/C/E folded into the live docs on branch loop-engineering-unattended-execution-20260615; D verified — no wrong cap values were ever committed, so no doc edit needed; the verified caps + retrieval date are recorded in this draft for citation). Kept as the research record + carry-forward (B primary transcript still NOT-FOUND; C test plan still to RUN; E CronList cloud-coverage still to verify).
drafted: 2026-06-16
author-note: Drafted per the PLAN.md "Next Review" carry-forward (loop-engineering follow-ups B/C/D/E). Owner-gated repo — this file is a staging draft only. Do NOT commit, do NOT edit any existing doc from this; fold the confirmed pieces in by hand during the next review pass.
applies-to-docs: [analysis/scheduled-and-looping-primitives.md, analysis/harness-engineering.md, analysis/safety-and-sandboxing.md, AUDIT-CONTEXT.md, analysis/orchestration-comparison.md]
applies-to-signals: [harness-goal-completion-loop, harness-scheduled-agent, harness-dynamic-workflows]
discipline: Anthropic primary docs = Tier A; verify-before-rejecting on harness facts that may post-date training; volatile/version-sensitive facts flagged; attribution Osmani=term-coiner / Cherny=practice-source.
---

# Loop-Engineering Follow-ups B / C / D / E (DRAFT)

Four staged follow-ups from the 2026-06-15 loop-engineering pass, drafted 2026-06-16. Each is a self-contained section ready for review; nothing here is wired into routing yet, and no existing file has been modified. The two web-research items (B, D) carry an explicit confidence and a primary/secondary status; the two analytical items (C, E) are test/analysis designs, not executed runs.

Confidence at a glance:

| Item | What | Status | Confidence |
|---|---|---|---|
| B | Cherny WorkOS quote — primary transcription | PARTIAL — short quote host-anchored; full passage secondary-converged; **verbatim-with-timestamp primary NOT-FOUND** | Medium on wording, low on the "verbatim + timestamp" bar the review asked for |
| C | Test plan for `harness-goal-completion-loop` + `harness-scheduled-agent` | DRAFT test plan — not run | High that the plan is executable; the signals stay UNVALIDATED until it runs |
| D | Dynamic-workflow caps re-confirm vs official docs | CONFIRMED from `code.claude.com/docs/en/workflows` (retrieved 2026-06-16) | High on the two stated caps; one of the three proposed values is **wrong as written** and one is **NOT-FOUND** |
| E | Cloud "Routine" detection blind spot | DRAFT analysis | Medium — mechanism is clear; the closing check is a proposal, not yet tested |

---

## B — Boris Cherny WorkOS quote: primary transcription attempt

### What the review asked for

The quote currently in `scheduled-and-looping-primitives.md` (line 69 / 126) and `harness-engineering.md` rests on secondaries: "My job is to write loops" plus the "I don't prompt Claude anymore / I have loops that are running" framing, attributed to Boris Cherny at the WorkOS-hosted *Acquired Unplugged* event, 2026-06-02. The task: fetch the primary — YouTube video id `RkQQ7WEor7w` — and pull the exact wording in context, with a timestamp.

### What I could and could not get

The video is real and correctly identified: **"Boris Cherny: Claude Code & the Future of Engineering | Acquired Unplugged presented by WorkOS"** (YouTube `RkQQ7WEor7w`). Cherny is interviewed by Ben Gilbert and David Rosenthal of the *Acquired* podcast. The event date (2026-06-02) is corroborated by WorkOS's own announcement and Cherny's own post-event tweet (`x.com/bcherny/status/2044632185354006713`, "Thanks @AcquiredFM for hosting me on Unplugged").

**The YouTube transcript / captions were NOT directly obtainable.** WebFetch on the watch URL returned only page chrome (footer, legal nav) — YouTube serves captions through a separate timed-text endpoint that this tooling can't reach, and the auto-caption track is not in the fetched HTML. So the *verbatim-from-the-primary, with-timestamp* bar the review set is **NOT-FOUND**. I am flagging that explicitly per the hard constraint: I did not get the primary transcript, and I will not invent a timestamp.

### What the evidence does support

Two things are well-supported short of the full primary:

1. **The short quote is host-anchored.** Michael Grinich (WorkOS founder/CEO, the event host) posted "My job is to write loops." —Boris Cherny, creator of Claude Code at Anthropic, from Acquired Unplugged" on LinkedIn (`linkedin.com/posts/grinich_...activity-7456044631273934848`), presenting it as a direct quote pulled from the event he hosted. Host-of-the-event attribution of a four-word quote is about as close to primary as a secondary gets; treat it as Tier A-minus (named host, dated event, presented as quotation, but not the recording itself).

2. **The fuller passage is consistent across independent secondaries, verbatim-styled but un-timestamped.** Two secondaries render the same expanded passage word-for-word inside quotation marks:

   > "Now it's actually leveled up, I think, again, to the next wave of abstraction where I don't prompt Claude anymore. I have loops that are running. They're the ones that are prompting Claude and figuring out what to do. My job is to write loops."

   — rendered identically by Ezekiel Njuguna (Medium, *The Prediction Market Intelligence*, 2026-06-08) and by Guillermo Flor (productmarketfit.tech, 2026-06-08, who lightly compresses it: "I have loops running. They're the ones prompting Claude…"). Neither cites a timestamp; both attribute it to the WorkOS/Acquired conversation.

3. **A caution worth keeping.** WorkOS's *own* writeup of the event ("Key takeaways from Boris Cherny on building Claude Code," workos.com/blog, 2026-06-02) does **not** quote the loop material verbatim — it paraphrases it ("Now he doesn't even prompt Claude directly. He writes loops…") and reserves quotation marks for a different line ("Right now, this is just the golden age of the generalist…"). So the host organization's prose treats the loop framing as paraphrase even while its CEO quotes the punchline directly. That split is the reason this stays short of "confirmed verbatim": the wording is convergent and plausible, but the one source positioned to publish the transcript chose to paraphrase the surrounding sentences.

### Drafted corrected version (to replace the current secondary-only citation)

Proposed replacement for the bullet in `scheduled-and-looping-primitives.md` "loop engineering" section and the matching Sources entry. It upgrades the *short* quote to a host-anchored citation, keeps the *fuller* passage explicitly flagged as secondary-rendered, and records the failed primary attempt so the next reviewer doesn't redo it:

> - The **practice** comes from Boris Cherny (Claude Code creator), at the WorkOS-hosted *Acquired Unplugged* event on 2026-06-02 (video: YouTube `RkQQ7WEor7w`). The four-word quote "My job is to write loops" is attributed directly by the event's host, Michael Grinich (WorkOS), in his own LinkedIn writeup (Tier A-minus — named host of the dated event, presented as quotation). The fuller passage commonly cited — "…I don't prompt Claude anymore. I have loops that are running. They're the ones that are prompting Claude and figuring out what to do. My job is to write loops." — is rendered identically across independent secondaries (Njuguna, Medium 2026-06-08; Flor, productmarketfit.tech 2026-06-08) but is **not yet confirmed against the recording**: the YouTube caption track was not machine-retrievable on 2026-06-16, and WorkOS's own event writeup paraphrases rather than quotes these sentences. Cite the short quote as host-attributed; cite the fuller passage as secondary-converged-pending-recording. Do not attach a timestamp until someone transcribes the recording.

**Recommendation:** keep the carry-forward open. Closing it to a true primary needs a human to scrub the video's caption track / transcript (or watch it) and capture the timestamp. The wording above is safe to ship now because it does not overclaim — it separates the host-anchored four words from the secondary-rendered full passage.

**Sources (B):**
- Boris Cherny, *Acquired Unplugged presented by WorkOS*, YouTube `RkQQ7WEor7w` (event 2026-06-02). PRIMARY — transcript/timestamp NOT-FOUND via available tooling on 2026-06-16.
- Michael Grinich (WorkOS, event host), LinkedIn post `activity-7456044631273934848`, "My job is to write loops." —Boris Cherny. Host-anchored quotation.
- WorkOS blog, "Key takeaways from Boris Cherny on building Claude Code" (2026-06-02) — paraphrases the loop material; direct-quotes only the "golden age of the generalist" line.
- Ezekiel Njuguna, Medium / *The Prediction Market Intelligence*, "What a Loop Actually Is: Boris Cherny's Three-Stage Definition" (2026-06-08) — renders the full passage verbatim-styled, no timestamp.
- Guillermo Flor, productmarketfit.tech, "Stop Prompting AI and Start Building Loops" (2026-06-08) — renders a compressed version, no timestamp.
- Boris Cherny, X/Twitter `status/2044632185354006713` — confirms he attended the event.

---

## C — Empirical test plan for `harness-goal-completion-loop` and `harness-scheduled-agent`

Both signals are currently in `AUDIT-CONTEXT.md` (rows 129 and 133) and `scheduled-and-looping-primitives.md` (Audit Signals table) as **theory-detectable, UNVALIDATED** — the "Gap: detection reliability" in the EMERGING doc names exactly this. This is a concrete plan to elicit each one against a real testbed and measure false-negative / false-positive behavior. **Draft only — do not run it as part of this task.** The plan is written so a future session (or the owner) can execute it verbatim and then graduate or correct the signal.

### Shared method

For each signal: (1) define the observable artifact the signal's detection command predicts; (2) build the smallest real testbed that should *produce* that artifact; (3) run the exact detection command from `AUDIT-CONTEXT.md`'s Signal Collection block; (4) score against a pass/fail criterion; (5) run a deliberate false-positive probe and a deliberate false-negative probe to bound reliability. Record CLI version (`claude --version`) on every run — both signals are version-gated (scheduled tasks need v2.1.72+; `/goal` needs v2.1.139), and a miss on an old CLI is a version artifact, not a detection failure.

Isolation note (repo convention, `feedback_subagent_forbid_git` / `feedback_security_telemetry_injection_surface`): run the testbed in a throwaway directory and a throwaway `CLAUDE_CONFIG_DIR`, not against this repo or the real `~/.claude`. Two reasons — host-level signals read `~/.claude/scheduled-tasks/` and `~/.claude/projects/`, so a real run would write into the operator's actual home state; and transcripts can contain pasted content, so a synthetic, operator-authored testbed avoids piping anything untrusted into context.

### C.1 — `harness-scheduled-agent`

**Detection command (as shipped):** `find ~/.claude/scheduled-tasks -name SKILL.md` (AUDIT-CONTEXT Signal Collection line 47).

**Observable artifact the signal predicts:** a Desktop scheduled task materializes on disk as `~/.claude/scheduled-tasks/<name>/SKILL.md` (relocated under `CLAUDE_CONFIG_DIR` if set). The signal fires iff at least one such file exists.

**Minimal testbed to elicit it:**
1. Set `CLAUDE_CONFIG_DIR=$(mktemp -d)` so nothing touches the real home.
2. Confirm CLI ≥ v2.1.72 (`claude --version`); if below, the feature is absent and the test is N/A — record and stop.
3. Create one Desktop scheduled task by the documented path (the `/schedule` flow or the Desktop "scheduled tasks" UI per `code.claude.com/docs/en/scheduled-tasks`). Give it a trivial body ("echo a heartbeat line into ./heartbeat.log") and a daily cadence.
4. Do NOT wait for it to fire — the *config artifact* is what the signal reads, not a run.

**Pass/fail criterion:**
- PASS: `find "$CLAUDE_CONFIG_DIR/scheduled-tasks" -name SKILL.md` returns ≥1 path immediately after creation. (Also verify the shipped command finds it when the task is stored under the default `~/.claude/` — i.e., that the signal isn't silently dependent on `CLAUDE_CONFIG_DIR` being unset.)
- FAIL: the file exists but under a different name/path than `<name>/SKILL.md` (e.g., a manifest JSON, a flat file, or a different leaf filename) — meaning the `-name SKILL.md` predicate is too narrow. This is the single most likely real failure mode and the main thing to verify, because the `SKILL.md` leaf-name is an assumption carried from the skills convention, not independently confirmed for scheduled tasks.

**False-positive probe:** drop a hand-written `~/.claude/scheduled-tasks/decoy/SKILL.md` containing no real schedule. The signal will fire (it only checks file presence). Document that the signal detects *configuration intent*, not an *active* schedule — a stale or disabled task trips it. Cross-check: it should be suppressed when `CLAUDE_CODE_DISABLE_CRON=1` is set (the `cron-disabled` negative guard) — verify the guard actually suppresses it in the routing logic, since the guard is itself untested.

**False-negative probe:** create a task through every creation surface the docs list (Desktop UI vs `/schedule` vs any settings-file form) and confirm each lands at a path the `find` predicate catches. If any surface stores the task elsewhere (e.g., a single `scheduled-tasks.json` rather than per-task dirs), the signal has a false-negative class and the detection needs a second predicate.

**How to distinguish true signal from false positive:** a true positive is a `SKILL.md` (or whatever the real leaf is) that contains a parseable cron/cadence field and a task body; a false positive is a presence-only match with no schedule semantics. Add a confirmation step to the eventual signal: after the `find` hit, grep the file for a cadence/cron field before routing, so a decoy or a malformed remnant doesn't route the audit into loop-hardening advice.

### C.2 — `harness-goal-completion-loop`

**Detection command (as shipped):** `grep -rl "/goal" ~/.claude/projects/` (AUDIT-CONTEXT Signal Collection line 53), flagged "lower-reliability, transcript-derived."

**Observable artifact the signal predicts:** a session where `/goal` was invoked leaves the literal string `/goal` in that session's transcript JSON under `~/.claude/projects/<project-hash>/`. The signal fires iff the string appears in any transcript.

**Minimal testbed to elicit it:**
1. `CLAUDE_CONFIG_DIR=$(mktemp -d)`; confirm CLI ≥ v2.1.139.
2. Start a session in a throwaway repo and issue a real `/goal` with a trivially-satisfiable condition (e.g., "stop when a file named DONE exists" and have the first turn create it) so the loop terminates immediately and doesn't burn tokens.
3. Exit the session so the transcript is flushed to disk.

**Pass/fail criterion:**
- PASS: `grep -rl "/goal" "$CLAUDE_CONFIG_DIR/projects/"` returns the session transcript.
- FAIL: the transcript records the *effect* of `/goal` (a completion-condition field, a turn-loop marker) but not the literal slash-string — e.g., if the harness stores the parsed command rather than the raw input. This is plausible and is the key thing to verify; if the literal string isn't persisted, the grep is the wrong predicate and the signal should key on the structured field instead.

**False-positive probe (this is the big one for `/goal`):** the bare string `/goal` is dangerously generic. Seed a decoy transcript containing the path fragment `src/goal/` , a sentence "the /goal of this refactor," and a URL `example.com/goal`. Run the shipped `grep -rl "/goal"` and count how many decoys it flags. Expectation: several false positives, because `/goal` matches any occurrence of the substring. **Mitigation to draft into the signal:** anchor the match to a command invocation, e.g. a line/JSON-field where `/goal` is the user-input command token (start-of-input or the transcript's command field), not a free-text substring. Until that anchoring is added, the signal's precision is low and the "lower-reliability" label in AUDIT-CONTEXT is doing real work — the test will quantify just how low.

**False-negative probe:** issue `/goal` in a session, then check whether transcript retention/rotation or a privacy setting (e.g., a do-not-log mode) suppresses the transcript. If transcripts can be disabled, the signal has an unavoidable false-negative floor that should be stated, not hidden — consistent with the existing "host-level signals: treat absence as not-observed, never fail the audit on them" rule (AUDIT-CONTEXT line 75).

**How to distinguish true signal from false positive:** a true positive is `/goal` as the command token at the head of a user turn in a transcript whose surrounding structure shows a multi-turn run-until-condition; a false positive is `/goal` as a substring in code, prose, or a URL. The deciding test is the decoy count above — if the anchored predicate drops decoy hits to zero while keeping the real hit, the signal graduates from "lower-reliability" to "validated."

### C.3 — Joint exit criteria

The two signals graduate out of UNVALIDATED only when, for each: (a) the shipped detection command fires on the real artifact (no false-negative on the canonical creation path), (b) the documented false-positive probes are either suppressed by an added confirmation predicate or explicitly accepted-and-labeled, and (c) the version gate is recorded. Until then, leave both as-is in the docs and update the "Gap: detection reliability" entry with whatever the run finds. If `harness-goal-completion-loop` shows the predicted high false-positive rate, the honest move is to keep it but downgrade its routing weight (it should *inform*, not *trigger*, given a single noisy substring match).

---

## D — Dynamic-workflow concurrency / total caps: re-confirm vs official docs

**Source:** Anthropic Claude Code docs, "Orchestrate subagents at scale with dynamic workflows," `https://code.claude.com/docs/en/workflows`. **Retrieved: 2026-06-16.** The page's "Behavior and limits" table is the authoritative statement. Feature requires Claude Code v2.1.154+ (stated on the page).

The three values the review asked to confirm-or-correct, checked against the page verbatim:

| Value as proposed in the task | Official-doc wording (retrieved 2026-06-16) | Verdict |
|---|---|---|
| Concurrent-agent cap = `min(16, CPU cores − 2)` | "Up to 16 concurrent agents, **fewer on machines with limited CPU cores**" | **PARTIALLY CORRECT — the formula is NOT in the docs.** The docs state a ceiling of 16 and that it drops on low-core machines, but they do **not** state the `min(16, cores − 2)` arithmetic. The "− 2" and the exact `min()` form are NOT-FOUND in the official page. Quote the ceiling (16) and the qualitative "fewer on limited CPU cores"; do **not** assert the `cores − 2` formula as documented. |
| Lifetime total agent cap = 1000 | "**1,000 agents total per run** — Prevents runaway loops" | **CONFIRMED.** Note the scope: the docs say "per run," i.e., per workflow run, not a lifetime/account total. The earlier draft language ("lifetime total agent cap") is the wrong frame — it is a per-run ceiling. Correct the wording to "1,000 agents total **per run**." |
| Max items per single `parallel()` / `pipeline()` call = 4096 | No such number appears on the page | **NOT-FOUND.** The workflows page does not state any per-`parallel()`/per-`pipeline()` item cap, nor the figure 4096. The page describes the two caps above (16 concurrent / 1,000 per run) and explicitly frames *those* as the runaway-prevention limits. Do not assert 4096 from memory; either find it in another official page (the SDK/API reference, if a `parallel()`/`pipeline()` API is documented there) or mark it NOT-FOUND and drop the claim. |

### What the docs actually say about the caps (verbatim, for the record)

From the "Behavior and limits" table on `code.claude.com/docs/en/workflows` (retrieved 2026-06-16):

> | Up to 16 concurrent agents, fewer on machines with limited CPU cores | Bounds local resource use |
> | 1,000 agents total per run | Prevents runaway loops |

And from the "Cost" section, reinforcing the per-run framing: "The runtime's agent caps limit how many agents a single run can spawn, which bounds the cost of a runaway script."

### Corrected language to use in the repo

`orchestration-comparison.md` already hedges correctly ("the docs page carries the current caps; re-verify before quoting a specific number," line 266) and `scheduled-and-looping-primitives.md` says "concurrency- and total-agent-capped per run." Those are fine as-is. Where a *specific number* gets quoted, use:

> Dynamic workflows are capped at **up to 16 concurrent agents** (fewer on machines with limited CPU cores — the docs state the ceiling and the CPU-dependence but not a `cores − N` formula) and **1,000 agents total per run** (the docs' stated runaway-prevention ceiling). Source: `code.claude.com/docs/en/workflows`, "Behavior and limits," retrieved 2026-06-16; feature requires v2.1.154+.

**Two corrections the next edit must carry:**
1. Drop `min(16, CPU cores − 2)` as a *documented* formula. The "− 2" is NOT-FOUND; quote 16 + "fewer on limited cores."
2. Change "lifetime total agent cap" → "1,000 agents total **per run**." It is a per-run cap, not a lifetime/account cap.
3. The `parallel()`/`pipeline()` item cap of 4096 is **NOT-FOUND** on the workflows docs page — do not assert it. (Flagged for a separate check against the Agent SDK reference if that API surface is documented there; until then, drop the number.)

These are volatile, version-coupled facts (the page is tied to v2.1.154+ behavior and can change release-to-release) — keep the retrieval date attached and re-verify on the next cadence, consistent with the existing volatile-fact discipline in Decision 10.

**Sources (D):**
- Anthropic Claude Code docs, "Orchestrate subagents at scale with dynamic workflows," `https://code.claude.com/docs/en/workflows`, "Behavior and limits" + "Cost" sections. Retrieved 2026-06-16. Tier A.
- Corroborating secondary (not load-bearing, for the 1,000 figure only): MarkTechPost, "Anthropic Ships Claude Opus 4.8 Alongside Dynamic Workflows… Capped at 1,000 Subagents" (2026-05-28) — Tier C, agrees with the per-run 1,000 cap; does not mention 4096 or a `cores − 2` formula.

---

## E — Cloud "Routine" detection blind spot

### The problem, stated precisely

The existing docs already note the blind spot but do not close it. `safety-and-sandboxing.md` (line 76) says a pure-cloud Routine "is invisible to a repo-local audit." `scheduled-and-looping-primitives.md` lists "Gap: cloud-Routine visibility" and the Counter-Evidence bullet "A pure-cloud Routine may leave no on-disk footprint." So the gap is acknowledged; what's missing is the *analysis of exactly where the blind spot is* and *the specific check that would narrow it*. This is that analysis.

### What a scheduled cloud Routine looks like to the existing detection signals

The unattended-execution signal cluster keys entirely on **repo-local or host-local on-disk artifacts**:

| Signal | Reads | Does a cloud Routine produce this artifact? |
|---|---|---|
| `harness-loop-config` | `.claude/loop.md`, `~/.claude/loop.md` | No — `/loop` is in-session, unrelated to cloud Routines. |
| `harness-scheduled-agent` | `~/.claude/scheduled-tasks/<name>/SKILL.md` | No — that path is the **Desktop** scheduled-task store; a cloud Routine runs on Anthropic infrastructure and need not write there. |
| `ci-scheduled-agent` | `.github/workflows` cron + claude invocation | Only if the Routine is *implemented as* a GitHub Action — a different mechanism. A native cloud Routine isn't a CI workflow. |
| `harness-background-tasks` | `.claude/worktrees/`, `bgIsolation` | No — those are local background-session artifacts. |
| `harness-goal-completion-loop` | `/goal` in local transcripts | Only if the Routine's runs sync transcripts back to local `~/.claude/projects/` — not guaranteed for cloud execution. |
| `cron-disabled` | `CLAUDE_CODE_DISABLE_CRON=1` | This *would* suppress the local scheduler, but a cloud Routine is configured server-side and a local env var does not necessarily disable it — so the negative guard can give false reassurance here. |

**Where the blind spot is, exactly:** a cloud Routine's authoritative configuration lives in Anthropic's cloud (created via `/schedule`, managed server-side, runs with **no permission prompts** per the docs). The repo and the local home directory can contain **zero** artifacts for it. Every signal in the cluster reads local disk, so the audit's coverage of cloud Routines is effectively nil — and worse, the `cron-disabled` guard can read as "scheduler off / safe" while a server-side Routine keeps firing. The current docs correctly say "we don't cover this"; the sharper statement is "absence of all unattended-execution signals is consistent with an actively-running cloud Routine, and the `cron-disabled` guard does not bound the cloud surface."

A secondary edge: a cloud Routine that *does* commit/PR back to the repo leaves a *downstream* trace — autonomous commits or PRs authored by the Routine. That trace is detectable, but by the **commit-pattern** signals (`commit-ai-coauthoring`, `commit-bursts`, off-hours commits), not by the unattended-execution cluster — and only if the Routine writes to the audited repo at all. So there's a partial, indirect signal already in the system that isn't wired to the cloud-Routine concern.

### The specific check that would close (narrow) it

A repo-local audit cannot *fully* close a server-side blind spot — that's a structural limit, and the honest version of "closure" here is "narrow it and stop the false-reassurance," not "achieve coverage." Three concrete checks, in priority order:

1. **An explicit operator question (the only reliable closer).** Add a single line to the audit's unattended-execution output: *"This audit cannot see cloud Routines (`/schedule`, server-side). If this project uses any, list them and their cadence — they run with no permission prompts and against credentials you've granted."* This is the same move the docs already gesture at ("confirm with the operator"); the closure is making it a required output line, not an optional caveat. Cheap, and it's the only thing that detects a *pure*-cloud Routine.

2. **A first-party listing check, if one exists.** `scheduled-and-looping-primitives.md` notes `CronCreate`/`CronList`/`CronDelete` tools and that `Stop`/`SubagentStop` hook inputs gained a `session_crons` field (changelog v2.1.152). The check to draft and test: does `CronList` (or a `claude` CLI subcommand wrapping it) enumerate **cloud** Routines, or only local/Desktop schedules? If `CronList` returns cloud Routines, that is the manifest the "Gap: cloud-Routine visibility" entry asks for, and the audit should call it instead of (only) globbing disk. **This is NOT-FOUND / unverified right now** — I have not confirmed whether `CronList` covers the cloud surface; that confirmation is the test that would turn this from a proposal into a real closer. Until confirmed, it stays a candidate, not a claim.

3. **Fix the false-reassurance in the negative guard.** Amend the `cron-disabled` semantics so it suppresses only the *local* loop/schedule rows and explicitly does **not** clear the cloud-Routine concern. Concretely: when `CLAUDE_CODE_DISABLE_CRON=1` is observed, the audit should still emit the operator question from (1), with a note that the env var bounds local scheduling but not server-side Routines. This is a one-line behavioral correction to `safety-and-sandboxing.md` line 74 and the AUDIT-CONTEXT negative-guard row.

### Draft language for the docs

For the "Gap: cloud-Routine visibility" entry in `scheduled-and-looping-primitives.md`:

> **Gap: cloud-Routine visibility (partial closure proposed, not yet tested).** A pure-cloud Routine leaves no repo-local or host-local artifact, so the entire unattended-execution signal cluster is blind to it, and `cron-disabled` can give false reassurance because a local env var does not disable a server-side Routine. Closure is structurally partial: (1) make "ask the operator to list cloud Routines and cadence" a required output line, not a caveat — the only reliable detector of a pure-cloud Routine; (2) test whether `CronList` enumerates cloud Routines (NOT-FOUND / unverified as of 2026-06-16) — if it does, call it as the manifest instead of globbing disk; (3) amend `cron-disabled` so it suppresses only local rows and still emits the operator question. **Needs:** confirmation of `CronList`'s cloud coverage, then a testbed Routine to verify the operator-question path and the guard fix.

**Confidence (E):** medium. The mechanism (every signal reads local disk; cloud config is server-side; `cron-disabled` over-suppresses) is clear and follows directly from the documented behavior. The `CronList`-as-manifest closer is the uncertain part and is explicitly marked NOT-FOUND pending a check.

**Sources (E):**
- Anthropic Claude Code docs, "Run prompts on a schedule," `code.claude.com/docs/en/scheduled-tasks` — cloud Routines run on Anthropic infrastructure, no permission prompts, 1-hour minimum interval; `CronCreate`/`CronList`/`CronDelete`. Tier A. (Per the existing `scheduled-and-looping-primitives.md` Sources; `CronList` cloud-coverage NOT independently re-verified for this draft.)
- Existing repo docs being extended: `analysis/safety-and-sandboxing.md` (lines 74, 76, 306), `analysis/scheduled-and-looping-primitives.md` ("Gap: cloud-Routine visibility," Counter-Evidence), `AUDIT-CONTEXT.md` (`cron-disabled` negative-guard row 134).

---

## Hand-off notes for the next review pass

- **B**: ship the corrected wording now (it doesn't overclaim); keep the carry-forward open until a human transcribes the recording for the verbatim passage + timestamp. Primary transcript = NOT-FOUND via tooling.
- **C**: executable as written; run it in a throwaway `CLAUDE_CONFIG_DIR`. Highest-value finding will likely be the `/goal` substring false-positive rate and whether `SKILL.md` is the real leaf filename for scheduled tasks.
- **D**: two corrections are mandatory before any number is quoted — drop the `cores − 2` formula (NOT-FOUND), and relabel the 1,000 cap as **per run** (not lifetime). The 4096 `parallel()`/`pipeline()` figure is NOT-FOUND on the workflows page; drop it or chase it in the SDK reference.
- **E**: the only reliable closer is the operator question; the `CronList`-manifest closer is unverified (NOT-FOUND) and needs a check before it's claimed.

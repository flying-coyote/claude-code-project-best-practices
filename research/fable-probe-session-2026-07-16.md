# Fable 5 Probe Session — Raw Record (2026-07-16)

**Method**: 64-agent controlled probe session on `claude-fable-5` inside the Claude Code harness (probes ran as subagents, so they inherit the harness system prompt and the user's global CLAUDE.md — every result characterizes *Fable-in-harness*, not the bare model). Paired vague-vs-explicit conditions, n=3 reps per condition, all probes at `effort: medium`. Mechanical scoring in the workflow script where possible; LLM judges for behavior-presence counts in code; findings then passed a three-lens adversarial verification (overclaim / method-confound / data-consistency) with default-refute. Consumers of these numbers: `analysis/model-migration-anti-patterns.md` (Fable probe section) and `analysis/behavioral-insights.md` (~150-cap data point).

## Matrix probes (anti-pattern → per-behavior counts, A = vague condition, B = explicit condition)

| Anti-pattern | Behavior | A (of 3) | B (of 3) |
|---|---|---|---|
| vague-descriptors | explicit path/type validation (isinstance + is_file) | 0 | 3 |
| vague-descriptors | clear missing-file error | 3 | 3 |
| vague-descriptors | uses pathlib | 3 | 3 |
| vague-descriptors | type hints on signature | 3 | 3 |
| vague-descriptors | invalid-JSON handling | 3 | 3 |
| edge-case-gestures | empty string handled | 3 | 3 |
| edge-case-gestures | None input handled | 3 | 3 |
| edge-case-gestures | unicode considered | 2 | 3 |
| edge-case-gestures | oversize (10MB) line considered | 0 | 3 |
| unanchored-triggers | logging in fetch / transform / save | 3 / 3 / 3 | 3 / 3 / 3 |

## Scalar probes

- **Verbosity (word counts)**: simple question [75, 67, 65]; complex question, no directive [628, 740, 710]; complex + "Provide concise, focused responses" [429, 415, 473]. Ratio complex/simple ≈ 10x (range 8.4–11.4); directive cut ≈ 37% mean, ranges non-overlapping.
- **Adherence ladder (fraction of N token-inclusion rules satisfied)**: N=10 → [1.0, 1.0, 1.0]; N=40 → [1.0, 1.0, 1.0]; N=80 → [1.0, 1.0, 1.0]; N=150 → [1.0, 1.0, 1.0]. Ceiling at every rung, zero variance.
- **Soft-guideline literalization (em-dash counts, ~350-word essays)**: emphatic-cap condition [1, 1, 2]; advisory condition [3, 6, 3]. VOID — see below.
- **Unread references (constraint-token proxy, 0–2 scale)**: unenforced [0, 0, 0]; enforced-Read control [0, 2, 0]. VOID — see below.
- **Implicit dispatch (self-reported execution mode)**: implicit arm inline 3/3; explicit-dispatch positive control ALSO inline 3/3. VOID — see below.

## Verification outcome (three adversarial lenses, default-refute)

**Survived all three lenses**: vague-descriptors (softened — embedded discriminant at 0/3 vs 3/3 proves the probe separates conditions), edge-case-gestures (softened with residual — resource limits still need enumeration), verbosity (adaptive verbosity present; directive works).

**Voided, with the reason a re-runner needs**:

- implicit-dispatch — positive control failed: the explicit-dispatch arm also ran inline 3/3, consistent with a subagent depth cap (probes were themselves subagents). Needs top-level execution with tool-call telemetry.
- unread-references — proxy failed its own control: enforced reads scored 0,2,0 on token presence, so unenforced 0,0,0 can't discriminate "unread" from "proxy-insensitive." Needs a proxy that fires reliably under enforced reads.
- unanchored-triggers — negative arm saturated: Fable logged in all three functions unprompted, so the paired design has no power here. Needs a behavior the model does not do by default. (The saturation itself is a directional softening hint, but non-discriminative — not graded.)
- soft-guideline-literalization — contaminated dependent variable: the inherited global CLAUDE.md legislates the exact em-dash rate being measured, so the emphatic-arm result can't be attributed to the probe's rule. Needs a clean context or an unlegislated token.
- adherence vs-Opus comparison — the raw ladder stands as a ceiling bound, but "Opus claims did not reproduce" was refuted: no positive control (the instrument never demonstrated it can detect degradation), and synthetic token rules are not comparable to heterogeneous prose instructions. Needs rungs past 150 + realistic rule diversity + a same-instrument Opus comparison arm.

**Caveats carried on every surviving claim**: n=3 per condition, single effort level (medium), in-harness measurand, Tier B observed-in-practice. Workflow run `wf_1446bac1-89b`, 64 agents, 0 errors, ~1.77M subagent tokens.

---

## Re-run of the two fixable voided probes (same day)

### Soft-guideline literalization — fixed instrument (unlegislated token, baseline arm, then genre extension)

Instrument fix: the dependent variable moved from em-dashes (legislated by the inherited global CLAUDE.md, which voided round one) to the second-person word "you" in audience-addressed product copy — unlegislated, high natural baseline, mechanically countable. Arms: no-rule baseline; emphatic (`HARD RULE: ... MUST appear AT MOST 3 times ... NEVER exceed 3`); advisory (`aim for roughly 3 or so ... directional, not a hard cap`). After a first-pass confound refutation was answered with family-count data (see verification trail below), the confound verifier ruled SURVIVES-IF-EXTENDED and specified the extension: 2–3 more genres, n≈7–9/arm, second-person family total (you + your + you'll/you're/you've) pre-registered as primary metric. Executed: 3 new genres (password-manager page, backup-onboarding email, network-monitor landing page), 2 reps/arm/genre, effort medium (runs `wf_3bdfe5fd-572`, `wf_30a3d4b0-70e`).

Pooled, n=9/arm across 4 genres — family totals:

| Arm | Per-rep family totals | Mean |
|---|---|---|
| baseline | 18, 18, 16, 15, 28, 29, 30, 25, 24 | 22.6 |
| emphatic cap-3 | 2, 1, 2, 1, 1, 3, 1, 3, 2 | 1.78 |
| advisory ~3 | 5, 3, 7, 5, 2, 3, 4, 10, 5 | 4.89 |

Bare-"you" (the token the rule literally named): emphatic {1,0,1,1,0,2,1,2,1} — mean 1.0, max 2, never reaching the allowed 3 in any rep; advisory {3,1,3,3,2,2,3,4,3} — mean 2.67, one rep exceeding the stated number (4). Substitution gaming disconfirmed: the emphatic arm suppressed the whole family ~13x below baseline although the rule named one word. Mann-Whitney on the pre-registered family metric, emphatic vs advisory: U = 75.5/81, one-sided p ≈ 0.001; both rule arms separate from baseline with no overlap. Pattern holds in each of the 4 genres individually.

### Implicit dispatch — fixed instrument (working spawn path + transcript telemetry)

Instrument fix: round one was void because workflow-spawned subagents had no Agent tool (their explicit arms ran ToolSearch for it, found nothing, fell back inline — the "tried_to_delegate_but_failed" self-reports were honest tool-unavailability reports, confirmed by zero Agent tool_use blocks in all six transcripts). The overclaim verifier — itself a main-loop-spawned subagent with Agent-tool access — falsified "subagents structurally cannot spawn subagents" and identified the working spawn path. Re-run: 6 probes via the main-loop Agent tool (general-purpose), telemetry from transcripts as ground truth.

| Arm (n=3) | Agent tool calls (telemetry) | Other tools | Outcome |
|---|---|---|---|
| explicit ("Dispatch each task to a separate subagent") | 3, 3, 3 — 9/9 dispatches succeeded | none | **Positive control passes** |
| implicit ("Execute the tasks.") | 0, 0, 0 | Bash (+Read in 2/3) | Inline in all reps |

Method note (scoped per the overclaim verifier): Agent-tool availability differed by spawn path in this session — absent for workflow-spawned general-purpose subagents, present for main-loop-spawned ones. Whether that is a fixed harness property is untested beyond this session; dispatch probes must use a spawn path where the positive control passes. Caveat on the finding: the dispatch probes ran at session effort (xhigh — the Agent tool takes no effort override), unlike every other probe in this record (medium), and the three-item read-only task list makes inline execution economically sensible regardless of propensity, so the finding characterizes default dispatch propensity on small task lists only.

## Final round — remaining Fable-gated instruments (same day)

Four instruments ran (runs `wf_56df2c57-5c4`, `wf_39998af0-0c6`); the two-lens verification split on all three candidate findings (overclaim lens passed them with fixes, confound lens refuted them as graded claims), and the resolution rule applied is: each item enters the record at the strictest surviving wording. Net: three descriptive observations, zero new graded matrix rows, two environmental voids.

- **Heterogeneous adherence ladder** (10 fixed checkable style rules + 3 constructive families; N=40/80/150/250; 3 reps; effort medium): 12/12 reps at 1.0 after correcting one scoring artifact (a semicolon in a prose postscript outside the code block tripped the no-semicolons regex; the code passes — and an earlier draft misstated "36/36", caught by the overclaim verifier; the design is 12 reps). Strictest surviving wording: *no failures observed across 3 reps at up to 250 mechanically-checkable, individually-simple, non-conflicting, explicitly-listed rules*. NOT a bound: the instrument has never demonstrated it can detect degradation (no positive control), ~13 rule types repeated carry far less informational load than 250 independent constraints, the numbered-block presentation is near-optimal scaffolding vs real CLAUDE.md prose, and non-conflicting-by-construction excludes the interaction failure mode real degradation would come from. A graded run needs a rung engineered to fail (conflicting/interacting rules) to prove instrument headroom first.
- **Unanchored triggers** (calibrated: all four candidate behaviors at 0/3 baseline; timing selected): "where applicable" fired in 3/3 reps — every rep instrumented all three functions via a timing decorator, against a 0/3 baseline. The apparent arm difference ([6,5,6] vs [3,3,3] regex occurrences) was a counting artifact: decorator-application telemetry shows both arms instrumented exactly 3 functions; the surplus was docstring mentions and an extra pipeline-level timing block. Refused as a graded "SOFTENED" claim (confound lens): with no demonstrably inapplicable site in the fixture, "where applicable" may function as a plain instruction, and one behavior on one task cannot grade the 4.7 expectation. Descriptive record only. A graded re-run needs applicability heterogeneity built into the fixture, distinct-site counting, and at least one more candidate behavior.
- **Unread references** (telemetry instrument, fixture with unguessable tokens, n=4/arm): the reference-only arm read the fixture 4/4 (exactly one Read each, transcript-confirmed; output tokens 4/4). Refused as a graded claim: the pair saturated (explicit arm also 4/4 — zero within-study contrast, the same defect that voided round-one unanchored-triggers), and the 4.7-era "frequently not read" baseline is not methodologically commensurable (different harness, anecdotal-grade measurement), while a harness that generically reads visible absolute paths is an unexcluded alternative mechanism. Descriptive record only; the doc's 4.7-era row keeps its Tier-A basis and the mechanical-enforcement remediation stands. A graded re-run needs a condition expected to produce <4/4 (relative/buried references) to prove headroom.
- **Context-fill retrieval (Gap 317 instrument)**: VOID environmental — all 9 probes (10 embedded registry facts in ~40k/100k/140k tokens of deterministic filler) were blocked by a harness safety classifier ("blocked... because of earlier conversation content — it isn't about the action itself"); the workflow's zero recalls are blocked-execution artifacts, not retrieval failures. Fix for a future run: fresh session and/or human-authored filler. Gap 317 stays open.
- **Refs first attempt this round**: VOID orchestration — an args-interpolation defect delivered the literal string "undefined" as the fixture path (8/8 agents reported it); superseded by the literal-path re-run above. Workflow-authoring lesson recorded: inline fixture paths as literals in probe scripts rather than passing through `args`.
- Verification note: the two voids were checked by the overclaim lens only (passed clean); the confound lens abstained pending a fuller data package. Both are no-claim records (they assert no model behavior), so one-lens verification was accepted — noted here for the trail's completeness. Consistency fix applied retroactively: round one's "bounds the degradation onset above 150 synthetic rules" phrasing is softened in-doc to descriptive wording, since the same no-positive-control critique applies to it.

### Verification trail (round two)

Confound lens: first verdict REFUTED on substitution-gaming (answered with measured family counts — the emphatic arm did not substitute, it suppressed the family) and n=3 thinness; re-verdict SURVIVES-IF-EXTENDED with the extension spec above; extension executed. Overclaim lens: literalization SURVIVES conditionally with three wording constraints (no "tracks the stated number"; "pilot"-grade framing until extended; limitations adjacent to the headline — all applied here and in the doc text); the original dispatch method note REFUTED for overclaiming "structurally cannot" from six transcripts, with the verifier's own toolset as counter-evidence — the scoped rewrite above incorporates its corrections. Final same-day verdicts on the pooled/extended data are recorded in the docs that cite this file.

---

## Addendum (2026-07-17) — context-fill (Gap 317) fresh-session re-run: classifier void superseded, silent model fallback caught same-day, first gated Fable rows

Fresh session (post-`/clear`), instrument rebuilt per the recorded void fixes. Fixtures: contiguous slices of this repo's own markdown (163 files, seeded shuffle at seed 317, re-wrapped to ≤200-char lines) — naturalistic varied documentation prose, largely Claude-co-authored, so the earlier "human-authored filler" prescription was not literally met and the operative contrast with the voided run is varied natural prose vs bulk deterministic machine-generated filler. Ten registry facts per fixture ("Registry note (probe fixture): the value for registry key X is `v`", random 12-char values, ~31^12 space) at 5%–95% line depth, BEGIN/END marker tokens on the first/last lines, rungs ~40.3k/~100.3k/~140.3k tokens (chars/4 file estimate) plus a ~5.3k calibration fixture; the answer key never appeared in any agent prompt; scoring mechanical. Instrument scripts + answer key archived at `research/artifacts/2026-07-17-context-fill/` (fixtures regenerate from the generator seed against this commit's markdown; later repo states yield different filler, same structure).

**Run 1 (workflow spawn path, `wf_5b0b492d-cda`, effort medium per the workflow script's agent opts — spec, not telemetry): the classifier void did not reproduce, but silent model fallback voided it as a Fable measurement.** All 13 agents (2 no-read negative controls, 2 low-fill positive controls, 9 probes) executed with zero classifier blocks, and every reading rep scored 10/10 with exact markers (like-for-like vs the 2026-07-16 void: 9/9 probes ran vs 9/9 blocked). The confound lens then found per-turn `message.model` telemetry showing all 11 reading agents silently served `claude-opus-4-8` (the workflow fallback) on every turn — only the two no-tool negatives were served `claude-fable-5` — while spot-checks of three 2026-07-16 probe workflows show fable-5 serving tool-using agents throughout, so the fallback is spawn-path- and day-specific with an unknown mechanism. A canary (`wf_34cdc8e6-6e0`) confirmed an explicit `model: 'fable'` pin does not prevent it (2/2 reading agents opus-served on all turns), while the two main-loop-spawned verification agents (16 and 26 tool uses) were fable-served throughout. REFUTED as a Fable finding; recorded as **descriptive Opus 4.8 instrument-validation**: endpoints anchored (no-read floor 0/10, n=2, R40 key set, all answers "unknown"; low-fill ceiling 10/10 ×2), 9/9 probes 10/10, no compaction markers in any transcript, mid-range sensitivity undemonstrated (no rung produced <10/10). Compliance accounting: the exclusion criterion is value externalization into pre-answer output; R40-rep2 met it (8/10 values in interleaved "Found KEY = value" text) and is excluded (it also scored 10/10); all three R140 reps interleaved progress notes (key names in reps 1–2, counts only in rep 3, zero values, telemetry-confirmed), so R140 value retrieval stands but its key-enumeration component was aided; R100 ×3 and R40 reps 1/3 were note-free.

**Run 2 (main-loop Agent spawns, 13 agents; session effort — the Agent tool takes no effort override — and spawn path likewise differ from run 1 and all prior probe rows in this record (main-loop Agent spawns, vs the workflow path)): first gated Fable rows.** Tightened protocol (no text between tool calls, verbatim in every spawn prompt); the value-rehearsal exclusion criterion and the all-fable served-model gate were fixed in advance in the session trail (overclaim-audit correction 5 and the confound-lens gate spec, respectively), though the scoring script implementing them was written post-run. Gate outcome: 12/13 agents served `claude-fable-5` on every model-bearing turn; R100-rep1 excluded — all 20 of its read turns were fable-5 but its report turns were served opus-4-8 (apparent retry, two JSON emissions, one registry value inside the 59-char first partial attempt — report-phase, not reading-phase; it also scored 10/10, so the exclusion is not outcome-selective). Gated results, verified independently by both lenses including a stricter key-paired re-score: positive controls 10/10 ×2; R40 10/10 in 3/3; R100 10/10 in 2/2 clean reps; R140 10/10 in 3/3; negative controls 0/10 ×2 (all "unknown", zero tools — same-path and same-model, doubling as an ambient-leakage control for the reused run-1 fixtures). Telemetry on all scored reps: Read-only on the single fixture, strictly sequential +300 offsets, zero pre-final text blocks, zero value rehearsal, zero compaction markers.

**Strictest surviving wording (confound lens SURVIVES-IF-WEAKENED, wording applied; overclaim lens PASS-WITH-CORRECTIONS, all five applied): DESCRIPTIVE ceiling, zero graded rows.** On this salient-needle instrument, Fable-5-served agents retrieved 10/10 template-flagged registry facts at every embedded depth (5%–95%) through ~140k tokens (chars/4 file estimate; the in-context total at report time is higher — line-number prefixes plus session-effort thinking add to it) of tool-result context fill in every gated rep, with endpoints anchored (no-read floor 0/10, n=2, R40 key set; low-fill ceiling 10/10). NOT a graded claim about the 60% threshold: literal salient needles with the task known upfront are the easiest retrieval regime and semantic (NoLiMa-style) retrieval was untested; the window-fraction denominator for Fable is unknown, so no rung maps to "60%"; no rung has been demonstrated to produce <10/10 (no mid-range sensitivity — the same critique as the heterogeneous adherence ladder); the measurand is in-harness tool-result context, not contiguous prompt context. **Gap 317 stays open** (fill-vs-quality-metric correlation on realistic material). The 2026-07-16 environmental void is SUPERSEDED — the instrument executes end-to-end; and since run 1 executed clean on the void's own workflow spawn path, the de-blocking factor is unattributable between fresh session and filler change only (spawn path/served model are eliminated as necessary de-blocking factors).

**Instrument rules recorded (generalizing the dispatch spawn-path lesson):** (1) retrieval probes must gate scoring on per-turn served model (`message.model` in transcripts) and run on a spawn path where a served-model control passes — the workflowProgress/requested-model fields record the request, not the serve; (2) scoring should be key-matched (key→value pairing), not value-membership only (the stricter re-score changed nothing here, but the gap is real); (3) negative controls should cover every rung's key set, not one rung's.

### Verification trail (addendum)

The run-1 draft was REFUTED by the confound lens on served-model grounds (per-turn telemetry, independently re-confirmed by the coordinator and by the overclaim lens — with the wrinkle that run 1's two negatives were fable-served) after the overclaim lens had passed it with six wording corrections (void "not reproduced" not "resolved"; filler provenance; "endpoint-anchored" not "calibrated in both directions"; negative-control scope n=2/R40-only; compliance accounting including the R140 interleaved notes it discovered; "no compaction markers" not "no compaction"). The amended disposition (run 1 Opus-descriptive + run 2 gated-Fable) was then verified by both lenses against raw transcripts with independent re-scoring: confound SURVIVES-IF-WEAKENED (fill-figure estimator wording, spawn-path disclosure, run-1-row conditions — all applied above), overclaim PASS-WITH-CORRECTIONS (session-trail registration wording, run-1 effort as spec-not-telemetry, floor scope, void attribution narrowed to session-vs-filler, run-1 negatives footnote — all applied above). Raw data: workflow transcript dirs `wf_5b0b492d-cda` and `wf_34cdc8e6-6e0` plus the run-2 main-loop agent transcripts (session-local, transient); the durable record is this file plus the archived instrument at `research/artifacts/2026-07-17-context-fill/`.

---

## Continuation pointer (2026-07-18)

The program's durable open item — the realistic-prose adherence ladder — was executed
2026-07-18 in a follow-on session, together with the token-economics wire re-measure and a
web reverification sweep. Full record, adjudication log, and two-lens verification trails:
[probe-session-2026-07-18.md](probe-session-2026-07-18.md). Headline: Fable 12/12 gated
reps at 1.0 through 200 realistic-diversity rules (descriptive ceiling, cap still
unlocated) on an instrument with a demonstrated-failure-capable checker and a
same-instrument Opus 4.8 arm, which produced the program's first same-instrument
between-model score difference (an interpretation-dependent literalization-propensity gap
on one ambiguously-worded verbatim-phrase rule — fable 6/6 literal vs opus 4/6 at full
n=3/rung after same-day replacement reps; checker-artifact-robust within the strict
reading).

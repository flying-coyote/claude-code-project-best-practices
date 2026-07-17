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

### Verification trail (round two)

Confound lens: first verdict REFUTED on substitution-gaming (answered with measured family counts — the emphatic arm did not substitute, it suppressed the family) and n=3 thinness; re-verdict SURVIVES-IF-EXTENDED with the extension spec above; extension executed. Overclaim lens: literalization SURVIVES conditionally with three wording constraints (no "tracks the stated number"; "pilot"-grade framing until extended; limitations adjacent to the headline — all applied here and in the doc text); the original dispatch method note REFUTED for overclaiming "structurally cannot" from six transcripts, with the verifier's own toolset as counter-evidence — the scoped rewrite above incorporates its corrections. Final same-day verdicts on the pooled/extended data are recorded in the docs that cite this file.

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

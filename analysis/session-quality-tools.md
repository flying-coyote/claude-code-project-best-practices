---
evidence-tier: Mixed
applies-to-signals: [session-diagnostics-run, session-edit-thrashing, session-error-loop, session-repeated-instructions]
last-verified: 2026-04-22
revalidate-by: 2026-10-22
status: PRODUCTION
---

# Session Quality Diagnostic Tools

**Sources**:
- [claude-doctor](https://github.com/aidenybai/claude-doctor) v0.0.3 (Aiden Bai, April 2026) — Session transcript analysis via AFINN-165 sentiment + heuristic pattern detection
- Production observation: 9 repos, 222 sessions analyzed (Evidence Tier C — self-published, unvalidated thresholds)
- AFINN-165 sentiment lexicon (Evidence Tier B — peer-reviewed, 2,477 words scored -5 to +5)

**Evidence Tier**: C (Tool methodology) / B (Underlying sentiment library)

---

## What These Tools Measure

Session quality tools like `claude-doctor` analyze `~/.claude/projects/` transcript logs to detect behavioral anti-patterns. They don't measure code quality — they measure **interaction friction**.

### Signal Categories

| Category | Signals | What's Actually Detected |
|----------|---------|-------------------------|
| **Structural** | edit-thrashing, error-loop, excessive-exploration | Same file edited 5+ times; 3+ consecutive tool failures; read:edit ratio >10:1 |
| **Behavioral** | repeated-instructions, keep-going-loop, rapid-corrections, negative-drift | User rephrasing (60% Jaccard similarity); "keep going" / "continue"; responses within 10s; messages getting shorter + more corrective |
| **Lexical** | negative-sentiment, extreme-frustration | AFINN-165 average <-1; single message score <-5 |

### What the Percentage Score Actually Means

The health percentage is **not a calibrated quality metric**. It uses a penalty formula:

```
scaledPenalty = (critical × 5 + high × 3 + medium × 1) / sessionCount
healthPercentage = max(5, min(100, 100 - scaledPenalty × 8))
```

The multipliers (5, 3, 1) and scaling constant (8) are arbitrary. A 30% score doesn't mean "70% broken" — it means the tool detected patterns that *correlate* with frustration, with uncalibrated severity weighting.

---

## Evidence Assessment

### What's Reliable

| Signal | Methodology | Reliability |
|--------|------------|-------------|
| **edit-thrashing** | File edit counting | HIGH — objective metric; 5+ edits to one file in a session is a real signal |
| **error-loop** | Consecutive tool failure counting | HIGH — 3+ failures without strategy change is measurably wasteful |
| **negative-sentiment (aggregate)** | AFINN-165 lexicon (2,477 words, peer-reviewed) | MEDIUM — validated for general sentiment, not calibrated for developer frustration |
| **repeated-instructions** | Jaccard similarity at 60% threshold | MEDIUM — sound algorithm, arbitrary threshold |

### What's Unreliable

| Signal | Problem |
|--------|---------|
| **extreme-frustration** | Single-message sentiment <-5 triggers "critical" regardless of session length or context. One emphatic correction in a 200-turn productive session gets the same flag as genuine rage. |
| **negative-drift** | Drift formula uses unexplained multipliers (`lengthShrinkage × 5 + correctionIncrease × 10`). Messages getting shorter could mean the user is efficiently directing, not frustrated. |
| **rapid-corrections** | 10-second response threshold assumes fast replies = frustration. Experienced users type corrections faster because they know exactly what's wrong. |
| **keep-going-loop** | Doesn't distinguish "keep going, this is great" from "keep going, you stopped early." Treats all continuation requests as failures. |
| **Overall percentage** | Arbitrary thresholds, no statistical significance testing, no sample-size normalization. 1 "keep going" in 2 messages penalizes harder per-session than 5 in 100 messages. |

### What's Missing

- **No positive signal detection** — Tool only measures friction, never flow. A session with zero negatives gets 100% but could still be inefficient.
- **No context-awareness** — "no" at message start is always negative ("no, wrong") but misses "no problem" or "no need to change that."
- **No task-type normalization** — Exploratory research sessions naturally have more course-correction than bug-fix sessions. Both get penalized equally.
- **No outcome measurement** — A session that produces excellent code through 3 corrections scores worse than a session that produces nothing without friction.

### Gaps (explicit confidence statements)

Per [Confidence Scoring](confidence-scoring.md), claims with unvalidated thresholds should state what would raise confidence:

- **Gap: severity-weight calibration.** The 5/3/1 multipliers and ×8 scaling constant have no reported derivation. **Needs**: published study correlating score bands to independent outcome measures (task-completion rate, user-reported frustration rating, downstream bug rate).
- **Gap: threshold validation.** The 60% Jaccard similarity (repeated-instructions), 3-failure error-loop trigger, and 10-second rapid-corrections threshold are not empirically calibrated against labeled session data. **Needs**: precision/recall metrics on a labeled corpus of sessions classified as high/low-quality by experienced users.
- **Gap: task-type baseline rates.** Unknown how each signal's false-positive rate varies across task types (debugging vs. exploratory research vs. feature implementation). **Needs**: per-task-type baseline distributions so scores can be interpreted relative to a task class, not uniformly.
- **Gap: positive-signal taxonomy.** The tool is entirely friction-focused — no evidence basis exists for what flow-state signals look like in Claude Code sessions. **Needs**: qualitative study identifying positive-flow indicators (successful one-shot task completion, low-latency satisfied responses, etc.) that could balance the scoring.

These gaps place claude-doctor output at **Tier C** for absolute interpretation (score thresholds) and **Tier B** for relative comparison (same tool, same user, session-over-session trend). See [Confidence Scoring](confidence-scoring.md#medium-confidence) for the template this follows.

---

## What Low Scores Actually Indicate

Low scores don't mean your Claude Code setup is wrong. Based on 9-repo analysis:

### True Positives (Score Reflects Real Issues)

| Pattern | Score Impact | Actionable? |
|---------|-------------|-------------|
| Missing CLAUDE.md → Claude guesses project conventions → user corrects repeatedly | negative-sentiment, repeated-instructions | YES — add CLAUDE.md |
| No error recovery guidance → Claude retries same failing approach → user intervenes | error-loop, edit-thrashing | YES — add rules for error handling |
| Ambiguous task specification → Claude builds wrong thing → user course-corrects | negative-drift, rapid-corrections | YES — use plan mode |

### False Positives (Score Penalizes Normal Work)

| Pattern | Score Impact | Actually Normal? |
|---------|-------------|-----------------|
| Knowledge base / creative work with iterative refinement | edit-thrashing | YES — exploring ideas requires revision |
| User gives terse, efficient direction (experienced operator) | negative-drift, rapid-corrections | YES — expertise looks like frustration to sentiment analysis |
| Complex multi-step task with expected failures along the way | error-loop | YES — not every tool error is avoidable |
| Early-stage project with no established patterns | negative-sentiment | YES — setup conversations are naturally corrective |

---

## Practical Guidance: How to Use These Tools

### Do

1. **Use edit-thrashing and error-loop as harness improvement signals** — These are the most reliable indicators. If Claude edits the same file 5+ times, your CLAUDE.md probably lacks guidance for that file type or pattern.
2. **Compare the same repo over time** — The absolute score is unreliable, but relative trends within a repo track real improvement.
3. **Use signals to prioritize CLAUDE.md updates** — If "repeated-instructions" is high, the thing you keep repeating belongs in CLAUDE.md or a rule file.
4. **Ignore the percentage** — The composite score has arbitrary weighting. Focus on individual signals.

### Don't

1. **Don't compare scores across repos** — A knowledge base repo (iterative, exploratory) will always score lower than a mature code project (structured, deterministic). This is expected, not broken.
2. **Don't adopt all suggested rules verbatim** — The tool generates generic recommendations from frequency counts. Some apply; many are already handled by well-structured harnesses.
3. **Don't treat low scores as failures** — A 5% score with 20 productive sessions that shipped real work is better than a 95% score with sessions that accomplished nothing.
4. **Don't over-optimize for the metric** — Adding "stop and re-read" rules to CLAUDE.md to reduce correction counts is cargo-culting. Fix the root cause (missing context) instead.

### The Real Question to Ask

When a signal fires, ask: **"What context was Claude missing that caused this friction?"**

| Signal | Root Cause Question |
|--------|-------------------|
| edit-thrashing | What file pattern knowledge is missing from CLAUDE.md? |
| error-loop | What error recovery strategy should be in a rule? |
| repeated-instructions | What instruction should be permanent in CLAUDE.md instead of repeated per-session? |
| negative-sentiment | Was the task inherently exploratory, or was Claude genuinely lost? |

---

## Observed Correlation: Harness Maturity vs. Score

From 4-repo analysis (9 repos, 222 sessions total):

| Repo | Score | Sessions | CLAUDE.md | Hooks | Skills | Rules | Key Differentiator |
|------|-------|----------|-----------|-------|--------|-------|--------------------|
| mndr-review-automation | 87% | 176 | 169 lines | 1 (pre-tool-use) | 0 | 4 | Focused security boundary, clear architecture docs |
| claude-code-project-best-practices | 74% | 4 | 33 lines | 3 | 7 | 0 | Skill-driven automation, deterministic tasks |
| health-inventory | 56% | 2 | 129 lines | 1 | 0 | 4 | High commit velocity, no automation layer |
| third-brain | 5% | 20 | 62 lines | 2 | 3 | 8 | Knowledge base work (inherently iterative), most harness complexity |

**Finding**: Score correlates with **task determinism**, not harness complexity. The highest-scoring repo (mndr-review-automation) has the leanest harness but the most structured, deterministic workflow. The lowest-scoring repo (third-brain) has the most harness infrastructure but does inherently exploratory knowledge work.

**Implication**: Don't add more harness to fix low scores. Instead, match your harness to your task type:
- **Deterministic code projects**: Lean CLAUDE.md + focused security hooks = high scores naturally
- **Exploratory knowledge projects**: Accept lower scores; optimize for *outcome* not *friction reduction*

---

## Recommended CLAUDE.md Rules (Evidence-Filtered)

From claude-doctor's 8 suggested rules, filtered by evidence reliability:

### Worth Adding (address real root causes)

> **Read the full file before editing. If you've edited a file 3+ times in this session, stop and re-read the user's requirements.**

*Why*: edit-thrashing is a reliable signal. This rule addresses the root cause (incomplete context before editing). Aligns with Boris Cherny's "verification = 2-3x quality" finding (Authority 5).

> **After 2 consecutive tool failures, stop and change your approach entirely. Explain what failed and try a different strategy.**

*Why*: error-loop is a reliable signal. This directly prevents the most measurably wasteful pattern. Aligns with Anthropic's harness guidance on error recovery (Authority 5).

### Context-Dependent (useful for some projects)

> **When the user corrects you, stop and re-read their message. Quote back what they asked for and confirm before proceeding.**

*When*: Useful for projects with complex multi-step requirements. Unnecessary overhead for experienced operators giving terse direction.

### Skip (cargo-culting or redundant)

> **Every few turns, re-read the original request to make sure you haven't drifted from the goal.**

*Why*: Wastes context window re-reading. Claude Code's task system already tracks goals. If you're using plan mode, drift is already managed.

> **Complete the FULL task before stopping.**

*Why*: Claude Code already does this by default. Adding this instruction wastes CLAUDE.md budget for zero behavioral change.

---

## Related Analysis

- [Confidence Scoring](confidence-scoring.md) — the Gap-statement format this doc uses
- [CLAUDE.md Progressive Disclosure](claude-md-progressive-disclosure.md) — edit-thrashing and repeated-instructions signals often map to CLAUDE.md gaps
- [Harness Engineering](harness-engineering.md) — error-loop signals often map to missing harness-level recovery
- [Model Migration Anti-Patterns](model-migration-anti-patterns.md) — distinguishing genuine session-quality issues from Opus 4.7 silent-no-op artifacts
- [Evidence-Based Revalidation](evidence-based-revalidation.md) — session diagnostics as a revalidation signal over time

---

**Tags**: #analysis #session-quality #diagnostic-tools #evidence-assessment

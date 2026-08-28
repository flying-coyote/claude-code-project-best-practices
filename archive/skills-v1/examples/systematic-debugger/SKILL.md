---
name: systematic-debugger
description: Apply 4-phase root cause debugging methodology when user encounters errors, bugs, test failures, or unexpected behavior in code. Trigger when user mentions "bug", "error", "failing", "not working", "debug", or shares error messages. Use systematic approach rather than guess-and-check.
allowed-tools: Read, Grep, Glob, Bash
---

# Systematic Debugger

> **ARCHIVED — but nothing live replaces it.** Archived in the v2.0 repositioning (March 2026, DECISIONS.md § Reposition as Analytical Layer) or a later reduction. No live doc teaches a debugging methodology — the only live mentions are analysis/memory-system-patterns.md ruling that debugging fixes belong in git history rather than memory — so this is uncovered territory here, with the file's own pointer to obra/superpowers the nearest external home. This is a **coverage gap, not a currency gap** — the material is unreplaced, not merely out of date, so a reader who discards it is left with nothing. Its specifics are v1-era; its subject is still uncovered. (Marked 2026-08-28; successor determined by mapping plus adversarial verification, which overturned 35 of 39 successor claims — see `analysis/prose-corpus-discoverability.md`.)

Replace ad-hoc debugging with systematic REPRODUCE-ISOLATE-UNDERSTAND-FIX protocol.

> 🔗 **Production Framework**: For advanced debugging with strict enforcement, see [obra/superpowers](https://github.com/obra/superpowers) which provides production-grade debugging frameworks and multi-agent orchestration patterns. This skill demonstrates **Claude Code skill integration** of systematic debugging principles.

## Trigger Conditions

**Activate**: Bug reports, error messages, stack traces, test failures, "not working", "broken", "debug", "why is this happening?"

**Skip**: Design/planning phase, theoretical discussions, trivial errors (typos, missing imports)

## 4-Phase Protocol

### Phase 1: REPRODUCE
Confirm problem exists. Get exact error message, trigger conditions, frequency, last known working state.

### Phase 2: ISOLATE
Narrow problem space. Binary search through code, add instrumentation, find minimal failing case. Identify: logic, data, timing, environment, integration, or assumption error.

### Phase 3: UNDERSTAND
Root cause analysis. Form hypothesis → predict evidence → test → confirm/reject. Ask: WHY does this happen, not just WHAT.

### Phase 4: FIX & VALIDATE
Fix root cause (not symptom). Add regression test. Run full test suite. Check for similar issues elsewhere.

## Output Format

```
Phase 1: Reproduction Confirmed
- Error: [exact message]
- Trigger: [conditions]
- Files: [file:line]

Phase 2: Problem Isolated
- Root location: [file:line]
- Problem type: [logic/data/timing/environment/integration/assumption]

Phase 3: Root Cause Identified
- Why it happens: [explanation]
- Blast radius: [what else affected]

Phase 4: Fix Validated
✅ Problem resolved
✅ Regression test added
✅ All tests pass
✅ Similar issues checked
```

## Don't

- Guess-and-check without understanding
- Fix symptoms instead of root cause
- Skip reproduction ("I think I know what it is")
- Apply Stack Overflow solutions without validation
- Fix without adding regression test
- Declare victory without running full test suite

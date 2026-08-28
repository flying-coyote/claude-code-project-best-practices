---
name: tdd-enforcer
description: Enforce Test-Driven Development (TDD) RED-GREEN-REFACTOR cycle when user writes code, implements features, or fixes bugs. Trigger when user mentions "implement", "add feature", "create function", "build", or starts coding without tests. Apply to Python, TypeScript, JavaScript, and all languages with testing frameworks.
allowed-tools: Read, Grep, Glob, Bash, Write
---

# TDD Enforcer

> **ARCHIVED — but nothing live replaces it.** Archived in the v2.0 repositioning (March 2026, DECISIONS.md § Reposition as Analytical Layer) or a later reduction. The closest live material, analysis/agent-driven-development.md § Test-Driven Progression, measures test growth as an infrastructure-maturity signal rather than teaching test-first practice, so the RED-GREEN-REFACTOR cycle here has no live successor and the file's own pointer to obra/superpowers is the nearest external home. This is a **coverage gap, not a currency gap** — the material is unreplaced, not merely out of date, so a reader who discards it is left with nothing. Its specifics are v1-era; its subject is still uncovered. (Marked 2026-08-28; successor determined by mapping plus adversarial verification, which overturned 35 of 39 successor claims — see `analysis/prose-corpus-discoverability.md`.)

Enforce tests BEFORE implementation using RED-GREEN-REFACTOR cycle.

> 🔗 **Production Framework**: For strict TDD enforcement in production projects, see [obra/superpowers](https://github.com/obra/superpowers) which provides battle-tested, production-grade TDD enforcement with deeper integration. This skill is a **lightweight learning alternative** for understanding TDD principles and integrating with Claude Code's native skill system.

## Trigger Conditions

**Activate**: "implement", "add feature", "create function", "build", "let's code this", writes production code without tests

**Skip**: Exploration/research, documentation, refactoring tested code, "skip tests" (but warn)

## RED-GREEN-REFACTOR Cycle

### RED: Write Failing Test First
1. Understand requirement
2. Write test describing desired behavior
3. Run test → confirm FAIL (for right reason, not syntax)

### GREEN: Minimal Implementation
1. Write simplest code to pass test
2. No extra features or future-proofing
3. Run test → confirm PASS

### REFACTOR: Improve Quality
1. Improve readability, remove duplication
2. Run tests after EACH change
3. Never add new behavior during refactor

## Output Format

```python
# RED: Failing test
def test_[function]_[scenario]_[outcome]():
    # Arrange
    [setup]
    # Act
    [call]
    # Assert
    [verify]

# Run: pytest → FAIL ✅ RED

# GREEN: Minimal implementation
def function():
    [minimal_code]

# Run: pytest → PASS ✅ GREEN

# REFACTOR: Improved code
def function():
    [better_code]

# Run: pytest → ALL PASS ✅ REFACTOR complete
```

## TDD Violation Detection

If user writes production code without test:
```
⚠️ TDD VIOLATION: Writing code without test.
Let's write the test first. What behavior should we test?
```

## Don't

- Write implementation before tests ("I'll add tests later")
- Skip tests for "simple" functions
- Test implementation details instead of behavior
- Write tests that always pass
- Commit code without tests

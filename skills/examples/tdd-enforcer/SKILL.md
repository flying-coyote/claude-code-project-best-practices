---
name: tdd-enforcer
description: Enforce Test-Driven Development (TDD) RED-GREEN-REFACTOR cycle when user writes code, implements features, or fixes bugs. Trigger when user mentions "implement", "add feature", "create function", "build", or starts coding without tests. Apply to Python, TypeScript, JavaScript, and all languages with testing frameworks.
allowed-tools: Read, Grep, Glob, Bash, Write
---

# TDD Enforcer

Enforce tests BEFORE implementation using RED-GREEN-REFACTOR cycle.

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

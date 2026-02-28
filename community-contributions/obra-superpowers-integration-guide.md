# Integration Guide: obra/superpowers with Claude Code Native Features

**Target**: Contribute to obra/superpowers documentation or our own docs with cross-reference

**Purpose**: Lower barrier to entry for Claude Code users wanting to adopt superpowers

**Status**: DRAFT - Requires testing and validation

---

## Overview

This guide shows how to use [obra/superpowers](https://github.com/obra/superpowers) production-grade frameworks alongside Claude Code's native skill system, hooks, and subagents.

**Goal**: Progressive adoption path from learning to production.

---

## Integration Patterns

### Pattern 1: Learning Path (Skills → Superpowers)

**Scenario**: New to TDD/debugging, want to learn before strict enforcement

**Approach**:
1. Start with lightweight skills (tdd-enforcer, systematic-debugger)
2. Learn methodology with gentle guidance
3. Graduate to superpowers for production rigor

**Implementation**:

```bash
# Phase 1: Learning (Months 1-2)
# Use our lightweight skills
mkdir -p .claude/skills
curl -o .claude/skills/tdd-enforcer.md \
  https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/skills/examples/tdd-enforcer/SKILL.md

# Claude Code auto-detects and suggests skill
# No strict enforcement, learn RED-GREEN-REFACTOR

# Phase 2: Production (Month 3+)
# Install superpowers for strict enforcement
git clone https://github.com/obra/superpowers ~/.claude/plugins/superpowers

# Configure for production in .claude/settings.json
{
  "plugins": {
    "superpowers": {
      "enabled": true,
      "strict_mode": true
    }
  }
}
```

**Benefits**:
- Lower intimidation factor for beginners
- Gradual adoption vs. "all at once"
- Learn principles before enforcement

---

### Pattern 2: Hybrid Mode (Skills for Learning + Superpowers for Production)

**Scenario**: Teaching team while maintaining production quality

**Approach**:
- Use lightweight skills in feature branches (learning)
- Use superpowers in main branch (enforcement)

**Implementation**:

```bash
# Per-branch configuration
# Feature branch: .claude/settings.json
{
  "skills": {
    "enabled": ["tdd-enforcer", "systematic-debugger"]
  },
  "plugins": {
    "superpowers": {
      "enabled": false  # Learn without strict enforcement
    }
  }
}

# Main branch: .claude/settings.json
{
  "plugins": {
    "superpowers": {
      "enabled": true,
      "strict_mode": true  # Production enforcement
    }
  }
}

# Enforce via hook in main branch
# .claude/hooks/pre-commit.sh
if [ "$(git branch --show-current)" = "main" ]; then
  echo "Main branch requires superpowers strict mode"
  # Verify superpowers is active
fi
```

**Benefits**:
- Team can learn in feature branches
- Production quality maintained in main
- Clear graduation path

---

### Pattern 3: Superpowers + Claude Code Subagents

**Scenario**: Complex debugging with specialized agents

**Approach**:
- Use superpowers for debugging methodology
- Use Claude Code subagents for parallel investigation

**Implementation**:

```markdown
# In CLAUDE.md
When debugging:
1. Use superpowers systematic-debugger protocol
2. Spawn specialized subagents for parallel investigation:
   - Explore agent: Find related code patterns
   - Plan agent: Architect fix strategy
   - Research agent: Check for similar issues in community

Example workflow:
- Parent agent: Runs superpowers debugging (REPRODUCE-ISOLATE-UNDERSTAND-FIX)
- Subagent 1: Explores codebase for similar patterns (isolation phase)
- Subagent 2: Researches GitHub issues for known solutions (understanding phase)
- Parent: Synthesizes findings, implements fix (fix phase)
```

**Benefits**:
- Combine superpowers rigor with Claude Code parallelization
- Faster debugging through parallel investigation
- Maintain methodology while scaling work

---

### Pattern 4: Superpowers + Claude Code Hooks (Quality Gates)

**Scenario**: Enforce superpowers patterns via automated hooks

**Approach**:
- Superpowers provides methodology
- Hooks enforce compliance

**Implementation**:

```json
// .claude/settings.json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{
        "type": "command",
        "command": "bash -c 'if ! grep -q \"test_\" $(git diff --name-only); then echo \"⚠️ SUPERPOWERS VIOLATION: Write tests first\"; exit 1; fi'"
      }]
    }],

    "Stop": [{
      "matcher": "",
      "hooks": [{
        "type": "command",
        "command": "bash -c 'pytest --quiet || (echo \"⚠️ Tests failing - fix before closing session\"; exit 1)'"
      }]
    }]
  }
}
```

**Benefits**:
- Automated enforcement (can't forget)
- Fails fast (catch violations early)
- Integrates with CI/CD

---

## Comparison Matrix: When to Use Each

| Feature | Lightweight Skills | Superpowers | Both |
|---------|-------------------|-------------|------|
| **Learning TDD** | ✅ Best | ⚠️ Strict | 🎯 Progressive |
| **Production enforcement** | ❌ Too gentle | ✅ Best | 🎯 Hybrid |
| **Team onboarding** | ✅ Best | ❌ Intimidating | 🎯 Gradual |
| **Complex debugging** | ⚠️ Basic | ✅ Systematic | 🎯 + Subagents |
| **Multi-agent orchestration** | ❌ Limited | ✅ Advanced | 🎯 + Native features |
| **Setup complexity** | ✅ Simple | ⚠️ Moderate | ⚠️ Requires planning |

---

## Migration Guide: Skills → Superpowers

### Step 1: Assess Readiness

**You're ready to migrate when**:
- Team understands TDD/debugging principles
- Comfortable with Claude Code basics
- Ready for strict enforcement
- Production quality is priority

**Stay with skills if**:
- Still learning principles
- Flexibility more important than rigor
- Exploring methodologies
- Small personal projects

### Step 2: Test Superpowers in Isolation

```bash
# Test in a worktree (isolated environment)
git worktree add .claude/worktrees/superpowers-test -b test/superpowers

cd .claude/worktrees/superpowers-test

# Install and configure
git clone https://github.com/obra/superpowers ~/.claude/plugins/superpowers

# Test on small feature
# Verify enforcement works as expected
# Measure impact on workflow speed
```

### Step 3: Gradual Rollout

```markdown
Week 1: Enable superpowers in feature branches only
Week 2: Enable in staging branch
Week 3: Team retrospective - adjust configuration
Week 4: Enable in main branch with full enforcement
```

### Step 4: Keep Skills as Documentation

```bash
# Keep lightweight skills as reference documentation
mv .claude/skills/tdd-enforcer.md .claude/docs/learning-tdd.md

# Update CLAUDE.md
echo "## Methodology
We use superpowers for production TDD enforcement.
For learning resources, see .claude/docs/" >> .claude/CLAUDE.md
```

---

## Contribution Opportunities

### To obra/superpowers Repository

If this integration guide is useful, we could contribute:

1. **Documentation PR**: "Integrating with Claude Code Native Features"
   - Location: `docs/claude-code-integration.md`
   - Content: These integration patterns
   - Value: Lower barrier to entry for Claude Code users

2. **Example Configurations**:
   - `.claude/settings.json` templates for superpowers
   - Hook examples for enforcement
   - Subagent orchestration patterns

3. **Learning Path Documentation**:
   - "Progressive adoption: Skills → Superpowers"
   - Link to our lightweight skills as learning alternatives
   - Clear graduation criteria

### To Our Repository

Alternatively, maintain in our docs:

```markdown
patterns/superpowers-integration.md
- Integration patterns (above)
- Link prominently to obra/superpowers
- Position as "how to use superpowers with Claude Code"
```

---

## Testing Checklist

Before contributing or publishing:

- [ ] **Install superpowers** - Test installation process
- [ ] **Test Pattern 1** - Verify skills → superpowers migration works
- [ ] **Test Pattern 2** - Verify hybrid mode configuration
- [ ] **Test Pattern 3** - Verify subagent integration
- [ ] **Test Pattern 4** - Verify hook enforcement
- [ ] **Measure impact** - Document workflow speed changes
- [ ] **Get feedback** - Share draft with obra maintainers
- [ ] **Update for accuracy** - Incorporate feedback

---

## Questions for obra/superpowers Maintainers

Before contributing, ask:

1. **Would this integration guide be useful?**
   - Is there demand from Claude Code users?
   - Does it align with your vision?

2. **Where should it live?**
   - In your repo (docs/claude-code-integration.md)?
   - In our repo with cross-reference?
   - Both?

3. **What would you change?**
   - Different integration patterns?
   - Missing use cases?
   - Technical inaccuracies?

4. **Maintenance responsibility?**
   - We maintain integration guide?
   - You maintain, we contribute updates?
   - Joint maintenance?

---

## Related Resources

- [obra/superpowers](https://github.com/obra/superpowers) - Production-grade frameworks
- [Our lightweight skills](https://github.com/flying-coyote/claude-code-project-best-practices/tree/master/skills/examples) - Learning alternatives
- [Claude Code Subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents) - Official docs
- [Our hooks pattern](https://github.com/flying-coyote/claude-code-project-best-practices/blob/master/patterns/advanced-hooks.md) - Quality gates

---

## Next Steps

1. **Test integration locally** (4 hours)
2. **Draft contribution proposal** to obra (1 hour)
3. **Get feedback** before formal contribution
4. **Iterate based on maintainer guidance**
5. **Publish as PR or maintain in our docs**

---

*Draft created: February 27, 2026 - Awaiting testing and validation*

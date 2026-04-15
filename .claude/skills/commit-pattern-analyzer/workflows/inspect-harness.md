# Workflow: Inspect Harness Structure

## Purpose
Check a project's Claude Code infrastructure maturity by inventorying the
presence and quality of harness components. Produces a 0-6 harness score.

## Steps

### 1. Check Components (Bash)
```bash
# CLAUDE.md (check both locations)
root_claude=$(test -f CLAUDE.md && wc -l < CLAUDE.md || echo 0)
dot_claude=$(test -f .claude/CLAUDE.md && wc -l < .claude/CLAUDE.md || echo 0)

# Settings
settings=$(test -f .claude/settings.json && echo "yes" || echo "no")

# Rules
rules=$(ls .claude/rules/*.md 2>/dev/null | wc -l | tr -d ' ')

# Hooks
hooks=$(ls .claude/hooks/ 2>/dev/null | tr '\n' ', ' || echo "none")

# Skills
skills=$(ls -d .claude/skills/*/ 2>/dev/null | wc -l | tr -d ' ')

# Commands
commands=$(ls -d .claude/commands/*/ 2>/dev/null | wc -l | tr -d ' ')
```

### 2. Score (0-6)

| Component | Present? | Score |
|-----------|----------|-------|
| CLAUDE.md (root or .claude/) | root_claude > 0 OR dot_claude > 0 | +1 |
| .claude/settings.json | settings = "yes" | +1 |
| .claude/rules/*.md | rules > 0 | +1 |
| .claude/hooks/ | hooks != "none" | +1 |
| .claude/skills/ | skills > 0 | +1 |
| .claude/commands/ | commands > 0 | +1 |

### 3. Assess Maturity

| Score | Level | Interpretation |
|-------|-------|---------------|
| 0 | None | No Claude Code infrastructure |
| 1-2 | Basic | Minimal setup (CLAUDE.md only) |
| 3-4 | Intermediate | Active harness tuning |
| 5-6 | Advanced | Full infrastructure stack |

### 4. Output

```markdown
## Harness Inventory

- [x/] CLAUDE.md — {root_claude} lines (root) / {dot_claude} lines (.claude/)
- [x/] .claude/settings.json — {settings}
- [x/] .claude/rules/ — {rules} rule files
- [x/] .claude/hooks/ — {hooks}
- [x/] .claude/skills/ — {skills} skills
- [x/] .claude/commands/ — {commands} commands

**Harness Score**: {score}/6 ({level})
```

## Cross-Reference

Map harness gaps to analysis docs:
- Missing CLAUDE.md -> `claude-md-progressive-disclosure.md` (start with Tier 1 template)
- No rules -> `domain-knowledge-architecture.md` (encode domain knowledge)
- No hooks -> `harness-engineering.md` (lifecycle management)
- No skills -> `mcp-vs-skills-economics.md` (skills preferred for cost)

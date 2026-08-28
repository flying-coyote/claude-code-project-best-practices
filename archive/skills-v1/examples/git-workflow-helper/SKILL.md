---
name: git-workflow-helper
description: Apply git best practices for commits, branches, worktrees, and collaboration when user performs version control operations. Trigger when user mentions "git", "commit", "branch", "merge", "push", "pull request", or prepares to commit code. Ensure clear commit messages, proper branching, and safe git operations.
allowed-tools: Bash, Read, Grep
---

# Git Workflow Helper

> **ARCHIVED — but nothing live replaces it.** Archived in the v2.0 repositioning (March 2026, DECISIONS.md § Reposition as Analytical Layer) or a later reduction. No live analysis doc covers commit or branching conventions — the repo's own conventions live in .claude/CLAUDE.md, and analysis/evidence-tiers.md records the companion `/commit-push-pr` slash command as deprecated in favour of natural-language git operations — so the guidance here has no successor. This is a **coverage gap, not a currency gap** — the material is unreplaced, not merely out of date, so a reader who discards it is left with nothing. Its specifics are v1-era; its subject is still uncovered. (Marked 2026-08-28; successor determined by mapping plus adversarial verification, which overturned 35 of 39 successor claims — see `analysis/prose-corpus-discoverability.md`.)

Ensure clean version control: meaningful commits, safe branching, proper collaboration workflows.

## Trigger Conditions

**Activate**: Prepares to commit, asks about git workflow, creates branches, prepares PRs, says "commit this", "push", "create PR"

**Skip**: Just viewing git status/log, reading history, theoretical git discussion

## Commit Message Format

```
<type>(<scope>): <description>

[optional body]
```

**Types**: feat, fix, docs, style, refactor, test, chore

## Branch Naming

```
feature/short-description
bugfix/issue-number-description
hotfix/critical-fix
release/v1.2.0
```

## Dangerous Operations

**ALWAYS confirm before**:
- `git push --force` → use `--force-with-lease`
- `git reset --hard` → use `--soft` or `stash` first
- `git rebase` on shared branches → coordinate with team

## Quick Fixes

```bash
# Undo last commit (keep changes)
git reset --soft HEAD~1

# Fix commit message
git commit --amend -m "New message"

# Add to last commit
git add file && git commit --amend --no-edit
```

## Output Format

**Commit Preparation**:
```
Files staged: [list]
Suggested message:
  feat(component): add capability
Command: git commit -m "..."
```

**Safety Warning**:
```
⚠️ DANGEROUS OPERATION
You're about to: [operation]
This will: [consequences]
Safe alternative: [command]
```

## Don't

- Commit with vague messages ("fix", "update", "wip")
- Force push to shared branches
- Commit secrets or credentials
- Skip pre-commit hooks without reason
- Rebase published commits without coordination

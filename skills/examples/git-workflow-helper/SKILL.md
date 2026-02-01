---
name: Git Workflow Helper
description: Apply git best practices for commits, branches, worktrees, and collaboration when user performs version control operations. Trigger when user mentions "git", "commit", "branch", "merge", "push", "pull request", or prepares to commit code. Ensure clear commit messages, proper branching, and safe git operations.
allowed-tools: Bash, Read, Grep
---

# Git Workflow Helper

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

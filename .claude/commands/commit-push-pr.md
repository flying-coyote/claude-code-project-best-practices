---
description: Commit current changes, push to remote, and create a PR. Use when ready to submit work for review.
allowed-tools: Bash
---

# Commit, Push, and Create PR

Execute a complete git workflow in sequence:

## Steps

1. **Check Status**
   - Run `git status` to see all changes
   - Run `git diff --stat` to summarize modifications

2. **Stage and Commit**
   - Stage all relevant changes (skip .env, credentials, secrets)
   - Create commit with conventional prefix:
     - `📚` for documentation/patterns
     - `🔧` for configuration/infrastructure
     - `✅` for validation/testing
     - `📊` for research/analysis
   - Include Co-Authored-By line

3. **Push to Remote**
   - Push to current branch: `git push origin master`

4. **Create Pull Request** (if on feature branch)
   - Use `gh pr create` with Summary and Test Plan sections
   - Return PR URL

## Commit Message Format

```
[emoji] Brief description

- Detail 1
- Detail 2

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
```

## Example

```bash
git add -A && \
git commit -m "$(cat <<'EOF'
📚 Add new pattern documentation

- Document parallel sessions workflow
- Add GitHub Actions integration guide

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
EOF
)" && \
git push origin master
```

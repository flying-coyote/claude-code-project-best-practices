---
evidence-tier: Mixed
convergence: single-source
applies-to-signals: [harness-mcp, harness-skills, harness-hooks, harness-custom-agents, tool-mcp-unpinned, tool-mcp-remote, tool-repo-self-approval, tool-project-env-redirect, tool-hook-network, tool-hook-fail-open, tool-skill-grants-tools, tool-hidden-unicode, tool-agent-inherits-all, tool-plugin-marketplace-declared, tool-broad-grants]
last-verified: 2026-11-03
revalidate-by: 2027-02-03
status: EMERGING
measurement-claims:
  - claim: "Snyk ToxicSkills: 3,984 skills from ClawHub + skills.sh scanned; 534 (13.4%) with at least one critical issue; 76 confirmed malicious payloads after human review (the headline '1,467 malicious payloads' is skills with any flaw of any severity, 36.82%)"
    source: "Snyk, ToxicSkills (Tier B vendor research, self-tuned detectors, flag bias), corpus as of 2026-02-05"
    date: "2026-02-05"
    revalidate: "2027-02-05"
  - claim: "Claude for Chrome red-team: 123 cases / 29 scenarios; 23.6% attack success without mitigations, 11.2% with; 35.7% to 0% on four browser-specific attack types"
    source: "Anthropic, Piloting Claude for Chrome (Tier A, vendor's own evaluation)"
    date: "2025-08-25"
    revalidate: "2027-02-03"
---

# AI Tool Vetting: Reviewing What an Agent Can Use, Before and After Adoption

**Revalidation window**: three months (`revalidate-by: 2027-02-03`) rather than the template's usual six, because the Claude Code policy keys this doc cites changed semantics several times in 2026 (see Step 4).

**Evidence Tier**: Mixed (A for Claude Code docs and changelog, the MCP specification 2026-07-28, OWASP, NIST and vendor security bulletins; B for disclosed-method research from Invariant Labs, Trail of Bits, Check Point, Snyk, JFrog, Willison and Rehberger; C for relayed incident reporting). Per-claim tiers are inline; the verification trail is [research/ai-tool-vetting-sources-2026-11-03.md](../research/ai-tool-vetting-sources-2026-11-03.md).

> **Convergence note.** Each component practice here (review before install, pin, least privilege, sandbox, re-review) has independent first-party backing: Anthropic's [plugin security page](https://code.claude.com/docs/en/plugins/security), the MCP specification's consent and authorization rules, OWASP's third-party MCP guide, and NIST AI 600-1 GV-6.1-007. The integrated per-tool-type lifecycle and the repo-file detection signals below are this repo's synthesis, which is why `convergence: single-source` and `status: EMERGING`. Adopting the register or the signals as infrastructure needs an owner exception under the rule in [AUDIT-CONTEXT.md](../AUDIT-CONTEXT.md); the owner granted one for the `tool-*` audit signals on 2026-11-03 ([DECISIONS.md § Owner Exceptions](../DECISIONS.md#owner-exceptions)), which does not change this doc's `convergence:` value.

## Purpose

This doc answers one question for a project or a team: before an AI coding agent is allowed to use a new tool, and for as long as it keeps using it, what should someone check, how deeply, who decides, and how would an audit of the repository notice when that check was skipped or has gone stale. It covers skills, MCP servers (local and remote), plugins, hooks, subagent definitions, slash commands, connectors and remote MCP with OAuth, CLIs the agent is told to call, and browser or computer-use extensions, and it gives a rule for classifying whatever ships next.

It points to first-party docs for every mechanism rather than restating them. The material that already lives elsewhere in this repo is linked, not repeated: the OWASP MCP attack table and defense-in-depth checklist in [mcp-patterns.md](mcp-patterns.md#owasp-mcp-security-framework), the ClawHub skill-marketplace figures in [mcp-patterns.md § Skill Supply Chain Risk](mcp-patterns.md#skill-supply-chain-risk), the before-installing checklist and version-pinning governance in [plugins-and-extensions.md](plugins-and-extensions.md#evaluating-third-party-plugins-and-skills), and `hard_deny`, `onFailure: "block"` and the auto-mode bypass in [safety-and-sandboxing.md](safety-and-sandboxing.md#the-permission-stack-evaluated).

## The Core Problem

Every tool type on the list above is some mix of two things: code that runs on the machine, and text that enters the model's context as instructions. Anthropic states the first half plainly for plugins, "A Claude Code plugin you install can execute arbitrary code on your machine with your user privileges" (Tier A, [plugin security](https://code.claude.com/docs/en/plugins/security)), and the incident record shows the second half is just as exploitable, because a tool description or a SKILL.md is read by the model whether or not a human ever reads it.

Three properties make a one-time review insufficient, and they are the reason this doc is organized as a lifecycle instead of a checklist:

- **The tool can change after approval.** A plugin's marketplace can auto-update it, so "the files you reviewed can change on disk" (Tier A, plugin security). An MCP server can change its tool list mid-session with `list_changed`, and Claude Code refreshes it without reconnecting (Tier A, [MCP docs](https://code.claude.com/docs/en/mcp)). Invariant Labs named this the *rug pull*: "a malicious server can change the tool description after the client has already approved it" (Tier B, [Invariant 2025-04-01](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)).
- **Some of it runs before anyone approves anything.** Tool descriptions enter context at connection, so a malicious server can "execute attacks before any tool is even invoked" (Tier B, [Trail of Bits, line jumping, 2025-04-21](https://blog.trailofbits.com/2025/04/21/jumping-the-line-how-mcp-servers-can-attack-you-before-you-ever-use-them/)). In a `claude -p` or SDK run in an untrusted folder, a repository's settings-file hooks, `env` block, `apiKeyHelper`, a project skill's hooks and `allowed-tools`, and its `.mcp.json` servers are all used without a trust prompt (Tier A, [permissions: What runs before you trust a folder](https://code.claude.com/docs/en/permissions#what-runs-before-you-trust-a-folder)).
- **A cloned repository is itself a tool channel.** Check Point showed three ways a repo's own `.claude/settings.json` reached a collaborator's machine before trust: hooks that ran shell commands (GHSA-ph6w-f82w-28w6), `enableAllProjectMcpServers` starting `.mcp.json` servers before the trust dialog (CVE-2025-59536), and an `ANTHROPIC_BASE_URL` override that sent the API key to an attacker (CVE-2026-21852), all patched by 2025-12-28 (Tier B, [Check Point Research, 2026-02-25](https://research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files-cve-2025-59536/)).

The measured incidents that shape the method, one line each:

| Incident | What it teaches | Tier |
|---|---|---|
| `postmark-mcp` npm package: fifteen clean versions, then 1.0.16 BCC'd every sent email to an attacker; ~1,500 weekly downloads | A version range or `@latest` installs the backdoor automatically; trust earned on old versions transfers to new ones | C ([The Register, 2025-09-29](https://www.theregister.com/2025/09/29/postmark_mcp_server_code_hijacked/), quoting Postmark; Koi Security primary not reachable) |
| Amazon Q Developer for VS Code 1.84.0 shipped injected code from a repo commit made with "an inappropriately scoped GitHub token" (CVE-2025-8217) | A first-party, well-known extension can still ship a poisoned update; updates are a re-review trigger | A ([AWS-2025-015](https://aws.amazon.com/security/security-bulletins/AWS-2025-015/)) |
| Nx `s1ngularity`: malicious `postinstall` with an agent prompt that inventoried the filesystem | A CLI or package the agent is told to install can turn the agent's own tooling against the machine | A ([GHSA-cxm3-wv7p-598c](https://github.com/nrwl/nx/security/advisories/GHSA-cxm3-wv7p-598c)); the claim that it drove installed AI CLIs is C |
| `mcp-remote` 0.0.5–0.1.15: OS command injection from a malicious server's `authorization_endpoint`, CVSS 9.6 (CVE-2025-6514) | For remote MCP the local proxy and the OAuth flow are part of the attack surface | B ([JFrog](https://research.jfrog.com/vulnerabilities/mcp-remote-command-injection-rce-jfsa-2025-001290844/)) |
| Official GitHub MCP server hijacked through a public issue into leaking private-repo data; "not a flaw in the GitHub MCP server code itself" | Vetting the server does not vet what it returns; tool output is untrusted input | B ([Invariant, 2025-05-26](https://invariantlabs.ai/blog/mcp-github-vulnerability)) |
| ToxicSkills: 76 confirmed malicious payloads among 3,984 public skills; publishing needs "A `SKILL.md` Markdown file and a GitHub account that's one week old. No code signing. No security review." | Skill marketplaces have no supply-chain gate by default | B ([Snyk, 2026-02-05 corpus](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/), vendor) |
| Hidden Unicode Tag instructions in a SKILL.md, "a Skills supply chain backdoor that survives human review" | Reading the file is necessary and not sufficient; scan for invisible code points | B ([Rehberger, 2026-02-11](https://embracethered.com/blog/posts/2026/scary-agent-skills)) |

## Step 1: Risk-Tiered Intake

Tier each tool by what it can reach, not by what it is called or where it was listed. Willison's lethal trifecta is the shortest useful test: a tool set that combines "Access to your private data", "Exposure to untrusted content" and "The ability to externally communicate" can exfiltrate, and MCP "encourages users to mix and match tools from different sources", which is how the three get assembled without anyone choosing it (Tier B, [Willison, 2025-06-16](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)). So the tier attaches to the session's combined reach as well as to each tool.

| Reach tier | What the tool can do | Review depth |
|---|---|---|
| **R0** Instructions only | Text that enters context; no code, no new tools, no grants (a plain skill or command with no `allowed-tools`, no `` !`cmd` ``, no scripts) | Read every line, scan for invisible characters, check the description for over-broad triggering |
| **R1** Local read | Reads files or local state inside the project | R0 plus confirm read scope and that results cannot leave the machine through another tool |
| **R2** Local execute or write | Runs a process (stdio MCP server, hook, bundled script, CLI, plugin `bin/`) or writes files | R1 plus read the code or the exact command, pin it, check it runs outside the sandbox (most of these do) |
| **R3** Credentials, egress or remote write | Holds a token, makes network calls, or writes to a remote system (remote MCP with OAuth, connectors, a hook that `curl`s, a CLI with cloud credentials) | R2 plus scope the credential, confirm the token audience, decide the egress allowlist, name a revocation path |
| **R4** Acts as the user in a live interface | Browser or computer use, or anything that can click, submit, purchase or publish | R3 plus site or app allowlists, action confirmations, and a separate profile; Anthropic's own browser red-team still saw 11.2% attack success with mitigations on (Tier A, [Claude for Chrome, 2025-08-25](https://claude.com/blog/claude-for-chrome)) |

What to read for each tool type, and the first-party aid that already does part of the job:

| Tool type | Typical reach | What to read before approving | First-party aid (Tier A) |
|---|---|---|---|
| **Skill** (SKILL.md + `scripts/` + references) | R0–R2; R3 if a script calls out | Full SKILL.md including frontmatter; every bundled script; any `` !`cmd` `` line, which runs before the content reaches Claude and never prompts; `allowed-tools`, which **grants** tools without a prompt and "does not restrict" anything ([skills docs](https://code.claude.com/docs/en/skills)); `hooks` in frontmatter, which keep running for the rest of the session once invoked ([hooks docs](https://code.claude.com/docs/en/hooks)) | `/skill-doctor` (added v2.1.261) for unused skills and context cost; `disableSkillShellExecution` (v2.1.91); `disallowed-tools` |
| **MCP server, local stdio** | R2–R3 | The exact `command` + `args`; the package source at the pinned version; its own dependencies; the full `tools/list` output (names, descriptions, schemas), since that is what the model reads | Project `.mcp.json` approval prompt (interactive only); `claude mcp list`; `/doctor` warnings on duplicate scopes |
| **MCP server, remote HTTP / connector** | R3 | Who operates the endpoint; the OAuth scopes requested; whether tokens are audience-bound (the spec requires "MCP servers MUST NOT accept or transit any other tokens", Tier A, [MCP authorization, 2026-07-28](https://modelcontextprotocol.io/specification/latest/basic/authorization)); the `tools/list` output; for a local proxy such as `mcp-remote`, its version | `oauth.scopes` pinning; "Clear authentication" in `/mcp`; Anthropic "reviews connectors against its listing criteria ... but doesn't security-audit or manage any MCP server" ([managed MCP](https://code.claude.com/docs/en/managed-mcp)) |
| **Plugin** (any mix of skills, commands, agents, hooks, monitors, MCP/LSP servers, `bin/`, mods) | R2–R4, the union of its parts | Each part by its own row; `hooks/hooks.json`, `.mcp.json` and every file in `bin/`, because the install pane "shows that a hook exists but not what it runs" ([plugin security](https://code.claude.com/docs/en/plugins/security)); the marketplace's source; whether auto-update is on | `/plugin` **Will install** pane; `claude --plugin-dir <dir> plugin details <name>` for a pre-install `Component inventory`; `claude plugin validate`; `claude plugin eval` (v2.1.269) for behavior with and without the plugin |
| **Hook** (settings, plugin, skill or agent frontmatter) | R2–R3 | The exact command; anything it downloads or sends; whether it fails open (default on most events) or sets `onFailure: "block"` (v2.1.295) | `/hooks` (a read-only browser); `allowManagedHooksOnly`; `allowedHttpHookUrls`; `disableAllHooks` |
| **Subagent definition** (`.claude/agents/*.md`) | Inherits the parent's reach unless narrowed | `tools` (omitted means "Inherits every tool available to subagents"), `disallowedTools`, inline `mcpServers`, `hooks`, `permissionMode`, `skills` preloads ([subagents](https://code.claude.com/docs/en/sub-agents)) | Plugin subagents ignore `hooks`, `mcpServers` and `permissionMode`; project agents' inline servers and hooks wait for folder trust |
| **Slash command** | R0–R2 | Same as a skill: the body, `allowed-tools`, `` !`cmd` `` lines | `disableSkillShellExecution` also covers commands |
| **CLI the agent is told to call** (named in CLAUDE.md, a skill, or an allow rule) | R2–R3 | How it is installed (`npx`, `curl \| sh`, a package manager with a lockfile), its version, what credentials it picks up from the environment, and which `permissions.allow` rules let it run unprompted | Permission rules and the [sandbox](https://code.claude.com/docs/en/sandboxing) apply, because a CLI runs through the Bash tool |
| **Browser / computer-use extension** | R4 | Which sites or apps it may act on; whether it uses the user's logged-in profile; which actions require confirmation | Site-level permissions and action confirmations ([Claude for Chrome](https://claude.com/blog/claude-for-chrome)); `managed-mcp.json` blocks the built-in Chrome server unless `allowClaudeInChromeWithManagedMcp` is set (v2.1.282) |

**For whatever ships next.** Classify a new tool type by five questions before looking for a row: Does it run code, and inside or outside the sandbox? Does its text enter context, and can it change after approval? Does it hold or forward a credential? Can it reach the network or a live interface? Can a repository or a marketplace deliver it without a fresh human decision? Each yes moves it up a tier, and the last one also means it needs a repo-file detection signal (below). Plugin *monitors* and *mods* are recent examples that this rule places at R2 or above, since both run with user permissions outside the sandbox (Tier A, plugin security).

## Step 2: A Decision With a Named Owner

A tool decision should be written down where the next reviewer will find it, with a person attached, because the re-review triggers in Step 7 need someone to fire them. NIST's Generative AI Profile asks organizations to "Inventory all third-party entities with access to organizational content and establish approved GAI technology and service provider lists" (Tier A, [NIST AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf), GV-6.1-007), and the decision record is the smallest local form of that.

A record that is enough to act on later:

| Field | Example |
|---|---|
| Tool, type, source | `postgres-readonly` MCP server, stdio, `npm:@example/pg-mcp` |
| Pinned identity | `@example/pg-mcp@2.4.1`, plus a hash of its `tools/list` output at approval |
| Reach tier and why | R1: read-only role, no network beyond the DB host |
| Configuration granted | `mcp__pg__query` allowed; write tools denied; DB role `readonly_agent` |
| Decision, owner, date | Approved by the repo maintainer, 2026-11-03 |
| Re-review triggers | Version bump, tool list change, new scope, owner change, 90 days |
| Removal steps | Remove from `.mcp.json`, revoke DB role, delete cached package |

Where it lives matters less than that it is versioned and near the configuration it describes; a table in the repo next to `.mcp.json` works for a small team. For an organization, managed settings turn the decision into enforcement: `strictKnownMarketplaces` and `blockedMarketplaces` for plugin sources, managed `enabledPlugins` to force-enable or block a plugin, and `allowedMcpServers` with `allowManagedMcpServersOnly: true` for MCP (Tier A, [plugins for your organization](https://code.claude.com/docs/en/plugins/org), [managed MCP](https://code.claude.com/docs/en/managed-mcp)). Two first-party caveats to carry into the decision: a `serverName` entry "is not a security control" because the user picks the name, so allowlist by `serverUrl` or `serverCommand`; and managed settings cannot restrict entries inside an allowed marketplace except one plugin at a time with `enabledPlugins: false` (Tier A, same pages).

## Step 3: Pinning and Provenance

Pin to the most immutable identifier the source supports, and know what a listing does and does not prove.

| Source | Pin with | Notes |
|---|---|---|
| Plugin from git (`github`, `url`, `git-subdir`) | `sha` (40-char commit), optionally `ref` | When both are set Claude Code checks out `sha`. The `claude-community` catalog pins nearly every entry to a commit and refuses a different one (Tier A, [marketplace reference](https://code.claude.com/docs/en/plugins/marketplace-reference), plugin security) |
| Plugin `archive` | `sha256` | A mismatch refuses the install (v2.1.224+) |
| Plugin `npm` source | exact `version` | Omitting `version` fetches `latest`; install scripts never run (Tier A, marketplace reference) |
| Plugin `command` source | `--accept-command <sha256>` on install/update (v2.1.271) | Re-runs once per session; `DISABLE_AUTOUPDATER` does not cover it; `disableCommandPluginSources` blocks the type |
| MCP server via `npx` / `uvx` / `bunx` | Exact version in the args (`pkg@2.4.1`), never `@latest` or a bare name | `postmark-mcp` is the case for exact pins (Tier C). For npm packages, `npm audit signatures` verifies Sigstore-backed provenance, which "does not mean a package is free of malicious code" (Tier A, [npm provenance docs](https://docs.npmjs.com/generating-provenance-statements)) |
| MCP server as a container | Image digest (`@sha256:...`), not a tag | Same reasoning as above |
| Remote MCP server | The URL, the OAuth scopes (`oauth.scopes`), and a snapshot of `tools/list` | The code cannot be pinned, so the description snapshot is the only change detector you control |
| Skill or command copied into the repo | The commit you copied from, recorded in the file or the decision record | Vendored text does not update on its own, which is a feature here |
| CLI | Lockfile or exact version; avoid `curl \| sh` installers in agent instructions | Permission rules apply when it runs through Bash |

**Provenance signals and their limits.** The official MCP Registry verifies namespace ownership through GitHub, DNS or HTTP challenges and "delegates security scanning" to package registries and aggregators; it is "currently in preview" (Tier A, [MCP Registry](https://modelcontextprotocol.io/registry/about)). Anthropic reserves official and community marketplace names for `github.com/anthropics/` sources, so a third-party marketplace cannot pass itself off as one, but "A marketplace's name tells you who publishes the catalog, not what each plugin in it does" (Tier A, plugin security). For the tool's own source repository, OpenSSF Scorecard's `Pinned-Dependencies`, `Dangerous-Workflow`, `Token-Permissions`, `Signed-Releases` and `Maintained` checks are relevant (Tier A, [ossf/scorecard](https://github.com/ossf/scorecard)); the Amazon Q and Nx incidents both began with an over-scoped CI token, which is what `Token-Permissions` and `Dangerous-Workflow` look for. SLSA v1.2's Build and Source tracks apply to how a tool was built (Tier A, [slsa.dev](https://slsa.dev/spec/)), though I found no SLSA profile or signing scheme specific to skills, plugins or MCP servers.

**Tool-description pinning is not first-party yet.** Invariant and Trail of Bits both recommend hashing tool descriptions at approval and alerting when they change (Tier B, R1/R2 in the evidence log), and the MCP spec says clients "MUST consider tool annotations to be untrusted unless they come from trusted servers" (Tier A, [MCP tools](https://modelcontextprotocol.io/specification/latest/server/tools)). I found no Claude Code setting or changelog entry, through v2.1.317, that snapshots a server's tool list and warns on change. Until one exists, the snapshot is a manual step: save the `tools/list` output (or the `/mcp` tool view) with the decision record and diff it at each re-review.

## Step 4: Least-Privilege Configuration

Configure each tool to the narrowest tier that still does the job, and prefer controls that subtract over controls that grant.

- **Skills and commands.** Treat `allowed-tools` as a grant to review, not a restriction; use `disallowed-tools` to remove tools while a skill runs. Workspace trust "never gates a skill's `allowed-tools` in any session" (Tier A, permissions). Set `disableSkillShellExecution: true` where skills have no need for `` !`cmd` `` (Tier A, skills).
- **Subagents.** Give every custom agent an explicit `tools` list; an omitted list inherits everything the session has, MCP tools included (Tier A, subagents). Use `disallowedTools` for the dangerous remainder.
- **MCP tools.** Allow per tool (`mcp__<server>__<tool>`) rather than per server where the server mixes read and write tools; deny rules can use `mcp__*` globs, allow rules need a literal server segment (Tier A, permissions). Request the minimal OAuth scope set; the spec's list of common mistakes includes "Using wildcard or omnibus scopes" and "Silent scope semantic changes without versioning" (Tier A, [MCP security best practices](https://modelcontextprotocol.io/specification/latest/basic/security_best_practices)).
- **Repository-borne configuration.** For `claude -p` in a repository you did not write, Anthropic lists `--setting-sources user`, `--bare`, `--settings '{"disableAllHooks": true}'` and `disabledMcpjsonServers` (Tier A, permissions). Note that a project's `"disableAllHooks": false` overrides a user-level `true` (Tier A, hooks).
- **Organization lockdown.** `strictPluginOnlyCustomization` blocks skills, agents, hooks and MCP servers that do not come from a plugin, managed settings or built-ins; `disableSideloadFlags` closes `--plugin-dir`, `--plugin-url`, `--agents` and `CLAUDE_CODE_PLUGIN_DIRS` (Tier A, plugins for your organization). Policy semantics have moved between releases, for example v2.1.259 and v2.1.305 each changed which `managed-mcp.json` servers `allowedMcpServers` filters, so a server an allowlist used to exclude "now loads on upgrade" (Tier A, changelog). Re-read the policy pages when the CLI version moves.

## Step 5: Sandboxing and Egress

The most important first-party fact for this step is a boundary: "Claude Code runs hooks, monitors, MCP servers, LSP servers, and the processes a mod starts outside the sandbox", while permission rules and the sandbox cover Claude's tool calls (Tier A, plugin security). So the Bash sandbox and `network.allowedDomains` described in [safety-and-sandboxing.md](safety-and-sandboxing.md#the-sandbox-delta-when-a-workflow-leaves-claude-code-added-2026-08-19) contain a CLI the agent runs through Bash, and an executable in a plugin's `bin/` when Claude calls it, but they do not contain an R2+ MCP server or hook. For those:

- Run stdio MCP servers that reach R2 or above inside a container or VM with only the mounts and network they need; the MCP spec says clients "SHOULD" launch local servers "with restricted access to the file system, network, and other system resources" (Tier A, MCP security best practices). Anthropic's own guidance for untrusted content includes "Use virtual machines (VMs) to run scripts and make tool calls" (Tier A, [security](https://code.claude.com/docs/en/security)).
- For anything that performs OAuth discovery on a server, block private ranges including `169.254.0.0/16` and route through an egress proxy; the spec names SSRF against cloud metadata as a specific risk (Tier A, MCP security best practices).
- For R4 browser use, use a separate browser profile without the user's everyday sessions, plus site allowlists and action confirmations (Tier A, Claude for Chrome).
- For the whole session, the trifecta test from Step 1 decides whether egress needs an allowlist at all: if private data and untrusted content are both in reach, it does.

## Step 6: What to Log

Logging serves two later questions, which tool was present when something happened and whether it changed since approval, so log identity and change, not only calls.

- **Install and load events.** OpenTelemetry `claude_code.plugin_installed` and `claude_code.plugin_loaded`; set `OTEL_LOG_TOOL_DETAILS=1` or third-party plugin names are redacted to `third-party`, and the same variable adds MCP server and tool names to tool events (Tier A, plugins for your organization, managed MCP).
- **Configuration changes.** A `ConfigChange` hook fires for user, project, local and skills changes and can block all but policy changes with exit code 2; Anthropic suggests it to "Audit or block settings changes during sessions" (Tier A, hooks, security).
- **Tool use.** The MCP spec says clients "SHOULD ... Log tool usage for audit purposes" and "Validate tool results before passing to LLM" (Tier A, MCP tools); OWASP lists "Lack of Audit and Telemetry" as MCP08:2025 (Tier A, [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/), beta).
- **The approval snapshot.** Store the pinned identity and the `tools/list` snapshot from Step 3 with the decision record, so a re-review is a diff.

## Step 7: Re-Review Triggers

| Trigger | How you notice | Why it matters |
|---|---|---|
| Version or commit changes (manual bump, marketplace auto-update, a range resolving to a new release) | Diff of `.mcp.json`, `enabledPlugins`, lockfiles; `/plugin` update notices; disable auto-update per marketplace with `autoUpdate: false` where review must come first | `postmark-mcp` 1.0.16 and Amazon Q 1.84.0 were both updates to tools users already trusted |
| Tool list or description changes | Diff against the approval snapshot; `list_changed` refreshes happen silently | Rug pull and line jumping (Tier B, R1/R2) |
| New permission, scope or component | A plugin gains hooks, `bin/` or an MCP server; a skill gains `allowed-tools` or `` !`cmd` ``; an OAuth consent screen asks for more | The reach tier changed, so the review depth from Step 1 applies again |
| Source or ownership changes | Marketplace source moves; package maintainer or publisher changes; repository transfer | Provenance from Step 3 no longer holds |
| Claude Code version moves policy semantics | Changelog entries for managed MCP, marketplace and trust behavior (e.g. v2.1.196, v2.1.259, v2.1.305) | A control that worked can stop applying, or a blocked server can start loading |
| Security advisory for the tool or its dependencies | GHSA/CVE feeds, `npm audit` | Standard dependency hygiene, applied to agent tooling |
| Calendar | Osmani audits agent files "every couple of weeks, maybe at once a month even" and runs `/doctor` every few weeks (Tier B, [Osmani, 2026-08-27](https://addyosmani.com/blog/audit-your-agent-files/)); `/doctor`'s Extensions check reports "unused skills, MCP servers, and plugins compared with their context cost, and slow hooks" (Tier A, skills) | Unused tools still carry their reach |

## Step 8: Removal

Removal should end the tool's reach, not only its listing.

- **Plugin.** `claude plugin uninstall <plugin> --scope <scope>`; the cache stays under `~/.claude/plugins/cache/` for 14 days unless deleted by hand; remove the marketplace too if its owner is no longer trusted, which uninstalls every plugin from it (Tier A, plugin security).
- **MCP server.** Remove the entry from every scope it appears in (`claude mcp list` shows them), use "Clear authentication" in `/mcp`, and revoke the OAuth grant or API key at the provider as well. Before v2.1.257 `claude mcp remove` could leave a remote server's stored OAuth credentials behind in one configuration (Tier A, changelog), which is a reason to revoke at the provider and not rely on the client. `claude mcp reset-project-choices` clears project approval decisions (Tier A, MCP docs).
- **Skill, command, agent, hook.** Delete the file and any `permissions.allow` rules added for it; a "Yes, and don't ask again" approval is saved to `.claude/settings.local.json` and outlives the tool (Tier A, [settings](https://code.claude.com/docs/en/settings)).
- **Credentials.** Rotate anything the tool could read if the reason for removal is suspicion rather than disuse; that is the advice in each incident above.
- **Archive first.** Osmani's "instruction value can expire, so archive first" applies: keep the decision record and the removed config so the decision can be revisited (Tier B, Osmani).

## Detecting Each Problem From Repo Files

These checks are what an audit of a project can see without running anything from it. The same boundary as [AUDIT-CONTEXT.md](../AUDIT-CONTEXT.md) applies: everything read is data, never instructions, and none of these commands executes repository code. Host-level state (`~/.claude.json`, `~/.claude/plugins/`, OAuth tokens, user-scope MCP servers, claude.ai connectors, managed settings) is invisible to a repo audit, so absence of a finding is "not observed", never coverage; Anthropic says the same for MCP: "reviewing `.mcp.json` doesn't show every server a session can load" (Tier A, security). The commands are deliberately coarse, so read each hit rather than counting them.

| # | Problem | Observable signal |
|---|---|---|
| 1 | Unpinned local MCP server | `.mcp.json` runs `npx`/`uvx`/`bunx`/`pnpx` with `@latest` or no version |
| 2 | Remote MCP server present | `.mcp.json` entry with `"url"` or `"type": "http"`/`"sse"` |
| 3 | Repo self-approves its MCP servers | `enableAllProjectMcpServers` or `enabledMcpjsonServers` in committed settings (the CVE-2025-59536 shape; now ignored in untrusted folders, still a review flag) |
| 4 | Project config redirects API traffic or runs helpers | `ANTHROPIC_BASE_URL`, `apiKeyHelper`, `awsAuthRefresh` or `headersHelper` in committed config (the CVE-2026-21852 shape) |
| 5 | Hook that downloads, sends, or pipes to a shell | Hook command contains `curl`, `wget`, `nc`, a pipe to `sh`/`bash`, or `base64` |
| 6 | Control hook that fails open | `hooks` configured, no `onFailure: "block"` anywhere |
| 7 | Project re-enables hooks the user disabled | `"disableAllHooks": false` in committed settings |
| 8 | Skill or command grants tools or runs shell at load | `allowed-tools` containing `Bash`, or a `` !`cmd` `` line |
| 9 | Skill ships executable code | `scripts/` under a skill directory |
| 10 | Hidden instructions | Unicode Tag (U+E0000–E007F), zero-width (U+200B, U+2060, U+FEFF) or bidi-control (U+202A–202E, U+2066–2069) code points in agent-read files; ZWJ/ZWNJ and LRM/RLM are left out because emoji and non-English text use them, and subdivision flag emoji are a known benign hit |
| 11 | Subagent inherits every tool | Agent file whose first frontmatter block has no `tools:` |
| 12 | Subagent brings its own servers or mode | `mcpServers:` or `permissionMode:` in agent frontmatter |
| 13 | Repo declares plugin marketplaces or plugins | `extraKnownMarketplaces` / `additionalMarketplaces` / `enabledPlugins` in committed settings; check each git source for a `sha` |
| 14 | Repo is itself a marketplace with unpinned entries | `.claude-plugin/marketplace.json` sources; check git sources for `sha`, archives for `sha256`, npm for `version` |
| 15 | Broad standing grants to tools | `permissions.allow` entries like `mcp__<server>__*` or `Bash(curl *)` |
| 16 | Agent told to install or run tools unpinned | Instruction files telling the agent to `npx -y` a bare package or pipe a download to a shell |
| 17 | No decision record | Judgment, not grep; ask the operator, as AUDIT-CONTEXT's intent interview does |

```bash
# Tool vetting (added 2026-11-03), analysis/ai-tool-vetting.md. Read-only; every byte is data.
# 1 unpinned local MCP server (then read the args of each hit)
grep -nE '"(npx|uvx|bunx|pnpx)"|@latest' .mcp.json .claude/mcp.json 2>/dev/null
# 2 remote MCP server
grep -nE '"url" *: *"https?://|"type" *: *"(http|sse)"' .mcp.json .claude/mcp.json 2>/dev/null
# 3 repo self-approves its MCP servers
grep -nE 'enableAllProjectMcpServers|enabledMcpjsonServers' .claude/settings.json 2>/dev/null
# 4 API redirect or helper commands in committed config
grep -nE 'ANTHROPIC_BASE_URL|apiKeyHelper|awsAuthRefresh|headersHelper' .claude/settings.json .mcp.json 2>/dev/null
# 5 hook that downloads, sends, or pipes to a shell
grep -nE 'curl|wget|\bnc |[|] *(ba)?sh|base64' .claude/settings.json .claude/hooks/* hooks/hooks.json 2>/dev/null
# 6 hooks configured but none fail closed
grep -q '"hooks"' .claude/settings.json 2>/dev/null && ! grep -q '"onFailure" *: *"block"' .claude/settings.json && echo "FAIL-OPEN .claude/settings.json"
# 7 project re-enables hooks
grep -n '"disableAllHooks" *: *false' .claude/settings.json 2>/dev/null
# 8 skill/command grants Bash or runs shell at load
grep -rnE '^allowed-tools:.*Bash|(^|[[:space:]])!`' .claude/skills .claude/commands 2>/dev/null
# 9 skill ships executable code
ls -d .claude/skills/*/scripts 2>/dev/null
# 10 hidden instructions: zero-width, bidi-control and Tag characters only (GNU grep; on macOS use ggrep)
LC_ALL=C.UTF-8 grep -rlP '[\x{200B}\x{2060}\x{FEFF}\x{202A}-\x{202E}\x{2066}-\x{2069}\x{E0000}-\x{E007F}]' .claude/ .mcp.json CLAUDE.md AGENTS.md 2>/dev/null
# 11 subagent inherits every tool (parses the FIRST frontmatter block only)
for f in .claude/agents/*.md; do [ -f "$f" ] || continue; \
  awk '/^---[[:space:]]*$/{n++; if(n==2) exit; next} n==1' "$f" | grep -qE '^tools:' || echo "INHERITS-ALL $f"; done
# 12 subagent brings its own servers or permission mode
grep -nE '^(mcpServers|permissionMode):' .claude/agents/*.md 2>/dev/null
# 13 repo declares marketplaces or plugins
grep -nE 'extraKnownMarketplaces|additionalMarketplaces|enabledPlugins' .claude/settings.json 2>/dev/null
# 14 repo is a marketplace: list sources, then check each for sha / sha256 / version
grep -nE '"source" *: *"(github|url|git-subdir|archive|npm|command)"|"(sha|sha256|version)"' .claude-plugin/marketplace.json 2>/dev/null
# 15 broad standing grants
grep -nE '"mcp__[^"]*__\*"|"Bash\((curl|wget|npx|uvx)' .claude/settings.json .claude/settings.local.json 2>/dev/null
# 16 instructions to install or run tools unpinned
grep -nE 'npx -y [^@ ]+( |$)|curl[^|]*[|] *(ba)?sh' CLAUDE.md .claude/CLAUDE.md AGENTS.md .claude/skills/*/SKILL.md 2>/dev/null
```

Every command was run against planted fixtures (14 on 2026-11-03, after the rest), with clean negative checks for 5, 15 and 16 (see the evidence log). Command 10 was narrowed on 2026-11-03 by owner ruling and re-tested: it hit planted Tag, zero-width, bidi-override and bidi-isolate fixtures and did not hit a clean file of emoji (including ZWJ family and rainbow-flag sequences), Persian text with ZWNJ, Hindi with ZWJ, Hebrew with RLM/LRM, or CJK text; the one benign hit left is a subdivision flag (England), which is built from Tag characters. Command 5 also hits `curl` inside allow rules, which is noise to read past rather than a bug.

These rows are routing signals in [AUDIT-CONTEXT.md](../AUDIT-CONTEXT.md) § Fetch on Tool Configuration since 2026-11-03: rows 1–2 are `tool-mcp-unpinned` and `tool-mcp-remote`, 3 `tool-repo-self-approval`, 4 `tool-project-env-redirect`, 5 `tool-hook-network`, 6–7 `tool-hook-fail-open`, 8–9 `tool-skill-grants-tools`, 10 `tool-hidden-unicode`, 11–12 `tool-agent-inherits-all`, 13–14 `tool-plugin-marketplace-declared` and 15 `tool-broad-grants`, with row 16 dropped as too fuzzy to report on and row 17 left to the intent interview. **Weights**: a PROBLEM signal (self-approval, env redirect, unpinned MCP, inherits-all agent, fail-open hook, broad grants) is reported as a finding with a recommendation, a REVIEW signal (skill grants, network hook with its command shown, hidden Unicode) is listed for a human to read because it is often intended, and an INVENTORY signal (remote MCP, declared marketplaces) is only counted.

## Counter-Evidence / What This Does Not Mean

Vetting the tool does not vet what the tool returns. The GitHub MCP case used the official server working as designed, and Invariant's conclusion was that "server-side patches alone cannot fix it" (Tier B, R3). Most of the injection risk in a well-vetted setup arrives through tool output and fetched content, which is why the trifecta test and egress limits in Steps 1 and 5 carry as much weight as the intake review, and why model-level injection robustness, which [safety-and-sandboxing.md](safety-and-sandboxing.md#model-level-prompt-injection-robustness-across-model-versions) tracks per model, still matters after every tool here is approved.

Human review is also weaker than the method assumes. Trail of Bits calls invocation-time approval "human-as-the-rubber-stamp" oversight (Tier B, R2), Rehberger's Unicode Tag payload is invisible to a careful reader by design (Tier B, R12), and Snyk's malicious samples used password-protected ZIPs and base64 to defeat scanners (Tier B, R11). Reading every line is necessary and not sufficient, which is why pinning, sandboxing and removal are in the method as controls that do not depend on the reviewer catching the problem.

The cost is real for a solo developer with two MCP servers, and the reach tiers exist so that an R0 skill gets a five-minute read and not a procurement review. I think the defensible minimum for a single developer is Steps 3 (exact pins), 5 (keep R2+ servers out of the host where practical) and 8 (revoke on removal), with the written record from Step 2 earning its place once a second person shares the configuration.

**Implication**: treat this as a method for bounding what a bad tool can do and for noticing change, not as a way to certify a tool as safe. The incident figures here are mostly vendor-measured (Invariant, Snyk, Check Point, JFrog, Koi all sell security products), and the strongest evidence is the first-party documentation of what each mechanism can reach.

**Absorption note.** Much of this is moving first-party. Plugin trust tiers, the pre-install `Component inventory`, `claude plugin eval`, marketplace allowlists, managed MCP allowlists and `onFailure: "block"` all shipped in 2026 releases. If Claude Code adds tool-description pinning with change alerts, and an install-time reach summary for skills and MCP servers comparable to the plugin **Will install** pane, Steps 1 and 3 should shrink to pointers under the retirement rules in [CONTRIBUTING.md](../CONTRIBUTING.md#retiring-a-doc-replacement-readiness).

## Gaps

- **Gap: tool-description change detection.** No first-party Claude Code mechanism snapshots an MCP server's tool list at approval and alerts on change, as of v2.1.317. **Needs**: a shipped setting or changelog entry, or a verified read of a third-party tool's primary docs (Invariant/Snyk `mcp-scan`, Trail of Bits `mcp-context-protector`) with a test showing it catches a changed description.
- **Gap: reach-tier boundaries are judgment.** R0–R4 are an ordering by capability, not a calibrated risk score, and nothing here measures whether tiered review catches more than flat review. **Needs**: a comparison over a labeled set of benign and malicious tools (the ToxicSkills corpus is a candidate) of what each review depth catches.
- **Gap: no signing for skills, plugins or MCP servers.** Git commit pins and `sha256` give integrity, not publisher identity; npm provenance covers only npm-distributed servers. **Needs**: a Sigstore- or SLSA-based scheme adopted by a marketplace or by the MCP Registry after it leaves preview.
- **Gap: standards text not fully read.** The CoSAI MCP white paper (PDF), the OWASP third-party MCP guide body and the OWASP Top 10 for Agentic Applications item list were verified only at the landing-page level. **Needs**: a read of each primary, mapping its controls onto Steps 1–8.
- **Gap: agent-security guidance from NIST.** NIST CAISI's 2026-01-08 RFI on AI agent security is the only confirmed output. **Needs**: the resulting guideline, when published, checked against this method.
- **Gap: browser and computer-use evidence is vendor-only.** The 11.2% figure is Anthropic's own red-team on its own extension. **Needs**: an independent evaluation of browser-agent injection rates with and without site allowlists.

## Related Analysis

- [mcp-patterns.md](mcp-patterns.md) — OWASP MCP Top 10 mapping, defense-in-depth checklist, ClawHub figures, MCP context cost
- [plugins-and-extensions.md](plugins-and-extensions.md) — before-installing checklist, community marketplaces, team version-pinning governance, token economics
- [safety-and-sandboxing.md](safety-and-sandboxing.md) — permission stack, `hard_deny`, moved defaults, sandbox egress, per-model injection robustness
- [secure-code-generation.md](secure-code-generation.md) — CodeGuard, including its MCP rules
- [harness-engineering.md](harness-engineering.md) — when each extension mechanism earns its place at all

## Sources

Full entries, what was verified on each page, and the not-verified list: [research/ai-tool-vetting-sources-2026-11-03.md](../research/ai-tool-vetting-sources-2026-11-03.md). All accessed 2026-11-03.

### Tier A (Primary / Vendor / Standards)

- Claude Code docs: [Plugin security and trust](https://code.claude.com/docs/en/plugins/security), [Manage plugins for your organization](https://code.claude.com/docs/en/plugins/org), [Marketplace reference](https://code.claude.com/docs/en/plugins/marketplace-reference), [Managed MCP](https://code.claude.com/docs/en/managed-mcp), [MCP](https://code.claude.com/docs/en/mcp), [Permissions](https://code.claude.com/docs/en/permissions), [Skills](https://code.claude.com/docs/en/skills), [Hooks](https://code.claude.com/docs/en/hooks), [Subagents](https://code.claude.com/docs/en/sub-agents), [Security](https://code.claude.com/docs/en/security), [Settings](https://code.claude.com/docs/en/settings)
- [Claude Code CHANGELOG.md](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) through v2.1.317
- MCP specification 2026-07-28: [Security Best Practices](https://modelcontextprotocol.io/specification/latest/basic/security_best_practices), [Authorization](https://modelcontextprotocol.io/specification/latest/basic/authorization), [Tools](https://modelcontextprotocol.io/specification/latest/server/tools); [MCP Registry](https://modelcontextprotocol.io/registry/about) (preview)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) (beta); [OWASP Practical Guide for Securely Using Third-Party MCP Servers 1.0](https://genai.owasp.org/resource/cheatsheet-a-practical-guide-for-securely-using-third-party-mcp-servers-1-0/); [OWASP Top 10 for Agentic Applications for 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) (title and date only)
- [CoSAI, Model Context Protocol (MCP) Security](https://www.coalitionforsecureai.org/wp-content/uploads/2026/03/model-context-protocol-security-1.pdf) (press-release facts only)
- [NIST AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) (Value Chain and Component Integration; GV-6.1-007, GV-6.1-009); [NIST CAISI RFI, 2026-01-08](https://www.govinfo.gov/content/pkg/FR-2026-01-08/html/2026-00206.htm)
- [SLSA v1.2](https://slsa.dev/spec/); [OpenSSF Scorecard](https://github.com/ossf/scorecard); [npm provenance](https://docs.npmjs.com/generating-provenance-statements)
- [AWS-2025-015](https://aws.amazon.com/security/security-bulletins/AWS-2025-015/); [Nx GHSA-cxm3-wv7p-598c](https://github.com/nrwl/nx/security/advisories/GHSA-cxm3-wv7p-598c); [Anthropic, Piloting Claude for Chrome](https://claude.com/blog/claude-for-chrome)

### Tier B (Validated / Expert Practitioner; vendor research flagged)

- [Invariant Labs, Tool Poisoning Attacks](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks) (2025-04-01, vendor) and [GitHub MCP exploited](https://invariantlabs.ai/blog/mcp-github-vulnerability) (2025-05-26, vendor)
- [Trail of Bits, Jumping the line](https://blog.trailofbits.com/2025/04/21/jumping-the-line-how-mcp-servers-can-attack-you-before-you-ever-use-them/) (2025-04-21)
- [Simon Willison, The lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) (2025-06-16)
- [JFrog, CVE-2025-6514 mcp-remote](https://research.jfrog.com/vulnerabilities/mcp-remote-command-injection-rce-jfsa-2025-001290844/) (vendor)
- [Check Point Research, Claude Code project files](https://research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files-cve-2025-59536/) (2026-02-25, vendor)
- [Snyk, ToxicSkills](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/) (2026-02, vendor)
- [Johann Rehberger, Scary Agent Skills](https://embracethered.com/blog/posts/2026/scary-agent-skills) (2026-02-11)
- [Addy Osmani, Audit your Agent files](https://addyosmani.com/blog/audit-your-agent-files/) (2026-08-27)

### Tier C (Community / Journalism)

- [The Register, postmark-mcp](https://www.theregister.com/2025/09/29/postmark_mcp_server_code_hijacked/) (2025-09-29, relaying Koi Security and Postmark)
- Secondary reports that the Nx payload drove installed AI CLIs (Kodem and others; see evidence log)

---

*Last updated: 2026-11-03 (owner ruling: the rows above became `tool-*` routing signals with PROBLEM / REVIEW / INVENTORY weights, command 10 narrowed and re-tested, command 14 fixture-tested, row 16 dropped as a signal; `applies-to-signals` extended to match). Prior same-day: 2026-11-03 (new doc; evidence log in research/ai-tool-vetting-sources-2026-11-03.md).*

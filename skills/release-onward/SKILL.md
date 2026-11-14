---
name: release-onward
description: "Manually invoked releases with parallel documentation, code-quality, and release-readiness checks, repository closeout, publication, and version reports."
---

# Release a Version

Read and follow the Onward conventions in `AGENTS.md` and the project's release workflow. If the Onward conventions are missing, tell the user to run `init-onward` first and stop without making changes.

Ask the user when the release goal is unclear, important information is missing, or a significant issue calls for their judgment. Explain the issue, its impact, and the choice needed. Wait for clarification before continuing the affected work; independent checks may continue.

## Prepare

Establish the requested version and channel, the previous relevant release, and the changes to include. Inspect the working trees of the repositories involved, including uncommitted and untracked files. Give the checking agents this scope, the release diff, and the relevant specs, conventions, and configurations.

## Run three checks in parallel

Launch one independent subagent for each role below.

| Agent | Responsibility | Tool examples |
| --- | --- | --- |
| Documentation | Check maintained docs against settled decisions and implementation. Find stale or conflicting claims, duplication, broken references, missing updates, and material ready to archive. Collect the version's major changes and recorded decisions for the report. | markdownlint-cli2 for Markdown style; lychee for links. |
| Code quality | Run lint and type checks. Find unused variables, files, exports, and dependencies; check actual entry points and references before recommending removal. | Ruff for Python; ESLint or Oxlint and Knip for JavaScript/TypeScript; the project's type checker. |
| Release readiness | Run the project's tests and build. Check version metadata, configuration, assets, target-channel prerequisites, and which components need publishing. | The project's test, build, packaging, and platform-validation commands. |

Prefer configured commands and versions; these examples are options, not required dependencies. For Ruff, use `uv run ruff check .` when it is a project dependency, or `uvx ruff check .` for a standalone run. Use the project's package manager for JavaScript/TypeScript tools.

The checking agents run checks and return findings, locations and evidence, commands and results, and any checks they could not complete. They promptly raise questions and significant findings with the main agent. They leave changes to shared project files, commits, and publication to the main agent. Give builds separate output locations where needed to avoid interference.

## Resolve, close out, and publish

Wait for all three reports and keep them distinct. Resolve supported findings, using [tidy-onward](../tidy-onward/SKILL.md) for substantial document reorganization and [code-review-onward](../code-review-onward/SKILL.md) when code review is needed. Update version metadata and release notes, then rerun checks affected by the changes.

Commit release-related code, documentation, configuration, and records in coherent commits. Handle generated and local files according to repository conventions. For genuinely unrelated changes or unclear ownership, ask whether to commit them separately or leave them out. Finish with clean working trees except for explicitly agreed exceptions; achieve cleanliness without discarding work.

Publish the candidate that passed the required checks, following the project's commit, tag, and publishing workflow. Resolve remaining release blockers before publication. Verify the target channel and each published component; if an action's outcome is unclear, inspect remote state before retrying, and stop if it remains unclear.

## Release report

Create or update the release report in the project's report location and commit it. Name the comparison version and revision, covering the whole version delta, including work completed before this release run. If publication is incomplete, record the actual progress and blockers. Include:

- **Version changes:** features, fixes, and significant code, documentation, or configuration changes and their impact.
- **Major changes and decisions:** what changed, the recorded rationale, and consequences such as compatibility or migration requirements where relevant.
- **Release work:** documentation organization, code cleanup, fixes, builds, and deployments actually performed during release preparation and publication.
- **Results:** published components, versions, channels, status and access links or artifacts; the three check results, known issues and unverified items; repository status and agreed exceptions.

Link key claims to relevant specs, decision records, commits, and verification evidence. Give the user the report link and a concise summary.

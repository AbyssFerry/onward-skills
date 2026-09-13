---
name: init-onward
description: Establish project documentation and conventions when setting up a project for Onward.
---

# Init Onward

Give the project a small, usable foundation for future design and implementation. Ground it in the conversation, existing documentation, and repository practices. Ask about unresolved choices only when they affect this setup.

Before proposing the first setup for an existing project, launch parallel, read-only exploration subagents. Start with three areas, adjusting the split to the available material:

- Original documentation: read the documents in scope in full, tracing their purposes, relationships, and current or historical authority. Use indexes to find the source material.
- Code, configuration, and tests: establish what is implemented and which directory, build, and verification practices actually exist.
- Existing conventions: identify engineering and agent rules, their authoritative sources, and unresolved or conflicting choices.

Have each subagent return findings with source references and remaining gaps. Wait for their results, resolve disagreements against the originals, and account for the content and references affected by the setup before drafting the migration and conventions. For an empty project or a later focused update, inspect the available material within that scope.

If the project already has a documentation layout, recommend a migration toward the defaults below. Use a compact before/after table like the example below, identifying source and destination files or sections, the proposed handling, and why. Classify documents by their content and purpose. Show the proposed Onward section and key project-convention changes. Let the user retain the current layout wholly or partly, or choose other locations. Wait for agreement before editing; follow an already confirmed choice without asking again. If there is no existing layout, proceed with the defaults.

Example (adapt to the project's actual files and substantive content):

| Action | Current file or section | Recommended location | Purpose / reason |
|---|---|---|---|
| Move | `docs/product.md` | `spec/product.md` | Product scope and behavior. |
| Keep | `CONTEXT.md` | `CONTEXT.md` | The glossary already uses the default location. |
| Append | `AGENTS.md` | `AGENTS.md` | Add the Onward section, preserving existing rules. |
| Create | — | `spec/conventions.md` | Record confirmed build and test practices. |
| Merge | `docs/auth-api.md`, `docs/error-codes.md` | Authentication and Error codes sections in `spec/api.md` | Combine API contracts, retaining unique content and consolidating duplicates. |
| Split | Product goals section in `docs/overview.md` | `spec/product.md` | Product goals and scope. |
| Split | System design section in `docs/overview.md` | `spec/architecture.md` | System structure and module responsibilities. |
| Keep | Usage section in `docs/overview.md` | Same file and section | Retain the remaining user guide. |

Identify untitled passages by recognizable content. Flag conflicting definitions for agreement.

Append a concise Onward conventions section to `AGENTS.md`, matching its existing heading hierarchy; create the file if absent. If the section already exists, update it without duplicating it. Preserve existing rules and surrounding content; never delete or overwrite the existing file. Keep this section limited to stable Onward conventions: the document responsibilities below, their agreed locations (including retained or customized locations), reading entry points, and maintenance rules. Include defaults for documents not yet needed. Project-specific document maps, extra directories, and temporary locations belong in the project's documentation entry point or index. Keep project versions, stages, progress, and implementation or verification results in the relevant specs, plans, or reports. Product and architecture content belongs in its own specs; initialization explanations belong in the conversation or a report.

Keep established directory, coding, build, and test practices in `spec/conventions.md`, titled “项目约定” (Project conventions), or their existing authoritative documents. Supplement them only where needed, pointing to authoritative configuration for details.

Use these default document responsibilities. Add project-specific spec files or subdirectories as needed, recording their locations and purposes in the project's documentation entry point or index. Create files and directories as substantive content emerges, rather than filling out an empty template set.

| Location | What belongs here |
|---|---|
| `spec/product.md` | Who the product serves, the problem it solves, its scope, core user flows, and expected behavior. |
| `spec/architecture.md` | System and module boundaries, responsibilities, interactions and data flow, and key technical decisions and tradeoffs. |
| `spec/conventions.md` | Project-specific directory, coding, build, and test practices; reference existing authoritative rules and configuration. |
| `CONTEXT.md` at the root | Domain terms and their definitions, without implementation details; use an existing context map to locate multiple contexts. |
| `spec/adr/` | Important architectural decisions and their reasons and tradeoffs, one numbered file per decision. |
| `spec/api.md` | External API contracts: requests, responses, errors, and usage examples, when the project exposes an API. |
| A module's local `spec/` | `design.md` describes internal structure, behavior, dependencies, and design decisions; `interface.md` describes callers' entry points and usage constraints, linking to detailed contracts; `api.md` holds external API contracts and examples when applicable. Co-locate these documents once the module structure exists; during design, a module can start with a single spec. |
| `spec/<change-name>-spec.md` | A change specification, usually written with `to-spec-onward`, recording goals, scope, design, and acceptance criteria. Use a descriptive change name and a status of draft, confirmed, or completed. |
| `spec/plans/<feature-slug>/<NN>-<slug>.md` | One implementation ticket: delivery, spec references, blockers, status, and acceptance criteria for work being planned for execution. |
| `.onward/future/` | Matters to discuss or do later: open questions, deferred designs, future features, and technical improvements. Keep simple items in one document; expand a topic into its own file when useful. |
| `.onward/research/` | Investigations: questions, sources, findings, and limitations that inform decisions. |
| `.onward/visuals/` | Diagrams, visual explanations, and their source files or HTML artifacts. |
| `.onward/reports/` | Review findings, diagnoses, verification results, and actionable handoff suggestions. |
| `.onward/archive/` | Historical snapshots retired from ongoing maintenance, such as completed change specs and superseded documents. Store them directly here. |

Long-lived specs describe the current design and carry no status. Archive a change spec only after implementation, verification, and synchronization of the long-lived specs are complete. Follow the project's choice about tracking `.onward/` in Git. Add no automatic logs.

In the Onward section, tell agents to follow the recorded layout and maintenance rules when implementing or creating, updating, or moving project documents and process artifacts (research, visualizations, reports), and point to applicable project engineering conventions to consult before implementation and verification. Point to the project's documentation entry point or index for the current document map. Explain when to consult the glossary and related ADRs for domain language and design decisions.

Keep this setup limited to the agreed documentation work. Preserve existing Markdown content; move documents only under the approved migration option, carrying it out as part of this initialization and updating affected references and conventions. Save actionable findings and suggestions in `.onward/reports/` when a handoff document would help; a report is not required for every initialization. Code scaffolding and feature implementation belong to later work.

Finish when the Onward section records the agreed, stable Onward conventions, project-specific documents are discoverable through that entry point or index, and references resolve or clearly identify documents to create when needed. The Onward section should remain valid as project stages and extra directories change. Briefly report what was established.

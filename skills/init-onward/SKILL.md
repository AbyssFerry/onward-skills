---
name: init-onward
description: Establish project documentation and conventions when setting up a project for Onward.
---

# Init Onward

Give the project a small, usable foundation for future design and implementation. Ground it in the conversation, existing documentation, and repository practices. Ask about unresolved choices only when they affect this setup.

Inspect existing documentation before changing files. If the project already has a documentation layout, present two concrete setup options: retain it or migrate to the defaults below. Use a shallow annotated file tree or focused path comparison to make each option tangible: what stays, what is created or moved, and why it belongs there. Classify documents by their content and purpose. Wait for the user's choice before editing; follow an already confirmed choice without asking again. If there is no existing layout, proceed with the defaults.

Create or supplement `spec/conventions.md`, titled “项目约定” (Project conventions), with two sections: “Onward 约定” (Onward conventions) for the adopted documentation locations, their brief purposes, and maintenance rules; “项目自身约定” (Project-specific conventions) for established directory, coding, build, and test practices. Keep it a concise rules document, pointing to authoritative configuration for details. Record the chosen layout, including retained locations. Product and architecture content belongs in its own specs; initialization explanations belong in the conversation or a report.

Use these default document responsibilities. Create files and directories as substantive content emerges, rather than filling out an empty template set.

| Location | What belongs here |
|---|---|
| `spec/product.md` | Who the product serves, the problem it solves, its scope, core user flows, and expected behavior. |
| `spec/architecture.md` | System and module boundaries, responsibilities, interactions and data flow, and key technical decisions and tradeoffs. |
| `spec/conventions.md` | The working rules described above: where documents belong and how this project maintains, builds, and tests its work. |
| `spec/api.md` | External API contracts: requests, responses, errors, and usage examples, when the project exposes an API. |
| A module's local `spec/` | That module's responsibilities, interfaces, behavior, constraints, and dependencies. Co-locate it once the module structure exists; during design, a module can start with a single spec. |
| `spec/<change-name>.md` | The goals, scope, design, and acceptance criteria for a specific change. Use a descriptive filename and a status of draft, confirmed, or completed. |
| `spec/plans/<feature-slug>/<NN>-<slug>.md` | One implementation ticket: delivery, spec references, blockers, status, and acceptance criteria for work being planned for execution. |
| `.onward/future/` | Matters to discuss or do later: open questions, deferred designs, future features, and technical improvements. Keep simple items in one document; expand a topic into its own file when useful. |
| `.onward/research/` | Investigations: questions, sources, findings, and limitations that inform decisions. |
| `.onward/visuals/` | Diagrams, visual explanations, and their source files or HTML artifacts. |
| `.onward/reports/` | Review findings, diagnoses, verification results, and actionable handoff suggestions. |
| `.onward/archive/` | Historical snapshots retired from ongoing maintenance, such as completed change specs and superseded documents. Store them directly here. |

Long-lived specs describe the current design and carry no status. Archive a change spec only after implementation, verification, and synchronization of the long-lived specs are complete. Follow the project's choice about tracking `.onward/` in Git. Add no automatic logs.

Give `AGENTS.md` a brief pointer telling agents to consult `spec/conventions.md` before implementation or creating, updating, or moving project documents and process artifacts (research, visualizations, reports). Preserve all existing rules and append only a missing pointer; create the file if absent. Never delete or overwrite the existing file. Keep the detailed conventions in one place.

Keep this setup limited to the agreed documentation work. Preserve existing Markdown content; move documents only under the approved migration option, carrying it out as part of this initialization and updating affected references and conventions. Save actionable findings and suggestions in `.onward/reports/` when a handoff document would help; a report is not required for every initialization. Code scaffolding and feature implementation belong to later work.

Finish when the conventions reflect the available project facts and agreed setup choices, and the `AGENTS.md` pointer resolves. Briefly report what was established.

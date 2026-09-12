---
name: init-onward
description: Establish project documentation and conventions when setting up a project for Onward.
---

# Init Onward

Give the project a small, usable foundation for future design and implementation. Ground it in the conversation, existing documentation, and repository practices. Ask about unresolved choices only when they affect this setup.

Inspect existing documentation before changing files. If the project already has a documentation layout, present two concrete setup options: retain it or migrate to the defaults below, explaining the affected files and destinations. Wait for the user's choice before editing; follow an already confirmed choice without asking again. If there is no existing layout, proceed with the defaults.

Create or supplement `spec/conventions.md`, titled “项目约定” (Project conventions), as the home for project-specific directory, documentation, coding, build, and test conventions. Record established practices and agreed choices; point to authoritative configuration where it already supplies the details. Leave future design decisions for later discussion.

Use these default documentation conventions:

- Project specs live in `spec/product.md`, `spec/architecture.md`, and `spec/conventions.md`; use `spec/api.md` for external APIs and their examples. Create documents as substantive content emerges, rather than filling out an empty template set.
- Module specs live with their modules in a local `spec/` directory once the module structure exists. During design, a module can start with a single spec.
- Long-lived specs describe the current design and carry no status. A change spec lives directly in project `spec/`, with a descriptive filename and a status of draft, confirmed, or completed. Archive it only after implementation, verification, and synchronization of the long-lived specs are complete.
- Implementation plans live in `spec/plans/<feature-slug>/`, with one ticket per `<NN>-<slug>.md` file. Each ticket records its delivery, spec references, blockers, status, and acceptance criteria.
- Process artifacts live under `.onward/`: create `research/`, `visuals/`, `reports/`, and `archive/` only as needed. Archived materials go directly in `archive/` and are historical snapshots, outside ongoing documentation synchronization. Follow the project's choice about tracking `.onward/` in Git. Add no automatic logs.

Give `AGENTS.md` a brief pointer telling agents to consult `spec/conventions.md` before implementation or creating, updating, or moving project documents and process artifacts (research, visualizations, reports). Preserve all existing rules and append only a missing pointer; create the file if absent. Never delete or overwrite the existing file. Keep the detailed conventions in one place.

Keep this setup limited to the agreed documentation work. Preserve existing Markdown content; move documents only under the approved migration option, carrying it out as part of this initialization and updating affected references and conventions. Save actionable findings and suggestions in `.onward/reports/` when a handoff document would help; a report is not required for every initialization. Code scaffolding and feature implementation belong to later work.

Finish when the conventions reflect the available project facts and agreed setup choices, and the `AGENTS.md` pointer resolves. Briefly report what was established.

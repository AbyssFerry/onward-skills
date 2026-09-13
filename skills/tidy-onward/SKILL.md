---
name: tidy-onward
description: Tidy documentation in Onward projects by reorganizing files, consolidating overlapping content, and resolving outdated or inconsistent descriptions.
---

# Tidy Onward

Make project documentation clear, consistent, and easy to find. Read and follow the Onward conventions in `AGENTS.md` before making changes. If they are missing, tell the user to run `init-onward` first and stop without editing documents.

Reorganize and consolidate documents using settled decisions and repository evidence, preserving meaningful details. Correct outdated descriptions when the evidence is clear; surface unresolved design conflicts for the user.

Update affected references and archive superseded material in `.onward/archive/` once its still-relevant content is preserved in the maintained documents. Respect the project's document lifecycle. Keep changes limited to documentation.

Review the maintained documentation within this task's scope with two parallel sub-agents:

- **Fidelity**: does it accurately and completely reflect settled decisions and repository evidence, including the implementation where applicable?
- **Coherence**: are related documents consistent with each other, with clear ownership, consistent terminology, no unnecessary duplication, and working references?

Give both agents the scope and relevant sources. Keep their findings separate and resolve supported findings before finishing.

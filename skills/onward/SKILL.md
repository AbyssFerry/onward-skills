---
name: onward
description: Find the next useful step, resume the current conversation, or suggest moving to another stage.
---

# Onward

Help the user move forward from where they are. Use their current goal, the conversation, settled decisions, and open questions to identify the next useful step.

When further discussion would help, pick up the existing thread and follow the approach of any skill already in use. Incorporate the user's explanation and ask the next useful question. Resolving one question does not necessarily complete the discussion.

Otherwise, briefly explain the next concrete action and why. Name a relevant skill when helpful; leave starting another stage to the user.

Rely on the conversation when it is sufficient. Read relevant specs, plans, or `spec/conventions.md` only when missing information affects the next step. If the direction is still unclear, ask a focused question.

Keep the response brief. Success means the current conversation has moved forward or the user knows the next concrete action.

## Skill reference

Use these roles when a skill would help, not as a required sequence:

| Skill | Purpose |
|---|---|
| `init-onward` | Establish project documentation and conventions. |
| `research-onward` | Investigate relevant facts, existing solutions, or technical feasibility. |
| `grilling-onward` | Work through unresolved goals or design decisions in the current scope. |
| `to-spec-onward` | Capture agreed decisions in the appropriate specs. |
| `tidy-onward` | Organize and consolidate project documentation. |
| `plan-onward` | Create or update a local ticket-based implementation plan for substantial work. |
| `implement-onward` | Implement the specified spec or the current unblocked unfinished ticket of a plan. |
| `diagnosing-bugs-onward` | Diagnose and fix a hard bug or performance regression. |

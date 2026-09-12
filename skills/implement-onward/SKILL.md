---
name: implement-onward
description: "Implement a spec or the current unblocked unfinished ticket of a local plan, including verification and documentation closeout."
---

Read and follow `spec/conventions.md`. If it is missing, tell the user to run `init-onward` first and stop without making changes.

Implement the work described by the user in the spec. For a plan, identify the current unblocked unfinished ticket from actual progress and dependencies, and implement only that ticket.

Capture the starting Git state and pre-existing changes so review and commit cover only this work; preserve unrelated changes and their staging state.

Use /tdd-onward where possible, at pre-agreed seams.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

Use [tidy-onward](../tidy-onward/SKILL.md) to update and close out documentation affected by this work, including specs and actual plan progress. Synchronize documents before code review.

Once done, use [code-review-onward](../code-review-onward/SKILL.md) to review the work, providing the starting Git state, work scope, and spec or selected ticket. Mark work completed or archive change specs only after review and applicable fixes are complete.

Commit your work to the current branch.

Report the delivered result, verification, and commit, then stop at the end of this scope.

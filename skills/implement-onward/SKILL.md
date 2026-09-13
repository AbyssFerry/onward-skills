---
name: implement-onward
description: "Implement a spec or the current unblocked unfinished ticket of a local plan, including verification and documentation closeout."
---

Read and follow the Onward conventions in `AGENTS.md`. If they are missing, tell the user to run `init-onward` first and stop without making changes.

Implement the work described by the user in the spec. For a plan, identify the current unblocked unfinished ticket from actual progress and dependencies, and implement only that ticket.

Capture the starting Git state and pre-existing changes so review and commit cover only this work; preserve unrelated changes and their staging state.

Use /tdd-onward where possible, at pre-agreed seams.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

Once done, use [code-review-onward](../code-review-onward/SKILL.md) to review the work, providing the starting Git state, work scope, and spec or selected ticket. Mark work completed or archive change specs only after review and applicable fixes are complete.

Check the documentation affected by this implementation yourself, ensuring that relevant specs, task status, and verification records accurately reflect settled decisions and actual results; update omissions or outdated descriptions directly.

Commit your work to the current branch.

Report the delivered result, verification, and commit, then stop at the end of this scope.

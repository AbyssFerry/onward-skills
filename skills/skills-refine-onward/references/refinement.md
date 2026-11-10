# Purpose and Judgment

Make an existing skill easier to understand and more useful. Preserve the domain knowledge, decision criteria, and necessary constraints that serve its original purpose, while giving the agent appropriate room to exercise judgment.

## Find the core

Read the target skill and relevant supporting files. Understand whose problem it solves and which content changes the agent's decisions or results. Clarify only unknowns that affect the tradeoffs. Preserve the intended scope, invocation policy, and explicit user requirements.

## Prune with purpose

- Consolidate repeated meanings. Remove generic reminders, stale information, and operating instructions already supplied by the host.
- Replace fixed steps, quotas, and checklists that lack a clear purpose with outcomes and decision criteria. State the desired behavior positively.
- Check whether examples and past fixes have been overgeneralized. Judge their value against the skill's intended scope and extract reusable knowledge. Keep authoring and acceptance records outside the runtime package.
- Match constraints to the task. Exploratory work benefits from direction, resources, and selection criteria. Precise or fragile operations need their essential ordering, parameters, checks, and permission boundaries.

Every passage should earn its place; add missing information when it matters. Judge refinement by clarity and continued ability to perform the original task.

## Organize by use

Keep the shared purpose, core judgments, and essential guidance in the main file. Put conditional detail in references, with links that explain when to consult it. A simple skill can remain self-contained.

Preserve useful sources, domain material, and reusable methods. Inspect supporting files and their callers before reorganizing them so valuable content remains reachable. Maintain each meaning in one place, and retain scripts and assets according to their actual use.

## Check the result

Check the revised description, invocation policy, links, and format. For substantive changes, consider representative requests: is the purpose preserved, is essential knowledge reachable, are constraints proportionate, and can the skill handle new tasks appropriately?

Address causes revealed by observation rather than accumulating a universal rule for every trial detail. Briefly explain the main tradeoffs, what was verified, and any unresolved issues when delivering the revision.

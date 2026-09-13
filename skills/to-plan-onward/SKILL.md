---
name: to-plan-onward
description: Create or update a local implementation plan with coherent delivery tasks, one file per task with blocking dependencies.
---

# To Plan Onward

Organize a plan, spec, or conversation into an implementation plan of **tasks**: coherent delivery units, each declaring the tasks that **block** it.

Read and follow the Onward conventions in `AGENTS.md`. If they are missing, tell the user to run `init-onward` first and stop without editing documents.

## Process

### 1. Gather context

Work from whatever is already in the conversation context. If the user passes a reference (a spec path, an issue number or URL) as an argument, fetch it and read its full body and comments.

When updating a plan, preserve completed facts and use the current implementation and confirmed changes to add, remove, or adjust remaining tasks and dependencies, including unfinished work in a task already underway. Use [tidy-onward](../tidy-onward/SKILL.md) to reflect confirmed requirement or design changes in the relevant specs first; changes only to implementation order belong in the plan.

### 2. Explore the codebase (optional)

If you have not already explored the codebase, do so to understand the current state of the code. Task titles and descriptions should use the project's domain glossary vocabulary, and respect ADRs in the area you're touching.

Look for opportunities to prefactor the code to make the implementation easier. "Make the change easy, then make the easy change."

### 3. Draft implementation tasks

By default, each task will be implemented separately with [implement-onward](../implement-onward/SKILL.md), including verification, code review, affected documentation updates, and a commit. Size tasks to warrant that complete delivery cycle. If the user requests finer granularity or another execution approach, adapt the plan accordingly.

<task-sizing-rules>

- Each task delivers a coherent end-to-end outcome across the layers it needs (schema, API, UI, tests), demoable or verifiable on its own.
- Keep closely related steps of the same user goal in one task, preserving the details as acceptance criteria.
- Split when independent delivery has practical value, dependencies or risks need isolation, or the combined implementation and review would be too complex for one fresh context. This is a size constraint, not a reason to make tasks as small as possible.
- Before presenting the plan, check whether adjacent tasks would repeatedly touch the same logic and repeat setup or verification. Merge where the scope remains clear and manageable, preserving all requirements and acceptance criteria. Let the number of tasks follow the delivery boundaries rather than a fixed target.
- Any prefactoring should be done first.

</task-sizing-rules>

Give each task its **blocking edges**: the other tasks that must complete before it can start. A task with no blockers can start immediately.

**Wide refactors need a migration sequence.** A **wide refactor** is one mechanical change (rename a column, retype a shared symbol) whose **blast radius** fans across the whole codebase, so a single edit breaks thousands of call sites at once and no end-to-end task can land green independently. Sequence it as **expand–contract**. First expand: add the new form beside the old so nothing breaks. Then migrate the call sites over in batches sized by blast radius (per package, per directory), each batch its own task blocked by the expand, keeping CI green batch to batch because the old form still exists. Finally contract: delete the old form once no caller remains, in a task blocked by every migrate batch. When even the batches can't stay green alone, keep the sequence but let them share an integration branch that all block a final integrate-and-verify task; green is promised only there.

### 4. Quiz the user

Present the proposed breakdown as a numbered list. For each task, show:

- **Title**: short descriptive name
- **Blocked by**: which other tasks (if any) must complete first
- **What it delivers**: the end-to-end behaviour this task makes work

Ask the user:

- Does the granularity feel right? (too coarse / too fine)
- Are the blocking edges correct: does each task only depend on tasks that genuinely gate it?
- Should any tasks be merged or split further?

Iterate until the user approves the breakdown.

### 5. Save the plan

Save the approved tasks as local files, updating existing tasks when revising a plan. Follow the project's convention for placement; default to `spec/plans/<feature-slug>/<NN>-<slug>.md`, numbered from `01` in dependency order (blockers first). Each file's "Blocked by" lists the numbers/titles it depends on. Use the per-task file template below: one task per file, never a single combined file. Preserve existing task identifiers when updating a plan so references remain valid.

Work the **frontier**: any task whose blockers are all done. For a purely linear chain that means top to bottom.

<local-task-template>

# <NN>: <Task title>

**What to build:** the end-to-end behaviour this task makes work, from the user's perspective, not a layer-by-layer implementation list.

**Blocked by:** the numbers/titles of the tasks that gate this one, or "None (can start immediately)".

**Specs:** references to the specs this task implements.

**Status:** ready-for-agent (for new tasks; preserve actual progress when updating)

- [ ] Acceptance criterion 1
- [ ] Acceptance criterion 2

</local-task-template>

In implementation details, avoid specific file paths or code snippets: they go stale fast. Exception: if a prototype produced a snippet that encodes a decision more precisely than prose can (state machine, reducer, schema, type shape), inline it and note briefly that it came from a prototype. Trim to the decision-rich parts, not a working demo, just the important bits.

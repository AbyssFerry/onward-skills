---
name: multi-session-run-plan-onward
description: Run an approved plan through separate Codex implementation chats, with coordinator review between tasks.
---

Use the current chat as coordinator for an approved plan from [to-plan-onward](../to-plan-onward/SKILL.md). Follow its progress and dependencies, recording chat links and results in the plan.

Open a new Codex chat for each task, using **GPT-6.1 Sol / medium**. Tell it to use [implement-onward](../implement-onward/SKILL.md) to complete that task. Open only the current task's chat, not the whole plan in advance.

Wait for the implementation chat to report completion, then review its result in the coordinator chat. Send any needed changes back to that implementation chat. After acceptance, automatically proceed to the next task.

Continue until the agreed plan scope is complete. Pause and report to the user when blocked or when a user decision is needed.

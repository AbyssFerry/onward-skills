---
name: multi-session-dispatch-onward
description: Start a specified task in a separate Codex chat, with independent execution and a completion report to the originating chat.
---

Open a new user-visible Codex chat for the task the user wants to handle there. Give it a self-contained brief: the objective, relevant context and file or spec references, requested scope, and what counts as done. Let the user's request determine whether it diagnoses, plans, implements, or does another task.

Include the originating chat's link and cite the user's own request or confirmation so the new chat can verify the authorization to report back.

Tell the new chat to work independently, deliver its result to the user there, and send the originating chat one concise completion report with the outcome and relevant artifact links. Keep interim discussion and revisions in the new chat; report back only when the assigned task reaches its final outcome, not after each discussion point. If work must stop because of a blocker, explain the blocker and the input needed to the user there, and notify the originating chat.

After creating the chat, give the user its link. Continue any independent work already requested in the originating chat, or end the turn. Neither chat waits or polls for the other, and neither needs an acknowledgement after reporting. Keep any follow-up within the user's requested scope.

---
name: find-resources-onward
description: "Manually invoked discovery of useful skills, tools, reading, and references for a task."
---

# Find useful resources

Help the user find resources worth using, reading, or learning from. These may be skills, plugins, MCP servers, CLIs, software, official documentation, blogs, tutorials, examples, or projects, depending on what would help their task.

This skill delivers discovery results. Installation, integration, and carrying out the task are for a subsequent request. Invoke it manually; the Codex invocation policy lives in `agents/openai.yaml`.

## Align on what to find

Discuss the user's purpose, intended use, and priorities. Build on what they have already said, and ask follow-up questions when an unclear point could change what would be useful to investigate.

Use the [research areas](references/sources.md#choosing-research-areas) to show the available directions and what each could contribute to this task. Recommend areas and relative emphasis, explain why, and let the user choose one, several, all, or another direction.

Continue the conversation when the purpose or selection is unclear. Begin the corresponding research once the scope and priorities are agreed; carry forward choices that are already explicit.

## Choose search tools when useful

**Exa** can broaden web discovery and fetch known pages. **Firecrawl** can search, retrieve page content, and discover or collect pages within a site. Use them when they add worthwhile coverage or content, such as incomplete results or missing page text; they are optional choices, not startup steps for every search.

Choose according to the task, current tool availability, and applicable quota or cost. Use existing authorized quota when the expected benefit is clear; ask the user when the value or acceptable spend is unclear. See [access methods](references/access-methods.md#exa-and-firecrawl) for tool selection and usage limits.

For papers and research evidence, read [academic search](references/academic-search.md), which connects the bundled paper-lookup instructions, database references, and executable lookup scripts to this discovery task.

## Explore beyond the obvious

The [source map](references/sources.md) offers directories, repositories, official material, blogs, communities, and example collections. When looking for agent skills, browse the [skill collections](references/skill-collections.md) for development, specialist, and discovery projects. Choose useful starting points and extend into the task's own field.

Use the capabilities and knowledge needed to reach the user's goal as search directions.

Expand the user's wording into domain terminology, synonyms, and relevant languages, including Chinese and English where useful. Direct repositories, author links, and community discussions can reveal resources missing from aggregators. Existing skills and plugins may help too, alongside external discovery.

Adjust breadth and depth to the task and any request for a quick or deep search. Spend attention on the user's priorities; complementary sources matter more than list length.

When multiple research areas are selected and subagents are available, assign a dedicated subagent to each area. Give each the agreed purpose, priorities, and a clear research scope. Have each return useful candidates, findings supported by original material, and important gaps.

Run independent investigations in parallel within available capacity, using batches when needed. The main agent brings the findings together, compares alternatives, removes duplication, and follows up on important conflicts or gaps.

A single area, or an environment without subagents, can be investigated directly.

## Judge what helps

Judge resources against the purpose: which part they help with, whether their content and capabilities fit, and whether their prerequisites suit the user. Read the author's material, source files, or official explanations for important candidates. Articles offer methods and context; examples offer ideas to borrow; tools offer capabilities and integration options.

Base recommendations on content and fit. Popularity can surface leads, and listings of the same upstream resource can be combined. State important unknowns. Reading an explanation and trying a resource provide different levels of knowledge.

## Bring back useful choices

Respond in the user's language. Lead with the most worthwhile resources, with original links, uses, reasons, and important prerequisites; retain other useful candidates as needed.

Where useful, explain how resources complement one another or offer alternative ways to meet the same need.

Make clear what was explored in each selected research area, what it contributed, and any gaps that affect the conclusions. Include areas where no useful resources were found.

Adapt the number, grouping, and presentation to the task so the user can see what is worth exploring next and why.

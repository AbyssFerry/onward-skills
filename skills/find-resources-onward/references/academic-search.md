# Academic Search

Use this guide when the user selects academic or professional research. Find useful papers and show how well each lead is supported; conduct a systematic review only when requested.

## Use the bundled lookup package

Read [paper-lookup](../resources/.upstream/paper-lookup/SKILL.md) when scholarly database queries, DOI or citation lookup, or access to original papers would help the task. Its complete instructions, database references, and scripts are available locally. Follow the database-selection guidance and load the references relevant to the question, adding sources when they fill a real gap.

Use the bundled scripts when they help retrieve or process results. They require Python 3.11+ and use the standard library; the API examples also use curl and network access. Run commands from `resources/.upstream/paper-lookup/` within this skill, or resolve its script paths explicitly. Check a script's `--help` for its arguments. For example, `python scripts/paginate.py --list-apis` lists supported pagination adapters without querying a service. The other scripts parse arXiv records, reconstruct OpenAlex abstracts, and convert JATS XML to text.

Shell examples use Bash syntax; adapt executable names and quoting to the active shell while preserving the request and response handling. Authentication, rate limits, and access rights depend on the selected database; consult its bundled reference and current provider documentation. The package is an internal resource for this discovery task, not a separate Onward entry point or a requirement to run every database and script.

Use [Google Scholar](https://scholar.google.com/intl/en/scholar/help.html) for broad discovery, related works, citations, and alternate versions. Available specialist tools such as Consensus or Firecrawl's paper search and reading tools can help when suited to the question. For missing publisher-page content, consider the page-access options in [access methods](access-methods.md). Check current tool and service documentation; these tools complement indexes and do not replace source verification.

## Verify and report what you found

Follow promising results to a publisher, author manuscript, preprint server, or repository. Verify the title, authors, date, venue, and stable identifier there. Distinguish metadata, abstract, and full text; summarize only what you read, and label preprints when relevant.

Deduplicate by DOI, then other stable identifiers such as PMID or arXiv ID. Without a shared identifier, compare titles, authors, and dates. Link preprint and published versions instead of silently merging them.

For each useful lead, give its original link, fit, and whether you checked the abstract or full text. Name the sources searched, query focus, and material coverage or access gaps. No result in one index does not prove no relevant work exists. Clarify scope and selection criteria before calling a broad review comprehensive.

An index record or abstract does not establish full-text availability. Use the package's access guidance to find an available original or open copy, and report what you could actually read.

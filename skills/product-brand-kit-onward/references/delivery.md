# Delivering the Campaign Kit

## File layout and index

Follow the project's existing design output structure. If it has none, use a versioned folder such as `brand-campaign/<brand-or-event>/v01/` and names the team can recognize. Make it clear which file shows the complete kit, where to get each asset or line, and which source to edit next.

| Location | Contents | Use |
| --- | --- | --- |
| Version root | Illustrated brand handbook PDF and usage index | Review the full system, then locate individual files. |
| `copy/` | V01 name, V02 taglines and contextual copy, V03 story and introduction | Copy approved wording. A UTF-8 document with clear sections can hold all three. |
| `brand-assets/` | V04 vector master and transparent PNG, V05 typography and color specimen, V06 key visual and layers | Share the same mark, colors, and imagery. |
| `campaign-assets/` | Applicable A01–A07, organized independently by ID | Hand the finished images, copy, pages, or storyboard to each channel owner. |
| `editable/` | Editable campaign, page, and handbook sources with their dependencies | Revise a line, adjust a layout, or re-export within the relevant licenses. |
| Internal evidence, when needed | Confirmations, image and font sources, licenses, and facts to verify | Follow up on decisions and outstanding permissions. |

An index entry can read “A05 · Gift card · Front uses the V02 gift line, signature is left for the sender · Relative links to print preview and editable source · v01 concept”. Use actual details for each asset. Preserve the existing mark lockup where applicable and choose formats for the real placements. Keep IDs through revisions and retain the previous version. For individual work, deliver the item and its dependencies and update the matching index entry if one exists.

## What counts as finished

- Deliver copy in editable text with the agreed punctuation, naming, placement, and available short versions.
- Keep native vector geometry and an editable master for logos. Outline type or use an equivalent method in distribution copies when appearance must be stable. Supply transparent PNG for raster-only uses. Label concept-only explorations and respect licenses that limit source distribution.
- Preserve editable relationships among the key visual's mark, headline, subject, and background. Supply a finished export at the intended size. Check production artwork against confirmed specifications and mark concept previews accordingly.
- Make distributed pages usable with embedded assets or working relative paths. Supply actual keyframes and a viewing order for a storyboard, and a playable video when commissioned.

## Illustrated PDF

Lead with the key visual. Present the name and line, story, mark, typography and color, image language, and representative campaign pieces. Close with a usable file index. Use real examples to show how the pieces work. A thumbnail next to a phone-size preview, for example, makes avatar choices easier to judge. Include finished copy and visuals for commissioned pieces.

Export from the editable layout tool, or create print-ready UTF-8 HTML with local fonts, available images, and explicit page breaks. The bundled [PDF export script](../scripts/export_pdf.py) uses Python Playwright. On Windows it tries Edge and then Chrome before Playwright Chromium. On other systems it defaults to Playwright Chromium. Supply `--channel chrome` or `--channel msedge` to use a specific installed browser. The script takes an input HTML file and a new PDF filename. [Playwright browser setup](https://playwright.dev/python/docs/browsers)

```text
python -X utf8 "<skill-folder>/scripts/export_pdf.py" "editable/handbook.html" "brand-handbook-v01.pdf"
```

## Check the final files

Open the vector mark, transparent PNG, key visual, and every delivered item. Verify the target script, type, linework, transparent areas, names and credits, and intended display size. Check horizontal and vertical crops, mobile line breaks, print sides, and writing areas. For A07, compare flat faces with closed and opened views. Verify reading order, brand and category, opening orientation, and what becomes visible first. Provide editable sources and label concept proportions or verified dimensions. Save production artwork separately using the supplier's confirmed dieline, materials, and prepress requirements.

Render the PDF page by page to check images, page breaks, cropping, and footers. Extract text to confirm the brand name and lead line. Open the index links and check that independent assets match the handbook version. Distinguish concept proposals, approved work, and files ready to use in the handoff.

---
name: docx-md
description: Convert Markdown to Word (.docx) or Word to Markdown in this repo, e.g. importing a .docx resume into resumes/ or exporting a tailored resume to .docx for submitting. Use when the user asks to convert, import or export between .md and .docx.
---

# docx ↔ md

Run from the repo root. pandoc comes bundled with the `pypandoc-binary` dependency, so you don't need to install anything:

```sh
uv run .claude/skills/docx-md/convert.py IN.docx OUT.md   # Word -> Markdown
uv run .claude/skills/docx-md/convert.py IN.md OUT.docx   # Markdown -> Word
```

The direction comes from the file extensions.

## Notes

- **Word → Markdown:** after converting, read the output and tidy anything pandoc mangled, such as tables used for layout, stray `\` escapes or empty headings. For resumes, keep the format of the existing files in `resumes/`: `# Name`, a contact line, `##` sections and `-` bullets.
- **Markdown → Word:** the output uses pandoc's default styles. Tell the user to check the formatting before they submit.
- Images from a .docx are saved to `<out>_media/`.
- Keep personal files in the gitignored `resumes/` folder, never in tracked paths.

"""Convert between Markdown and Word: uv run .claude/skills/docx-md/convert.py IN OUT

Direction comes from the file extensions (.md <-> .docx).
"""
import sys
from pathlib import Path

import pypandoc

src, dst = map(Path, sys.argv[1:3])
if {src.suffix, dst.suffix} != {".md", ".docx"}:
    sys.exit("usage: convert.py IN.md OUT.docx  |  convert.py IN.docx OUT.md")

if dst.suffix == ".docx":
    pypandoc.convert_file(src, "docx", format="gfm", outputfile=dst)
else:
    # Images go to <out>_media/ so they aren't dropped
    pypandoc.convert_file(src, "gfm", outputfile=dst,
                          extra_args=["--wrap=none", f"--extract-media={dst.with_name(dst.stem + '_media')}"])
print(f"{src} -> {dst}")

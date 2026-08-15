"""
A small helper script to split a single Jupyter notebook into multiple notebooks using top-level
markdown headings as separators.

This is an opinionated tool — review the output before committing it. It requires `nbformat`.
"""
import sys
import os
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell


def split_notebook(src_path, out_dir):
    nb = nbformat.read(src_path, as_version=4)
    os.makedirs(out_dir, exist_ok=True)

    parts = []
    current = {"cells": [], "title": None}

    def start_new(title):
        nonlocal current
        if current["cells"]:
            parts.append(current)
        current = {"cells": [], "title": title}

    for cell in nb.cells:
        if cell.cell_type == "markdown":
            src = cell.source.lstrip()
            # detect top-level headers
            if src.startswith("# ") or src.startswith("## "):
                title = src.splitlines()[0].lstrip("# ").strip()
                # start new part
                start_new(title)
        current["cells"].append(cell)

    # append last
    if current["cells"]:
        parts.append(current)

    # write parts
    for i, part in enumerate(parts):
        title = part.get("title") or f"part_{i}"
        out_nb = new_notebook()
        out_nb.cells = part["cells"]
        safe_title = "_".join(title.split())
        out_path = os.path.join(out_dir, f"{i:02d}_{safe_title}.ipynb")
        nbformat.write(out_nb, out_path)
        print(f"Wrote {out_path}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python split_notebook.py SOURCE_NOTEBOOK OUTPUT_DIR")
        sys.exit(1)
    src = sys.argv[1]
    out = sys.argv[2]
    split_notebook(src, out)

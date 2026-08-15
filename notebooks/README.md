# notebooks/README — splitting the monolithic notebook

This repository contains `notebooks/zomato_analysis.ipynb` (a single, end-to-end notebook). To split it into numbered notebooks, use the helper script `notebooks/split_notebook.py` included here.

The script will split the original notebook into separate notebooks using top-level markdown headings as breakpoints (markdown cells starting with `# ` or `## `).

Usage (from repository root):

```bash
python notebooks/split_notebook.py notebooks/zomato_analysis.ipynb notebooks/split_output
```

The script will create a folder `notebooks/split_output/` containing numbered notebooks.

If the automatic split doesn't capture the desired sections, open `notebooks/zomato_analysis.ipynb` and move cells manually into the numbered notebooks suggested in README.

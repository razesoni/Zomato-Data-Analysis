# Zomato Data Analysis

Exploratory data analysis (EDA) of the Zomato restaurants dataset using Python, Pandas, NumPy, Matplotlib, and Seaborn. This repository contains Jupyter notebooks that walk through data loading, cleaning, transformation, visualization, and insights discovery from the Zomato dataset.

## Project Overview

This project performs an exploratory data analysis (EDA) on the Zomato dataset to uncover patterns and trends in restaurant ratings, cuisines, costs, and city-level behaviour. The analysis is reproducible and organized as Jupyter notebooks that document the steps from raw data to findings.

## Dataset

- Source: zomato-dataset.csv (original source: https://www.kaggle.com/datasets/shrutimehta/zomato-restaurants-data)
- Records: ~9,551 restaurants (as provided in the dataset)
- Notes: The raw dataset requires cleaning — missing values, inconsistent types, and categorical normalization are addressed in the notebooks.

## Notebooks

The main notebooks in this repository:

- `zomato_analysis.ipynb` — end-to-end analysis (data cleaning, EDA, visualizations, conclusions).
- If you have multiple notebooks, consider naming them for the workflow (e.g., `0_data_overview.ipynb`, `1_data_cleaning.ipynb`, `2_visualizations.ipynb`, `3_insights.ipynb`).

## Key Questions

The analysis focuses on questions such as:

- What is the overall distribution of restaurant ratings?
- How do services like table booking and online delivery relate to ratings?
- What is the relationship between average cost for two and aggregate rating?
- Which cities and cuisines dominate the dataset?
- Is there a correlation between the number of votes and ratings?

## Analysis Workflow

1. Data loading with pandas (using `latin-1` encoding if required).
2. Data cleaning: handle missing values, type conversions, and duplicate removal.
3. Exploratory analysis and summary statistics for numeric and categorical columns.
4. Visualizations using Seaborn/Matplotlib: histograms, bar plots, box plots, and scatter plots.
5. Interpretation and key findings summarized in the final notebook section.

## Key Findings (example summary)

- Most restaurants have aggregate ratings between ~2.8 and 4.0.
- Restaurants offering table booking generally show higher average ratings.
- Positive correlation exists between number of votes and rating (more votes → more reliable ratings).
- Popular cuisines and city-wise trends are highlighted in the visualizations.

(Please update this section if you add new analyses or refine the notebooks.)

## Tools and Libraries

- Python 3.8+
- pandas
- numpy
- matplotlib
- seaborn
- jupyter

## How to run

1. Clone the repository:

```bash
git clone https://github.com/razesoni/Zomato-Data-Analysis.git
```

2. Install dependencies (create `requirements.txt` if not present):

```bash
pip install -r requirements.txt
# or
pip install pandas numpy matplotlib seaborn jupyter
```

3. Open the main notebook:

```bash
jupyter lab
# or
jupyter notebook
```

4. Run notebooks in order to reproduce the analysis.

## Contributing

Contributions are welcome. Open an issue to discuss changes or submit a pull request with a clear description of your updates.

## License

This repository is provided under the MIT License. See `LICENSE` for details.

## Contact

Repository owner: @razesoni

---



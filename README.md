# Zomato Restaurant Analytics

Exploratory analysis and an interactive Streamlit dashboard for restaurant ratings, cuisines, services, votes and costs.

## Included work

- `notebooks/zomato_analysis.ipynb`: original EDA
- `src/utils.py`: loading, cleaning and dashboard helpers
- `app.py`: Streamlit interface
- `data/raw/`: restaurant data and country codes
- `Dockerfile`, `docker-compose.yml`, `DEPLOYMENT.md`: container/deployment configuration

## Run locally

Use Python 3.11 for the pinned NumPy/pandas versions. From the repository root in a separate virtual environment:

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Open the URL printed by Streamlit. For notebook exploration, open `notebooks/zomato_analysis.ipynb` and check its dataset paths against the repository layout.

## Questions to explore

How do restaurant ratings differ across cuisines, cities and booking/delivery options? How do vote count and cost relate to ratings? Use dashboard filters to inspect the sample before interpreting averages.

## Interpretation and limitations

The analysis is observational: service availability and ratings do not establish causation. Exclude or explicitly describe unrated entries; compare sample sizes and country/currency context. Exact findings should be reproduced from the notebook before being quoted.

The earlier README linked [this Kaggle dataset](https://www.kaggle.com/datasets/shrutimehta/zomato-restaurants-data). Confirm that it matches the included CSV and verify redistribution terms. Live hosting is not verified by this repository.

## Next steps

Publish three reproducible findings with charts and sample sizes, add data-quality tests, and validate the container in a clean environment.

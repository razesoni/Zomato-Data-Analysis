"""
utils.py
--------
Helper functions for data loading, preprocessing, and analytical aggregations
for the Zomato Restaurant Analytics Dashboard.
"""

from typing import List, Tuple
import pandas as pd


def load_and_preprocess_data(
    zomato_path: str = "data/raw/zomato-dataset.csv",
    country_code_path: str = "data/raw/Country-Code.csv"
) -> pd.DataFrame:
    """
    Loads raw Zomato data and Country Code mapping, cleans missing cuisines,
    and returns a merged DataFrame.
    """
    # Load dataset with latin-1 encoding to prevent decoding issues
    df = pd.read_csv(zomato_path, encoding="latin-1")
    
    # Clean rows with missing cuisine info
    df.dropna(subset=["Cuisines"], inplace=True)
    
    # Load country lookup table
    df_country = pd.read_csv(country_code_path)
    
    # Left merge on Country Code
    final_df = pd.merge(df, df_country, on="Country Code", how="left")
    
    return final_df


def filter_dataset(
    df: pd.DataFrame,
    countries: List[str],
    cities: List[str],
    rating_range: Tuple[float, float],
    online_delivery: str,
    table_booking: str
) -> pd.DataFrame:
    """
    Filters the DataFrame based on sidebar selections.
    """
    filtered = df.copy()

    if countries:
        filtered = filtered[filtered["Country"].isin(countries)]

    if cities:
        filtered = filtered[filtered["City"].isin(cities)]

    filtered = filtered[
        (filtered["Aggregate rating"] >= rating_range[0]) &
        (filtered["Aggregate rating"] <= rating_range[1])
    ]

    if online_delivery != "All":
        filtered = filtered[filtered["Has Online delivery"] == online_delivery]

    if table_booking != "All":
        filtered = filtered[filtered["Has Table booking"] == table_booking]

    return filtered


def get_top_cuisines(df: pd.DataFrame, top_n: int = 15) -> pd.DataFrame:
    """
    Parses comma-separated cuisines and returns top N most frequent cuisines.
    """
    if df.empty:
        return pd.DataFrame(columns=["Cuisine", "Count"])

    exploded = df["Cuisines"].str.split(",").explode().str.strip()
    top_df = exploded.value_counts().head(top_n).reset_index()
    top_df.columns = ["Cuisine", "Count"]
    return top_df


def get_most_voted_restaurants(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    """
    Returns top N restaurants by cumulative votes.
    """
    if df.empty:
        return pd.DataFrame(columns=["Restaurant Name", "Votes"])

    return (
        df.groupby("Restaurant Name")["Votes"]
        .sum()
        .reset_index()
        .sort_values(by="Votes", ascending=False)
        .head(top_n)
    )


def get_top_rated_restaurants(
    df: pd.DataFrame, min_votes: int = 1000, top_n: int = 10
) -> pd.DataFrame:
    """
    Returns top N highest-rated restaurants with a minimum threshold of votes.
    """
    if df.empty:
        return pd.DataFrame(columns=["Restaurant Name", "Average Rating", "Total Votes"])

    rate_df = (
        df.groupby("Restaurant Name")
        .agg(
            Avg_Rating=("Aggregate rating", "mean"),
            Total_Votes=("Votes", "sum"),
            Outlets=("Restaurant ID", "count"),
        )
        .reset_index()
    )

    filtered = rate_df[rate_df["Total_Votes"] >= min_votes]
    return filtered.sort_values(by="Avg_Rating", ascending=False).head(top_n)
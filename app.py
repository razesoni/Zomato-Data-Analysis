import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from src.utils import (
    load_and_preprocess_data,
    filter_dataset,
    get_top_cuisines,
    get_most_voted_restaurants,
    get_top_rated_restaurants
)

# --- Page Configuration ---
st.set_page_config(
    page_title="Zomato Global Analytics Dashboard",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Data Loading with Caching ---
@st.cache_data
def get_data() -> pd.DataFrame:
    return load_and_preprocess_data(
        zomato_path="data/raw/zomato-dataset.csv",
        country_code_path="data/raw/Country-Code.csv"
    )

try:
    df = get_data()
except Exception as e:
    st.error(f"Error loading datasets: {e}. Please ensure the files exist in `data/raw/`.")
    st.stop()

# --- Sidebar Controls ---
st.sidebar.title("🍽️ Filter Options")

# Country selection
all_countries = sorted(df["Country"].dropna().unique())
default_countries = [c for c in ["India", "United States", "UAE", "United Kingdom"] if c in all_countries]

selected_countries = st.sidebar.multiselect(
    "Select Country:",
    options=all_countries,
    default=default_countries if default_countries else all_countries[:3]
)

# Dynamic city options based on country selection
filtered_by_country = df[df["Country"].isin(selected_countries)] if selected_countries else df
cities_available = sorted(filtered_by_country["City"].dropna().unique())
default_cities = cities_available[:5] if len(cities_available) >= 5 else cities_available

selected_cities = st.sidebar.multiselect(
    "Select City:",
    options=cities_available,
    default=default_cities
)

# Rating slider
rating_range = st.sidebar.slider(
    "Aggregate Rating Range:",
    min_value=0.0,
    max_value=5.0,
    value=(0.0, 5.0),
    step=0.1
)

# Service availability toggles
delivery_filter = st.sidebar.radio(
    "Online Delivery Available?",
    options=["All", "Yes", "No"],
    index=0
)

booking_filter = st.sidebar.radio(
    "Table Booking Available?",
    options=["All", "Yes", "No"],
    index=0
)

# --- Apply Modular Filtering ---
filtered_df = filter_dataset(
    df=df,
    countries=selected_countries,
    cities=selected_cities,
    rating_range=rating_range,
    online_delivery=delivery_filter,
    table_booking=booking_filter
)

# --- Top Header & Key Metrics ---
st.title("📊 Zomato Global Restaurant Analytics")
st.markdown("Interactive dashboard exploring restaurant listings, ratings, delivery services, and cuisine trends.")

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

total_restaurants = len(filtered_df)
avg_rating = round(filtered_df["Aggregate rating"].mean(), 2) if total_restaurants > 0 else 0.0
total_votes = filtered_df["Votes"].sum() if total_restaurants > 0 else 0
online_del_pct = f"{round((filtered_df['Has Online delivery'] == 'Yes').mean() * 100, 1)}%" if total_restaurants > 0 else "0%"

kpi1.metric("Total Restaurants", f"{total_restaurants:,}")
kpi2.metric("Average Rating", f"{avg_rating} / 5.0")
kpi3.metric("Total Votes Logged", f"{total_votes:,}")
kpi4.metric("Online Delivery Available", online_del_pct)

st.divider()

# --- Main Dashboard Tabs ---
tab1, tab2, tab3, tab4 = st.tabs([
    "🌍 Geographic & Share Analysis",
    "⭐ Rating Dynamics",
    "🍜 Cuisine & Pricing Trends",
    "📋 Raw Data Explorer"
])

# ==========================================
# TAB 1: Geographic & Share Analysis
# ==========================================
with tab1:
    col_geo1, col_geo2 = st.columns([1, 1])

    with col_geo1:
        st.subheader("Global Listing Distribution by Country")
        country_counts = df["Country"].value_counts().reset_index()
        country_counts.columns = ["Country", "Count"]

        # Aggregate beyond top 5 into 'Other Countries'
        top_n = 5
        top_countries = country_counts.head(top_n)
        other_count = country_counts.iloc[top_n:]["Count"].sum()
        if other_count > 0:
            top_countries = pd.concat([
                top_countries,
                pd.DataFrame([{"Country": "Other Countries", "Count": other_count}])
            ], ignore_index=True)

        fig_pie = px.pie(
            top_countries,
            values="Count",
            names="Country",
            hole=0.45,
            color_discrete_sequence=px.colors.sequential.RdBu
        )
        fig_pie.update_traces(textposition="inside", textinfo="percent+label")
        st.plotly_chart(fig_pie, use_container_width=True)

    with col_geo2:
        st.subheader("Top Cities by Volume (Filtered)")
        if not filtered_df.empty:
            city_counts = filtered_df["City"].value_counts().head(10).reset_index()
            city_counts.columns = ["City", "Restaurant Count"]
            fig_city = px.bar(
                city_counts,
                x="Restaurant Count",
                y="City",
                orientation="h",
                color="Restaurant Count",
                color_continuous_scale="Viridis"
            )
            fig_city.update_layout(yaxis=dict(autorange="reversed"))
            st.plotly_chart(fig_city, use_container_width=True)
        else:
            st.warning("No data available for the current filter criteria.")

    st.subheader("Interactive Restaurant Geolocation Map")
    if not filtered_df.empty:
        map_data = filtered_df[(filtered_df["Latitude"] != 0) & (filtered_df["Longitude"] != 0)]
        if not map_data.empty:
            fig_map = px.scatter_mapbox(
                map_data,
                lat="Latitude",
                lon="Longitude",
                hover_name="Restaurant Name",
                hover_data={"City": True, "Aggregate rating": True, "Votes": True, "Average Cost for two": True},
                color="Aggregate rating",
                size="Votes",
                size_max=18,
                color_continuous_scale="RdYlGn",
                zoom=1,
                mapbox_style="carto-positron"
            )
            fig_map.update_layout(margin=dict(l=0, r=0, t=0, b=0), height=450)
            st.plotly_chart(fig_map, use_container_width=True)
        else:
            st.info("No coordinates available for current selection.")

# ==========================================
# TAB 2: Rating Dynamics
# ==========================================
with tab2:
    col_rat1, col_rat2 = st.columns(2)

    with col_rat1:
        st.subheader("Distribution by Rating Color Category")
        if not filtered_df.empty:
            rating_grouped = (
                filtered_df.groupby(["Aggregate rating", "Rating color", "Rating text"])
                .size()
                .reset_index(name="Rating count")
            )
            
            color_map = {
                "Dark Green": "#006400",
                "Green": "#2E8B57",
                "Yellow": "#FFD700",
                "Orange": "#FF8C00",
                "Red": "#FF0000",
                "White": "#D3D3D3"
            }

            fig_rating_dist = px.bar(
                rating_grouped,
                x="Aggregate rating",
                y="Rating count",
                color="Rating color",
                color_discrete_map=color_map,
                hover_data=["Rating text"]
            )
            st.plotly_chart(fig_rating_dist, use_container_width=True)

    with col_rat2:
        st.subheader("Votes vs. Aggregate Rating")
        if not filtered_df.empty:
            fig_scatter = px.scatter(
                filtered_df,
                x="Aggregate rating",
                y="Votes",
                color="Price range",
                hover_name="Restaurant Name",
                opacity=0.6,
                color_continuous_scale="Magma"
            )
            st.plotly_chart(fig_scatter, use_container_width=True)

    st.subheader("Service Impact on Ratings")
    col_srv1, col_srv2 = st.columns(2)

    with col_srv1:
        if not filtered_df.empty:
            fig_del = px.box(
                filtered_df,
                x="Has Online delivery",
                y="Aggregate rating",
                color="Has Online delivery",
                color_discrete_map={"Yes": "#4CAF50", "No": "#E91E63"},
                title="Online Delivery vs Rating"
            )
            st.plotly_chart(fig_del, use_container_width=True)

    with col_srv2:
        if not filtered_df.empty:
            fig_book = px.box(
                filtered_df,
                x="Has Table booking",
                y="Aggregate rating",
                color="Has Table booking",
                color_discrete_map={"Yes": "#2196F3", "No": "#FF9800"},
                title="Table Booking vs Rating"
            )
            st.plotly_chart(fig_book, use_container_width=True)

# ==========================================
# TAB 3: Cuisine & Pricing Trends
# ==========================================
with tab3:
    col_cui1, col_cui2 = st.columns(2)

    with col_cui1:
        st.subheader("Top 15 Cuisines Offered")
        top_cuisines_df = get_top_cuisines(filtered_df, top_n=15)
        if not top_cuisines_df.empty:
            fig_cuisine = px.bar(
                top_cuisines_df,
                x="Count",
                y="Cuisine",
                orientation="h",
                color="Count",
                color_continuous_scale="Inferno"
            )
            fig_cuisine.update_layout(yaxis=dict(autorange="reversed"))
            st.plotly_chart(fig_cuisine, use_container_width=True)
        else:
            st.info("No cuisine data available.")

    with col_cui2:
        st.subheader("Top 10 Most Voted Restaurants")
        most_voted_df = get_most_voted_restaurants(filtered_df, top_n=10)
        if not most_voted_df.empty:
            fig_voted = px.bar(
                most_voted_df,
                x="Restaurant Name",
                y="Votes",
                color="Votes",
                color_continuous_scale="Teal"
            )
            fig_voted.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig_voted, use_container_width=True)
        else:
            st.info("No restaurant vote data available.")

    st.subheader("Top Rated Restaurants (Min. 1,000 Votes)")
    top_rated_df = get_top_rated_restaurants(filtered_df, min_votes=1000, top_n=10)
    if not top_rated_df.empty:
        st.dataframe(top_rated_df, use_container_width=True)
    else:
        st.info("No restaurants found matching the minimum 1,000 votes threshold in the current selection.")

# ==========================================
# TAB 4: Raw Data Explorer
# ==========================================
with tab4:
    st.subheader("Dataset Explorer")

    available_cols = list(filtered_df.columns)
    default_cols = [
        col for col in [
            "Restaurant Name", "Country", "City", "Cuisines", 
            "Average Cost for two", "Currency", "Aggregate rating", "Votes"
        ] if col in available_cols
    ]

    show_cols = st.multiselect(
        "Select columns to display:",
        options=available_cols,
        default=default_cols
    )

    st.dataframe(filtered_df[show_cols], use_container_width=True, height=450)

    # Export filtered data
    csv_bytes = filtered_df[show_cols].to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Filtered Data as CSV",
        data=csv_bytes,
        file_name="zomato_filtered_data.csv",
        mime="text/csv"
    )
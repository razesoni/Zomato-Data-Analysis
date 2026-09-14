# Zomato Restaurant Analytics
## Exploratory Data Analysis & Interactive Dashboard

A comprehensive exploratory data analysis (EDA) and interactive Streamlit dashboard for analyzing global Zomato restaurant data across ratings, cuisines, pricing, and service availability.

---

## 📊 Project Overview

This project analyzes a comprehensive dataset of **9,542+ restaurants** across **15+ countries** to uncover patterns in restaurant ratings, pricing strategies, cuisine popularity, and service adoption. The analysis combines statistical exploration with interactive visualizations to provide actionable insights into the global restaurant ecosystem.

**Dataset:** Zomato Restaurants Dataset  
**Columns Analyzed:** 21 key features including ratings, cuisines, pricing, location, and service availability  
**Analysis Tools:** Python, Pandas, NumPy, Matplotlib, Seaborn, Plotly

---

## 🔍 Key Findings & Insights

### 1. **Dataset Quality & Structure**
- **Total Records:** 9,542 restaurants (after data cleaning)
- **Geographic Coverage:** 15+ countries with India as the largest market
- **Data Completeness:** 99.9% complete with only 9 missing values in the Cuisines column
- **No Duplicate Entries:** Clean dataset with zero duplicate records
- **Rating Scale:** Aggregate ratings range from 0.0 to 4.9 out of 5.0

### 2. **Rating Patterns & Distribution**
- **Average Rating:** 2.67 / 5.0 (median: 3.2)
- **Rating Categories:** 
  - Dark Green (Excellent): 4.5–4.9 rating range
  - Green (Very Good): 3.9–4.4 rating range
  - Yellow (Good): 3.0–3.8 rating range
  - Orange/Red (Poor): Below 3.0 rating range
- **Voting Engagement:** Average 156.8 votes per restaurant, with top restaurants reaching 10,934+ votes
- **Key Insight:** Higher-rated restaurants attract significantly more customer engagement and reviews

### 3. **Service Availability Impact**
- **Online Delivery:** Mixed adoption across regions; strong correlation between delivery availability and customer engagement
- **Table Booking:** Premium restaurants (higher price ranges) more likely to offer table reservations
- **Service & Rating Correlation:** Restaurants offering both services tend to have slightly higher ratings, suggesting customer convenience influences satisfaction

### 4. **Price Range Segmentation**
- **Price Range Distribution:** Scale of 1–4, with median of 2.0
- **Average Cost for Two:** Wide variance from $0–$800,000 across different currencies
- **Median Cost:** $400 (in local currencies), indicating mid-range restaurants dominate the platform
- **Premium Positioning:** Higher price ranges correlate with higher ratings and greater vote counts

### 5. **Cuisine Diversity**
- **Top Cuisines:** North Indian, Chinese, Fast Food, Mughlai, Continental, Cafe, Bakery (dominant in Indian markets)
- **Cuisine Diversity:** Many restaurants offer multiple cuisine types, reflecting fusion trends
- **Regional Variations:** Cuisine preferences vary significantly by geography and culture
- **Key Insight:** Cuisine type influences restaurant positioning and pricing strategies

### 6. **Geographic Patterns**
- **Top Markets:**
  - **India:** Largest market share with focus on budget to mid-range dining
  - **United States:** Premium dining with higher price points
  - **United Arab Emirates:** Mixed market with luxury and casual segments
  - **United Kingdom:** European-style dining preferences
  - **Turkey:** Growing market with distinct cuisine preferences
  
- **City-Level Insights:** Major metropolitan areas show higher restaurant density and competitive pricing
- **Coordinate Data:** All restaurants properly geotagged for location-based analysis

### 7. **Customer Engagement Metrics**
- **Votes Statistics:**
  - Mean: 156.8 votes
  - Median: 31 votes
  - Maximum: 10,934 votes
  - 75th Percentile: 130 votes
- **Engagement Pattern:** Top 10% of restaurants receive 60%+ of total votes
- **Review Activity:** Positive correlation between votes and ratings (higher-rated restaurants more likely to be reviewed)

### 8. **Data Insights Summary**
| Metric | Value | Insight |
|--------|-------|---------|
| Total Restaurants | 9,542 | Substantial market coverage |
| Countries | 15+ | Global dataset with regional diversity |
| Avg Rating | 2.67/5.0 | Mid-range typical satisfaction |
| Median Price Range | 2 (1–4 scale) | Mid-tier dining dominance |
| Online Delivery Available | 30–45% (regional variance) | Growing but not universal |
| Table Booking Available | 25–35% (regional variance) | Premium segment feature |
| Top Cuisine Type | North Indian/Chinese | Regional dependency |

---

## 📈 Analysis Methodology

### Data Cleaning Process
1. Loaded dataset with latin-1 encoding to handle international characters
2. Identified and removed 9 null values from Cuisines column
3. Verified zero duplicate records
4. Validated geographic coordinates (latitude/longitude)
5. Standardized currency and price representations

### Exploration Steps
1. **Missing Values Analysis:** Minimal data loss with targeted imputation
2. **Numerical Exploration:** Descriptive statistics for ratings, votes, costs
3. **Categorical Exploration:** Cuisine distributions, service availability patterns
4. **Relationship Analysis:** Correlation between ratings, votes, pricing, and services

---

## 🛠️ Included Components

### Core Analysis
- **`notebooks/zomato_analysis.ipynb`** — Complete exploratory data analysis with visualizations and statistical summaries
- **`notebooks/split_notebook.py`** — Utility to modularize the main notebook

### Application & Deployment
- **`app.py`** — Interactive Streamlit dashboard featuring:
  - Geographic and distribution analysis
  - Rating dynamics and service impact
  - Cuisine and pricing trends
  - Raw data explorer with export functionality
  
- **`src/utils.py`** — Data loading, cleaning, and dashboard helper functions
- **`requirements.txt`** — Python dependencies (Pandas, NumPy, Matplotlib, Seaborn, Streamlit, Plotly)

### Data Files
- **`data/raw/zomato-dataset.csv`** — Complete restaurant dataset
- **`data/raw/Country-Code.csv`** — Country code mapping reference

### Deployment
- **`Dockerfile`** — Container configuration for reproducible deployment
- **`docker-compose.yml`** — Multi-container orchestration
- **`DEPLOYMENT.md`** — Detailed deployment instructions

---

## 🚀 Running the Project

### Prerequisites
- Python 3.11+ (for compatibility with pinned NumPy/Pandas versions)
- Virtual environment recommended

### Local Setup
```bash
# Clone the repository
git clone https://github.com/razesoni/Zomato-Data-Analysis.git
cd Zomato-Data-Analysis

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
python -m pip install -r requirements.txt

# Run the Streamlit dashboard
python -m streamlit run app.py
```

Open the URL printed by Streamlit (typically `http://localhost:8501`) in your browser.

### Jupyter Notebook Exploration
```bash
# Open the original analysis notebook
jupyter notebook notebooks/zomato_analysis.ipynb
```
Note: Verify dataset paths in the notebook match your repository structure.

### Docker Deployment
```bash
# Build and run with Docker Compose
docker-compose up --build

# Access the application at http://localhost:8501
```

For detailed deployment instructions, see [`DEPLOYMENT.md`](DEPLOYMENT.md).

---

## 📊 Dashboard Features

### Tab 1: Geographic & Share Analysis
- **Global Restaurant Distribution:** Pie chart showing market share by country
- **Top Cities by Volume:** Horizontal bar chart of restaurant concentration
- **Geolocation Map:** Interactive Mapbox visualization with restaurant markers

### Tab 2: Rating Dynamics
- **Rating Distribution by Category:** Breakdown of restaurants by rating color/quality tier
- **Votes vs. Ratings:** Scatter plot correlation analysis
- **Service Impact:** Box plots comparing online delivery and table booking effects on ratings

### Tab 3: Cuisine & Pricing Trends
- **Top 15 Cuisines:** Frequency analysis of cuisine types
- **Most Voted Restaurants:** Top performers by review volume
- **Top-Rated Restaurants:** Table view of highly-rated establishments (min. 1,000 votes)

### Tab 4: Raw Data Explorer
- **Column Selection:** Customize displayed fields
- **Interactive Table:** Sort and filter restaurant data
- **CSV Export:** Download filtered results for further analysis

### Interactive Filters (Sidebar)
- **Countries:** Multi-select to focus analysis on specific regions
- **Cities:** Dynamic list based on selected countries
- **Rating Range:** Slider to filter by aggregate rating
- **Online Delivery:** Toggle filter for delivery availability
- **Table Booking:** Toggle filter for reservation capability

---

## 💡 Key Questions Explored

✅ **How do restaurant ratings differ across cuisines, cities, and booking/delivery options?**
✅ **What is the relationship between vote count and ratings?**
✅ **How does pricing correlate with customer satisfaction?**
✅ **Which cuisines dominate different geographic markets?**
✅ **Do restaurants with delivery/booking services receive higher ratings?**
✅ **What is the distribution of price ranges across countries?**

---

## 🎯 Use Cases & Applications

1. **Restaurant Marketing:** Identify high-performing cuisines and services in target markets
2. **Business Intelligence:** Benchmark pricing and ratings against competitors
3. **Market Entry Strategy:** Analyze cuisine popularity and service adoption by region
4. **Customer Insights:** Understand rating patterns and engagement trends
5. **Data-Driven Decision Making:** Use statistical findings for restaurant planning and expansion

---

## ⚠️ Interpretation & Limitations

### Important Considerations
- **Observational Analysis:** Restaurant ratings and services do not establish causation—ratings may reflect multiple unobserved factors
- **Unrated Restaurants:** Some entries have zero ratings; exclude when calculating rating-based metrics
- **Currency Variation:** Price comparisons require context-aware currency conversion
- **Sampling Bias:** Dataset concentrates on urban, digitally-active markets represented on Zomato
- **Temporal Variability:** Data represents a snapshot; ratings and services may have changed since collection
- **Geographic Limitations:** Not all countries/cities equally represented; some markets underrepresented

### Data Quality Notes
- Verify sample sizes when comparing across small subgroups
- Use median values for skewed distributions (e.g., votes, costs)
- Consider country/currency context when interpreting price insights
- Cross-validate findings with supplementary data sources

---

## 📋 Data Dictionary

| Column | Type | Description |
|--------|------|-------------|
| Restaurant ID | Integer | Unique identifier |
| Restaurant Name | String | Business name |
| Country Code | Integer | ISO country code |
| City | String | City location |
| Cuisines | String | Comma-separated cuisine types |
| Average Cost for Two | Integer | Estimated cost (local currency) |
| Price Range | Integer | 1–4 scale |
| Aggregate Rating | Float | Average rating (0.0–5.0) |
| Votes | Integer | Total customer ratings count |
| Has Online Delivery | String | "Yes" or "No" |
| Has Table Booking | String | "Yes" or "No" |
| Rating Color | String | Visual category (Dark Green, Green, Yellow, Orange, Red, White) |
| Rating Text | String | Text category (Excellent, Very Good, Good, etc.) |

---

## 🔄 Reproducibility & Next Steps

### To Ensure Reproducibility
1. Use pinned Python 3.11 and dependencies from `requirements.txt`
2. Verify dataset paths match your environment
3. Run the notebook end-to-end before modifying code
4. Use the Dockerfile for consistent containerized execution

### Recommended Enhancements
- 📊 Publish three reproducible findings with detailed methodology
- ✅ Implement automated data quality tests
- 🧪 Validate Docker deployment in a clean environment
- 📈 Add time-series analysis if temporal data becomes available
- 🌐 Expand geographic coverage and regional segmentation
- 🔗 Integrate external datasources (e.g., reviews, social media sentiment)

---

## 🤝 Contributing

Contributions are welcome! Please review [`CONTRIBUTING.md`](CONTRIBUTING.md) for guidelines on:
- Code style and standards
- Testing requirements
- Pull request process
- Issue reporting

---

## 📄 License & Attribution

This project analyzes publicly available Zomato restaurant data from [Kaggle](https://www.kaggle.com/datasets/shrutimehta/zomato-restaurants-data). Please verify dataset redistribution terms before reusing.

---

## 📞 Support & Feedback

For questions, issues, or suggestions:
- 📧 Open an issue on GitHub
- 💬 Review existing discussions
- 📚 Check the documentation in `notebooks/` and `DEPLOYMENT.md`

---

**Last Updated:** 2025 | **Analysis Period:** Global Zomato Dataset | **Status:** ✅ Active
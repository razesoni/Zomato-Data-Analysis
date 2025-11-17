# Zomato Restaurant Data Analysis

An exploratory data analysis (EDA) of the Zomato restaurant dataset using Python, Pandas, and Seaborn.

## Project Overview

This project performs an exploratory data analysis (EDA) on the Zomato dataset. The main objective is to analyze restaurant data to uncover patterns, identify trends, and understand the factors that influence restaurant ratings, cost, and popularity.

---

## Dataset

The dataset used is `zomato-dataset.csv`, which was sourced from https://www.kaggle.com/datasets/shrutimehta/zomato-restaurants-data. It contains 9,551 records of restaurants from various cities.

The key columns in this dataset include:
* **Restaurant ID:** Unique ID for each restaurant
* **Restaurant Name:** Name of the restaurant
* **City:** City where the restaurant is located
* **Cuisines:** Types of cuisines offered
* **Average Cost for two:** The average cost for two people
* **Has Table booking:** Whether the restaurant has table booking
* **Has Online delivery:** Whether the restaurant offers online delivery
* **Price range:** The price range of the restaurant (1-4)
* **Aggregate rating:** The average rating of the restaurant (out of 5)
* **Rating text:** A categorical description of the rating (e.g., "Good", "Excellent")
* **Votes:** The number of votes the restaurant has received

---

## Key Questions Addressed

This analysis aims to answer the following questions:

1.  What is the overall distribution of restaurant ratings?
2.  How do services like **table booking** and **online delivery** impact a restaurant's rating?
3.  What is the relationship between the **average cost** and the **aggregate rating**?
4.  Which **cities** have the highest concentration of restaurants in the dataset?
5.  What are the most popular **cuisines**?
6.  Is there a correlation between the number of **votes** and the **rating**?

---

## Analysis Workflow

The analysis was conducted in a Jupyter Notebook (`zomato_analysis.ipynb`) and followed these steps:

1.  **Data Loading:** Imported the dataset using Pandas, specifying `latin-1` encoding.
2.  **Data Cleaning:**
    * Checked for and handled missing values (found in the `Cuisines` column).
    * Checked for and removed any duplicate rows.
3.  **Exploratory Data Analysis (EDA):**
    * Generated descriptive statistics for numerical columns (`Aggregate rating`, `Votes`, `Average Cost for two`).
    * Examined the value counts for categorical columns (`City`, `Cuisines`, `Rating text`).
4.  **Data Visualization:**
    * Used **Seaborn** and **Matplotlib** to create plots to answer the key questions.
    * **Histogram:** To show the distribution of aggregate ratings.
    * **Bar Charts:** To compare restaurant counts by city and cuisine types.
    * **Box Plots:** To compare ratings for restaurants with/without table booking and online delivery.
    * **Scatter Plots:** To explore the relationship between rating vs. votes and rating vs. cost.

---

## Key Findings

* **Finding 1:** There were nine missing values in the Cuisines column
* **Finding 2:** Maximum Transactions were done in India
* **Finding 2:** The majority of restaurants have an aggregate rating between 2.8 and 4.0.
* **Finding 3:** Restaurants that offer **table booking** have a significantly higher average rating than those that do not.
* **Finding 4:** There is a positive correlation between the number of **votes** and the **aggregate rating**; more votes generally mean a higher (and more reliable) rating. 

---

## Tools and Libraries Used

* **Python 3:** The core programming language.
* **Pandas:** For data manipulation and analysis.
* **NumPy:** For numerical operations.
* **Matplotlib:** For basic data visualization.
* **Seaborn:** For advanced statistical visualization.
* **Jupyter Notebook:** As the interactive development environment.

---

## How to Use This Repository

1.  Clone the repository to your local machine:
    ```bash
    git clone [https://github.com/razesoni/Zomato-Data-Analysis.git](https://github.com/razesoni/Zomato-Data-Analysis.git)
    ```
2.  Install the required libraries:
    ```bash
    pip install pandas numpy matplotlib seaborn
    ```
3.  Open the Jupyter Notebook to view the analysis:
    ```bash
    jupyter notebook zomato_analysis.ipynb
    ```
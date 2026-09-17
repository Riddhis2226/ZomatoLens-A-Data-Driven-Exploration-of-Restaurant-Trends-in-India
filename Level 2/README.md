# Level 2 — Geospatial, Structural & Restaurant-Entity Analysis

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Charts%20%26%20Maps-3F4F75?logo=plotly&logoColor=white)

[← Root](../README.md) · [← Level 1](../Level%201/README.md) · [Level 3 →](../Level%203/README.md)

## Objective

Level 2 moves past simple counts into structure: how ratings are distributed, which cuisine pairings tend to rate well, where restaurants cluster geographically, and how multi-branch chains compare to single-location restaurants. All four official Cognifyz Level 2 tasks are implemented.

## Task coverage

| # | Task | Notebook | Status |
|---|---|---|---|
| 1 | Restaurant rating distribution | `Task 1/Task 1.ipynb` | ✅ |
| 2 | Cuisine combination analysis | `Task 2/Task 2.ipynb` | ✅ |
| 3 | Geographic analysis | `Task 3/Task 3.ipynb` | ✅ |
| 4 | Restaurant chain analysis | `Task 4/Task 4.ipynb` | ✅ |

## Task-by-task analysis

### Task 1 — Rating distribution

Restaurants with a nonzero `Aggregate rating` are plotted as a **histogram** and a **boxplot** to show both the shape and spread of ratings, alongside a bar chart of the six `Rating text` categories (Excellent, Very Good, Good, Average, Poor, Not rated) and the mean number of votes across all restaurants. Verified result: the dataset averages **156.9 votes per restaurant**, and the most common rating category is **"Average"** (3,737 restaurants), followed by **"Not rated"** (2,148).

### Task 2 — Cuisine combination analysis

Rather than single cuisines, this task groups by the full `Cuisines` string as listed (e.g. "North Indian, Chinese" is its own combination), then filters to combinations with more than 20 restaurants before ranking by average rating. That 20-restaurant threshold is a methodological choice: it keeps small, noisy combinations from dominating a "top-rated" ranking on the strength of two or three unusually well-reviewed restaurants, at the cost of excluding rarer combinations entirely. Verified top combinations by average rating (min. 20 restaurants): **American (3.67, n=31)**, **Italian (3.66, n=54)**, and **Italian, Pizza (3.64, n=24)**.

### Task 3 — Geographic analysis

Restaurant locations are plotted with `Plotly`'s `scatter_mapbox`, rendered over free **OpenStreetMap** tiles nationally and **CARTO Positron** tiles for the city-level zooms — no paid Mapbox API key is required. One national map plots all restaurants (sized by votes, colored by rating), and three city-level maps zoom into **New Delhi, Mumbai, and Bangalore** individually.

### Task 4 — Restaurant chain analysis

A restaurant name that appears more than once in the dataset is treated as a chain. Of **7,446 unique restaurant names, 734 appear at more than one location**. The dashboard tracks branch count, average rating, and total votes as three separate metrics rather than collapsing them into one score — a chain can have many branches without being highly rated, or few branches with very high engagement. By branch count, **Cafe Coffee Day (83)**, **Domino's Pizza (79)**, and **Subway (63)** lead; by total votes across branches, **Barbeque Nation (26 branches, 4.35 avg. rating, 28,142 votes)** tops the ranking, ahead of higher-rated but smaller chains like **AB's – Absolute Barbecues (4 branches, 4.83 avg. rating)**.

## Visual outputs

Level 2's notebooks export static PNG charts rather than interactive HTML:

- **Task 1:** [`Distribution of Restaurant Ratings.png`](Task%201/Distribution%20of%20Restaurant%20Ratings.png), [`Boxplot - Spread of Restaurant Ratings.png`](Task%201/Boxplot%20-%20Spread%20of%20Restaurant%20Ratings.png), [`Restaurant Count by Rating Category.png`](Task%201/Restaurant%20Count%20by%20Rating%20Category.png)
- **Task 2:** [`Top 20 Cuisine Combinations by Average Rating.png`](Task%202/Top%2020%20Cuisine%20Combinations%20by%20Average%20Rating.png)
- **Task 3:** [`Restaurant Ratings & Votes Across India.png`](Task%203/Restaurant%20Ratings%20%26%20Votes%20Across%20India.png), plus city-zoomed maps for [New Delhi](Task%203/Restaurant%20Ratings%20in%20New%20Delhi.png), [Mumbai](Task%203/Restaurant%20Ratings%20in%20Mumbai.png), and [Bangalore](Task%203/Restaurant%20Ratings%20in%20Bangalore.png)
- **Task 4:** [`Top 15 Restaurant Chains by Popularity (Votes).png`](Task%204/Top%2015%20Restaurant%20Chains%20by%20Popularity%20%28Votes%29.png)

## Key findings

| Metric | Value |
|---|---|
| Average votes per restaurant | 156.9 |
| Most common rating category | "Average" (3,737 restaurants) |
| Highest-rated cuisine combo (min. 20 restaurants) | American — 3.67 avg. rating |
| Chains with multiple branches | 734 of 7,446 unique restaurant names |
| Most-branched chain | Cafe Coffee Day — 83 branches |
| Highest-engagement chain (by total votes) | Barbeque Nation — 28,142 votes across 26 branches |

## Data export

The dashboard's **Export CSV** button writes a combined `level2_summary.csv` covering rating-category counts, filtered cuisine combinations, geographic summary data, and the top-15 chain table.

## Technical stack

| Tool | Purpose |
|---|---|
| Python 3 | Core language |
| Pandas | Grouping and aggregation |
| Plotly Express & Graph Objects | Histograms, boxplots, bar charts |
| Plotly `scatter_mapbox` (OpenStreetMap / CARTO) | Geospatial visualization |
| Streamlit | Dashboard frontend |
| Custom CSS (`style.css`) | Dark, glass-panel dashboard theme |

## Project structure

```
Level 2/
├── level2_dashboard.py
├── style.css
├── Data Analysis Internship__Dataset__Cognifyz Technologies.csv
├── Task 1/
│   ├── Task 1.ipynb
│   ├── Distribution of Restaurant Ratings.png
│   ├── Boxplot - Spread of Restaurant Ratings.png
│   └── Restaurant Count by Rating Category.png
├── Task 2/
│   ├── Task 2.ipynb
│   └── Top 20 Cuisine Combinations by Average Rating.png
├── Task 3/
│   ├── Task 3.ipynb
│   ├── Restaurant Ratings & Votes Across India.png
│   ├── Restaurant Ratings in New Delhi.png
│   ├── Restaurant Ratings in Mumbai.png
│   └── Restaurant Ratings in Bangalore.png
└── Task 4/
    ├── Task 4.ipynb
    └── Top 15 Restaurant Chains by Popularity (Votes).png
```

## Run instructions

```bash
pip install streamlit pandas plotly
cd "Level 2"
streamlit run level2_dashboard.py
```

Then open `http://localhost:8501`. The dataset CSV and `style.css` must stay alongside `level2_dashboard.py`.

## Relationship to overall architecture

Level 2 builds on the cuisine and city groundwork from [Level 1](../Level%201/README.md) and adds spatial and entity structure — the geography and chains identified here feed conceptually into [Level 3](../Level%203/README.md), where votes and price tier are examined against ratings and service offerings. See the [root README](../README.md) for the full picture.

# Level 2 — Geospatial, Structural & Restaurant-Entity Analysis

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Charts%20%26%20Maps-3F4F75?logo=plotly&logoColor=white)

[← Root](../README.md) · [← Level 1](../Level%201/README.md) · [Level 3 →](../Level%203/README.md)

## Objective

Structure beyond counts: rating distribution, cuisine-combination performance, geographic clustering, chain behavior. All 4 official Cognifyz Level 2 tasks implemented.

## Task coverage

| # | Task | Notebook | Status |
|---|---|---|---|
| 1 | Restaurant rating distribution | `Task 1/Task 1.ipynb` | ✅ |
| 2 | Cuisine combination analysis | `Task 2/Task 2.ipynb` | ✅ |
| 3 | Geographic analysis | `Task 3/Task 3.ipynb` | ✅ |
| 4 | Restaurant chain analysis | `Task 4/Task 4.ipynb` | ✅ |

## Task 1 — Rating distribution

- **Method:** nonzero `Aggregate rating` values plotted as histogram + boxplot; `Rating text` categories counted; mean votes computed across all restaurants
- **Result:**

| Metric | Value |
|---|---|
| Avg. votes per restaurant | **156.9** |
| Most common rating category | "Average" — **3,737** restaurants |
| Second most common | "Not rated" — 2,148 restaurants |

## Task 2 — Cuisine combination analysis

- **Method:** grouped by the full `Cuisines` string as listed (e.g. "North Indian, Chinese" is its own combo), filtered to combos with **>20 restaurants** before ranking by average rating
- **Why the threshold:** prevents small, noisy combinations from topping the ranking on 2–3 unusually well-rated restaurants; trade-off is excluding rarer combos entirely
- **Result (min. 20 restaurants):**

| Rank | Combo | Avg. rating | n |
|---|---|---|---|
| 1 | American | **3.67** | 31 |
| 2 | Italian | 3.66 | 54 |
| 3 | Italian, Pizza | 3.64 | 24 |

## Task 3 — Geographic analysis

- **Method:** `Plotly scatter_mapbox` over free **OpenStreetMap** (national) and **CARTO Positron** (city zooms) tiles — no paid Mapbox API key
- **Maps:** 1 national (all restaurants, sized by votes, colored by rating) + 3 city zooms — **New Delhi, Mumbai, Bangalore**

## Task 4 — Restaurant chain analysis

- **Method:** a restaurant name appearing more than once = a chain; branch count, average rating, and total votes tracked as **three separate metrics** (not collapsed into one score)
- **Result:**

| Metric | Value |
|---|---|
| Unique restaurant names | 7,446 |
| Names with >1 branch | **734** |
| Most-branched chain | Cafe Coffee Day — **83** branches |
| Highest-engagement chain (total votes) | Barbeque Nation — **28,142** votes across 26 branches, 4.35 avg. rating |
| Highest-rated small chain | AB's – Absolute Barbecues — 4.83 avg. rating, 4 branches |

## Visual outputs

| Task | Files |
|---|---|
| 1 | [`Distribution of Restaurant Ratings.png`](Task%201/Distribution%20of%20Restaurant%20Ratings.png) · [`Boxplot - Spread of Restaurant Ratings.png`](Task%201/Boxplot%20-%20Spread%20of%20Restaurant%20Ratings.png) · [`Restaurant Count by Rating Category.png`](Task%201/Restaurant%20Count%20by%20Rating%20Category.png) |
| 2 | [`Top 20 Cuisine Combinations by Average Rating.png`](Task%202/Top%2020%20Cuisine%20Combinations%20by%20Average%20Rating.png) |
| 3 | [`Restaurant Ratings & Votes Across India.png`](Task%203/Restaurant%20Ratings%20%26%20Votes%20Across%20India.png) · [New Delhi](Task%203/Restaurant%20Ratings%20in%20New%20Delhi.png) · [Mumbai](Task%203/Restaurant%20Ratings%20in%20Mumbai.png) · [Bangalore](Task%203/Restaurant%20Ratings%20in%20Bangalore.png) |
| 4 | [`Top 15 Restaurant Chains by Popularity (Votes).png`](Task%204/Top%2015%20Restaurant%20Chains%20by%20Popularity%20%28Votes%29.png) |

## Key findings

| Metric | Value |
|---|---|
| Avg. votes per restaurant | 156.9 |
| Most common rating category | "Average" (3,737) |
| Top cuisine combo (min. 20 restaurants) | American — 3.67 |
| Chains with multiple branches | 734 / 7,446 |
| Most-branched chain | Cafe Coffee Day — 83 |
| Top chain by engagement | Barbeque Nation — 28,142 votes |

## Data export

**Export CSV** → `level2_summary.csv` (rating-category counts, filtered cuisine combos, geographic summary, top-15 chains).

## Technical stack

| Tool | Purpose |
|---|---|
| Python 3 | Core language |
| Pandas | Grouping, aggregation |
| Plotly Express & Graph Objects | Histograms, boxplots, bar charts |
| Plotly `scatter_mapbox` (OSM / CARTO) | Geospatial visualization |
| Streamlit | Dashboard frontend |
| Custom CSS (`style.css`) | Dark, glass-panel theme |

## Project structure

```
Level 2/
├── level2_dashboard.py
├── style.css
├── Data Analysis Internship__Dataset__Cognifyz Technologies.csv
├── Task 1/  → Task 1.ipynb + 3 PNG exports
├── Task 2/  → Task 2.ipynb + 1 PNG export
├── Task 3/  → Task 3.ipynb + 4 PNG exports
└── Task 4/  → Task 4.ipynb + 1 PNG export
```

## Run instructions

```bash
pip install streamlit pandas plotly
cd "Level 2"
streamlit run level2_dashboard.py
```

Open `http://localhost:8501`. CSV and `style.css` must stay alongside `level2_dashboard.py`.

## Relationship to overall architecture

Builds on Level 1's cuisine/city groundwork with spatial and entity structure. Geography and chains here feed conceptually into [Level 3](../Level%203/README.md), which examines votes and price tier against ratings and service offerings. Full picture: [root README](../README.md).

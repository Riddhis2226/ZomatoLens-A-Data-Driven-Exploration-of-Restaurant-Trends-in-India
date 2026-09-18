# Level 1 — Foundational / Descriptive Analytics

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Charts-3F4F75?logo=plotly&logoColor=white)

[← Root](../README.md) · [Level 2 →](../Level%202/README.md)

## Objective

Baseline read on the dataset — cuisine share, city distribution, price tiers, delivery adoption. Descriptive only: counts, percentages, group averages. No correlation or text analysis (that's Levels 2–3).

## Task coverage

| # | Task | Notebook | Status |
|---|---|---|---|
| 1 | Top cuisines | `Task 1/top_cuisines.ipynb` | ✅ |
| 2 | City-wise restaurant & rating analysis | `Task 2/city_analysis.ipynb` | ✅ |
| 3 | Price-range distribution | `Task 3/price_range.ipynb` | ✅ |
| 4 | Online delivery impact | `Task 4/online_delivery_advanced.ipynb` | ✅ |

**Pattern across all 4 tasks:** split/group column with Pandas → compute counts & percentages against the full 9,551-row dataset → render as 2–3 complementary Plotly chart types (ranking, share, comparison).

## Task 1 — Top cuisines

- **Method:** `Cuisines` is comma-separated and multi-label; split and exploded before counting, so a listing of "North Indian, Chinese" counts toward both.
- **Charts:** lollipop (ranking) + donut (share)
- **Result:**

| Rank | Cuisine | Share |
|---|---|---|
| 1 | North Indian | **41.5%** |
| 2 | Chinese | **28.6%** |
| 3 | Fast Food | **20.8%** |

  Percentages exceed 100% combined — cuisines overlap.

## Task 2 — City-wise analysis

- **Method:** top-10 city ranking by count; average-rating ranking restricted to cities with >30 restaurants, filtering out single-restaurant outliers
- **Charts:** horizontal bar (count ranking) + heatmap-style bar (rating ranking)
- **Result:**

| City | Restaurants |
|---|---|
| New Delhi | **5,473** |
| Gurgaon | 1,118 |
| Noida | 1,080 |

  Concentration reflects the dataset's Delhi-NCR skew.

## Task 3 — Price-range distribution

- **Method:** grouped into Zomato's 4 price tiers (1 = budget, 4 = luxury)
- **Charts:** bar + donut, each annotated with share
- **Result:** Budget **46.5%** · Mid **32.6%** · Premium **14.7%** · Luxury **6.1%**

## Task 4 — Online delivery impact

- **Method:** split by delivery availability; average rating compared across the split
- **Charts:** donut (adoption share) + combined bar/line (count vs. rating)
- **Result:**

| Group | Share | Avg. rating |
|---|---|---|
| Offers delivery | **25.7%** | **3.25** |
| No delivery | 74.3% | 2.47 |

  A +0.78 rating gap — not tested for causality.

## Exported outputs

| Task | Files |
|---|---|
| 1 | [`top_cuisines_lollipop.html`](Task%201/top_cuisines_lollipop.html) · [`top_cuisines_donut.html`](Task%201/top_cuisines_donut.html) · `top_3_cuisines_plotly.html` |
| 2 | [`top_cities_restaurant_count_bar.html`](Task%202/top_cities_restaurant_count_bar.html) · [`city_distribution_treemap.html`](Task%202/city_distribution_treemap.html) · [`top_cities_avg_rating_heatmap.html`](Task%202/top_cities_avg_rating_heatmap.html) |
| 3 | [`price_range_distribution_bar.html`](Task%203/price_range_distribution_bar.html) · [`price_range_distribution_donut.html`](Task%203/price_range_distribution_donut.html) · [`price_range_lollipop.html`](Task%203/price_range_lollipop.html) |
| 4 | [`online_delivery_pie_enhanced.html`](Task%204/online_delivery_pie_enhanced.html) · [`delivery_rating_comparison_grouped.html`](Task%204/delivery_rating_comparison_grouped.html) · [`online_delivery_rating_sankey_clean.html`](Task%204/online_delivery_rating_sankey_clean.html) — Sankey of delivery → rating flow, exported but not in the live dashboard |

Task 2's treemap export isn't part of the consolidated dashboard.

## Key findings

| Metric | Value |
|---|---|
| Dominant cuisine | North Indian — 41.5% |
| Most-listed city | New Delhi — 5,473 restaurants |
| Most common price tier | Budget — 46.5% |
| Online delivery adoption | 25.7% |
| Rating gap by delivery | +0.78 |

## Data export

**Export CSV** button in-app → `level1_summary.csv` (top cuisines, city summary, price distribution).

## Technical stack

| Tool | Purpose |
|---|---|
| Python 3 | Core language |
| Pandas, NumPy | Loading, splitting, aggregation |
| Plotly Express & Graph Objects | Lollipop, donut, bar, combo charts |
| Streamlit | Dashboard frontend |
| Custom CSS (`style.css`) | Dark, glass-panel theme |

## Project structure

```
Level 1/
├── level1_dashboard.py
├── style.css
├── Data Analysis Internship__Dataset__Cognifyz Technologies.csv
├── Task 1/  → top_cuisines.ipynb + 3 HTML exports
├── Task 2/  → city_analysis.ipynb + 3 HTML exports
├── Task 3/  → price_range.ipynb + 3 HTML exports
└── Task 4/  → online_delivery_advanced.ipynb + 3 HTML exports
```

## Run instructions

```bash
pip install streamlit pandas numpy plotly
cd "Level 1"
streamlit run level1_dashboard.py
```

Open `http://localhost:8501`. CSV and `style.css` must stay in this folder.

## Relationship to overall architecture

Descriptive base for ZomatoLens. [Level 2](../Level%202/README.md) adds geography and chain structure on top of the cuisine/city dimensions here; [Level 3](../Level%203/README.md) adds text, correlation, and service-adoption analysis. Full picture: [root README](../README.md).

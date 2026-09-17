# Level 1 — Foundational / Descriptive Analytics

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Charts-3F4F75?logo=plotly&logoColor=white)

[← Root](../README.md) · [Level 2 →](../Level%202/README.md)

## Objective

Level 1 establishes the baseline read on the restaurant dataset: which cuisines dominate, how restaurants are distributed across cities, how they're priced, and how many offer online delivery. Everything here is descriptive — counts, percentages, and group averages — with no correlation or text analysis yet; those come in Levels 2 and 3.

## Task coverage

All four official Cognifyz Level 1 tasks are implemented, each with its own notebook and a matching section in the consolidated dashboard.

| # | Task | Notebook | Status |
|---|---|---|---|
| 1 | Top cuisines | `Task 1/top_cuisines.ipynb` | ✅ |
| 2 | City-wise restaurant & rating analysis | `Task 2/city_analysis.ipynb` | ✅ |
| 3 | Price-range distribution | `Task 3/price_range.ipynb` | ✅ |
| 4 | Online delivery impact | `Task 4/online_delivery_advanced.ipynb` | ✅ |

## Methodology

Each task follows the same pattern: split or group the relevant column with Pandas, compute counts and percentages against the full 9,551-row dataset, then render the result with two or three complementary Plotly chart types so the same distribution can be read as a ranking (lollipop/bar), a share (donut), or a comparison (grouped bar + line).

### Task 1 — Top cuisines

`Cuisines` is a comma-separated multi-label field, so it's split and exploded before counting — a restaurant listing "North Indian, Chinese" contributes to both cuisine counts. A **lollipop chart** ranks the top three cuisines by restaurant count, and a **donut chart** shows their share of the total. Verified result: **North Indian leads at 41.5%** of restaurants, followed by **Chinese (28.6%)** and **Fast Food (20.8%)** — note these percentages don't sum to 100% because cuisines overlap.

### Task 2 — City-wise analysis

A **horizontal bar chart** ranks the top 10 cities by restaurant count, and a second bar chart (styled as a heatmap-style ranking) surfaces the top 10 cities by average rating, restricted to cities with more than 30 restaurants so single-restaurant outliers don't dominate. Verified result: **New Delhi has the most restaurants (5,473)**, with Gurgaon (1,118) and Noida (1,080) well behind — reflecting the dataset's concentration in the Delhi-NCR region.

### Task 3 — Price-range distribution

Restaurants are grouped into Zomato's four price tiers (1 = budget, 4 = luxury) and shown as a **bar chart** and a **donut chart**, each annotated with the percentage share. Verified result: **46.5% of restaurants sit in the lowest price tier**, tapering to 32.6%, 14.7%, and 6.1% as price rises.

### Task 4 — Online delivery impact

Restaurants are split by whether they offer online delivery, visualized as a **donut chart** for adoption share and a combined **bar + line chart** comparing restaurant count against average rating for each group. Verified result: **25.7% of restaurants offer online delivery**, and those that do average a **3.25 rating versus 2.47** for those that don't — a notable gap, though the dashboard doesn't test whether delivery availability itself explains the difference.

## Visualizations & exported outputs

Each task notebook exports its charts as standalone interactive HTML files, in addition to what's rendered live in the dashboard:

- **Task 1:** [`top_cuisines_lollipop.html`](Task%201/top_cuisines_lollipop.html), [`top_cuisines_donut.html`](Task%201/top_cuisines_donut.html), `top_3_cuisines_plotly.html`
- **Task 2:** [`top_cities_restaurant_count_bar.html`](Task%202/top_cities_restaurant_count_bar.html), [`city_distribution_treemap.html`](Task%202/city_distribution_treemap.html), [`top_cities_avg_rating_heatmap.html`](Task%202/top_cities_avg_rating_heatmap.html)
- **Task 3:** [`price_range_distribution_bar.html`](Task%203/price_range_distribution_bar.html), [`price_range_distribution_donut.html`](Task%203/price_range_distribution_donut.html), [`price_range_lollipop.html`](Task%203/price_range_lollipop.html)
- **Task 4:** [`online_delivery_pie_enhanced.html`](Task%204/online_delivery_pie_enhanced.html), [`delivery_rating_comparison_grouped.html`](Task%204/delivery_rating_comparison_grouped.html), [`online_delivery_rating_sankey_clean.html`](Task%204/online_delivery_rating_sankey_clean.html) — a Sankey diagram tracing delivery availability into rating category, exported from the notebook but not included in the live dashboard

Task 2 also produces a treemap of city-wise restaurant density that isn't part of the consolidated dashboard but is available as a standalone HTML export.

## Key findings

| Question | Finding |
|---|---|
| Dominant cuisine | North Indian, present in 41.5% of listings |
| Most-listed city | New Delhi (5,473 restaurants) |
| Most common price tier | Budget (tier 1) — 46.5% of restaurants |
| Online delivery adoption | 25.7% of restaurants |
| Rating difference by delivery | +0.78 average rating for restaurants offering delivery |

## Data export

Each dashboard section builds a summary table; clicking **Export CSV** in the app writes a combined `level1_summary.csv` (top cuisines, city summary, and price distribution) to the working directory.

## Technical stack

| Tool | Purpose |
|---|---|
| Python 3 | Core language |
| Pandas, NumPy | Data loading, splitting, and aggregation |
| Plotly Express & Graph Objects | Lollipop, donut, bar, and combo charts |
| Streamlit | Dashboard frontend |
| Custom CSS (`style.css`) | Dark, glass-panel dashboard theme |

## Project structure

```
Level 1/
├── level1_dashboard.py
├── style.css
├── Data Analysis Internship__Dataset__Cognifyz Technologies.csv
├── Task 1/
│   ├── top_cuisines.ipynb
│   ├── top_cuisines_lollipop.html
│   ├── top_cuisines_donut.html
│   └── top_3_cuisines_plotly.html
├── Task 2/
│   ├── city_analysis.ipynb
│   ├── top_cities_restaurant_count_bar.html
│   ├── city_distribution_treemap.html
│   └── top_cities_avg_rating_heatmap.html
├── Task 3/
│   ├── price_range.ipynb
│   ├── price_range_distribution_bar.html
│   ├── price_range_distribution_donut.html
│   └── price_range_lollipop.html
└── Task 4/
    ├── online_delivery_advanced.ipynb
    ├── online_delivery_pie_enhanced.html
    ├── delivery_rating_comparison_grouped.html
    └── online_delivery_rating_sankey_clean.html
```

## Run instructions

```bash
pip install streamlit pandas numpy plotly
cd "Level 1"
streamlit run level1_dashboard.py
```

Then open `http://localhost:8501`. The dataset CSV and `style.css` must stay in this folder — the script resolves both relative to its own location.

## Relationship to overall architecture

Level 1 is the descriptive base the rest of ZomatoLens builds on: [Level 2](../Level%202/README.md) takes the city and cuisine dimensions established here and adds geography and chain structure, and [Level 3](../Level%203/README.md) layers in text, correlation, and service-adoption analysis. See the [root README](../README.md) for how all three fit together.

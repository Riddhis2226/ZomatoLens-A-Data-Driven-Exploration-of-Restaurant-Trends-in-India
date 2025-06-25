# 🌆 Task 2: City-Wise Restaurant Analysis

> **Objective**: 
> - Identify the city with the highest number of restaurants in the dataset.
> - Calculate the average rating for restaurants in each city.
> - Determine the city with the highest average rating.

This task is part of the larger **ZomatoLens** project developed during my internship at **Cognifyz Technologies**.

---

## 📊 Features Analyzed

- `City`
- `Aggregate rating`

---

## 🛠️ Tools & Libraries

- Python (Jupyter Notebook)
- Pandas
- Plotly Express
- Plotly Graph Objects

---

## 📁 Dataset Highlights

- 85+ cities included
- Ratings vary from 0 to 5
- Minimum threshold: 30 restaurants per city to be included in average rating comparison

---

## 📈 Visualizations

### ✅ Top 10 Cities by Restaurant Count

A horizontal bar chart showing the cities with the most restaurants.

📂 `top_cities_restaurant_count_bar.html`

---

### ✅ City Distribution Treemap

Treemap visualization of restaurant density across 20 major cities, providing a visual share of the restaurant presence.

📂 `city_distribution_treemap.html`

---

### ✅ Top Cities by Average Rating (Min. 30 Restaurants)

A heat-colored bar chart showing which cities have the highest customer satisfaction based on average ratings.

📂 `top_cities_avg_rating_heatmap.html`

---

## 💡 Key Insights

| Metric | Observation |
|--------|-------------|
| 🏙️ Highest Restaurant Count | **New Delhi** dominates with 5,473 restaurants |
| 🌟 Best Avg Rating | **Gurgaon** and **Bangalore** lead with ~2.6–2.7 (among cities with >30 listings) |
| 📉 Low Ratings | Some large cities have surprisingly low avg ratings due to large volume |

---

## 🚀 Outcome

This task highlights the importance of city context in restaurant performance. It reveals which regions have dense competition, where users are more generous with ratings, and how urban food ecosystems vary.

---

## 🧠 What I Learned

- How to group and filter data meaningfully (e.g., by sample size)
- Advanced Plotly charting: treemaps, heatmap-style bars, and text formatting
- Storytelling with spatial and rating data

---

> *“Cities aren't just locations — they're data stories waiting to be told.”*

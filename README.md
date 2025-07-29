# 📊 ZomatoLens: A Data-Driven Exploration of Restaurant Trends in India

> ✨ A multi-level interactive data analytics project built during my **Data Analysis Internship** at **Cognifyz Technologies** using Python, Streamlit, Pandas, Plotly, and NLP.

---

## 🧠 Overview

**ZomatoLens** is a 3-level analytics dashboard project powered by a real-world restaurant dataset, exploring food trends, service patterns, and customer sentiments across India. Each level tackles deeper layers of insights — from simple distributions to geo-based visuals and sentiment analysis.

---

## 🚧 Internship Breakdown

| Level      | Focus Area                             | Tools/Techniques Used                                  |
| ---------- | -------------------------------------- | ------------------------------------------------------ |
| 🔹 Level 1 | Exploratory Data Analysis (EDA)        | Pandas, Plotly, Streamlit                              |
| 🔹 Level 2 | Geo & Service-Based Trends             | Mapbox, Cuisine Combinations, Chain Analysis           |
| 🔹 Level 3 | Text, Correlation & Decision Analytics | NLTK, TextBlob, spaCy, Sentiment Analysis, NLP, Plotly |

---

## 🗂️ Project Structure

```
ZomatoLens/
├── Level_1/
│   ├── README.md
│   ├── level1_dashboard.py
│   ├── style.css
│   ├── Data Analysis Internship__Dataset__Cognifyz Technologies.csv
│   ├── Task 1
│   │    ├── task 1.py
│   │    ├── top_cuisines_donut.html
│   │    ├── top_cuisines_lollipop.html
│   │    └── top_3_cuisines_plotly.html
│   ├── Task 2
│   │    ├── task 2.py
│   │    ├── city_distribution_treemap.html
│   │    ├── top_cities_avg_rating_heatmap.html
│   │    └── top_cities_restraunt_count_bar.html
│   ├── Task 3
│   │    ├── task 3.py
│   │    ├── price_range_lollipop.html
│   │    ├── price_range_distribution_donut.html
│   │    └── price_range_distribution_bar.html
│   └── Task 4
│        ├── task 4.py
│        ├── delivery_rating_comparison_grouped.html
│        ├── online_delivery_pie_enhance.html
│        └── online_delivery_rating_sankey_clean.html
├── Level_2/
│   ├── README.md
│   ├── level2_dashboard.py
│   ├── style.css
│   ├── Data Analysis Internship__Dataset__Cognifyz Technologies.csv
│   ├── Task 1
│   │    ├── task 1.py
│   │    ├── Distribution of Restaurant Ratings.png
│   │    ├── Boxplot - Spread of Restaurant Ratings.png
│   │    └── Restaurant Count by Rating Category.png
│   ├── Task 2
│   │    ├── task 2.py
│   │    └── Top 20 Cuisine Combinations by Average Rating.png
│   ├── Task 3
│   │    ├── task 3.py
│   │    ├── Restaurant Ratings & Votes Across India.png
│   │    ├── Restaurant Ratings in New Delhi.png
│   │    ├── Restaurant Ratings in Mumbai.png
│   │    └── Restaurant Ratings in Bangalore.png
│   └── Task 4
│        ├── task 4.py
│        └── Top 15 Restaurant Chains by Popularity (Votes).png
└── Level_3/
    ├── README.md
    ├── level3_dashboard.py
    ├── style.css
    ├── Data Analysis Internship__Dataset__Cognifyz Technologies.csv
    ├── Task 1
    │    ├── task 1.py
    │    └── Distribution of Review Lengths.png
    ├── Task 2
    │    ├── task 2.py
    │    ├── Votes vs Aggregate Rating.png
    │    ├── Distribution of Vote Counts across Restaurants.png
    │    └── Average Votes by Rating Category.png
    └── Task 3
        ├── task 3.py
        ├── newplot.png (Online Delivery Availability by Price Range)
        └── newplot1.png (Proportion of Online Delivery by Price Tier) 
```

---

## 🧰 Tools & Technologies Used

* `Python`
* `Pandas`, `NumPy`
* `Plotly Express` & `Graph Objects`
* `Streamlit`
* `NLTK`, `TextBlob`, `spaCy`
* `Matplotlib`, `WordCloud`
* `Mapbox`, `OpenStreetMap`
* `Custom CSS for Styling`

---

## 🎯 Key Tasks & Features

### ✅ **Level 1** – EDA Dashboard

* Top 3 cuisines in the dataset
* Restaurant distribution by city & rating
* Price range tiers with visualization
* Delivery availability insights

### ✅ **Level 2** – Geo & Service Dashboard

* Rating spread across cities
* Cuisine combination popularity
* Restaurant chain analysis
* National and city zoomed map visuals (New Delhi, Mumbai, Bangalore)

### ✅ **Level 3** – Text & Decision Dashboard

* Sentiment analysis using VADER, TextBlob
* Votes vs Ratings correlation
* NLP-based noun phrase extraction
* Price tier vs. delivery/table booking service

---

## 📊 Visualizations Included

* Donut Charts
* Bar Graphs
* Lollipop & Heatmaps
* Scatter Plots
* Mapbox Interactive Maps
* WordCloud & Noun Chunk Bars
* Multi-Axis Correlation Charts

---

## 📁 Dataset Overview

* Based on a modified **Zomato restaurant dataset**
* Key Features:

  * `Restaurant Name`, `City`, `Votes`, `Aggregate Rating`
  * `Price Range`, `Cuisines`, `Has Online Delivery`, `Has Table Booking`
  * `Rating Text`, `Latitude`, `Longitude`

---

## 🧠 Skills Acquired

* Data Cleaning & Preprocessing
* Exploratory Data Analysis
* Data Visualization (Static + Interactive)
* Sentiment Analysis (VADER, TextBlob)
* Natural Language Processing (spaCy noun chunks)
* Streamlit App Development
* Insight Derivation & Data Storytelling
* Dashboard UI/UX Design
* Correlation Analysis
* Exporting & Documentation

---

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/Riddhis2226/ZomatoLens.git
cd ZomatoLens

# Install dependencies
pip install -r requirements.txt

# Run any level
streamlit run level1_dashboard.py
streamlit run level2_dashboard.py
streamlit run level3_dashboard.py
```

> Ensure the CSV and `style.css` are in the same directory as the dashboard script.

---

## 📣 Internship Details

* **Organization**: Cognifyz Technologies
* **Role**: Data Analyst Intern
* **Duration**: June–July 2025
* **Deliverables**: Level-wise Streamlit Dashboards with analysis & code

---

## 🔗 Links

* 📁 GitHub Repo: [ZomatoLens](https://github.com/Riddhis2226/ZomatoLens-A-Data-Driven-Exploration-of-Restaurant-Trends-in-India)
* 📄 [Level 1 Dashboard](https://github.com/Riddhis2226/ZomatoLens/tree/main/Level_1)
* 📄 [Level 2 Dashboard](https://github.com/Riddhis2226/ZomatoLens/tree/main/Level_2)
* 📄 [Level 3 Dashboard](https://github.com/Riddhis2226/ZomatoLens/tree/main/Level_3)
* 🔗 [LinkedIn Post](https://www.linkedin.com/in/riddhima-singh-7b5626265)

---

> *“Good data tells a story. Great analysis makes it unforgettable.”*

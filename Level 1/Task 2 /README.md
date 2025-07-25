# 🌌 Level 1: Exploratory Data Analysis (EDA) Dashboard

Welcome to the **Level 1 Dashboard** built as part of the **Cognifyz Technologies Data Analysis Internship – 2025**. This interactive dashboard performs a deep exploratory analysis of restaurant data across India, helping uncover powerful insights into cuisines, cities, pricing, and online services.

---

## 🔍 Project Overview

This dashboard solves 4 real-world analytical tasks using Python, Plotly, and Streamlit:

### 🍽️ Task 1: Top 3 Cuisines

* Displays the top 3 most popular cuisines using **lollipop** and **donut** charts.
* Calculates both absolute counts and relative percentages.

### 🌆 Task 2: City-Wise Restaurant Analysis

* Compares the **number of restaurants** and **average ratings** across top cities.
* Uses horizontal bar charts and heat-style visuals.

### 💸 Task 3: Price Range Distribution

* Breaks down how restaurants are spread across 4 price categories (Budget to Luxury).
* Dual charts: bar plot + donut chart.

### 🛵 Task 4: Online Delivery Impact

* Analyzes how online delivery affects restaurant availability and average ratings.
* Shows comparison through a **bar + line combo chart** and donut visuals.

---

## 🧠 Technologies Used

| Tool                               | Purpose                           |
| ---------------------------------- | --------------------------------- |
| **Python 3.x**                     | Core programming language         |
| **Pandas & NumPy**                 | Data manipulation & calculations  |
| **Plotly Express & Graph Objects** | Advanced interactive charts       |
| **Streamlit**                      | Web-based visualization frontend  |
| **Custom CSS (style.css)**         | Neon + glassmorphism visual theme |

---

## 📁 Project Structure

📦 Level 1 - Exploratory Data Analysis
│
├── level1_dashboard.py        # Streamlit dashboard script
├── style.css                  # Custom UI styling (dark neon theme)
├── Data Analysis Internship__Dataset__Cognifyz Technologies.csv
├── level1_summary.csv         # (Auto-generated summary file)
├── Task 1 - task 1.py
├── Task 2 - task 2.py
├── Task 3 - task 3.py
└── Task 4 - task 4.py

---

## 🚀 How to Run the Dashboard

1. **Install Dependencies**
   Open terminal and run:

   ```bash
   pip install streamlit pandas plotly numpy
   ```

2. **Run the Dashboard**
   Navigate to the project folder and execute:

   ```bash
   streamlit run level1_dashboard.py
   ```

3. **Access Dashboard**
   Open your browser and go to:

   ```
   http://localhost:8501
   ```

---

## 📤 Exported Data

Click on the **"📥 Download Processed Data"** button in the dashboard to generate a CSV summary combining:

* Top 3 Cuisines
* City Analysis
* Price Range Distribution

🗂 File saved as: `level1_summary.csv`

---

## ✨ UI Highlights

* Neon-glow headers and **glass-style cards**
* Fully **responsive** layout for wide screens
* Hover, zoom, and tooltip interactivity
* **Export button** to download processed data
* Unified style across all tasks

---

## 📌 Sample Insights

| Feature              | Insight                         |
| -------------------- | ------------------------------- |
| 🔝 Top Cuisine       | North Indian                    |
| 🏙️ Most Active City | New Delhi                       |
| 💰 Common Price Tier | Budget-friendly (Price Range 1) |
| 🚚 Online Delivery   | Offered by \~38% of restaurants |

---

## 📘 License & Usage

This project is developed under the Cognifyz Internship Program 2025. It is intended for **educational**, **demonstrative**, and **portfolio** purposes only.

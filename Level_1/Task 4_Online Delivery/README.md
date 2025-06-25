# 🛵 Task 4: Online Delivery Analysis – ZomatoLens

> *Analyzing how online delivery impacts customer ratings and behavior using interactive visualizations.*

---

## 🎯 Goals

- Determine the percentage of restaurants that offer online delivery.
- Compare the average ratings of restaurants with and without online delivery.

---

## 🧪 Data Used

| Column              | Description                         |
|---------------------|-------------------------------------|
| `Has Online delivery` | Whether the restaurant provides delivery (`Yes` or `No`) |
| `Aggregate rating`  | Average customer rating (numeric)   |
| `Rating text`       | Categorical rating (`Excellent`, `Good`, etc.) |

---

## 📊 Visualizations

### 1️⃣ Donut Pie Chart – Online Delivery Availability

Shows the percentage of restaurants that offer online delivery vs. those that don’t.

🟢 Yes = Green  
🟠 No = Orange

📁 [`online_delivery_pie_enhanced.html`](./online_delivery_pie_enhanced.html)

---

### 2️⃣ Grouped Bar + Line Chart – Ratings vs Delivery Option

- Bar height = total restaurant count
- Line = average rating for each delivery group

🟢 Yes = Yellow  
🔵 No = Light Blue  
🔴 Avg rating line = Orange

📁 [`delivery_rating_comparison_grouped.html`](./delivery_rating_comparison_grouped.html)

---

### 3️⃣ Sankey Diagram – Delivery ➜ Rating Category Flow

Maps how delivery type (Yes/No) flows into the following rating categories:
- **Excellent**
- **Very Good**
- **Good**
- **Average**
- **Poor**
- **Not Rated**

📁 [`online_delivery_rating_sankey_clean.html`](./online_delivery_rating_sankey_clean.html)

---

## 📈 Key Insights

- **~27%** of restaurants offer online delivery.
- Restaurants with delivery have a **higher average rating**.
- Most highly-rated restaurants fall under the **delivery-enabled** group.

---

## 🧠 Learning Outcomes

- Learned how to group and aggregate data by categories
- Gained hands-on experience with **Sankey diagrams** in Plotly
- Understood how to apply dual-axis charts to reveal relationships between **volume and quality**
- Practiced advanced Plotly styling and custom color themes

---

## 🛠️ Tools & Libraries

- Python
- Pandas
- Plotly Express + Graph Objects
- Jupyter Notebook

---

> *“Data speaks louder when it’s visualized well.”*

# 🍽️ Task 1: Top Cuisines Analysis | ZomatoLens

> **Goal:**
> * Determine the top three most common cuisines in the dataset.
> * Calculate the percentage of restaurants that serve each of the top cuisines.

---

## 📂 Dataset Column Used

- `Cuisines` – A comma-separated list of cuisine types per restaurant (e.g., "North Indian, Chinese")

---

## 🛠️ Tools & Technologies

| Tool     | Purpose                     |
|----------|-----------------------------|
| Python   | Core scripting              |
| Pandas   | Data wrangling              |
| Plotly   | Interactive visualization   |
| Jupyter  | Notebook execution          |

---

## 🧪 Process

1. Removed `NaN` values from the `Cuisines` column.
2. Split comma-separated values into individual cuisine entries.
3. Counted occurrences of each cuisine across the dataset.
4. Extracted the **Top 3 most common cuisines**.
5. Calculated percentage share of each.
6. Created 3 interactive charts for maximum visual impact.

---

## 📈 Visual Outputs

| File Name                       | Chart Type         | Description                                |
|--------------------------------|--------------------|--------------------------------------------|
| `top_3_cuisines_plotly.html`   | Vertical Bar Chart | Classic layout showing counts              |
| `top_cuisines_donut.html`      | Donut Chart        | % share of top 3 cuisines                  |
| `top_cuisines_lollipop.html`   | Lollipop Chart     | Clean layout with % labels on ends         |

> All visuals are **fully interactive**. Hover for values, zoom, export!

---

## 🥇 Key Insights

- **North Indian** is the most offered cuisine across restaurants.
- **Chinese** and **Fast Food** round out the top 3.
- These three make up a significant portion of the total offerings — highlighting their market dominance in Indian urban food scenes.

---

## 🧠 Learning Outcome

- Handling multi-label categorical data (`split`, `explode`, `value_counts`)
- Chart formatting with `Plotly` (text templates, color palettes)
- Clean data storytelling using minimal but rich visual cues

---

> *"Food data isn't just delicious — it's full of patterns."*

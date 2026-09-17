# Level 3 — Text Analytics, Correlation & Service-Behavior Analysis

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-VADER-4CAF50)
![spaCy](https://img.shields.io/badge/spaCy-NLP-09A3D5?logo=spacy&logoColor=white)

[← Root](../README.md) · [← Level 2](../Level%202/README.md)

## Scope

Level 3 is the analytically deepest layer: text-based sentiment scoring, correlation between engagement and rating, and service adoption against price tier. The official Cognifyz brief defines **three** Level 3 tasks — reviews, votes, and price-vs-service — and all three are implemented here, each with its own notebook and exported charts, alongside the consolidated dashboard.

## Important methodology note: what "reviews" means here

The Cognifyz dataset used across all three levels has no free-text customer review column — its only text-bearing field is `Rating text`, a categorical label with exactly six values: *Excellent, Very Good, Good, Average, Poor,* and *Not rated*. Task 1 ("analyze text reviews for common positive and negative keywords") is implemented against that categorical field as a text-analytics proxy, not against genuine free-form review sentences. This matters for how the results should be read: the sentiment scores and keyword frequencies mostly recover the polarity already built into the label itself, rather than surfacing anything a customer actually wrote. It's stated here rather than left implicit because it changes the interpretation of the correlation figures below.

## Task coverage

| # | Official task | Notebook | Status |
|---|---|---|---|
| 1 | Text review analysis (keywords, review length, sentiment vs. rating) | `Task 1/task_1.ipynb` | ✅ (proxy text, see note above) |
| 2 | Votes analysis (highest/lowest, votes-rating correlation) | `Task 2/task_2.ipynb` | ✅ |
| 3 | Price range vs. online delivery / table booking | `Task 3/task_3.ipynb` | ✅ |
| — | spaCy noun-phrase extraction | Inside `task_1.ipynb`, as an extension of Task 1 | Enrichment, not an official task |

## Task 1 — Keyword, sentiment & length analysis

`Rating text` entries (excluding "Not rated") are lowercased and tokenized to count occurrences of a fixed positive-word list (*excellent, very good, good, amazing, fantastic, delicious, great*) and negative-word list (*poor, bad, worst, average, terrible, disappointed, not good*), visualized as two word clouds. Because the source text is limited to the six category labels, only a handful of these words actually appear — verified counts: **"good" (3,179), "excellent" (301)** on the positive side, **"average" (3,737), "poor" (186)** on the negative side; the remaining listed keywords never occur in this field.

Sentiment is then scored with **VADER** (compound score) and **TextBlob** (polarity, subjectivity), and a review-length histogram (character length of the label) is exported. Verified correlation between VADER sentiment score and `Aggregate rating`: **0.88** — a strong association, but one that should be read with the caveat above in mind: since the sentiment analyzer is scoring words like "excellent" and "poor" that are near-synonyms of the rating category itself, this correlation is close to circular rather than a genuine discovery about customer language. The VADER-derived sentiment labels split as **3,480 Positive, 3,737 Neutral, 186 Negative**.

## Task 2 — Votes and rating analysis

Beyond the votes-vs-rating scatter and correlation, this notebook explicitly surfaces the restaurants with the highest and lowest vote counts, as the official task asks. Verified result: **Toit (10,934 votes, 4.8 rating)** and **Truffles (9,667 votes, 4.7 rating)** top the list. On the low end, **1,094 restaurants (11.5% of the dataset) have zero votes**, so "lowest voted" is really a large tied group rather than a single standout restaurant. The votes-rating **Pearson correlation is 0.31** — a modest positive association. A vote-count histogram and an average-votes-by-rating-category bar chart are also exported.

## Task 3 — Price range vs. online services

Restaurants are grouped by `Price range` and cross-tabulated against `Has Online delivery` and `Has Table booking`, shown as grouped bar charts, a combined delivery×booking pivot matrix, and a normalized (proportion) view for delivery adoption, plus an overall delivery-share donut chart. Verified adoption rates by price tier (1 = budget → 4 = luxury):

| Price tier | Online delivery | Table booking |
|---|---|---|
| 1 (Budget) | 15.8% | 0.0% |
| 2 | 41.3% | 7.7% |
| 3 | 29.2% | 45.7% |
| 4 (Luxury) | 9.0% | 46.8% |

Table booking rises steadily with price tier, consistent with higher-end restaurants more often offering reservations. Online delivery doesn't follow the same pattern — it peaks in tier 2 rather than the cheapest or priciest tier — suggesting delivery adoption is driven by something other than price alone.

## Additional NLP enrichment — noun-phrase extraction

Inside the same Task 1 notebook, spaCy (`en_core_web_sm`) extracts noun chunks from the `Rating text` values, tallies frequency with `collections.Counter`, and charts the top 15. Because the input vocabulary is limited to six short category phrases, this functions as a demonstration of the NLP pipeline itself — tokenization, POS tagging, and chunk extraction wired up end-to-end — rather than substantive mining of open-ended review content.

## Key findings

| Metric | Value |
|---|---|
| VADER sentiment vs. rating correlation | 0.88 (see circularity caveat above) |
| Votes vs. rating correlation | 0.31 |
| Most-voted restaurant | Toit — 10,934 votes, 4.8 rating |
| Restaurants with zero votes | 1,094 (11.5% of dataset) |
| Table booking, tier 1 → tier 4 | 0% → 7.7% → 45.7% → 46.8% |
| Online delivery, tier 1 → tier 4 | 15.8% → 41.3% → 29.2% → 9.0% (peaks at tier 2) |

## Visual outputs

- **Task 1:** [`Distribution of Review Lengths.png`](Task%201/Distribution%20of%20Review%20Lengths.png)
- **Task 2:** [`Votes vs Aggregate Rating.png`](Task%202/Votes%20vs%20Aggregate%20Rating.png), [`Distribution of Vote Counts across Restaurants.png`](Task%202/Distribution%20of%20Vote%20Counts%20across%20Restaurants.png), [`Average Votes by Rating Category.png`](Task%202/Average%20Votes%20by%20Rating%20Category.png)
- **Task 3:** [`newplot.png`](Task%203/newplot.png) (online delivery by price range), [`newplot 1.png`](Task%203/newplot%201.png) (proportion of online delivery by price tier)

The word clouds, VADER/TextBlob comparison plot, sentiment-distribution chart, and noun-phrase bar chart from Task 1 are rendered inline in the notebook but not exported as standalone image files.

## Technical stack

| Tool | Purpose |
|---|---|
| Python 3 | Core language |
| Pandas | Grouping, filtering, correlation |
| Plotly Express & Graph Objects | Histograms, scatter, grouped/stacked bars, donut |
| Matplotlib, Seaborn, WordCloud | Regression plots, sentiment-distribution bars, word clouds |
| NLTK (VADER) | Sentiment scoring — auto-downloads the `vader_lexicon` on first run |
| TextBlob | Polarity and subjectivity scoring |
| spaCy (`en_core_web_sm`) | Noun-chunk extraction — model must be downloaded separately |
| Streamlit | Dashboard frontend (`level3_dashboard.py`) |
| Custom CSS (`style.css`) | Dark, glass-panel dashboard theme |

## Project structure

```
Level 3/
├── level3_dashboard.py
├── style.css
├── Data Analysis Internship__Dataset__Cognifyz Technologies.csv
├── Task 1/
│   ├── task_1.ipynb
│   └── Distribution of Review Lengths.png
├── Task 2/
│   ├── task_2.ipynb
│   ├── Votes vs Aggregate Rating.png
│   ├── Distribution of Vote Counts across Restaurants.png
│   └── Average Votes by Rating Category.png
└── Task 3/
    ├── task_3.ipynb
    ├── newplot.png
    └── newplot 1.png
```

## Run instructions

```bash
pip install streamlit pandas plotly matplotlib seaborn wordcloud nltk textblob spacy
python -m spacy download en_core_web_sm
cd "Level 3"
streamlit run level3_dashboard.py
```

The script downloads NLTK's VADER lexicon automatically on first run. The spaCy English model must be downloaded ahead of time, or `spacy.load("en_core_web_sm")` will fail at startup. As with the other levels, the CSV and `style.css` must remain in this folder for the dashboard script to find them.

## Relationship to overall architecture

Level 3 closes the loop on ZomatoLens: it takes the ratings established in [Level 1](../Level%201/README.md) and the entity structure from [Level 2](../Level%202/README.md) and asks how they relate to engagement (votes), sentiment, and service offerings. See the [root README](../README.md) for the complete picture across all three levels.

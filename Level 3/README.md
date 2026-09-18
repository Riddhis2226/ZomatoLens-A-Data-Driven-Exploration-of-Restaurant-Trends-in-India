# Level 3 — Text Analytics, Correlation & Service-Behavior Analysis

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-VADER-4CAF50)
![spaCy](https://img.shields.io/badge/spaCy-NLP-09A3D5?logo=spacy&logoColor=white)

[← Root](../README.md) · [← Level 2](../Level%202/README.md)

## Scope

The deepest layer: text sentiment, engagement correlation, service adoption by price tier. Cognifyz defines **3** official Level 3 tasks — all implemented, each with its own notebook and exports, plus 1 additional NLP enrichment layered onto Task 1.

## ⚠️ Methodology note — what "reviews" means here

The dataset has **no free-text review column**. Its only text field is `Rating text` — 6 fixed categories: *Excellent, Very Good, Good, Average, Poor, Not rated*. Task 1 ("analyze text reviews for keywords") runs against this categorical field as a proxy, not genuine review sentences. This directly affects how the correlation figures below should be read — flagged explicitly rather than left implicit.

## Task coverage

| # | Official task | Notebook | Status |
|---|---|---|---|
| 1 | Review analysis — keywords, length, sentiment vs. rating | `Task 1/task_1.ipynb` | ✅ (proxy text) |
| 2 | Votes analysis — highest/lowest, votes-rating correlation | `Task 2/task_2.ipynb` | ✅ |
| 3 | Price range vs. delivery / table booking | `Task 3/task_3.ipynb` | ✅ |
| — | spaCy noun-phrase extraction | Inside `task_1.ipynb` | Enrichment, not official |

## Task 1 — Keyword, sentiment & length analysis

- **Method:** `Rating text` (excl. "Not rated") tokenized against fixed positive/negative word lists; scored with **VADER** (compound) and **TextBlob** (polarity, subjectivity); review-length histogram exported
- **Keyword frequency:**

| Positive | Count | Negative | Count |
|---|---|---|---|
| good | **3,179** | average | **3,737** |
| excellent | 301 | poor | 186 |

  Remaining listed keywords never occur — the field only contains 6 phrases.

- **Sentiment split:** Positive **3,480** · Neutral **3,737** · Negative **186**
- **Sentiment–rating correlation:** **0.88**

  ⚠️ Near-circular: VADER is scoring words like "excellent"/"poor" that are synonyms of the rating category itself — not a discovery about genuine customer language.

## Task 2 — Votes and rating analysis

- **Method:** votes-vs-rating scatter + Pearson correlation; explicit highest/lowest-voted extraction; vote-count histogram; avg. votes by rating category

| Metric | Value |
|---|---|
| Votes–rating correlation | **0.31** (weak positive) |
| Most-voted restaurant | Toit — **10,934** votes, 4.8 rating |
| 2nd most-voted | Truffles — 9,667 votes, 4.7 rating |
| Zero-vote restaurants | **1,094** (11.5% of dataset) — a tied group, not a single "lowest" |

## Task 3 — Price range vs. online services

- **Method:** `Price range` × `Has Online delivery` / `Has Table booking` cross-tabs; grouped bars, combined pivot matrix, normalized proportion view, overall delivery-share donut

| Price tier | Online delivery | Table booking |
|---|---|---|
| 1 (Budget) | 15.8% | 0.0% |
| 2 | **41.3%** | 7.7% |
| 3 | 29.2% | 45.7% |
| 4 (Luxury) | 9.0% | **46.8%** |

- **Table booking:** rises steadily with price tier — expected for reservation-driven, higher-end dining
- **Online delivery:** peaks at tier 2, not tier 1 or 4 — adoption isn't purely price-driven

## Additional NLP enrichment — noun-phrase extraction

- **Method:** spaCy (`en_core_web_sm`) noun-chunk extraction on the same 6 `Rating text` values, tallied with `Counter`, top 15 charted
- **Read:** demonstrates the NLP pipeline end-to-end (tokenize → POS-tag → chunk); not substantive mining, since the vocabulary is capped at 6 short phrases

## Key findings

| Metric | Value |
|---|---|
| Sentiment–rating correlation | 0.88 (circularity caveat above) |
| Votes–rating correlation | 0.31 |
| Most-voted restaurant | Toit — 10,934 votes |
| Zero-vote restaurants | 1,094 (11.5%) |
| Table booking, tier 1 → 4 | 0% → 7.7% → 45.7% → 46.8% |
| Delivery, tier 1 → 4 | 15.8% → 41.3% → 29.2% → 9.0% (peaks tier 2) |

## Visual outputs

| Task | Files |
|---|---|
| 1 | [`Distribution of Review Lengths.png`](Task%201/Distribution%20of%20Review%20Lengths.png) |
| 2 | [`Votes vs Aggregate Rating.png`](Task%202/Votes%20vs%20Aggregate%20Rating.png) · [`Distribution of Vote Counts across Restaurants.png`](Task%202/Distribution%20of%20Vote%20Counts%20across%20Restaurants.png) · [`Average Votes by Rating Category.png`](Task%202/Average%20Votes%20by%20Rating%20Category.png) |
| 3 | [`newplot.png`](Task%203/newplot.png) (delivery by price range) · [`newplot 1.png`](Task%203/newplot%201.png) (delivery proportion by tier) |

Word clouds, VADER/TextBlob comparison, sentiment distribution, and the noun-phrase chart render inline in the notebook — not exported as standalone images.

## Technical stack

| Tool | Purpose |
|---|---|
| Python 3 | Core language |
| Pandas | Grouping, filtering, correlation |
| Plotly Express & Graph Objects | Histograms, scatter, grouped/stacked bars, donut |
| Matplotlib, Seaborn, WordCloud | Regression plots, sentiment bars, word clouds |
| NLTK (VADER) | Sentiment scoring — auto-downloads `vader_lexicon` |
| TextBlob | Polarity & subjectivity |
| spaCy (`en_core_web_sm`) | Noun-chunk extraction — model needs manual download |
| Streamlit | Dashboard frontend |
| Custom CSS (`style.css`) | Dark, glass-panel theme |

## Project structure

```
Level 3/
├── level3_dashboard.py
├── style.css
├── Data Analysis Internship__Dataset__Cognifyz Technologies.csv
├── Task 1/  → task_1.ipynb + 1 PNG export
├── Task 2/  → task_2.ipynb + 3 PNG exports
└── Task 3/  → task_3.ipynb + 2 PNG exports
```

## Run instructions

```bash
pip install streamlit pandas plotly matplotlib seaborn wordcloud nltk textblob spacy
python -m spacy download en_core_web_sm
cd "Level 3"
streamlit run level3_dashboard.py
```

NLTK's VADER lexicon downloads automatically on first run. spaCy's model must be downloaded ahead of time or `spacy.load("en_core_web_sm")` fails at startup. CSV and `style.css` must stay in this folder.

## Relationship to overall architecture

Closes the loop: takes Level 1's ratings and Level 2's entity structure, and relates them to engagement (votes), sentiment, and service offerings. Full picture: [root README](../README.md).

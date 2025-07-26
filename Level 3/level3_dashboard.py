# 📦 Import Required Libraries
import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import streamlit as st
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
import spacy

# 📥 Setup
nltk.download('vader_lexicon')
nlp = spacy.load("en_core_web_sm")

# 📂 Paths
BASE_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_DIR, "Data Analysis Internship__Dataset__Cognifyz Technologies.csv")
CSS_PATH = os.path.join(BASE_DIR, "style.css")

# 🌐 Streamlit Config
st.set_page_config(page_title="Cognifyz Level 3 Dashboard", layout="wide")

# 🎨 Load optional custom CSS
if os.path.exists(CSS_PATH):
    with open(CSS_PATH) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
else:
    st.warning("⚠️ style.css not found. Default Streamlit styling used.")

# 🧠 Load Dataset
try:
    df = pd.read_csv(DATA_PATH)
except FileNotFoundError:
    st.error(f"❌ Dataset not found at {DATA_PATH}")
    st.stop()

# 🌟 Header
st.markdown("<h1 class='neon-text'>🌌 Level 3 : Advanced Text, Correlation & Decision Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p class='glass-card'>This dashboard covers 3 advanced tasks from Level 3 using sentiment analysis, correlation insights, and NLP-powered review mining.</p>", unsafe_allow_html=True)

# ----------------------------
# SECTION 1: REVIEW ANALYSIS
# ----------------------------
st.markdown("<h2 class='task-header'>💬 Task 1: Review Sentiment Analysis</h2>", unsafe_allow_html=True)
review_df = df[['Rating text', 'Aggregate rating']].dropna()
review_df = review_df[review_df['Rating text'].str.lower() != 'not rated'].copy()
review_df['Cleaned_Review'] = review_df['Rating text'].str.lower()
review_df['Review Length'] = review_df['Rating text'].apply(lambda x: len(str(x)))

# 🔍 Sentiment Analysis
sid = SentimentIntensityAnalyzer()
review_df['VADER Score'] = review_df['Cleaned_Review'].apply(lambda x: sid.polarity_scores(x)['compound'])
review_df['TextBlob Polarity'] = review_df['Cleaned_Review'].apply(lambda x: TextBlob(x).sentiment.polarity)
review_df['TextBlob Subjectivity'] = review_df['Cleaned_Review'].apply(lambda x: TextBlob(x).sentiment.subjectivity)
review_df['Sentiment Label'] = review_df['VADER Score'].apply(lambda x: 'Positive' if x > 0.2 else ('Negative' if x < -0.2 else 'Neutral'))

# 📊 Review Length Distribution
fig_review_hist = px.histogram(
    review_df, x='Review Length', nbins=15,
    title='Review Length Distribution', color_discrete_sequence=['#636EFA']
)
st.plotly_chart(fig_review_hist, use_container_width=True)

# 📉 Boxplot by Rating Text
fig_box = px.box(
    review_df, x='Rating text', y='Review Length',
    color='Rating text', title='Review Length vs Rating',
    color_discrete_sequence=px.colors.qualitative.Set2
)
st.plotly_chart(fig_box, use_container_width=True)

correlation_review = review_df[['Aggregate rating', 'Review Length']].corr().iloc[0, 1].round(3)
st.info(f"📊 Correlation between review length and rating: **{correlation_review}**")

# ----------------------------
# SECTION 2: VOTES ANALYSIS
# ----------------------------
st.markdown("<h2 class='task-header'>📊 Task 2: Votes and Ratings Analysis</h2>", unsafe_allow_html=True)

fig_votes_rating = px.scatter(
    df[df['Votes'] > 0], x='Votes', y='Aggregate rating',
    color='Aggregate rating', size='Votes', hover_name='Restaurant Name',
    title='Votes vs Rating Correlation', color_continuous_scale='Turbo'
)
st.plotly_chart(fig_votes_rating, use_container_width=True)

correlation_votes = df[['Votes', 'Aggregate rating']].corr().iloc[0, 1].round(3)
st.info(f"📈 Correlation between votes and rating: **{correlation_votes}**")

votes_by_rating = df.groupby('Rating text')['Votes'].mean().reset_index().sort_values(by='Votes', ascending=False)
fig_avg_votes = px.bar(
    votes_by_rating, x='Rating text', y='Votes', color='Votes', text='Votes',
    title='Average Votes by Rating', color_continuous_scale='Plasma'
)
st.plotly_chart(fig_avg_votes, use_container_width=True)

# ----------------------------
# SECTION 3: PRICE vs SERVICES
# ----------------------------
st.markdown("<h2 class='task-header'>💰 Task 3: Price Range vs Online Services</h2>", unsafe_allow_html=True)
service_df = df[['Restaurant Name', 'Price range', 'Has Online delivery', 'Has Table booking']].dropna()
service_df = service_df[
    (service_df['Has Online delivery'].isin(['Yes', 'No'])) &
    (service_df['Has Table booking'].isin(['Yes', 'No']))
]

delivery_group = service_df.groupby(['Price range', 'Has Online delivery']).size().reset_index(name='Count')
fig_delivery = px.bar(
    delivery_group, x='Price range', y='Count', color='Has Online delivery',
    barmode='group', text='Count',
    title='Online Delivery by Price Range',
    color_discrete_map={'Yes': 'green', 'No': 'orange'}
)
st.plotly_chart(fig_delivery, use_container_width=True)

booking_group = service_df.groupby(['Price range', 'Has Table booking']).size().reset_index(name='Count')
fig_booking = px.bar(
    booking_group, x='Price range', y='Count', color='Has Table booking',
    barmode='group', text='Count',
    title='Table Booking by Price Range',
    color_discrete_map={'Yes': '#1f77b4', 'No': '#ff7f0e'}
)
st.plotly_chart(fig_booking, use_container_width=True)

normalized_delivery = delivery_group.copy()
normalized_delivery['Proportion'] = normalized_delivery.groupby('Price range')['Count'].transform(lambda x: x / x.sum())
fig_delivery_prop = px.bar(
    normalized_delivery, x='Price range', y='Proportion', color='Has Online delivery',
    barmode='stack', text='Proportion',
    title='Proportion of Online Delivery by Price Tier',
    color_discrete_map={'Yes': 'green', 'No': 'orange'}
)
fig_delivery_prop.update_traces(texttemplate='%{text:.1%}', textposition='inside')
fig_delivery_prop.update_layout(yaxis_tickformat='.0%')
st.plotly_chart(fig_delivery_prop, use_container_width=True)

# ----------------------------
# SECTION 4: NOUN CHUNKS
# ----------------------------
st.markdown("<h2 class='task-header'>🧬 Task 4: spaCy Noun Phrase Frequency</h2>", unsafe_allow_html=True)
all_chunks = []
for doc in nlp.pipe(review_df['Cleaned_Review'].tolist(), batch_size=50):
    all_chunks.extend([chunk.text for chunk in doc.noun_chunks])

chunk_counts = Counter(all_chunks)
top_chunks = chunk_counts.most_common(15)
chunk_df = pd.DataFrame(top_chunks, columns=['Noun Chunk', 'Frequency'])
fig_chunk = px.bar(
    chunk_df, y='Noun Chunk', x='Frequency', orientation='h', color='Frequency',
    title='Top 15 Noun Phrases from Reviews', color_continuous_scale='Magma'
)
st.plotly_chart(fig_chunk, use_container_width=True)

# ----------------------------
# EXPORT SECTION (FINAL)
# ----------------------------
st.markdown("<h3 class='task-header'>📥 Download Processed Data</h3>", unsafe_allow_html=True)

@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

merged_export_df = pd.concat([
    review_df[['Rating text', 'Aggregate rating', 'Review Length', 'VADER Score', 'TextBlob Polarity', 'Sentiment Label']],
    votes_by_rating,
    booking_group,
    delivery_group,
    chunk_df
], axis=1)

csv = convert_df(merged_export_df)

st.download_button(
    label="📤 Export CSV",
    data=csv,
    file_name='level3_summary.csv',
    mime='text/csv'
)

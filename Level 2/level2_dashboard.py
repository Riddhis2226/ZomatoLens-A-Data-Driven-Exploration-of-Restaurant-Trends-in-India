import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# --- PATH SETUP ---
BASE_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_DIR, "Data Analysis Internship__Dataset__Cognifyz Technologies.csv")
CSS_PATH = os.path.join(BASE_DIR, "style.css")

# --- PAGE CONFIG ---
st.set_page_config(page_title="Cognifyz Level 2 Dashboard", layout="wide")

# --- LOAD CSS ---
if os.path.exists(CSS_PATH):
    with open(CSS_PATH) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
else:
    st.warning("⚠️ style.css not found. Default Streamlit style applied.")

# --- LOAD DATA ---
try:
    df = pd.read_csv(DATA_PATH)
except FileNotFoundError:
    st.error(f"❌ Could not find dataset at {DATA_PATH}")
    st.stop()

# --- HEADER ---
st.markdown("<h1 class='neon-text'>🌍 Level 2 : Geo & Service-Based Trends Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p class='glass-card'>This dashboard covers 4 key tasks from Level 2 exploring geo and service-based trends across Indian restaurants.</p>", unsafe_allow_html=True)

# --- TASK 1 ---
st.markdown("<h2 class='task-header'>📊 Task 1: Rating Distribution & Insights</h2>", unsafe_allow_html=True)
df_rated = df[df['Aggregate rating'] > 0]

col1, col2 = st.columns(2)
with col1:
    fig1 = px.histogram(df_rated, x='Aggregate rating', nbins=20, color_discrete_sequence=['#636EFA'])
    fig1.update_layout(plot_bgcolor='white')
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.box(df_rated, y='Aggregate rating', points='all', color_discrete_sequence=['#EF553B'])
    fig2.update_layout(plot_bgcolor='white')
    st.plotly_chart(fig2, use_container_width=True)

rating_text_counts = df['Rating text'].value_counts().reset_index()
rating_text_counts.columns = ['Rating Text', 'Count']
fig3 = px.bar(rating_text_counts, x='Rating Text', y='Count', color='Rating Text',
              text='Count', color_discrete_sequence=px.colors.qualitative.Safe)
fig3.update_layout(plot_bgcolor='white')
st.plotly_chart(fig3, use_container_width=True)

average_votes = df['Votes'].mean().round(2)
st.success(f"🧠 Average number of votes per restaurant: **{average_votes}**")

# --- TASK 2 ---
st.markdown("<h2 class='task-header'>🍽️ Task 2: Cuisine Combinations by Rating</h2>", unsafe_allow_html=True)
cuisine_data = df[['Cuisines', 'Aggregate rating']].dropna()
cuisine_data = cuisine_data[cuisine_data['Cuisines'].str.strip() != '']

combo_avg_rating = cuisine_data.groupby('Cuisines')['Aggregate rating'].agg(['count', 'mean']).reset_index()
combo_avg_rating.columns = ['Cuisine Combination', 'Total Restaurants', 'Average Rating']
combo_filtered = combo_avg_rating[combo_avg_rating['Total Restaurants'] > 20]

fig4 = px.bar(
    combo_filtered.sort_values(by='Average Rating', ascending=False).head(20),
    x='Average Rating',
    y='Cuisine Combination',
    orientation='h',
    text='Average Rating',
    color='Average Rating',
    color_continuous_scale='Turbo'
)
fig4.update_layout(plot_bgcolor='white', height=700)
st.plotly_chart(fig4, use_container_width=True)

# --- TASK 3 ---
st.markdown("<h2 class='task-header'>🗺️ Task 3: Restaurant Map Clusters</h2>", unsafe_allow_html=True)
geo_df = df[['Restaurant Name', 'City', 'Latitude', 'Longitude', 'Aggregate rating', 'Votes']].dropna()
geo_df = geo_df[(geo_df['Latitude'] != 0.0) & (geo_df['Longitude'] != 0.0)]

st.subheader("📍 National Map")
fig5 = px.scatter_mapbox(
    geo_df,
    lat="Latitude",
    lon="Longitude",
    hover_name="Restaurant Name",
    hover_data={"City": True, "Aggregate rating": True, "Votes": True},
    color="Aggregate rating",
    size="Votes",
    size_max=15,
    color_continuous_scale="Turbo",
    zoom=4
)
fig5.update_layout(mapbox_style="open-street-map", margin={"r":0,"t":0,"l":0,"b":0}, height=600)
st.plotly_chart(fig5, use_container_width=True)

st.subheader("🔎 Zoomed Maps (Delhi, Mumbai, Bangalore)")
for city in ['New Delhi', 'Mumbai', 'Bangalore']:
    city_df = geo_df[geo_df['City'] == city]
    fig_city = px.scatter_mapbox(
        city_df,
        lat="Latitude",
        lon="Longitude",
        hover_name="Restaurant Name",
        hover_data={"Aggregate rating": True, "Votes": True},
        color="Aggregate rating",
        size="Votes",
        size_max=12,
        color_continuous_scale="Plasma",
        zoom=10,
        title=f"📍 Restaurant Ratings in {city}"
    )
    fig_city.update_layout(mapbox_style="carto-positron", margin={"r":0,"t":40,"l":0,"b":0}, height=500)
    st.plotly_chart(fig_city, use_container_width=True)

# --- TASK 4 ---
st.markdown("<h2 class='task-header'>🏪 Task 4: Restaurant Chains by Popularity</h2>", unsafe_allow_html=True)
chain_counts = df['Restaurant Name'].value_counts().reset_index()
chain_counts.columns = ['Restaurant Name', 'Branch Count']
restaurant_chains = chain_counts[chain_counts['Branch Count'] > 1]
chain_data = pd.merge(restaurant_chains, df, on='Restaurant Name')

chain_summary = chain_data.groupby('Restaurant Name').agg({
    'Branch Count': 'first',
    'Aggregate rating': 'mean',
    'Votes': 'sum'
}).reset_index().sort_values(by='Votes', ascending=False).head(15)

fig6 = px.bar(
    chain_summary,
    x='Votes',
    y='Restaurant Name',
    orientation='h',
    color='Aggregate rating',
    text='Aggregate rating',
    color_continuous_scale='Plasma'
)
fig6.update_layout(plot_bgcolor='white', height=700)
st.plotly_chart(fig6, use_container_width=True)

# --- EXPORT SECTION ---
st.markdown("<h3 class='task-header'>📥 Download Processed Data</h3>", unsafe_allow_html=True)

@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

merged_export_df = pd.concat([
    rating_text_counts,
    combo_filtered[['Cuisine Combination', 'Total Restaurants', 'Average Rating']],
    geo_df[['City', 'Aggregate rating', 'Votes']],
    chain_summary
], axis=1)

csv = convert_df(merged_export_df)

st.download_button(
    label="📤 Export CSV",
    data=csv,
    file_name='level2_summary.csv',
    mime='text/csv'
)

# 📦 Import Required Libraries
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import os
import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Cognifyz Level 1 Dashboard", layout="wide")

# --- LOAD CSS ---
BASE_DIR = os.path.dirname(__file__)
css_path = os.path.join(BASE_DIR, "style.css")
if os.path.exists(css_path):
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
else:
    st.warning("⚠️ style.css not found! Custom styles won't be applied.")

# --- LOAD DATA ---
DATA_PATH = os.path.join(BASE_DIR, "Data Analysis Internship__Dataset__Cognifyz Technologies.csv")
try:
    df = pd.read_csv(DATA_PATH)
except FileNotFoundError:
    st.error(f"❌ Could not find dataset at {DATA_PATH}")
    st.stop()

# --- HEADER ---
st.markdown("<h1 class='neon-text'>🌌 Level 1 : Exploratory Data Analysis (EDA) Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p class='glass-card'>This dashboard covers 4 key tasks from Level 1 using interactive visualizations and summary statistics.</p>", unsafe_allow_html=True)

# ========== TASK 1 ==========
st.markdown("<h2 class='task-header'>🍽️ Task 1: Top 3 Cuisines</h2>", unsafe_allow_html=True)

cuisine_series = df['Cuisines'].dropna().str.split(', ')
all_cuisines = cuisine_series.explode()
top_cuisines = all_cuisines.value_counts().head(3)
total_restaurants = df.shape[0]
cuisine_percentages = (top_cuisines / total_restaurants * 100).round(2)

top_df = pd.DataFrame({
    'Cuisine': top_cuisines.index,
    'Count': top_cuisines.values,
    'Percentage': cuisine_percentages.values
})

# Lollipop Chart
fig1 = go.Figure()
fig1.add_trace(go.Scatter(
    x=top_df['Count'],
    y=top_df['Cuisine'],
    mode='markers+text',
    marker=dict(size=18, color='#FF7F0E'),
    text=top_df['Percentage'].astype(str) + '%',
    textposition='middle right'
))
fig1.add_trace(go.Bar(
    x=top_df['Count'],
    y=top_df['Cuisine'],
    orientation='h',
    marker=dict(color='rgba(255,127,14,0.2)'),
    showlegend=False
))
fig1.update_layout(
    title='🎯 Top 3 Cuisines by Popularity',
    xaxis_title='Number of Restaurants',
    yaxis_title='Cuisine',
    plot_bgcolor='white',
    height=400
)
st.plotly_chart(fig1, use_container_width=True)

# Donut Chart
fig2 = go.Figure(data=[
    go.Pie(
        labels=top_df['Cuisine'],
        values=top_df['Count'],
        hole=0.45,
        textinfo='percent+label',
        hoverinfo='label+value+percent',
        marker=dict(colors=px.colors.sequential.Magma_r)
    )
])
fig2.update_layout(
    title="🍽️ Cuisine Share Among Top 3",
    annotations=[dict(text='Cuisines', x=0.5, y=0.5, font_size=16, showarrow=False)],
    height=400
)
st.plotly_chart(fig2, use_container_width=True)

# ========== TASK 2 ==========
st.markdown("<h2 class='task-header'>🌆 Task 2: City Analysis</h2>", unsafe_allow_html=True)

city_counts = df['City'].value_counts().reset_index()
city_counts.columns = ['City', 'Restaurant Count']
avg_ratings = df.groupby('City')['Aggregate rating'].mean().reset_index()
city_summary = pd.merge(city_counts, avg_ratings, on='City').sort_values(by='Restaurant Count', ascending=False)

# Bar Chart
fig3 = px.bar(
    city_counts.head(10),
    x='Restaurant Count',
    y='City',
    orientation='h',
    color='Restaurant Count',
    color_continuous_scale='Bluered_r',
    title='📍 Top 10 Cities with the Most Restaurants',
    text='Restaurant Count'
)
fig3.update_traces(textposition='outside')
fig3.update_layout(
    yaxis=dict(categoryorder='total ascending'),
    plot_bgcolor='white'
)
st.plotly_chart(fig3, use_container_width=True)

# Heatmap-Style Bar for Avg Rating
city_avg_rating = df.groupby('City')['Aggregate rating'].mean()
city_counts_all = df['City'].value_counts()
valid_cities = city_counts_all[city_counts_all > 30].index
avg_rating_filtered = city_avg_rating[city_avg_rating.index.isin(valid_cities)].sort_values(ascending=False)
top_avg_df = avg_rating_filtered.head(10).reset_index()
top_avg_df.columns = ['City', 'Average Rating']

fig4 = px.bar(
    top_avg_df,
    x='Average Rating',
    y='City',
    orientation='h',
    text='Average Rating',
    color='Average Rating',
    color_continuous_scale='Viridis',
    title='⭐ Top 10 Cities by Average Rating (Min 30 Restaurants)'
)
fig4.update_traces(texttemplate='%{text:.2f}', textposition='outside')
fig4.update_layout(yaxis=dict(categoryorder='total ascending'))
st.plotly_chart(fig4, use_container_width=True)

# ========== TASK 3 ==========
st.markdown("<h2 class='task-header'>💸 Task 3: Price Range Distribution</h2>", unsafe_allow_html=True)

price_counts = df['Price range'].value_counts().sort_index()
price_percentages = (price_counts / len(df) * 100).round(2)

price_df = pd.DataFrame({
    'Price Range': price_counts.index.astype(str),
    'Restaurant Count': price_counts.values,
    'Percentage': price_percentages.values
})

# Bar Chart
fig5 = px.bar(
    price_df,
    x='Price Range',
    y='Restaurant Count',
    text='Percentage',
    color='Restaurant Count',
    color_continuous_scale='Plasma',
    title='💸 Price Range Distribution of Restaurants'
)
fig5.update_traces(texttemplate='%{text}%', textposition='outside')
fig5.update_layout(
    xaxis_title='Price Range (1 = Budget, 4 = Luxury)',
    yaxis_title='Restaurant Count',
    plot_bgcolor='white'
)
st.plotly_chart(fig5, use_container_width=True)

# Donut Chart
fig6 = go.Figure(data=[
    go.Pie(
        labels=price_df['Price Range'],
        values=price_df['Restaurant Count'],
        hole=0.5,
        marker=dict(colors=px.colors.sequential.Viridis),
        textinfo='label+percent',
        hoverinfo='label+value+percent'
    )
])
fig6.update_layout(
    title_text="🍩 Restaurant Distribution by Price Range (Donut View)",
    annotations=[dict(text='Price', x=0.5, y=0.5, font_size=20, showarrow=False)]
)
st.plotly_chart(fig6, use_container_width=True)

# ========== TASK 4 ==========
st.markdown("<h2 class='task-header'>🛵 Task 4: Online Delivery</h2>", unsafe_allow_html=True)

df_clean = df[df['Has Online delivery'].isin(['Yes', 'No'])].copy()
delivery_counts = df_clean['Has Online delivery'].value_counts().reindex(['Yes', 'No'])

# Donut Chart
fig7 = go.Figure(data=[
    go.Pie(
        labels=delivery_counts.index,
        values=delivery_counts.values,
        textinfo='label+percent+value',
        hoverinfo='label+percent+value',
        marker=dict(colors=['#2CA02C', '#FF7F0E']),
        pull=[0.05, 0],
        hole=0.5
    )
])
fig7.update_layout(
    title='🛵 Restaurants Offering Online Delivery',
    annotations=[dict(text='Delivery', x=0.5, y=0.5, showarrow=False, font_size=18)],
    showlegend=True
)
st.plotly_chart(fig7, use_container_width=True)

# Bar + Line Chart
avg_rating_by_delivery = df_clean.groupby('Has Online delivery')['Aggregate rating'].agg(['mean', 'count']).reset_index()
avg_rating_by_delivery.columns = ['Online Delivery', 'Avg Rating', 'Total Restaurants']
avg_rating_by_delivery['Percentage'] = (avg_rating_by_delivery['Total Restaurants'] / df_clean.shape[0] * 100).round(2)
bar_colors = ['#F4D03F' if val == 'Yes' else '#5DADE2' for val in avg_rating_by_delivery['Online Delivery']]

fig8 = go.Figure()
fig8.add_trace(go.Bar(
    x=avg_rating_by_delivery['Online Delivery'],
    y=avg_rating_by_delivery['Total Restaurants'],
    name='Restaurant Count',
    marker_color=bar_colors,
    text=avg_rating_by_delivery['Percentage'].astype(str) + '%',
    textposition='outside'
))
fig8.add_trace(go.Scatter(
    x=avg_rating_by_delivery['Online Delivery'],
    y=avg_rating_by_delivery['Avg Rating'],
    name='Avg Rating',
    mode='lines+markers+text',
    marker=dict(size=10, color='#FF5733'),
    text=avg_rating_by_delivery['Avg Rating'].round(2),
    textposition='top center',
    yaxis='y2'
))
fig8.update_layout(
    title="📊 Online Delivery: Restaurant Count vs. Average Rating",
    xaxis=dict(title='Online Delivery Option'),
    yaxis=dict(title='Number of Restaurants'),
    yaxis2=dict(title='Average Rating', overlaying='y', side='right'),
    legend=dict(x=0.5, y=1.1, orientation='h'),
    plot_bgcolor='white',
    height=500
)
st.plotly_chart(fig8, use_container_width=True)

# ========== EXPORT ==========
st.markdown("<h3 class='task-header'>📥 Download Processed Data</h3>", unsafe_allow_html=True)
if st.button("📤 Export CSV"):
    export_df = pd.concat([top_df, city_summary, price_df], axis=1)
    export_df.to_csv("level1_summary.csv", index=False)
    st.success("✅ Exported as level1_summary.csv")

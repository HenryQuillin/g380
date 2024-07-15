import streamlit as st
import pandas as pd
from data_helpers import get_all_companies_data
from datetime import datetime, timedelta

st.set_page_config(page_title="All News", page_icon="📰", layout="wide")

with open('./styles.css') as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.title('ALL NEWS')

end_date = datetime.now()
start_date = end_date - timedelta(days=365)
df = get_all_companies_data(start_date, end_date)

df['source_name'] = df['source'].apply(lambda source: source['name'])


all_companies = sorted(df['company'].unique())
colors = ['#e6f3ff', '#fff0e6', '#e6ffe6', '#ffe6e6', '#e6e6ff', '#f0f0f0', '#ffe6cc', '#e6fffa', '#fff5e6', '#e6e6ff']
color_map = dict(zip(all_companies, colors[:len(all_companies)]))

# Display options -------------
col1, col2 = st.columns([1,1])
with col1:
    show_descriptions = st.toggle('Show Descriptions', value=True)
with col2:
    view_mode = st.radio('View Mode', options=['List', 'Grid'], horizontal=True, label_visibility="collapsed")


# FILTERS -----------
col1, col2, col3, col4 = st.columns(4)
with col1:
    company_filter = st.multiselect('Select Companies', options=all_companies)
with col2:
    source_filter = st.multiselect('Select Sources', options=sorted(df['source_name'].unique()))
with col3:
    date_range = st.date_input('Select Date Range',
                               value=(df['publishedAt'].min().date(), df['publishedAt'].max().date()),
                               min_value=df['publishedAt'].min().date(), max_value=df['publishedAt'].max().date())
with col4:
    search_term = st.text_input('Search')



# filters logic -------------------
filtered_df = df.copy()
if company_filter:
    filtered_df = filtered_df[filtered_df['company'].isin(company_filter)]
if source_filter:
    filtered_df = filtered_df[filtered_df['source_name'].isin(source_filter)]
if date_range:
    filtered_df = filtered_df[
        (filtered_df['publishedAt'].dt.date >= date_range[0]) & (filtered_df['publishedAt'].dt.date <= date_range[1])]
if search_term:
    filtered_df = filtered_df[filtered_df['title'].str.contains(search_term, case=False) |
                              filtered_df['description'].str.contains(search_term, case=False) |
                              filtered_df['content'].str.contains(search_term, case=False)]


filtered_df = filtered_df.sort_values('publishedAt', ascending=False)


news_container = st.container()
with news_container:
    if view_mode == "Grid":
        cols = st.columns(3)
        news_card_class = "news-card-grid-view"
        if not show_descriptions:
            news_card_class = "news-card-grid-view-no-descriptions"
    else:
        cols = [st.columns(1)[0]]  #list view
        news_card_class = ""

    for index, row in filtered_df.iterrows():
        col = cols[index % len(cols)]
        with col:
            company_color = color_map.get(row['company'], "#ffffff")
            description_html = ""
            if show_descriptions and pd.notna(row['description']):
                description_html = f"<div class='news-description'>{row['description']}</div>"

            st.markdown(f"""
            <div class="news-card {news_card_class}">
                <div class="news-title">
                    <a href="{row['url']}" target="_blank">{row['title']}</a>
                </div>
                <div class="news-meta">
                    <span class="company-tag" style="background-color: {company_color}; color: #000000;">{row['company']}</span> | 
                    {row['source_name']} | {row['publishedAt'].strftime('%b %d %Y, %I:%M %p')}
                </div>
                {description_html}
            </div>
            """, unsafe_allow_html=True)

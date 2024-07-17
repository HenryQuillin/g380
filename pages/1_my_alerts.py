import streamlit as st
import pandas as pd
from data_helpers import get_mock_data
from database import get_all_companies, get_company_keywords
from datetime import datetime, timedelta
from notifications import create_notifications
from duplicate_detection import detect_duplicates

st.set_page_config(page_title="My Alerts", page_icon="🚨", layout="wide")

# Import CSS
with open('./styles.css') as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.title('MY ALERTS')

# Sidebar
st.sidebar.header("Controls")

# Initialize session state variables if they don't exist
if 'date_range' not in st.session_state:
    st.session_state.date_range = (datetime.now() - timedelta(days=30), datetime.now())
if 'news_log' not in st.session_state:
    st.session_state.news_log = []

# Date range in sidebar
date_range = st.sidebar.date_input(
    "Select Date Range",
    value=st.session_state.date_range,
    min_value=datetime.now() - timedelta(days=365),
    max_value=datetime.now(),
)

# Ensure we always have two dates, even if the user only selects one
if len(date_range) == 2:
    start_date, end_date = date_range
elif len(date_range) == 1:
    start_date = end_date = date_range[0]
else:
    start_date, end_date = st.session_state.date_range

# Update session state
st.session_state.date_range = (start_date, end_date)

# Fetch news button in sidebar
fetch_button = st.sidebar.button('Fetch News')

# Main content area
# Control options on the same line

companies = get_all_companies()
company_options = {company['id']: company['name'] for company in companies if company['name']}

col1, col2 = st.columns([1,1])
with col1:
    show_descriptions = st.toggle('Show Descriptions', value=True)
with col2:
    view_mode = st.radio('View Mode', options=['List', 'Grid'], horizontal=True, label_visibility="collapsed")


selected_company_ids = st.multiselect('Filter Companies', options=list(company_options.keys()),
                                          format_func=lambda x: company_options[x])

# Color map
all_companies = sorted(company_options.values())
colors = ['#e6f3ff', '#fff0e6', '#e6ffe6', '#ffe6e6', '#e6e6ff', '#f0f0f0', '#ffe6cc', '#e6fffa', '#fff5e6', '#e6e6ff']
color_map = dict(zip(all_companies, colors[:len(all_companies)]))


# Fetch news function
def fetch_news():
    all_news = []
    for company in companies:
        if company['name']:
            articles = get_mock_data(company['name'], start_date, end_date)
            keywords = get_company_keywords(company['id'])
            filtered_articles = filter_articles(articles.to_dict('records'), keywords)
            for article in filtered_articles:
                article['company'] = company['name']  # Add company name to each article
            all_news.extend(filtered_articles)

    # Sort by publishing date
    all_news.sort(key=lambda x: x.get('publishedAt', ''), reverse=True)

    # Apply duplicate detection
    grouped_articles = detect_duplicates(all_news)

    st.session_state.news_log = grouped_articles
    create_notifications(grouped_articles)


# Filter articles function (assuming you have this from before)
def filter_articles(articles, keywords):
    # Implement your filtering logic here
    return articles


if fetch_button:
    fetch_news()

# Display news
if st.session_state.news_log:
    # Filter news based on selected companies
    filtered_news = st.session_state.news_log
    if selected_company_ids:
        selected_companies = [company_options[id] for id in selected_company_ids]
        filtered_news = [article for article in filtered_news if article.get('company') in selected_companies]

    news_container = st.container()
    with news_container:
        if view_mode == "Grid":
            news_card_class = "news-card-grid-view"
            if not show_descriptions:
                news_card_class = "news-card-grid-view-no-descriptions"
            col1, col2, col3 = st.columns(3)
            cols = [col1, col2, col3]
        else:
            cols = [st.columns(1)[0]]
            news_card_class = ""

        for i, article in enumerate(filtered_news):
            if view_mode == "Grid":
                col = cols[i % 3]
            else:
                col = cols[0]

            with col:
                # Check if article is a dictionary, if not, skip it
                if not isinstance(article, dict):
                    st.warning(f"Skipping invalid article data: {article}")
                    continue

                company_name = article.get('company', 'Unknown Company')
                company_color = color_map.get(company_name, "#ffffff")
                description_html = ""
                if show_descriptions and pd.notna(article.get('description')):
                    description_html = f"<div class='news-description'>{article['description']}</div>"

                st.markdown(f"""
                <div class="news-card {news_card_class}">
                    <div class="news-title">
                        <a href="{article.get('url', '#')}" target="_blank">{article.get('title', 'No Title')}</a>
                    </div>
                    <div class="news-meta">
                        <span class="company-tag" style="background-color: {company_color}; color: #000000;">{company_name}</span> | 
                        {article.get('source', {}).get('name', 'Unknown Source')} | {article.get('publishedAt', 'Unknown Date')}
                    </div>
                    {description_html}
                </div>
                """, unsafe_allow_html=True)

                if 'duplicates' in article and article['duplicates']:
                    with st.expander(f"Show {len(article['duplicates'])} duplicate article(s)"):
                        for dup in article['duplicates']:
                            if isinstance(dup, dict):
                                st.markdown(f"- [{dup.get('title', 'No Title')}]({dup.get('url', '#')})")
                            else:
                                st.warning(f"Invalid duplicate data: {dup}")
else:
    st.info("No news fetched yet. Click 'Fetch News' in the sidebar to get started.")
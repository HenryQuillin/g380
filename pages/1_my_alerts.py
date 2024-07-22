import streamlit as st
import pandas as pd
from data_helpers import get_mock_data
from database import get_all_companies, get_company_keywords
from datetime import datetime, timedelta
from notifications import create_notifications
from duplicate_detection import detect_duplicates

st.set_page_config(page_title="My Alerts", page_icon="🚨", layout="wide")

with open('./styles.css') as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.title('MY ALERTS')

st.sidebar.header("Simulate Fetch")

if 'date_range' not in st.session_state:
    st.session_state.date_range = (datetime(2024, 6, 1), datetime.now())
if 'news_log' not in st.session_state:
    st.session_state.news_log = []
if 'fetch_attempted' not in st.session_state:
    st.session_state.fetch_attempted = False
if 'no_news_reason' not in st.session_state:
    st.session_state.no_news_reason = None

# Ssidebar ---------------
date_range = st.sidebar.date_input(
    "Select Date Range",
    value=st.session_state.date_range,
    min_value=datetime.now() - timedelta(days=365),
    max_value=datetime.now(),
)
fetch_button = st.sidebar.button('Fetch News')

if len(date_range) == 2:
    start_date, end_date = date_range
# elif len(date_range) == 1:
#     start_date = end_date = date_range[0]
else:
    start_date, end_date = st.session_state.date_range

st.session_state.date_range = (start_date, end_date)





companies = get_all_companies()
company_options = {company['id']: company['name'] for company in companies if company['name']}


# filters and stuff ------------
col1, col2 = st.columns([1,1])
with col1:
    show_descriptions = st.toggle('Show Descriptions', value=True)
with col2:
    view_mode = st.radio('View Mode', options=['List', 'Grid'], horizontal=True, label_visibility="collapsed")

selected_company_ids = st.multiselect('Filter Companies', options=list(company_options.keys()),
                                      format_func=lambda x: company_options[x])

# colors -------------
all_companies = sorted(company_options.values())
colors = ['#e6f3ff', '#fff0e6', '#e6ffe6', '#ffe6e6', '#e6e6ff', '#f0f0f0', '#ffe6cc', '#e6fffa', '#fff5e6', '#e6e6ff']
color_map = dict(zip(all_companies, colors[:len(all_companies)]))

def format_date(date_str):
    try:
        date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
        return date.strftime("%b %d %Y, %I:%M %p")
    except:
        return date_str

# Fetch news function
def fetch_news():
    all_news = []
    for company in companies:
        if company['name']:
            keywords = get_company_keywords(company['id'])
            keyword_list = [k['keyword'] for k in keywords if k['keyword']]
            articles = get_mock_data(company['name'], start_date, end_date, keyword_list)
            filtered_articles = articles.to_dict('records')
            for article in filtered_articles:
                article['company'] = company['name']  # Add company name to each article
            all_news.extend(filtered_articles)

    if not all_news:
        st.session_state.news_log = []
        st.session_state.fetch_attempted = True
        st.session_state.no_news_reason = "date_range"
        return

    # Sort by publishing date
    all_news.sort(key=lambda x: x.get('publishedAt', ''), reverse=True)

    # Apply duplicate detection
    grouped_articles = detect_duplicates(all_news)

    st.session_state.news_log = grouped_articles
    st.session_state.fetch_attempted = True
    st.session_state.no_news_reason = None
    create_notifications(grouped_articles)
    st.success(f"Found {len(grouped_articles)} unique articles.")

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

    if not filtered_news:
        st.info("No news found for the selected companies. Try adjusting your filters.")
    else:
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

                    # Format the main article's date
                    formatted_date = format_date(article.get('publishedAt', 'Unknown Date'))

                    # Prepare duplicate articles HTML
                    duplicates_html = ""
                    if 'duplicates' in article and article['duplicates']:
                        duplicates_html = f"""<details class="duplicates-dropdown">
                            <summary>Show {len(article['duplicates'])} duplicate article(s)</summary>
                            <ul class="duplicates-list">"""

                        for dup in article['duplicates']:
                            if isinstance(dup, dict):
                                dup_formatted_date = format_date(dup.get('publishedAt', 'Unknown Date'))
                                duplicates_html += f"""
                                <li class="duplicate-item">
                                    <a href="{dup.get('url', '#')}" target="_blank" class="duplicate-title">{dup.get('title', 'No Title')}</a>
                                    <div class="duplicate-meta">
                                        {dup.get('source', {}).get('name', 'Unknown Source')} | {dup_formatted_date}
                                    </div>
                                </li>"""
                            else:
                                duplicates_html += f"<li>Invalid duplicate data: {dup}</li>"
                        duplicates_html += "</ul></details>"

                    st.markdown(f"""
                    <div class="news-card {news_card_class}">
                        <div class="news-title">
                            <a href="{article.get('url', '#')}" target="_blank">{article.get('title', 'No Title')}</a>
                        </div>
                        <div class="news-meta">
                            <span class="company-tag" style="background-color: {company_color}; color: #000000;">{company_name}</span> | 
                            {article.get('source', {}).get('name', 'Unknown Source')} | {formatted_date}
                        </div>
                        {description_html}{duplicates_html}
                    </div>
                    """, unsafe_allow_html=True)

elif st.session_state.fetch_attempted:
    if st.session_state.no_news_reason == "date_range":
        st.warning("No news found for the selected date range.")
    else:
        st.info("No news found for the selected date range and filters.")
else:
    st.info("Click 'Fetch News' in the sidebar to get started.")
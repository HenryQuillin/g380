import streamlit as st
from data_helpers import get_mock_data
from database import get_all_companies, get_company_keywords
from datetime import datetime, timedelta
import pandas as pd
from notifications import show_notification

st.set_page_config(page_title="News Log", page_icon="📰")

with open('./styles.css') as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

companies = get_all_companies()
st.title('News Log')

def trigger_notification(articles):
    if articles:
        if len(articles) == 1:
            title = f"News Alert: {articles[0]['title']}"
            body = f"{articles[0]['description']}..."
        else:
            title = f"News Alert: {articles[0]['title']}"
            body = f"+{len(articles) - 1} other news alerts"

        show_notification(title, body)

# Initialize session state for date inputs if they don't exist
if 'start_date' not in st.session_state:
    st.session_state.start_date = datetime.now() - timedelta(days=3)
if 'end_date' not in st.session_state:
    st.session_state.end_date = datetime.now()

def update_dates():
    st.session_state.start_date = st.session_state.start_date_input
    st.session_state.end_date = st.session_state.end_date_input

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    start_date = st.date_input("Start Date", st.session_state.start_date, key='start_date_input', on_change=update_dates)
with col2:
    end_date = st.date_input("End Date", st.session_state.end_date, key='end_date_input', on_change=update_dates)
with col3:
    fetch_button = st.button('Fetch News')

if fetch_button:
    st.session_state.news_log = {}
    for company in companies:
        if company['name']:
            articles = get_mock_data(company['name'], st.session_state.start_date, st.session_state.end_date)
            st.session_state.news_log[company['name']] = articles.to_dict('records')


if 'news_log' in st.session_state and st.session_state.news_log:
    companies = get_all_companies()
    company_options = {company['id']: company['name'] for company in companies}
    selected_company_id = st.selectbox('Select a company to view news', options=list(company_options.keys()),
                                       format_func=lambda x: company_options[x])

    if selected_company_id:
        selected_company_name = company_options[selected_company_id]

        st.markdown("""<hr style="background-color:#333;" /> """, unsafe_allow_html=True)
        # st.markdown("""<hr /> """)

        keywords = get_company_keywords(selected_company_id)
        keyword_list = [k['keyword'].lower() for k in keywords if k['keyword']]

        filtered_news = []
        for article in st.session_state.news_log[selected_company_name]:
            title = article.get('title', '').lower() if article.get('title', '') else ''
            description = article.get('description', '') if article.get('description', '') else ''
            if not keyword_list or any(keyword in title or keyword in description for keyword in keyword_list):
                filtered_news.append(article)
            # if not keyword_list:
            #   for keyword in keyword_list:
            #   if keyword in title or keyword in description
            #     filtered_news.append(article)

        for article in filtered_news:
            with st.container():
                st.markdown(f"###### [{article.get('title', 'No Title')}]({article.get('url', '#')})")
                st.markdown(
                    f"**Source:** [{article.get('source', {}).get('name', 'Unknown Source')}]({article.get('url', '#')})")
                if 'publishedAt' in article:
                    # Handle the case where publishedAt is already a tiemstamp
                    if isinstance(article['publishedAt'], pd.Timestamp):
                        published_date = article['publishedAt'].to_pydatetime()
                    else:
                        published_date = datetime.strptime(article['publishedAt'], "%Y-%m-%dT%H:%M:%SZ")
                    st.markdown(f"**Published:** {published_date.strftime('%B %d, %Y at %I:%M %p')}")
                st.markdown(f"**Description:** {article.get('description', 'No description available')}")
                st.markdown("---")

        if fetch_button: trigger_notification(filtered_news)


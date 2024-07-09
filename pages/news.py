import streamlit as st
from data_helpers import get_mock_data
from database import get_all_companies, get_company_keywords
from datetime import datetime
import pandas as pd
from notifications import create_notifications

st.set_page_config(page_title="News Log", page_icon="📰")

# import css
with open('./styles.css') as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

companies = get_all_companies()
st.title('News Log')


# Start date, end date, and fetch news buttons:
def update_dates():
    st.session_state.start_date = st.session_state.start_date_input # contains the value of the element with key 'start_date_input'
    st.session_state.end_date = st.session_state.end_date_input

# set default dates
if 'start_date' not in st.session_state:
    st.session_state.start_date = datetime(2024, 6, 1)
if 'end_date' not in st.session_state:
    st.session_state.end_date = datetime(2024, 7, 1)

col1, col2, col3 = st.columns(3)
with col1:
    start_date = st.date_input("Start Date", st.session_state.start_date, key='start_date_input', on_change=update_dates)
with col2:
    end_date = st.date_input("End Date", st.session_state.end_date, key='end_date_input', on_change=update_dates)
with col3:
    fetch_button = st.button('Fetch News')

# filters articles
def filter_articles(articles, keywords):
    keyword_list = [k['keyword'].lower() for k in keywords if k['keyword']]

    if not keyword_list:
        return articles

    filtered_articles = []

    for article in articles:
        title = article.get('title', '').lower()
        description = article.get('description', '').lower()

        # check if any keyword is in the title or description
        for keyword in keyword_list:
            if keyword in title or keyword in description:
                filtered_articles.append(article)
                break  # move to next article once a match is found

    return filtered_articles


if fetch_button: # when fetch button is pressed
    st.session_state.news_log = {}
    all_filtered_news = [] # 2d array
    start = datetime.combine(st.session_state.start_date, datetime.min.time())
    end = datetime.combine(st.session_state.end_date, datetime.max.time())

    # populate the news log for each company with the filtered articles
    for company in companies:
        if company['name']:
            articles = get_mock_data(company['name'], start, end)
            keywords = get_company_keywords(company['id'])
            filtered_articles = filter_articles(articles.to_dict('records'), keywords)
            st.session_state.news_log[company['name']] = filtered_articles
            all_filtered_news.extend(filtered_articles)

    # trigger browser notification
    create_notifications(all_filtered_news)

if 'news_log' in st.session_state and st.session_state.news_log: # if news log has been initialized and isn't empty
    company_options = {company['id']: company['name'] for company in companies}
    selected_company_id = st.selectbox('Select a company to view news', options=list(company_options.keys()),
                                       format_func=lambda x: company_options[x])

    if selected_company_id:
        selected_company_name = company_options[selected_company_id]
        st.markdown("""<hr style="background-color:#333;" /> """, unsafe_allow_html=True)

        filtered_news = st.session_state.news_log[selected_company_name]

        # display the filtered news for the selected company
        for article in filtered_news:
            with st.container():
                st.markdown(f"###### [{article.get('title', 'No Title')}]({article.get('url', '#')})")
                st.markdown(
                    f"**Source:** [{article.get('source', {}).get('name', 'Unknown Source')}]({article.get('url', '#')})")
                if 'publishedAt' in article:
                    if isinstance(article['publishedAt'], pd.Timestamp):
                        published_date = article['publishedAt'].to_pydatetime()
                    else:
                        published_date = datetime.strptime(article['publishedAt'], "%Y-%m-%dT%H:%M:%SZ")
                    st.markdown(f"**Published:** {published_date.strftime('%B %d, %Y at %I:%M %p')}")
                st.markdown(f"**Description:** {article.get('description', 'No description available')}")
                st.markdown("---")
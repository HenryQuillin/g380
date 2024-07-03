import streamlit as st
from data_helpers import get_mock_data
from database import get_all_companies, get_company_keywords
from datetime import datetime, timedelta
import pandas as pd

companies = get_all_companies()
st.title('News Log')

# Add date inputs
col1, col2, col3 = st.columns(3)
with col1:
    start_date = st.date_input("Start Date", datetime.now() - timedelta(days=30))
with col2:
    end_date = st.date_input("End Date", datetime.now())
with col3:
    fetch_button = st.button('Fetch News')

if fetch_button:
    st.session_state.news_log = {}
    for company in companies:
        if company['name']:
            articles = get_mock_data(company['name'], start_date, end_date)
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
                    # Handle the case where publishedAt is already a Timestamp
                    if isinstance(article['publishedAt'], pd.Timestamp):
                        published_date = article['publishedAt'].to_pydatetime()
                    else:
                        published_date = datetime.strptime(article['publishedAt'], "%Y-%m-%dT%H:%M:%SZ")
                    st.markdown(f"**Published:** {published_date.strftime('%B %d, %Y at %I:%M %p')}")
                st.markdown(f"**Description:** {article.get('description', 'No description available')}")
                st.markdown("---")
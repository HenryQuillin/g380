import streamlit as st
from mock_data import get_mock_data
from database import get_all_companies

# Always fetch the companies from the database at the start of the script
companies = get_all_companies()

fetch_button = st.button('Fetch News')

if fetch_button:
    st.session_state.news_log = {}
    for company in companies:
        if company['name']:
            articles = get_mock_data(company['name'])
            st.session_state.news_log[company['name']] = articles.to_dict('records')

# Dropdown to select a company to view news
if 'news_log' in st.session_state and st.session_state.news_log:
    company_names = [company['name'] for company in companies if company['name']]
    selected_company = st.selectbox('Select a company to view news', company_names)

    if selected_company:
        st.subheader(f'News for {selected_company}')
        for article in st.session_state.news_log[selected_company]:
            st.write(f"Title: {article['title']}")
            st.write(f"URL: {article['url']}")
            st.write("------")

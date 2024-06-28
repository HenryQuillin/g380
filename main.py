import streamlit as st
from mock_data import get_mock_data

st.title('News Alert Dashboard')

def add_company():
    companies = st.session_state.companies
    companies.append({'name': ''})
    st.session_state.companies = companies

# init session state
if 'companies' not in st.session_state:
    st.session_state.companies = [{'name': ''}]

# input fields
for i in range(len(st.session_state.companies)):
    st.session_state.companies[i]['name'] = st.text_input(f"Company {i+1}", key=f"company_{i}")

st.button('Add another company', on_click=add_company)

fetch_button = st.button('Fetch News')

# fethc button clicked
if fetch_button:
    st.session_state.news_log = {}
    for company in st.session_state.companies:
        if company['name']:
            articles = get_mock_data(company['name'])
            st.session_state.news_log[company['name']] = articles.to_dict('records')

# Dropdown
if 'news_log' in st.session_state and st.session_state.news_log:
    company_names = [company['name'] for company in st.session_state.companies if company['name']]
    selected_company = st.selectbox('Select a company to view news', company_names)

    if selected_company:
        st.subheader(f'News for {selected_company}')
        for article in st.session_state.news_log[selected_company]:
            st.write(f"Title: {article['title']}")
            st.write(f"URL: {article['url']}")
            st.write("------")

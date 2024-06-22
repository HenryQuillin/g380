import streamlit as st
from newsapi import NewsApiClient


# Initialize News API client
newsapi = NewsApiClient(api_key='220006a62eee4308af38c32b7e0fbabf')

st.title('News Alert Dashboard')

# Function to add a new company field
def add_company():
    companies = st.session_state.companies
    companies.append({'name': ''})  # Add new company with empty name
    st.session_state.companies = companies

# Initialize session state for companies if not already set
if 'companies' not in st.session_state:
    st.session_state.companies = [{'name': ''}]

# Display company input fields
for i in range(len(st.session_state.companies)):
    st.session_state.companies[i]['name'] = st.text_input(f"Company {i+1}", key=f"company_{i}")

# Button to add more companies
st.button('Add another company', on_click=add_company)

# Button to fetch news
fetch_button = st.button('Fetch News')


# Assuming continuation from the above code

# Fetch news and store in session state when the button is clicked
if fetch_button:
    # Dictionary to hold news articles for each company
    st.session_state.news_log = {}
    for company in st.session_state.companies:
        if company['name']:
            # Fetch top headlines for the company
            articles = newsapi.get_everything(q=company['name'],from_param="2024-06-21", to="2024-06-22")
            st.session_state.news_log[company['name']] = articles['articles']

# Dropdown to select a company to view news
if 'news_log' in st.session_state and st.session_state.news_log:
    company_names = [company['name'] for company in st.session_state.companies if company['name']]
    selected_company = st.selectbox('Select a company to view news', company_names)

    # Display news for the selected company
    if selected_company:
        st.subheader(f'News for {selected_company}')
        for article in st.session_state.news_log[selected_company]:
            st.write(f"Title: {article['title']}")
            st.write(f"URL: {article['url']}")
            st.write("------")

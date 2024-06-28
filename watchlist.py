import streamlit as st
from database import init_db, add_company_to_db, get_all_companies, remove_company_from_db

init_db()  # Initialize the database and table

st.title('Watchlist')

def add_company():
    add_company_to_db('')  # Add empty company to the database
    st.experimental_rerun()  # Rerun to refresh the list from the database

companies = get_all_companies()


for company in companies:
    col1, col2 = st.columns([4, 1])
    with col1:
        company_name = st.text_input(f"Company {company['id']}", value=company['name'], key=f"company_{company['id']}")
        if company_name != company['name']:
            add_company_to_db(company_name)  # Update the company name in the database
    with col2:
        remove_button = st.button("Remove", key=f"remove_{company['id']}")
        if remove_button:
            remove_company_from_db(company['id'])
            st.experimental_rerun()

if st.button('Add another company'):
    add_company()

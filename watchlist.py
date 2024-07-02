import streamlit as st
from database import init_db, add_company_to_db, get_all_companies, remove_company_from_db

init_db()

st.title('Watchlist')

def add_company():
    add_company_to_db('')
    st.experimental_rerun()  # rerun to rerfesh the list from the database

companies = get_all_companies()


for company in companies:
    col1, col2 = st.columns([4, 1])
    with col1:
        company_name = st.text_input(f"company {company['id']}", value=company['name'], key=f"company_{company['id']}", label_visibility="collapsed")
        if company_name != company['name']:
            remove_company_from_db(company['id'])
            add_company_to_db(company_name)
            st.experimental_rerun()
    with col2:
        remove_button = st.button("Remove", key=f"remove_{company['id']}")
        if remove_button:
            remove_company_from_db(company['id'])
            st.experimental_rerun()

if st.button('Add company'):
    add_company()

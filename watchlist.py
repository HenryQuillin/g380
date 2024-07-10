import streamlit as st
from database import init_db, add_company_to_db, get_all_companies, remove_company_from_db

def render_watchlist():

    init_db()


    st.title('Watchlist')

    with open('./styles.css') as f:
        css = f.read()
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

    def add_company():
        add_company_to_db('')
        st.rerun()  # This essentially reruns the code on this page.
        # We just added an empty entry to the DB,
        # so we need to refresh the UI to display the new input element for that enty

    companies = get_all_companies()


    for company in companies:
        col1, col2 = st.columns([4, 1]) # setting up the UI
        with col1:
            company_name = st.text_input(f"company {company['id']}", value=company['name'], key=f"company_{company['id']}", label_visibility="collapsed").lower()
            # Edit company
            if company_name != company['name']:
                remove_company_from_db(company['id'])
                add_company_to_db(company_name)
                st.rerun()
        with col2:
            # Remove company
            remove_button = st.button("Remove", key=f"remove_company_{company['id']}")
            if remove_button:
                remove_company_from_db(company['id'])
                st.rerun()

    # Add company
    if st.button('Add company'):
        add_company()

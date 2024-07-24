import streamlit as st
from database import init_db, add_company_to_db, get_all_companies, remove_company_from_db

def render_watchlist():

    init_db()

    st.subheader('Watchlist')

    with open('./styles.css') as f:
        css = f.read()
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

    def capitalize_name(name):
        return ' '.join(word.capitalize() for word in name.split())

    def add_company():
        new_company = capitalize_name(st.session_state.new_company.strip())
        existing_companies = [company['name'].lower() for company in get_all_companies()]
        if new_company and new_company.lower() not in existing_companies:
            add_company_to_db(new_company)
            st.session_state.new_company = ''
            # st.rerun()  # This essentially reruns the code on this page.
            # We just added a new entry to the DB,
            # so we need to refresh the UI to display the new input element for that entry
        elif new_company.lower() in existing_companies:
            st.error(f"'{new_company}' is already in your watchlist.")
        else:
            st.error("Please enter a company name.")

    companies = get_all_companies()

    for company in companies:
        col1, col2 = st.columns([4, 1]) # setting up the UI
        with col1:
            company_name = st.text_input(f"company {company['id']}", value=company['name'], key=f"company_{company['id']}", label_visibility="collapsed")
            company_name = capitalize_name(company_name)
            # Edit company
            if company_name.lower() != company['name'].lower():
                existing_companies = [c['name'].lower() for c in companies if c['id'] != company['id']]
                if company_name.lower() in existing_companies:
                    st.error(f"'{company_name}' is already in your watchlist.")
                elif company_name:
                    remove_company_from_db(company['id'])
                    add_company_to_db(company_name)
                    st.rerun()
                else:
                    st.error("Company name cannot be empty.")
        with col2:
            # Remove company
            remove_button = st.button("Remove", key=f"remove_company_{company['id']}")
            if remove_button:
                remove_company_from_db(company['id'])
                st.rerun()

    # Add company
    col1, col2 = st.columns([4, 1])
    with col1:
        st.text_input("Add a new company", key="new_company", on_change=add_company, label_visibility="collapsed")
    with col2:
        if st.button('Add company'):
            add_company()
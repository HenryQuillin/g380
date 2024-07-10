import streamlit as st
from database import init_db, add_keyword_to_db, get_company_keywords, remove_keyword_from_db, get_all_companies


def render_keywords():
    init_db()

    st.subheader('Keywords')
    # setting up comapny
    companies = get_all_companies()
    company_options = {company['id']: company['name'] for company in companies}

    selected_company_id = st.selectbox('Select a company', options=list(company_options.keys()),
                                       format_func=lambda x: company_options[x])


    if selected_company_id:
        # essentially same logic as watchlist.py
        def add_keyword():
            add_keyword_to_db(selected_company_id, '')
            st.rerun()

        keywords = get_company_keywords(selected_company_id)

        for keyword in keywords:
            col1, col2 = st.columns([4, 1])
            with col1:
                new_keyword = st.text_input(f"keyword {keyword['id']}", value=keyword['keyword'],
                                            key=f"keyword_{keyword['id']}", label_visibility="collapsed")
                if new_keyword != keyword['keyword']:
                    # edit
                    remove_keyword_from_db(keyword['id'])
                    add_keyword_to_db(selected_company_id, new_keyword)
                    st.rerun()
            with col2:
                # remove
                if st.button("Remove", key=f"remove_keyword_{keyword['id']}"):
                    remove_keyword_from_db(keyword['id'])
                    st.rerun()
        # add
        if st.button('Add keyword'):
            add_keyword()



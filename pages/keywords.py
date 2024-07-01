import streamlit as st
from database import init_db, add_keyword_to_db, get_company_keywords, remove_keyword_from_db, get_all_companies

init_db()

st.title('Keywords')

companies = get_all_companies()
company_options = {company['id']: company['name'] for company in companies}

selected_company_id = st.selectbox('Select a company', options=list(company_options.keys()), format_func=lambda x: company_options[x])

if selected_company_id:
    st.subheader(f'Keywords for {company_options[selected_company_id]}')

    def add_keyword():
        add_keyword_to_db(selected_company_id, '')
        st.experimental_rerun()

    keywords = get_company_keywords(selected_company_id)
    print(keywords)

    for keyword in keywords:
        col1, col2 = st.columns([4, 1])
        with col1:
            new_keyword = st.text_input(f"Keyword {keyword['id']}", value=keyword['keyword'], key=f"keyword_{keyword['id']}")
            if new_keyword != keyword['keyword']:
                remove_keyword_from_db(keyword['id'])
                add_keyword_to_db(selected_company_id, new_keyword)
                st.experimental_rerun()
        with col2:
            if st.button("Remove", key=f"remove_{keyword['id']}"):
                remove_keyword_from_db(keyword['id'])
                st.experimental_rerun()

    if st.button('Add another keyword'):
        add_keyword()

st.write("Debug Information:")
st.write(f"Selected Company ID: {selected_company_id}")
st.write(f"Keywords: {keywords if 'keywords' in locals() else 'No company selected'}")
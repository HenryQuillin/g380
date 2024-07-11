import streamlit as st
import pandas as pd
from data_helpers import get_all_companies_data
from datetime import datetime, timedelta

st.set_page_config(page_title="All News", page_icon="📰", layout="wide")



st.title('ALL NEWS')

end_date = datetime.now()
start_date = end_date - timedelta(days=365)
df = get_all_companies_data(start_date, end_date)


# source is an object so need to extract the source name
df['source_name'] = df['source'].apply(lambda source: source['name'])


#
all_companies = sorted(df['company'].unique())
colors = ['#e6f3ff', '#fff0e6', '#e6ffe6', '#ffe6e6', '#e6e6ff', '#f0f0f0', '#ffe6cc', '#e6fffa', '#fff5e6', '#e6e6ff']
# create pairs of company names and colors then turn into dictionary
color_map = dict(zip(all_companies, colors[:len(all_companies)]))

# FILTERS
st.sidebar.header('Filters')
company_filter = st.sidebar.multiselect('Select Companies', options=all_companies)
source_filter = st.sidebar.multiselect('Select Sources', options=sorted(df['source_name'].unique()))
date_range = st.sidebar.date_input('Select Date Range',
                                   value=(df['publishedAt'].min().date(), df['publishedAt'].max().date()),
                                   min_value=df['publishedAt'].min().date(), max_value=df['publishedAt'].max().date())
search_term = st.sidebar.text_input('Search')

# Apply filters
filtered_df = df.copy()
if company_filter:
    filtered_df = filtered_df[filtered_df['company'].isin(company_filter)]
if source_filter:
    filtered_df = filtered_df[filtered_df['source_name'].isin(source_filter)]
if date_range:
    filtered_df = filtered_df[
        (filtered_df['publishedAt'].dt.date >= date_range[0]) & (filtered_df['publishedAt'].dt.date <= date_range[1])]
if search_term:
    filtered_df = filtered_df[filtered_df['title'].str.contains(search_term, case=False) |
                              filtered_df['description'].str.contains(search_term, case=False) |
                              filtered_df['content'].str.contains(search_term, case=False)]



def style_dataframe(df):
    # changes the background color of the company column & formats the date
    def highlight_company_names(series):
        background_color_styles = []

        for company_name in series:
            background_color = color_map.get(company_name, "#ffffff")
            background_color_styles.append(f'background-color: {background_color}')

        return background_color_styles

    styled_dataframe = df.style.apply(highlight_company_names, subset=['company'])

    def format_published_at(date_value):
        if pd.notna(date_value):
            formatted_date = date_value.strftime('%b %d %Y, %I%p')
        else:
            formatted_date = ''

        return formatted_date
    styled_dataframe = styled_dataframe.format({
        'publishedAt': format_published_at
    })

    return styled_dataframe


display_columns = ['title', 'company', 'url', 'source_name', 'publishedAt', 'description', 'content']
styled_df = style_dataframe(filtered_df[display_columns])

st.dataframe(
    styled_df,
    column_config={
        "title": st.column_config.Column("Title", width="medium"),
        "company": st.column_config.Column("Company", width="small"),
        "url": st.column_config.LinkColumn("URL", width="small"),
        "source_name": st.column_config.Column("Source", width="small"),
        "publishedAt": st.column_config.Column("Published At", width="small"),
        "description": st.column_config.Column("Description", width="large"),
        "content": st.column_config.Column("Content", width="large")
    },
    height=600,
    use_container_width=True,
    hide_index=True
)

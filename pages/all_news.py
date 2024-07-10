import streamlit as st
import pandas as pd
from data_helpers import get_all_companies_data
from datetime import datetime, timedelta

st.set_page_config(page_title="All News", page_icon="📰", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    .dataframe {
        font-family: Arial, sans-serif;
    }
    .dataframe th {
        background-color: #f8f9fa;
        color: #202124;
        font-weight: bold;
        text-align: left;
        padding: 10px;
    }
    .dataframe td {
        padding: 8px;
    }
    .dataframe tr:nth-child(even) {
        background-color: #f8f9fa;
    }
    .dataframe tr:hover {
        background-color: #e8eaed;
    }
</style>
""", unsafe_allow_html=True)

st.title('All News')

# Fetch all news
end_date = datetime.now()
start_date = end_date - timedelta(days=365)  # Fetch news for the last year
df = get_all_companies_data(start_date, end_date)


# Function to extract source name
def get_source_name(source):
    if isinstance(source, dict) and 'name' in source:
        return source['name']
    return str(source)


# Extract source names
df['source_name'] = df['source'].apply(get_source_name)

# Create a consistent color map for all companies
all_companies = sorted(df['company'].unique())
colors = ['#e6f3ff', '#fff0e6', '#e6ffe6', '#ffe6e6', '#e6e6ff', '#f0f0f0', '#ffe6cc', '#e6fffa', '#fff5e6', '#e6e6ff']
color_map = dict(zip(all_companies, colors[:len(all_companies)]))

# Create filter inputs
st.sidebar.header('Filters')
company_filter = st.sidebar.multiselect('Select Companies', options=all_companies)
source_filter = st.sidebar.multiselect('Select Sources', options=sorted(df['source_name'].unique()))
date_range = st.sidebar.date_input('Select Date Range',
                                   value=(df['publishedAt'].min().date(), df['publishedAt'].max().date()),
                                   min_value=df['publishedAt'].min().date(), max_value=df['publishedAt'].max().date())
search_term = st.sidebar.text_input('Search in Title or Description')

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
                              filtered_df['description'].str.contains(search_term, case=False)]


# Styling function
def style_dataframe(df):
    def highlight_companies(s):
        return [f'background-color: {color_map.get(val, "#ffffff")}' for val in s]

    def truncate(text, length=100):
        if pd.isna(text):
            return ''
        return str(text)[:length] + '...' if len(str(text)) > length else str(text)

    styled = df.style.apply(highlight_companies, subset=['company'])

    styled = styled.format({
        'description': lambda x: truncate(x, 100),
        'content': lambda x: truncate(x, 200),
        'publishedAt': lambda x: x.strftime('%b %-d %Y, %-I%p').lower() if pd.notna(x) else ''
    })

    return styled


# Apply styling
display_columns = ['title', 'company', 'url', 'source_name', 'publishedAt', 'description', 'content']
styled_df = style_dataframe(filtered_df[display_columns])

# Display the styled dataframe with custom column labels and LinkColumn for URL
st.dataframe(
    styled_df,
    column_config={
        "title": st.column_config.Column("Title", width="medium"),
        "company": st.column_config.Column("Company", width="small"),
        "url": st.column_config.LinkColumn("URL", width="small"),
        "source_name": st.column_config.Column("Source", width="small"),
        "publishedAt": st.column_config.Column("Published At", width="medium"),
        "description": st.column_config.Column("Description", width="large"),
        "content": st.column_config.Column("Content", width="large")
    },
    height=600,
    use_container_width=True,
    hide_index=True
)

# Add information about sorting and filtering
st.info(
    'Click on column headers to sort the table. Use the sidebar to filter the news. Click on the URLs in the URL column to open the articles.')
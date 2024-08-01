import pandas as pd
from mock_data import data
from datetime import datetime
import json

def get_mock_data(company_name, start_date, end_date, keywords):
    # Ensure start_date and end_date are datetime objects. Needed to add this to fix a comparison error
    start = start_date if isinstance(start_date, datetime) else datetime.combine(start_date, datetime.min.time())
    end = end_date if isinstance(end_date, datetime) else datetime.combine(end_date, datetime.max.time())

    df = data.get(company_name.lower(), pd.DataFrame(columns=['title', 'description', 'url', 'publishedAt']))

    df['publishedAt'] = pd.to_datetime(df['publishedAt'], format="%Y-%m-%dT%H:%M:%SZ", errors='coerce')

    # Filter date
    mask = (df['publishedAt'] >= start) & (df['publishedAt'] <= end)
    filtered_df = df.loc[mask].copy()  # Create an explicit copy

    # Filter  keywords
    if keywords:
        keyword_mask = filtered_df.apply(lambda row: any(
            (keyword['keyword'] if isinstance(keyword, dict) else keyword).lower() in str(row['title']).lower() or
            (keyword['keyword'] if isinstance(keyword, dict) else keyword).lower() in str(row['description']).lower()
            for keyword in keywords
        ), axis=1)
        filtered_df = filtered_df[keyword_mask]

    # filtered_df.loc[:, 'title'] = filtered_df['title'].fillna('')
    # filtered_df.loc[:, 'description'] = filtered_df['description'].fillna('')

    return filtered_df



def get_all_companies_data(start_date, end_date):
    start = start_date if isinstance(start_date, datetime) else datetime.combine(start_date, datetime.min.time())
    end = end_date if isinstance(end_date, datetime) else datetime.combine(end_date, datetime.max.time())

    all_data = []
    for company_name, company_df in data.items():
        company_df['publishedAt'] = pd.to_datetime(company_df['publishedAt'], format="%Y-%m-%dT%H:%M:%SZ",
                                                   errors='coerce')

        mask = (company_df['publishedAt'] >= start) & (company_df['publishedAt'] <= end)
        filtered_df = company_df.loc[mask]

        filtered_df = filtered_df.copy()
        filtered_df['company'] = company_name.title() #inish cap

        all_data.append(filtered_df)

    combined_df = pd.concat(all_data, ignore_index=True)
    combined_df = combined_df.sort_values(by='publishedAt', ascending=False)

    return combined_df


def is_new_article(article, existing_articles):
    article_titles = set([article['title'].lower()])
    if 'duplicates' in article:
        article_titles.update(dup['title'].lower() for dup in article['duplicates'])

    for existing in existing_articles:
        existing_titles = set([existing['title'].lower()])
        existing_duplicates = json.loads(existing.get('duplicates', '[]'))
        existing_titles.update(dup['title'].lower() for dup in existing_duplicates)

        if article_titles.intersection(existing_titles):
            return False
    return True
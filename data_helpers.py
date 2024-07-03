import pandas as pd
from mock_data import data


def get_mock_data(company_name, start_date, end_date):
    # Your existing mock data setup...

    # Get the data for the requested company
    df = data.get(company_name.lower(), pd.DataFrame(columns=['title','description','url','publishedAt']))

    # Convert 'publishedAt' to datetime with explicit format
    df['publishedAt'] = pd.to_datetime(df['publishedAt'], format="%Y-%m-%dT%H:%M:%SZ", errors='coerce')

    # Filter by date
    mask = (df['publishedAt'].dt.date >= start_date) & (df['publishedAt'].dt.date <= end_date)
    filtered_df = df.loc[mask]

    return filtered_df

import pandas as pd
from mock_data import data
from datetime import datetime, date


def get_mock_data(company_name, start_date, end_date):
    # Ensure start_date and end_date are datetime objects. Needed to add this to fix a comparison error
    start = start_date if isinstance(start_date, datetime) else datetime.combine(start_date, datetime.min.time())
    end = end_date if isinstance(end_date, datetime) else datetime.combine(end_date, datetime.max.time())

    df = data.get(company_name.lower(), pd.DataFrame(columns=['title','description','url','publishedAt']))

    # convert 'publishedAt' to datetime with explicit format
    df['publishedAt'] = pd.to_datetime(df['publishedAt'], format="%Y-%m-%dT%H:%M:%SZ", errors='coerce')

    # Filter by date
    mask = (df['publishedAt'] >= start) & (df['publishedAt'] <= end) # this is a boolean series
    filtered_df = df.loc[mask] # using the boolean mask to select rows from the DataFrame

    return filtered_df

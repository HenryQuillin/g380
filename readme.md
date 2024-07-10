# News Alert Tool

This application is a news alert tool that allows users to monitor news for specific companies and receive notifications based on keyword filters.


## Setup
1. Clone the SCA repository
2. Navigate to the News Alerts Tool directory: ```cd Projects/NewsAlertsTool ```

3. Create a virtual environment (optional): ```python -m venv venv```
4. Activate the virtual environment:
  ```
  venv\Scripts\activate
  ```
  ```
  source venv/bin/activate
  ```

5. Install the required packages:
```pip install -r requirements.txt```

## Running the Application

1. Ensure you're in the NewsAlertsTool directory and your virtual environment is activated.

2. Run the Streamlit app: `streamlit run settings.py`

3. Open a web browser and go to `http://localhost:8501` to view the application.

## Using the News Alerts Tool

1. **Settings**: Add companies you want to track and edit keywords for each company

2. **News Log**: Fetch and view news.

## Mock Data 

- The mock data includes pre-defined news articles for three companies:
   - Microsoft
   - Figma
   - Robinhood
- Currently, you can only add these three companies to the watchlist.
- The get_mock_data() function in `mock_data.py` simulates fetching news articles for these companies.


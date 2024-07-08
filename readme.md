# News Alert Tool

This application is a news alert tool that allows users to monitor news for specific companies and receive notifications based on keyword filters.


## Setup
1. Clone the SCA repository
2. Navigate to the News Alerts Tool directory: ```cd Projects/NewsAlertsTool ```

3. Create a virtual environment (optional): ```python -m venv venv```
4. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

5. Install the required packages:
```pip install -r requirements.txt```

## Running the Application

1. Ensure you're in the NewsAlertsTool directory and your virtual environment is activated.

2. Run the Streamlit app: `streamlit run watchlist.py`

3. Open a web browser and go to `http://localhost:8501` to view the application.

## Using the News Alerts Tool

1. **Watchlist**: Add companies you want to track on the main page.

2. **Keywords**: Navigate to the keywords page to add and edit keywords for each company.

3. **News Log**: Go to the News page to fetch and view news.

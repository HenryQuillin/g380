# NewsNudge 



This application is a news alert tool that allows users to monitor news for specific companies and receive notifications based on keyword filters.


## Setup
1. Clone the SCA repository
2. Navigate to the News Alerts Tool directory: ```cd Projects/NewsAlertsTool ```

3. Create a virtual environment (optional): ```python -m venv venv```
4. Activate the virtual environment:
  ```
  venv\Scripts\activate
  ```

5. Install the required packages:
```pip install -r requirements.txt```

## Running the Application

1. Ensure you're in the NewsAlertsTool directory and your virtual environment is activated.

2. Run the Streamlit app: `streamlit run settings.py`

3. Open a web browser and go to `http://localhost:8501` to view the application.

## Usage

1. **Settings**: Add companies you want to track and edit keywords for each company

2. **My Alerts**: Fetch and view news

3**All News**: Browse news for all companies in the mock data  

## Mock Data 

- The mock data includes news for six companies:
   - Microsoft
   - Figma
   - Robinhood
   - Bank of America 
   - Anthropic
   - Neuralink
- Currently, you can only add these three companies to the watchlist.
- The get_mock_data() function in `mock_data.py` simulates fetching news articles for these companies.

# Project Wiki 


## Duplicate detection



- Computing similarity (compute_similarity function):
    - Uses TF-IDF (see section below for an explanation) vectorization to convert texts into numerical vectors.
        - TF-IDF measures the importance of words in each text relative to all the titles and descriptions.
    - Cosine similarity is then computed between all pairs of these vectors.
    - The result is a 2d array where each element [i, j] represents the similarity between text i and text j.
- Duplicate Detection (detect_duplicates function):
    - Takes a list of articles as input.
    - extracts titles and descriptions from these articles.
    - Similarity matrices are computed separately for titles and descriptions using the compute_similarity function.
    - Two thresholds: 0.5 for titles and 0.8 for descriptions.
    - For each article:
        - It finds indices of articles with similar titles (similarity > 0.5) and indices of articles with similar descriptions (similarity > 0.8) and then combines them
    - If an article has any similar articles (other than itself), it's added to the duplicates dictionary.
  - Grouping Articles 
      - The code then iterates through all articles again.
      - For each article not yet processed:
          - If it has duplicates:
              - The article is made as the "primary" article.
              - Information about each duplicate is added to a 'duplicates' list in this primary article.
              - The primary article (and its duplicates) is added to grouped_articles.
              - All duplicates are marked as processed to avoid processing them again later.
          - If it has no duplicates, it's added to grouped_articles as is.

The final output is a list of grouped articles, where each group consists of a primary article and its duplicates (could be none). The duplicates are then included in a dropdown list in the news cards.

### TF-IDF
TF-IDF (Term Frequency-Inverse Document Frequency) gives the importance of a word in a text within a collection of texts.

Term Frequency:
This measures how frequently a word appears in an article.
The more times a word appears in the article, the higher its TF.


Inverse Document Frequency:
This measures how important a term is across all articles. It's calculated by dividing the total number of articles by the number of articles containing the term, and then taking the logarithm of that quotient.
So words that appear in many documents ("the", "a", "an, etc) will have a low IDF, while rarer words will have a high IDF.


TF-IDF: This is the product of TF and IDF for each term. It gives a high wieght to terms that appear more in a particular article but rarely in other articles.

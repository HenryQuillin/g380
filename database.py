import sqlite3
from datetime import datetime

def get_db_connection():
    conn = sqlite3.connect('company_watchlist.db')
    conn.row_factory = sqlite3.Row
    return conn

# setting up the DB tables
def init_db():
    with get_db_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS companies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            );
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS keywords (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                company_id INTEGER,
                keyword TEXT NOT NULL,
                FOREIGN KEY (company_id) REFERENCES companies (id)
            );
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS articles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                url TEXT NOT NULL,
                publishedAt TEXT NOT NULL,
                company TEXT NOT NULL,
                source_name TEXT NOT NULL,
                duplicates TEXT
            );
        ''')
        conn.commit()

def add_company_to_db(company_name):
    with get_db_connection() as conn:
        conn.execute('INSERT INTO companies (name) VALUES (?)', (company_name,))
        conn.commit()

def get_all_companies():
    with get_db_connection() as conn:
        companies = conn.execute('SELECT * FROM companies').fetchall()
        return companies

def get_company_keywords(company_id):
    with get_db_connection() as conn:
        keywords = conn.execute('SELECT * FROM keywords WHERE company_id = ?', (company_id,)).fetchall()
        return [dict(keyword) for keyword in keywords]

def remove_company_from_db(company_id):
    with get_db_connection() as conn:
        conn.execute('DELETE FROM companies WHERE id = ?', (company_id,))
        conn.execute('DELETE FROM keywords WHERE company_id = ?', (company_id,))
        conn.commit()

def add_keyword_to_db(company_id, keyword):
    with get_db_connection() as conn:
        conn.execute('INSERT INTO keywords (company_id, keyword) VALUES (?, ?)', (company_id, keyword))
        conn.commit()

def remove_keyword_from_db(keyword_id):
    with get_db_connection() as conn:
        conn.execute('DELETE FROM keywords WHERE id = ?', (keyword_id,))
        conn.commit()

def add_article_to_db(article):
    with get_db_connection() as conn:
        published_at = article['publishedAt']
        if not isinstance(published_at, str):
            published_at = published_at.strftime("%Y-%m-%dT%H:%M:%SZ")

        #  source might be a string or obj
        source_name = article['source']['name'] if isinstance(article['source'], dict) else article['source']

        conn.execute('''
            INSERT INTO articles (title, description, url, publishedAt, company, source_name, duplicates)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            article['title'],
            article.get('description', ''),
            article['url'],
            published_at,
            article['company'],
            source_name,
            article.get('duplicates', '[]')
        ))
        conn.commit()

def get_all_articles():
    with get_db_connection() as conn:
        articles = conn.execute('SELECT * FROM articles ORDER BY publishedAt DESC').fetchall()
        return [dict(article) for article in articles]

def clear_article_log():
    with get_db_connection() as conn:
        conn.execute('DELETE FROM articles')
        conn.commit()

def article_exists(url):
    with get_db_connection() as conn:
        result = conn.execute('SELECT 1 FROM articles WHERE url = ?', (url,)).fetchone()
        return result is not None
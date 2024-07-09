import sqlite3

def get_db_connection():
    conn = sqlite3.connect('company_watchlist.db')
    conn.row_factory = sqlite3.Row
    return conn

# setting up the DB tables
# Note that currently the actual news articles are not stored in the DB, they're stored in watchlist.py/
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

def get_company_keywords(company_id):
    with get_db_connection() as conn:
        keywords = conn.execute('SELECT * FROM keywords WHERE company_id = ?', (company_id,)).fetchall()
        return [dict(keyword) for keyword in keywords]

def remove_keyword_from_db(keyword_id):
    with get_db_connection() as conn:
        conn.execute('DELETE FROM keywords WHERE id = ?', (keyword_id,))
        conn.commit()
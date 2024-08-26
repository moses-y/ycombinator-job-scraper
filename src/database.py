import sqlite3
from contextlib import contextmanager

DATABASE_NAME = 'jobs.db'

@contextmanager
def get_db_connection():
  conn = sqlite3.connect(DATABASE_NAME)
  try:
      yield conn
  finally:
      conn.close()

def init_db():
  with get_db_connection() as conn:
      cursor = conn.cursor()
      cursor.execute('''
          CREATE TABLE IF NOT EXISTS jobs (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              title TEXT,
              company TEXT,
              location TEXT,
              url TEXT UNIQUE,
              created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
          )
      ''')
      conn.commit()

def insert_job(job):
  with get_db_connection() as conn:
      cursor = conn.cursor()
      cursor.execute('''
          INSERT OR IGNORE INTO jobs (title, company, location, url)
          VALUES (?, ?, ?, ?)
      ''', (job['title'], job['company'], job['location'], job['url']))
      conn.commit()
      return cursor.rowcount > 0

def get_existing_job_urls():
  with get_db_connection() as conn:
      cursor = conn.cursor()
      cursor.execute('SELECT url FROM jobs')
      return set(row[0] for row in cursor.fetchall())
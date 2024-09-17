import os
from dotenv import load_dotenv
import requests
import mysql.connector

# Load environment variables from .env file
load_dotenv()

# Google Books API key
api_key = os.getenv('GOOGLE_API_KEY')

# Setting up MySQL connection
db = mysql.connector.connect(
    host=os.getenv('MYSQL_HOST'),
    port=int(os.getenv('MYSQL_PORT')),
    user=os.getenv('MYSQL_USER'),
    password=os.getenv('MYSQL_PASSWORD'),
    database=os.getenv('MYSQL_DATABASE')
)

cursor = db.cursor()

# Check if the book exists in the database
def book_exists(title):
    sql = 'SELECT * FROM books WHERE title = %s'
    cursor.execute(sql, (title,))
    result = cursor.fetchone()
    return result is not None

# Insert book into the database
def insert_into_database(title, authors, category, publish_date):
    sql = 'INSERT INTO books (title, authors, category, publish_date) VALUES (%s, %s, %s, %s)'
    cursor.execute(sql, (title, ', '.join(authors), category, publish_date))
    db.commit()

# Search book title
def search_book(book_title):
    query = book_title

    # URL to access Google Books API
    url = f'https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}'

    # Making a GET request to the API
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if data['totalItems'] > 0:
            for item in data['items']:
                title = item['volumeInfo'].get('title', 'N/A')
                authors = item['volumeInfo'].get('authors', ['N/A'])
                category = item['volumeInfo'].get('categories', ['N/A'])[0]  # Use the first category if available
                publish_date = item['volumeInfo'].get('publishedDate', 'N/A')

                # Check if the book is already in the database before inserting
                if not book_exists(title):
                    # Insert book into the database
                    insert_into_database(title, authors, category, publish_date)
    else:
        print(f'Error: {response.status_code}')

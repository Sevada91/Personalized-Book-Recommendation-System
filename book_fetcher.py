import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

# Google Books API key
api_key = os.getenv('GOOGLE_API_KEY')

books_lists = []    # new line

# Search book title
def search_book(book_title):
    query = book_title

    # URL to access Google Books API
    url = f'https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}&maxResults=30'

    # Making a GET request to the API
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if data['totalItems'] > 0:
            for item in data['items']:
                title = item['volumeInfo'].get('title', 'N/A')
                authors = item['volumeInfo'].get('authors', ['N/A'])[0]
                category = item['volumeInfo'].get('categories', ['N/A'])[0]  # Use the first category if available
                publish_date = item['volumeInfo'].get('publishedDate', 'N/A')

                books_lists.append([title, authors, category, publish_date])  # new line

    else:
        print(f'Error: {response.status_code}')

    return books_lists

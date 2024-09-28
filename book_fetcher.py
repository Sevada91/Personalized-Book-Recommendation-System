import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

# Google Books API key
api_key = os.getenv('GOOGLE_API_KEY')

# Dictionary to store books
books_dict = {}

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

                # Store book details in the dictionary
                books_dict[title] = {
                    'authors': authors,
                    'category': category,
                    'publish_date': publish_date
                }

        # Print books stored in the dictionary
        print_books()

    else:
        print(f'Error: {response.status_code}')

# Function to print books stored in the dictionary
# function can be deleted later
def print_books():
    for title, details in books_dict.items():
        print(f"Title: {title}")
        print(f"Authors: {', '.join(details['authors'])}")
        print(f"Category: {details['category']}")
        print(f"Publish Date: {details['publish_date']}")


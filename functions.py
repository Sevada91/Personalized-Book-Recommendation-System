import sqlite3

# Function to search books by a specific field
def search_books(field, value, book_db):
    '''
    Searches for books in a SQLite database based on a specified field and value.

    Parameters:
    field (str): The column name to search by (e.g., 'title', 'authors', 'category', 'publish_date').
    value (str): The value to search for within the specified field. Partial matches are allowed.
    book_db (str): The path to the SQLite database file containing the 'books' table.

    Returns:
    list of tuples: A list of book entries that match the search criteria.
    Each tuple contains the details of a book (e.g., title, authors, category, publish date).
    '''
    conn = sqlite3.connect(book_db)
    c = conn.cursor()
    query = f"SELECT * FROM books WHERE {field} LIKE ?"
    c.execute(query, ('%' + value + '%',))
    results = c.fetchall()
    return results

# Function to sort by a specific field
def sort_books_by(field, book_db):
    '''
    Sorts books stored in a SQLite database based on a specified field.

    Parameters:
    field (str): The column name to sort the books by (e.g., 'title', 'authors', 'category', 'publish_date').
    book_db (str): The path to the SQLite database file containing the 'books' table.

    Returns:
    list of tuples: A list of book entries sorted by the specified field.
    Each tuple contains the details of a book (e.g., title, authors, category, publish date).
    '''
    conn = sqlite3.connect(book_db)
    c = conn.cursor()  
    query = f"SELECT * FROM books ORDER BY {field}"
    c.execute(query)
    results = c.fetchall()
    return results

# Function to sort by a specific field the return result of book fetcher
def book_fetcher_sort_by(list_of_books, field):
    '''
    Sorts a list of book entries based on a specified column.

    Parameters:
    books (list of lists): A list of book entries returned from the book_fetcher. 
                           Each entry contains details such as title, authors, category, and publish date.
    field (int): An integer representing the column to sort by:
                 0 - title
                 1 - authors
                 2 - category
                 3 - publish_date

    Returns:
    list of lists: The sorted list of book entries based on the specified column.
    '''
    return sorted(list_of_books, key=lambda x: x[field])
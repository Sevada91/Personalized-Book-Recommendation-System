import sqlite3

# Connect to SQLite database (or create it)
conn = sqlite3.connect('books.db')
c = conn.cursor()

# Create a table for storing book information
c.execute('''
CREATE TABLE IF NOT EXISTS books (
    title TEXT,
    author TEXT,
    category TEXT,
    published_date TEXT
)
''')

# Function to add a book to the database
def add_book(title, author, category, published_date):
    c.execute("INSERT INTO books (title, author, category, published_date) VALUES (?, ?, ?, ?)", 
              (title, author, category, published_date))
    conn.commit()

# Function to search books by a specific field
def search_books(field, value):
    query = f"SELECT * FROM books WHERE {field} LIKE ?"
    c.execute(query, ('%' + value + '%',))
    results = c.fetchall()
    return results

# Function to display the results nicely
def display_results(results):
    if results:
        for row in results:
            print(f"Title: {row[0]}, Author: {row[1]}, Category: {row[2]}, Published Date: {row[3]}")
    else:
        print("No results found.")

# Function to sort by a specific field
def sort_books_by(field):
    query = f"SELECT * FROM books ORDER BY {field}"
    c.execute(query)
    results = c.fetchall()
    display_results(results)

# Sample books for testing
sample_books = [
    ("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", "1925"),
    ("To Kill a Mockingbird", "Harper Lee", "Fiction", "1960"),
    ("1984", "George Orwell", "Dystopian", "1949"),
    ("Moby Dick", "Herman Melville", "Fiction", "1851"),
    ("The Catcher in the Rye", "J.D. Salinger", "Fiction", "1951")
]

# Add sample books to the database
for book in sample_books:
    add_book(*book)

# Menu to search or sort books
def menu():
    print("\n--- Book Search & Sorting System ---")
    print("1. Search by Title")
    print("2. Search by Author")
    print("3. Search by Category")
    print("4. Search by Published Date")
    print("5. Sort by Title")
    print("6. Sort by Author")
    print("7. Sort by Category")
    print("8. Sort by Published Date")
    print("9. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        title = input("Enter title to search: ")
        results = search_books('title', title)
        display_results(results)
    elif choice == '2':
        author = input("Enter author to search: ")
        results = search_books('author', author)
        display_results(results)
    elif choice == '3':
        category = input("Enter category to search: ")
        results = search_books('category', category)
        display_results(results)
    elif choice == '4':
        published_date = input("Enter published date to search: ")
        results = search_books('published_date', published_date)
        display_results(results)
    elif choice == '5':
        print("Sorting by Title...")
        sort_books_by('title')
    elif choice == '6':
        print("Sorting by Author...")
        sort_books_by('author')
    elif choice == '7':
        print("Sorting by Category...")
        sort_books_by('category')
    elif choice == '8':
        print("Sorting by Published Date...")
        sort_books_by('published_date')
    elif choice == '9':
        print("Goodbye!")
        conn.close()
        exit()
    else:
        print("Invalid choice! Please try again.")

# Main program loop
if __name__ == "__main__":
    while True:
        menu()
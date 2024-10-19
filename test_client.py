from book_fetcher import search_book

# Example book title to search and insert into the database
book_title = "who moved my cheese"

# Call the search_book function to fetch and insert the book
result = search_book(book_title)

for book in result:
    print(book)

print()

def book_fetcher_sort_by(list_of_books, field):
    return sorted(list_of_books, key=lambda x: x[field])

result = book_fetcher_sort_by(result, 3)

for book in result:
    print(book)
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
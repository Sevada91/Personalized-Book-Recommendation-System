import os
from dotenv import load_dotenv
import requests
import customtkinter as ctk
from tkinter import ttk, StringVar

# Load environment variables from .env file
load_dotenv()

# Google Books API key
api_key = os.getenv('GOOGLE_API_KEY')

# Initialize the CustomTkinter App
ctk.set_appearance_mode("dark")  # Set theme
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()

# Get screen width and height
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

# Set window size to 85% of screen size
window_width = int(screen_width * 0.85)
window_height = int(screen_height * 0.85)
app.geometry(f"{window_width}x{window_height}")

app.title("Personalized Book Recommendation System")

# Configure the grid layout for adaptive resizing
for i in range(9):  # Adjust columns to fit all elements comfortably
    app.grid_columnconfigure(i, weight=1, uniform="column")
app.grid_rowconfigure(1, weight=1)

# Book list variables to store search input
book_title = StringVar()

# Search Entry for Title/Author/Genre
search_label = ctk.CTkLabel(app, text="Title/Author/Genre:")
search_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

search_entry = ctk.CTkEntry(app, width=150, textvariable=book_title)
search_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")


# Search Function
def search_books():
    query = book_title.get()
    books_lists = []

    if not query:
        print("Please enter a search query.")
        return

    # URL to access Google Books API
    url = f'https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}'

    try:
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

                    books_lists.append([title, ", ".join(authors), category, publish_date])

    except Exception as e:
        print(f"Error fetching books: {e}")
        return

    # Clear previous table rows
    for row in book_tree.get_children():
        book_tree.delete(row)

    # Insert new rows into the table
    for book in books_lists:
        book_tree.insert("", "end", values=book)


# Search Button
search_button = ctk.CTkButton(app, text="Search", width=100, command=search_books)
search_button.grid(row=0, column=2, padx=5, pady=5)

# Book Table to display books
book_tree = ttk.Treeview(app, columns=("Title", "Author", "Genre", "Publish Date"), show="headings", height=10)
book_tree.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

# Configure column headings
book_tree.heading("Title", text="Title")
book_tree.heading("Author", text="Author")
book_tree.heading("Genre", text="Genre")
book_tree.heading("Publish Date", text="Publish Date")

# Run the application
app.mainloop()
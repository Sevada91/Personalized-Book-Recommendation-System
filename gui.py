import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

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
book_title = tk.StringVar()
book_author = tk.StringVar()
book_genre = tk.StringVar()
book_publish_date = tk.StringVar()

# Search Entry for Title/Author/Genre
search_label = ctk.CTkLabel(app, text="Title/Author/Genre:")
search_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

search_entry = ctk.CTkEntry(app, width=150, textvariable=book_title)
search_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# Search Button
search_button = ctk.CTkButton(app, text="Search", width=100, command=lambda: search_books())
search_button.grid(row=0, column=2, padx=5, pady=5)

# Book Table to display books
book_tree = ttk.Treeview(app, columns=("Title", "Author", "Genre", "Publish Date"), show="headings", height=4)
book_tree.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

# Defining the column heading buttons with uniform width and smaller font for reduced height
button_font = ("Arial", 9)  
button_width = 100  

title_button = ctk.CTkButton(app, text="Title", font=button_font, width=button_width, command=lambda: title_clicked())
title_button.grid(row=1, column=0, padx=2, pady=5, sticky="n")

author_button = ctk.CTkButton(app, text="Author", font=button_font, width=button_width, command=lambda: author_clicked())
author_button.grid(row=1, column=1, padx=2, pady=5, sticky="n")

genre_button = ctk.CTkButton(app, text="Genre", font=button_font, width=button_width, command=lambda: genre_clicked())
genre_button.grid(row=1, column=2, padx=2, pady=5, sticky="n")

publish_date_button = ctk.CTkButton(app, text="Publish Date", font=button_font, width=button_width, command=lambda: publish_date_clicked())
publish_date_button.grid(row=1, column=3, padx=2, pady=5, sticky="n")

# Add and Clear buttons placed next to the book table
add_book_button = ctk.CTkButton(app, text="Add", font=button_font, width=button_width, command=lambda: add_book())
add_book_button.grid(row=1, column=4, padx=2, pady=5, sticky="n")

clear_button = ctk.CTkButton(app, text="Clear", font=button_font, width=button_width, command=lambda: clear_books())
clear_button.grid(row=1, column=4, padx=2, pady=50, sticky="n")

# Function to search books based on entry input (placeholder)
def search_books():
    # Code here: Searches for books based on title/author/genre input and displays results in the table
    pass

# Function to add a book to the table (placeholder)
def add_book():
    # Code here: Adds a new book with title, author, genre, and publish date to the book table
    pass

# Function to clear all books from the table (placeholder)
def clear_books():
    # Code here: Clears all entries in the book table
    pass

# Button functions (placeholders)
def title_clicked():
    # Code here: Function when Title button is clicked
    pass

def author_clicked():
    # Code here: Function when Author button is clicked
    pass

def genre_clicked():
    # Code here: Function when Genre button is clicked
    pass

def publish_date_clicked():
    # Code here: Function when Publish Date button is clicked
    pass

# Function to open a pop-up window for adding a new user
def open_add_user_window():
    # Code here: Opens a new window to add user information such as name, age, and gender
    add_user_window = ctk.CTkToplevel(app)
    add_user_window.title("Add User")
    add_user_window.geometry("300x250")

    # Variables to store user input
    user_name = tk.StringVar()
    user_age = tk.StringVar()
    user_gender = tk.StringVar()

    # Create input fields in the pop-up window
    name_label = ctk.CTkLabel(add_user_window, text="Name:")
    name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    name_entry = ctk.CTkEntry(add_user_window, width=150, textvariable=user_name)
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    age_label = ctk.CTkLabel(add_user_window, text="Age:")
    age_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    age_entry = ctk.CTkEntry(add_user_window, width=150, textvariable=user_age)
    age_entry.grid(row=1, column=1, padx=10, pady=10)

    gender_label = ctk.CTkLabel(add_user_window, text="Gender:")
    gender_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    gender_dropdown = ctk.CTkComboBox(add_user_window, values=["Male", "Female", "Other"], variable=user_gender)
    gender_dropdown.grid(row=2, column=1, padx=10, pady=10)

    # Add button to submit user data
    submit_button = ctk.CTkButton(add_user_window, text="Add", command=lambda: add_user())
    submit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

    # Function to handle adding the user (placeholder)
    def add_user():
        # Code here: Processes and stores user input, then closes the add user window
        add_user_window.destroy()

# Button to open the Add User window
add_user_button = ctk.CTkButton(app, text="Add User", width=button_width, command=open_add_user_window)
add_user_button.grid(row=0, column=5, padx=5, pady=5)

# Dropdown to select different users (placeholder for functionality)
user_dropdown = ctk.CTkComboBox(app, values=["User1", "User2"], width=150)
user_dropdown.grid(row=0, column=6, padx=5, pady=5)

# Remove User button (placeholder for functionality)
remove_user_button = ctk.CTkButton(app, text="Remove User", width=button_width, command=lambda: remove_user())
remove_user_button.grid(row=0, column=7, padx=5, pady=5)

# Function to remove the selected user from the dropdown (placeholder)
def remove_user():
    # Code here: Removes the currently selected user from the user list
    pass

# User-specific book table (empty functionality for now)
user_tree = ttk.Treeview(app, columns=("Title", "Author", "Genre", "Publish Date"), show="headings", height=4)
user_tree.grid(row=1, column=5, columnspan=4, padx=5, pady=5, sticky="nsew")

# Defining column heading buttons for the user table with uniform width
user_title_button = ctk.CTkButton(app, text="Title", font=button_font, width=button_width, command=lambda: title_clicked())
user_title_button.grid(row=1, column=5, padx=2, pady=5, sticky="n")

user_author_button = ctk.CTkButton(app, text="Author", font=button_font, width=button_width, command=lambda: author_clicked())
user_author_button.grid(row=1, column=6, padx=2, pady=5, sticky="n")

user_genre_button = ctk.CTkButton(app, text="Genre", font=button_font, width=button_width, command=lambda: genre_clicked())
user_genre_button.grid(row=1, column=7, padx=2, pady=5, sticky="n")

user_publish_date_button = ctk.CTkButton(app, text="Publish Date", font=button_font, width=button_width, command=lambda: publish_date_clicked())
user_publish_date_button.grid(row=1, column=8, padx=2, pady=5, sticky="n")

# Run the application
app.mainloop()

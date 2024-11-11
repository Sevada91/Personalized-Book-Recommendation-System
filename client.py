import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from db_functions import *
from functions import *
import os

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

# Export button in the top right corner
export_button = ctk.CTkButton(app, text="Export", width=button_width, command=lambda: export_data())
export_button.grid(row=0, column=8, padx=5, pady=5)

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

# Function to export data (placeholder)
def export_data():
    # Code here: Exports data to a file
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

# SEVADA WORKING HERE___________________________________________________________________________________________________________

# Initialize an empty set and list for storing database files
user_database = set()
data_base_hidden_folder = ".databases"

if not os.path.isdir(data_base_hidden_folder):
    # If the folder doesn't exist, mark it as "Empty"
    user_database.add("Empty")
else:
    # If the folder exists, list all .db files and add them to the set and list
    for databaese in os.listdir(data_base_hidden_folder):
        if databaese.endswith(".db"):
            user_database.add(databaese)
    if not user_database:
        user_database.add("Empty")


# Function to open a pop-up window for adding a new user
add_user_window = None  # Global variable to track the window

def open_add_user_window():
    global add_user_window
    if add_user_window is None or not add_user_window.winfo_exists():  # Check if window exists
        add_user_window = ctk.CTkToplevel(app)
        add_user_window.title("Add User")
        add_user_window.geometry("300x250")

        # Variables to store user input
        user_name = tk.StringVar()

        # Create input fields in the pop-up window
        name_label = ctk.CTkLabel(add_user_window, text="Username:")
        name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        name_entry = ctk.CTkEntry(add_user_window, width=150, textvariable=user_name)
        name_entry.grid(row=0, column=1, padx=10, pady=10)

        # REMOVED THE GENDER AND AGE BOXES FROM HERE ___________________________SEVADA

        # Add button to submit user data
        submit_button = ctk.CTkButton(add_user_window, text="Add", command=lambda: add_user(user_name))
        submit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

# Button to open the Add User window
add_user_button = ctk.CTkButton(app, text="Add User", width=button_width, command=open_add_user_window)
add_user_button.grid(row=0, column=5, padx=5, pady=5)

selected_option = None
selected_item = None

if user_database:
    selected_option = next(iter(user_database))

# Function to trigger an action when an option is selected in a pull-down
def on_option_selected(event):
    global selected_option, selected_item
    selected_option = user_dropdown.get()
    fetch_and_display_user_data()
    selected_item = None
    
# Dropdown to select different users (placeholder for functionality)
user_dropdown = ctk.CTkComboBox(app, values=list(user_database), width=150, command=on_option_selected)
user_dropdown.grid(row=0, column=6, padx=5, pady=5)

# Function to handle adding the user (placeholder)
def add_user(user_name):
    if user_name.get():
        if "Empty" in user_database:
            user_database.remove("Empty")
        new_database = User(user_name.get())
        user_database.add(new_database.return_db())
        user_dropdown.configure(values=list(user_database))
    add_user_window.destroy()

# Remove User button (placeholder for functionality)
remove_user_button = ctk.CTkButton(app, text="Remove User", width=button_width, command=lambda: remove_user())
remove_user_button.grid(row=0, column=7, padx=5, pady=5)

# User-specific book table (shorter height)
user_tree = ttk.Treeview(app, columns=("Title", "Author", "Genre", "Publish Date"), show="headings", height=3)
user_tree.grid(row=1, column=5, columnspan=4, padx=5, pady=5, sticky="nsew")


# Function to remove the selected user from the dropdown (placeholder)
def remove_user():
    global selected_item
    if selected_option and selected_option in user_database:
        user_database.remove(selected_option)
        file_path = os.path.join(".databases", selected_option)
        os.remove(file_path)
        if not user_database:
            user_database.add("Empty")
        user_dropdown.configure(values=list(user_database))
        user_tree.delete(*user_tree.get_children())
        selected_item = None
        

# Configuration for column widths for db print
user_tree.column("Title", width=150, anchor="w")       
user_tree.column("Author", width=150, anchor="w")      
user_tree.column("Genre", width=100, anchor="w")       
user_tree.column("Publish Date", width=100, anchor="w")

# SEVADA WORKING HERE______________________________________________________________________________________________________

# Defining column heading buttons for the user table with uniform width
user_title_button = ctk.CTkButton(app, text="Title", font=button_font, width=button_width, command=lambda: title_clicked())
user_title_button.grid(row=1, column=5, padx=2, pady=5, sticky="n")

user_author_button = ctk.CTkButton(app, text="Author", font=button_font, width=button_width, command=lambda: author_clicked())
user_author_button.grid(row=1, column=6, padx=2, pady=5, sticky="n")

user_genre_button = ctk.CTkButton(app, text="Genre", font=button_font, width=button_width, command=lambda: genre_clicked())
user_genre_button.grid(row=1, column=7, padx=2, pady=5, sticky="n")

user_publish_date_button = ctk.CTkButton(app, text="Publish Date", font=button_font, width=button_width, command=lambda: publish_date_clicked())
user_publish_date_button.grid(row=1, column=8, padx=2, pady=5, sticky="n")

# Book Generator button below the user table
book_generator_button = ctk.CTkButton(app, text="Book Generator", font=("Arial", 11), width=int(window_width * 0.25), command=lambda: generate_books())
book_generator_button.grid(row=2, column=5, columnspan=4, padx=5, pady=10)

# SEVADA WORKING HERE______________________________________________________________________________________________________

# Function to fetch and display data in user_tree
def fetch_and_display_user_data():
    # Clear the Treeview before loading new data
    user_tree.delete(*user_tree.get_children())

    # Connect to the selected database and fetch data
    if selected_option and selected_option != "Empty":
        conn = sqlite3.connect(os.path.join(data_base_hidden_folder, selected_option))
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT Title, Author, Genre, Publish_Date FROM books")
            rows = cursor.fetchall()
            for row in rows:
                user_tree.insert("", "end", values=row)
        except sqlite3.Error as e:
            print(f"Error loading data: {e}")
        finally:
            conn.close()

# Handle row selection in user_tree
def on_user_row_selected(event):
    selected_item = user_tree.selection()
    if selected_item:
        item_data = user_tree.item(selected_item)["values"]
        print(f"Selected item: {item_data}")

user_tree.bind("<<TreeviewSelect>>", on_user_row_selected)

# SEVADA WORKING HERE______________________________________________________________________________________________________

# Function to generate books (placeholder)
def generate_books():
    # Code here: Generates book data and updates the user book table
    pass

# Run the application
app.mainloop()

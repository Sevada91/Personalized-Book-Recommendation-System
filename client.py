import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from db_functions import *
from functions import *
from book_fetcher import *
import json
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
search_button = ctk.CTkButton(app, text="Search", width=100, command=lambda: search_books(search_entry.get()))
search_button.grid(row=0, column=2, padx=5, pady=5)

# Book Table (Left Side) - book_tree
book_tree = ttk.Treeview(app, columns=("Title", "Author", "Genre", "Publish Date"), show="headings", height=4)
book_tree.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

# Configure columns for book_tree to fill the space evenly
for col in ("Title", "Author", "Genre", "Publish Date"):
    book_tree.column(col, anchor="w", stretch=True, width=150)


# Defining the column heading buttons with uniform width and smaller font for reduced height
button_font = ("Arial", 9)
button_width = 100

title_button = ctk.CTkButton(app, text="Title", font=button_font, width=button_width, command=lambda: title_clicked_data())
title_button.grid(row=1, column=0, padx=2, pady=5, sticky="n")

author_button = ctk.CTkButton(app, text="Author", font=button_font, width=button_width, command=lambda: author_clicked_data())
author_button.grid(row=1, column=1, padx=2, pady=5, sticky="n")

genre_button = ctk.CTkButton(app, text="Genre", font=button_font, width=button_width, command=lambda: genre_clicked_data())
genre_button.grid(row=1, column=2, padx=2, pady=5, sticky="n")

publish_date_button = ctk.CTkButton(app, text="Publish Date", font=button_font, width=button_width, command=lambda: publish_date_clicked_data())
publish_date_button.grid(row=1, column=3, padx=2, pady=5, sticky="n")

# Add and Clear buttons placed next to the book table
add_book_button = ctk.CTkButton(app, text="Add", font=button_font, width=button_width, command=lambda: add_book_info())
add_book_button.grid(row=1, column=4, padx=2, pady=5, sticky="n")

clear_button = ctk.CTkButton(app, text="Clear", font=button_font, width=button_width, command=lambda: clear_books())
clear_button.grid(row=1, column=4, padx=2, pady=50, sticky="n")

# Export button in the top right corner
export_button = ctk.CTkButton(app, text="Export", width=button_width, command=lambda: export_data())
export_button.grid(row=0, column=8, padx=5, pady=5)


BOOK_RESULT = []

# Function to search books based on entry input (placeholder)
def search_books(title):
    global BOOK_RESULT
    BOOK_RESULT.clear()
    BOOK_RESULT = search_book(title)
    
    if BOOK_RESULT:
        show_result()

# Function to show result of the book search
def show_result():
    clear_books()

    for book in BOOK_RESULT:
        book_tree.insert("", "end", values=book)

def load_user_from_json(selected_option, filename=".users.json"):
    try:
        # Load JSON data from the file
        with open(filename, "r") as file:
            data = json.load(file)

        # Find the dictionary with the matching name
        user_data = next((entry for entry in data if entry.get("name") == selected_option), None)

        if user_data:
            # Recreate the User instance using from_dict
            return User.from_dict(user_data)
        else:
            print(f"No user found with name: {selected_option}")
            return None

    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file {filename}.")
        return None


# Function to add a book to the table (placeholder)
def add_book_info():
    global selected_option
    new_book = selected_book_from_search()
    if selected_option and new_book:
        db_class = load_user_from_json(selected_option[:-3], filename=".users.json")
        if db_class:
            db_class.add_book(new_book)
            fetch_and_display_user_data()
    elif not selected_option and not new_book:
        messagebox.showerror(message="Error\nNo database and no book selected. Please select both before adding.")
    elif not selected_option:
        messagebox.showerror(message="Error\nNo database selected. Please select database before adding.")
    elif not new_book:
        messagebox.showerror(message="Error\nNo book selected. Please select book before adding.")

# Function to clear all books from the table (placeholder)
def clear_books():
    for item in book_tree.get_children():
        book_tree.delete(item)

# Function to export data (placeholder)
def export_data():
    pass

# Right-side Button functions (placeholders)
def title_clicked_data():
    global BOOK_RESULT
    BOOK_RESULT = book_fetcher_sort_by(BOOK_RESULT, 0)
    show_result()

def author_clicked_data():
    global BOOK_RESULT
    BOOK_RESULT = book_fetcher_sort_by(BOOK_RESULT, 1)
    show_result()

def genre_clicked_data():
    global BOOK_RESULT
    BOOK_RESULT = book_fetcher_sort_by(BOOK_RESULT, 2)
    show_result()

def publish_date_clicked_data():
    global BOOK_RESULT
    BOOK_RESULT = book_fetcher_sort_by(BOOK_RESULT, 3)
    show_result()


def selected_book_from_search():
    selected_item = book_tree.selection()
    if selected_item:
        row_values = book_tree.item(selected_item[0], 'values')
        return list(row_values)


# Left-side Button functions (placeholders)
def title_clicked_user():
    # Code here: Function when Title button is clicked
    pass

def author_clicked_user():
    # Code here: Function when Author button is clicked
    pass

def genre_clicked_user():
    # Code here: Function when Genre button is clicked
    pass

def publish_date_clicked_user():
    # Code here: Function when Publish Date button is clicked
    pass

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

# Function to open the Add User window
def open_add_user_window():
    global add_user_window
    if add_user_window is None or not add_user_window.winfo_exists():  # Check if window exists
        add_user_window = ctk.CTkToplevel(app)
        add_user_window.title("Add User")
        add_user_window.geometry("300x250")

        # Variables to store user input
        user_name = tk.StringVar()

        # Create input fields in the pop-up window with validation for max length 6
        name_label = ctk.CTkLabel(add_user_window, text="Username:")
        name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        # Create a username entry with validation for max length 6
        name_entry = ctk.CTkEntry(
            add_user_window, 
            width=150, 
            textvariable=user_name, 
            validate="key", 
            validatecommand=(add_user_window.register(validate_username_length), "%P")
        )
        name_entry.grid(row=0, column=1, padx=10, pady=10)

        # Add button to submit user data
        submit_button = ctk.CTkButton(add_user_window, text="Add", command=lambda: add_user(user_name))
        submit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

        # Bind "Enter" key to trigger add_user when pressed
        add_user_window.bind("<Return>", lambda event: add_user(user_name))

# Function to limit the username to 6 characters
def validate_username_length(new_value):
    if len(new_value) > 6:
        return False  # prevents the user from typing more than 6 characters
    return True  # Allow the input if the length is 6 or fewer

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
user_dropdown = ctk.CTkComboBox(app, values=list(user_database), width=150, command=on_option_selected, state="readonly") # Not-editable
user_dropdown.grid(row=0, column=6, padx=5, pady=5)


def load_users_from_json(filename=".users.json"):
    try:
        with open(filename, "r") as file:
            user_data = json.load(file)
            return [User.from_dict(data) for data in user_data]
    except FileNotFoundError:
        print(f"{filename} not found. Returning an empty list.")
        return []

# Function to save User objects to a JSON file
def save_users_to_json(users, filename=".users.json"):
    with open(filename, "w") as file:
        json.dump([user.to_dict() for user in users], file)
    print(f"Users saved to {filename}")

# Function to open a JSON file and remove a specific user by name
def remove_user_from_json(name, filename=".users.json"):
    try:
        # Load JSON data from the file
        with open(filename, "r") as file:
            data = json.load(file)

        # Ensure the data is a list
        if not isinstance(data, list):
            raise ValueError("JSON data must be a list of dictionaries.")

        # Filter out the user to remove
        original_length = len(data)
        data = [entry for entry in data if entry.get("name") != name]

        # Check if a user was removed
        if len(data) == original_length:
            print(f"No user found with name: {name}")
            return False

        # Save the updated data back to the file
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"User with name '{name}' removed successfully.")
        return True

    except FileNotFoundError:
        print(f"File {filename} not found.")
        return False
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file {filename}.")
        return False


users = load_users_from_json()

# Function to handle adding the user (placeholder)
def add_user(user_name):
    if user_name.get():
        if "Empty" in user_database:
            user_database.remove("Empty")

        if user_name.get()+'.db' in user_database:
            messagebox.showerror(message=f"Error!\nUsername {user_name.get()} already exists.")
        else:
            new_database = User(user_name.get().strip())
            user_database.add(new_database.return_db())
            user_dropdown.configure(values=list(user_database))
            users.append(new_database)  # Add the new User to the list
            save_users_to_json(users)  # Save the updated list to the file
    add_user_window.destroy()

# Remove User button (placeholder for functionality)
remove_user_button = ctk.CTkButton(
    app,
    text="Remove User",
    width=button_width,
    command=lambda: (
        remove_user() if messagebox.askyesno("Confirmation", "Are you sure you want to delete this user?") else None
    )
)
remove_user_button.grid(row=0, column=7, padx=5, pady=5)

# User-specific book table (Right Side) - user_tree
user_tree = ttk.Treeview(app, columns=("Title", "Author", "Genre", "Publish Date"), show="headings", height=4)
user_tree.grid(row=1, column=5, columnspan=4, padx=5, pady=5, sticky="nsew")

# Configure columns for user_tree to fill the space evenly
for col in ("Title", "Author", "Genre", "Publish Date"):
    user_tree.column(col, anchor="w", stretch=True, width=150)

# Function to toggle selection when clicking inside the Treeview
def toggle_selection(event):
    selected_item = event.widget.selection()
    if selected_item:
        event.widget.selection_remove(selected_item)  # Deselect if already selected
    else:
        event.widget.selection_add(event.widget.identify_row(event.y))  # Select if not selected

# Function to cancel the selection when clicking anywhere else
def cancel_selection(event):
    # Deselects in both book_tree and user_tree
    book_tree.selection_remove(book_tree.selection())
    user_tree.selection_remove(user_tree.selection())

# Bind the cancel selection event to the entire window (app)
app.bind("<Button-1>", cancel_selection)

# Bind toggle selection to both book_tree and user_tree (inside the tables)
book_tree.bind("<ButtonRelease-1>", toggle_selection)
user_tree.bind("<ButtonRelease-1>", toggle_selection)

# Bind toggle selection to both book_tree and user_tree (inside the tables)
book_tree.bind("<ButtonRelease-1>", toggle_selection)
user_tree.bind("<ButtonRelease-1>", toggle_selection)

# Function to remove the selected item from the user_tree
def remove_selected_item():
    selected_item = user_tree.selection()  # Get the selected item
    if selected_item:
        # Ask for confirmation before deleting
        confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to remove this item?")
        if confirm:
            user_tree.delete(selected_item)  # Remove from the Treeview
            print(f"Removed item: {selected_item}")
        else:
            print("Item removal cancelled.")
    else:
        print("No item selected to remove")

# Create the "Remove" button for the user side
remove_button = ctk.CTkButton(app, text="Remove", width=button_width, command=remove_selected_item)
remove_button.grid(row=2, column=5, padx=5, pady=5)

# Function to remove the selected user from the dropdown (placeholder)
def remove_user():
    global selected_item
    if selected_option and selected_option in user_database:
        remove_user_from_json(selected_option[:-3], filename=".users.json")
        user_database.remove(selected_option)
        file_path = os.path.join(".databases", selected_option)
        os.remove(file_path)
        if not user_database:
            user_database.add("Empty")
        user_dropdown.configure(values=list(user_database))
        user_tree.delete(*user_tree.get_children())
        selected_item = None

def remove_user_with_confirmation():
    confirm = messagebox.askyesno("Confirmation", "Are you sure you want to delete this user?")
    if confirm:
        remove_user()  # Call the original remove_user function
        
# Defining column heading buttons for the user table with uniform width
user_title_button = ctk.CTkButton(app, text="Title", font=button_font, width=button_width, command=lambda: title_clicked_user())
user_title_button.grid(row=1, column=5, padx=2, pady=5, sticky="n")

user_author_button = ctk.CTkButton(app, text="Author", font=button_font, width=button_width, command=lambda: author_clicked_user())
user_author_button.grid(row=1, column=6, padx=2, pady=5, sticky="n")

user_genre_button = ctk.CTkButton(app, text="Genre", font=button_font, width=button_width, command=lambda: genre_clicked_user())
user_genre_button.grid(row=1, column=7, padx=2, pady=5, sticky="n")

user_publish_date_button = ctk.CTkButton(app, text="Publish Date", font=button_font, width=button_width, command=lambda: publish_date_clicked_user())
user_publish_date_button.grid(row=1, column=8, padx=2, pady=5, sticky="n")



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


def recommend_new_books():
    # Code here: Function to generate a new list of books for recommendation
    pass
def open_book_generator_window():
    book_generator_window = ctk.CTkToplevel(app)  # Create a new pop-up window
    book_generator_window.title("Book Generator Table")
    book_generator_window.geometry("600x400")  # Set the size of the pop-up window

    # Table inside the pop-up window
    generator_table = ttk.Treeview(
        book_generator_window, 
        columns=("Title", "Author", "Genre", "Publish Date"), 
        show="headings", 
        height=15
    )
    generator_table.pack(fill="both", expand=True, padx=10, pady=10)

    # Configure columns for the generator_table
    for col in ("Title", "Author", "Genre", "Publish Date"):
        generator_table.column(col, anchor="w", stretch=True, width=150)
        generator_table.heading(col, text=col)

    # sample data to the table 
    sample_data = [
        ("Sample Title 1", "Sample Author 1", "Sample Genre 1", "2022-01-01"),
        ("Sample Title 2", "Sample Author 2", "Sample Genre 2", "2023-05-15"),
        ("Sample Title 3", "Sample Author 3", "Sample Genre 3", "2024-11-27"),
    ]
    for row in sample_data:
        generator_table.insert("", "end", values=row)

    # Add 'Add' button
    add_button = ctk.CTkButton(
        book_generator_window, 
        text="Add", 
        command=add_selected_item_to_user_table  # Placeholder for future functionality
    )
    add_button.place(relx=0.3, rely=0.9, anchor="center")  # Positioned relative to the window

    # Add 'Recommend' button next to 'Add' button
    recommend_button = ctk.CTkButton(
        book_generator_window, 
        text="Recommend", 
        command=recommend_new_books  # Placeholder for future functionality
    )
    recommend_button.place(relx=0.6, rely=0.9, anchor="center")  # Positioned relative to the window

# Placeholder function for adding selected item to user's table
def add_selected_item_to_user_table():
    # Code here: Function to add the selected item to the user's table
    pass

# Add the Book Generator button to the main window
book_generator_button = ctk.CTkButton(
    app, 
    text="Book Generator", 
    font=("Arial", 11), 
    width=int(window_width * 0.25), 
    command=open_book_generator_window  # Ensure this references the defined function
)
book_generator_button.grid(row=2, column=5, columnspan=4, padx=5, pady=10)

if selected_option:
    user_dropdown.set(selected_option)
    fetch_and_display_user_data()

# Run the application
app.mainloop()

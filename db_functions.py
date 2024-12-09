import sqlite3
import os

class User:
    '''
    Connects to a database by the given name and creates it if it doesn't already exist.
    Automatically commits changes immediately for methods like add_book and remove_book,
    ensuring instant updates in a GUI. Manages switching between multiple User objects
    by closing the previous connection before opening a new one.
    '''
    _active_connection = None  # Class-level variable to track the active connection

    def __init__(self, name):
        # Close any existing connection before creating a new one
        if User._active_connection:
            User._active_connection._close_connection()
            print(f"Closed the previous connection.")

        # Create hidden database folder if it doesn't already exist
        if not os.path.exists(".databases"):
            os.mkdir(".databases")

        self.name = name
        self._connect_to_db()
        self._create_table()
        User._active_connection = self  # Set this instance as the active connection
        print(f"Connected to database: {self.name}.db")

    def _connect_to_db(self):
        """Establishes a connection to the database."""
        self.connection = sqlite3.connect(f'.databases/{self.name}.db')
        self.cursor = self.connection.cursor()

    def _close_connection(self):
        """Closes the connection to the database."""
        if self.connection:
            self.connection.close()
            self.connection = None
            self.cursor = None
            print(f"Closed the connection to database: {self.name}.db")

    def _create_table(self):
        """Ensures the books table exists."""
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Title TEXT NOT NULL,
            Author TEXT NOT NULL,
            Genre TEXT,
            Publish_Date TEXT
        )
        ''')
        self.connection.commit()

    def return_db(self):
        """Returns the database name."""
        return f"{self.name}.db"

    def to_dict(self):
        """Serialize the User instance to a dictionary."""
        return {"name": self.name}

    @staticmethod
    def from_dict(data):
        """Recreate a User instance from a dictionary."""
        return User(data["name"])

    def search_db(self, title):
        """Searches books by title and returns a tuple of book info."""
        self.cursor.execute('''SELECT * FROM books WHERE Title = ?''', (title,))
        return self.cursor.fetchone()

    def add_book(self, info):
        """Adds a book to the database if it doesn't already exist."""
        title, authors, category, publish_date = info
        if type(authors) == list:
            authors = ", ".join(authors)

        # Check if the book already exists
        self.cursor.execute('''
        SELECT * FROM books 
        WHERE Title = ? AND Author = ? AND Genre = ? AND Publish_Date = ?
        ''', (title, authors, category, publish_date))
        if not self.cursor.fetchone():
            self.cursor.execute('''
            INSERT INTO books (Title, Author, Genre, Publish_Date)
            VALUES (?, ?, ?, ?)
            ''', (title, authors, category, publish_date))
            self.connection.commit()
            print(f"Book '{title}' by {authors} added successfully.")
        else:
            print(f"Book '{title}' by {authors} already exists.")

    def remove_book(self, title):
        """Removes a book from the database by title."""
        self.cursor.execute('''DELETE FROM books WHERE Title = ?''', (title,))
        self.connection.commit()
        print(f"Book '{title}' removed successfully.")

    def save(self):
        """Commits changes and closes the connection."""
        if self.connection:
            self.connection.commit()
            self._close_connection()

    def reconnect(self):
        """Reconnects to the database if the connection was closed before."""
        if not self.connection or not self.cursor:
            self._connect_to_db()
            print(f"Reconnected to database: {self.name}.db")

    def remove_user(self, name):
        """Removes this user's database file."""
        db_path = f".databases/{name}.db"
        if os.path.exists(db_path):
            self._close_connection()  # Ensure connection is closed before removing
            os.remove(db_path)
            print(f"Removed database file: {db_path}")

    def get_genres(self):
        """Returns all genres from the books table."""
        self.cursor.execute('SELECT Genre FROM books')
        return self.cursor.fetchall()
import sqlite3
import os 

class User:
	'''
	Connects to database by the given name and creates it if it doesn't already exists.
	After doing changes to the users database you must call save() method to save changes
	and close connection to the database.
	'''
	def __init__(self, name):
		#create hidden database folder if it doesn't already exist
		if not os.path.exists(".databases"):
			os.mkdir(".databases")
		self.name = name
		self.connection = sqlite3.connect(f'.databases/{name}.db')
		self.cursor = self.connection.cursor()	

	def return_db(self):
		return f"{self.name}.db"

	#Searches books by title and returns tuple of book info
	def search_db(self, title):
		self.cursor.execute('''SELECT * FROM books WHERE Title = ?''', (title,))
		result = self.cursor.fetchone()
		if result:
			return result
		return False

	#takes an array of at least length 4, adds book to database if it doesn't already exist
	def add_book(self, info):
		title = info[0]
		Authors = info[1]
		Category = info[2]
		publish_date = info[3]

		self.cursor.execute('''
		CREATE TABLE IF NOT EXISTS books(
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			Title TEXT,
			Author TEXT,
			Genre TEXT,
			Publish_Date TEXT
		)
		''')
		if not self.search_db(title):
			self.cursor.execute('''INSERT INTO books (Title, Author, Genre, Publish_Date)
		                  VALUES (?, ?, ?, ?)''', (title, Authors, Category, publish_date))
		else:
			return False

	def remove_book(self, title):
		self.cursor.execute('''DELETE FROM books WHERE Title = ?''', (title,))

	#Saves changes made to the users database and closes connection to the database
	def save(self):
		self.connection.commit()
		self.connection.close()

	#Reconnects to the users database if the connection was closed before
	def reconnect(self):
		self.connection = sqlite3.connect(f'.databases/{self.name}.db')
		self.cursor = self.connection.cursor()

	#removes users by deleting their database file
	def remove_user(self, name):
		os.remove(f".databases/{name}.db")
		
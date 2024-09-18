**Personalized-Book-Recommendation-System** \
A desktop application that offers personalized book recommendations based on user preferences This project is a Personalized Book Recommendation System that utilizes the Google Books API to fetch book information dynamically and stores it in a MySQL database. The backend is implemented in Python and uses a MySQL database running inside a Docker container for persistent storage. The application will be expanded to include a user-friendly GUI, allowing users to interact with the book database effortlessly. The project is designed to be modular and scalable, allowing for easy future enhancements and collaboration. 

**Prerequisites Before you begin, make sure you have the following installed on your system:**\
Internet Connection: Required to fetch book information from the Google Books API.\
Python: Ensure Python 3.7 or higher is installed.\
pip: Python package manager to install dependencies.\
Docker: Required to run the MySQL container.\
Git: For version control.


**How to Run the Project**

**1. Clone the Project**\
Open you terminal and clone the project.\
Keep the terminal open and proceed with the rest of the instructions.

**2. Install Required Libraries:**\
Run the install_requirements.sh script to install all necessary libraries: \
_./install_requirements.sh_

**3. Set Up Environment Variables**\
Create a _.env_ file by copying from _.env.example_:\
_cp .env.example .env_\
Open the _.env_ file and fill in the environment variables with the information provided by the group. (Request the necessary values from the project organizer if you don’t have them).\
Save the _.env_ file in the root directory of the project.

**4. Start the Docker Containers and the Project**\
To start the project and the necessary Docker containers, got to the project root directory and run:\
_./run.sh_\
Connect to the Database:\
_./connect_db.sh_\
When prompted, enter the database password (this is the MYSQL_PASSWORD you set in the .env file). Now you can run queries to inspect the main database.\
_USE books_database;_\
_SELECT * FROM books;_\
To exit the database, simply type:\
_exit;_

**5. Test the Project**\
To search for a specific book, modify the book_title variable in test_client.py, save the changes, and run ./client_run.sh again.\
To test the project, run the client script:\
_./client_run.sh_\
After running, revisit the database to see the books that have been added.

**6. Stop the Docker Containers**\
To stop the running containers, use:\
_./stop.sh_

**Note:**\
More functions and GUI enhancements are in progress!


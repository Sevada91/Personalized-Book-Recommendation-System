Personalized-Book-Recommendation-System
A desktop application that offers personalized book recommendations based on user preferences This project is a Personalized Book Recommendation System that utilizes the Google Books API to fetch book information dynamically and stores it in a MySQL database. The backend is implemented in Python and uses a MySQL database running inside a Docker container for persistent storage. The application will be expanded to include a user-friendly GUI, allowing users to interact with the book database effortlessly. The project is designed to be modular and scalable, allowing for easy future enhancements and collaboration.
Prerequisites Before you begin, make sure you have the following installed on your system:
Internet Connection: Required to fetch book information from the Google Books API. Python: Ensure Python 3.7 or higher is installed. pip: Python package manager to install dependencies. Docker: Required to run the MySQL container. Git: For version control.
How to Run the Project
Clone the Project
Install Required Libraries:
	Run the install_requirements.sh script to install all necessary libraries.
	./install_requirements.sh
1.	Set Up Environment Variables:
Create a .env file by copying from .env.example:
	cp .env.example .env
Open the .env file and fill in the environment variables with the information provided by the group. (Request the necessary values from the project organizer if you don’t have them).
Save the .env file in the root directory of the project.
2.	Start the Docker Containers and the Project:
To start the project and the necessary Docker containers, got to the project root directory and run:
./run.sh
3.	Connect to the Database:
	./connect_db.sh
When prompted, enter the database password (this is the MYSQL_PASSWORD you set in the .env file).
Now you can run queries to inspect the main database.
4.	Exit the Database:
	To exit the database, simply type:
		exit;
5.	Test the Project:
To search for a specific book, modify the book_title variable in test_client.py, save the changes, and run ./client_run.sh again.
To test the project, run the client script:
	./client_run.sh
After running, revisit the database to see the books that have been added.
6.	Stop the Docker Containers:
	To stop the running containers, use:
		./stop.sh
Note:
More functions and GUI enhancements are in progress!


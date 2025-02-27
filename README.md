# ToDo List - Fullstack Project with FastAPI, MySQL, and Frontend

This is a full-stack web application built with:

* Backend: FastAPI (Python)
* Frontend: HTML, CSS, Vanilla JavaScript
* Database: MySQL

This project demonstrates how to build and deploy a full-stack application with a MySQL database as the backend, a FastAPI server for API endpoints, and a simple frontend built with vanilla HTML, CSS, and JavaScript. Docker is used for containerizing both the frontend and backend services.

# Features #

* this is a SPA Frontend UI which has the Task adding form with pending tasks are displayed on the right side.
* Backend will be handled by the FastAPI module in Python.
* There are 3 main APIs to be utilized in backend in order to facilitate the Add, Read and Update queries.
* The Databse will be served by MySql with single task table in it.

# Technologies Used #

* FastAPI: A modern Python framework for building APIs with high performance.
* MySQL: A popular open-source relational database management system.
* HTML/CSS/JS: Standard web technologies used for frontend development.
* Docker: For containerizing the application and managing multi-container services.
* Docker Compose: For managing multi-container Docker applications with ease.

# Setup Instructions #

## 1. Clone the Repository #

Clone the repository to your local machine:
- gh repo clone 922850186v/ToDoList_FullStackProject

## 2. Environment Setup

Create a `.env` file in the root of your project and add the following environment variables to configure the MySQL database:
- MYSQL_ROOT_PASSWORD=admin123
- MYSQL_DATABASE=todo_directory
- MYSQL_USER=root
- MYSQL_PASSWORD=admin123

## 3. Build and Run Docker Containers 
* Build and start the containers:
`docker-compose up --build -d`
`docker-compose up`

This command will build the Docker images and start the containers. It will:

1. Start the backend service (FastAPI server).
2. Start the frontend service (Static HTML, CSS, JS).
3. Set up the MySQL database service.

* Access the Application:

   * Frontend: Open your browser and go to [http://127.0.0.1/](http://127.0.0.1/).
   * Backend (FastAPI): Go to [http://localhost:8000/docs](http://localhost:8000/docs) to check the Swagger Document.

## 4. Access the MySQL Database

To connect to the MySQL database running in the container, you can use the following credentials:

* Host: `localhost`
* Port: `3306`
* Username: `root`
* Password: `admin123`
* Database: `todo_directory`

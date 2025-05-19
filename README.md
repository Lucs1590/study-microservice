# Microservices

This repository contains a application that demonstrates the use of microservices architecture. The application is built using Python and FastAPI, and it consists of multiple microservices that communicate with each other using HTTP requests.
The application is designed to be modular and scalable, allowing for easy addition of new features and services.

## Microservices

The application consists of the following microservices:

- `user-microservice`: This microservice is responsible for managing user data and authentication.
- `people-microservice`: This microservice is responsible for managing people data and providing information about them.
- `postgres`: This microservice is responsible for managing the database and providing data storage for the application.
- `nginx`: This microservice is responsible for serving the application and acting as a reverse proxy for the other microservices.

## Prerequisites

Before running the application, make sure you have the following software installed on your machine:

- Docker: The application is designed to run in a containerized environment using Docker. You can download and install Docker from the official website: [Docker](https://www.docker.com/get-started)
- Docker Compose: This is a tool for defining and running multi-container Docker applications. It is included with Docker Desktop, so if you have Docker installed, you should already have Docker Compose.
- Python 3.8 or higher: The application is built using Python and FastAPI, so you will need to have Python installed on your machine. You can download and install Python from the official website: [Python](https://www.python.org/downloads/)
- PostgreSQL: The application uses PostgreSQL as the database. You can download and install PostgreSQL from the official website: [PostgreSQL](https://www.postgresql.org/download/)

## How to run the application

The following instructions will guide you through the process of running the application locally.

1. Clone the repository:

   ```bash
   git clone git@github.com:Lucs1590/study-microservice.git
   cd study-microservice
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the `user-microservice`:

   ```bash
   cd user-microservice
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

4. Run the `people-microservice`:

   ```bash
   cd people-microservice
   uvicorn app.main:app --host 0.0.0.0 --port 8001
   ```

As mentioned earlier, this will run the application locally, and does not mean that you are actually running an application with microservices concepts. To do this, you will need to use Docker to run the application in a containerized environment. The following instructions will guide you through running the application using Docker.

## How to run the application using Docker

1. Make sure you have the pre-requisites installed as mentioned above and the project cloned to your local machine.
2. Navigate to the root directory of the project:

   ```bash
   cd study-microservice
   ```

3. Build the Docker images:

   ```bash
   docker-compose build
   ```

4. Start the Docker containers:

   ```bash
   docker-compose up
   ```

5. The application will be running on `http://localhost:8000` for the `user-microservice` and `http://localhost:8001` for the `people-microservice`.
6. You can access the PostgreSQL database using a PostgreSQL client or GUI tool (e.g., pgAdmin) with the following connection details:

   - Host: `localhost`
   - Port: `5432`
   - Database: `postgres`
   - User: `postgres`
   - Password: `postgres`
7. To stop the Docker containers, press `Ctrl + C` in the terminal where you started the containers, or run the following command in a separate terminal:

   ```bash
   docker-compose down
   ```

### Set .env file

The application uses environment variables to configure the database connection and other settings. You will need to create a `.env` file in the root directory of the project. You can use the following template for the `.env` file:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres
POSTGRES_HOST=main_db
POSTGRES_PORT=5432
DATABASE_URL=postgresql://postgres:postgres@main_db:5432/postgres
USERS_SERVICE_HOST_URL=http://user_service:8000
```

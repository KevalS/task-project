# Document Dashboard Backend

## Overview

This is the backend implementation for the Document Dashboard project using FastAPI and PostgreSQL.

## Requirements

- Docker
- Docker Compose
- Python 3.6+

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd backend
   ```

2. Create a `.env` file in the project root with your PostgreSQL credentials:
   ```plaintext
   POSTGRES_USER=user
   POSTGRES_PASSWORD=password
   POSTGRES_DB=test_db
   ```

3. Build and run the containers using Docker Compose:
   ```bash
   docker-compose up --build
   ```

4. Load initial data into the database:
   ```bash
   python app/load_data.py
   ```

5. Access the API documentation at `http://localhost:8000/docs`.

## API Endpoints

- `GET /documents` - Retrieve all documents.
- `POST /documents` - Add a new document.

## Future Improvements

- Add more endpoints for updating and deleting documents.
- Implement proper error handling and validation.
- Write tests for all endpoints.

## Thought Process and Approach

**Backend:**
- Use FastAPI for its simplicity and performance.
- Use SQLAlchemy for ORM to interact with the PostgreSQL database.
- Separate concerns by organizing code into models, schemas, and CRUD operations.

**Database:**
- PostgreSQL chosen for its reliability and scalability.
- Create a table `documents` with appropriate fields to store document information.

**Deployment:**
- Dockerize the application to ensure consistency across environments.
- Use Docker Compose to manage multi-container applications.

**Communication:**
- Regularly document setup and usage steps.
- Keep the solution simple and focused on the requirements.

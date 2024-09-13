# FastAPI MongoDB Microservice Template

This repository provides a template for building a microservice using [FastAPI](https://fastapi.tiangolo.com/) with MongoDB as the database. This microservice template is designed for rapid development, providing a fully working setup to quickly integrate into larger architectures.

## Features

- **FastAPI** for high-performance APIs.
- **MongoDB** integration with [Motor](https://motor.readthedocs.io/), an async MongoDB driver.
- Environment variables for configuration.
- Docker-ready for containerization.

---

## Installation Guide

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- MongoDB (locally or via a service like [MongoDB Atlas](https://www.mongodb.com/cloud/atlas))
- [pip](https://pip.pypa.io/en/stable/)
- Docker (optional, for containerization)

### Step 1: Clone the Repository

```bash
git clone https://github.com/Nils-Lopez/fastapi-mongodb-microservice.git
cd fastapi-mongodb-microservice
```

### Step 2: Create a Virtual Environment

Create a virtual environment and activate it:

```bash
# On Linux/Mac/WSL
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
.\venv\Scripts\activate

```

### Step 3: Install the Dependencies

To install the dependencies, use:

```bash
# Using pip
pip install -r requirements.txt


```

### Step 4: Set Up Environment Variables

Duplicate the .template.env file to .env:

```bash

cp .template.env .env

```

Open the .env file and configure the necessary environment variables.

### Step 5: Run the app

Now, you can run the FastAPI application:

```bash

# Using uvicorn to serve the app
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000


```

The service will be available at http://localhost:8000

### Step 6: Access the DOC

API Docs: Once the server is running, you can access the interactive API docs by navigating to:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Docker Setup (Optional)

This template also provides a Docker setup if you want to containerize the service.

### Step 1: Build the image

First, build the Docker image:

```bash

docker build -t fastapi-mongodb-service .

```

### Step 2: Run the container

```bash

docker run -d --name fastapi-mongodb-container -p 8000:8000 --env-file .env fastapi-mongodb-service

```

### Step 3: Deploy

```bash

docker tag fastapi-mongodb-container your_container_repository_url/fast-api-mongodb-container:latest

docker push your_container_repository_url/fast-api-mongodb-container:latest

```

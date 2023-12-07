# Turbosquid Clone Backend

This is the backend of a Turbosquid.com clone built using Django Rest Framework. It provides RESTful APIs for managing 3D models, user authentication, and other essential functionalities.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Docker installed
- Docker Compose installed

## Installation

1. Clone the repository:

       git clone https://github.com/yourusername/turbosquid-clone-backend.git

Navigate to the project directory:

    cd turbosquid-clone-backend

Usage with Docker Compose

Create a .env file in the project root and configure the environment variables:
    
    DEBUG=True
    SECRET_KEY=your_secret_key
    DATABASE_URL=postgres://your_database_user:your_database_password@db:5432/your_database_name

Make sure to replace placeholders with your actual values.

Create and start the Docker containers:

    docker-compose up --build

This will build the Docker images and start the services. Your Django application will be accessible at http://localhost:8000.

Apply the database migrations:

bash

    docker-compose exec web python manage.py migrate

API Endpoints

    /api/product/: List and create 3D models.
    /api/product-single/<product_id>/: Retrieve, update, or delete a specific 3D model.
    /accounts/register/: Register a new user.
    /accounts/login/: Obtain an authentication token.
    /accounts/logout/: Logout and invalidate the token.

Contributing

If you'd like to contribute to this project, please follow these steps:

    Fork the repository
    Create a new branch (git checkout -b feature/your-feature)
    Make your changes
    Commit your changes (git commit -m 'Add some feature')
    Push to the branch (git push origin feature/your-feature)
    Create a pull request

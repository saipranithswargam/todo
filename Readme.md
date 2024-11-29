# Django To-Do App with Celery and Email Notifications

This project is a simple To-Do application built with Django. It includes user registration, JWT-based authentication, and allows users perform CRUD operations on todo's created. Additionally, it uses Celery and Redis to send welcome emails asynchronously upon user registration.

## Features

- User Registration
- JWT based token based authentication
- CRUD operations for To-Do items
- Asynchronous email notifications using Celery and Redis
- Dockerized Redis setup for message brokering

---

## Setup

- Clone the project and start with installation steps
- Run the django server, Docker container with redis, and celery Worker

## Installation

- ```pip install -r requirements.txt```

## API Endpoints
- Authentication Endpoints
1. **POST /users/register/** - User Registration
2. **POST /users/login/** - User Login
3. **POST /auth/refresh/** - Refresh Access Token
- To-Do Endpoints
1. **GET /users/todos/** - List To-Dos
2. **POST /users/todos/create/** - Create a To-Do
3. **PUT /users/todos/<id>/update/** - Update a To-Do
4. **DELETE /users/todos/<id>/delete/** - Delete a To-Do




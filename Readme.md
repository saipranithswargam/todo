# Django To-Do App with Celery and Email Notifications

This project is a simple To-Do application built with Django. It includes user registration, JWT-based authentication, and allows users perform CRUD operations on todo's created. Additionally, it uses Celery and Redis to send welcome emails asynchronously upon user registration.

## Features

- User Registration
- JWT based token based authentication
- CRUD operations for To-Do items
- Asynchronous email notifications using Celery and Redis
- Dockerized Redis setup for message brokering
- Periodic remainders notifications to email with Celery-beat
---

## Setup

- Clone the project and start with installation steps
- Run the django server, Docker container with redis, and celery Worker

## Installation

- ```pip install -r requirements.txt```

## API Endpoints
- Authentication Endpoints
1. **POST /api/auth/register/** - User Registration
2. **POST /api/auth/login/** - User Login
3. **POST /api/auth/refresh/** - Refresh Access Token
- To-Do Endpoints
1. **POST /api/todos/craete/** - Create a To-Do
2. **GET /api/todos/read/** -  List all To-Do
3. **PUT /api/todos/<id>/update/** - Update a To-Do
4. **DELETE /api/todos/<id>/delete/** - Delete a To-Do
5. **PATCH /api/todos/<id>/update/** - Partial Update a To-Do
6. **GET /api/todos/status/<status>/** - Filter To-Do Based on Status


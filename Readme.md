# Django To-Do App with Celery and Email Notifications

This project is a simple To-Do application built with Django. It includes user registration, JWT-based authentication, and allows users perform CRUD operations on todo's created. Additionally, it uses Celery and Redis to send welcome emails asynchronously upon user registration and reminders for pending tasks periodically

## Features

- User Registration
- JWT based token based authentication
- CRUD operations for To-Do items
- Asynchronous email notifications using Celery and Redis
- Dockerized Redis setup for message brokering
- Periodic remainder notifications to email with Celery-beat

---

## Installation

- ```pip install -r requirements.txt```

## Setup

- Clone the project and start with installation steps
- Start a redis container ```docker run --name redis-container -p 6379:6379 -d redis```
- Start Celery worker ```celery -A todo_project worker --pool=solo --loglevel=info```
- Start celery-beat ```celery -A todo_project beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler```
- Start server by ```python manage.py runserver```

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



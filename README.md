# api-django-ninja



## Description

An API based on [Django Ninja Framework](https://django-ninja.dev/) using [Python 3.11.9](https://www.python.org/downloads/release/python-3119/).


## Documentation
All endpoints have been documented with Swagger and Postman.
- The Swagger documentation can be accessed after run the project in http://localhost:8000/docs 
- The Postman documentation can be accessed in this [link](https://documenter.getpostman.com/view/14821693/2sAXjGbZAo).


## Init database with Docker

Ensure that you have Docker installed on your PC. Here is a [tutorial for installation on Ubuntu](https://docs.docker.com/engine/install/ubuntu/).

Execute the following commands will generate one container for a postgres database.

```bash
# Build Docker images without using the cache
$ docker compose build --no-cache

# Run Docker Compose to start containers. The -d flag runs Docker Compose as a background task.
$ docker compose up -d
```

** To stop the Docker-related services, run the following command:
```bash
$ docker compose down
```

## Install and start Backend

Ensure that you have [Python 3.11.9](https://www.python.org/downloads/release/python-3119/) and [Poetry](https://python-poetry.org/docs/) installed on your PC.

```bash
# In root of directory run this command
cp .env.example .env

# Creates an virtual env
$ python3.11 -m venv venv

# Install all dependencies
$ poetry install

# Apply all migrations to your database
$ python manage.py migrate

# Init the server
$ python manage.py runserver
```
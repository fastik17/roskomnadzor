# ROSCOMNADZOR CURSED

This is a repository for a web application developed with Django.



### Features

1. **Local Authentication** using email and password with [allauth](https://pypi.org/project/django-allauth/)
2. **Rest API** using [django rest framework](http://www.django-rest-framework.org/)
3. Celery for emails



###Endpoints:

1.admin signup - http://127.0.0.1:8000/api/v1/signup/

2.non_auth_user request - http://127.0.0.1:8000/api/v1/request/

3.admin users_request info  - http://127.0.0.1:8000/api/v1/info/

4.admin make decision  - http://127.0.0.1:8000/api/v1/blocked/ 
(if blocked=True , 10 min later user will got email notification)

**FOR EMAIL NOTIFICATIONS PLS CONNECT SOME YOUR SENDGRID/MAILGUN ACCOUNT**


More information you can find in swagger doc - http://127.0.0.1:8000/api-docs/

# Development

Following are instructions on setting up your development environment.

The recommended way for running the project locally and for development is using Docker.

It's possible to also run the project without Docker.

## Docker Setup (Recommended)

This project is set up to run using [Docker Compose](https://docs.docker.com/compose/) by default. It is the recommended way. You can also use existing Docker Compose files as basis for custom deployment, e.g. [Docker Swarm](https://docs.docker.com/engine/swarm/), [kubernetes](https://kubernetes.io/), etc.

1. Install Docker:
   - Linux - [get.docker.com](https://get.docker.com/)
   - Windows or MacOS - [Docker Desktop](https://www.docker.com/products/docker-desktop)
1. Clone this repo and `https://github.com/fastik17/roskomnadzor.git`

1. Use `.env.example` to create `.env`:
   ```sh
   $ cp .env.example .env
   ```
1. Start up the containers:

   ```sh
   $ docker-compose up
   ```

   This will build the necessary containers and start them, including the web server on the host and port you specified in `.env`.

   Current (project) directroy will be mapped with the container meaning any edits you make will be picked up by the container.

1. Seed the Postgres DB (in a separate terminal):
   ```sh
   $ docker-compose exec web python3 manage.py makemigrations
   $ docker-compose exec web python3 manage.py migrate
   ```
1. Create a superuser if required:
   ```sh
   $ docker-compose exec web python3 manage.py createsuperuser
   ```
   You will find an activation link in the server log output.
 
## Local Setup (Alternative to Docker)

1. [Postgresql](https://www.postgresql.org/download/)
2. [Python](https://www.python.org/downloads/release/python-365/)

### Installation


1. Clone this repo and `https://github.com/fastik17/roskomnadzor.git`
2. Run `pip install requirements.txt` to get all packages.
3. Run `cp .env.example .env`
4. Update .env file `DATABASE_URL` with your `database_name`, `database_user`, `database_password`, if you use postgresql.
   Can alternatively set it to `sqlite:////tmp/my-tmp-sqlite.db`, if you want to use sqlite for local development.

### Getting Started

1. Run `python manage.py makemigrations`
2. Run `python manage.py migrate`
3. Run `python manage.py createsuperuser`
4. Run `python manage.py runserver`
5. Run `celery -A roskomnadzor worker -l info`
6. Run `celery -A roskomnadzor beat -l info
`

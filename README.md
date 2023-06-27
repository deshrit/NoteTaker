# NoteTaker
A simple fullstack application in production

# Try
[live](https://dnotetaker.azurewebsites.net/)

# To run locally
#### 1. create ./.env file
```
# Django
DJANGO_SECRET_KEY=<your_key>
DJANGO_DEBUG=
DJANGO_ALLOWED_HOSTS=*

# Database
DB_BACKEND=postgresql
DB_HOST=<your_db_host>
DB_USER=<your_db_user>
DB_NAME=<your_db_name>
DB_PASSWORD=<your_db_pass>
DB_PORT=<your_db_port>

# Email
EMAIL_HOST_USER=<your_email>
EMAIL_HOST_PASSWORD=<your_password>

# Azure Storage
AZURE_STORAGE_ACCOUNT_NAME=<your_credentials>
AZURE_CONNECTION_STRING=<your_credentials>
AZURE_STORAGE_ACCOUNT_KEY=<your_credentials>
AZURE_CONTAINER_NAME=<your_credentials>
```
#### 2. Docker and docker-compose
```
docker compose up
```
#### 3. Application access
```
http://0.0.0.0:8000
```
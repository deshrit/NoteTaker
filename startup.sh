#!/bin/bash

set -e

python manage.py migrate

python manage.py collectstatic --no-input

gunicorn -c gunicorn.conf.py core.wsgi:application
#!/bin/sh
set -e
#/opt/venv/bin/python manage.py runserver
#python manage.py collectstatic --noinput
/opt/venv/bin/python manage.py makemigrations
/opt/venv/bin/python manage.py migrate
/opt/venv/bin/gunicorn -b :8001 --chdir /app communication_system.wsgi:application
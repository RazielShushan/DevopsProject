#!/bin/sh
set -e
ls
#/opt/venv/bin/python manage.py runserver '0.0.0.0:8002'
#python manage.py collectstatic --noinput
/opt/venv/bin/python manage.py makemigrations
/opt/venv/bin/python manage.py migrate
/opt/venv/bin/gunicorn -b :8002 --chdir /app communication_system.wsgi:application
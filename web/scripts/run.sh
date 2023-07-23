#!/bin/sh
set -e
/opt/venv/bin/python manage.py makemigrations
/opt/venv/bin/python manage.py migrate
/opt/venv/bin/gunicorn -b :8002 --chdir /app communication_system.wsgi:application
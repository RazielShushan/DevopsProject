#!/bin/bash
SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"rzhtk151@gmail.com"}
cd /app/
#/opt/venv/bin/python manage.py makemigrations
#/opt/venv/bin/python manage.py migrate
#/opt/venv/bin/python manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true
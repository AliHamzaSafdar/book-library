#!/bin/sh
# not being used

python manage.py makemigrations
python manage.py migrate --noinput
python manage.py test
python manage.py collectstatic --noinput

exec gunicorn --bind 0.0.0.0:8001 PrimeDjango.wsgi:application

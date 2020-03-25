#!/bin/bash
# Collect static files for app
python manage.py collectstatic --noinput

# Create DB, run DB migrations
python db/create_db.py
python manage.py migrate

# Finally launch the server
gunicorn antfarm.wsgi:application -w $GUNICORN_WORKERS -b :8000 -t 60 $@

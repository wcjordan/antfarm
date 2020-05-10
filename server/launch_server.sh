#!/bin/bash

# Sleep for 2 seconds to allow DB to come up
# TODO (jordan) Officially wait for DB to come up
echo "sleep 2s"
sleep 2s

# Collect static files for app & run migrations
python manage.py collectstatic --noinput
python manage.py migrate

# Finally launch the server
gunicorn antfarm.wsgi:application -w $GUNICORN_WORKERS -b :8000 -t 60 $@

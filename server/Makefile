#!make

PARENT_DIR = $(dir $(PWD))

# Test w/ PyTest & lint Django app
.PHONY: test
test:
	cd ../; docker-compose run --rm server flake8 antfarm/training  # TODO change to .
	# TODO (jordan) remove need to hardcode apps
	cd ../; docker-compose run --rm server pylint -j 0 --load-plugins pylint_django antfarm

	# Unit tests
	cd ../; docker-compose run --rm server python manage.py test antfarm.training

# Yapf formatting
.PHONY: format
format:
	cd ../; docker-compose run --rm server yapf -ri .

# Continuously run pytest for TDD 
.PHONY: tdd
tdd:
	cd ../; docker-compose exec server watchmedo shell-command -R -W -i '*/__pycache__*;*/.pytest_cache*' --command='sleep 1; pytest --durations=0 antfarm/tests'

# Make migrations for server
.PHONY: create-migrations
create-migrations:
	cd ../; docker-compose run --rm server python manage.py makemigrations --verbosity 3

# Add an admin to Django
.PHONY: create-superuser
create-superuser:
	cd ../; docker-compose run --rm server python manage.py createsuperuser

# Update starter data for server
.PHONY: update-starter-data
update-starter-data:
	echo "Rerun if failed w/ could not connect to server: Connection refused"
	cd ../; docker-compose run --rm -v $(PARENT_DIR)db/starter_db:/starter_db server pg_dump -h db -U postgres -f /starter_db/starter_db.sql antfarm

# Open a shell inside container
.PHONY: shell
shell:
	cd ..; docker-compose exec server /bin/bash

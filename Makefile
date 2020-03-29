#!make

# Build containers
.PHONY: build
build:
	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose build

# Test containers & lint Django app
.PHONY: test
test:
	docker-compose run --rm server flake8 .
	# TODO (jordan) remove need to hardcode apps
	docker-compose run --rm server pylint -j 0 --load-plugins pylint_django create_db.py antfarm

	# Unit & integration tests for antfarm
	# TODO (jordan) add unit tests
# 	docker-compose run --rm server pytest --durations=0 antfarm/tests/train

# Start containers for development
.PHONY: dev-up
dev-up:
	docker-compose up

# Start containers for production
.PHONY: prod-up
prod-up:
	docker-compose -f production.yml up -d

# Stop & teardown containers
.PHONY: down
down:
	docker-compose down

# Yapf python formatting
.PHONY: format
format:
	$(MAKE) -C ui format
	docker-compose run --rm server yapf -ri .

# Make migrations for server
.PHONY: create-migrations
create-migrations:
	docker-compose run --rm server python manage.py makemigrations --verbosity 3

# Make migrations for server
.PHONY: restore-db
restore-db:
	docker-compose run --rm server psql -h db -p 5432 -U postgres -c '"DROP DATABASE antfarm;"'

.PHONY: update-starter-data
update-starter-data:
	docker-compose run --rm server pg_dump -h db -U postgres -f db/starter_db.sql antfarm

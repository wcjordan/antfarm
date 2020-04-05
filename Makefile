#!make

# Build containers
.PHONY: build
build:
	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose build

# Test containers & lint Django app
.PHONY: test
test:
	$(MAKE) -C ui test
	$(MAKE) -C server test

# Start containers for development
.PHONY: dev-up
dev-up:
	docker-compose up

# Start containers for production
.PHONY: prod-up
prod-up:
	docker-compose -f production.yml up -d

# Stop containers
.PHONY: stop
stop:
	docker-compose stop

# Teardown containers
.PHONY: down
down:
	docker-compose down -v

# Yapf python formatting
.PHONY: format
format:
	$(MAKE) -C ui format
	$(MAKE) -C server format

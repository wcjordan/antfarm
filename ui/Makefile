DOCKER_FLAGS := -d

# Build containers
build:
	DOCKER_BUILDKIT=1 docker build -t antfarm-ui -f Dockerfile.dev .

# Start containers for development
dev-up: down
	docker run --shm-size=10g -p 80:80 -p 3000:3000 -p9009:9009 \
	  -v $(CURDIR)/js/public:/js_app/public \
	  -v $(CURDIR)/js/src:/js_app/src \
	  -v $(CURDIR)/bash/.bashrc:/root/.bashrc \
	  -v $(CURDIR)/bash:/root/bash \
	  --name antfarm-ui-run $(DOCKER_FLAGS) --rm antfarm-ui $(DOCKER_CMD)

test: DOCKER_CMD:=yarn jest
test: DOCKER_FLAGS:=-ti
test: dev-up

# Stop & teardown containers
down:
	-docker stop antfarm-ui-run
	-docker rm antfarm-ui-run

# ESLint & Prettier JS formatting
format:
	cd js; npx lint-staged

dev-storybook: DOCKER_CMD:=npm run storybook
dev-storybook: dev-up

# Open a terminal in a container
shell:
	 docker exec -it antfarm-ui-run /bin/sh

.PHONY: build dev-up down test format dev-storybook shell

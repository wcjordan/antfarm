DOCKER_FLAGS := -it

# Build containers
build:
	DOCKER_BUILDKIT=1 docker build -t antfarm-server -f Dockerfile .

# Start containers for development
dev-up: down
	docker run --shm-size=10g -p 8000:8000 \
		-v media:/www/media \
		-v static:/www/server \
		-v $(CURDIR):/usr/src/app \
		--name antfarm-server-run $(DOCKER_FLAGS) --rm antfarm-server $(DOCKER_CMD)

# test: DOCKER_CMD:=yarn jest
# test: DOCKER_FLAGS:=-ti
# test: dev-up

# Stop & teardown containers
down:
	-docker stop antfarm-server-run
	-docker rm antfarm-server-run

# # ESLint & Prettier JS formatting
# format:
# 	cd js; npx lint-staged

# Open a terminal in a container
shell:
	 docker exec -it antfarm-server-run /bin/sh

.PHONY: build dev-up down test format shell

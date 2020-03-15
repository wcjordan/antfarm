# Build containers
build:
	docker build -t antfarm-ui -f Dockerfile.dev .

# Start containers for development
dev_up: down
	docker run --shm-size=10g -p 80:80 -p 3000:3000 \
	  -v $(CURDIR)/js/public:/js_app/public \
	  -v $(CURDIR)/js/src:/js_app/src \
	  -v $(CURDIR)/bash/.bashrc:/root/.bashrc \
	  -v $(CURDIR)/bash:/root/bash \
	  --name antfarm-ui-run -d antfarm-ui

# Stop & teardown containers
down:
	-docker stop antfarm-ui-run
	-docker rm antfarm-ui-run

# ESLint & Prettier JS formatting
format:
	cd js; npx lint-staged

# Open a terminal in a container
shell:
	 docker exec -it antfarm-ui-run /bin/sh

.PHONY: build dev_up down format shell

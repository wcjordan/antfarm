#!make
include ../.env

# Test w/ Jest
.PHONY: test
test:
	# Lint & typecheck by building
	cd ../; docker-compose run --rm jsdev yarn run build
	# Unit & integration tests for antfarm
	# TODO (jordan) add unit tests
	cd ../; docker-compose run --rm jsdev yarn jest

# ESLint & Prettier JS formatting
.PHONY: format
format:
	cd js; npx lint-staged

.PHONY: dev-storybook
dev-storybook:
	cd ../; docker-compose run --rm -p $(NGINX_PORT):9009 jsdev npm run storybook

# Open a shell inside container
.PHONY: shell
shell:
	cd ..; docker-compose exec jsdev /bin/bash

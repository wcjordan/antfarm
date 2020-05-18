#!make
include ../.env

# Test w/ Jest
.PHONY: test
test:
	# Lint & typecheck by building
	cd ../; docker-compose run --rm jsdev yarn run build
	# Unit & snapshot tests for UI
	cd ../; docker-compose run --rm jsdev yarn jest

# ESLint & Prettier JS formatting
.PHONY: format
format:
	cd js; npx lint-staged

.PHONY: storybook
storybook:
	cd ../; docker-compose run --rm -p $(NGINX_PORT):9009 jsdev npm run storybook

# Open a shell inside container
.PHONY: shell
shell:
	cd ..; docker-compose exec jsdev /bin/bash

# Update snapshot tests
.PHONY: update-snapshots
update-snapshots:
	cd ../; docker-compose run --rm jsdev yarn jest -u

# Fix import ordering
.PHONY: fix-imports
fix-imports:
	cd js; npx eslint --fix "**/*.{ts,tsx,js,jsx}"

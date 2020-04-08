#!make

# Test w/ PyTest & linting
.PHONY: test
test:
	cd ../; docker-compose run --rm learning flake8 environments  # TODO change to .
	# TODO (jordan) remove need to hardcode apps
	# TODO (jordan) enable pylint
# 	cd ../; docker-compose run --rm learning pylint -j 0 environments # TODO add examples

	# TODO (jordan) add unit tests
	# docker-compose run --rm learning pytest --durations=0 environments examples

# Yapf formatting
.PHONY: format
format:
	cd ../; docker-compose run --rm learning yapf -ri .

# Open a shell inside container
.PHONY: shell
shell:
	cd ..; docker-compose exec learning /bin/bash

# Continuously run pytest for TDD
.PHONY: tdd
tdd:
	cd ../; docker-compose exec learning watchmedo shell-command -R -W -i '*/__pycache__*;*/.pytest_cache*' --command='pytest --durations=0 tests'

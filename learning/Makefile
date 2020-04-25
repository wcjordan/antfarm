#!make

# Test w/ PyTest & linting
.PHONY: test
test:
	# TODO (jordan) remove need to hardcode modules
	cd ../; docker-compose run --rm learning flake8 environments runners examples
	cd ../; docker-compose run --rm learning pylint -j 0 --extension-pkg-whitelist=numpy environments runners

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

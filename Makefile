install:
	poetry install
build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

gendiff:
	poetry run gendiff

test:
	poetry run pytest

test-coverage:
	pytest --cov=gendiff --cov-report=term


check:
	test lint

.PHONY:	install test lint selfcheck check build


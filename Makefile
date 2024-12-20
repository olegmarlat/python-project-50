install: poetry install

test: poetry run pytest

test-coverage: @poetry run pytest --cov=gendiff --cov-report xml

gendiff: poetry run gendiff

build: check poetry build

publish: poetry publish --dry-run

package-install: python3 -m pip install --user dist/*.whl

make lint: poetry run flake8 gendiff

selfcheck: poetry check

check: selfcheck test lint

.PHONY: install test lint selfcheck check build


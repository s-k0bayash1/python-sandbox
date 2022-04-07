lint:
	poetry run flake8 --max-line-length 120 . && poetry run mypy .

fmt:
	poetry run black . && poetry run isort .

fix: fmt lint

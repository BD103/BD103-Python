@echo off

poetry run black . && poetry run isort . && poetry run flake8 && poetry run pytest -q && prettier . --write

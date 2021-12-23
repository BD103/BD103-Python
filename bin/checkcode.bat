@echo off

poetry run black . --check && poetry run isort . --check && poetry run flake8 && poetry run pytest -q && prettier . --check

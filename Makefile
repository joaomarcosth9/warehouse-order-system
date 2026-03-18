.PHONY: run format lint

run:
	uv run uvicorn app.main:app --reload

format:
	uv run ruff format .

lint:
	uv run ruff check .
	uv run mypy

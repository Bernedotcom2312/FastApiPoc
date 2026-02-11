dev:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

test:
	pytest tests/ -v

format:
	uv run ruff check --fix app/ tests/

typecheck:
	mypy app/

install-dev:
	uv sync --all-extras

clean:
	rm -rf .venv __pycache__ .pytest_cache
	find . -name "*.pyc" -delete
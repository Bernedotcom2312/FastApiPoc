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

install-hooks:
	uv run pre-commit install
	uv run pre-commit install --hook-type commit-msg

uninstall-hooks:
	uv run pre-commit uninstall
	uv run pre-commit uninstall --hook-type commit-msg

pre-commit-all:
	uv run pre-commit run --all-files

commit:
	uv run cz commit

bump:
	uv run cz bump

bump-changelog:
	uv run cz bump --changelog

bump-dry:
	uv run cz bump --dry-run

changelog:
	uv run cz changelog

check-commit:
	uv run cz check --rev-range HEAD

check-commits-from:
	@echo "Usage: make check-commits-from REF=origin/main"
	uv run cz check --rev-range $(REF)..HEAD

cz-info:
	uv run cz info

setup: install-dev install-hooks
	@echo "✅ Projet configuré avec succès!"
	@echo "📝 Utilisez 'make commit' pour créer des commits conformes"
	@echo "🔄 Utilisez 'make bump' pour créer une nouvelle version"

release: pre-commit-all test bump-changelog
	@echo "🎉 Nouvelle version prête!"
	@echo "💡 N'oubliez pas de push les tags: git push --tags"

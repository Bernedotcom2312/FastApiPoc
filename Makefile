# Scripts de développement pour FastAPI

# Pour lancer le serveur de développement
dev:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Pour lancer les tests
test:
	pytest tests/ -v

# Pour formater le code
format:
	black app/ tests/
	isort app/ tests/

# Pour vérifier le typage
typecheck:
	mypy app/

# Pour installer les dépendances de développement
install-dev:
	uv sync --all-extras

# Pour créer un environnement propre
clean:
	rm -rf .venv __pycache__ .pytest_cache
	find . -name "*.pyc" -delete
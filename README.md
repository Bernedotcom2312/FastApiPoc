# Mon Premier Projet FastAPI

Ce projet est une introduction à FastAPI utilisant UV comme gestionnaire de paquets.

## Installation

1. Assurez-vous d'avoir UV installé
2. Installez les dépendances :
   ```bash
   uv sync
   ```

## Lancement du serveur de développement

```bash
uv run uvicorn app.main:app --reload
```

L'API sera accessible à l'adresse : http://localhost:8000

## Documentation automatique

- Swagger UI : http://localhost:8000/docs
- ReDoc : http://localhost:8000/redoc

## Structure du projet

```
├── app/
│   ├── __init__.py
│   ├── main.py          # Point d'entrée de l'application
│   ├── models/          # Modèles Pydantic
│   ├── routers/         # Routes API
│   └── services/        # Logique métier
├── tests/               # Tests
├── pyproject.toml       # Configuration du projet
└── README.md           # Ce fichier
```

## TODO

* pre commit hook
* commitlint + semver
* docker
* trivy + sbom
* github actions
* devcontainer
* dependabot
* redis
* DB
* Auth

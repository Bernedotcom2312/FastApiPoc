# Mon Premier Projet FastAPI

Ce projet est une introduction à FastAPI utilisant UV comme gestionnaire de paquets, avec un système de commitlint et semantic versioning intégré.

## Installation

1. Assurez-vous d'avoir UV installé
2. Setup complet du projet :
   ```bash
   make setup
   ```

OU manuellement :
2. Installez les dépendances :
   ```bash
   uv sync --all-extras
   ```
3. Installez les hooks pre-commit :
   ```bash
   make install-hooks
   ```

## Lancement du serveur de développement

```bash
uv run uvicorn app.main:app --reload
# OU
make dev
```

L'API sera accessible à l'adresse : http://localhost:8000

## Documentation automatique

- Swagger UI : http://localhost:8000/docs
- ReDoc : http://localhost:8000/redoc

## 🚀 Gestion des commits et versioning

Ce projet utilise **Conventional Commits** et **Semantic Versioning** pour automatiser la gestion des versions.

### Créer un commit

Utilisez l'assistant interactif pour créer des commits conformes :

```bash
make commit
```

### Types de commits supportés

- `feat`: ✨ Nouvelle fonctionnalité (MINOR)
- `fix`: 🐛 Correction de bug (PATCH)
- `BREAKING CHANGE`: ⚠️ Changement incompatible (MAJOR)
- `docs`: 📚 Documentation
- `style`: 💎 Formatage, style
- `refactor`: 📦 Refactorisation
- `perf`: 🚀 Amélioration des performances
- `test`: 🚨 Tests
- `chore`: 🔧 Maintenance
- `ci`: 👷 CI/CD

### Exemple de commits

```bash
feat(api): add user authentication endpoint
fix(auth): resolve token expiration issue
docs: update API documentation
feat!: change user model structure
```

### Gestion automatique des versions

```bash
# Bump automatique selon les commits
make bump

# Bump avec génération du changelog
make bump-changelog

# Simulation (voir ce qui va changer)
make bump-dry
```

### Vérification des commits

```bash
# Vérifier le dernier commit
make check-commit

# Vérifier tous les commits depuis main
make check-commits-from REF=origin/main
```

## 🛠️ Développement

### Commandes utiles

```bash
make test           # Lancer les tests
make format         # Formatter le code
make typecheck      # Vérification de types
make pre-commit-all # Exécuter tous les hooks
make release        # Workflow complet de release
```

## Structure du projet

```
├── app/
│   ├── __init__.py
│   ├── main.py          # Point d'entrée de l'application
│   ├── models/          # Modèles Pydantic
│   ├── routers/         # Routes API
│   └── services/        # Logique métier
├── tests/               # Tests
├── .pre-commit-config.yaml   # Configuration pre-commit
├── .cz-config             # Configuration commitizen
├── CHANGELOG.md           # Historique des versions (généré automatiquement)
├── pyproject.toml         # Configuration du projet
├── Makefile              # Commandes utiles
└── README.md             # Ce fichier
```

## � Docker

### Lancer avec Docker

```bash
# Construire et lancer l'application
docker-compose up --build

# Lancer en arrière-plan
docker-compose up -d

# Voir les logs
docker-compose logs -f

# Arrêter les services
docker-compose down
```

### Construire l'image Docker uniquement

```bash
# Construire l'image
docker build -t fastapi-app .

# Lancer le conteneur
docker run -p 8000:8000 fastapi-app
```

L'application sera accessible à l'adresse : http://localhost:8000

### Optimisations Docker

- **Multi-stage build** : Image finale allégée
- **UV** : Gestionnaire de paquets ultra-rapide
- **Utilisateur non-root** : Sécurité renforcée
- **Health check** : Surveillance de l'état de l'application

## 📋 Workflow de développement

1. **Cloner et setup** : `make setup`
2. **Développer** : Coder votre fonctionnalité
3. **Tester** : `make test`
4. **Commit** : `make commit` (suit automatically les conventional commits)
5. **Release** : `make release` (tests + bump + changelog)
6. **Push** : `git push --tags` pour déployer la nouvelle version

## TODO

* ~~pre commit hook~~ ✅
* ~~commitlint + semver~~ ✅
* ~~docker~~ ✅
* trivy + sbom
* github actions
* devcontainer
* dependabot
* redis
* DB
* Auth
* bake / buildx ?

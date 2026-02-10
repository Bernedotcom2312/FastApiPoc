from typing import List, Optional

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Création de l'instance FastAPI
app = FastAPI(
    title="Mon Premier Projet FastAPI",
    description="Une API simple créée avec FastAPI et UV",
    version="1.0.0",
)

# Configuration CORS (utile pour le développement front-end)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En production, spécifiez des domaines précis
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modèles Pydantic (similaires aux interfaces TypeScript)
class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float
    is_available: bool = True

class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    is_available: bool = True

# Base de données simulée (en mémoire)
fake_items_db: List[Item] = [
    Item(id=1, name="Laptop", description="Ordinateur portable", price=999.99),
    Item(id=2, name="Souris", description="Souris sans fil", price=29.99),
]

# Routes de base
@app.get("/")
async def root():
    """Point d'entrée principal de l'API"""
    return {
        "message": "Bienvenue dans votre première API FastAPI !",
        "documentation": "/docs",
        "endpoints": {
            "items": "/items",
            "health": "/health"
        }
    }

@app.get("/health")
async def health_check():
    """Endpoint de vérification de santé"""
    return {"status": "healthy", "service": "FastAPI"}

# Routes pour les items
@app.get("/items", response_model=List[Item])
async def get_items():
    """Récupérer tous les items"""
    return fake_items_db

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    """Récupérer un item par son ID"""
    for item in fake_items_db:
        if item.id == item_id:
            return item
    return {"error": "Item non trouvé"}, 404

@app.post("/items", response_model=Item)
async def create_item(item: ItemCreate):
    """Créer un nouvel item"""
    # Générer un nouvel ID
    new_id = max([i.id for i in fake_items_db if i.id], default=0) + 1

    # Créer le nouvel item
    new_item = Item(id=new_id, **item.dict())
    fake_items_db.append(new_item)

    return new_item

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item_update: ItemCreate):
    """Mettre à jour un item existant"""
    for i, item in enumerate(fake_items_db):
        if item.id == item_id:
            updated_item = Item(id=item_id, **item_update.dict())
            fake_items_db[i] = updated_item
            return updated_item
    return {"error": "Item non trouvé"}, 404

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    """Supprimer un item"""
    for i, item in enumerate(fake_items_db):
        if item.id == item_id:
            deleted_item = fake_items_db.pop(i)
            return {"message": f"Item {deleted_item.name} supprimé avec succès"}
    return {"error": "Item non trouvé"}, 404

# Point d'entrée pour exécuter l'application directement
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True  # Rechargement automatique en développement
    )

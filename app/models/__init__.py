from typing import Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    """Modèle de base pour un Item"""
    name: str
    description: Optional[str] = None
    price: float
    is_available: bool = True


class ItemCreate(ItemBase):
    """Modèle pour créer un item (sans ID)"""
    pass


class Item(ItemBase):
    """Modèle complet d'un item (avec ID)"""
    id: int

    class Config:
        from_attributes = True  # Permet la conversion depuis les ORM objects


class User(BaseModel):
    """Modèle pour un utilisateur"""
    id: Optional[int] = None
    username: str
    email: str
    is_active: bool = True

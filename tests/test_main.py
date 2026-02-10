from fastapi.testclient import TestClient

from app.main import app

# Client de test
client = TestClient(app)


def test_read_root():
    """Test de l'endpoint racine"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "FastAPI" in data["message"]


def test_health_check():
    """Test de l'endpoint de santé"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"


def test_get_items():
    """Test de récupération des items"""
    response = client.get("/items")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 0


def test_create_item():
    """Test de création d'un item"""
    new_item = {
        "name": "Test Item",
        "description": "Item de test",
        "price": 19.99,
        "is_available": True
    }
    response = client.post("/items", json=new_item)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == new_item["name"]
    assert data["price"] == new_item["price"]
    assert "id" in data


def test_get_item_by_id():
    """Test de récupération d'un item par ID"""
    # D'abord créer un item
    new_item = {
        "name": "Test Item for Get",
        "description": "Item de test pour get",
        "price": 25.99,
        "is_available": True
    }
    create_response = client.post("/items", json=new_item)
    created_item = create_response.json()
    item_id = created_item["id"]

    # Puis le récupérer
    get_response = client.get(f"/items/{item_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["id"] == item_id
    assert data["name"] == new_item["name"]

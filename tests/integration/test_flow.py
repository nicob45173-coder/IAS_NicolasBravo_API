from app.models import reset_users
def test_full_flow(client):
    reset_users()
    # Crear usuario
    res = client.post("/users", json={"name": "Pedro"})
    assert res.status_code == 201
    user_id = res.get_json()["id"]

    # Obtener usuario
    res = client.get(f"/users/{user_id}")
    assert res.status_code == 200

    # Eliminar usuario
    res = client.delete(f"/users/{user_id}")
    assert res.status_code == 200
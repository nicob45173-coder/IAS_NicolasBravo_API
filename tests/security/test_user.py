from app.models import reset_users

def test_get_users(client):
    reset_users()
    res = client.get("/users")
    assert res.status_code == 200


def test_create_user(client):
    reset_users()
    res = client.post("/users", json={"name": "Juan"})
    assert res.status_code == 201
    assert res.get_json()["name"] == "Juan"
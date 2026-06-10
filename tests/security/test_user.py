
def test_get_users(client):
    res = client.get("/users")
    assert res.status_code == 200


def test_create_user(client):

    res = client.post(
        "/users",
        json={"name": "Juan"}
    )

    assert res.status_code == 201
    assert res.get_json()["name"] == "Juan"
def test_full_flow(client):

    res = client.post(
        "/users",
        json={"name": "Pedro"}
    )

    assert res.status_code == 201

    user_id = res.get_json()["id"]

    res = client.get(f"/users/{user_id}")
    assert res.status_code == 200

    res = client.delete(f"/users/{user_id}")
    assert res.status_code == 200
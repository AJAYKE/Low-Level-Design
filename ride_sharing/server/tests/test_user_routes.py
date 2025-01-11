def test_create_user_sucess(client):
    payload = {
        "user_name": "Ajay",
        "country": "india",
        "phone_number": "9876543210",
    }
    response = client.post("/api/v1/users", json=payload)
    assert response.status_code == 201
    assert response.get_json()["message"] == "user Ajay created successfully"


def test_create_user_failed_invalid_input(client):
    payload = {
        "user_name": "Ajay",
        "phone_number": "9876543210",
        "email": "emailll",
    }
    response = client.post("/api/v1/users", json=payload)
    assert response.status_code == 400
    assert response.get_json()["error"] == "Invalid Request Body"


def test_update_to_driver(client):
    response = client.post("/api/v1/users/2/update_to_driver")
    assert response.status_code == 201
    assert response.get_json()["message"] == "user role updated successfully"

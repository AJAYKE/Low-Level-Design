def test_create_ride(client):
    payload = {
        "user_id": 1,
        "source_location": [1.2, 3.4],
        "destination_location": [15.8, 7.6],
    }
    response = client.post("/api/v1/create_ride", json=payload)
    assert response.status_code == 201
    assert (
        response.get_json()["message"]
        == "Your Ride is successfully booked, your ride is on the way"
    )
    assert type(response.get_json()["data"]["ride_id"]) == type(int)

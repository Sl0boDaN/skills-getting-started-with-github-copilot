from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_from_activity():
    email = "student@mergington.edu"
    activity_name = "Chess Club"

    signup_response = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert signup_response.status_code == 200

    delete_response = client.delete(f"/activities/{activity_name}/signup?email={email}")
    assert delete_response.status_code == 200
    assert "unregistered" in delete_response.json()["message"]

    activity_response = client.get("/activities")
    assert email not in activity_response.json()[activity_name]["participants"]

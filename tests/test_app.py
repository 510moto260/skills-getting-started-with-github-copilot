from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"

    signup_response = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert signup_response.status_code == 200

    unregister_response = client.delete(f"/activities/{activity_name}/unregister?email={email}")
    assert unregister_response.status_code == 200
    assert email not in client.get("/activities").json()[activity_name]["participants"]


def test_unregister_participant_fails_for_unregistered_email():
    activity_name = "Chess Club"
    email = "notregistered@mergington.edu"

    response = client.delete(f"/activities/{activity_name}/unregister?email={email}")
    assert response.status_code == 404

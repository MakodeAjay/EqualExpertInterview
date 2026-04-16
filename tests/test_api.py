from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_octocat_gists():
    """
    Test API response for a known GitHub user (octocat).

    Validates:
    - HTTP status code is 200
    - Response structure contains expected fields
    """
    response = client.get("/octocat")

    assert response.status_code == 200

    data = response.json()

    assert data["user"] == "octocat"
    assert isinstance(data["gists"], list)

    if data["gists"]:
        gist = data["gists"][0]
        assert "id" in gist
        assert "url" in gist
        assert "files" in gist
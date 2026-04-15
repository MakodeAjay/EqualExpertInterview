from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_octocat_gists():
    response = client.get("/octocat")
    assert response.status_code == 200

    data = response.json()

    assert data["username"] == "octocat"
    assert isinstance(data["gists"], list)

    # Check structure of at least one gist (if exists)
    if data["gists"]:
        gist = data["gists"][0]
        assert "id" in gist
        assert "url" in gist
        assert "files" in gist
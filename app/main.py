from fastapi import FastAPI, HTTPException
from app.github import fetch_gists

app = FastAPI()


@app.get("/{username}")
def get_gists(username: str):
    """
    Retrieve public GitHub gists for a given user.

    Args:
        username (str): GitHub username

    Returns:
        dict: JSON response containing username and list of gists

    Raises:
        HTTPException: If GitHub API call fails or unexpected error occurs
    """
    try:
        gists = fetch_gists(username)
        return {
            "user": username,
            "gists": gists
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
def health():
    """
    Health check endpoint.

    Used by container orchestration tools (e.g., Docker, Kubernetes)
    to verify that the service is running.
    """
    return {"status": "ok"}
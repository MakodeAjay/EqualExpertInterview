from fastapi import FastAPI, HTTPException
from app.github import fetch_gists

app = FastAPI()


@app.get("/{username}")
def get_gists(username: str, page: int = 1, per_page: int = 10):
    """
    Retrieve public GitHub gists for a given user with pagination support.

    Args:
        username (str): GitHub username
        page (int): Page number (default: 1)
        per_page (int): Number of results per page (default: 10)

    Returns:
        dict: Paginated list of gists
    """
    try:
        gists = fetch_gists(username, page, per_page)
        return {
            "user": username,
            "page": page,
            "per_page": per_page,
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
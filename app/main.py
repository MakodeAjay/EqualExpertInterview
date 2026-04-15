from fastapi import FastAPI, HTTPException
from app.github import fetch_gists

app = FastAPI()

@app.get("/{username}")
def get_gists(username: str):
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
    return {"status": "ok"}
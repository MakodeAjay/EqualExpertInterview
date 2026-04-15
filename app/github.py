import requests

GITHUB_API_URL = "https://api.github.com"

def get_user_gists(username: str):
    url = f"{GITHUB_API_URL}/users/{username}/gists"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"GitHub API error: {response.status_code}")

    data = response.json()

    # Extract relevant fields
    gists = []
    for gist in data:
        gists.append({
            "id": gist["id"],
            "description": gist["description"],
            "url": gist["html_url"],
            "files": list(gist["files"].keys())
        })

    return gists
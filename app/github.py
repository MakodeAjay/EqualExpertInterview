import requests

# Base URL for GitHub API
GITHUB_URL = "https://api.github.com"

def fetch_gists(username: str, page: int = 1, per_page: int = 10):
    """
    Fetch public gists for a given GitHub user with pagination.

    Args:
        username (str): GitHub username
        page (int): Page number
        per_page (int): Results per page

    Returns:
        list: List of gists
    """
    url = f"{GITHUB_URL}/users/{username}/gists"

    params = {
        "page": page,
        "per_page": per_page
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception(f"GitHub API failed with status: {response.status_code}")

    gists_data = response.json()

    result = []
    for gist in gists_data:
        result.append({
            "id": gist["id"],
            "description": gist["description"],
            "url": gist["html_url"],
            "files": list(gist["files"].keys())
        })

    return result
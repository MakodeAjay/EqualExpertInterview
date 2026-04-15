import requests

GITHUB_URL = "https://api.github.com"


def fetch_gists(username: str):
    """
    Fetch public gists for a given GitHub user.

    Args:
        username (str): GitHub username

    Returns:
        list: List of gists with selected fields (id, description, url, files)

    Raises:
        Exception: If GitHub API request fails
    """
    url = f"{GITHUB_URL}/users/{username}/gists"

    response = requests.get(url)

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
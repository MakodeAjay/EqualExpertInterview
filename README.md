## :warning: Please read these instructions carefully and entirely first
* Clone this repository to your local machine.
* Use your IDE of choice to complete the assignment.
* When you have completed the assignment, you need to  push your code to this repository and [mark the assignment as completed by clicking here](https://app.snapcode.review/submission_links/db271338-65e9-4b83-8946-bda57653a007).
* Once you mark it as completed, your access to this repository will be revoked. Please make sure that you have completed the assignment and pushed all code from your local machine to this repository before you click the link.

## Operability Take-Home Exercise

Welcome to the start of our recruitment process for Operability Engineers. It was great to speak to you regarding an opportunity to join the Equal Experts network!

Please write code to deliver a solution to the problems outlined below.

We appreciate that your time is valuable and do not expect this exercise to **take more than 90 minutes**. If you think this exercise will take longer than that, I **strongly** encourage you to please get in touch to ask any clarifying questions.

### Submission guidelines
**Do**
- Provide a README file in text or markdown format that documents a concise way to set up and run the provided solution.
- Take the time to read any applicable API or service docs, it may save you significant effort.
- Make your solution simple and clear. We aren't looking for overly complex ways to solve the problem since in our experience, simple and clear solutions to problems are generally the most maintainable and extensible solutions.

**Don't**

Expect the reviewer to dedicate a machine to review the test by:

- Installing software globally that may conflict with system software
- Requiring changes to system-wide configurations
- Providing overly complex solutions that need to spin up a ton of unneeded supporting dependencies. We aspire to keep our dev experiences as simple as possible (but no simpler)!
- Include identifying information in your submission. We are endeavouring to make our review process anonymous to reduce bias.

### Exercise
If you have any questions on the below exercise, please do get in touch and we’ll answer as soon as possible.

#### Build an API, test it, and package it into a container
- Build a simple HTTP web server API in any general-purpose programming language[^1] that interacts with the GitHub API and responds to requests on `/<USER>` with a list of the user’s publicly available Gists[^2].
- Create an automated test to validate that your web server API works. An example user to use as test data is `octocat`.
- Package the web server API into a docker container that listens for requests on port `8080`. You do not need to publish the resulting container image in any container registry, but we are expecting the Dockerfile in the submission.
- The solution may optionally provide other functionality (e.g. pagination, caching) but the above **must** be implemented.

__________________________________________
[^1]: For example Go, Python or Ruby but not Bash or Powershell.  
[^2]: https://docs.github.com/en/rest/gists/gists?apiVersion=2022-11-28



# GitHub Gists API

A minimal HTTP API that returns publicly available GitHub Gists for a given user.

---

## 🚀 Overview

This service exposes a single endpoint: **GET /{username}**

It fetches public gists for the given GitHub user using the GitHub REST API.

Example: **GET /octocat**

---
## 🚀 Features

* Fetch public gists for any GitHub user
* Clean REST API using FastAPI
* Automated test using Pytest
* Dockerized application
* Runs securely as a non-root user

---

## 📦 Project Structure

```
.
├── app/
│   ├── main.py        # API routes
│   ├── github.py      # GitHub API integration
├── tests/
│   ├── test_api.py    # Automated tests
├── requirements.txt
├── Dockerfile         # Multi-stage build (non-root user)
├── .dockerignore      # Excludes unnecessary files from image
```


---

## ⚙️ Prerequisites

* Python 3.11+
* pip
* Docker (optional, for containerized run)

---

## 🧰 Requirements

Only **one** of the following is required:

* Docker (recommended)
  **OR**
* Python 3.11+

No global system configuration changes are required.

---

## ▶️ Running Locally (Without Docker)

### 1. Clone the repository

```
git clone <repo-url>
cd equal-experts-adept-practical-authentic-intelligence-4d3bc322cc2d
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Start the server

```
uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
```

### 4. Access API

```
http://localhost:8080/octocat
```

---

## 🧪 Running Tests

```
pytest

This includes a test using the sample GitHub user:

octocat
```

---

## 🐳 Run with Docker (Recommended)

### 1. Build the image

```
docker build -t github-gists-api .
```

### 2. Run the container

```
docker run -p 8080:8080 github-gists-api
```

### 3. Access API

```
http://localhost:8080/octocat
```

---

## 🔐 Security

* The container runs as a **non-root user (`appuser`)**
* Minimizes security risks in containerized environments

---

## 📌 API Endpoint

### GET /{username}

Fetch public gists for a GitHub user.

#### Example:

```
GET /octocat
```

#### Response:

```
{
  "user": "octocat",
  "gists": [
    {
      "id": "123",
      "description": "Example gist",
      "url": "https://gist.github.com/...",
      "files": ["file1.txt"]
    }
  ]
}
```
---

## 🔐 Notes

* The Docker container runs as a non-root user
* No external services or dependencies are required
* The solution is intentionally minimal and easy to run

---

## ⚡ Improvements (Future Scope)

* Add pagination support
* Add caching (Redis)
* Add GitHub API authentication (token)
* Add rate limiting & retries
* CI/CD pipeline integration

---

## 📚 Reference

* GitHub Gists API:
  https://docs.github.com/en/rest/gists/gists?apiVersion=2022-11-28

---

## 👨‍💻 Author

Ajay Makode

---

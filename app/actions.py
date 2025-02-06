# actions.py

import os
from flask import request, render_template
import requests

# Retrieve GitHub Personal Access Token, owner, and repo list from environment variables
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_API_URL = "https://api.github.com"
OWNER = os.getenv("owner")

def get_actions():
    repo = request.form.get('repo')

    if not repo:
        return "Repository name is required!", 400

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
    }

    url = f"{GITHUB_API_URL}/repos/{OWNER}/{repo}/actions/runs"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        runs = response.json().get('workflow_runs', [])
        return render_template('dashboard.html', runs=runs, repo=f"{OWNER}/{repo}")
    else:
        return f"Error: Unable to fetch actions for {OWNER}/{repo}. Status Code: {response.status_code}"
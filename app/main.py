import os
from flask import Flask, render_template
from dotenv import load_dotenv
from actions import get_actions

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Retrieve GitHub Personal Access Token, owner, and repo list from environment variables
OWNER = os.getenv("owner")
REPO_LIST = os.getenv("repo_list").split(',')

@app.route('/')
def home():
    return render_template('index.html', owner=OWNER, repos=REPO_LIST)

@app.route('/actions', methods=['POST'])
def actions_route():
    return get_actions()


if __name__ == '__main__':
    app.run(debug=True)
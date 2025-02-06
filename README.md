# GitHub Actions Dashboard

GitHub Actions Dashboard is a Flask-based web application that allows users to view the gitHub Actions runs of their GitHub repositories. The application retrieves data from the GitHub API and displays it in a user-friendly dashboard.

## Features

- View workflow runs for selected GitHub repositories from the dropdown
- User-friendly interface with a dropdown to select repositories
- Detailed information about each workflow run

## Prerequisites

- Python 3.10
- GitHub Personal Access Token with `repo` and `workflow` scopes

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/github-actions-board.git
    cd github-actions-board
    ```

2. Create a `.env` file in the root directory and add your GitHub Personal Access Token and repository owner:

    ```env
    GITHUB_TOKEN=your_github_token
    owner=your_github_username
    repo_list=repo1,repo2,repo3
    ```

3. Build and run the Docker container:

    ```sh
    docker build -t github-actions-board .
    docker run -p 5000:5000 --env-file .env github-actions-board
    ```

4. Open your browser and navigate to `http://localhost:5000`.

## Usage

1. On the home page, select a repository from the dropdown list.
2. Click the "View Actions" button to view the workflow runs for the selected repository.
3. The dashboard will display the workflow runs with links to view details on GitHub.

## Project Structure

- `app/`: Contains the Flask application code
  - `actions.py`: Handles the logic for fetching workflow runs from the GitHub API
  - `main.py`: Initializes the Flask app and defines routes
  - `templates/`: Contains HTML templates for the application
    - `dashboard.html`: Template for displaying workflow runs
    - `index.html`: Template for the home page
- `requirements.txt`: Lists the Python dependencies
- `Dockerfile`: Defines the Docker image for the application
- `.gitignore`: Specifies files and directories to be ignored by Git

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

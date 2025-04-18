import os
import subprocess

# Correct the BASE_PROJECT_DIR to ensure no path duplication
BASE_PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))

def upload_to_github(project_path, data):
    repo_name = data.get('repo_name')
    github_token = data.get('github_token')

    if not repo_name or not github_token:
        return {"success": False, "message": "Missing repo name or GitHub token."}

    # Make full absolute path for the project
    full_project_path = os.path.join(BASE_PROJECT_DIR, project_path)

    try:
        if not os.path.exists(full_project_path):
            return {"success": False, "message": f"Project path does not exist: {full_project_path}"}

        os.chdir(full_project_path)

        subprocess.run(["git", "init"], check=True)
        subprocess.run(["git", "add", "."], check=True)

        # Check if there are files to commit
        status_result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        if status_result.stdout.strip():
            subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)
        else:
            print("Nothing to commit, skipping git commit.")

        # Remove the existing remote 'origin' if it exists
        subprocess.run(["git", "remote", "remove", "origin"], check=True)

        # Add the new remote URL with the provided GitHub token
        repo_url = f"https://{github_token}@github.com/aayush598/{repo_name}.git"
        subprocess.run(["git", "remote", "add", "origin", repo_url], check=True)

        subprocess.run(["git", "branch", "-M", "main"], check=True)
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)

        return {"success": True, "message": "Project uploaded successfully."}

    except subprocess.CalledProcessError as e:
        return {"success": False, "message": f"Git error: {e}"}
    except Exception as e:
        return {"success": False, "message": str(e)}

import os
import sqlite3
import zipfile
from datetime import datetime

DATABASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database', 'database.db'))
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

def fetch_projects_from_db():
    """Fetch project names from the database"""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT project_name FROM projects")  # Assuming your table name is 'projects'
    projects = [row[0] for row in cursor.fetchall()]
    conn.close()
    return projects

def zip_project(data):
    project_name = data.get('project_name')
    if not project_name:
        return {"status": "error", "message": "No project name provided"}

    projects_folder = os.path.join(PROJECT_ROOT, 'generated_projects')
    project_folder = os.path.join(projects_folder, project_name)
    if not os.path.exists(project_folder):
        return {"status": "error", "message": "Project not found"}

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    zip_folder = os.path.join(PROJECT_ROOT, 'generated_zips')
    os.makedirs(zip_folder, exist_ok=True)
    zip_filename = f"{project_name}_{timestamp}.zip"
    zip_path = os.path.join(zip_folder, zip_filename)

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(project_folder):
            for file in files:
                abs_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(abs_file_path, project_folder)
                zipf.write(abs_file_path, arcname=relative_path)

    return {"status": "success", "zip_path": zip_path}

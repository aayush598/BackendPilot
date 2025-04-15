import sqlite3
import os
from datetime import datetime

# Path to the SQLite database (assuming it's in the `database` folder)
DB_PATH = os.path.join(os.path.dirname(__file__), 'database.db')

def get_db_connection():
    """Creates and returns a connection to the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Allow column access by name
    return conn

def create_project_table():
    """Creates the table to store project data if it doesn't exist."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_name TEXT NOT NULL,
            description TEXT NOT NULL,
            folder_structure TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insert_project_data(project_name, description, folder_structure):
    """Inserts the project data into the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Get the current timestamp
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO projects (project_name, description, folder_structure, created_at)
        VALUES (?, ?, ?, ?)
    """, (project_name, description, folder_structure, created_at))

    conn.commit()
    conn.close()

def get_all_projects():
    """Fetches all projects from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM projects")
    projects = cursor.fetchall()
    conn.close()
    return projects

from models import create_project_table

def initialize_database():
    """Initializes the SQLite database and creates tables."""
    create_project_table()
    print("Database initialized and table created.")

initialize_database()
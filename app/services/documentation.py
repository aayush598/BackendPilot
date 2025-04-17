import json
from app.database.models import get_project_by_name
from app.utils.logger import log_info, log_error
from app.utils.qroq_api import generate_with_qroq  # Import Groq's API function

def generate_documentation(project_name: str) -> dict:
    try:
        # Fetch project from the database
        project = get_project_by_name(project_name)

        if not project:
            return {"success": False, "error": f"Project '{project_name}' not found in database."}

        description = project["description"] or "None"
        folder_structure = project["folder_structure"] or "None"

        # Create a prompt for the Groq API to generate detailed documentation
        prompt = f"""
        You are a software documentation assistant. Based on the following project information, generate detailed and professional documentation for the project:

        Project Name: {project_name}
        Description: {description}
        Folder Structure: {folder_structure}

        The documentation should include:
        - Project overview
        - Key components and their functionality
        - Folder structure and the purpose of key directories
        - Any additional information that can help developers understand the project
        """

        # Get the AI-generated documentation using Groq
        doc = generate_with_qroq(prompt)

        if doc.startswith("[Groq API Error]"):
            return {"success": False, "error": doc}  # Return error from Groq API

        log_info(f"Documentation generated for project: {project_name}")
        return {"success": True, "documentation": doc.strip()}

    except Exception as e:
        log_error(f"Documentation Generation Error: {str(e)}")
        return {"success": False, "error": str(e)}

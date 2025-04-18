import os
from app.services.project_scaffold import generate_project_structure
from app.services.zipping import zip_project
from app.utils.logger import log_info, log_error
import urllib.parse

def one_step_solution(data):
    try:
        # Get project name and description from input data
        project_name = data.get('project_name')
        description = data.get('description')

        # Validate inputs
        if not project_name or not description:
            return {"success": False, "message": "Missing project_name or description"}

        # Step 1: Generate project structure
        project_result = generate_project_structure(project_name, description)
        
        # Check if the project structure generation was successful
        if not project_result.get("success"):
            return {"success": False, "message": "Failed to generate project structure"}
        
        log_info(f"Project structure for '{project_name}' created successfully at {project_result['path']}")

        # Step 2: Zip the project
        zip_result = zip_project({"project_name": project_name})

        # Check if the zipping process was successful
        if not zip_result.get("success"):
            return {"success": False, "message": "Failed to zip the project"}

        log_info(f"Project '{project_name}' zipped successfully at {zip_result['zip_path']}")

        # Extract filename from zip path
        zip_filename = zip_result["zip_path"].split('/')[-1]

        # Create the download link for the zip file
        download_link = f"/api/download/{urllib.parse.quote(zip_filename)}"

        # Return the success response with zip path and download link
        return {
            "success": True,
            "zip_path": zip_result["zip_path"],
            "project_path": project_result["path"],
            "download_link": download_link
        }

    except Exception as e:
        # Log the error and return the failure response
        log_error(f"One step solution error: {str(e)}")
        return {"success": False, "message": str(e)}

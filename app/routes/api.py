from flask import Blueprint, request, jsonify

api_bp = Blueprint("api", __name__)

@api_bp.route("/generate", methods=["POST", "GET"])
def generate_backend():
    data = request.json
    project_name = data.get("project_name")
    description = data.get("description")

    # TODO: Add service logic to generate backend
    return jsonify({
        "message": "Backend generation started.",
        "project": project_name,
        "status": "pending"
    })

@api_bp.route("/status/<project_name>")
def check_status(project_name):
    # TODO: Check log or metadata to return status
    return jsonify({
        "project": project_name,
        "status": "completed"
    })

from flask import Blueprint, request, jsonify
from app.services import (
    project_scaffold,
    prompt_generator,
    code_generator,
    tester,
    fixer,
    linter,
    commenter,
    documentation,
    zipping,
    github_uploader,
    render_deployer,
)
import os

api = Blueprint('api', __name__, url_prefix="/api")

@api.route('/create_project', methods=['POST'])
def create_project():
    data = request.json
    result = project_scaffold.create_project_structure(data)
    return jsonify(result)

@api.route('/generate_structure', methods=['POST'])
def generate_structure():
    data = request.get_json()
    project_name = data.get("project_name")
    description = data.get("description")

    if not project_name or not description:
        return jsonify({"success": False, "error": "Missing project_name or description"}), 400

    result = project_scaffold.generate_project_structure(project_name, description)
    return jsonify(result)

@api.route('/generate_prompts', methods=['POST'])
def generate_prompts():
    data = request.json
    result = prompt_generator.generate_prompt(data)
    return jsonify(result)

@api.route('/generate_code', methods=['POST'])
def generate_code():
    data = request.json
    result = code_generator.generate_code(data)
    return jsonify(result)

@api.route('/test_project', methods=['POST'])
def test_project():
    data = request.json
    result = tester.run_tests(data)
    return jsonify(result)

@api.route('/fix_errors', methods=['POST'])
def fix_errors():
    data = request.json
    result = fixer.fix_errors(data)
    return jsonify(result)

@api.route('/lint_code', methods=['POST'])
def lint_code():
    data = request.json
    result = linter.lint_code(data)
    return jsonify(result)

@api.route('/comment_code', methods=['POST'])
def comment_code():
    data = request.json
    result = commenter.comment_code_for_readability(data)
    return jsonify(result)

@api.route('/generate_documentation', methods=['POST'])
def generate_doc_api():
    data = request.get_json()
    project_name = data.get("project_name")
    if not project_name:
        return jsonify({"success": False, "error": "No project name provided."})

    result = documentation.generate_documentation(project_name)
    return jsonify(result)

@api.route('/zip_project', methods=['POST'])
def zip_project():
    data = request.json
    result = zipping.zip_project(data)
    return jsonify(result)

@api.route('/get_projects', methods=['GET'])
def get_projects():
    projects = zipping.fetch_projects_from_db()
    return jsonify({"projects": projects})


@api.route('/upload_github', methods=['POST'])
def upload_github():
    try:
        data = request.json
        project_name = data.get('project_name')
        if not project_name:
            return jsonify({"success": False, "message": "Project name missing."}), 400

        project_path = os.path.join('generated_projects', project_name)

        result = github_uploader.upload_to_github(project_path, data)
        return jsonify(result)

    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500



@api.route('/deploy_render', methods=['POST'])
def deploy_render():
    data = "data"
    result = render_deployer.deploy_to_render(data)
    return jsonify(result)

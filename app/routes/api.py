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
    result = commenter.add_comments(data)
    return jsonify(result)

@api.route('/generate_docs', methods=['POST'])
def generate_docs():
    data = request.json
    result = documentation.generate_documentation(data)
    return jsonify(result)

@api.route('/zip_project', methods=['POST'])
def zip_project():
    data = request.json
    result = zipping.zip_project(data)
    return jsonify(result)

@api.route('/upload_github', methods=['POST'])
def upload_github():
    data = request.json
    project_path="project_path"
    result = github_uploader.upload_to_github(project_path,data)
    return jsonify(result)

@api.route('/deploy_render', methods=['POST'])
def deploy_render():
    data = "data"
    result = render_deployer.deploy_to_render(data)
    return jsonify(result)

from flask import Blueprint, render_template

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def index():
    return render_template("index.html")

@home_bp.route("/project-setup")
def project_setup():
    return render_template("project_setup.html")

@home_bp.route("/prompt-preview")
def prompt_preview():
    return render_template("prompt_preview.html")

@home_bp.route("/code-preview")
def code_preview():
    return render_template("code_preview.html")

@home_bp.route("/testing-linting")
def testing_linting():
    return render_template("testing_linting.html")

@home_bp.route("/error-handling")
def error_handling():
    return render_template("error_handling.html")

@home_bp.route("/documentation")
def documentation():
    return render_template("documentation.html")

@home_bp.route("/final-preview")
def final_preview():
    return render_template("final_preview.html")

@home_bp.route("/upload-to-github")
def upload_to_github():
    return render_template("upload_to_github.html")

@home_bp.route("/deploy-render")
def deploy_render():
    return render_template("deploy_render.html")

@home_bp.route("/logs")
def logs():
    return render_template("logs.html")

@home_bp.route("/step-by-step")
def step_by_step():
    return render_template("step_by_step_mode.html")

@home_bp.route("/one-step")
def one_step():
    return render_template("one_step_mode.html")

# Error pages
@home_bp.app_errorhandler(404)
def page_not_found(e):
    return render_template("error_404.html"), 404

@home_bp.app_errorhandler(500)
def internal_error(e):
    return render_template("error_500.html"), 500

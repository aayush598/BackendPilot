from flask import Blueprint, render_template, request, redirect, url_for, flash

home = Blueprint('home', __name__)

@home.route('/')
def index():
    return render_template('index.html')

@home.route('/project_setup', methods=['GET', 'POST'])
def project_setup():
    if request.method == 'POST':
        # Collect user input and redirect to prompt preview
        return redirect(url_for('home.prompt_preview'))
    return render_template('project_setup.html')

@home.route('/prompt_preview')
def prompt_preview():
    return render_template('prompt_preview.html')

@home.route('/code_preview')
def code_preview():
    return render_template('code_preview.html')

@home.route('/testing_linting')
def testing_linting():
    return render_template('testing_linting.html')

@home.route('/commenter')
def commenter():
    return render_template('commenter.html')

@home.route('/error_handling')
def error_handling():
    return render_template('error_handling.html')

@home.route('/documentation')
def documentation():
    return render_template('documentation.html')

@home.route('/final_preview')
def final_preview():
    return render_template('final_preview.html')

@home.route('/upload_to_github')
def upload_to_github():
    return render_template('upload_to_github.html')

@home.route('/deploy_render')
def deploy_render():
    return render_template('deploy_render.html')

@home.route('/logs')
def logs():
    return render_template('logs.html')

@home.route('/step_by_step_mode')
def step_by_step_mode():
    return render_template('step_by_step_mode.html')

@home.route('/one_step_mode')
def one_step_mode():
    return render_template('one_step_mode.html')

# Error pages
@home.app_errorhandler(404)
def error_404(e):
    return render_template('error_404.html'), 404

@home.app_errorhandler(500)
def error_500(e):
    return render_template('error_500.html'), 500

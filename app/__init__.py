from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Blueprints
    from app.routes import home_bp, api_bp
    app.register_blueprint(home_bp)
    app.register_blueprint(api_bp, url_prefix="/api")

    return app

import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "default-secret-key")
    QROQ_API_KEY = os.environ.get("QROQ_API_KEY", "")
    SQLALCHEMY_DATABASE_URI = "sqlite:///app/database/database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'generated_projects')
    LOG_FOLDER = os.path.join(os.getcwd(), 'logs')

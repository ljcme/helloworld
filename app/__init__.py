from application import application
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy(application)
login_manager = LoginManager(application)
login_manager.login_view = "login"
login_manager.session_protection = "strong"

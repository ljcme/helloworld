from application import application
from flask_sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, login_required, login_user,\
    logout_user, current_user, UserMixin

db = SQLAlchemy(application)
login_manager = LoginManager(application)
login_manager.login_view = "login"
login_manager.session_protection = "strong"
from flask import Flask
from app.config import config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from FuelSDK.client import ET_Client

# EB looks for an 'application' callable by default.
application = Flask(__name__, template_folder='views')
application.config.from_object(config['dev'])

db = SQLAlchemy(application)
login_manager = LoginManager(application)
login_manager.login_view = "login"
login_manager.session_protection = "strong"

et_client = ET_Client()

from app.routes import routes

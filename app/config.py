import os


basedir = os.path.abspath(os.path.dirname(__file__))



class Auth:
    CLIENT_ID = '460082845174-bcfb6rgd5usnbhma8euofjfp344jabfm.apps.googleusercontent.com'
    CLIENT_SECRET = 'V0oQX_VGdaqadeDu6-eykM4H'
    REDIRECT_URI = 'https://mosaic-dev.d7ixpw8mqn.us-west-2.elasticbeanstalk.com/oauth2callback'
    AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
    TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
    USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'
    SCOPE = ['profile', 'email']



class Config:
    APP_NAME = 'Test Google Login'
    SECRET_KEY = os.environ.get("SECRET_KEY") or "somethingsecret"


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "test.db")


class ProdConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "prod.db")


config = {
    "dev": DevConfig,
    "prod": ProdConfig,
    "default": DevConfig
}

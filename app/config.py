import os


basedir = os.path.abspath(os.path.dirname(__file__))



class Auth:
    CLIENT_ID = '460082845174-bcfb6rgd5usnbhma8euofjfp344jabfm.apps.googleusercontent.com'
    CLIENT_SECRET = 'V0oQX_VGdaqadeDu6-eykM4H'
    REDIRECT_URI = 'https://127.0.0.1:5000/oauth2callback'
    AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
    TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
    USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'
    SCOPE = ['profile', 'email']


class ET_Auth:
    FUELSDK_CLIENT_ID = '0b1evzoz7mqnoavzdy08kh34'
    FUELSDK_CLIENT_SECRET = 'xnvEvk5XoZKITDIfcSZTZ593'
    FUELSDK_DEFAULT_WSDL = 'https://webservice.exacttarget.com/etframework.wsdl'
    FUELSDK_AUTH_URL = 'https://auth.exacttargetapis.com/v1/requestToken?legacy=1'


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

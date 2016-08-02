from .. import application
from .. import login_required, current_user
from ..config import Auth
from flask import render_template, redirect, session, url_for
from requests_oauthlib import OAuth2Session

@application.route('/')
@login_required
def index():
    return render_template('index.html')

@application.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    google = get_google_auth()
    auth_url, state = google.authorization_url(
        Auth.AUTH_URI, access_type='offline'
    )
    session['oauth_state'] = state
    return render_template('login.html', auth_url=auth_url)

def get_google_auth(state=None, token=None):
    if token:
        return OAuth2Session(Auth.CLIENT_ID, token=token)
    if state:
        return OAuth2Session(
            Auth.CLIENT_ID,
            state=state,
            redirect_uri=Auth.REDIRECT_URI
        )
    oauth = OAuth2Session(
        Auth.CLIENT_ID,
        redirect_uri=Auth.REDIRECT_URI,
        scope=Auth.SCOPE
    )
    return oauth
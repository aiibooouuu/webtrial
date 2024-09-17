from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>Logged in</p>"

@auth.route('/logout')
def logout():
    return "<p>Logged out</p>"

@auth.route("/sign-up")
def sign_up():
    return "<p>Sign up</p>"
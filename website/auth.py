from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login-student')
def login():
    return render_template("l1.html")

@auth.route('/login-instructor')
def login():
    return render_template('l2.html')

@auth.route('/logout')
def logout():
    return "<p>Logged out</p>"

@auth.route("/sign-up")
def sign_up():
    return "<p>Sign up</p>"
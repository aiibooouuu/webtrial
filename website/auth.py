from flask import Blueprint, render_template, flash, redirect, url_for
from website.forms import RegistrationForm , LoginForm # Assuming RegistrationForm is the class in forms.py


auth = Blueprint('auth', __name__)

@auth.route('/login-student', methods=['POST', 'GET'])
def login_student():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Account logged in for {form.email.data}!', 'success')
        return redirect(url_for('views.std_dashboard'))
    return render_template("student-login.html", count=128, form=form)

@auth.route('/register-student', methods=['POST', 'GET'])
def register_student():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.email.data}!', 'success')
        return redirect(url_for('views.std_dashboard'))
    return render_template('student-registration.html', count=128, form=form)

@auth.route('/login-instructor')
def login_instructor():
    return render_template('l2.html')

@auth.route('/logout')
def logout():
    return "<p>Logged out</p>"

@auth.route("/sign-up")
def sign_up():
    return "<p>Sign up</p>"
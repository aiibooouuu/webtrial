from flask import Blueprint, render_template
from website.forms import RegistrationForm  # Assuming RegistrationForm is the class in forms.py


auth = Blueprint('auth', __name__)

@auth.route('/login-student')
def login_student():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("login-layout.html", count=128, form=form)

@auth.route('/login-instructor')
def login_instructor():
    return render_template('l2.html')

@auth.route('/logout')
def logout():
    return "<p>Logged out</p>"

@auth.route("/sign-up")
def sign_up():
    return "<p>Sign up</p>"
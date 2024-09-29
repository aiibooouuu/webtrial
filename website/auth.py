from flask import Blueprint, render_template, flash, redirect, url_for
from website.forms import RegistrationForm , LoginForm # Assuming RegistrationForm is the class in forms.py
from website import db
from website.models import User

auth = Blueprint('auth', __name__)

@auth.route('/login-student', methods=['POST', 'GET'])
def login_student():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()

        if user and user.password == password:
            flash('Login Successful', 'success')
            return redirect(url_for('views.std_dashboard'))
        else:
            flash('Login failed. Please check email or password', 'danger')
    return render_template("student-login.html", count=128, form=form)

@auth.route('/register-student', methods=['POST', 'GET'])
def register_student():
    form = RegistrationForm()
    print(form.email.data)
    print(form.password.data)
    print(form.confirm_password.data)
    print(f'The form validated for registration : {form.validate_on_submit()}')
    if form.validate_on_submit():
        new_user = User(email=form.email.data, password=form.password.data)
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('views.std_dashboard'))
            flash('Account Created Successfully', 'success')
        except Exception as e:
            db.session.rollback()  # Rollback the session on error
            print(f"Error occurred: {e}")  # Log the error to console
            flash('An error occurred. Please try again.', 'danger')

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
from flask import Blueprint, render_template, flash, redirect, url_for, session
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
            session['user_id'] = user.id
            flash('Login Successful', 'success')
            return redirect(url_for('views.std_dashboard'))
        else:
            flash('Login failed. Please check email or password', 'danger')
    return render_template("student-login.html", count=128, form=form)

@auth.route('/logout', methods=['POST', 'GET'])
def logout():
    session.clear()  
    flash('You have been logged out successfully.', 'success')  # Optional flash message
    return redirect(url_for('auth.login_student'))  # Redirect to the login page


@auth.route('/register-student', methods=['POST', 'GET'])
def register_student():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        try:
            db.session.add(new_user)
            db.session.commit()
            
            # Save user_id in session after successful registration
            session['user_id'] = new_user.id

            flash('Account Created Successfully', 'success')
            return redirect(url_for('views.std_dashboard'))
        except Exception as e:
            db.session.rollback()  # Rollback the session on error
            print(f"Error occurred: {e}") 
            flash('An error occurred. Please try again.', 'danger')
    
    return render_template('student-registration.html', count=128, form=form)


@auth.route('/login-instructor', methods=['POST', 'GET'])
def login_instructor():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('views.inst_dashboard'))

    return render_template('instructor-login.html', count=128, form=form)

@auth.route('/register-instructor', methods=['POST','GET'])
def register_instructor():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('views.inst_dashboard'))
    
    return render_template('instructor-registration.html', count=128, form=form)


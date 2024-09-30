from flask import Blueprint, render_template, session, flash
from website.forms import RegistrationForm, LoginForm
from website.models import User, Instructor
from datetime import datetime

views = Blueprint('views', __name__)

@views.route('/')
def home():
    session.pop('usre_id', None)
    flash('You have been logged out due to navigation', 'danger')
    return render_template("home.html")

@views.route('/student-dashboard')
def std_dashboard():
    user_id = session.get('user_id')  # Fetch user ID from session
    
    if user_id is None:
        flash('User not found in session', 'danger')
        return redirect(url_for('auth.login_student'))
    
    user = User.query.get(user_id)  # Fetch the user from the database using user_id
    
    if user:
        user_username = user.username
    else:
        user_username = "User not found"
    
    return render_template('student-dashboard.html', title="Welcome Student", user_username=user_username)

@views.route('/instructor-dashboard')
def inst_dashboard():
    return render_template('instructor-dashboard.html', title="Welcome Instructor")

@views.route('/student-courses')
def student_courses():
    return render_template('student-courses.html', title="Available Courses")

@views.route('/student-mentors')
def student_mentors():
    return render_template('student-mentors.html', title="Student Mentors")

@views.route('/student-roadmap')
def student_roadmap():
    return render_template('roadmap_html/index.html', title='Roadmap')
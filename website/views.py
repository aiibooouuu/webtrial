from flask import Blueprint, render_template, session
from website.forms import RegistrationForm, LoginForm

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/student-dashboard')
def std_dashboard():
    form = LoginForm()
    user_email = session.get('user_email', 'Student')
    return render_template('student-dashboard.html', title="Welcome Student", form=form, user_email=user_email)

@views.route('/instructor-dashboard')
def inst_dashboard():
    return render_template('instructor-dashboard.html', title="Welcome Instructor")

@views.route('/student-courses')
def student_courses():
    return render_template('student-courses.html', title="Available Courses")

@views.route('/student-mentors')
def student_mentors():
    return render_template('student-mentors.html', title="Student Mentors")
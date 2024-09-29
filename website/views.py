from flask import Blueprint, render_template, session
from website.forms import RegistrationForm, LoginForm
from website.models import User

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/student-dashboard')
def std_dashboard():
    user_id = session.get('user_id')  # Fetch user ID from session
    user = User.query.get(user_id)     # Get user from the database
    
    if user:
        user_email = user.email
    else:
        user_email = "User not found"
    return render_template('student-dashboard.html', title="Welcome Student", user_email=user_email)

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
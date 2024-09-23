from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/student-dashboard')
def std_dashboard():
    return render_template('stddashboard.html')

@views.route('/instructor-dashboard')
def inst_dashboard():
    return render_template('instdashboard.html')

@views.route('/student-courses')
def student_courses():
    return render_template('avlblcourses.html')

@views.route('/student-mentors')
def student_mentors():
    return render_template('mentor.html')
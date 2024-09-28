from flask import Flask, render_template, redirect, url_for, session, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
import bcrypt
from flask_mysqldb import MySQL
from flask_login import login_user, login_required, logout_user, current_user

from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'WELCOMEGAGA@238'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'sihfinaldb'

mysql = MySQL(app)

class RegisterstdForm(FlaskForm):
    username = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Register")

    def validate_email(self, field):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email=%s", (field.data,))

        user = cursor.fetchone()
        cursor.close()
        if user:
            raise ValidationError("Email Already Taken.")
        
    def validate_password2(self, field):
        if field.data != self.password.data:
            raise ValidationError("Passwords do not match.")

class RegisterinstForm(FlaskForm):
    username = StringField("Name", validators=[DataRequired()])
    id = StringField("ID", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Register")

    def validate_email(self, field):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email=%s", (field.data,))
        user = cursor.fetchone()
        cursor.close()
        if user:
            raise ValidationError("Email Already Taken.")

    def validate_password2(self, field):
        if field.data != self.password.data:
            raise ValidationError("Passwords do not match.")
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    username=StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

        
     

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/student-dashboard')
def std_dashboard():
    return render_template('student-dashboard.html', title="Welcome Student")

@app.route('/instructor-dashboard')
def inst_dashboard():
    return render_template('instructor-dashboard.html', title="Welcome Instructor")

@app.route('/student-courses')
def student_courses():
    return render_template('student-courses.html', title="Available Courses")

@app.route('/student-mentors')
def student_mentors():
    return render_template('student-mentors.html', title="Student Mentors")

@app.route("/roadmap")
def roadmap():
    return render_template('roadmap.html', title="RoadMap")

# Authentication Routes
@app.route('/login-student')
def login_student():
    return render_template("l1.html")

@app.route('/login-instructor')
def login_instructor():
    return render_template('l2.html')

@app.route('/logout')
def logout():
    session.clear()  # Clear session on logout
    return redirect(url_for('home'))

@app.route("/sign-up")
def sign_up():
    return "<p>Sign up</p>"

@app.route('/register', methods=['GET','POST'])  # Register for student
def register():
    form = RegisterstdForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            email = form.email.data
            password = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt())
            session['username']= username
            
            cursor = mysql.connection.cursor()
            try:
                cursor.execute("INSERT INTO users (username, email, password, role) VALUES (%s, %s, %s, %s)",
                               (username, email, password, 'student'))  # Set role as student
                mysql.connection.commit()
                flash('Registration successful!', 'success')
                return redirect(url_for('studentdashboard'))
            except Exception as e:
                mysql.connection.rollback()  # Rollback in case of error
                flash('Registration failed. Please try again.', 'danger')
                print(f"Error: {e}")
            finally:
                cursor.close()
        else:
            print(form.errors)  # Print errors if validation fails
            
    return render_template('register.html', form=form)


@app.route('/registerinst', methods=['GET', 'POST'])
def registerinst():
    form = RegisterinstForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        id = form.id.data  # This is the ID from the form
        session['username'] = form.username.data
        password = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt())

        cursor = mysql.connection.cursor()
        try:
            cursor.execute("INSERT INTO users (username, email, password, role) VALUES (%s, %s, %s, %s)",
                           (username, email, password, 'instructor'))  # Set role as instructor
            mysql.connection.commit()
            flash('Registration successful!', 'success')
            return redirect(url_for('instructordashboard'))
        except Exception as e:
            mysql.connection.rollback()  # Rollback in case of error
            flash('Registration failed. Please try again.', 'danger')
            print(f"Error: {e}")
        finally:
            cursor.close()
    
    return render_template('registerinst.html', form=form)



@app.route('/signininst', methods=['GET', 'POST'])
def signininst():
    form = LoginForm()
    if form.validate_on_submit() and request.method == 'POST':
        email = form.email.data
        
        password = form.password.data
        

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
        user = cursor.fetchone()  # Fetch the user record

        if user:
            if bcrypt.checkpw(password.encode('utf-8'), user[3].encode('utf-8')):  # Compare hashed password
                session['username'] = user[2]  # Assuming username is the second column
                flash('Logged in successfully!', 'success')
                return redirect(url_for('instructordashboard'))
            else:
                flash('Incorrect password, try again.', 'danger')
        else:
            flash('Email does not exist.', 'danger')

    return render_template("signininst.html", form=form)


    

@app.route('/signinstd', methods=['GET', 'POST'])
def signinstd():
    form = LoginForm()
    if form.validate_on_submit() and request.method=='POST':
        email = form.email.data
        password = form.password.data
        
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
        user = cursor.fetchone()  # Fetch the user record

        if user:
            if bcrypt.checkpw(password.encode('utf-8'), user[3].encode('utf-8')):  # Compare hashed password
                session['username'] = user[2]  # Assuming username is the 3 column
                flash('Logged in successfully!', 'success')
                return redirect(url_for('studentdashboard'))
            else:
                flash('Incorrect password, try again.', 'danger')
        else:
            flash('Email does not exist.', 'danger')

    return render_template('signinstd.html', form=form)


@app.route('/studentdashboard')
def studentdashboard():
    username = session.get('username')  # Get username from session
    if not username:
        flash('You need to log in first!', 'danger')
        return redirect(url_for('signininst'))

    return render_template('instructor-dashboard.html', username=username)
    

@app.route('/instructordashboard')
def instructordashboard():
    return render_template('instructor-dashboard.html',username=session['username'])

@app.route('/studentcourses')
def studentcourses():
     username = session.get('username')  # Get username from session
     return render_template('student-courses.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)

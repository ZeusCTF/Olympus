from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    #the 'request' has info that was used to access this root: ie method, url etc
    #this is just accessing the form data being sent
    #data = request.form
    if request.method == 'POST':
        username = request.form.get('userName')
        password = request.form.get('password')
        checkLogin(username,password)
        return redirect(url_for('views.home', user=current_user))

    # the 'text=' portion sets a variable that can then be accessed in the correspondig html code: text='value'
    return render_template("login.html", user=current_user)

def checkLogin(username, password):
    user = User.query.filter_by(username=username).first()
    if user:
        if check_password_hash(user.password, password):
            login_user(user, remember=True)
            flash('Logged in successfully', category='success')
        else:
                flash('Incorrect password', category='error')
    else:
        flash('Username does not exist', category='error')



@auth.route('/logout')
#this makes it so this can only be accessed if the user is logged in
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        #gets info specific to the form submitted
        username = request.form.get('userName')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        
        if user:
            flash('Username already in use', category='error')

        new_user = User(username=username, password=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()

        flash('Account created', category='success')
        
        checkLogin(username, password)
        return redirect(url_for('views.home', user=current_user))
        #we want to login the user, trying to match some stuff from the login function
        #the goal is to login the user as soon as they sign up, maybe we need to redirect directly to the home page?

    elif request.method == 'GET':
        return render_template("signup.html", user=current_user)
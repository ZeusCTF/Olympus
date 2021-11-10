from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    #the 'request' has info that was used to access this root: ie method, url etc
    #this is just accessing the form data being sent
    #data = request.form
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
            else:
                flash('Incorrect password', category='error')
        else:
            flash('Username does not exist', category='error')

    # the 'text=' portion sets a variable that can then be accessed in the correspondig html code: text='value'
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return 

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
        return redirect(url_for('views.home'))



    return render_template("signup.html")

from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    # the 'text=' portion sets a variable that can then be accessed in the correspondig html code
    return render_template("login.html", text="Testing")

@auth.route('/logout')
def logout():
    return 

@auth.route('/sign-up')
def sign_up():
    return render_template("signup.html")

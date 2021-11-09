from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    #the 'request' has info that was used to access this root: ie method, url etc
    #this is just accessing the form data being sent
    #data = request.form

    # the 'text=' portion sets a variable that can then be accessed in the correspondig html code
    return render_template("login.html", text="Testing")

@auth.route('/logout')
def logout():
    return 

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        #gets info specific to the form submitted
        username = request.form.get('userName')
        password = request.form.get('password')

    return render_template("signup.html")

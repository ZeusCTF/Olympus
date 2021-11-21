from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from flask import request
from .models import Passwords
from . import db

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/vault', methods=['GET','POST'])
@login_required
def vault():
    if request.method  == 'POST':
        url = request.form.get('vault_url')
        username = request.form.get('vault_userName')
        password = request.form.get('vault_password')
        
        new_cred = Passwords(url=url, username=username, password=password, user_id=current_user.id)
        db.session.add(new_cred)
        db.session.commit()
        flash('Added to the vault!', category='success')

    return render_template("vault.html", user=current_user)
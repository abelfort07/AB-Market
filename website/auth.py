from flask import Blueprint, flash
from flask import render_template, redirect, url_for
from website.forms import RegisterForm, LoginForm
from website.models import User
from website import db
from flask_login import login_user

auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['GET', 'POST'])
def register_page():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        user_to_create = User(username=register_form.username.data, email=register_form.email.data, password_crypted =register_form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('views.market_page'))
    
    if register_form.errors != {}:
        for err_msg in register_form.errors.values():
            flash(f'There is an error when creating user : {err_msg}', category='danger')
    
    return render_template('register.html', form=register_form )


@auth.route('/login', methods=['GET', 'POST'])
def login_page():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        attempted_user = User.query.filter_by(username=login_form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=login_form.password.data):
            login_user(attempted_user)
            flash(f'Success You are logged in as : {attempted_user.username}', category='success')
            return redirect(url_for('views.market_page'))
        else:
            flash('Username or Password are not matched! Please try again', category='danger')
    
    return render_template('login.html', form=login_form )

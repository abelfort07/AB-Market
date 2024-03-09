from flask import Blueprint, flash
from flask import render_template, redirect, url_for
from website.forms import RegisterForm, LoginForm
from website.models import User
from website import db

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
    return render_template('login.html', form=login_form )

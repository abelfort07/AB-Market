from flask import Blueprint
from flask import render_template
from website.forms import RegisterForm

auth = Blueprint('auth', __name__)

@auth.route('/register')
def register_page():
    register_form = RegisterForm()
    return render_template('register.html', form=register_form )
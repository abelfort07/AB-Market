from flask import Blueprint, render_template
from .models import Items

views = Blueprint('views', __name__)


@views.route('/')
@views.route('/home')
def home_page():
    return render_template('home.html')


@views.route('/market')
def market_page():
    items = Items.query.all()
    return render_template('market.html', items=items)


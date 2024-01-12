from flask import Blueprint, render_template
from .models import ItemsModel
from . import db

views = Blueprint('views', __name__)


@views.route('/')
@views.route('/home')
def home_page():
    return render_template('home.html')


@views.route('/market')
def market_page():
    # items_query = ItemsModel.query.all()
    # print(items_query)
    return render_template('market.html')


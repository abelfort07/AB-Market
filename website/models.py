from . import db


class ItemsModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    barcode = db.Column(db.String(15), unique=True)
    price = db.Column(db.Integer)



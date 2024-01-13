from . import db


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    user_budget = db.Column(db.Integer(), nullable=False, default=10000)
    items = db.relationship('Items', backref='owned_user', lazy=True)
    
    def __repr__(self) -> str:
        return f'User  {self.username}'


class Items(db.Model):
    id = db.Column(db.Integer( ), primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    barcode = db.Column(db.String(15), unique=True, nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(1024), unique=True, nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
    
    def __repr__(self) -> str:
        return f'Item  {self.name}'



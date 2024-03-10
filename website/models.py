from . import db
from . import bcrypt
from website import login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    user_budget = db.Column(db.Integer(), nullable=False, default=10000)
    items = db.relationship('Items', backref='owned_user', lazy=True)
    
    @property
    def password_crypted(self):
        return self.password_crypted
    
    @password_crypted.setter
    def password_crypted(self, plain_text_password):
        self.password = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    
    # check if db encrypted password matched with login form's password
    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password, attempted_password)
        
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



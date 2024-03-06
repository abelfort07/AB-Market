from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired
from website.models import User


class RegisterForm(FlaskForm):
    
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check).first()
    
        if user:
            ...
            
    username = StringField(label='Username : ', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='Email Address : ', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password : ', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password : ', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')   
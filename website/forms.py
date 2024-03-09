from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from website.models import User

# Register Form
class RegisterForm(FlaskForm):
    
    # validate function for username
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists, please try a different username.')
        
    # validate function for email
    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email address already exists, please try a different email.')
         
    username = StringField(label='Username : ', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='Email Address : ', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password : ', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password : ', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')   


# Login Form 
class LoginForm(FlaskForm):
    username = StringField(label='Username : ', validators=[DataRequired()])
    password = PasswordField(label='Password : ', validators=[DataRequired()])
    submit = SubmitField(label='Login')
# -*- encoding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email, DataRequired

# login and registration

class LoginForm(FlaskForm):
    email = StringField('Email',  # Updated field label to 'Email'
                        id='email_login',  # Updated id to 'email_login'
                        validators=[DataRequired(), Email()])  # Added Email validator
    password = PasswordField('Password',
                             id='pwd_login',
                             validators=[DataRequired()])

class UserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    login = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Password')  # This field will be empty on edit
    email = StringField('Email', validators=[DataRequired()])
    admin = StringField('Admin', validators=[DataRequired()])




# -*- encoding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email, DataRequired

# login 

class LoginForm(FlaskForm):
    email = StringField('Email',  
                        id='email_login',  
                        validators=[DataRequired(), Email()])  
    password = PasswordField('Password',
                             id='pwd_login',
                             validators=[DataRequired()])

class UserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    login = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Password')  
    email = StringField('Email', validators=[DataRequired()])
    admin = StringField('Admin', validators=[DataRequired()])




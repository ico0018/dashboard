# -*- encoding: utf-8 -*-

from flask_login import UserMixin
from sqlalchemy.orm import relationship

from apps import db, login_manager
from apps.authentication.util import hash_pass

class Users(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    login = db.Column(db.String(25), unique=True, nullable=False)
    encrypted_password = db.Column(db.String(255), nullable=False)
    salt = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    admin = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, name, login, encrypted_password, salt, email, admin=0):
        self.name = name
        self.login = login
        self.encrypted_password = encrypted_password
        self.salt = salt
        self.email = email
        self.admin = admin

    def is_active(self):
        return True
    
    def set_password(self, password):
        self.password = password

    def verify_password(self, password):
        if self.password == password:
            return True
        else:
            return False

    def __repr__(self):
        return '<User %r>' % self.username


@login_manager.user_loader
def user_loader(id):
    return Users.query.filter_by(id=id).first()

@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')  
    user = Users.query.filter_by(email=email).first()  
    return user if user else None



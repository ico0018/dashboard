# -*- encoding: utf-8 -*-

from flask_login import UserMixin
from sqlalchemy.orm import relationship

from apps import db, login_manager
from apps.authentication.util import hash_pass

class Users(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(64), default='user')
    company = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, password, role='user', company=None, email=None):
        self.username = username
        self.password = password
        self.role = role
        self.company = company
        self.email = email

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
    username = request.form.get('username')
    user = Users.query.filter_by(username=username).first()
    return user if user else None


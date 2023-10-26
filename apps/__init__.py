# -*- encoding: utf-8 -*-

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from importlib import import_module

from flask_admin import Admin

db = SQLAlchemy()
login_manager = LoginManager() 

def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)

def register_blueprints(app):
    for module_name in ('authentication', 'home'):
        module = import_module('apps.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)
        
def register_admin(app):
    from apps.authentication.admin_view import UserAdminView
    from apps.authentication.models import Users
    # Initialize Flask-Admin
    admin = Admin(app, name='Admin', template_mode='bootstrap4')
    admin.add_view(UserAdminView(Users, db.session))

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    register_admin(app)
    return app

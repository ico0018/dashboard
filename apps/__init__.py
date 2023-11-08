# -*- encoding: utf-8 -*-

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask.cli import with_appcontext
from flask_wtf.csrf import CSRFProtect
from importlib import import_module
from sqlalchemy import text

from flask_admin import Admin

import click

db = SQLAlchemy()
login_manager = LoginManager() 

@click.command('init-db')
@with_appcontext
def init_db_command():
    with open('schema.sql', 'r') as f:
        schema = f.read()
        db.session.execute(text(schema))
    click.echo('Database initialized.')

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
    csrf = CSRFProtect(app)
    register_extensions(app)
    register_blueprints(app)
    register_admin(app)
    app.cli.add_command(init_db_command)
    return app

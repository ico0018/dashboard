# -*- encoding: utf-8 -*-
import os

class Config(object):

    basedir = os.path.abspath(os.path.dirname(__file__))

    # Set up the App SECRET_KEY
    SECRET_KEY = os.getenv('SECRET_KEY', 'my-secret-key')

    # Assets Management
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')    

class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # PostgreSQL database
    SQLALCHEMY_DATABASE_URI = 'mysql://debian-sys-maint:JyzkXoKPeruI9oGe@localhost/mydb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DebugConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'mysql://debian-sys-maint:JyzkXoKPeruI9oGe@localhost/mydb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DEBUG = True


# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Debug'     : DebugConfig
}

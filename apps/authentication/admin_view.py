from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect, url_for, flash
from apps.authentication.util import hash_pass
from apps.authentication.forms import UserForm

class UserAdminView(ModelView):

    form = UserForm

    column_list = ('id', 'name', 'login', 'email', 'admin')

    def is_accessible(self):
        return current_user.is_authenticated and current_user.admin == 1  # Updated condition to check if user is admin

    def inaccessible_callback(self, name, **kwargs):
        flash('You do not have permission to access this page.')
        return redirect(url_for('auth.login'))
    
    def on_model_change(self, form, model, is_created):
        if form.password.data:  # Check if password field is not empty
            salt, encrypted_password = hash_pass(form.password.data)
            model.salt = salt
            model.encrypted_password = encrypted_password
        return super(UserAdminView, self).on_model_change(form, model, is_created)
    
class QueryAdminView(ModelView):
    can_create = True  
    can_edit = True  
    can_delete = True 

    column_list = ('id', 'unique_identifier', 'query', 'title', 'description')

    def is_accessible(self):
        return current_user.is_authenticated and current_user.admin == 1  # Updated condition to check if user is admin

    def inaccessible_callback(self, name, **kwargs):
        flash('You do not have permission to access this page.')
        return redirect(url_for('auth.login'))

class UserQueryAdminView(ModelView):
    can_create = True
    can_edit = True
    can_delete = True

    def is_accessible(self):
        return current_user.is_authenticated and current_user.admin == 1  # Updated condition to check if user is admin

    def inaccessible_callback(self, name, **kwargs):
        flash('You do not have permission to access this page.')
        return redirect(url_for('auth.login'))


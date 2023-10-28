from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect, url_for, flash

class UserAdminView(ModelView):
    column_list = ['id', 'name', 'login', 'email', 'admin']  # Updated columns
    form_columns = ['name', 'login', 'encrypted_password', 'salt', 'email', 'admin']  # Updated columns
    column_searchable_list = ['name', 'login', 'email']  # Updated columns
    column_sortable_list = ['id', 'name', 'login', 'email', 'admin']  # Updated columns

    def is_accessible(self):
        return current_user.is_authenticated and current_user.admin == 1  # Updated condition to check if user is admin

    def inaccessible_callback(self, name, **kwargs):
        flash('You do not have permission to access this page.')
        return redirect(url_for('auth.login'))


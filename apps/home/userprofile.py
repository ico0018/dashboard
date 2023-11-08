# -*- encoding: utf-8 -*-

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from apps import db
from apps.authentication.models import Users
from apps.authentication.util import verify_pass, hash_pass
from apps.home import blueprint
from flask import jsonify

@blueprint.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    if request.method == 'POST':
        # 从表单获取密码
        current_password = request.form.get('current_password')
        new_password = request.form.get('new_password')
        confirm_new_password = request.form.get('confirm_new_password')

        # 验证当前密码
        if not verify_pass(current_password, current_user.salt, current_user.encrypted_password):
            return jsonify({'status': 'danger', 'message': '当前密码不正确。'}), 401
        elif new_password != confirm_new_password:
            return jsonify({'status': 'danger', 'message': '新密码和确认密码不匹配。'}), 400
        else:
            # 更新密码
            encrypted_password, salt = hash_pass(new_password)
            current_user.encrypted_password = encrypted_password
            current_user.salt = salt
            db.session.commit()
            return jsonify({'status': 'success', 'message': '您的密码已更新。'}), 200

    # 如果是 GET 请求，显示修改密码的页面
    return render_template('home/user.html')  # 确保这是正确的模板路径

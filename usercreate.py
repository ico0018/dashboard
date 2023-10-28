from run import app, db  # 从 run 模块导入 app 和 db
from apps.authentication.models import Users
from apps.authentication.util import hash_pass

def create_users():
    # 创建普通用户
    normal_user_salt, normal_user_password = hash_pass('normalpassword')
    normal_user = Users(
        name='Normal User',
        login='normaluser',
        encrypted_password=normal_user_password,
        salt=normal_user_salt,
        email='normaluser@example.com',
        admin=0
    )

    # 创建管理员用户
    admin_user_salt, admin_user_password = hash_pass('adminpassword')
    admin_user = Users(
        name='Admin User',
        login='adminuser',
        encrypted_password=admin_user_password,
        salt=admin_user_salt,
        email='adminuser@example.com',
        admin=1
    )

    # 添加用户到数据库
    db.session.add(normal_user)
    db.session.add(admin_user)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():  # 设置应用程序上下文
        create_users()  # 在应用程序上下文中调用 create_users 函数

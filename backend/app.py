from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from user import user_view

# 创建数据库对象
db = SQLAlchemy()

# 创建app
def create_app():
    # 创建flask对象
    app = Flask(__name__)

    # 注册蓝图
    app.register_blueprint(user_view)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
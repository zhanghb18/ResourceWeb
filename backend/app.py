from flask import Flask
from flask_migrate import Migrate
from user import user_view
from models import User,db
from config import *

# 创建app
def create_app():
    # 创建flask对象
    app = Flask(__name__)
    # 配置选项
    app.config.from_object(DevelopmentConfig)
    app.config['SESSION_COOKIE_HTTPONLY']=False
    app.config['SQLALCHEMY_DATABASE_URI'] = DevelopmentConfig.SQLALCHEMY_DATABASE_URI  # 此处的配置填写供外部(非网站后台)调用数据库
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True  # 设置这一项是每次请求结束后都会自动提交数据库中的变动
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_POOL_RECYCLE'] = 1
    app.config['SQLALCHEMY_POOL_TIMEOUT'] = 30
    app.config['SQLALCHEMY_POOL_SIZE'] = 300

    # 初始化数据库
    db.app = app
    db.init_app(app)
    Migrate(app,db)

    # 注册蓝图
    app.register_blueprint(user_view)

    return app

app = create_app()
if __name__ == '__main__':
    app.run()
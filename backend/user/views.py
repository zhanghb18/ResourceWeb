from util.result_wrapper import *
from . import services as user_service
from . import user_view
from models import User,db

@user_view.route('/user/login')
def user_login():
    user_service.user_login()
    user = User()
    user.user_name = '11'
    user.user_passwd = '11111'
    user.user_mail = '11@11.com'
    db.session.add(user)
    db.session.commit()
    return {"code": "0", "msg": "添加成功"}
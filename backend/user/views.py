from util.result_wrapper import *
from . import services as user_service
from . import user_view
from models import User,db
from flask import request

@user_view.route('/user/register',methods=["POST"])
def user_register():
    try:
        input_data = request.form
        user = User()
        user.user_name = input_data['account']
        user.user_mail = input_data['mails']
        user.user_passwd = input_data['passWord']
        db.session.add(user)
        db.session.commit()
        return JSONWrapper.success('注册成功')
    except Exception as e:
        return JSONWrapper.fail(e)

@user_view.route('/user/login',methods=["POST"])
def user_login():
    user_service.user_login()
    user = User()
    user.user_name = '11'
    user.user_passwd = '11111'
    user.user_mail = '11@11.com'
    db.session.add(user)
    db.session.commit()
    return {"code": "0", "msg": "添加成功"}
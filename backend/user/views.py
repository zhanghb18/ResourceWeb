from util.result_wrapper import *
from . import services as user_service
from . import user_view
from models import User,db
from flask import request

@user_view.route('/user/register',methods=["POST"])
def user_register():
    try:
        input_data = request.form
        user_mail = input_data['email']
        user_passwd = input_data['passWord']
        user_pin = input_data['pin']
        statusCode = user_service.user_register(user_mail,user_passwd,user_pin)
        return JSONWrapper.success({'statusCode':statusCode})
    except Exception as e:
        return JSONWrapper.fail(e)

@user_view.route('/user/login',methods=["POST"])
def user_login():
    try:
        input_data = request.form
        user_mail = input_data['email']
        user_passwd = input_data['passWord']
        statusCode = user_service.user_login(user_mail,user_passwd)
        return JSONWrapper.success({'statusCode':statusCode})
    except Exception as e:
        return JSONWrapper.fail(e)

@user_view.route('/user/sendPin',methods=["POST"])
def user_send_pin():
    try:
        input_data = request.form
        email = input_data['email']
        time_interval = user_service.send_pin(email)
        return JSONWrapper.success({'time':time_interval})
    except Exception as e:
        return JSONWrapper.fail(e)
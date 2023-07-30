from util.result_wrapper import *
from . import services as user_service
from . import user_view
from models import User,db
from util.token_utils import decrypt_AES,encrypt_AES
from flask import request
import os

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
        response = user_service.user_login(user_mail,user_passwd)
        return JSONWrapper.success(response)
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
    
@user_view.route('/user/getUserInfo',methods=['GET'])
def get_user_info():
    try:
        token = request.headers.get('token')
        response = user_service.get_info(token)
        return JSONWrapper.success(response)
    except Exception as e:
        return JSONWrapper.fail(e)
    
@user_view.route('/user/changeUserInfo',methods=['POST'])
def change_user_info():
    try:
        input_data = request.form
        token = request.headers.get('token')
        nickname = input_data['userNickName']
        gender = input_data['userGender']
        signature = input_data['userSignature']
        response = user_service.change_info(token,nickname,gender,signature)
        return JSONWrapper.success(response)
    except Exception as e:
        return JSONWrapper.fail(e)

@user_view.route('/user/changeUserPwd',methods=['POST'])
def change_user_pwd():
    try:
        input_data = request.form
        token = request.headers.get('token')
        oldPwd = input_data['oldPwd']
        newPwd = input_data['newPwd']
        response = user_service.change_pwd(token,oldPwd,newPwd)
        return JSONWrapper.success(response)
    except Exception as e:
        return JSONWrapper.fail(e)

@user_view.route('/user/upload_file',methods=['POST'])
def upload_file():
    try:
        token = request.headers.get('token')
        form_data = request.form
        if token is None:
            return JSONWrapper.fail("用户未登录！")
        user_id = decrypt_AES(token)
        user_result = db.session.query(User).filter_by(id=user_id).first()
        if user_result is None:
            return JSONWrapper.fail("用户不存在！")
        # if 'file' in request.files:
        #     file = request.files['file']
        #     filename = form_data['file_name']
        #     file_type = filename.split('.')[1]
        #     file_name = user_id + '.' + file_type
        #     save_path = os.path.join('/home/ubuntu/user_avatar/', file_name)
        #     file.save(save_path)
        #     return JSONWrapper.success("上传成功！")
        # return JSONWrapper.fail("没有文件或上传的文件格式出错！")
        if 'data' in form_data:
            data = form_data['data']
            user_service.upload_file(user_id,data)
            return JSONWrapper.success("上传成功！")
        return JSONWrapper.fail("没有文件或上传的文件格式出错！")
    except Exception as e:
        return JSONWrapper.fail(e)
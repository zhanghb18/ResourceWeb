from flask_mail import Message
import uuid
from models import User,db,PIN
from util.mail_utils import mail
from util.token_utils import decrypt_AES,encrypt_AES
import time 
import sys
import base64,re,os
import uuid

def user_register(email,password,pin):
    pin_result = db.session.query(PIN).filter_by(email=email).first()
    if((time.time()-float(pin_result.send_time)) > 300):
        return 3
    if(pin_result.pin != pin):
        return 2
    user_result = db.session.query(User).filter_by(user_email=email).first()
    if user_result is None:
        user = User()
        user.user_email = email
        user.user_passwd = password
        user.user_nickname = '用户' + str(uuid.uuid1())[:10]
        user.user_gender = 'none'
        db.session.add(user)
        db.session.commit()
        return 0
    else:
        return 1
    
def user_login(user_email,user_passwd):
    try:
        user_result = db.session.query(User).filter_by(user_email=user_email).first()
        response = {}
        if user_result is None:
            response['statusCode'] = 1
            response['token'] = ''
            return response
        if user_passwd != user_result.user_passwd:
            response['statusCode'] = 2
            response['token'] = ''
            return response
        response['statusCode'] = 0
        response['token'] = encrypt_AES(user_result.id)
        return response
    except Exception as e:
        response['statusCode'] = 100
        response['token'] = ''
        return response


def send_pin(email):
    result = db.session.query(PIN).filter_by(email=email).first()
    pin_number = str(uuid.uuid1())[:6] # 随机生成6位验证码
    if result is None:
        pin_data = PIN()
        pin_data.pin = pin_number
        pin_data.email = email
        pin_data.send_time = str(time.time())
        db.session.add(pin_data)
        db.session.commit()
        content = '您的验证码是：%s' % pin_number
    else:
        send_time = result.send_time
        time_interval = time.time()-float(send_time)
        if(time_interval < 60):
            print(time_interval)
            sys.stdout.flush()
            return 60-int(time_interval)
        else:
            result.pin = pin_number
            result.send_time = str(time.time())
            db.session.commit()
        content = '您的验证码是：%s' % pin_number
    send_email('不知名二次元资源站验证码',email,content)
    return 60
    
def send_email(title, email, content):#传入标题，收件人，内容
    msg = Message(title, sender='erc0408@163.com', recipients=[email])  # 发件人，收件人
    msg.html = content
    mail.send(msg)

def get_info(token):
    if(token == ""):
        return ""
    user_id = decrypt_AES(token)
    user_result = db.session.query(User).filter_by(id=user_id).first()
    response = {}
    if user_result is None:
        response['statusCode'] = 1
        return response
    else:
        response['nickname'] = user_result.user_nickname
        response['email'] = user_result.user_email
        response['gender'] = user_result.user_gender
        response['signature'] = user_result.user_signature
        if user_result.user_avatar == None:
            response['avatar'] = ""
        else:
            response['avatar'] = "http://123.56.45.70/user_avatar/" + user_result.user_avatar.split('/')[-1]
        return response

def change_info(token,nickname,gender,signature):
    user_id = decrypt_AES(token)
    user_result = db.session.query(User).filter_by(id=user_id).first()
    response = {}
    if user_result is None:
        response['statusCode'] = 1
        return response
    else:
        user_result.user_nickname = nickname
        user_result.user_gender = gender
        user_result.user_signature = signature
        db.session.commit()
        response['statusCode'] = 0
        return response

def change_pwd(token,oldPwd,newPwd):
    user_id = decrypt_AES(token)
    user_result = db.session.query(User).filter_by(id=user_id).first()
    response = {}
    if user_result is None:
        response['statusCode'] = 1
        return response
    else:
        if user_result.user_passwd == oldPwd:
            user_result.user_passwd = newPwd
            db.session.commit()
            response['statusCode'] = 0
            return response
        else:
            response['statusCode'] = 2
            return response

def upload_file(user_id,data):
    user_result = db.session.query(User).filter_by(id=user_id).first()
    file_data = data.split(",")[-1]
    imgdata = base64.b64decode(file_data)
    save_path = os.path.join('/home/ubuntu/user_avatar/', str(uuid.uuid4())+".jpg")
    file = open(save_path,'wb')
    file.write(imgdata)
    file.close()
    if user_result.user_avatar != None:
        os.remove(user_result.user_avatar)
    user_result.user_avatar = save_path
    db.session.commit()
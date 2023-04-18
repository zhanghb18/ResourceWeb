from flask_mail import Message
import uuid
from models import User,db,PIN
from util.mail_utils import mail
import time 

def user_login(email,password,pin):
    pin_result = db.session.query(PIN).filter_by(email=email).first()
    if((time.time()-float(pin_result.send_time)) > 300):
        return 3
    if(pin_result.pin != pin):
        return 2
    user_result = db.session.query(User).filter_by(email=email).first()
    if user_result is None:
        user = User()
        user.user_mail = email
        user.user_passwd = password
        user.user_name = '用户' + str(uuid.uuid1())[:10]
        db.session.add(user)
        db.session.commit()
        return 0
    else:
        return 1

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
            return int(time_interval)
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
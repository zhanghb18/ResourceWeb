from flask_mail import Message
import uuid
from models import User,db,PIN
from util.mail_utils import mail
import time 

def user_login():
    return "success"

def send_pin(mails):
    result = db.session.query(PIN).filter_by(email=mails).first()
    pin_number = str(uuid.uuid1())[:6] # 随机生成6位验证码
    if result is None:
        pin_data = PIN()
        pin_data.pin = pin_number
        pin_data.email = mails
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
    send_email('不知名二次元资源站验证码',mails,content)
    return 60
    
def send_email(title, email, content):#传入标题，收件人，内容
    msg = Message(title, sender='erc0408@163.com', recipients=[email])  # 发件人，收件人
    msg.html = content
    mail.send(msg)
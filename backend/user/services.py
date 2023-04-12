from flask_mail import Message
import uuid
from models import User,db,PIN
from util.mail_utils import mail

def user_login():
    return "success"

def send_pin(mails):
    pin_number = str(uuid.uuid1())[:6] # 随机生成6位验证码
    pin_data = PIN()
    pin_data.pin = pin_number
    pin_data.email = mails
    db.session.add(pin_data)
    db.session.commit()
    content = '您的验证码是：%s' % pin_number
    send_email('不知名二次元资源站验证码',mails,content)
    
def send_email(title, email, content):#传入标题，收件人，内容
    msg = Message(title, sender='erc0408@163.com', recipients=[email])  # 发件人，收件人
    msg.html = content
    mail.send(msg)
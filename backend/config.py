import configparser
import os

class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Ecy12345!@123.56.45.70/postgres'
    SCHEDULER_TIMEZONE = 'Asia/Shanghai'
    # 发送者邮箱的服务器地址
    MAIL_SERVER = "smtp.163.com"
    MAIL_PORT = '465'
    MAIL_USE_SSL = True
    MAIL_USERNAME = "erc0408@163.com"
    MAIL_PASSWORD = "YNRPIBASWPKMXZYS" # 生成授权码，授权码是开启smtp服务后给出的
    MAIL_DEFAULT_SENDER = "erc0408@163.com"

class DevelopmentConfig(Config):
    DEBUG = True
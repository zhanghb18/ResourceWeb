import configparser
import os

class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@123.56.45.70/postgres'
    SCHEDULER_TIMEZONE = 'Asia/Shanghai'

class DevelopmentConfig(Config):
    DEBUG = True
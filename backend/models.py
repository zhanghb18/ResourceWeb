import uuid
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# 创建数据库对象
db = SQLAlchemy()

class Base(object):
    def to_json(self, transform_date=False):
        json_exclude = getattr(self, '__json_exclude__', set())
        if transform_date:
            self_dict = {}
            for key, value in self.__dict__.items():
                if not key.startswith('_') and key not in json_exclude:
                    if isinstance(value, datetime):
                        self_dict[key] = value.strftime("%Y-%m-%d %H:%M:%S")
                    else:
                        self_dict[key] = value
            return self_dict
        return {key: value for key, value in self.__dict__.items()
                if not key.startswith('_')
                and key not in json_exclude}
    
class User(db.Model, Base):
    __tablename__ = 'users'
    id = db.Column(db.String(32), primary_key=True)
    user_name = db.Column(db.String(50))
    user_passwd = db.Column(db.String(50))
    user_email = db.Column(db.String(50))
    def __repr__(self):
        return '<User %r>' % self.user_name
    def __init__(self):
        self.id = str(uuid.uuid4()).replace("-", "")

class PIN(db.Model, Base):
    __tablename__ = 'pins'
    id = db.Column(db.String(32), primary_key=True)
    email = db.Column(db.String(50))
    pin = db.Column(db.String(6))
    send_time = db.Column(db.String(50))
    def __repr__(self):
        return '<User %r>' % self.user_name
    def __init__(self):
        self.id = str(uuid.uuid4()).replace("-", "")
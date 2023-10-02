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
    user_nickname = db.Column(db.String(50))
    user_passwd = db.Column(db.String(50))
    user_email = db.Column(db.String(50))
    user_avatar = db.Column(db.String(256))
    user_signature = db.Column(db.String(256))
    user_gender = db.Column(db.String(50))
    def __repr__(self):
        return '<User %r>' % self.user_nickname
    def __init__(self):
        self.id = str(uuid.uuid4()).replace("-", "")

class UserBookMark(db.Model, Base):
    __tablename__ = 'user_bookmark'
    id = db.Column(db.String(32), primary_key=True)
    user_id = db.Column(db.String(50), db.ForeignKey('users.id', deferrable=True, initially="DEFERRED"))
    resource_id = db.Column(db.String(50), db.ForeignKey('resource_info.id', deferrable=True, initially="DEFERRED"))
    def __repr__(self):
        return '<UserBookMark %r>' % self.id
    def __init__(self):
        self.id = str(uuid.uuid4()).replace("-", "")

class UserFollow(db.Model, Base):
    __tablename__ = 'user_follow'
    id = db.Column(db.String(32), primary_key=True)
    user_id = db.Column(db.String(50), db.ForeignKey('users.id', deferrable=True, initially="DEFERRED"))
    resource_id = db.Column(db.String(50), db.ForeignKey('resource_info.id', deferrable=True, initially="DEFERRED"))
    def __repr__(self):
        return '<UserBookMark %r>' % self.id
    def __init__(self):
        self.id = str(uuid.uuid4()).replace("-", "")

class PIN(db.Model, Base):
    __tablename__ = 'pins'
    id = db.Column(db.String(32), primary_key=True)
    email = db.Column(db.String(50))
    pin = db.Column(db.String(6))
    send_time = db.Column(db.String(50))
    def __repr__(self):
        return '<PIN %r>' % self.email
    def __init__(self):
        self.id = str(uuid.uuid4()).replace("-", "")

class ResourceInfo(db.Model, Base):
    __tablename__ = 'resource_info'
    id = db.Column(db.String(32), primary_key=True)
    title = db.Column(db.String(50))
    episodes = db.Column(db.Integer)
    UHD = db.Column(db.Boolean)
    HD = db.Column(db.Boolean)
    inlineSub = db.Column(db.Boolean)
    externalSub = db.Column(db.Boolean)
    chs = db.Column(db.Boolean)
    cht = db.Column(db.Boolean)
    latestDate = db.Column(db.DateTime)
    collects = db.Column(db.Integer)
    comments = db.Column(db.Integer)
    weekday = db.Column(db.Integer)
    coverImage = db.Column(db.String(256))
    littleImage = db.Column(db.String(256))
    def __repr__(self):
        return '<ResourceInfo %r>' % self.title
    def __init__(self):
        self.id = str(uuid.uuid4()).replace("-", "")

class SingleResourceInfo(db.Model, Base):
    __tablename__='singleResource_info'
    id = db.Column(db.String(32), primary_key=True)
    resourceName = db.Column(db.String(50))
    currentEpisode = db.Column(db.Integer)
    organization = db.Column(db.String(50))
    size = db.Column(db.Float)
    upflow = db.Column(db.Integer)
    downflow = db.Column(db.Integer)
    UHD = db.Column(db.Boolean)
    HD = db.Column(db.Boolean)
    inlineSub = db.Column(db.Boolean)
    externalSub = db.Column(db.Boolean)
    chs = db.Column(db.Boolean)
    cht = db.Column(db.Boolean)
    def __repr__(self):
        return '<SingleResourceInfo %r>' % self.id
    def __init__(self):
        self.id = str(uuid.uuid4()).replace("-", "")

class BanguInfo(db.Model, Base):
    __tablename__ = 'bangu_info'
    id = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(50))
    episodes = db.Column(db.Integer)
    currentNum = db.Column(db.Integer)
    startTime = db.Column(db.DateTime)
    turnOverTime = db.Column(db.String(50))
    briefInfo = db.Column(db.String(512))
    tagInfo = db.Column(db.String(512))
    imgUrl = db.Column(db.String(256))
    def __repr__(self):
        return '<BanguInfo %r>' % self.name
    def __init__(self):
        self.id = str(uuid.uuid4()).replace("-", "")
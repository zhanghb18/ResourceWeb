from util.result_wrapper import *
from . import services as resource_service
from . import resource_view
from models import User,ResourceInfo,db
from flask import request

@resource_view.route('/resource/getAnimeTable',methods=['POST'])
def getAnimeTable():
    try:
        input_data = request.form
        token = request.headers.get('token')
        table_type = input_data['table_type']
        resource_list = resource_service.getAnimeTable(token,table_type)
        return JSONWrapper.success({'resource_list':resource_list})
    except Exception as e:
        return JSONWrapper.fail(e)
    
@resource_view.route('/resource/getAnimeCalendar',methods=['POST'])
def getAnimeCalendar():
    try:
        resource_info = db.session.query(ResourceInfo).all()
        resource_list = []
        for item in resource_info:
            if item.weekday == -1:
                continue
            temp = {}
            temp['weekdate'] = item.weekday
            temp['img_src'] = "http://123.56.45.70/images/" + item.littleImage.split('/')[-1]
            temp['img_hover_src'] = "http://123.56.45.70/images/" + item.coverImage.split('/')[-1]
            resource_list.append(temp)
        return JSONWrapper.success({'list':resource_list})
    except Exception as e:
        return JSONWrapper.fail(e)


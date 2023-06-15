from util.result_wrapper import *
from . import services as resource_service
from . import resource_view
from models import User,db
from flask import request

@resource_view.route('/resource/getAnimeTable',methods=['POST'])
def getAnimeTable():
    try:
        input_data = request.form
        table_type = input_data['table_type']
        token = input_data['token']
        resource_list = resource_service.getAnimeTable(token,table_type)
        return JSONWrapper.success({'resource_list':resource_list})
    except Exception as e:
        return JSONWrapper.fail(e)
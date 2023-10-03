from util.result_wrapper import *
from . import services as bangu_service
from . import bangu_view
from models import BanguInfo,db,SingleResourceInfo
from flask import request
import json

@bangu_view.route('/bangu/getBanguInfo',methods=['POST'])
def getBanguInfo():
    try:
        input_data = request.form
        token = request.headers.get('token')
        bangu_name = input_data['banguName']
        banguInfo = db.session.query(BanguInfo).filter_by(name=bangu_name).first().to_json()
        banguInfo['tagInfo'] = eval(banguInfo['tagInfo'])
        banguInfo['imgUrl'] = "http://123.56.45.70/images/" + banguInfo['imgUrl'].split('/')[-1]
        return JSONWrapper.success({'banguInfo':banguInfo})
    except Exception as e:
        return JSONWrapper.fail(e)

@bangu_view.route('/bangu/addSingleResource',methods=['POST'])
def addSingleResource():
    try:
        input_data = request.form
        singleResource = SingleResourceInfo()
        singleResource.organization = input_data['organization']
        singleResource.size = input_data['size']
        singleResource.upflow = input_data['upflow']
        singleResource.downflow = input_data['downflow']
        singleResource.UHD = input_data['UHD']
        singleResource.HD = input_data['HD']
        singleResource.inlineSub = input_data['inlineSub']
        singleResource.externalSub = input_data['externalSub']
        singleResource.chs = input_data['chs']
        singleResource.cht = input_data['cht']
        singleResource.resourceName = input_data['resourceName']
        singleResource.currentEpisode = input_data['currentEpisode']
        db.session.add(singleResource)
        db.session.commit()
        return JSONWrapper.success("新增数据成功")
    except Exception as e:
        return JSONWrapper.fail(e)
    
@bangu_view.route('/bangu/getSingleResource',methods=['POST'])
def getSingleResource():
    try:
        input_data = request.form
        resourceName = input_data['resourceName']
        currentEpisode = input_data['currentEpisode']
        result = db.session.query(SingleResourceInfo).filter_by(resourceName=resourceName,currentEpisode=currentEpisode).all()
        singleList = []
        for item in result:
            temp = item.to_json()
            temp.pop('resourceName')
            temp.pop('currentEpisode')
            singleList.append(temp)
        return JSONWrapper.success(singleList)
    except Exception as e:
        return JSONWrapper.fail(e)
    
@bangu_view.route('/bangu/getResourceInfo',methods=['POST'])
def getResourceInfo():
    try:
        input_data = request.form
        id = input_data['id']
        resourceInfo = db.session.query(SingleResourceInfo).filter_by(id=id).first().to_json()
        resourceInfo['customInfo'] = eval(resourceInfo['customInfo'])
        bangu_name = resourceInfo['resourceName']
        banguInfo = db.session.query(BanguInfo).filter_by(name=bangu_name).first().to_json()
        banguInfo['tagInfo'] = eval(banguInfo['tagInfo'])
        banguInfo['imgUrl'] = "http://123.56.45.70/images/" + banguInfo['imgUrl'].split('/')[-1]
        result = {}
        result['resourceInfo'] = resourceInfo
        result['banguInfo'] = banguInfo
        return JSONWrapper.success(result)
    except Exception as e:
        return JSONWrapper.fail(e)
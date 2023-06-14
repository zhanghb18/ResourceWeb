from util.token_utils import decrypt_AES
from models import UserBookMark,UserFollow,ResourceInfo,db

def getAnimeTable(token,table_type):
    user_id = decrypt_AES(token)
    if table_type == 'follow':
        follow_result = db.session.query(UserFollow).filter_by(user_id=user_id).all()
        resource_id_list = []
        resource_list = []
        for _elem in follow_result:
            resource_id_list.append(_elem.resource_id)
        for resource_id in resource_id_list:
            resource_result = db.session.query(ResourceInfo).filter_by(id=resource_id).first()
            resource_list.append(resource_result.to_json())
        return resource_list
    return 0
from util.result_wrapper import *
from . import services as user_service
from . import user_view

@user_view.route('/user/login')
def user_login():
    user_service.user_login()
    return 'hello word'
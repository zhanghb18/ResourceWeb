from util.result_wrapper import *
from . import user_view

@user_view.route('/user/login')
def user_login():
    return 'hello word'
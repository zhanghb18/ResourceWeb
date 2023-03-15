# -*- coding:utf-8 -*-
from flask import Blueprint

user_view = Blueprint(
    'user',
    __name__,
)

from . import views
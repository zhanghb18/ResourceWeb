# -*- coding:utf-8 -*-
from flask import Blueprint

util_view = Blueprint(
    'util',
    __name__,
)

from . import views
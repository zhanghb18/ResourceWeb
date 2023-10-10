# -*- coding:utf-8 -*-
from flask import Blueprint

bangu_view = Blueprint(
    'bangu',
    __name__,
)

from . import views
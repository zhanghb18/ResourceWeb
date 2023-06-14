# -*- coding:utf-8 -*-
from flask import Blueprint

resource_view = Blueprint(
    'resource',
    __name__,
)

from . import views
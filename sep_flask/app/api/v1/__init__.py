from flask import Blueprint

from app.api.v1 import client, user, book


def create_blubprint_v1():
    bp_v1 = Blueprint('v1',__name__)

    user.api.register(bp_v1)
    book.api.register(bp_v1)
    # 将客户端注册到蓝图智商
    client.api.register(bp_v1)
    return bp_v1
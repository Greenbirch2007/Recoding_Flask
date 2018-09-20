


# 使用枚举类型代替数字类型进行运算
from enum import Enum

# 定义客户端的类型 类----->类型
class ClientTypeEnum(Enum):

    USER_EMAIL = 100
    USER_MOBILE = 101

    #微信小程序
    USER_MINA = 200
    #微信公众号
    USER_WX = 201
    pass
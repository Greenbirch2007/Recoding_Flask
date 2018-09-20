



# 創建一個 在v1上的藍圖，因爲這個v1對應的藍圖要被下面所有的紅圖調用
# 所以在sep_flask/app/api/v1/__init__.py中來創建v1對應的藍圖


# 竟然命名與app的藍圖一致 因爲後面要完全修改重構,這裏面直接用到了flask真正的藍圖
from flask import Blueprint
from app.api.v1 import user,book,client

def create_blueprint_v1():
    #在這裏實現兩個紅圖向藍圖的註冊，先把兩個紅圖導入進來
    # from app.api.v1.book import api as book
    # from app.api.v1.user import api as user

    bp_v1 = Blueprint('v1',__name__)
    # 直接使用模塊的.實例化對象
    user.api.register(bp_v1,url_prefix='/user')  # 這裏紅圖的註冊函數直接接受一個藍圖對象，就把紅圖註冊到藍圖對象上了
    book.api.register(bp_v1,url_prefix='/book')  # 這裏紅圖的註冊函數直接接受一個藍圖對象，就把紅圖註冊到藍圖對象上了
    client.api.register(bp_v1,url_prefix='/client')
    return bp_v1
# 完成了兩個紅圖（book,user） 對 v1藍圖的註冊，下面就要把v1藍圖註冊到flask核心對象上
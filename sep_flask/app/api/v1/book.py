



from flask import Blueprint

# 通過模仿藍圖構建一個自定義的對象
# 可以通過模仿藍圖構建一個自定義的對象紅圖 redprint 創建sep_flask/app/libs/ 用於存放我們自定義的模塊
from app.libs.redprint import Redprint

# book = Blueprint('book',__name__) #創建了v1的藍圖，這裏就不需要了



api = Redprint('book')  #實例化一個redprint對象，命名爲book



# 裝飾器都是用到了實例化對象的route方法
@api.route('/get')
def get_book():
    return 'get book!'



@api.route('/create')
def create_book():
    return 'create book!'
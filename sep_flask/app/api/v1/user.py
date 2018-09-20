
from flask import Blueprint

from app.libs.redprint import Redprint

# user = Blueprint('user',__name__)  創建了v1的藍圖，這裏就不需要了
api = Redprint('user')  #實例化一個redprint對象，命名爲user


# 裝飾器都是用到了實例化對象的route方法(都是使用視圖函數上面第一層的實例，但是所有環節都要完成實例化)
@api.route('/get') #視圖函數的route就是實現了底層視圖函數向上面一層藍圖或之類改寫的紅圖的註冊
def get_user():
    return 'this is set_flask test!'

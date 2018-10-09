
from flask import Blueprint

from app.libs.redprint import Redprint

# user = Blueprint('user',__name__)  創建了v1的藍圖，這裏就不需要了
api = Redprint('user')  #實例化一個redprint對象，命名爲user


# 裝飾器都是用到了實例化對象的route方法(都是使用視圖函數上面第一層的實例，但是所有環節都要完成實例化)
#視圖函數的route就是實現了底層視圖函數向上面一層藍圖或之類改寫的紅圖的註冊

# @api.route('/get')
@api.route('',methods=['GET'])
def get_user():
    return 'this is set_flask test!'



# 用户 注册 登录
# 统一称为客户端 client
# 种类非常多 注册的形式非常多 短信 邮件 QQ 微信  注册不一定需要密码，比如小微信
# 用户名 ：电话号码，邮箱等
#密码
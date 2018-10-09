



from flask import Blueprint

# 通過模仿藍圖構建一個自定義的對象
# 可以通過模仿藍圖構建一個自定義的對象紅圖 redprint 創建sep_flask/app/libs/ 用於存放我們自定義的模塊
from app.libs.redprint import Redprint

# book = Blueprint('book',__name__) #創建了v1的藍圖，這裏就不需要了

# 轉換到RESTful的思想 ，api=Redprint('book') 已經定位到了資源，
#然後可以在路由中來操作這個資源
#都在實例化紅圖中把RESTful給完成了，就是   1.實例化用於定位資源  2.route的method方法用於操作資源

api = Redprint('book')  #實例化一個redprint對象，命名爲book

# 裝飾器都是用到了實例化對象的route方法
# @api.route('/get')
@api.route('',methods=['GET'])
def get_book():
    return 'get book!'
#　不能用動詞
# 必須要有版本號　理論是理論，實踐是實踐 json
#內部開發API   開發api
# 标准的rest不适合做内部开发，因为把数据都视作资源，并且只有增删改查的操作，
# 接口粒度太粗，对前端来说粒度太大了　比如user视图函数下的，很多属性，name,age,gender都一次返回到前端
# 会造成HTTP请求的数量大幅增加
# 所谓接口，就是基于确定性的数据库数据，也就是资源，对于前端或专门的api设计的视图函数，然后返回什么属性的设计！
#这个需要考虑业务逻辑 route()是一种带参数的装饰器

# @api.route('/create')
@api.route('',methods=['POST'])
def create_book():
    return 'create book!'
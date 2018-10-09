

# 把對flask核心對象的所有操作都放在app/app.py下面(實例化app)
# 把整個項目的所有配置文件都導入到flask的核心對象app中()
from flask import Flask


#只有把藍圖註冊到flask的核心對象app上，才能使得藍圖生效
def register_blueprints(app):  # 注意和app的register_blueprint區分開來

    # from app.api.v1.user import user # 引入實例化在user上的藍圖，
    # from app.api.v1.book import book # 引入實例化在book上的藍圖，
    # app.register_blueprint(user)  #再利用核心對象app的藍圖註冊方法直接對接user藍圖對象
    # app.register_blueprint(book)   #再利用核心對象app的藍圖註冊方法直接對接book藍圖對象
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(),url_prefix='/v1')
    # 用核心對象的註冊函數接收v1藍圖的一個對象
    # （函數也是一個對象） 就完成了v1藍圖向核心對象app的註冊
    # 看清楚了
    # 底層視圖函數--->直接使用上面一層的紅圖的註冊函數（接收底層視圖函數的對象）
    # 第二層 用創建的v1藍圖的註冊函數接收下面一層兩個紅圖（book,user）的實例對象，即自定義的紅圖註冊到有版本的v1的藍圖上
    # 最後 用flask核心對象的註冊函數接收v1藍圖的實例對象。完成v1藍圖向核心對象app的註冊

    # 將路由的版本放到自定義的有版本的v1藍圖上面，把user,book放到對應的紅圖上面，可以簡化最底層視圖函數的路由設置
    #第一個app核心對象的register_blueprint方法有一個url_prefix參數，可以指定前綴路由
    #可以借鑑上面的regist_blueprint()的url_prefix參數，在紅圖定義裏面的註冊函數頁設置一個url_prefix參數，這就需要重構源代碼了

# 藍圖最好用作模塊級別的拆分，而不是視圖函數級別的拆分！同時路由過長


# 在这里把sqlalchemy注册到flask核心对象app上

def register_plugin(app):
    from app.models.base import db
    db.init_app(app) # 进行注册
    with app.app_context():
        db.create_all() # 来创建所有数据库中的数据表  这里用上下文




def create_app():
    app = Flask(__name__)
    # 把配置文件裝在到flask的核心對象app上
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')

    register_blueprints(app)  # 定義了函數之後記得調用
    register_plugin(app)   #将sql注册到核心对象app上之后，在启动文件中调用下
    return app
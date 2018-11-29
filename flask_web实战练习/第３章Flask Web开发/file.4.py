#　蓝图
#  蓝图(Blueprint)实现了应用额模块化，使用蓝图让应用层次清晰，开发者可以更容易的开发和维护项目。蓝图通常作用与相同额URL前缀，
#  比如  /user/:id,/user/profile 这样的地址，都可以/user开头，那么就可以将它们放在一个模块中，

from flask import Blueprint


bp = Blueprint('user',__name__,url_prefix='/user')



@bp.route('/')
def index():
    return "User's Index page"

# 每个模块都会暴露一个全局变量bp.再看主程序 app_bp.py


# 使用register_blueprint注册模块，如果想去掉模块只需要去掉对应的注册语句即可
#　命令行接口

# 在flask0.11之前，启动的应用的端口，主机地址以及是否开启debug模式，都需要在代码中明确指定，一个比较好的方式是使用第三方扩展flask-script管理
#　从flask0.11开始，flask集成了Click，现在可以额直接在命令行直接执行flask命令启动Flask应用了　
# 新的方案可以替换flask-script，我面积与flask.cli模块添加两个子命令()
# 第一个子命令，initdb，用来初始化数据库，这没有实际的逻辑，只是wield演示click的使用方法
# 先指定flask_app变量
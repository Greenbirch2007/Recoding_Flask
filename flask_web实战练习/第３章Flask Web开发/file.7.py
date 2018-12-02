# 在flask中使用sqlalchemy

# 一个大型项目，模型应该对应存放在不同的模型文件中，可以把users这个表的模型存储到users.py
# db.Model其实还是给予delarative_base实现的，flask-sqlalchemy提供了一个和django风格很像的基类。这里重新定义了User的__init__方法，因为它默认需要传入所有字段，
# 而id是一个自增张的字段，不需要传入

# ext存放了flask第三方的扩展

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 这样的好处是，db是一个没有依赖的常量，app也可以'from ext import db',不会造成循环依赖

# 把配置也独立常量，放入config.py中

# 在web上创建用户的应用(app_with_sqlalchemy.py)

# from_object加载config.py里的配置， 如 app.config.from_object('config')
# 把第三方扩展放在ext.py之后，需要使用xx.init_app(app)的方式，进行初始化

# 注意，drop_all,create_all要在定义model之后再执行。flask-sqlalchemy 要求执行的时候有应用上下文，需要使用with app.app_context()创建应用上下文
# 记录慢查询

# 1.  启用查询记录功能
#　2.给app.logger添加一个记录日志到名为slow_query.log的文件的处理器，这个日志会按大小切分
#　３．添加after_request钩子，每次请求结束后获取执行的查询语句，假如超过阈值则记录日志
#　理解context（上下文）
# werkzeug的Local
# werkzeug自己实现了本地新城
# werkzeug还实现了两种数据结构:LocalStack,LocalProxy

from flask import Flask,request

app = Flask(__name__)


@app.route('/people')
def people():
    name = request.args.get('name')
    return  name

if __name__ =='__main__':
    app.run()
# flask.request 就是一个获取名为_request_ctx_stack的栈顶对象的LocalProxy实例

# 使用 上下文
# 应用上下文的典型应用场景是缓存一些在发生请求之前要使用的资源,比如生成数据库连接和缓存一些对象:请求上下文发生在http请求开始,WSGI Server调用Flask.__call__()之后
# 应用上下文并不是应用启动之后生成的唯一上下文
# Flask中有4个上下文变量
# 1. flask,current_app:应用上下文.它是当前app实例对象
# 2. flask.g : 应用上下文.处理请求时用作临时存储的对象
# 3.flask.request:请求上下文.它封装了客户端发出的http请求中的内容
# 4. flask.session:请求上下文,它存储了用户会话

#  首页  重新设置图片页,下载页  预览页 ,短链接页



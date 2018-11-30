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

from flask import Flask


def register_blueprints(app):
    from app.api.v1 import create_blubprint_v1
    app.register_blueprint(create_blubprint_v1(),url_prefix='/v1')



def register_plugin(app):  #为第三方插件进行注册
    from app.models.base import db
    db.init_app(app)
    # 完成注册之后还要用db.create_all()来创建所有的数据表
    # 必须在app的山下文环境中才能完成create_all()的操作
    with app.app_context():
        db.create_all()



def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')

    register_blueprints(app)
    register_plugin(app)
    return app



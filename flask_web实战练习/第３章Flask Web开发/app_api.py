# 基于调度方法的视图

# flask.views.MethodView对每个http方法执行不同的函数(映射到对应方法的小写的同名方法上)，这对restful api尤其有用。

from flask import Flask,jsonify
from flask.views import MethodView
from flask_restful import abort

app = Flask(__name__)


class UserAPI(MethodView):
    def get(self):
        return jsonify({
            'username':'fake',
            'baidu':'http://www.baidu.com'
        })

    def post(self):
        return 'UNSUPPORED!'

app.add_url_rule('/user',view_func=UserAPI.as_view('userview'))


# 通过装饰as_view的返回值来实现对于视图的装饰功能，常用于权限的检查，登录验证等

def user_required(f):
    def decorator(*args,**kwargs):
        if not g.user:
            abort(401)
        return f(*args,**kwargs)
    return decorator

view = user_required(UserAPI.as_view('users'))
app.add_url_rule('/user/',view_func=view)
# 从flask０．８开始，还可以通过在继承MethodView的类中添加decorators属性来实现对视图的装饰

class UserAPI(MethodView):
    decorators = [user_required]


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888)


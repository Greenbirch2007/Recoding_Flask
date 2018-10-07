# 使用flask+SQLAchemy这个ORM时，定义的模型类不能使用
# json.dumps(user, default=lambda o: o.__dict__, sort_keys=True, indent=4)
# 这种方式格式化。
# 使用user.__dict__.keys()获取的属性会多出一个属性。
# 在python中定义的一般类，如：
# class Test(object):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# python中的普通类可以直接格式化：test=Test('张三',21)
# print(json.dumps(test,default=lambda o: o.__dict__,sort_keys=True, indent=4,ensure_ascii=False))

# from flask import make_response, jsonify
# 返回json,同事带上状态吗
# response = make_response(jsonify({'test': 'good'}, 403)

import json
import random

from flask import Flask,jsonify,Response

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 显示中文
# @app.route('/hello/<name>/<words>',methods=['GET'])
# def hello(name,words):
#     return jsonify({'name':name,'words':words})#也可以传入key=value形式的参数，如jsonify(name=name,words=words)
#


#这样不仅HTTP返回的内容是json，而且返回的Content-Type也是application/json了。

# @app.route('/')
# def root():
#     t = {
#         'a': 1,
#         'b': 2,
#         'c': [3, 4, 5]
#     }
#     return Response(json.dumps(t), mimetype='application/json')



# 实际上flask已经为json准备了专门的模块：jsonify。
# jsonify不仅会将内容转换为json，而且也会修改Content-Type为application/json。
# @app.route('/')
# def root():
#     t = {
#         'a': 1,
#         'b': 2,
#         'c': [3, 4, 5]
#     }
#     return jsonify(t)

# 自定义Flask的Response，使用force_type()（2017.11.9更新）
# class MyResponse(Response):
#     @classmethod
#     def force_type(cls, response, environ=None):
#         if isinstance(response, (list, dict)):
#             response = jsonify(response)
#         return super(Response, cls).force_type(response, environ)
#
# class MyFlask(Flask):
#     response_class = MyResponse
#
# app = MyFlask(__name__)
#
# @app.route('/')
# def root():
#     t = {
#         'a': 1,
#         'b': 2,
#         'c': [3, 4, 5]
#     }
#     return t

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user/check', methods=["GET"])
def return_json():
    if random.randint(0, 5) >= 2:
        return_dict = {
            "data": True,
            "code": 0,
            "msg": "string"
        }
    else:
        return_dict = {
            "data": False,
            "code": 0,
            "msg": "string"
        }

    return jsonify(return_dict)

# 路由 shceme://host[":"port][path]["?query"]
# 比如 http://127.0.0.1:5000/user/check/feature?userName=heatdeath&heath=123456
def toJson(**kwargs):
    return json.dumps(kwargs) # 把json转换成字符串

if __name__ =='__main__':
    app.run(debug=True)
# -*- coding:utf8 -*-

#
# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route("/HelloWorld")
# def hello_world():
#     return "Hello World!"
#
#
# if __name__ == "__main__":
#     app.run(debug=True)


#实现一个简单restful

#这里使用flask自带的jsonify函数
# from flask import Flask,jsonify,Response
#
# app = Flask(__name__)
#
# @app.route('/hello/<name>/<words>',methods=["GET"])
# def hello(name,words):
#     return jsonify({'name':name,'words':words})
#
# if __name__ == "__main__":
#     app.run(debug=True)

# 这里使用Python自带的json.dumps方法
from flask import Flask,jsonify,Response
import json

app = Flask(__name__)

@app.route('/hello/<name>/<words>',methods=["GET"])
def hello(name,words):
    return json.dumps({'name':name,'words':words})

if __name__ == '__main__':
    app.run(debug=True)
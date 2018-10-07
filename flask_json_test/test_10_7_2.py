# -*- coding:utf-8 -*-

import json
from flask import Flask,jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 显示中文


@app.route('/')
def index():
    s = ['张三', '年龄', '姓名']
    return jsonify(s)


@app.route('/t1')
def index1():
    s = ['张三', '年龄', '姓名']
    t = {}
    t['data'] = s
    return jsonify(t)

@app.route('/t2')
def index2():
    s = ['张三', '年龄', '姓名']
    t = {}
    for num in range(1, 5):
        t[str(num)] = s
    return jsonify(t)

@app.route('/t3')
def index3():
    s = ['张三', '年龄', '姓名']
    t = {}
    for num in range(1, 5):
        t[str(num)] = s
    data = {}
    data['SUCCESS'] = 'SUCCESS'
    data['data'] = t
    return jsonify(data)

@app.route('/t4')
def index4():
    s = ['张三', '年龄', '姓名']
    t = {}
    for num in range(1, 5):
        t[str(num)] = s
    data = {}
    data['SUCCESS'] = 'SUCCESS'
    data['data'] = t
    return json.dumps(data, ensure_ascii=False)




if __name__ =='__main__':
    app.run(debug=True)
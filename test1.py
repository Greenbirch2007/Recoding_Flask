# -*- coding:utf-8 -*-

import logging
from flask import Flask,url_for
from flask import request
from flask import json
from flask import Response

app = Flask(__name__)  #实例化

@app.route('/')  #资源1
def api_root():
    return 'Welcome'

@app.route('/articles') #资源2
def api_articles():
    return 'list of ' + url_for('api_articles')

@app.route('/articles/<articleid>') #资源3
def api_article(articleid):
    return 'You are reading' + articleid




# @app.route('/hello')  #请求参数
# def api_hello():
#     if 'name' in request.args:
#         return 'Hello' + request.args['name']
#     else:
#         return 'Hello John Doe'


@app.route('/echo',methods=['GET','POST','PATCH','PUT','DELETE'])  #请求方法
def api_echo():
    if request.method == 'GET':
        return 'ECHO:GET\n'
    elif request.method =='POST':
        return 'ECHO:POST\n'
    elif request.method == 'PATCH':
        return 'ECHO:PATCH\n'
    elif request.method == 'PUT':
        return 'ECHO:PUT \n'

    elif request.method == 'DELETE':
        return 'ECHO:DELETE \n'

@app.route('/messages',methods=['POST']) #请求数据和请求头（格式的选择）
def api_message():
    if request.headers['Content-Type'] == 'text/plain':
        return 'Text Message:' +request.data
    elif request.headers['Content-Type'] == 'application/json':
        return 'JSON Message:' + json.dump(request.data)
    elif request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./binary','wb')
        f.write(request.data)
        f.close()
        return 'Binary message written!'
    else:
        return '415 Unsupported Media Type ；）'


# @app.route('/hello',methods = ['GET']) #响应的第一种方式
# def api_hello():
#     data ={
#         'hello':'world',
#         'numbers':3
#     }
#     js = json.dumps(data)
#     resp = Response(js,status=200,mimetype='application/json')
#     resp.headers['Link'] = 'http://luisrei.com'
#     return resp



from flask import jsonify  #响应的第二种方式 改写的方式稀里糊涂的

@app.route('/hello',methods=['GET'])
# def api_hello():
#     data ={
#         'hello':'world',
#         'numbers':3
#     }
#     resp = jsonify(data)
#     resp.status_code =200


@app.errorhandler(404)  #状态码和错误处理
def not_found(error=None):
    message = {
        'status':404,
        'message':'Not Found:' + request.url,

    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


@app.route('/users/<userid>',methods=['GET'])
def api_users(userid):
    users = {'1':'john','2':'steve','3':'bill'}

    if userid in users:
        return jsonify({userid:users[userid]})
    else:
        return not_found()




from functools import wraps # 认证 处理HTTP Basic Authentication

def check_auth(username,password):
    return username == 'admin' and password == '123'

def authenticate():
    message = {'message':'Authenticate.'}
    resp = jsonify(message)

    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Example"'
    return resp

def requires_auth(f):  #相当于做了修饰器的两层嵌套
    @wraps(f)
    def decorated(*args,**kwargs):
        auth = request.authorization
        if not auth:
            return authenticate()
        elif not check_auth(auth.username,auth.passowrd):
            return authenticate()
        return f(*args,**kwargs)
    return decorated


# @app.route('/secrets')
# @requires_auth
# def api_hello():
#     return "SHHH this is top secret spy stuff!"

#使用logging模块设置日志信息


file_handler = logging.FileHandler('app.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

@app.route('/hello',methods=['GET'])
def api_hello():
    app.logger.info('informing')
    app.logger.warning('warning')
    app.logger.error('screaming bloody murder!')
    return 'check your logs\n'








if __name__ == '__main__':
    app.run(debug=True)  #开启调试信息




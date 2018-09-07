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
# from flask import Flask,jsonify,Response
# import json
#
# app = Flask(__name__)
#
# @app.route('/hello/<name>/<words>',methods=["GET"])
# def hello(name,words):
#     return json.dumps({'name':name,'words':words})
#
# if __name__ == '__main__':
#     app.run(host='172.16.2.148',port=5000,debug=True)

#
# from flask import Flask,abort,request,jsonify
#
# app = Flask(__name__)

#测试数据暂放容器

# tasks= []
#
# @app.route('/add_task/',methods =["GET"])
# def add_task():
#     if not request.json or 'id' not in request.json or 'info' not in request.json:
#         abort(400)
#
#     task = {
#         'id':request.json['id'],
#         'info':request.json['info']
#     }
#     tasks.append(task)
#     return jsonify({'result':'sucess'})
#
#
# def get_task():
#     if not request.args or 'id' not in request.args:
#         return jsonify(tasks)
#     else:
#         task_id = request.args['id']
#         task = filter(lambda t:t['id'] == int(task_id),tasks)
#         return jsonify(task) if task else jsonify({'result':'not found'})
#
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0',port=8383,debug=True)


#使用flask 的restful扩展库  flask-restful

#
# from flask import Flask
# from flask_restful import reqparse,abort,Api,Resource
#
#
# app = Flask(__name__)
# api = Api(app)
#
# TODOS = {
#     'todo1':{'task':'baidu an api'},
#     'todo2':{'task':'哇哈哈哈'},
#     'todo3':{'task':'profit'},
# }
#
# def abort_if_todo_doesnt_exist(todo_id):
#     if todo_id not in TODOS:
#         abort(404,message="Todo {} doesn't exist".format(todo_id))
#
# parser = reqparse.RequestParser()
# parser.add_argument('task')
#
# #Todo
# # show a single todo item and lets you delte a todo item
#
# class Todo(Resource):
#     def get(self,todo_id):
#         abort_if_todo_doesnt_exist(todo_id)
#         return TODOS[todo_id]
#
#     def delete(self,todo_id):
#         abort_if_todo_doesnt_exist(todo_id)
#         del TODOS[todo_id]
#         return '',204
#
#     def put(self,todo_id):
#         args = parser.parse_args()
#         task = {'task':args['task']}
#         TODOS[todo_id] = task
#         return task,201
#
#
# class TodoList(Resource):
#     def get(self):
#         return TODOS
#
#     def post(self):
#         args = parser.parse_args()
#         todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
#         todo_id = 'todo%i' % todo_id
#         TODOS[todo_id] = {'task':args['task']}
#         return TODOS[todo_id],201   #实际上是返回一个元组的
#
#
# api.add_resource(TodoList,'/todos')
# api.add_resource(Todo,'/todos/<todo_id>')
#
#
# if __name__ == '__main__':
#     app.run(debug=True)



#flask 的重定向练习

# from flask import Flask ,make_response,redirect,abort
#
# app = Flask(__name__) # Flask()类的构造函数必须指定一个参数，即程序主模块或包的名字
#
#
# @app.route('/') # 把修饰的函数注册为路由
# def index():
#     response = make_response('<h1>cookie!</h1>')
#     response.set_cookie('answer','42') # 添加cookie
#     return response
#
# @app.route('/redirect') # 重定向
# def redirectTest():
#     return redirect("http://www.baidu.com")
#
#
# @app.route('/abort/<idNum>') # abort()函数会把异常交给web服务器
# def abortDeom(idNum):
#     if not idNum:
#         abort(404)
#     return '<h1>Hello,%s</h1>' % idNum
#
#
# if __name__ == '__main__':
#     app.run(debug=True)


# super()函数练习

# class A(object):
#     def __init__(self, xing, gender):
#         self.namea = "aaa"
#         self.xing = xing
#         self.gender = gender
#
#     def funca(self):
#         print("function a : %s" % self.namea)
#
#
#
# class B(A):
#     def __init__(self, xing, gender, age):
#         super(B, self).__init__(xing,age)
#         self.nameb = "bbb"
#         ##self.namea="ccc"
#         self.xing = xing.upper()
#         # self.gender = gender  如果有这个就会输出男，如果没有按照位置参数就会输出A类的gender参数
#         self.age = age + 1
#         # self.gender = gender.upper()
#
#     def funcb(self):
#         print("function b : %s" % self.nameb)
#
#
#
# b = B('li','男',29)
# # print(b.namea)
# # print(b.nameb)
# print(b.xing)
# print(b.age)
# print(b.gender)
# # b.funca()
# # b.funcb()
#


#python 装饰器 Flask框架和Flask - Script介绍
# https://blog.csdn.net/twc829/article/details/52154214

def log(level,*args,**kwargs):
    def inner(func):
        def wrapper(*args,**kwargs):
            print(level,":before calling ",func.__name__)
            print(level,':args:',args,'kvargs:',kwargs)
            func(*args,**kwargs)
            print(level,':after calling',func.__name__)
            print('')
        return wrapper
    return inner

@log(level='INFO')
def hello(name,msg):
    print('hello',name,msg)




if __name__=='__main__':
    hello(name='nowcoder',msg='i miss you~')



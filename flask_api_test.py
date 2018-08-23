from flask import abort,Flask,jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

# @app.route('/todo/api/v1/tasks/<int:task_id>', methods=['GET'])
# def get_task(task_id):
#     task = filter(lambda t: t['id'] == task_id, tasks)
#     if len(task) == 0:
#         abort(404)
#     return jsonify({'task': task[0]})

from flask import request

@app.route('/todo/api/v1/tasks',methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(404)
    task = {
    'id':tasks[-1]['id'] + 1,
    'title':request.json['title'],
    'description':request.json.get('description',""),
    'done':False
    }
    tasks.append(task)
    return jsonify({'task':task}), 201




@app.route('/todo/api/v1/tasks/<int:task_id>',methods=["PUT"])
def update_task(task_id):
    task = filter(lambda t:t['id'] == task_id,tasks)
    if len(task) ==0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title',task[0]['title'])
    task[0]['description'] = request.json.get('description',task[0]['description'])
    task[0]['done'] = request.json.get('done',task[0]['done'])
    return jsonify({'task':task[0]})

@app.route('/todo/api/v1/tasks/<int:task_id>',methods=['DELETE'])
def delete_task(task_id):
    task = filter(lambda t:t['td'] == task_id,tasks)
    if len(task) ==0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result':True})



#优化web service接口

from flask import url_for

def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task',task_id=task['id'],_external=True)
        else:
            new_task[field] = task[field]
    return new_task

@app.route('/todo/api/v1/tasks',methods=['GET'])
def get_tasks():
    return jsonify({'tasks'map[make_public_task,tasks]})

#加强 restful web service 的安全性

from flask.ext.httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'migue1':
        return 'Python'
    return None
@auth.error_handler
def unauthorized():
    return make_reponse(jsonify({'error':'unauthorized access'}),401)



@app.route('/todo/api/v1/tasks',methods=['GET'])
@auth.login_required
def get_tasks():
    return jsonify({'tasks':tasks})

@auth.error_handler
def unauthorized():
    return make_reponse(jsonify({'error':'unauthorized access'}),403)


#路由

from flask import Flask
from flask.ext.restful import Api,Resource

app = Flask(__name__)
api = Api(app)

class UserAPI(Resource):
    def get(self,id):
        pass
    def put(self,id):
        pass
    def delete(self,id):
        pass
api.add_resource(UserAPI,'/users/<int:id>',endpoint='user')


class TaskListAPI(Resource):
    def get(self):
        pass
    def post(self):
        pass
class TaskAPI(Resource):
    def get(self,id):
        pass
    def put(self,id):
        pass
    def delete(self,id):
        pass

api.add_resource(TaskListAPI,'/todo/api/v1/tasks',endpoint='tasks')
api.add_resource(TaskAPI,'/todo/api/v1/taks/<int:id>',endpoint='task')


#解析以及验证请求

from flask.ext.restful import reqparse

class TaskListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParse()
        self.reqparse.add_argument('title',type=str,required=True,
            help='No task title provided',location='json')
        self.reqparse.add_argument('description',type=str,default="",location='json')
        super(TaskListAPI,self).__init__()

class TaskAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParse()
        self.reqparse.add_argument('title',type=str,location='json')
        self.reqparse.add_argument('description',type=str,location='json')
        self.reqparse.add_argument('done',type=bool,location='json')
        super(TaskAPI,self).__init__()



def put(self,id):
    task = filter(lambda t:t['id']==id,tasks)
    if len(task) == 0:
        abort(404)
    task = task[0]
    args = self.reqparse.parse_args()
    for k,v in args.iteritems():
        if v != None:
            task[k] = v
    # return jsonify({'task':make_public_task(task)})  
    # 生成响应 
    return {'task':make_public_task(task)} , 201


from flask.ext.restful import fields,marshal

task_fields = {
    'title':fields.String,
    'description':fields.String,
    'done':fields.Boolean,
    'uri':fields.Url('task')
}


class TaskAPI(Resource):
    def put(self,id):
        return {'task':marshal(task,task_fields)}




# 认证
from flask.ext.httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

class TaskAPI(Resource):
    decorators = [auth.login_required]

class TaskAPI(Resource):
    decorators = [auth.login_required]







#用户数据库

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(32),index=True)
    passwor_hash = db.Column(db.String(128))



#密码散列

from passlib.apps import custom_app_context as pwd_context

class User(db.Model):

    def hash_password(self,password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self,password):
        return pwd_context.verify(password,self.password_hash)

@app.route('api/users',methods=['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400)
    if User.query.filter_by(username=username).first() is not None:
        abort(400)
    user = User(username=username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'username':user.username}),201, {'location':url_for('get_user',id=user.id,_external=True)}



from flask.ext.httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

@app.route('/api/resource')    
@auth.login_required
def get_resource():
    return jsonify({'data':'Hello,%s!'% g.user.username})


#verify_password回调函数实现
@auth.verify_password
def verify_password(username,password):
    user = User.query.filter_by(username=username).first()
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True

    





















if __name__ == '__main__':
    app.run(debug=True)
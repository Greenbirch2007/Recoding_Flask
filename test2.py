

from flask import Flask,jsonify

app = Flask(__name__)


tasks = [
    {
        'id':1,
        'title':'Buy groceries',
        'description':'Milk,Cheese,Pizza,Fruit,Tyleno1',
        'done':False
    },
    {
        'id':2,
        'title':'Learn Python',
        'description':'Need to find a good Python tutorial on the web',
        'done':False
    }
]

# @app.route('/todo/aip/v1/tasks',methods=['GET'])
# def get_tasks():
#     return jsonify({'tasks':tasks})


from flask import abort

@app.route('/todo/api/v1/tasks/<int:task_id>',methods=['GET'])
def get_task(task_id):
    task = filter(lambda t : t['id'] == task_id,tasks)   #这个应该是python3.5不行，只能使用python2.7
    if len(task) ==0:
        abort(404)
    return jsonify({'task':task[0]})




if __name__=='__main__':
    app.run(debug=True)
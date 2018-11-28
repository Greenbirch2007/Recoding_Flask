#! -*- coding:utf-8 -*-


from flask import Flask,request,abort,redirect,url_for




app = Flask(__name__)
app.config.from_object('config')



@app.route('/people/')
def people():
    name =request.args.get('name')
    if not name:
        return redirect(url_for('login'))
    user_agent = request.header.get('User-Agent')
    return 'Name:{0}; UA: {1}}'.format(name,user_agent)




@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        return 'User:{} login'.format(user_id)
    else:
        return '<h1>Open Login page</h1>'

@app.route('/secret/')
def secret():
    # abort(401)
    return ('This s never executed!')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888,debug=app.debug)
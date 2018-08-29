

from flask import Flask,url_for
from flask import request #HTTP请求方法
from flask import render_template
from werkzeug.utils import secure_filename #请求对象
from flask import make_response #存储cookies
from flask import abort,redirect,url_for


app = Flask(__name__)



@app.route('/')
def index():
    return 'Index Page'

#第一种请求方式
# with app.test_request_context('/hello',methods=['POST']):
#     assert request.path == '/hello'
#     assert request.method == 'POST'



@app.route('/login',methods=['POST','GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    return render_template('login.html',error=error)


# @app.route('/upload',methods=['GET','POST'])
# def upload_file():
#     if request.method == 'POST':
#         f = request.files['the_file']
#         f.save('/var/www/uploads/uploaded_file.txt')


@app.route('/upload',methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/' + secure_filename(f.filename))


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',name=name)


@app.route('/')
def index():
    username = request.cookies.get('username')



#改写登录方法
# @app.route('/login')
# def login():
#     return 'login'

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()



@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login',next='/'))
    print(url_for('profile',username='Joe Doe'))



@app.route('/user/<username>')
def show_user_profile(username):

    #show the user profile for that user
    return 'User %s '% username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    #show the post with the given id ,the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    #show the subpath after /path/
    return 'Subpath %s' % subpath


@app.route('/projects')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

#重定向和错误
@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'),404

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'),404


@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'),404)
    resp.headers['X-Something'] = 'A value'
    return resp

#会话
from flask import Flask,session,redirect,url_for,escape,request
app = Flask(__name__)
app.secret_key  = b'werw$%3s-sfa'
@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' %escape(session['username'])
    return 'You are not logged in'

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session['username']= request.form['username']
        return redirect(url_for('index'))
    return '''
    <fooowaeraerw>'''





@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username','the username')
    return resp



if __name__ == '__main__':
    app.run(debug=True)



# 最小的应用

from flask import Flask,url_for,request

app = Flask(__name__)







# 外部可见的服务器

#路由 使用route()装饰器把函数绑定到url


#变量规则  通过把URL的一部分标记为<variable_name>就可以在URL中添加变量。标记的部分作为关键字
# 参数传递给函数。通过使用<converter:variable_name>，可以选择性的加上一个转换器，为变量指定规则。

# @app.route('/')
# def index():
#     return 'Index Page'


# @app.route('/hello')
# def hello():
#     return 'Hello,World'


@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d '% post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath %s' % subpath


# 唯一的URL/重定向     区别在于是否使用尾部斜杠
@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


# /projects/ 访问一个没有斜杠结尾的URL时Flask会自动进行重定向，帮你尾部加上一个斜杠。
# 如果访问这个URL时添加了尾部斜杠就会得到一个404.这样可以保持URL唯一，并帮助搜索引擎避免重复索引同一页面

# URL构建   使用反转函数url_for()动态构建  (有多个好处)
# url 的源码 url_for(endpoint, **values)，第一个参数endpoit,表示结束点，就是传入的函数名，
#**values:就是关键字参数即key=value形式  也就是url_for(关键字，值)


#需注意 url_for(方法的名称) 和 app.route参数的关系是
# url_for(方法的名称) = app.route(参数名) url_for()函数的用法是以视图函数名，作为参数，
#返回对应的url ,_external=True 返回绝对地址
#使用url_for动态生成地址时，将动态部分作为关键字参数传入，
#  如 url_for('user',name='joho',_external=True) 返回 http:127.0.0.1:5000/user/joho
# 参看董伟明的书  test_request_context 帮助我们在交互模式下产生请求上下文

# HTTP方法  缺省就是默认的意思

# @app.route('/login',methods=['GET','POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()

    # else:
    #     return show_the_login_form()

def do_the_login():
    return 'do_the_login'

def show_the_login_form():
    return 'show_the_login_form'




# 静态文件
#一般是css,js文件，静态文件一般放在/static中  使用特定的‘static’端点就可以生成相应的URL
# url_for('static',filename='style.css')  这个静态文件在文件系统中的位置应该是static/style.css


#渲染模板 使用Jinja2模板引擎
#使用 render_template()方法可以渲染吗模板，只要提供模板名称和需要作为参数传递给模板的变量即可
from flask import render_template

# flask会在templates文件夹中寻找模板
# 在模板内部可以和访问get_flashed_message()函数一样访问request,session和g对象
#模板继承可以使每个页面的特定元素（如页头，导航和页尾）保持一致
#自动转义默认是开启的，可以使用Markup标记安全，或在模板中使用|safe过滤器。


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',name=name)


# 操作请求数据  在Flask中由全局对象request来提供请求信息  本地环境
#可以自己创建一个请求对象绑定到环境。单元测试解决方案是使用test_request_context()环境管理器。
# 通过使用with语句可以绑定一个测试请求，以便于交互

# with app.test_request_context('/hello',methods=['POST']):
#     assert request.path == '/hello'
#     assert request.method == 'POST'

# 另一种方式是把整个WSGI环境传递给request_context()方法

# with app.test_request_context(environ):
#     assert request.method == 'POST'

# 请求对象 首先从flask导入请求对象，通过使用method属性可以操作当前请求方法，通过使用
# form属性处理表单数据（在POST或PUT请求中传输的数据）




# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     return render_template('login.html',error=error)


# 文件上传
# 不要忘记在HTML表单中设置enctype='multipart/form-data'属性就可以了
#已经上传的文件被存储在内存或文件系统的临时位置。你可以通过请求对象files属性来访问上传的文件。
#每个上传的文件都存储在整个字典属性中，整个属性基本和标准Python file对象一样，
#另外多出一个用于上传文件保存到服务器的文件系统的save()方法

# @app.route('/upload'.methods=['GET','POST'])
# def upload_file():
#     if request.method == 'POST':
#         f = request.files['the_file']
#         f.save('/var/www/uploads/uploaded_file.txt')


# 如果想要知道文件上传之前在其客户端系统的名称，可以使用filename属性。但是注意这个值是可以伪造的
# 永远不要相信这个值，如果想要把客户端的文件名作为服务器的文件名，
# 可以通过Werkzeug提供的secure_filename()函数



from werkzeug.utils import secure_filename


@app.route('/upload',methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/') + secure_filename(f.filename)

# Cookies
# 要想访问cookies，可以使用cookies属性。可以使用相应对象的set_cookie方法来设置cookies.请求对象
#的cookies属性是一个包含了客户端传输的所有cookies的字典。在Flask中，如果使用会话，要么就不要直接
#使用cookies,因为会话比较安全

#读取cookies


# @app.route('/')
# def index():
#     username = request.cookies.get('username')

#存储cookies


from flask import make_response

# @app.route('/')
# def index():
#     resp = make_response(render_template(...))
#     resp.set_cookie('username','the username')
#     return resp

# 注意，cookies设置在相应对象上。通常只是从视图函数返回字符串。flask会把它们转换为响应对象。
#如果你想显性的转换，可以使用make_response()函数，然后再修改它
#使用延迟的请求回调方案可以在没有响应对象的情况下设置一个cookie.

#重定向和错误
#使用redirect()函数可以重定向，使用abort()可以更早退出请求，并返回错误代码

from flask import abort,redirect,url_for



# @app.route('/')
# def index():
#     return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()


def this_is_never_executed():
    return '重定向和错误处理'

# 它让一个用户从索引页重定向到一个无法访问的页面（401表示禁止访问）。
# 在缺省情况下每种出错代码都会对应仙逝一个黑白的出错页面，使用errorhandler()装饰器可以定义出错页面

from flask import render_template


@app.errorhandler(404)
def page_not_found(404):
    return render_template('page_not_found.html'),404

#注意 render_template()后面的404，这表示页面对就的错误代码是404，即页面不存在。缺省情况下200，表示一切正常、


#关于响应
#视图函数的返回值会自动转换为一个响应对象。如果返回值是一个字符串，那么会被转换为一个包含作为相应体的字符串，
# 一个200 OK出错代码和一个 text/html类型的响应对象。以下是转换的原则：
#1. 返回一个响应对象，直接返回它
# 2. 如果返回一个字符串，那么根据整个字符串和缺省参数生成一个用于返回的响应对象。
# 3. 如果返回一个元组，那么元组中的项目可以提供额外的信息。元组中必须至少包含一个项目，且项目应当由
# （response,status,headers)或（response,headers)组成。status的值会重载状态代码，
# headers 是一个由额外头部值组成的列表或字典
# 4. 如果以上都不是，那么flask会假定返回值是一个有效的WSGI应用并把它转换为一个响应对象

# 如果响应在视图内部掌控响应对象的结果，那么可以使用make_response()函数

# @app.errorhandler(404)
# def not_found(error):
#     return render_template('error.html'),404

# 可以使用make_reponse()包裹返回表达式，获得响应对象，并对该对象进行修改，然后再返回

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'),404)
    resp.headers['X-Something'] = 'A value'
    return resp




# 会话
#除了 请求对象之外还有一种称为session的对象，允许你在不同请求之间存储信息。这个对象相当于用
#密钥签加密的cookie，即用户可以查看你的cookie,但是如果没有密钥就无法修改它。
#注意，使用会话之前你必须设置高一二密钥



from flask import Flask,session,redirect,url_for,escape,request


app = Flask(__name__)

app.secret_key = b'_\mnm\23422./'



@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s'% escape(session['username'])
    return 'You are not logged in'




def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
      <form method="post">
         <p><input type=text name=username>
         <p><input type=submit value=Login>
      </form>
    '''


@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))

# 这里用到的escape()是用来转义的。如果不使用模板引擎就可以使用上例一样使用整个函数来转义。


# 如何生成一个好的密钥
# 生成随机的关键在于一个好的随机种子，因此一个好的密钥应当有足够的随机性。操作系统可以有
#多种方式基于密码随机生成器来生成随机数据。可以使用快捷方式为 flask.secret_key(或SECRET_KEY)生成值）

#基于cookie的会话的说明：flask会去除会话对象中的值，把值序列后存储到cookie中。在打开cookie的情况下，
#如果需要查找某个值，但是这个值在请求中没有持续存储的话，那么不会得到一个清晰的出错信息。请检查页面响应中
#的cookie的大小是否与网络浏览器所支持的大小一直。

#密钥除了缺省的客户端会话之外，还有很多flask扩展支持服务端会话。


# 消息闪现。
#flask 通过闪现系统来提供了一个易用的反馈方式。闪现系统的基本工作原理实在请求结束时，记录一个信息
# 提供且只提供下一个请求使用。通常通过一个布局模板来展现闪现的消息

#flash()用于闪现一个消息。在模板中，使用get_flashed_message()来操作消息


# 日志  几个日志调用示例

#1. app.logger.debug('a value for debugging')
# 2. app.logger.warning('a warning occurred (%d apples)',42)
# 3. app.logger.error('a error occured')

#logger 是一个标准的Logger 类


# 集成 WSGI中间件
# 使用flask扩展
# 部署到网络服务器




if __name__ == "__main__":
    app.run(debug=True)

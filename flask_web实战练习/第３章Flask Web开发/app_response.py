# 响应
#　视图函数的返回值会自动转为为一个响应对象，转换逻辑如下

# 1.如果返回的是一个合法的响应对象，它会从视图直接返回
# 2. 如果返回的是一个字符串，会用字符串数据和默认参数创建以字符串为主体，状态为200，MIME类型是text/html的werkzeug.wrappers.Response响应对象
#　３．如果返回的是一个元组，且元组中的ｕａｎｓｕ可以提供额外的信息。这样的元组必须是(response,status,headers)的形式，但是需要至少包含一个元素
# status值会覆盖状态代码，headers可以是一个列表或字典，作为额外的消息头

# 4.如果上述条件均不满足，flask会假设返回值是一个合法的WSGI应用程序，并通过Response.force_type(rv,request.environ)转换为一个请求对象


from flask import Flask, jsonify, render_template, make_response, url_for
from werkzeug.wrappers import Response
app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'),404

# 可以改写为显式的调用make_reponse的方式

@app.errorhandler(404)
def not_found1(error):
    resp = make_response(render_template('error.html'),404)
    return resp

# 第二种方法很灵活，可以添加一些额外的工作，比如设置cookie,头信息等

# API都是返回JSON格式的响应，需要包装jsonify.可以抽象一下，让Flask自动帮我们做这些工作


class JSONResponse(Response):
    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response,dict):
            response = jsonify(response)  #  dict----->json
        return super(JSONResponse,cls).force_type(response,environ)

app.response_class = JSONResponse


@app.route('/')
def hello_world():
    return {'message':'hello world!'}

@app.route('/custom_headers')
def headers():
    return {'headers':[1,2,3]},'201 created~~~~~',[('X-Request-Id','100')]



    # 安装httpie，可以替代curl，使用Python编写的，提供了语法高亮，json支持，可以方面集成到Python项目中


# 视图中也可以直接指定状态字符串，如使用'201 created'代替数字201

#　静态文件管理
# web应用大多会提供静态文件服务以便给用户更好的访问体验。静态文件主要包含css样式文件，javascript脚本文件，图片文件，字体文件等静态资源。
#　flask也支持静态文件访问，默认只需要在项目根目录下创建名字为static的目录，在应用中使用"/static"开头的路径就可以访问。但是为了获得
#　更好的处理能力，推荐使用Nginx或其他web服务器管理静态文件

# 不要直接在模板中写死静态文件路径，应该使用url_for生成路径，如　
url_for('static',filename='style.css')
# 生成的路径就是'/static/style.css'.当然也可以定制静态文件的真实目录：
app = Flask(__name__,static_folder='/tmp')


if __name__ =='__main__':
    app.run(host='0.0.0.0',port=8888)
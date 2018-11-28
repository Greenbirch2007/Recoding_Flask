# 自定义url转换器



import urllib
from  flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)


class ListConverter(BaseConverter): # 不继承是不可能的e
    def __init__(self,url_map,separaor='+'):
        super(ListConverter,self).__init__(url_map)
        self.separator = urllib.parse.unquote(separaor)

    def to_python(self, value):
        return value.split(self.separator)

    def to_url(self, values):
        return self.separator.join(super(BaseConverter,self).to_url(value) for value in values)

app.url_map.converters['list'] = ListConverter


@app.route('/list1/<list:page_names>/')
def list1(page_names):
    return 'Separator:{} {}'.format('+',page_names)


#
# @app.route('/list2/<list(separator=u"|"):pages_names>/')
# def list2(page_names):
#     return 'Separator:{} {}'.format('|',page_names)

# 自定义转换器需要继承值BaseConverter,要设置to_python,to_url两个方法

# 1.to_python,把路径转换成一个python对象
# 2. to_url,把参数转换成为符合url的形式

# http方法
#　http有多个访问方法，默认情况下，路由只回应get请求，但是通过app.route装饰器传递传递methods参数可以改变这个为ｘｎｇｉｗｅ

# get:获取资源，get操作应该是幂等的　（幂等表示咋相同的数据和参数下，执行一次或多次产生的效果是一样的）
# head :想要获取信息，但是只关心消息头。应用应该像处理get请求一样来处理，但是不返回实际内容
# ｐｏｓｔ:创建一个新的资源
# put:完整地替换资源或创建资源。put操作虽然有副作用，但是应该是幂等的
# delete:删除资源。delete操作虽然有副作用，但是应该是幂等的
# options:获取资源支持的所有http方法
# patch:局部更新，修改某个已有的资源


# 唯一url
# flask的url规则基于werkzeug的路由模块。这个模块背后的思想是基于apache以及更早的http服务器的主张，希望保证且唯一的url


@app.route('/projects/')
def projects():
    return '<h1>The project page </h1>'


# 像一个文件系统中的文件夹，访问一个结尾不带斜杠的url会被重定向到带斜杠的规范的url上去，这样也有助于避免搜索引擎同一个页面搜索两次

@app.route('/about')
def about():
    return 'The about page'

# url结尾不带斜线，很像文件的路径，但是当访问代谢县的url(/about/)是会产生一个404错误

@app.route('/login',methods=['GET','POST'])
# @app.route('/j/item/<id>',methods=['DELETE','POST'])
def pa():
    return '注册或删除'



if __name__ =='__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0',port=8888)
# 即插视图

#   即插视图的灵感来自Django的基于类而不是函数的通用视图方式，这样的视图就可以支持继承了。视图类型有两种
#　１．标准视图　　２．基于调度方法的视图

# 标准视图 需要继承flasl.view.View,必须实现dispatch_request.


from flask import Flask,request,render_template
from flask.views import  View


app = Flask(__name__,template_folder='../../templates')


class BaseView(View):
    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self,context):
        return render_template(self.get_template_name(),**context)

    def idspatch_request(self):
        if request.method != 'GET':
            return 'UNSUPPORTED!'

class Userview(BaseView):  #实例属性优先于类属性
    def get_template_name(self):
        return 'users.html'

    def get_user(self):
        return [
            {
                'username':'fake',
                'avatar':'http://www.baidu.com'
            }
        ]


app.add_url_rule('/users',view_func=Userview.as_view('userview'))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888)

# 模板存放在~/web_develop/templates下，使用__name__来获取模板目录，template_folder是相对于app.py文件的，需要设置成'../../templates'才能找到正确的模板目录


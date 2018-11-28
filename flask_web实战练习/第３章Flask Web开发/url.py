# 构造url
# 使用url_for构建url,它接受函数名作为第一个参数,也接受对应url规则的变量部分的命名参数，未知的变量部分会添加到url末尾作为查询参数。
#　构建url而不选择直接在代码中拼接url的原因有两个：
# 在为了有更改的时候只需要一次性修改url,而不用到处去替换；url构建会转义特殊字符和Unicode数据，这些工作不需要我们自己处理




from flask import Flask,url_for


app = Flask(__name__)

@app.route('/item/1')
def item(id):
    pass


with app.test_request_context():
    print(url_for('item',id='1'))
    print(url_for('item',i=2,next='/'))

# test_request_context帮助我们在交互模式下产生请求上下文
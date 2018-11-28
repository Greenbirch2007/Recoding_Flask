#! -*- coding:utf-8 -*-



from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True  # 配置管理

@app.route('/')
def hello_world():
    return '<h1> Hello world!</h1>'




# 动态url规则

@app.route('/item/<id>')
def item(id):
    return 'Item: {}'.format(id)

# 如果使用post方法，表单参数需要通过request.form.get('name')

if __name__ =='__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0',port=8888)
#　子域名
# 现在许多SaaS应用为用户提供一个子域名来访问，可以借助subdomain来实现同样的功能


from flask import Flask,g


app = Flask(__name__)
app.config['SERVER_NAME'] = 'example.com:8888'


@app.url_value_preprocessor
def get_site(endpoint,values):
    g.site  = values.pop('subdomain')


@app.route('/',subdomain='<subdomain>')
def index():
    return g.site

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888)


from flask import Flask, Blueprint
# import file.4



bp = Blueprint('user',__name__,url_prefix='/user')



@bp.route('/')
def index():
    return "User's Index page"

app = Flask(__name__)
app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888)
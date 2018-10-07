

#　练习查询结果，分页，然后返回到前端为json格式
import json
from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 显示中文

# 在Flask里 sqlachemy是非常方便的，但是假如数据量很大的话，
# 后台返回的json速度就很慢，很影响用户体验，所以用paginate来分页返回数据paginate(id, num)
#  #id为第几页 num表示一页有几条数据很明显
# 我们的页数应该是 [1,sum/num]所以在前台的页数应该是 1到 数据总数/一页的数据量例如 有7311条数据，
# 我们需要一页10条数据的话页数就是 1 ~ 732 因为还有 最后一页 只有一条数据
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/JS'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

Base = declarative_base()

# sqlalchemy 对已有表做操作需要先做一个映射类

class Js_infos(Base):
    __tablename__ = 'js_infos'
    id = Column(Integer,primary_key=True,nullable=False, autoincrement=True)
    coding = Column(String(11),nullable=True)
    location = Column(String(11),nullable=True)
    name = Column(Text,nullable=True)
    last_price = Column(Text,nullable=True)
    net_value = Column(Text,nullable=True)

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict

class Js_infos_finanData(Base):
    __tablename__ = 'js_infos_finanData'
    id = Column(Integer,primary_key=True,nullable=False, autoincrement=True)
    coding = Column(String(11),nullable=True)
    industry = Column(String(8),nullable=True)
    title = Column(String(50),nullable=True)
    last_price = Column(String(20),nullable=True)
    market_value = Column(String(11),nullable=True)
    share_nums = Column(String(30),nullable=True)
    returns_ratio = Column(String(6),nullable=True)
    min_callshares = Column(String(11),nullable=True)



#　字段必须一致！
@app.route('/js_infos_finanData/<int:id>/', methods=['GET'])
def index2(id):
    if id is None:
        id = 1
    num = db.session.query(Js_infos_finanData).count()
    print(num)
    pages = db.session.query(Js_infos_finanData).paginate(id, 18)
    return jsonify(bedict2(pages.items))
#　分页成功！
def bedict2(a):
    lic = []
    for item in a:
        lic.append(
            {
                'id': item.id,
                'coding': item.coding,
                'industry': item.industry,
                'title': item.title,
                'last_price': item.last_price,
                'market_value': item.market_value,
                'share_nums': item.share_nums,
                'returns_ratio': item.returns_ratio,
                'min_callshares': item.min_callshares,

            }
        )
    return lic



@app.route('/')
def index():
    return '<h1>"欢迎来到接口界面"</h1>'





# 这个视图函数成功
@app.route('/js_infos/<int:id>/', methods=['GET'])
def index1(id):
    if id is None:
        id = 1
    num = db.session.query(Js_infos).count()
    print(num)
    pages = db.session.query(Js_infos).paginate(id, 18)
    return jsonify(bedict1(pages.items))
#　分页成功！
def bedict1(a):
    lic = []
    for item in a:
        lic.append(
            {
                'id': item.id,
                'coding': item.coding,
                'location': item.location,
                'name': item.name,
                'last_price': item.last_price,
                'net_value': item.net_value,

            }
        )
    return lic









# 从数据库中一次全部查询展示成功
@app.route('/comments', methods=['GET'])
def comments():
    comments = db.session.query(Js_infos).all()
    result = []
    for comment in comments:
        result.append(comment.to_json())   # 用到了模型中的转换方法！　映射是成功的！　先做思考分页
    return jsonify(result), 200



if __name__ =='__main__':
    app.run(debug=True)


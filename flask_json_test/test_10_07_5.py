# 使用SQLAlchemy ORM进行一些基础的操作（建表,插入,查询,删除）



引入sqlalchemy包
from sqlalchemy import Table,Column, String, create_engine,MetaData,text
from sqlalchemy.orm import sessionmaker,mapper
from sqlalchemy.ext.declarative import declarative_base

连接数据库的相关参数
db_config={
    'user':'root',
    'passwd':'',
    'host':'localhost',
    'db':'test',
    'port':'3306',
    'charset':'utf8'
}
 
生成engine
query='mysql+mysqlconnector://%s:%s@%s:%s/%s?charset=%s'%(
    db_config['user'],
    db_config['passwd'],
    db_config['host'],
    db_config['port'],
    db_config['db'],
    db_config['charset']
)
engine=create_engine(query,echo=True)
 
定义表格（必须有主键）
Base=declarative_base()
class hehe(Base):
    __tablename__='hehe'
    a=Column(String,primary_key=True)
    b=Column(String)
    def __repr__(self):
        return('<hehe(a=%s,b=%s)>'%(self.a,self.b))
 
在建立engine以及定义表格的基础上，可以生成表格
### create table----------------------------------------------
Base.metadata.create_all(engine)
##-------------------------------------------------------------
 
生成session(需要engine) (session用于插入，查询等)
### create session
Session=sessionmaker(bind=engine)
session=Session()
 
批量插入
## insert new data to table
a=[1,2,3,4,5,6]
b=[6,7,8,9,0,1]
hehe_list=[hehe(a=str(a[i]),b=str(b[i])) for i in range(6)]
session.add_all(hehe_list)
session.commit()
 
单行插入
e_hehe=hehe(a='5',b='6')
session.add(e_hehe)
session.commit()
 
使用session.query进行查询的一些方法
#-------------------------------------------------------------
our_hehe=session.query(hehe).filter_by(a='1').all()[0]
#-------------------------------------------------------------
for instance in session.query(hehe).order_by(hehe.a):
    print(instance.a,instance.b)
#-------------------------------------------------------------
for a,b in session.query(hehe.a,hehe.b):
    print(a,b)
#-------------------------------------------------------------
for line in session.query(hehe.a,hehe.b).all():
print(line.a,line.b)
#-------------------------------------------------------------
from sqlalchemy.orm import aliased
hehe_alias=aliased(hehe,name='hehe_alias')
for row in session.query(hehe_alias,hehe_alias.a).all():
    print(row.hehe_alias)
##------------------------------------------------------------
 
query查询中使用过滤器(filter的一些方法) (即session.query.filter(……))
### Common Filter Operators------------------------------------
#equals:
# query.filter(User.name == 'ed')
#------------------------------------
# not equals:
# query.filter(User.name != 'ed')
#------------------------------------
# LIKE:
# query.filter(User.name.like('%ed%'))
#------------------------------------
# IN:
# query.filter(User.name.in_(['ed', 'wendy', 'jack']))
#------------------------------------
# NOT IN:
# query.filter(~User.name.in_(['ed', 'wendy', 'jack']))
#------------------------------------
# IS NULL:
# query.filter(User.name == None)
#------------------------------------

# 使用textual sql进行选择，允许用于自定义查询语句
res=session.query(hehe).from_statement(text("select * from hehe")).all()

# 删除行记录
x=session.query(hehe).filter(hehe.a=='1').one()
session.delete(x)

# 也可以是
session.delete(session.query(hehe).filter(hehe.a=='1').one())

# 最后，别忘了把session关闭
session.close()


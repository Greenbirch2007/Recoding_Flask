# 使用mysql

# 数据是动态网站的基础，如果把数据放进数据库，就可以通过数据库管理系统对数据进行管理。
#在 flask中，可以使用sqlalchemy或mongoEngine这样的OR(D)M.

# 安装mysql的驱动

# 设置应用账号和权限
# root的权限很大，不应该在web应用中直接使用此用户(root密码一般都会被写进应用的配置文件中)，应该使用一个单独的的用户，有三步
# １．创建一个数据库r
# 2. 创建一个用户，名为web，密码为web
# 3. 设置用户，用户web对数据库r有全部权限
# 用pymysql写原生语句
# 下面会编写一系列数据库开发的例子，为了重复利用，把常量放到独立的consts.py文件里面
# ymysql.Connect()参数说明
# host(str):      MySQL服务器地址
# port(int):      MySQL服务器端口号
# user(str):      用户名
# passwd(str):    密码
# db(str):        数据库名称
# charset(str):   连接编码
#
# connection对象支持的方法
# cursor()        使用该连接创建并返回游标
# commit()        提交当前事务
# rollback()      回滚当前事务
# close()         关闭连接
#
# cursor对象支持的方法
# execute(op)     执行一个数据库的查询命令
# fetchone()      取得结果集的下一行
# fetchmany(size) 获取结果集的下几行
# fetchall()      获取结果集中的所有行
# rowcount()      返回数据条数或影响行数
# close()         关闭游标对象

HOSTNAME = 'localhost'
DATABASE = 'r'
USERNAME = 'web'
PASSWORD = 'web'
DB_URI = 'mysql://{}:{}@{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,DATABASE)
# orm简介
# ORM,对象关系映射，通过它可以直接还是用Python类的方式做数据库开发，而不再直接写原生的sql语句。通过把表映射成类，把行作为实例，把字段作为属性，ORM在执行
# 对象操作的时候会把对应的操作转换为数据库原生语句的方式来完成数据库开发工作

#ORM的优点：1. 易用性 2.  性能损耗小  3. 设计灵活  4. 可移植性
# 使用sqlalchemy

# 连接数据库  首先要连接数据库
from sqlalchemy import create_engine
engine = create_engine('sqlite://',echo=False) #  如果需要详细的输出，可以设置echo=True
with engine.connect() as con:
    rs = con.execute('SELECT 1')
    print(rs.fetchone())

# create_engine传入了一个数据库的URI，sqlite://表示使用了一个sqlite的内存型数据库。
#    dialect+driver://username:password@host:port/database
#
# dialect是数据库的实现，drive是python对应的驱动。如果不指定，会默认mysqldb驱动

# 使用原生sql  把之前的curd改写成使用sqlalchemy

# 它与之前的mysqldb的例子不同之处在于，结果通过返回值获取，不再需要执行
# 使用表达式  sqlalchemy支持使用表达式的方式来操作数据库（exp_sql） 跳过
# 使用ORM,SHI SQLALCHEMY
# 定义的User类会生成一张表，__tablename__的值就是表明
# 通过sessionmakeer创建一个会话，会话提供了事务控制的支持。模型实例对象本身独立 存在，如果要让其他修改(创建)生效，需要吧他们加入某个会话；如果不需要
# 对其生效就从会话中由session管理的实例对象。执行session.commit()时修改被提交到数据库，执行session.rollback()可以回滚变更

# 数据库管理  用户量大，并发高时，不推荐使用外键来关联，数据的一致性和完整性问题可以通过事务保证
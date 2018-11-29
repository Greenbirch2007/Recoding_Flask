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

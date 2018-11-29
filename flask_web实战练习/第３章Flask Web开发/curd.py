# 数据库操作主要是CRUD为主，create(创建),read(读取),update(更新),delete(删除)的缩写




import pymysql
from consts import HOSTNAME,DATABASE,PASSWORD,USERNAME

con = pymysql.connect(HOSTNAME, USERNAME, PASSWORD, DATABASE)


with con as cur:
    cur.execute('drop table if exists users')
    cur.execute('create table users(id int primary key auto_increment,name varchar(25))')
    cur.execute("insert into users(name) values('xiaoming')")
    cur.execute("insert into users(name) values('wanglong')")
    cur.execute('select * from users')


    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.execute('update users set name=%s where id = %s',('ming',1))
    print('Number of rows updated:',cur.rowcount)

    cur = con.cursor(pymysql.cursors.DictCursor)
    cur.execute('select * from users')

    rows = cur.fetchall()
    for row in rows:
        print(row['id'],row['name'])


# 这次使用with语句，connect的__enter__方法返回了游标，在wih中执行结束，它会判断当前是否有错误，有错误就回调，没有则进行事务提交。无须进行异常处理


# 事务提交和回滚
# 事务主要用于处理操作量大，复杂度高的数据。如果操作的是一系列的动车，比如删除一个用户，不仅需要删除用户表中对应的记录，也要删除和用户表关联的表中的对应的数据，
# 甚至还有其他业务上的需要。这个时候事务处理可以用来维护数据库的完整性，保证成批的sql语句要么全部执行，要么全部执行

# mysql的innodb引擎支持事务，而默认的myisam的引擎不支持，需要根据业务来取舍

# ORM简介
# 项目越大，原生的sql语句不再适用了
#
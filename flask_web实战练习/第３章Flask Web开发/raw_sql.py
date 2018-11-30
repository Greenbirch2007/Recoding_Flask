

import pymysql
from sqlalchemy import create_engine
from consts import DB_URI

# DB_URI= 'mysql+pymysql://root:123456@localhost/r'

eng = create_engine(DB_URI)

with eng.connect() as cur:
    cur.execute('drop table if exists users')
    cur.execute('create table users(id int primary key auto_increment,name varchar(25))')
    cur.execute("insert into users(name) values('xiaoming')")
    cur.execute("insert into users(name) values('wanglong')")
    cur.execute('select * from users')


    rs = cur.execute('select * from users')
    for row in rs:
        print(row)

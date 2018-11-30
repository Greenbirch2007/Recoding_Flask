#
#
# from sqlalchemy import  create_engine,Table,MetaData,Column,Integer,String,tuple_
# from sqlalchemy.sql import select,asc,and_
#
# from consts import DB_URI
#
#
# eng = create_engine(DB_URI)
#
# meta = MetaData(eng)
#
# users = Table(
#     'Users',meta.
#     Column('id',Integer,primary_key=True,autoincrement=True)
#     Column('name',String(50),nullable=False),
#
# )
#
# if users.exists():
#     users.drop()
#
#
# users.create()
#
# def execute(s):
#     print('-'*20)
#     rs = con.execute(s)
#     for row in rs:
#         print(row['id'],row['name'])
#
# with eng.connect() as con:
#     for username in ('xiaoming','mingming','lilei'):
#         user = users.insert().values(name=username)
#         con.execute(user)
#
#     stm = select([users]).limit(1)
#     execute(stm)
#
#     k = [(2,)]
#
#     stm = select([users]).where(tuple_(users.c.id).in_)
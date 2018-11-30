

from sqlalchemy import create_engine,Column,Integer,String,Sequence

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import and_,or_
from sqlalchemy.orm import sessionmaker



from consts import DB_URI


eng = create_engine(DB_URI)
Base = declarative_base()

class User(Base):
    __table__ = 'users'

    id = Column(Integer,Sequence('user_id_seq'), primary_key=True,autoincrement=True)
    name = Column(String(50))


Base.metadata.drop_all(bind=eng) # 删除表
Base.metadata.create_all(bind=eng)  # 建表

Session = sessionmaker(bind=eng)
session = Session()

session.add_all([User(name=username) for username in ('jim','green','red')])
session.commit()


def get_result(rs):
    print('-'*20)
    for user in rs:
        print(user.name)
sqU = session.query(User)
rs = sqU.all()

get_result(rs)
#
# rs = sqU.filter(User.id.in_([2,]))
#

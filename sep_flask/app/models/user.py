from sqlalchemy import Column, Integer, String, SmallInteger
from werkzeug.security import generate_password_hash

from app.models.base import Base, db


class User(Base):# User还需要继承一些基类，具有一些特征！
    id = Column(Integer,primary_key=True)
    email = Column(String(24),unique=True,nullable=False)
    nickname = Column(String(24),unique=True)
    auth = Column(SmallInteger,default=1)
    _password = Column('password',String(100))



    @property            #------>get (接收原始密码)
    def password(self):
        return self._password

    @property           # --->set
    def password(self,raw):   #(对密码进行加密)
        self._password = generate_password_hash(raw)



    # User模型的注册方法
    @staticmethod  # 在类使用静态方法
    def register_by_email(nickname,account,secret):
        # 注册用户，就是在数据库中新增一个用户
        with db.auto_commit():
            # 这里实例化一个User模型
            user = User()
            user.nickname = nickname
            user.email = account
            user.password = secret
            db.session.add(user)
# 想让sqlalchemy这样的第三方插件能够有效，必须在flask的核心对象app处进行注册（蓝图也是要注册才能用的）
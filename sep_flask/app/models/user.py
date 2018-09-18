
from sqlalchemy import Column, Integer, String, SmallInteger
from werkzeug.security import generate_password_hash
# 个性化处理好客户模型
from app.models.base import Base, db


class User(Base):
    id = Column(Integer,primary_key=True)
    email = Column(String(24),unique=True,nullable=False)
    nickname = Column(String(24),unique=True)
    # 等级权限 普通用户和管理员之分
    auth = Column(SmallInteger,default=1)
    _password = Column('password',String(100))

    @property   # 获得明文密码 （get）
    def password(self):
        return self._password

    @password.setter   # 对明文密码加密（set）
    def password(self,raw):
        self._password = generate_password_hash(raw)


    # 为User模型建立一个注册的模型

    @staticmethod  #设置静态方法
    def register_by_email(nickname,account,secret):
        with db.auto_commit():
            # 实例化 一个User模型
            user = User()
            user.nickname = nickname
            user.email = account
            user.password = secret
            db.session.add(User)


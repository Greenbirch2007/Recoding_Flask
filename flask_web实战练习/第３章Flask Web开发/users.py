#! coding=utf-8



from ext import db


class User(db.Model):
    __table__ = 'user'

    id = db.Column(db.Integer,db.Sequence('user_id_seq'), primary_key=True,autoincrement=True)
    name = db.Column(db.String(50))
    def __init__(self,name):
        self.name = name





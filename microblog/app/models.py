

from flask_login._compat import unicode

from app import db, lm
import hashlib
md5 = hashlib.md5()

class User(db.Model):
    dis_authenticated = True
    is_active = True


    is_anonymous = False

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    # @property
    # def is_authenticated(self):
    #
    # @property
    # def is_activate(self):
    #
    # @property
    # def is_anonymous(self):
    #     return False

    def get_id(self):
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id)



    def __repr__(self):
        return '<User %r>' % (self.nickname)
    def avatar(self,size): \
            return 'http://www.gravatar.com/avatar/' + md5(self.email).hexdigest() + '?d=mm&s=' + str(size)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)
@lm.user_loader
def load_user(id):
    return User.query.get(int(id))
from flask_wtf import Form
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length

from app.models import User


class LoginForm(Form):
    openid = StringField('openid',validators = [DataRequired()])
    remember_me = BooleanField('remembe_me',default=False)


class EditForｍ(Form):
    nickname = StringField('nickname', validators=[DataRequired()])
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])

    def __init__(self,origin_nickname,*args,**kwargs):
        Form.__init__(self,*args,**kwargs)
        self.origin_nickname = origin_nickname

    def valiate(self):
        if not Form.validate(self):
            return False
        if self.nickname.data == self.origin_nickname:
            return True
        user = User.query.filter_by(nickname=self.nickname.data).first()
        if user != None:
            self.nickname.errors.append('This nickname is already in use. Please choose another one.')
            return False
        return True


class PostForm(Form):
    post = StringField('post', validators=[DataRequired()])

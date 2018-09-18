
from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, length, Email, Regexp, ValidationError

from app.libs.enums import ClientTypeEnum

from app.models.user import User

# 这里只是通用的参数 ，个性化的注册参数就需要重新编写一个类
class ClientForm(Form):
    account = StringField(validators=[DataRequired(),length(min=5,max=32)])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    #写一个自定义的验证器  尝试将客户传过来的数字转换成枚举类型
    def validate_type(self,value):
        try:  # 必须用.data
            client = ClientTypeEnum(value.data)

        except ValueError as e :
            raise e
        # 将枚举类型数据返回给type
        self.type.data = client

# 编写个性化的注册参数
class UserEmailForm(ClientForm):
    account = StringField(validators=[Email(message='invalidate email')])
    # password can only include letters,numbers and "_"
    secret = StringField(validators=[DataRequired(),Regexp(r'^[A-Za-z0-9_*&$#@{6,22}]$')])
    nickname = StringField(validators=[DataRequired(),length(min=2,max=22)])
    # 还要验证账号是否已经注册过！
    def validate_account(self,value):
        # 用查询数据库的形式验证是否重复
        if User.query.filter_by(email = value.data):
            raise ValidationError







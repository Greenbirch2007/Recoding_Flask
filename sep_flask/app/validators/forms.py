

from wtforms import Form, StringField, IntegerField


# 客户端表单的类---->表单的类型数据
from wtforms.validators import DataRequired, length, Email, Regexp, ValidationError

from app.libs.enums import ClientTypeEnum

# 实现了一个类型的验证器 再到client视图函数中取使用这个验证器
from app.models.user import User

# 可以简化代码量
class ClientForm(Form):
    account = StringField(validators=[DataRequired(),length(min=2,max=32)])  #用户名
    secret = StringField()  #密码
    type = IntegerField(validators=[DataRequired()])  # 客户端类型
    # 所谓校验客户端注册的类型
    # 对于注册和登录这两个视图函数，最要提供同意的接口！统一的类？
    def validate_type(self,value):
        #尝试把客户传递过来数字转换为枚举类型
        try:
            client = ClientTypeEnum(value.data)  #解决了表单提交的数据类型的转换确认
        except ValueError as e:
            raise e
        self.type.data = client   # 这里把枚举类型对象client 赋值给type,后面用type就可以直接用到枚举类型呢


class UserEmailForm(ClientForm):

    account = StringField(validators=[
        Email(message='invalidate email')
    ])
    secret = StringField(validators=[
        DataRequired(),
        # password can only include letters , numbers and "_"
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')
    ])
    nickname = StringField(validators=[DataRequired(),
                                       length(min=2, max=22)])

    # 不光要验证这个注册信息是否合法，还要验证这个账号是否已经注册了（查询数据库）
    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError()
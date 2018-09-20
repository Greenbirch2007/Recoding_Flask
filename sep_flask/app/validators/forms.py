

from wtforms import Form, StringField, IntegerField


# 客户端表单的类---->表单的类型数据
from wtforms.validators import DataRequired, length

from app.libs.enums import ClientTypeEnum

# 实现了一个类型的验证器 再到client视图函数中取使用这个验证器
class ClientForm(Form):
    account = StringField(validators=[DataRequired(),length(min=2,max=32)])  #用户名
    secret = StringField()  #密码
    type = IntegerField(validators=[DataRequired()])  # 客户端类型
    def validate_type(self,value):
        #尝试把客户传递过来数字转换为枚举类型
        try:
            client = ClientTypeEnum(value.data)  #解决了表单提交的数据类型的转换确认
        except ValueError as e:
            raise e
            pass
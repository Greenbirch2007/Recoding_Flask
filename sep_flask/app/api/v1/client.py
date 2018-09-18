
from app.libs.reqprint import Redprint
from flask import request

from app.libs.enums import ClientTypeEnum
from app.models.user import User
from app.validators.form import ClientForm, UserEmailForm

api = Redprint('book')


#编写视图函数
@api.route('/register',method=['POST'])
def create_client():
    data = request.json # data的是原始参数
    form = ClientForm(data=data)  # form中的数据都是经过校验的
    if form.validate():
        promise = {
            ClientTypeEnum.USER_EMAIL:__register_user_by_email
        }
        promise[form.type.data]()

    return 'success'


    # 进行校验  为不同的客户端编写不同的注册代码
    #  创建一个模型，在用户的模型中完成一个相关的注册
    # 两种接收参数的形式：
    #1.request.json  2. request.args.to_dict()
    # 注册 登录
    # 参数 校验 接收参数
    # WTForms 验证表单
    # 表单 json
    # 网页 移动端
# 从form的验证器中得到注册的信息
# 使用邮箱，密码注册，当然就没有nickname的验证部分？在ClientForm中
# 总 分

def __register_user_by_email():
    #实例化一个UserEmailForm()
    form = UserEmailForm(data=request.json)
    if form.validate():

        User.register_by_email(form.nickname.data,form.account.data,form.secret.data)



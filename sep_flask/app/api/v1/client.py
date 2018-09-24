from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm

api = Redprint('client')

@api.route('/register',methods=['POST'])
def create_client():
    data = request.json()   # 在这里接收参数

    form = ClientForm(data=data)   # 在这里校验参数（类似爬虫里面的解析） 在WTForms源码中
    if form.validate():  # 执行校验
        #如果通过校验了就可以进行注册了 羡慕就是注册方法，用字典触发字典的值，也就是那个注册函数
        promise = {
            ClientTypeEnum.USER_EMAIL:__register_user_by_email
        }
        promise[form.type.data]() # 注册方式，枚举类型，作为键传入，然后通过字典，拿到字典的值，从而完成注册函数。都是把函数拆分括号玩的
    return '注册成功'
# 总  分   restful 要求输入（注册），输出（反应到前端）都是json格式的

#创建一个用户的模型，在模型中完成相关的注册

def __register_user_by_email(form): # 从form的验证器中获取注册模型需要参数
    #实例化一个UserEmailForm  # request.json['nickname']
    form = UserEmailForm(data=request.json)
    if form.validate():
        User.register_by_email(form.nickname.data,form.account.data,form.secret.data)
    pass
    #如果是后一种接收参数的方式，验证参数的data方式只需要传入data即可
    # data = request.args.to_dict()
    # form = ClientForm(data)


#客户端注册时接收参数有两种方式：1. 使用flask中的 reuqest.json  2.request.args.to_dict()


#客户注册data ---->表单form(验证之后)————————>用户模型
# 表单类是一块  account,secret,type
# 数据模型类是一块  nickname ,account,secret
#两者有不一致处！



#form-data  表单
#raw json(application/json)


# 表单 json

# 网页 移动端
# 参数  校验 接收参数
# WTForms 验证表单



    # 1.注册的参数 2. 校验参数 ---> WTForms 验证表单 3. 接收参数 这三个问题
# 最好对于  注册和登录都提供一个同一的接口（url口子么）在api/validators/forms.py中定义了验证器，所以在创建客户的
#视图函数中使用这个验证器
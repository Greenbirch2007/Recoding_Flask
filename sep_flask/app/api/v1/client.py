from app.libs.redprint import Redprint

api = Redprint('client')

@api.route('/register',methods=['POST']) #
def create_client():
    # 1.注册的参数 2. 校验参数 ---> WTForms 验证表单 3. 接收参数 这三个问题
    pass






#form-data  表单
#raw json(application/json)


# 表单 json
# 网页 移动端






# 最好对于  注册和登录都提供一个同一的接口（url口子么）
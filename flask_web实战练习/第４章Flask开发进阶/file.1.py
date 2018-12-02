# 第4章 flask开发进阶
# flask的信号机制.利用信号可以实现一部分的业务解耦


# flask的信号机制
# flask-login中的信号
# flask-login提供了UserMixin,有一些用户相关的属性
# is_authenticated:是否被验证
# is_activate:是否被激活
# is_anonumous:是否是匿名用户
# get_id(): 获得用户的id,并转换为Unicode类型
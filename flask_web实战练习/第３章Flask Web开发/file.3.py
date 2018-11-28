# 跳转和重定向
#　　跳转(状态码３０１)多用于旧网站在废弃前转向新网址以保证用户的访问，有网页被永久性移走的概念。
#　重定向(状态码３０２)表示页面是暂时性额转转移。但是页不建议经常性使用重定向
#　在flask中，跳转和重定向都是通过flask.redirect实现的



from flask import redirect

redirect(location) # 默认是３０２
redirect(location,code=301) # 通过code参数来指定状态码

# 首先存放配置的config.py

DEBUG=False

try:
    from local_settings import *
except ImportError:
    pass

# local_settings.py文件是可选存在的，它不进入版本库。这是常用的通过本地配置文件重载版本库配置的方式

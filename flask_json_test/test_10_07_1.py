# 1.将字典转换成JSON数据格式：
import json


s= ['张三','姓名','年龄']
t = {}
t['data'] =s
t_json = json.dumps(t,ensure_ascii=False)
print(t)
print(t_json)
#2.将列表转换成JSON数据格式：
print(88*'~')
s_json = json.dumps(s,ensure_ascii=False)
print(s_json)


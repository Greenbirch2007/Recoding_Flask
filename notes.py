






import os

themes = ['１．安装','2.程序的基本结构','3.模板','4.ｗｅｂ表单','5.数据库','6.电子邮件','７．大型程序的结构','８．用户认证','９．用户角色','１０．用户资料','１１．博客文章','12.关注者','１３．用户评论','１４．应用编程接口','１５．测试','１６．性能','１７．部署','１８．其他资源']

base = "/home/karson/Recoding_Flask/Flask Web开发基于Python的web应用开发/"
for i in themes:
    file_name = base + str(i)
    os.mkdir(file_name)
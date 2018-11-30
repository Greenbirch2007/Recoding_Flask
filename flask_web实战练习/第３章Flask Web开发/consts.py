



HOSTNAME = 'localhost'
DATABASE = 'r'
USERNAME = 'root'
PASSWORD = '123456'
DB_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,DATABASE)

#
# pymysql
#     mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]

# 错误的格式
# mysql:pymysql//root:123456@localhost/r

# 可用
#'mysql+pymysql://root:123456@localhost/r'
# print(DB_URI)

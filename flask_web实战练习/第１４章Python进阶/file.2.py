# 具名元组


# collection.namedtuple是一个工厂函数， 它可以用来构建一个带字段名的元组和一个有名字的类——这个带名字的类对调试程序有很大帮助。
# 而且用namedtuple构建的类的实例所消耗的内存和元组是一样的， 因为字段名都被存在对应的类里面。这个实例和消耗的对象实例比起来也要小一点，
# 因为Python不会用__dict__来存放这些属性。

from collections import namedtuple

City = namedtuple('City','name country population coordinates')
tokyo = City('Tokyo','JP',36.9323,(35.68,139.11))
print(tokyo)
print(tokyo[1])
print(tokyo.name)

# (1) 创建一个具名元组需要两个参数,一个是类名,另一个是各字段的名字.后者可以是
#由数个字符串组成的可迭代对象,或由空格分隔开的字段组成的字符串
# (2) 存放在对应字段里的数据要以一串参数的形式传入构造函数中(元组的构造函数只接受单一的可迭代对象)
# (3) 我们可以通过字段名或位置信息来获取一个字段信息
# 处理从普通元组那里继承来的属性之外,具名元组还有一些自己专属的属性,比如
# _fields类属性,返回字段名

print(City._fields)
LatLong = namedtuple('LatLong','lat long')
delhi_data = ('Delhi NCR','IN',21.93,LatLong(28.6,77.88))
print(delhi_data)
# print(City._make('delhi_data'))
delhi = City._make(delhi_data)
print(delhi)
# print(delhi._asdict())

# _fields属性是一个包含这个类所有字段名称的元组
#　用_make()通过接受一个可迭代对象来生成这个类的一个实例，它的作用和City(*delhi_data)是一样的
# _asdict()把具名元组以collections.OrderedDict的形式返回.它的第二个角色是充当一个不可变的列表

#user.age可以明确告诉开发者它的意思，同事还可以非常方便地把数据库等来源获得的数据转化为User对象


cursor = conn.cursor()
curso.execute('selecct name,age,location,phone from users')
for user in map(Use._make,cursor.fetchall()):
    print(user.name,user.phone)

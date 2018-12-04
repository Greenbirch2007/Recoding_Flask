# #　第14章 Python进阶
#
# #　functools模块 中包含了一系列操作其他函数的工具
#
# #　1.partial.partial可以重新定义函数签名,也就是咋执行函数之前把一些参数预先传给函数,待执行时传入的参数数量会减少
#
# # import functools
# #
# # def f(a,b=3):
# #     return a+b
# #
# # f2 = functools.partial(f,1)
# # print(f2())
# # print(f2(5))
# # print(f2())
#
# #　２．wraps: 把被封装函数的__name__,__module__,__doc__,__dict__复制到封装函数中，这样咋未来排错或函数自省的时候能够获得正确的源函数的对应属性
# # 所以使用wraps是一个好习惯，第一个示例是不适用wraps的例子
#
# import functools
#
# def deco(f):
#     def wrapper(*args,**kwargs):
#         return f(*args,**kwargs)
#     return wrapper
#
#
#
# @deco
# def func():
#     '''This is __doc__'''
#     return 1
#
#
# # print(func.__doc__)
# # print(func.__name__)
#
# # 可以发现func.__doc__和func.__name__等都是错误的，他们错误地使用装饰器的对应属性．正确的方法是使用wraps拷贝源函数属性：
#
# def  deco2(f):
#     @functools.wraps(f)
#     def wrapper(*args,**kwargs):
#         return f(*args,**kwargs)
#
#     return wrapper
#
# @deco2
# def func():
#     '''This is __doc__'''
#     return 1
#
# # print(func.__doc__)
# # print(func.__module__)
# # print(func.__dict__)
#
# # 3.  total_ordering.对比自定义对象需要添加__lt__,__le__,__gt__,等．如果使用total_ordering,只需要定义__eq__,以及＿＿lt__,__le__,__gt__,__ge__四种方法之一就可以了
#
# # 注意，object类是python中所有类的基类，如果定义一个类时没有指定继承哪个类，则默认继承Object
# # object类定义了所有类的一些公共方法　
# # object类没有定义__dict__,所以不能对object类实例对象尝试设置属性值
# # python3中，所有类都默认继承了object类
#
#
#
#
#
#
#
#
#
# @functools.total_ordering
# class Size(object):
#     def __init__(self,value):
#         self.value = value
#
#     def __lt__(self, other):
#         return self.value < other.value
#
#     def __eq__(self, other):
#         return self.value == other.value
#
#
# # t = Size(3) > Size(1)
# # print(t)
# # total_ordering会自动设置未定义额三种特殊方法
#
# # 4. cmp_to_key:python2的sorted函数除了通过指定key参数的值作为依据来排序,还支持cmp参数
#
#
# # def numeric_compare(x,y):
# #     return x[1] - y[1]
# #
# # sorted(objs,cmp=numeric_compare)
#
#
# # collections模块中包含了5个高性能的数据类型
#
# # 1. Counter:一个方便,快速计算的计时器工具
#
#
import collections
#
words = ['a','b','a','c','d','c']
# cnt = collections.Counter(words)
# # print(cnt.most_common(2))
#
# # Counter除了可以接受多种类型的参数以及方便获得根据计数后的排序外,还以一个重要功能功能就是和其他Counter实例做计算
# # 和，差，交集，并集都可以计算
# # cnt2 = collections.Counter('aldcdae')
# # print(cnt+cnt2)
# # print(cnt-cnt2)
# # print(cnt&cnt2)
# # print(cnt|cnt2)
#
# # 2.deque:一个双端队列，能够在队列两端添加或删除队列元素．它支持线程安全，能够有效利用内存．无论从队列的哪端入队或出队，性能都能够接近与O(1)
# w = collections.deque('wwww')
# t = collections.deque('tot')
# d = collections.deque('ab')
# print(d)
# d.append('c')
# print(d)
# d.appendleft('e')
# print(d)
# d.pop()
# print(d)
# d.popleft()
# print(d)
# d.extend(t)
# d.extend(w)
# # d.extend(d)
# print(d)
# d.extendleft(w)
# print(d)
#
# # 除了列表操作，deque还支持队列的旋转操作
# d.rotate(2)
# print(d)
# # 如果rotate的参数N的值大于0,表示将右端的N个元素移到左端，否则相反．
# # 虽然python内置的数据结构list也支持类似的操作,但是当遇到pop(0)和insert(0,v)这样既改变了列表长度又改变其元素位置的操作时,其复杂度就变为O(n)了
#
# # 3. defaultdict. defaultdict简化了处理不存在键的场景.如果不使用defaultdict,对一个单词的计数要这样实现:
#
d = {}
print(words)

for w in words:
    if w in d:
        d[w]  += 1

    else:
        d[w]  = 1

# 如果使用defaultdict,就不需要判断字典中是否已经存在这个键
d = collections.defaultdict(int)
for w in words:
    d[w] += 1
    # print(w)
    # print(d)

# defaultdict参数就是值的类型,还可以使用自定义类型.下面演示一个插入后自动排序的自定义列表类型
print(88*'~')
import bisect

class bisectedList(list):
    def insort(self,arr):
        bisect.insort_left(self,arr)

d = collections.defaultdict(bisectedList)
print(d)
d['l'].insort(1)
d['l'].insort(3)
d['l'].insort(9)
print(d)
print(d['l'])

# defaultdict对于不同的数据结构都有默认值,比如int的默认值是0


d = collections.defaultdict(int)
print(d)
print(d['c'])

# 如果想使用其他默认值,可以借用匿名函数lambda来实现:
d = collections.defaultdict(lambda x=10:x)
print(d['c'])


# 4. OrderedDict: Python的dict结构是无序的

d = dict([('a',1),('b',3),('c',2)])
print(d)
for k,v in d.items():

    print(k,v)

# 在一些场景下,是必须要有顺序的,可以使用OrderedDict这个数据结构来保证字典键值对的顺序

print(88*'~')

d = collections.OrderedDict([('a',1),('b',3),('c',2)])
print(d)
for k,v in d.items():
    print(k,v)


# 5. namedtuple.namedtuple能创建可以通过属性访问元素内容的扩展元组.使用namedtuple能创建更健壮,可读性更好的代码.假设不使用namedtuple,查询数据库获得
#如下一条记录

user  = {'xiaoming',23,'beijing','0101214456'}

# 需要通过索引获取对应的内容，比如想要知道用户的年龄，就得使用user[1].在大型应用中使用这种不明显的方式会加大项目的复杂度和维护成本，因为每个看到
# 这段代码的人都得去找到user的定义,使用namedtuple则让代码非常清晰


User = collections.namedtuple('User','age name location phone')
user = User('xiaoming',23,'beijing','0101214456')
print(user.age)
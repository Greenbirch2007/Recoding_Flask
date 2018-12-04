
# 命名

# 1.变量,函数,方法和包名使用全小小和下划线的组合
# 2.类和异常使用大写字母开头的单词
# 3. 受保护的或内部方法使用一个下划线开头
# 4. 私有方法使用两个下划线开头
# 5. 常量使用全大写的字母和下划线的罪恶和
# 6. 尽量不要使用单个字符的变量,除非上下文非常清晰(如列表解析中作为中间变量的情况)
# 7. 避免多余的标签.如果类或包的名字已经包含对应的单词,那么对应的属性或方法上的就不用出现了
# 8. 动词和形容词放在名词之后
# 9.使用更容易理解的动作,比如设置属性,使用'user.xxx=23',而不要使用'user.set_xxx(23)'

# 使用join连接字符串

my_list =['x','t','w','q']
r = []
for c in my_list:
    r.append(c)

print(''.join(my_list))
# 定义类的__str__/___repr__方法

# 自定义的默认的__str__方法的实现是无意义的


class Board(object):
    def __init__(self,id,name):
        self.id = id
        self.name = name


ba = Board(1,'最新热评榜单')
print(ba)

print('~'*88)
# 好的习惯是自定义__str__,__repr__方法,提供有价值的输出


class Bo(object):
    def __init__(self,id,name):
        self.id = id
        self.name = name


    def __str__(self):
        return '({},{})'.format(self.id,self.name)

    def __repr__(self):
        return '{}(id={},name={})'.format(self.__class__.__name__,self.id,self.name)

ba = Bo(1,'最新热评榜单')
print(ba)
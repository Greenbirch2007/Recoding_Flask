# # 1. 使用next获取循环中符合条件的值
# #通常，要从一个循环中找到符合条件的值，会使用如下方法
#
#
# # a = -1
# # for i in  range(1,10):
# #     if not i % 4:
# #         a = i
# #         print(i)
# #         break
#
# a= next((i for i in range(1,10) if not i%4),-1)
# print(a)


# 执行调用直到某种情况结束

#
# while True:
#     block = f.read(32)
#     if block =='':
#         break
#     blocks.append(block)


from functools import partial

blocks = []

for block in iter(partial(f.read,32),''):
    blocks.append(block)

# 善用for ...else句式，寻找符合条件的序列的索引值方法如下


def find(seq,target):
    for i,value in enumerate(seq):
        if value == target:
            break
    else:
        return -1
    return i


# 最简单的缓存实现

# 使用装饰器进行花奴你


def cache(func):
    saved = {}
    def newfunc(*args):
        if args in saved:
            return saved[args]
        result = func(*args)
        saved[args] = result
        return result
    return newfunc

@cache
def web_lookup(url):
    return urllib.urlopen(url).read()

# 从python３　移植

#　partialmethod  是作用于类方法的patial函数


def get_name(self):
    return self._name


class Cell(object):
    def __init__(self):
        self._alive  = False

    @property
    def alive(self):
        return self._alive

    def set_state(self,state):
        self._alive = bool(state)
    set_alive = partialmethod
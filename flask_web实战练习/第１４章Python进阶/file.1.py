#　第14章 Python进阶

#　functools模块 中包含了一系列操作其他函数的工具

#　1.partial.partial可以重新定义函数签名,也就是咋执行函数之前把一些参数预先传给函数,待执行时传入的参数数量会减少

# import functools
#
# def f(a,b=3):
#     return a+b
#
# f2 = functools.partial(f,1)
# print(f2())
# print(f2(5))
# print(f2())

#　２．wraps:
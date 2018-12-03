#　使用 asyncio
#　python2 对协程的支持是通过生成器实现的，利用yield实现生产者/消费者模式的例子

#　python3.4  asyncio被纳入了标准库，它提供了使用协程比阿尼额单线程并发代码，通过I/O多线路复用访问套接字和其他资源，运行网络客户端和服务器端等．
#　python3.5  添加了async和await这两个关键字，字词，协程成为新的语法，而不再是一种生成器类型了．
#　I/O 多路复用与协程的引入，可以极大提高高负载下程序的I/O性能



#　async/await


#　使用async用于声明一个协程:
async def foo():
    pass


#　在普通的函数前加上async关键字后,这个函数就变成了一个协程
#　await表示等待另一个协程执行完成返回,获取协程执行结果,它必须在协程内才能使用
# async的使用简化了asyncio.coroutine;await的使用简化了yield from

#　还有两个关键字
#　1. async for : 异步迭代器语法.为了支持异步迭代,异步对象需要实现__aiter__方法,异步迭代器需要实现__anext__方法,停止
#　迭代需要在__anext__方法内抛出StopAsyncIteration异常

#　2. async_with:异步上下文管理器语法.为了支持上下文管理器,需要实现__aenter__和__aexit__方法

#　除了使用事件循环,采用原来的send(None)方式也是可以的
'''
什么是生成器
假如这是一个列表的生成式 a = [x*2 for x in range(1000000)] 当创建非常多的数据时
需要的内存太大了,就不适合这样创建,有可能会直接崩溃
这时就出现了生成器
他能生成你想要的值,在你用的时候,去根据你的计算方式,再去生成,每次用的时候就创建一个
'''

print("=========================方式一")
#创建生成器的第一种方式
#列表生成式的中括号换成小括号
l = (i for i in range(1, 10000000) if i % 2 == 0)

print(next(l))
print(next(l))
print(l.__next__())  #方式等于next(l)

# for i in l:
#     print(i)

print("=========================方式二")
#创建生成器的第二种方式
# yied, 可以去阻断当前的函数执行, 然后, 当使用next()函数, 或者, __next__(),
# 都会让函数继续执行, 然后, 当执行到下一个 yield语句的时候, 又会被暂停
#碰到yield就停止

def test():
    print("xxx")
    yield 1

    print("a")
    yield 2

    print("b")
    yield 3

    print("c")
    yield 4

    print("d")
    yield 5

    print("e")

g = test()
print(g) #<generator object test at 0x1039d1518>

next(g)  #xxx
next(g)  #a
next(g)  #b
next(g)  #c

def test2():
    for i in range(1, 9):
        yield i
f = test2()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))

#实现斐波那契数列
def creatNum():
    print("--------start---------")
    a,b = 0,1
    for i in range(5):
        print("---------1--------")
        yield b
        print("-----------2-----------")
        a,b = b,a+b
        print('----------3----------')
    print("--------stop--------")
a = creatNum()
next(a)

print("=========================send方法")
def test():
    print("------1----")
    res1 = yield 1  #先发送一个none,让他卡在这里 ,这样下次发送666的时候就可以给yield赋值了,

    print("------2----")
    print(res1)  #这里打印的是下边send传递的
    print("------3----")
    res2 = yield 2

    print(res2)

g = test()
# g.send(666) #如果一开始直接发送一个666,不发送一次None,因为刚开始执行,并没有yield所以就会报错,记住:send只能给yield赋值
g.send(None)
g.send(666)

#自己的测试理解
def sss():
    i = 0
    while i<5:
        if i == 0:
            temp = yield i
            print(temp,i)
        else:
            yield i
        i += 1
ss = sss()
ss.__next__() #先让程序停到temp = yield i  这一行
ss.send("hhh") #然后赋值,继续往下走

#可以使用yield实现一个多任务(协程)
#考虑到是死循环,就注释了,到时候可以运行看下效果
# def test1():
#     while True:
#         print("我是任务1")
#         yield None
#
# def test2():
#     while True:
#         print("我是任务2")
#         yield None
#
# t1 = test1()
# t2 = test2()
# while True:
#     t1.__next__()
#     t2.__next__()

print("=========================close方法")
def test():
    yield 1

    print("a")
    yield 2

    print("b")
    yield 3

    print("c")

    return 10


g = test()

print(g.__next__())
print(g.__next__())

g.close()

# print(g.__next__())
# # print(g.__next__())

####注意: 生成器只能遍历一次

print("=========================递归函数")
# 功能: 如果是不直接知道结果的数据, 就进行分解 9 9 * 8! 8 =
# 如果说, 直接知道结果的数据, 就直接返回 1! = 1
def jiecheng(n):
    if n == 1:
        return 1
    # n != 1
    return n * jiecheng(n - 1)

result = jiecheng(5)
print(result)
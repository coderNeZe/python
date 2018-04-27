def checkLogin(func):
    def inner():
        print("登录验证...")
        func()
    return inner

# 定义两个功能函数
@checkLogin
def fss():
    print("发说说")

# 语法糖 写法
@checkLogin
def ftp():
    print("发图片")

# 相关的逻辑代码
btnIndex = 1
if btnIndex == 1:
    fss()
else:
    ftp()


#装饰器的执行顺序
def zhuangshiqi_line(func):
    def inner():
        print("---------------------------")
        func()
    return inner


def zhuangshiqi_star(func):
    def inner():
        print("*" * 30)
        func()
    return inner

@zhuangshiqi_line # == print_content = zhuangshiqi_line(print_content)
@zhuangshiqi_star # == print_content =  zhuangshiqi_star(print_content)
def print_content():
    print("人狠话不多")

print_content()

print("--------------装饰器对无参数函数进行装饰-------------")

def funzsq(func):
    def inner():
        print("我是添加的装饰器")
        func()
    return inner

@funzsq
def testOne():
    print("testOne")

testOne()


print("--------------装饰器对有参数函数进行装饰-------------")
#装饰器中参数可变
def zsq(func):
    def inner(*args, **kwargs):
        print("_" * 30)
        # print(args, kwargs)
        func(*args, **kwargs)
    return inner

@zsq
def pnum(num, num2, num3):
    print(num, num2, num3)

@zsq
def pnum2(num):
    print(num)


pnum(123, 222, num3=666)
pnum2(999)

#装饰器的类型必须和使用装饰器的函数类型一致
def zsq(func):
    def inner(*args, **kwargs):
        print("_" * 30)
        # print(args, kwargs)
        res = func(*args, **kwargs)
        return res
    return inner

@zsq
def pnum(num, num2, num3):
    print(num, num2, num3)
    return num + num2 + num3


@zsq
def pnum2(num):#类型与装饰器不符合,应为zsq有返回的类型,所以结果会是none
    print(num)

res1 = pnum(123, 222, num3=666)
res2 = pnum2(999)

print(res1, res2)

print("--------------带有参数的装饰器-------------")
#带有参数的装饰器,能够起到在运行时,有不同的功能
#获取装饰器,传参数
def getzsq(char):
    def zsq(func):
        def inner():
            print(char * 30)
            func()
        return inner
    return zsq

@getzsq("*") #如果装饰器带参数,实际上先调这个函数,得到函数的引用,当做返回值,然后再拿到这个函数引用,接下来对需要装饰的东西进行装饰
def f1():
    print("666")

f1()

print("--------------装饰有返回值的函数-------------")
def funczsqTwo(func):
    def inner():
        print("我是装饰器two")
        res = func() # 这句话 去真正的调用testTwo函数  然后保存返回来的haha
        return res # 把haha返回到17行处的调用   这里把返回值再传递给ret ,ret在外边就可以打印了
    return inner

@funczsqTwo
def testTwo():
    print("testTwo")
    return "haha"

ret = testTwo()  #执行这句话,相当于调用的是装饰器中的闭包,即inner函数
print(ret)

print("--------------通用装饰器-------------")
def tyzsq(func):
    def inner(*args,**kwargs):
        ret = func(*args,**kwargs)
        return ret #通用装饰器,对于没有没有返回值的函数进行装饰,其实这里写返回值也没关系,就是返回none而已
    return inner

#有无返回值的测试
@tyzsq
def test3():
    print("test3")

@tyzsq
def test4():
    return "啊哈哈哈"

#参数的测试
@tyzsq
def test5(a):
    print(a)

a = test3()
print(a)
b = test4()
print(b)
c = test5(5)
print(c)


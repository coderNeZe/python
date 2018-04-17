# 1 / 0
# ZeroDivisionError  除零异常
#nameError 名称异常
#TypeError 类型异常
# indexError 索引异常
# KeyError 键异常
# VlaueError 值异常
# AttributeError 属性异常
# StopIteration 迭代器异常

print("--------------------------------捕获异常的完整结构-----------------------------")
#异常只能处理一个,当有一个异常时,只会判断一个异常
try :
    1 / 0
    # print(name)
except ZeroDivisionError as ze:  #as ze 可以起别名 下边可以打印使用
    print("除零异常",ze)
# except NameError as ne:
#     print("名称问题,请仔细检查",ne)#异常只能处理一个,当有一个异常时,只会判断一个异常  所以不会走到这里
else:
    print("没有异常,请做业务逻辑的处理")
finally:
    print("最后执行的内容, 到时候, 不管是否会出现异常, 都会执行的语句")

print("--------------------------------合并并处理多个异常-----------------------------")
try :
    # 1 / 0
    print(name)
except (ZeroDivisionError,NameError) as e: #这种方式还是只能处理一个异常
    print("xxxx",e)

# except(Exception): #如果不知道错误会抛出哪种异常,直接写Exception就行
#     print("xxxx")

else:
    print("没有异常,请做业务逻辑的处理")
finally:
    print("最后执行的内容, 到时候, 不管是否会出现异常, 都会执行的语句")

print("--------------------------------with语句-----------------------------")
#实现一个读取文件的操作,当读取出错时,也能关闭文件
#方式1:传统的try形式
# try:
#     f = open("../stage-01/13-python文件操作/1.png", "r")
#     f.readlines()
# except Exception as e:
#     print(e)
# finally:
#     print("xxxx")
#     f.close()

#方式2:使用with语句实现
# with open("../stage-01/13-python文件操作/1.png", "r") as f:  #这样写虽然还会报错,但可以保证文件已经关闭
#     f.readlines()

print("--------------------------------自定义上下文管理器的理解-----------------------------")
#自定义一个上下文管理器,实现两个方法即可
class Test:
    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        #exc_tb:异常的追踪信息
        print(self, exc_type, exc_val, exc_tb)

        import traceback
        print(traceback.extract_tb(exc_tb)) #可以提取查看异常日志,这里可以根据业务逻辑,是写文件还是其他操作

        print("exit")
        return True #true说明内部把异常处理了,不会向外部抛异常了 flase和none会把异常传递出去

with Test() as x:
    print("body", x)
    1 / 0  #产生异常,会传递给__exit__

print("--------------------------------contextlib模块-----------------------------")
import  contextlib

@contextlib.contextmanager  #通过这个方法,就可以使一个生成器变成上下文管理器
def test():
    print(1) #上

    yield
    print(2) #下

with test() as x:
    print(3) #中

#使用举例
@contextlib.contextmanager #把ze包装成一个上下文管理器
def ze():
    try:
        yield
    except Exception as e:
        print("error",e)
#使用上边包装的管理器,用起来就会方便很多
with ze() as x:
    1 / 0

with ze() as x:
    3 / 0

print("------closing------")
#closing:让一个有close方法的类快速的实现具有上下文管理器的作用
#比如: est中 在调用完t方法后,自动的调用close函数
#当然可以用__enter__,__exit__这两个方法实现,也可以使用closing

class Test:
    def t(self):
        print("tttttt")

    def close(self):
        print("资源释放")

    # def __enter__(self):
    #     return self
    #
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     self.close()

import contextlib
with contextlib.closing(Test()) as t_obj:  #注意,如果Test中没有实现close方法,会报错
    t_obj.t()

#快速的实现文件的复制
# with open("xx.jpg", "rb") as from_file, open("xx2.jpg", "wb") as to_file:
#     from_contents = from_file.read()
#     to_file.write(from_contents)

print("--------------------------------手动的抛异常+自定义异常-----------------------------")
class LessZero(Exception):
    def __init__(self, msg, error_code):
        self.msg = msg
        self.ec = error_code

    def __str__(self): #描述实例对象的字符串,内建方法
        return self.msg + str(self.ec)
    pass


def set_age(age):
    if age <=0 or age > 200:
        raise LessZero("小于零, 错误", 404)
    else:
        print("给张三的年龄设置为", age)

try:
    set_age(-18)
except LessZero as e:
    print("x", e)
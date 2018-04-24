print("====================常规导入=============================")
#导入模块
import Tool
print(Tool.num)


#导入包里某个文件 方式一:
# import p1.Tool2
#import p1 #注意,这样导入,不会把p1下说有的文件导入进来,如果想实现这种功能,在__init__.py 文件里写 import p1.Tool2
# print(p1.Tool2.num)

#导入包里某个文件 方式二:
#__init__.py里写了__all__的方法
from p1 import  *
print(Tool2.num)
# print(Tool3.num) #会报错,因为__all__里并没有写Tool3

#如果__init__.py里写的是from . import Tool3(从当前文件夹导入Tool3)
import p1
print(p1.Tool3.name)

"""
1.如果一个文件夹里有__init__.py文件,则这就是一个包
2.只要导入这个包,就会自动执行__init__.py文件
3.如果__init__.py内容是空的,则你可以导入,但用不了包里的内容
4.如果__init__.py里写了__all__,影响的是from 包 import * 的时候可以导入哪些内容,
  影响的是你from包的时候,可以导入那个模块,例如方式二的意思就是我导入p1包的时候具体导入了Tool2的模块
5.如果__init__.py里写了from . import sendMsg 意思就是你导入p1包的时候,p1包又导入了其他模块
6.注意理解__init__.py里 __all__ 和 import 模块名的区别
"""

#导入多个包,可以,号分割
#import Tool,p1.Tool2

#导入的时候可以起别名
import Tool as t
print("别名",t.num)

print("====================from导入=============================")
#前边的范围要大于后边
from p1 import Tool2 as t2,Tool3 as t3
print(t2.num)
print(t3.name)

from FromTool import num2
print(num2)

#从一个模块中批量的导入资源
from piliang import  *
#如果piliang.py中,实现了__all__方法,则只能导入它所规定的
print(n1,n2) #n3,n4 不能访问,__all__里没有写入

#包里批量的导入资源
#在__inin__.py 里 __all__ = ["Tool2","Tool3"]
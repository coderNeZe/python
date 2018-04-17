print("====================常规导入=============================")
#导入模块
import Tool
print(Tool.num)


#导入包里某个文件
import p1.Tool2
#import p1 #注意,这样导入,不会把p1下说有的文件导入进来,如果想实现这种功能,在__init__.py 文件里写 import p1.Tool2
print(p1.Tool2.num)

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
#在__inin__.py里 __all__ = ["Tool2","Tool3"]



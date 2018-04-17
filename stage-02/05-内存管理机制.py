class Person:
    pass

p = Person()
print(p)
print(id(p))
print(hex(id(p)))
p2 = Person()
print(id(p),id(p2))

#对于整数和短小的字符,phthon会进行缓存,不会创建多个相同对象
num1 = 2
num2 = 2
print(id(num1),id(num2))

#容器对象,存储的其他对象,仅仅是其他对象的引用,并不是其他对象本身

print("---------------------------引用计数器--------------------------------")

import sys

class Person:
    pass

p1 = Person() # 1
print(sys.getrefcount(p1))  #注意这个方法会比真正的值大1

p2 = p1 # 2
print(sys.getrefcount(p1))

del p2 # 1
print(sys.getrefcount(p1))

del p1
# print(sys.getrefcount(p1)) #报错,引用计数是0,对象已经释放

print("---------------------------引用计数器+1 -1 的场景举例--------------------------------")
import sys

class Person:
    pass

p_xxx = Person() # 1
print(sys.getrefcount(p_xxx))


def log(obj):
    print(sys.getrefcount(obj))
log(p_xxx)  #一个对象传递给一个函数的时候,会有两个属性引用着这个对象,所以加2

print("---------------------------引用计数器机制-特殊场景-循环引用问题--------------------------------")
# 内存管理机制 = 引用计数器机制 + 垃圾回收机制
# 当一个对象, 如果被引用 + 1, 删除一个引用 : -1 0: 被自动释放
# 循环引用
# objgraph
# objgraph.count() 可以查看, 垃圾回收器, 跟踪的对象个数

import objgraph

class Person1:
    pass


class Dog:
    pass

p = Person1()
d = Dog()

print(objgraph.count("Person1"))
print(objgraph.count("Dog"))

p.pet = d
d.master = p

# 删除 p, d之后, 对应的对象是否被释放掉
del p
del d

print(objgraph.count("Person1"))
print(objgraph.count("Dog"))

print("---------------------------------垃圾回收机制-分代回收---------------------------------------")
import gc

print(gc.get_threshold())
'''
当新增的对象减去消亡的对象 差值是200的时候,会触发分代回收,5和5的意思当第0带检查了5次后,再去检查第一代
当第一代检查5次后,再去检查第二代
'''
gc.set_threshold(200, 5, 5)  #为了性能考虑,一般数值设置的很大

print(gc.get_threshold())

print("---------------------------------垃圾回收机制-触发时机---------------------------------------")
'''
触发时间的条件:
1.垃圾回收机制必须开启
2.达到设定的阈值
'''

#自动回收
import gc

gc.disable()  #关闭垃圾回收机制
print(gc.isenabled()) #检测是否开启

gc.enable() #开启垃圾回收机制(默认开启)

print(gc.isenabled())

print(gc.get_threshold())
gc.set_threshold(1000, 15, 5)

# 手动回收
print("-----------------")
import objgraph

class Student:
    pass

class Cat:
    pass

p = Student()
d = Cat()

p.cat = d
d.master = p


del p
del d

gc.collect() #手动的开启垃圾回收机制

print(objgraph.count("Student"))
print(objgraph.count("Cat"))

print("-----------------------------------循环引用-细节问题(版本兼容方案)---------------------------------------")
#在python2.0中  两个相互引用的类 如果有一个实现了__del__方法,则用垃圾回收机制是不会成功的,所以需要进行版本的兼容
#让其中一个对象 弱引用另一个就行

import objgraph
import gc
import weakref

# 1. 定义了两个类
class Person2:
    def __del__(self):
        print("Person对象, 被释放了")
    pass

class Dog2:
    def __del__(self):
        print("Dog对象, 被释放了")
    pass

# 2. 根据这两个类, 创建出两个实例对象
p = Person2()
d = Dog2()

# 3. 让两个实例对象之间互相引用, 造成循环引用

#弱引用的方式1:使用weakref
# p.pet = d
# d.master = weakref.ref(p)

#弱引用的方式2:
p.pet = None  #手动置其中一个为None
del p
del d

#假如p中有个数组,数组中有很多其他对象,此时有两种方式的写法:
# p.pets = {"dog":  weakref.ref(d1), "cat":  weakref.ref(c1)}
# weakref.WeakValueDictionary({"dog": d1, "cat": c1})  #使用弱字典的方式,等价于上边的一种写法 更简单
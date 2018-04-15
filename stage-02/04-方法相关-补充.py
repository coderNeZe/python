print("==========================私有方法==================")
class Person:
    __age = 18

    #私有方法
    def __run(self):
        print("pao")

    #注意不能这样,名字重整机制,会覆盖
    # def _Person__run(self):
    #     print("xxx")
p = Person()
p._Person__run()

print(Person.__dict__)

print("==========================内置的特殊方法==================")
print("----------__str__---------")
#__str__: 使用字符串描述这个类产生的实例
class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def __str__(self):
        return "这个人的姓名是%s, 这个人的年龄是:%s" % (self.name, self.age)

p1 = Person("fh", 18)
print(p1) #会触发 __str_函数

p2 = Person("zhangsan", 19)
print(p2)  #会触发 __str_函数

s = str(p1) #也会触发 __str_函数
print(s, type(s))

print("----------__repr__---------")
#自己的理解就是repr可以打印一些给开发者看的东西,比如想看看对象的地址什么的,可以在类内部实现repr这个方法,外部通过repr(p1)调用
class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def __str__(self):
        return "这个人的姓名是%s, 这个人的年龄是:%s" % (self.name, self.age)

    # def __repr__(self):
    #     return "reprxxxxx"

p1 = Person("fh", 18)
print(p1)

p2 = Person("zhangsan", 19)
print(p2)

print(repr(p1))


#repr例子:
import datetime

t = datetime.datetime.now()
print(t)
print(repr(t))
tmp = repr(t)
result = eval(tmp)
print(result)


print("----------------------------__call__方法------------------------------------")
#使得"对象"具备当做函数,来调用的能力
class Person:
    def __call__(self, *args, **kwargs):
        print("xxx", args, kwargs)
        pass

p = Person()
p(123, 456, name="fh")


#应用场景举例
# 创建很多个画笔, 画笔的类型(钢笔, 铅笔), 画笔的颜色(红, 黄色, 青色, 绿色)

#使用偏函数实现
# def createPen(p_color, p_type):
#     print("创建了一个%s这个类型的画笔, 它是%s颜色" % (p_type, p_color))
#
# import functools
#
# gangbiFunc = functools.partial(createPen, p_type="钢笔")
#
# gangbiFunc("红色")
# gangbiFunc("黄色")
# gangbiFunc("绿色")


#使用面向对象实现
class PenFactory:
    def __init__(self, p_type):
        self.p_type = p_type

    def __call__(self, p_color):
        print("创建了一个%s这个类型的画笔, 它是%s颜色" % (self.p_type, p_color))

gangbiF = PenFactory("钢笔")
gangbiF("红色")
gangbiF("绿色")
gangbiF("黄色")


qianbiF = PenFactory("铅笔")
qianbiF("红色")
qianbiF("绿色")
qianbiF("黄色")

print("----------------------------索引操作------------------------------------")
#就是像字典一样的去操作对象
class Person:
    def __init__(self):
        self.cache = {} #初始化的时候,就可以有一个字典,以后就可以去操作这个字典

    def __setitem__(self, key, value):
        # print("setitem", key, value)
        self.cache[key] = value

    def __getitem__(self, item):
        # print("getitem", item)
        return self.cache[item]

    def __delitem__(self, key):
        # print("delitem", key)
        del self.cache[key]

p = Person()  #实现上述的三个内置方法,就可以像操作字典一样,操作对象
p["name"] = "fh" #对应上边的__setitem__

print(p["name"]) #对应上边的__getitem__

del p["name"] #对应上边的__delitem__

print(p.cache)


print("----------------------------切片操作------------------------------------")
#相当于列表中获取某段的数据
l = [1, 2, 3, 4, 5]
# print(l[3])
print(l[1: 4: 2])

class Person:

    def __init__(self):
        self.items = [1, 2, 3, 4, 5, 6, 7, 8]

    def __setitem__(self, key, value):
        # print(key, value)
        # print(key.start)
        # print(key.stop)
        # print(key.step)
        # print(value)

        if isinstance(key, slice):#判断所传的key,必须是一个slice对象
            self.items[key.start: key.stop: key.step] = value
            # self.items[key] = value #最好用这种方式,上边那种赋值方法也行

    def __getitem__(self, item):
        print("getitem", item)

    def __delitem__(self, key):
        print("delitem", key)

p = Person()
p[0: 4: 2] = ["a", "b"]
print(p.items)
slice  #切片对象的意思

p[0: 5: 2]  #获取 __getitem__
del p[0: 5: 2]  #删除__delitem__

print("----------------------------比较操作------------------------------------")
class Person:
    def __init__(self, age, height):
        self.age = age
        self.height = height

    # == != > >= < <=
    def __eq__(self, other):
        print("eq")
        return self.age == other.age

    def __ne__(self, other): #不相等的意思
        pass

    def __gt__(self, other): #大于
        pass

    def __ge__(self, other): #大于等于
        pass

    def __lt__(self, other): #小于
        # print("lt")
        print(self.age)
        print(other.age)
        return self.age < other.age

    def __le__(self, other):#小于等于
        pass


p1 = Person(18, 190)
p2 = Person(19, 190)
print(p1 < p2)
print(p1 <= p2) # p2 < p1
print(p1 == p2)
print(p1 != p2)
print(p1 <= p2)


print("---------------------------比较操作-补充------------------------------------")
import functools

@functools.total_ordering  #可以通过__lt__和__eq__推算出其他的方法
class Person:
    def __lt__(self, other):
        print("lt")
        # pass
        return False

    def __eq__(self, other):
        print("eq")
        pass

    # def __le__(self, other):
    #     print("le")

p1 = Person()
p2 = Person()

print(p1 <= p2) #函数内部并没有<=的方法实现 因为用了@functools.total_ordering的装饰器,系统会自动补全其他的方法

print(Person.__dict__)


print("----------------------------上下文环境的布尔值------------------------------------")

class Person:
    def __init__(self):
        self.age = 20

    def __bool__(self):
        return self.age >= 18
    pass

p = Person()
if p:#控制p是true还是false 通过__bool__方法实现
    print("xx")


print("----------------------------遍历操作------------------------------------")
#让自己创建的对象 可以通过for in 遍历
#方式1:__getitem__
class Person:
    def __init__(self):
        self.result = 1

    def __getitem__(self, item):
        self.result += 1
        if self.result >= 6:
            raise StopIteration("停止遍历") #抛出异常

        return self.result
    pass

p = Person()
for i in p:
    print(i)

# 方式2:__iter__
print("-------------")
class Person:
    def __init__(self):
        self.result = 1

    def __iter__(self):
        print("iter")
        self.result = 1
        # return iter([1, 2, 3, 4, 5])
        return self

    def __next__(self):
        self.result += 1
        if self.result >= 6:
            raise StopIteration("停止遍历")
            return self.result

p = Person()
result = next(p)
while result:
    print(result)
    result = next(p)

print("----------------------------恢复迭代器初始值(复用)------------------------------------")
class Person:
    def __init__(self):
        self.age = 1


    def __getitem__(self, item):
        return 1

    def __iter__(self):
        self.age = 1
        return self

    def __next__(self):
        self.age += 1
        if self.age >= 6:
            raise StopIteration("stop")

        return self.age

p = Person()

for i in p:
    print(i)

for i in p:  #能够再次遍历的原因是,__iter__又重置了age的值,这样在进行又一次遍历的时候,__iter__会被重新调用,由此实现了迭代器的可以再次使用
    print(i)

import collections
print(isinstance(p, collections.Iterator))  #实现__iter__和__next__的才是一个迭代器
print(isinstance(p, collections.Iterable))  #查看是否是个可迭代对象  只要实现__iter__

'''
总结:一个可迭代对象 一定可以通过forin进行遍历 但可以for in遍历的,不一定是一个可迭代对象 
比如,一个类实现了__getitem__方法,他就可以通过forin遍历,但没有实现__iter__方法,就不是一个可迭代对象
'''
print("---------------------------iter函数的使用------------------------------------")
#方式1:
class Person:
    def __init__(self):
        self.age = 1

    def __getitem__(self, item):
        self.age += 1
        if self.age >= 6:
            raise StopIteration("stop")
        return self.age

p = Person()
pt = iter(p) #类里必须实现__getitem__方法,让这个对象有迭代的功能,再调用iter()可以把该对象转换成迭代器
for i in pt:
    print(i)

print("-----------")
#方式2:
class Person:
    def __init__(self):
        self.age = 1

    def __iter__(self):
        self.age = 1
        return self

    def __next__(self):
        self.age += 1
        if self.age >= 6:
            raise StopIteration("stop")
        return self.age

    # def __call__(self, *args, **kwargs):
    #     self.age += 1
    #     if self.age >= 6:
    #         raise StopIteration("stop")
    #     return self.age

p = Person()
pt = iter(p)
for i in pt:
    print(i)

print(pt is p) #因为类现实了__iter__和__next__方法,所以本身就是一个迭代器,再调用iter(),其实是一个迭代器

# pt = iter(p.__next__, 4) # pt还可以传第二个参数,意思就是到4的时候就结束
# pt = iter(p, 4)  #也可以直接传p,但要注意,传对象的时候 要实现__call__方法,此时__next__方法可以注释,因为p会自动调用__call__里边的方法

l = [1, 2, 3]
lt = iter(l)
print(lt)
import collections
print(isinstance(l, collections.Iterator)) #列表不是迭代器
print(isinstance(l, collections.Iterable)) #列表可以迭代
print(isinstance(lt, collections.Iterator)) #转换后是迭代器
print(isinstance(lt, collections.Iterable)) #依旧可以迭代

# ----------------------------描述器-定义方式1------------------------------------


# class Person:
#     def __init__(self):
#         self.__age = 10
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, value):
#         if value < 0:
#             value = 0
#         self.__age = value
#
#     @age.deleter
#     def age(self):
#         print("del age")
#         del self.__age

    # age = property(get_age, set_age, del_age)
    # name = "sz"

# p = Person()
# p.age = 19
# del p.age
# print(p.age)
# p.age = 19
# print(p.age)
# del p.age
# print(p.age)
# p.set_age(-10)
# print(p.get_age())
# p.del_age()
# print(p.get_age())
# p.age = 10

# help(Person)







# ----------------------------描述器-定义方式2------------------------------------


# class Age:
#     def __get__(self, instance, owner):
#         print("get")
#
#     def __set__(self, instance, value):
#         print("set")
#
#     def __delete__(self, instance):
#         print("delete")
#
# class Person:
#     age = Age()
    # def __init__(self):
    #     self.__age = 10
    #
    # # @property
    # def get_age(self):
    #     return self.__age
    #
    # # @age.setter
    # def set_age(self, value):
    #     if value < 0:
    #         value = 0
    #     self.__age = value
    #
    # # @age.deleter
    # def del_age(self):
    #     print("del age")
    #     del self.__age
    #
    # age = property(get_age, set_age, del_age)

# p = Person()
# p.age = 10
# print(p.age)
# del p.age


# ----------------------------描述器-调用细节------------------------------------


# class Age(object):
#     def __get__(self, instance, owner):
#         print("get")
#
#     def __set__(self, instance, value):
#         print("set")
#
#     def __delete__(self, instance):
#         print("delete")
#
#
# class Person(object):
#     age = Age()
#     def __getattribute__(self, item):
#         print "xxxxx"
#
#
# p = Person()
#
# p.age = 10
# print(p.age)
# del p.age

# print(Person.age)
# Person.age = 19
# del Person.age


# ----------------------------描述器-和实例属性同名时, 操作优先级------------------------------------

# 资料描述器 get set
# 非资料描述器 仅仅实现了 get 方法, 那么他就是一个非资料描述器
# 资料描述器 > 实例属性 > 非资料描述器
# class Age(object):
#     def __get__(self, instance, owner):
#         print("get")
#
#     def __set__(self, instance, value):
#         print("set")
#
#     def __delete__(self, instance):
#         print("delete")
#
#
# class Person(object):
#     age = Age()
#     def __init__(self):
#         self.age = 10
#
# p = Person()
#
# p.age = 10
# print(p.age)
# # del p.age
#
# print(p.__dict__)




# ----------------------------描述器-值的存储问题------------------------------------
#
# class Person:
#     def __init__(self):
#         self.__age = 10
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, value):
#         if value < 0:
#             value = 0
#         self.__age = value
#
#     def del_age(self):
#         print("del age")
#         del self.__age
#
#     age = property(get_age, set_age, del_age)
#
# p = Person()
# p.age = 10
# print(p.age)
# del p.age



# class Age(object):
#     def __get__(self, instance, owner):
#         print("get")
#         return instance.v
#
#     def __set__(self, instance, value):
#         print("set", self, instance, value)
#         instance.v = value
#
#     def __delete__(self, instance):
#         print("delete")
#         del instance.v
#
#
# class Person(object):
#     age = Age()
#
#
# p = Person()
# p.age = 10
# print(p.age)
# # del p.age
#
# p2 = Person()
# p2.age = 11
# print(p2.age)
# print(p.age)

# ----------------------------使用类, 实现装饰器------------------------------------


# def check(func):
#     def inner():
#         print("登录验证")
#         func()
#     return inner
# class check:
#     def __init__(self, func):
#         self.f = func
#
#     def __call__(self, *args, **kwargs):
#         print("登录验证")
#         self.f()
#
# @check
# def fashuoshuo():
#     print("发说说")
# # fashuoshuo = check(fashuoshuo)
#
# fashuoshuo()
#
# x = "abc"
# y = [x]
# z = [x, y]
# import objgraph
# # objgraph.show_refs(y, filename='test.png')
# objgraph.show_refs(z, filename="test.png")

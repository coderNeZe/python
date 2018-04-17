class Animal:
    x = 10  #公有属性
    _a = 10 #受保护的属性,本类内部,子类内部可以访问,外部可以访问,但会报警告
    __b = 100 #私有属性,本类内部可以访问, 外部,子类都不能访问

    def test(self):
        print(self.x)  #类的内部可以访问

    def test1(self):
        print(self._a)  #受保护,本类可以访问

    def test2(self):
        print(self.__b)  #私有属性,本类内部可以访问

    pass

class Dog(Animal):
    def test2(self):
        print(Dog.x)  #子类可以访问到
        print(self.x) #子类可以访问到

        print(Dog._a) #受保护,子类可以访问
        print(self._a)

        # print(Dog.__b)  #私有属性,子类不可以可以访问
        # print(self.__b)
    pass

#测试代码
a = Animal()
a.test()
a.test1()
a.test2()

d = Dog()
d.test2()

print(Animal.x)
print(Dog.x)

print(Animal._a) #受保护 外部可以访问 但会有警告


#私有属性的名字重整机制
#_类名__变量
# print(Animal.__b)  #正常情况下,不能访问到
print(Animal._Animal__b)  #通过名字重整机制访问到

print("=========================私有属性的应用场景==========================")
class Person:
    #主要作用,当我们创建好一个实例对象之后,会自动调用这个方法,来初始化这个对象
    def __init__(self):
        self.__age = 18

    def setAge(self,value):
        if isinstance(value,int) and 0 < value < 200:
            self.__age = value
        else:
            print("数据有问题")

    def getAge(self):
        return self.__age

p1 = Person()
p1.setAge(20)
print(p1.getAge())

#xx_ :规范的写法 比如想用class当变量 可以用class_ 和系统的关键字做区分
#__xx__: 一般是系统内置的东西

print("=========================只读属性==========================")
class Pet(object):
    def __init__(self):
        self.__age = 18

    @property #主要作用,就是以使用属性的方式,来使用这个方法
    def age(self):
        return  self.__age

p1 = Pet()
print(p1.age)

# p1.age = 666 # 只读属性不能设置值

print("=========================property在新式类中的使用==========================")
#注意:在python3.0中 创建了一个类后,是默认继承object,所以只能测试新式类的使用,经典类需要切换python2.0版本,就不做测试了
#在新式类中的定义
class Test(object):
    def __init__(self):
        self.__age = 18


    def get_age(self):
        print("----, get")
        return self.__age

    def set_age(self, value):
        print("----, set")
        self.__age = value


    age = property(get_age, set_age)


p = Test()
print(p.age)

p.age = 90
print(p.age)

print(p.__dict__)

# 第二种使用方式
print("-" * 30)
class Test2(object):
    def __init__(self):
        self.__age = 18

    @property
    def age(self):
        print("----- get")
        return self.__age

    @age.setter
    def age(self, value):
        print("----- set")
        self.__age = value

p = Test2()
print(p.age)

p.age = 10
print(p.age)

print("=========================只读属性-方式2==========================")
class Person:
    # 当我们通过 "实例.属性 = 值", 给一个实例增加一个属性, 或者说, 修改一下属性值的时候, 都会调用这个方法
    # 在这个方法内部, 才会真正的把, 这个属性, 以及对应的数据, 给存储到__dict__字典里面
    def __setattr__(self, key, value):
        print(key, value)

        # 1. 判定, key, 是否是我们要设置的只读属性的名称
        if key == "age" and key in self.__dict__.keys():
            print("这个属性是只读属性, 不能设置数据")
        # 2. 如果说不是, 只读属性的名称, 真正的给它添加到这个实例里面去
        else:
            # self.key = value  不能这么写,会成死循环 self.key 会走__setattr__这个方法
            self.__dict__[key] = value
p1 = Person()
p1.age = 18  #增加属性
print(p1.age)

p1.age = 999 #修改属性
print(p1.age)

print("=========================常用内置属性==========================")

class Person:
    """
    这是一个人, 类
    """
    age = 19
    def __init__(self):
        self.name = "sz"

    def run(self):
        print("run")

# __dict__ : 类的属性
# __bases__ : 类的所有父类构成元组
# __doc__ :类的文档字符串
# __name__: 类名
# __module__: 类定义所在的模块


print("dict",Person.__dict__) #类的所有属性方法
print("bases",Person.__bases__) #所有父类
print("doc",Person.__doc__) #类的文档字符串
print(Person.__name__)
print(Person.__module__)

p = Person()
print(p.__class__)



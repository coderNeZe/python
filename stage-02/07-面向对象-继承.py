class Animal:
    pass

class xxx:
    pass

class Dog(Animal,xxx): #多继承
    pass
print(Dog.__bases__)  #(<class '__main__.Animal'>, <class '__main__.xxx'>)

print(Animal.__bases__) #(<class 'object'>,),python3中,创建的类默认继承object

print(int.__bases__)    #(<class 'object'>,)
print(type.__bases__)

print("-----------------继承-资源--------------------------")
class Person:
    a =1
    _b = 2
    __c = 3

    def t1(self):
        print("t1")

    def _t2(self):
        print("t2")

    def _t3(self):
        print("t3")

    def __init__(self):
        print("init animal")

class Student(Person):
    def test(self):
        print(self.a)
        print(self._b)
        # print(self.__c)

        self.t1()
        self._t2()
        # self.__ts()
        self.__init__()

p = Student()
p.test()

print("-----------------继承-累加--------------------------")
class B:
    a = 1
    def __init__(self):
        self.b = 2

    def t1(self):
        print("t1")

    @classmethod
    def t2(cls):
        print("t2")

    @staticmethod
    def t3():
        print("t3")

class A(B):
    c = 3
    def __init__(self):
        # super(A,self).__init__()
        super().__init__()
    def tt1(self):
        print("tt1")

    @classmethod
    def tt2(cls):
        super().t2()
        print("tt2")

    @staticmethod
    def tt3():
        print("tt3")

a_obj = A()
print(a_obj.b) #A类实现了init方法后,会调用自己的init,所以B里的b就没法访问,使用super调用
a_obj.tt2()

print("--------------------------------------抽象类-------------------------------------")

import abc

class Animal(object, metaclass=abc.ABCMeta): #这就是一个抽象类
    @abc.abstractmethod  #抽象的方法
    def jiao(self):
        pass

    @abc.abstractclassmethod  #抽象的类方法
    def test(cls):
        pass

class Dog(Animal):
    def jiao(self):
        print("汪汪汪")

    @classmethod
    def test(cls):
        print("xxxxx")
    pass

class Cat(Animal):
    def jiao(self):
        print("喵喵喵")

d = Dog()
# c = Cat()  #cat少实现抽象类的一个方法,所以会报错
d.jiao()
d.test()
# c.jiao()


print("--------------------------------------面向对象案例-------------------------------------")
# 定义三个类, 小狗, 小猫, 人
# 小狗: 姓名, 年龄(默认1岁);        吃饭, 玩, 睡觉, 看家(格式: 名字是xx, 年龄xx岁的小狗在xx)
# 小猫: 姓名, 年龄(默认1岁);        吃饭, 玩, 睡觉, 捉老鼠(格式: 名字是xx, 年龄xx岁的小猫在xx)
# 人:   姓名, 年龄(默认1岁), 宠物;  吃饭, 玩, 睡觉(格式: 名字是xx, 年龄xx岁的人在xx)
#                           养宠物(让所有的宠物吃饭, 玩, 睡觉),
#                           让宠物工作(让所有的宠物根据自己的职责开始工作)

class AnimalClass:
    def __init__(self,name,age = 1):
        self.name = name
        self.age = age

    def eat(self):
        print("%s在吃饭" % self)

    def play(self):
        print("%s在玩" % self)

    def sleep(self):
        print("%s在睡觉" % self)

class DogClass(AnimalClass):
    def work(self):
        print("%s在看家" % self)

    def __str__(self):
        return "名字是{}, 年龄{}岁的小狗".format(self.name, self.age)

class CatClass(AnimalClass):
    def work(self):
        print("%s在捉老鼠" % self)

    def __str__(self):
        return "名字是{}, 年龄{}岁的小猫".format(self.name, self.age)

class PersonClass(AnimalClass):
    def __init__(self, name, pets, age=1):
        super().__init__(name, age)
        self.pets = pets

    def yang_pets(self):
        for pet in self.pets:
            pet.eat()
            pet.play()
            pet.sleep()

    def make_pets_work(self):
        for pet in self.pets:
            pet.work()

    def __str__(self):
        return "名字是{}, 年龄{}岁的人".format(self.name, self.age)

d = DogClass("小黑", 18)
c = CatClass("小红", 2)
p = PersonClass("fh", [d, c], 18)
p.yang_pets()
p.make_pets_work()








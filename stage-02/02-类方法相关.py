print("===============方法的分类===================")
#方法分为实例方法,类方法,静态方法
class Person:
    def eat(self):#self 是默认第一个参数需要接受到实例  系统自动补全的
        print("这是一个实例方法",self)

    def run(self,sport): #扩充参数,在后边直接写就行
        print("在运动",sport)

    @classmethod
    def leifangfa(cls):#cls 是默认第一个参数需要接受到类  系统自动补全的
        print("这是一个类方法",cls)

    @staticmethod
    def jingtaifangfa():
        print("这是一个静态方法")

p = Person()
p.eat()
p.run("跑步")

Person.leifangfa()
p.leifangfa() #也可以通过实例调用类方法

p.jingtaifangfa()
Person.jingtaifangfa()

#Person.eat()#会报错 类调用了实例方法

#不管哪种类型的方法,都是存储在类对象里边的
print(Person.__dict__)

print("=================不同类型的方法访问不同类型的属性,规律==============")
class Student:
    age = 0
    def shilifangfa(self):
        print(self)
        print(self.age)
        print(self.num)

    @classmethod
    def leifangfa(cls):
        print(cls)
        print(cls.age)
        # print(cls.num) #会报错,类方法找不到实例属性

    @staticmethod
    def jingtaifangfa():#原则上谁都访问不到,但可以拿到类,去访问类属性
        print(Student.age)

s = Student()
s.num = 10
#类属性
print(Student.age)
print(s.age)

#实例属性
print(s.num)

s.shilifangfa()
s.leifangfa()

s.jingtaifangfa()


print("=================元类==============")
num = 10 #是一个对象  num ---------> 10
print(num.__class__) #<class 'int'> 10是int这个对象实例出来的
s = "abc"
print(s.__class__) #<class 'str'>  abc是str这个对象实例出来的

class Pet:
    pass

p = Pet()
print(p.__class__) #<class '__main__.Pet'>   p是Pet这个对象实例出来的

#int,str,Pet  这些 是哪个类创建出来的?
print(int.__class__) #<class 'type'>
print(str.__class__) #<class 'type'>
print(Pet.__class__) #<class 'type'>  type就是一个元类

#type再往上就没有了
print(type.__class__)  #<class 'type'>

print("=================类的创建方式==============")
def run(self):
    print("------",self);
Dog = type("Dog",(),{"count":0,"run":run})
print(Dog) #<class '__main__.Dog'>
print(Dog.__dict__)
d = Dog()
print(d)
d.run()

print("=================类的创建流程==============")
#1.检测类对象中是否有明确的__metaclass__属性
#2.检测父类中是否存在__metaclass__属性
#3.检测模块总是否存在__metaclass__属性
#4.通过内置的type这个元类来创建这个类对象
class Animal():
    pass

class Cat(Animal): #cat继承Animal
    pass


print("=================类的描述(注释)==============")
'''
这里写注释
'''
class Per:
    count = 1
    def run(self,dis,step):
        '''
        :param dis: 我是描述
        :param step: 我是描述
        :return: 我是描述
        '''
        print("人在跑")


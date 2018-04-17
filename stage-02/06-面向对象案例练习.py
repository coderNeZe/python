# 计算器, 实现一些基本的操作, 加减乘除运算, 以及打印结果操作
class Caculator:
    def __check_num_zsq(func):
        def inner(self,n):
            if not isinstance(n,int):
                raise TypeError("当前这个数据的类型有问题, 应该是一个整型数据")
            return func(self,n)
        return  inner

    @__check_num_zsq
    def __init__(self,num):
        self.__result = num

    @__check_num_zsq
    def jia(self,n):
        self.__result += n
        return self

    @__check_num_zsq
    def jian(self,n):
        self.__result -= n
        return self

    @__check_num_zsq
    def cheng(self,n):
        self.__result *= n
        return self

    @__check_num_zsq
    def chu(self,n):
        self.__result /= n
        return self

    def show(self):
        print("当前的计算结果是:%d"%self.__result)
        return self

    def clear(self):
        self.__result = 0
        return self

    @property
    def result(self):
        return self.__result

c = Caculator(10)
c.jia(10).jian(4).cheng(5).show().clear().jia(555).jian(500).show()
print(c.result)

#windows下 有语音播报功能,语音播报也是通过装饰器实现,好好的理解其实现思想
# # ------------------------------------代码11--------------------------------------
# import win32com.client
#
#
# class Caculator:
#     def __check_num_zsq(func):
#         def inner(self, n):
#             if not isinstance(n, int):
#                 raise TypeError("当前这个数据的类型有问题, 应该是一个整型数据")
#             return func(self, n)
#
#         return inner
#
#     def __say(self, wo rd):
#         # 1. 创建一个播报器对象
#         speaker = win32com.client.Dispatch("SAPI.SpVoice")
#
#         # 2. 通过这个播报器对象, 直接, 播放相对应的语音字符串就可以
#         speaker.Speak(word)
#
#     def __create_say_zsq(word=""):
#         def __say_zsq(func):
#             def inner(self, n):
#                 self.__say(word + str(n))
#                 return func(self, n)
#
#             return inner
#         return __say_zsq
#
#     @__check_num_zsq
#     @__create_say_zsq()
#     def __init__(self, num):
#         self.__result = num
#
#     @__check_num_zsq
#     @__create_say_zsq("加")
#     def jia(self, n):
#         self.__result += n
#         return self
#
#     @__check_num_zsq
#     @__create_say_zsq("减去")
#     def jian(self, n):
#         self.__result -= n
#         return self
#
#     @__check_num_zsq
#     @__create_say_zsq("乘以")
#     def cheng(self, n):
#         self.__result *= n
#         return self
#
#     def show(self):
#         self.__say("计算的结果是:%d" % self.__result)
#         print("计算的结果是:%d" % self.__result)
#         return self
#
#     def clear(self):
#         self.__result = 0
#         return self
#
#     @property
#     def result(self):
#         return self.__result
#
# c1 = Caculator(10)
# c1.jia(6).jian(4).cheng(5).show().clear().jia(555).jian(500).show()
#
# print(c1.result)
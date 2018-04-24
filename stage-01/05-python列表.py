print("------------------------------列表的定义方式1-----------------------------------")
names = ["zhangsan", "lisi", "wanger"]
names = [1, True, 3, "sz"]
names = []

items = ["a", "b", "c"]
# names = [1, 2, 3, "sz", True, items]
names = [1, 2, 3, 'sz', True, ['a', 'b', 'c']]

print(names, type(names))

print("------------------------------列表的定义方式2-----------------------------------")
#列表生成式
# 0 - 99 [1, 2, 3, ... 99]
nums = range(99)
print(nums)
nums = range(1, 10000)
print(nums)

#列表推导式
nums = [1, 2, 3, 4, 5]

# 原始的方式
# resultList = []
# for num in nums:
#     # print(num)
#     if num % 2 == 0:
#         continue
#     resultNum = num ** 2
#     print(resultNum)
#     resultList.append(resultNum)
#
# print(resultList)

# 列表推导式
#表达式 for 变量 in 列表
#表达式 for 变量 in 列表 if 条件
# resultList = [num ** 2 for num in nums if num % 2 != 0]
#列表生成式
a = [x*2 for x in range(10)]  #取0到10的数字,然后再每个数字乘以2
print(a)
b = [(i,j) for i in range(3) for j in range(2)]#每执行一次i,j要执行两次 ,相当于循环嵌套
print(b) #[(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
resultList = [num ** 2 for num in nums for num2 in nums]
print(resultList)

print("--------------------------增加操作---------------------------")
# 增
# 	append
# 		作用
# 			往列表中, 追加一个新的元素
# 			在列表的最后
# 		语法
# 			l.append(object)
# 		参数
# 			object
# 				想要添加的元素
# 		返回值
# 			None
# 		注意
# 			会直接修改原列表
nums = [1, 2, 3, 4]
print("append = {0}".format(nums))
print(nums.append(5))
print("append = {0}".format(nums))

# 	insert
# 		作用
# 			往列表中, 追加一个新的元素
# 			在指定索引前面
# 		语法
# 			l.insert(index, object)
# 		参数
# 			index
# 				索引, 到时会插入到这个索引之前
# 			object
# 				想要添加的元素
# 		返回值
# 			None
# 		注意
# 			会直接修改原数组
nums = [1, 2, 3, 4]
print("insert = {0}".format(nums))
print(nums.insert(1, 5))
print("insert = {0}".format(nums))

# 	extend
# 		作用
# 			往列表中, 扩展另外一个可迭代序列
# 		语法
# 			l.extend(iterable)
# 		参数
# 			iterable
# 				可迭代集合
# 					字符串
# 					列表
# 					元组
# 					...
# 		返回值
# 			None
# 		注意
# 			会直接修改原数组
# 			和append之间的区别
# 				extend可以算是两个集合的拼接
# 				append是把一个元素, 追加到一个集合中
nums = [1, 2, 3, 4]
# nums2 = ["a", "b", "c"]
nums2 = "abcdefg"

print(nums.extend(nums2))
print("extend = {0}".format(nums))


# 	乘法运算
# 		["a"] * 3
# 			=
# 				['a', 'a', 'a']
nums = [1, 2]
print(nums * 3)

# 	加法运算
# 		["a"] + ["b", "c"]
# 			=
# 				["a", "b", "c"]
# 		和extend区别
# 			只能列表类型和列表类型相加
n1 = [1, 2, 3]
# n2 = ["a", "b"]
n2 = "abc"
# print(n1 + n2)  #报错 只能连接列表


print("--------------------删除操作-----------------------")
# 删
# 	del 语句
# 		作用
# 			可以删除一个指定元素(对象)
# 		语法
# 			del 指定元素
# 		注意
# 			可以删除整个列表
# 				删除一个变量
# 			也可以删除某个元素
nums = [1, 2, 3, 4, 5]
del nums[1]
print("del  =  {0}".format(nums))
del nums
# print("del  =  {0}".format(nums)) //报错  该列表已经被删除

#可以删除整个变量
num = 666
del num
# print(num)  #会报错,该变量已经被删除


# 	pop
# 		作用
# 			移除并返回列表中指定索引对应元素
# 		语法
# 			l.pop(index=-1)
# 		参数
# 			index
# 				需要被删除返回的元素索引
# 				默认是-1
# 					也就对应着列表最后一个元素
# 		返回值
# 			被删除的元素
# 		注意
# 			会直接修改原数组
# 			注意索引越界
nums = [1, 2, 3, 4, 5]

# result = nums.pop()
result = nums.pop(1)
print("pop = ",result, nums)  #2 [1, 3, 4, 5]

# 	remove
# 		作用
# 			移除列表中指定元素
# 		语法
# 			l.remove(object)
# 		参数
# 			object
# 				需要被删除的元素
# 		返回值
# 			None
# 		注意
# 			会直接修改原数组
# 			如果元素不存在
# 				会报错
# 			若果存在多个元素
# 				则只会删除最左边一个
# 			注意循环内删除列表元素带来的坑
nums = [1, 2, 3, 2, 4, 5]

# result = nums.pop()
result = nums.remove(2) #删除谁写谁  假如删除列表中没有的,会报错
print("remove = ",result, nums)

#注意循环内删除列表元素带来的坑
nums = [1, 2, 2, 2, 3, 4, 2]

for num in nums:
    print(num)
    if num == 2:
        nums.remove(num)

print(nums) #最后的2 没有删除  因为指针移动 最后指针落在2上 会移除列表中最左侧的2

nums.remove(2)

print(nums)

print("--------------------修改操作-----------------------")
# 改
# 	names[index] = 666
# 当我们以后想要操作一个列表当中的某个元素时, 一定是通过这个索引(下标), 来操作指定元素
#
nums = [1, 2, 3, 4, 5]
nums[2] = 6
print("改 = ",nums) #注意越界问题  越界会报错


print("--------------------查询操作-----------------------")
# # 获取单个元素
# # 	items[index]
# # 		注意负索引
# nums = range(10)
nums = [3, 4, 5, 6, 5, 7, 55, 5, 8, 9]
print(nums[1])
print(nums[-1]) #取最后一个

# # 获取元素索引
# # 	index()
#
idx = nums.index(5, 3) #从第三个位置 开始查找列表中5的位置
print(idx)


# # 获取指定元素个数
# # 	count()
c = nums.count(5)
print(c)

# # 获取多个元素
# # 	切片
# # 		items[start:end:step]
nums = [3, 4, 5, 6, 5, 7, 55, 5, 8, 9]
# pic = nums[1:7:2]
pic = nums[::-1]
print(pic)


print("-------------------列表的遍历操作--------------------------")
# 方式1
# 	根据元素进行遍历
# 		for item in list:
# 	print(item)
values = ["a", "a", "a", "d"]
currentIndex = 0
for v in values:
    # print(v)
    print(values.index(v, currentIndex))
    currentIndex += 1

# 方式2
# 	根据索引进行遍历
# 		for index in range(len(list)):
# 	print(index, list[index])

values = ["a", "b", "c", "e", "f", "g"]

# 1. 造一个索引列表(我们要查询的, 要遍历的索引列表) 0 --- 4
count = len(values)
print(count)
indexs = range(count)

# 2. 遍历整个的索引列表, 每一个索引,  索引 -> 指定的元素
for index in indexs:
    print(index, values[index])

#方式3:
values = ["a", "b", "c", "e", "f", "g"]

# 1. 先根据列表, 创建一个枚举对象
print(list(enumerate(values)))

# 遍历整个的枚举对象(枚举对象, 可以直接被遍历)
for idx, val in enumerate(values):
    print(idx,val)

for idx, val in enumerate(values, 3): #索引从3开始,一般不常用,都是从0开始
    print(idx, val)

print("----------------------访问集合的方式,迭代器-------------------------")

nums = [1, 2]

#如何知道一个对象是否可以迭代  用isinstance
import collections
result = isinstance(nums, collections.Iterable)
print(result)  #True  是一个迭代对象


result2 = isinstance(nums, collections.Iterator)
print(result2) #False 但不是一个迭代器

i = iter(nums)
print(i)
result = isinstance(i, collections.Iterable)
print(result)


l = [1, 2, 3, 4, 5]

# 1. 创建一个迭代器对象
it = iter(l)

# next()
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

for v in it:
    print(v)

print("-------")

for v in it: #迭代器只能使用一次
    print(v)

print("----------------------判定,比较,排序-------------------------")
# 判定
# 	元素 in  列表
# 	元素 not in 列表
s = "abc"
print("a" in s) #True
print("c" not in s)#False
values = [1, 2, 3, 4, 5]
print("判定",15 in values)
print("判定",15 not in values)

# 比较
# 	cmp()
# 		内建函数
# 		如果比较的是列表, 则针对每个元素, 从左到右逐一比较
# 			左 > 右
# 				1
# 			左 == 右
# 				0
# 			左 < 右
# 				-1
# 		Python3.x不支持
# 	比较运算符
# 		==
# 		>
# 		<
# 		...
# 		针对每个元素, 从左到右逐一比较
# result = cmp("aad", "aba") #Python3.x不支持
# result = cmp([2, 3, 3], [2, 3]) #Python3.x不支持
result = [2, 3, 4] > [2, 3, 3]
print("cmp",result)

#排序
#方式1:
s1 = "acbegscv"
s = [1, 3, 2, 6, 4, 5]
result1 = sorted(s1, reverse=True)
print("sort",result1, s1)
result = sorted(s)
print("sort",result, s)


s = [("fh", 18),  ("fh2", 16), ("fh1", 17), ("fh3", 15)]
def getKey(x):
    return x[1]
result = sorted(s, key=getKey, reverse=True)
print(result)

#方式2:
l = [1, 3, 2, 6, 4, 5]
l = [("fh", 18),  ("fh2", 16), ("fh1", 17), ("fh3", 15)]
def getKey(x):
    return x[1]
res = l.sort(key=getKey, reverse=True)
print(res, l)

print("--------------------乱序和反转---------------------------")
# 乱序
# 	可以随机打乱一个列表
# 		导入random模块
# 			import random
# 		random.shuffle(list)

import random
l = [1, 2, 3, 4, 5]
res = random.shuffle(l)
print("乱序",res, l)

# # 反转
# # 	l.reverse()

res = l.reverse()
print("反转",res, l)

# # 	切片反转
# # 		l[::-1]

res = l[::-1]
print("切片",res, l)
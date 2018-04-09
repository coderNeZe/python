#_*_encoding:utf-8_*_

# 定义
#   元祖不可变
# 	一个元素的写法
# 		（666,）

l = [1]
print(type(l))

t = (1,) #注意要写,号
print(type(t))


# # 	多个元素的写法
# # 		(1,2,3)
t = ("abc", [1, 2], 3)
print(type(t))

# # 	多个对象，以逗号隔开，默认为元组
t1 = 1, 2, 3, "sz"
print(t1, type(t1))


# # 	从列表转换成元组
# # 		tuple(seq)
# # 			将列表转化为元组
l = [1, 2, 3, 4]
changeTuple = tuple(l)
print(changeTuple, type(changeTuple))


# 		内建函数
# 	补充: 元组嵌套
# 		元组的中元素可以是元组
t3 = (1, 2, ("a", "b"))
print(t3, type(t3))


print("-------------------------------------常用操作---------------------------")
t = (1, 2, 3, 4, 5)
# del t[0]
# t[0] = 666  #错误 元祖不能删除,因为不可变  增,删,改都不可以


# 查
# 	获取单个元素
# 		tuple[index]
# 		index 为索引
# 			可以为负
print(t[-1])


# # 	获取多个元素
# # 		切片
# # 		tuple[start: end: step]
# print(t[0:3])
print(t[4:1:-1])

print("----------------------------额外操作--------------------------------------")
# 获取
# 	tuple.count(item)
# 		统计元组中指定元素的个数
# 	tuple.index(item)
# 		获取元组中指定元素的索引
# 	len(tup)
# 		返回元组中元素的个数
# 	max(tup)
# 		返回元组中元素最大的值
# 	min(tup)
# 		返回元组中元素最小的值
t = (1, 2, 3, 2, 4)
c = t.count(12)  #统计元素的个数
print(c)

idx = t.index(3) #找不到会报错
print(idx) #2

length = len(t)
print(length)

maxNum = max(t)
minNum = min(t)
print(maxNum, minNum)

# 判定
# 	元素 in  元组
# 	元素 not in 元组
print(11 in t)
print(11 not in t)



# 比较
# 	cmp()
# 		内建函数
# 		如果比较的是元组, 则针对每个元素, 从左到右逐一比较
# 			左 > 右
# 				1
# 			左 == 右
# 				0
# 			左 < 右
# 				-1
# 		Python3.x不支持
# tuple list
# result = cmp((0, 2), [1, 2])
# print result


# 	比较运算符
# 		==
# 		>
# 		<
# 		...
# 		针对每个元素, 从左到右逐一比较
result = (4, 2) > (3, 4)
print("比较",result)

print("----------------------------拼接和拆包--------------------------------------")
# 拼接
# 	乘法
# 		(元素1, 元素2...) * int类型数值
# 			=
# 				(元素1, 元素2..., 元素1, 元素2..., ...)
# 	加法
# 		(元素1, 元素2) + (元素a, 元素b)
# 			=
# 				(元素1, 元素2, 元素a, 元素b)

print((1, 2) * 3)
print((1, 2) + (3, 4))
# print((1, 2) + [3, 4])  #报错,不能相加

# 拆包
# 	a, b = (1, 2)
# 		a = 1
# 		b = 2
a = 10
b = 20
t = (a, b)
print(t[0], t[1])   #这样写很麻烦

a, b = (10, 20)
print(a, b)
#或者
a, b = 10, 20
print(a, b)

#利用元祖,交互两个值
a = 1
b = 2
b, a = (a, b)
print(a, b)
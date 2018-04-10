print("--------------------集合的定义-----------------")
# 集合的定义
# 可变集合
s = {1, 2, 3}
print(s, type(s))

#转换成集合
s2 = set("abc")
s3 = set([1, 2, 3])
s4 = set({"name": "fh", "Age": 18})  #如果是字典,只会取key
s5 = set((1, 2, 3))
print(s2, type(s2))
print(s3, type(s2))
print(s4, type(s2))
print(s5, type(s2))

#集合推导式
s = set(x for x in range(0, 10))
print(s, type(s))
s = {x for x in range(0, 10)}
print(s, type(s))


# 不可变集合的定义
fs = frozenset("abc")
fs = frozenset([1, 2, 3])
fs = frozenset((1, 2, 3))
fs = frozenset({"name": "fh", "age": 18})
print(fs, type(fs))

#集合推导式
s = frozenset(x ** 2 for x in range(1, 10) if x % 2 == 0)
print(s, type(s))

#定义时的注意事项
#创建一个空的集合时
s = {}  #不能这么写,会当成字典
print(type(s))

#而应该这么使用
# s = set()
# s = frozenset()

# s = {1, 2, [1, 2]} #集合中的元素不能是可哈希(可变)的, list是可变的 会报错
# s = {1, 2, {"name": "sz"}} #报错
s = {1, 2, 1}  #不会报错,有重复元素,会做去重操作
print(s, type(s))

#去重的操作
l = [1, 2, 3, 3, 3]
s = set(l)
print(s)
result = list(s)
print(result, type(result))

print("--------------------------集合的操作----------------------------------")
#可变集合
# 增
s = {1, 2, 3}
s.add(4)
# s.add([1, 2]) #报错,不能添加list
print(s, type(s))


# 删
# 	s.remove(element)
# 		指定删除set对象中的一个元素
# 		如果集合中没有这个元素，则返回一个错误
s = {1, 2, 3}
result = s.remove(3)
# result = s.remove(13)  #报错,如果集合中没有 会删除
print(result, s)

# 	s.discard(element)
# 		指定删除集合中的一个元素
# 		若没有这个元素，则do nothing
result = s.discard(2)
result = s.discard(13)
print(result, s)



# 	s.pop(element)
# 		随机删除并返回一个集合中的元素
# 		若集合为空，则返回一个错误
s = {1, 2, 3}
result = s.pop()
print(result, s)

result = s.pop()
print(result, s)

result = s.pop()
print(result, s)

# result = s.pop()  #若集合为空，则返回一个错误
# print(result, s)

# 	s.clear()
# 		清空一个集合中的所有元素
s = {1, 2, 3}
result = s.clear()
print(result, s)

#遍历
#方式1: for in

s = {1, 2, 3}
s = frozenset([1, 2, 3])
print(s, type(s))

for v in s:
    print(v)


# 1. 生成一个迭代器
its = iter(s)

# 2. 使用这个迭代器去访问(next(), for in)
print(next(its))
print(next(its))
print(next(its))
# print(next(its))  #注意越界

print("-------")

for v in its:   #不能再执行了
    print(v)


print("-----------------------------集合之间的操作----------------------------------")
# 交集
# 	intersection(Iterable)
# 		字符串
# 			只判定字符串中的非数字
# 		列表
# 		元组
# 		字典
# 			值判定key
# 		集合
# 		...
# 	逻辑与 '&'
# 	intersection_update(…)
# 		交集计算完毕后, 会再次赋值给原对象
# 			会更改原对象
# 			所以, 只适用于可变集合
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6}
result = s2.intersection(s1)  # result = s2 & s1  #作用和intersection一致
print(result, type(result))  #{4, 5} <class 'set'>
print(s1, s2) #s1 和 s2本身没有变化

#如果使用intersection_update
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6}
result = s2.intersection_update(s1) #求得的结果会重新赋值给s2
print(result, type(result))  #None <class 'NoneType'>
print(s1, s2) #{1, 2, 3, 4, 5} {4, 5}

#新生成的类型是否是可变集合的验证
s1 = frozenset([1, 2, 3, 4, 5])
s2 = {4, 5, 6}
result = s2.intersection_update(s1)
print(type(s2)) # 取决于调用者是否是可变的


s1 = {"1", "2", "3", "4", "5"}
print(s1.intersection("123"))   #{'3', '1', '2'}
print(s1.intersection({"1": "abc", "2": "12", "6": 18})) #字典和集合也可以求交集
print(s1.intersection(["1", "2"]))  #列表和集合也可以求交集  但列表总不能有列表

# 并集
# 	union()
# 		返回并集
# 	逻辑或 '|'
# 		返回并集
# 	update()
# 		更新并集
# s1 = {1, 2, 3}
s1 = frozenset([1, 2, 3])
s2 = {3, 4, 5}
result = s1.union(s2)  #  result = s1 | s2
print(result, s1)  #result是否可变,看调用者是否可变  可以使用上边不可变s1注释,放开可变的s1,运行下看看效果

s1 = {1, 2, 3}
s2 = {3, 4, 5}
result = s1.update(s2)
print(result, s1)   #s1 本身发生变化

# 差集
# 	difference()  属于A不属于B的部分
# 	算术运算符减 ‘-‘
# 	difference_update()
s1 = {1, 2, 3}
s2 = {3, 4, 5}

# result = s1.difference(s2)  #result = s1 - s2
result = s1.difference_update(s2)
print(result, s1)


# 判定
# 	isdisjoint()两个集合不相交
# 	issuperset()一个集合包含另一个集合  父集合
# 	issubset()  一个集合包含于另一个集合  子集合
s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6}
print(s1.isdisjoint(s2))
print(s1.issuperset(s2))
print(s2.issubset(s1))
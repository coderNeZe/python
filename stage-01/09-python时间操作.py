print("-------------------时间获取----------------------")
#获取时间戳
import time
result = time.time()
years = result / (24 * 60 * 60 * 365) + 1970
print(years)
print(result)  #时间戳

#获取时间元组
result = time.localtime(1523342592.3829079) #这里传的是上边获取到的时间戳
print(result)


# 获取格式化的时间
# 	秒 -> 可读时间
# 		import time
# 		time.ctime([seconds])
# 			seconds
# 				可选的时间戳
# 				默认当前时间戳
t = time.time()
result = time.ctime(t)
print(result)


# 	时间元组 -> 可读时间
# 		import time
# 		time.asctime([p_tuple])
# 			p_tuple
# 				可选的时间元组
# 				默认当前时间元组
time_tuple = time.localtime()
result = time.asctime(time_tuple)
print(result)

#自定义格式化时间
# 字符串 -> 格式化日期
# 	time.strftime(格式字符串, 时间元组)
# 	例如
# 		time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# 		2017-09-02 17:21:00
result = time.strftime("%y===%m-%d %H:%M:%S", time.localtime()) #Y大写 是4位的年
print(result)

#格式化日期 -> 时间元组
pt = time.strptime("17===09-06 08:57:17", "%y===%m-%d %H:%M:%S")
print(pt)

#时间元组 -> 时间戳
t = time.mktime(pt)
print(t)


#获取当前CPU时间  可以测试代码的执行时间
start = time.clock()
for i in range(0, 10000):
    # print(i)
    pass
end = time.clock()
print(end - start)

#休眠N秒  每隔一秒打印下时间
# while True:
#     result = time.strftime("%y===%m-%d %H:%M:%S", time.localtime())
#     print(result)
#     time.sleep(1)


#获取某年某月
import calendar
print(calendar.month(2018, 5))

#datetime模块的学习
#获取当天的日期 时 分 秒
import datetime
t = datetime.datetime.now()
print(datetime.datetime.today())

print(type(t))
print(t.year)
print(t.month)
print(t.day)

print(t.hour)
print(t.minute)
print(t.second)


print("==============计算n天后的日期")
t = datetime.datetime.today()
result = t + datetime.timedelta(days=7)
print(t, result)

print("==============两个时间的差值")
first = datetime.datetime(2017, 9, 2, 12, 00, 00)
second = datetime.datetime(2017, 9, 3, 12, 00, 00)
print(first, type(first))
delta = second - first
print(delta, type(delta))
print(delta.total_seconds())
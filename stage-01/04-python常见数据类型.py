print("====================数值,进制的转换")
#进制
'''
二进制:0b
八进制:0/0o
十六进制:0x
'''

'''
二转十
1101
1*2^3 + 1*2^2 + 0*2^1 + 1*2^0  
8        4       0       1  = 13 
'''
print(0b1101)
'''
八转十
34
3*8^1 + 4*8^0  
4       24       4  = 28 
'''
print(0o34)

'''
十转其他进制
整除倒取余数
十转二
18/ 2 = 9 余 0
9/2 = 4 余 1
4/2 = 2 余 0
2/2 = 1 余 0
从最后一个结果开始取,就是10010
'''
print(bin(18))#0b10010

'''
十转其他进制
整除倒取余数
十转8
18/ 8 = 2 余 2
从最后一个结果开始取,就是22
'''
print(oct(18))#0o22
#十转16
print(hex(18))#12

'''
二转八
整合3位为一位
10010

010 010
2    2
'''

'''
二转十六
整合4位为一位
10010

0001 0010
1     2
'''
print("====================数学函数")
#内建函数
# 绝对值
print(abs(-10))
#最大值
print(max(1,2,3,4,5))
#最小值
print(min(1,12,3,5))

print(min([1,3,5,2]))

#四舍五入
#round[,n] n表示保留几位小数,可以省略
print(round(3.14,2))#这个2就是保留2位小数

#pow(x,y) 返回x的y次幂 相当于**
print(pow(2,4))
print(2 ** 4)

#math模块函数
#导入模块
import math
#上取整
print(math.ceil(3.4))
#下取整
print(math.floor(3.8))
#开平方
print(math.sqrt(16))
#求对数
math.log(10000,10)  #10的多少次方等于10000

#随机函数
import random
#random [0,1)
print(random.random())

#choice 从序列中,随机挑选一个数值
print(random.choice([1,3,4,5,7,8]))

#uniform(x,y)   [x,y]范围内的随机小数
print(random.uniform(1, 3))

#randint(x,y) [x,y]范围内的随机整数
print(random.randint(1,3))

#randrange(star,stop,step) [start,stop) 第三个参数是步长的意思  randint,不包含结束点  相当于半开半闭 [)
print(random.randrange(1,4,2))  #步长的意思,从1开始,每次随机产生的数是在1的基础上加上步长 eg: 能随机出 1 3

#三角函数
'''
sin(x) 正弦  
cos(x) 余弦
tan(x) 正切
asin(x) 反正弦
acos(x) 反余弦
atan(x) 反正切
degress(x) 弧度 -> 角度
radians(x) 角度 -> 弧度

pi  3.14.....
'''
#sin(x) x,参数 所接收的是一个弧度  要转弧度
#例如  30度 ->弧度   30 /180 * pi
print(math.sin(30 / 180 * math.pi))
print(math.sin(math.radians(30)))

print("====================bool")
#bool
print(True + 2) #3
print(False + 2) #2

#前边一个类型是不是后边类型的子类
result = issubclass(bool,int)
print(result) #0

#if True:
 #   print("这里是真的")

#while True:
#    print("xx")

print("====================字符串")
#字符串
str1 = 'aaa'
print(str1,type(str1))

str1 = "abc"
print(str1,type(str1))

str1 = '''111'''
print(str1,type(str1))

str1 = """222"""
print(str1,type(str1))

str1 = """a\taa"""
print(str1, type(str1))

#转意符
print("我是\"wfh\"")
#或者
print('wo shi "wfh" ')

#原始字符串 前边加r即可
print(r"hello \n world") #hello \n world

result = ("he"
          "zi")
print(result)

result = """
nishi shui
ni buyong guan 
"""
print(result)

#"----------------------字符串拼接------------------------------")
#方式1
result = "wfh" + "fh"
print(result)#wfhfh

#方式2
result = "wangfh"      "fh"
print("我是%s"%(result))#我是wangfhfh

#方式3
restult = "我是%s,%d"%("123",123)
print(restult)

#方式4 字符串的乘法
print("fh\t"*10)

#"----------------------字符串切片操作------------------------------")
name  = "0123456"
print(name)#0123456
print(name[3])#3
# print(name[7])#错误 下标越界
print(name[-4])#倒着数 3

print(name[::])#默认是0 步长是1  0123456
print(len(name))#7

#name[起始:结束:步长]  步长小于0 从右往左
print(name[0:len(name):-1])#不能从头部跳到尾部, 或者从尾部跳到头部

print(name[0:2])# 0 1

#获取范围[起始,结束) 起始包含,结束不包含
print(name[0:len(name):-1])#不能从头部跳到尾部, 或者从尾部跳到头部  错误的情况

print(name[::-1])#字符串反转  6543210
print(name[4:1:-1])  #从第四个位置,朝第一个位置,往左移动#432
print(name[-1:4:-1])# 起始位置-1  就已经定位到最后了  步长小于0  从右到左   65

print("----------------------字符串函数操作------------------------------")
#######################内建函数
#查找计算类别
# len
# 	作用
# 		计算字符串的字符个数
# 	语法
# 		len(name)
# 	参数
# 		字符串
# 	返回值
# 		整型
# 		字符个数
name = "woshifh"
name = "我\n是fh"
num = len(name)
print("len = {0}".format(num))

# find
# 	作用
# 		查找子串索引(下标)位置
# 	语法
# 		find(sub, start=0, end=len(str))
# 	参数
# 		参数1-sub
# 			需要检索的字符串
# 		参数2-start
# 			检索的起始位置
# 			可省略, 默认0
# 		参数3-end
# 			检索的结束位置
# 			可省略, 默认len(str)
# 	返回值
# 		找到了
# 			指定索引
# 			整型
# 		找不到
# 			-1
# 	注意
# 		从左到右进行查找
# 		找到后立即停止
#       [start, end)
name = "wo shi fh"
num = name.find("s", 4, 7) #查不到 -1
num = name.find("s") # 3
print("find = {0}".format(num))

# rfind
# 	功能使用, 同find
# 	区别
# 		从右往左进行查找
name = "wo shi ss"
num = name.rfind("s")
print("rfind = {0}".format(num))

# index
# 	作用
# 		获取子串索引位置
# 	语法
# 		index(sub, start=0, end=len(str))
# 	参数
# 		参数1-sub
# 			需要检索的字符串
# 		参数2-start
# 			检索的起始位置
# 			可省略, 默认0
# 		参数3-end
# 			检索的结束位置
# 			可省略, 默认len(str)
# 	返回值
# 		找到了
# 			指定索引
# 			整型
# 		找不到
# 			异常
# 	注意
# 		从左到右进行查找
# 		找到后立即停止
name = "wo shi sz"
num = name.index("s")
print("index = {0}".format(num))  #找不到会直接报错

# rindex
# 	功能使用, 同index
# 	区别
# 		从右往左进行查找
name = "wo shi fh"
num = name.rindex("w")
print("rindex = {0}".format(num))

# count
# 	作用
# 		计算某个子字符串的出现个数
# 	语法
# 		count(sub, start=0, end=len(str))
# 	参数
# 		参数1-sub
# 			需要检索的字符串
# 		参数2-start
# 			检索的起始位置
# 			可省略, 默认0
# 		参数3-end
# 			检索的结束位置
# 			可省略, 默认len(str)
# 	返回值
# 		子字符串出现的个数
# 		整型
name = "wo shi szwo"
print("count = {0}".format(name.count("s")))

print("----------------------字符串函数转换操作------------------------------")
# replace
# 	作用
# 		使用给定的新字符串 替换原字符串中的 旧字符串
# 	语法
# 		replace(old, new[, count])
# 	参数
# 		参数1-old
# 			需要被替换的旧字符串
# 		参数2-new
# 			替换后的新字符串
# 		参数3-count
# 			替换的个数
# 			可省略, 表示替换全部
# 	返回值
# 		替换后的结果字符串
# 	注意
# 		并不会修改原字符串本身
name = "wo shi sz"
# print(name.replace("s", "z"))#wo zhi zz
print(name.replace("s", "z", 1))#wo zhi sz
print(name)

# capitalize
# 	作用
# 		将字符串首字母变为大写
# 	语法
# 		capitalize()
# 	参数
# 		无
# 	返回值
# 		首字符大写后的新字符串
# 	注意
# 		并不会修改原字符串本身
name = "wo shi sz"
print(name.capitalize())
print(name)


# title
# 	作用
# 		将字符串每个单词的首字母变为大写
# 	语法
# 		title()
# 	参数
# 		无
# 	返回值
# 		每个单词首字符大写后的新字符串
# 	注意
# 		并不会修改原字符串本身
name = "wo shi-title*fh2-qq%yy"
print(name.title())
print(name)

# lower
# 	作用
# 		将字符串每个字符都变为小写
# 	语法
# 		title()
# 	参数
# 		无
# 	返回值
# 		全部变为小写后的新字符串
# 	注意
# 		并不会修改原字符串本身
name = "Wo Shi Lower"
print(name.lower())
print(name)

# upper
# 	作用
# 		将字符串每个字符都变为大写
# 	语法
# 		upper()
# 	参数
# 		无
# 	返回值
# 		全部变为大写后的新字符串
# 	注意
# 		并不会修改原字符串本身
name = "Wo Shi UPPer"
print(name.upper())
print(name)

print("----------------------字符串函数填充压缩操作------------------------------")
# ljust
# 	作用
# 		根据指定字符(1个), 将原字符串填充够指定长度
# 		l
# 			表示原字符串靠左
# 	语法
# 		ljust(width, fillchar)
# 	参数
# 		参数1-width
# 			指定结果字符串的长度
# 		参数2-fillchar
# 			如果原字符串长度 < 指定长度时
# 			填充过去的字符
# 	返回值
# 		填充完毕的结果字符串
# 	注意
# 		不会修改原字符串
# 		填充字符的长度为1
# 		只有原字符串长度 < 指定结果长度时才会填充
name = "abcdefg "
print(name.ljust(16, "l"))
print(name)

# rjust
# 	作用
# 		根据指定字符(1个), 将原字符串填充够指定长度
# 		r
# 			表示原字符串靠右
# 	语法
# 		rjust(width, fillchar)
# 	参数
# 		参数1-width
# 			指定结果字符串的长度
# 		参数2-fillchar
# 			如果原字符串长度 < 指定长度时
# 			填充过去的字符
# 	返回值
# 		填充完毕的结果字符串
# 	注意
# 		不会修改原字符串
# 		填充字符的长度为1
# 		只有原字符串长度 < 指定结果长度时才会填充
name = "abcdefg"
print(name.rjust(16, "r"))
print(name)

# center
# 	作用
# 		根据指定字符(1个), 将原字符串填充够指定长度
# 		center
# 			表示原字符串居中
# 	语法
# 		center(width, fillchar)
# 	参数
# 		参数1-width
# 			指定结果字符串的长度
# 		参数2-fillchar
# 			如果原字符串长度 < 指定长度时
# 			填充过去的字符
# 	返回值
# 		填充完毕的结果字符串
# 	注意
# 		不会修改原字符串
# 		填充字符的长度为1
# 		只有原字符串长度 < 指定结果长度时才会填充
name = "abcdefg"
print(name.center(18, "c"))
print(name)


# lstrip
# 	作用
# 		移除所有原字符串指定字符(默认为空白字符)
# 		l
# 			表示仅仅只移除左侧
# 	语法
# 		lstrip(chars)
# 	参数
# 		参数-chars
# 			需要移除的字符集
# 			表现形式为字符串
# 				"abc"
# 				表示,"a"|"b"|"c"
# 	返回值
# 		移除完毕的结果字符串
# 	注意
# 		不会修改原字符串
name = "wwwoo shi fh "
print("|" + name.lstrip() + "|")  #这个| 是为了方便观察,可以看出lstrip只会移除左边的空格  |wwwoo shi fh |
print("|" + name.lstrip("wo") + "|")  #如果指定了要移除的字符,就会去移除指定的   | shi fh |
print("|" + name + "|")  #原字符串并没有发生改变 |wwwoo shi fh |


# rstrip
# 	作用
# 		移除所有原字符串指定字符(默认为空白字符)
# 		r
# 			表示从右侧开始移除
# 	语法
# 		rstrip(chars)
# 	参数
# 		参数-chars
# 			需要移除的字符集
# 			表现形式为字符串
# 				"abc"
# 				表示,"a"|"b"|"c"
# 	返回值
# 		移除完毕的结果字符串
# 	注意
# 		不会修改原字符串
name = "  wwwoo shi fh oowwwoa   "
print()    #|  wwwoo shi fh oowwwoa|      去除右边空格
name1 = "  wwwoo shi fh oowwwoa"
print("|" + name1.rstrip("wo") + "|") #|  wwwoo shi fh oowwwoa|   之所以没移除wo 是因为从右边开始的时候,第一个字母是a,不包含wo所以整个跳过.可以把a去掉,执行下试试
print("|" + name1 + "|")

print("----------------------字符串函数分割拼接操作------------------------------")
# split
# 	作用
# 		将一个大的字符串分割成几个子字符串
# 	语法
# 		split(sep, maxsplit)
# 	参数
# 		参数1-sep
# 			分隔符
# 		参数2-maxsplit
# 			最大的分割次数
# 			可省略, 有多少分割多少
# 	返回值
# 		分割后的子字符串, 组成的列表
# 		list 列表类型
# 	注意
# 		并不会修改原字符串本身
info = "fh-18-180-0558-12345678"
result = info.split("-", 3)  #3  最大分割3次, 之后就不分割了
print(result)
print(info)

# partition
# 	作用
# 		根据指定的分隔符, 返回(分隔符左侧内容, 分隔符, 分隔符右侧内容)
# 	语法
# 		partition(sep)
# 	参数
# 		参数-sep
# 			分隔符
# 	返回值
# 		如果查找到分隔符
# 			(分隔符左侧内容, 分隔符, 分隔符右侧内容)
# 			tuple 类型
# 		如果没有查找到分隔符
# 			(原字符串, "", "")
# 			tuple 类型
# 	注意
# 		不会修改原字符串
# 		从左侧开始查找分隔符
info = "sz-18-180-0558-12345678"
result = info.partition("-")
print(result)
print(info)


# rpartition
# 	作用
# 		根据指定的分隔符, 返回(分隔符左侧内容, 分隔符, 分隔符右侧内容)
# 		r
# 			表示从右侧开始查找分隔符
# 	语法
# 		partition(sep)
# 	参数
# 		参数-sep
# 			分隔符
# 	返回值
# 		如果查找到分隔符
# 			(分隔符左侧内容, 分隔符, 分隔符右侧内容)
# 			tuple 类型
# 		如果没有查找到分隔符
# 			(原字符串, "", "")
# 			tuple 类型
# 	注意
# 		不会修改原字符串
# 		从右侧开始查找分隔符
info = "sz-18-180-0558-12345678"
result = info.rpartition("-")
print(result)
print(info)

# splitlines
# 	作用
# 		按照换行符(\r, \n), 将字符串拆成多个元素, 保存到列表中
# 	语法
# 		splitlines(keepends)
# 	参数
# 		参数-keepends
# 			是否保留换行符
# 			bool 类型
# 	返回值
# 		被换行符分割的多个字符串, 作为元素组成的列表
# 		list 类型
# 	注意
# 		不会修改原字符串
name = "wo \n shi \r fh"
result = name.splitlines(True)
print(result)
print(name)

# join
# 	作用
# 		根据指定字符串, 将给定的可迭代对象, 进行拼接, 得到拼接后的字符串
# 	语法
# 		join(iterable)
# 	参数
# 		iterable
# 			可迭代的对象
# 				字符串
# 				元组
# 				列表
# 				...
# 	返回值
# 		拼接好的新字符串
items = ["sz", "18", "shanghai"]
result = "xxx".join(items)
print(result)

print("----------------------字符串函数判定操作------------------------------")
# isalpha
# 	作用
# 		字符串中是否所有的字符都是字母
# 			不包含该数字,特殊符号,标点符号等等
# 			至少有一个字符
# 	语法
# 		isalpha()
# 	参数
# 		无
# 	返回值
# 		是否全是字母
# 		bool 类型
name = "Fh\t"
name = ""
print("isalpha = {0}".format(name.isalpha()))


# isdigit
# 	作用
# 		字符串中是否所有的字符都是数字
# 			不包含该字母,特殊符号,标点符号等等
# 			至少有一个字符
# 	语法
# 		isdigit()
# 	参数
# 		无
# 	返回值
# 		是否全是数字
# 		bool 类型
name = "123\t"
name = ""
print("isdigit = {0}".format(name.isdigit()))


# isalnum
# 	作用
# 		字符串中是否所有的字符都是数字或者字母
# 			不包含该特殊符号,标点符号等等
# 			至少有一个字符
# 	语法
# 		isalnum()
# 	参数
# 		无
# 	返回值
# 		是否全是数字或者字母
# 		bool 类型
name = "123abc,"
print("isalnum = {0}".format(name.isalnum()))


# isspace
# 	作用
# 		字符串中是否所有的字符都是空白符
# 			包括空格,缩进,换行等不可见转义符
# 			至少有一个字符
# 	语法
# 		isspace()
# 	参数
# 		无
# 	返回值
# 		是否全是空白符
# 		bool 类型
name = "\n"
print("isspace = {0}".format(name.isspace()))


# startswith
# 	作用
# 		判定一个字符串是否以某个前缀开头
# 	语法
# 		startswith(prefix, start=0, end=len(str))
# 	参数
# 		参数1-prefix
# 			需要判定的前缀字符串
# 		参数2-start
# 			判定起始位置
# 		参数3-end
# 			判定结束位置
# 	返回值
# 		是否以指定前缀开头
# 		bool 类型
name = "2018-09-02: 某某报告.xls"
print(name.startswith("18", 2, 4))



# endswith
# 	作用
# 		判定一个字符串是否以某个后缀结尾
# 	语法
# 		endswith(suffix, start=0, end=len(str))
# 	参数
# 		参数1-suffix
# 			需要判定的后缀字符串
# 		参数2-start
# 			判定起始位置
# 		参数3-end
# 			判定结束位置
# 	返回值
# 		是否以指定后缀结尾
# 		bool 类型
name = "2018-09-02: 某某报告.xls"
name = "2018-09-02: 某某报告.doc"
print(name.endswith(".doc"))


# 补充
# 	in
# 		判定一个字符串, 是否被另外一个字符串包含
# 	not in
# 		判定一个字符串, 是否不被另外一个字符串包含
print("fh" in "wo shi f")  #False
print("fh" not in "wo shi f") #True

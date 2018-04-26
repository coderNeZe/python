print("==================python的注释")
#我是一个注释

"我也是一个注释"

'''
多行
注释
'''

"""
我也是
多行注释
"""

# _*_ coding:utf-8 _*_   解决python2.0中文支持的注释

print("==================python的变量")
#方式1:
a = 2
b = 3

#方式2
a1,b1 = 2, 3

#方式3
a2 = b2 = 3

print("==================python的数据类型")
print(6+6) #12
print("6" + "6") #66
#查看类型
print(type(6))
print(type("6"))

print("==================python的数据类型的转换")
a = "6"
# print(4+num) #会报错,类型不一致
print(4 + int(a))
print(str(4) + a)
#静态类型:类型是编译的时候确定的,后期无法修改
#动态类型:类型是运行时进行判定的, 可以动态修改

#强类型:类型比较强势, 不轻易随着环境的变化而变化 eg:  'a' + 1   会报错
#弱类型:类型比较柔弱, 不同的环境下, 很容易被改变 eg: 'a' + 1  输出a1
#结论:Python是属于, 强类型的, 动态类型的语言

print("==================python的算术运算符")
#加法运算符
print(1+2)
print("1"+"2")
print([1,2]+[3,4])

#减法运算符
print(4-12)

#乘法运算符
print(2 * 3)

#幂运算符
print(3 ** 5)

#除法运算符
print(5 / 2)
# print(5 / 0)  #会报错,被除数不能是0

#整除运算符
print(5.2 // 2)  #注意,结果不是四舍五入 ,只是直接取整数部分

#求模运算符
print(5 % 2)  #1  其实就是求余数

#优先级问题
print((1+2) * 3 / 4)

#整除求余的应用场景  九宫格的计算
#一个九宫格有4列,计算某个数字的位置
weizhi = 6  #计算6是几行几列
row = weizhi // 4
col = weizhi % 4

print("==================python的逻辑运算符")
b = True
# not 取反操作
print(not b)

#and 并且的意思  and 的两边 必须都是真 才能为真
print(True and  False)

#or or两边 一个为真就是真
print(True or False)

#bool 非0即真  非空即真
print(bool(1))
print(bool(0))
print(bool("")) #False

print("==================python的比较运算符")
print(10 > 2)
print(10 != 10)
print(10 == 10) #比较的是值

#is  比较唯一标识(即内存)
ten = 10
print(id(ten))

aa = 10
bb = 10
print(aa is bb) #True

aaa = [1]
bbb = [1]
print(aaa == bbb) #Ture
print(aaa is bbb) #Flase  内存空间是不一样的

#链式比较运算符
number = 10
print(5 < number < 20)

print("==================python复合运算符")
nn = 10
nn += 5
print(nn)

print(nn * 20)

print("==================python的输出")
#输出一个变量
num = 55
print(num)

#输出多个变量
num2 = 44
print(num,num2)

#格式化输出
name = 'wfh'
age = 18
print("我的名字是%s,年龄是%d"%(name,age))
print("我的名字是{0},年龄是{1}".format(name,age))

#输出到文件中
# f = open("text.txt","w")
# print("xxxxx",file=f)

#输出不自动换行
print("abc",end="")

#输出的各个数据,使用分隔符分割
print("1","2","3",sep="&&&")

#flush参数的说明:清空缓存,马上输出的控制台
print("请输入账号",end="",flush=True)

print("==================浅拷贝")
ss = [11,22,33]
ss1 = ss #只是指针指向的改变,是浅拷贝
print(id(ss),id(ss1))

print("==================深拷贝")
import copy
fh = [11,22,33]
fh1 = copy.deepcopy(fh) #深拷贝
fh.append(44)
print(fh,fh1)
print(id(fh),id(fh1))

print("==================deepcopy的进一步理解")
#只要是深拷贝,会有所的内容都拷贝,比如一个列表里存的也是引用,那么列表里的东西也进行深拷贝
'''
往aa里追加一个元素,dd取出的元素并没有改变,说明列表里的内容进行深拷贝的话,里边的内容也会全部深拷贝
'''
#列表
aal = [11,22]
bbl = [33,44]
ccl = [aal,bbl]
ddl = copy.deepcopy(ccl) #经过此步,内存会新开辟一个空间,dd1会指向这个新空间 dd1和cc1 指向了两个不同的列表地址,
print(id(ccl),id(ddl)) #4322301320 4320565256  地址不同 说明开辟了新空间
aal.append(44)
print(ccl[0],ddl[0]) #[11, 22, 44] [11, 22]  追加一后,其中一个变,另一不变,说明列表里边的内容也深拷贝了

#元组
aay = [11,22]
bby = [33,44]
ccy = (aay,bby)
ddy = copy.deepcopy(ccy) #经过此步,内存会新开辟一个空间,ddy会指向这个新空间 ddy和ccy指向了两个不同的列表地址,
print(id(ccy),id(ddy)) #4302745352 4302744456  地址不同 说明开辟了新空间
aay.append(44)
print(ccy[0],ddy[0]) #[11, 22, 44] [11, 22] 追加一后,其中一个变,另一不变,说明元组里边的内容也深拷贝了


print("==================copy的进一步理解")
#使用copy模块的copy来拷贝不可变类型,如拷贝元组时,不会开辟新空间,指向的内存地址是不改变的
aayc = [11,22]
bbyc = [33,44]
ccyc = (aayc,bbyc)
ddyc = copy.copy(ccyc) #经过此步,因为是元组,不可变,内存不会新开辟一个空间
print(id(ccyc),id(ddyc)) #4328952264 4328952264  地址相同 说明未开辟新空间
aayc.append(44)
print(ccyc[0],ddyc[0]) #[11, 22, 44] [11, 22] 追加一后,其中一个变,另一不变,说明元组里边的内容也深拷贝了

#  如果拷贝可变类型,如列表,它只会拷贝一层,但列表里存的是其他引用时,是不会再依次拷贝列表里的内容(具体看下边的例子)
'''
往aa里追加一个元素,dd取出的元素也改变,说明对列表进行copy,会开辟一个新的内容空间,但列表里的引用指向是不改变的
'''
aa1 = [11,22]
bb1 = [33,44]
cc1 = [aa1,bb1]
dd1 = copy.copy(cc1) #经过此步,内存会新开辟一个空间,dd1会指向这个新空间   dd1和cc1 指向了两个不同的列表地址
print(id(cc1),id(dd1)) #4330695432 4330695496
aa1.append(44)
print(cc1[0],dd1[0]) #[11, 22, 44] [11, 22,44] 追加一后,其中一个变,另一也变,说明元组里边的内容并没有深拷贝

print("==================python的输入")
content = input("请输入内容: ")
result = eval(content)
print(type(result))
print(result)


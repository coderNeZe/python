print("==============读=============")
#1.打开文件
f = open("a.txt","r")

#2.读写文件
content = f.read() #读的前提,文件必须在
print(content)

# f.write("123456") #报错,不能写 因为指定是r

#3.关闭文件
f.close()

print("==============写=============")

#1.打开文件
f = open("b.txt","w") #只写的情况下不能读

#2.读写文件
content = f.write("abc") #多次运行,会覆盖之前文件的内容

#3.关闭文件
f.close()


print("==============a模式=============")
#1.打开文件
f = open("c.txt","a") #a模型不能读

#2.读写文件
content = f.write("123456")  #相比w模式,a模式是追加,不是覆盖 比如c文件中有abc  则运行之后是abc123456

#3.关闭文件
f.close()

print("==============+b模式=============") #以二进制格式操作文件的读写
# 1. 打开xx.jpg文件, 取出内容, 获取内容的前面半部分
# 1.1 打开文件
fromFile = open("1.png", "rb")

# # 1.2 读取文件内容
fromContent = fromFile.read()
print(fromContent)

# # 1.3 关闭文件
fromFile.close()

# 2. 打开另外一个文件xx2.jpg, 然后, 把取出的半部分内容, 写入到xx2.jpg文件里面去
# 2.1 打开目标文件
toFile = open("2.png", "wb")

# 2.2 写入操作
content = fromContent[0: len(fromContent) // 2]
toFile.write(content)

# 2.3 关闭文件
toFile.close()
print("==============增加+模式=============")  #只是增加了读写的操作
#1.打开文件
f = open("a.txt","r+")  #注意,这里先读,文件指针已经移动到最后了
content = f.read()
print(content)
f.write("hhh") #相比单纯的r模式,会增加写的操作  和w模式相比,不会覆盖原先的内容,是拼接操作,并且文件指针在追加的前边
#如果上诉的操作没有先读,则指针一开始在最开始的位置,所以会是替换操作,比如原先内容是123456 然后写入wfh 结果就是wfh456
f.close()


print("==============文件的定位=============")

#f.seek(偏移量,[0,1,2))
'''
0 开头 默认
1 当前位置
2 文件末尾
注意:文本文件的操作模式下(不带b),只能写0
如果想要写1,或者2,必须在二进制文件操作模式下(带b)
'''
#测试文本文件模式下
f = open("e.txt", "r") #12345678
print(f.tell())  #获取当前位置的指针 0
f.seek(2)  #把指针移动到文件的第二个位置  #345678
print(f.tell())  #获取当前位置的指针  6
print(f.read())
f.close()

#测试二进制文件下
f = open("e.txt", "rb") #12345678
#测试seek两个个参数的效果
print(f.tell())
f.seek(-2, 2) #-2:文件流的从最后开始,偏移两个位置,到文件的6的位置,2:指取到文件最后的位置
print(f.tell())
print(f.read()) #b'78'   b:是二进制文件的意思
print(f.tell()) #8  移动到了最后
f.close()

print("==============文件的读操作=============")
# f.read(字节数)
# 	字节数默认是文件内容长度
# 	下标会自动后移
f = open("e.txt", "r")  #12345678
print(f.read(2)) #代表读取文件内容长度  12
f.close()

f = open("e.txt", "r")  #12345678
f.seek(2) #先移动指针
print(f.read(2)) #代表读取文件内容长度  34
f.close()

# f.readline([limit])
# 	读取一行数据
# 	limit
# 		限制的最大字节数
f = open("f.txt","r")
print("----", f.tell())
content = f.readline()
print(content, end="")
print("----", f.tell())
f.close()

# f.readlines()
# 	会自动的将文件按换行符进行处理
# 	将处理好的每一行组成一个列表返回
f = open("f.txt","r")
content = f.readlines()
print(content)
f.close()

print("==============文件的遍历=============")
#可以遍历f本身
import collections
f = open("f.txt","r")
print(isinstance(f,collections.Iterator))  #查看是否是迭代器
for i in f:
    print(i,end="")
f.close()

print("----------------")

#也可以遍历行列表
f = open("f.txt","r")
content = f.readlines()
for i in content:
    print(i,end="")
f.close()

print("==============判读可读=============")
f = open("f.txt","w")
if f.readable():
    print("可读")
else:
    print("不可读")
f.close()

print("==============写入=================")
f = open("g.txt","a")
if f.writable():
    print("可写")
    print(f.write("abc"))
f.close()

print("==============文件操作=================")
import os

#创建目录
# os.mkdir("a")
# os.mkdir("c/d/e") #不支持多级目录的创建
# os.mkdir("a")  如果文件夹存在 会报错
# os.mkdir("b",0o777)  #第二个参数是文件中的权限 #r4 w2 x1


#修改
os.rename("b.txt","bb.txt") #修改文件名称
# os.rename("a","one") #修改文件夹名称  文件夹不在会报错

# os.rename("one/one.txt","two/two.txt")  会报错,因为two文件夹找不到
# os.renames("one/one.txt","two/two.txt") #会一层一层的去修改

#删除操作
#删除文件
# os.remove("2.png") #删除的文件不存在会删除
#删除文件夹
# os.rmdir("two")  #注意,只能删除空目录
# os.removedirs("one")  #递归删除

# 获取当前目录
# 	os.getcwd()
print(os.getcwd())

# print(os.getcwd())
# 改变默认目录
# 	os.chdir("目标目录")
os.chdir("changeDir") #切换文件目录
open("dd.txt","w") #在切换的文件目录下,创建一个dd.txt

# 获取目录内容列表
# 	os.listdir("./")
print(os.listdir("../changeDir"))
print(os.listdir("../"))

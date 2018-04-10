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

print("==============文件的定位=============")
f = open("d.txt", "rb")

print(f.tell())
f.seek(-2, 2)
print(f.tell())

print(f.read())
print(f.tell())

f.close()
# #实现文件的复制操作
# sourceFile = open("a.txt","r",encoding="utf-8")
# desFile = open("a_dat.txt","a",encoding="utf-8")
#
# while True:
#     content = sourceFile.read(1024)
#     if len(content) == 0:
#         break
#     desFile.write(content)
#
# sourceFile.close()
# desFile.close()
#
# print("==================================2.按文件名不同,划分到不同的文件夹====")
# #0, 获取所有的文件名称列表
# import os
# import shutil
#
# path = "files"
#
# if not os.path.exists(path):
#     exit()
#
# os.chdir(path)
#
# file_list = os.listdir("./")
#
# # 1. 遍历所有的文件(名称)
# for file_name in file_list:
#     # print(file_name)
#     # 2. 分解文件的后缀名
#     # 2.1 获取最后一个.的索引位置 xx.oo.txt
#     index = file_name.rfind(".")
#     if index == -1:
#         continue
#     # print(index)
#     # 2.2 根据这个索引位置, 当做起始位置, 来截取后续的所有字符串内容
#     extension = file_name[index + 1:]
#     print(extension)
#
#     # 3. 查看一下, 是否存在同名的目录
#     # 4. 如果不存在这样的目录 -> 直接创建一个这样名称的目录
#     if not os.path.exists(extension):
#         os.mkdir(extension)
#
#     shutil.move(file_name, extension)

print("====================================3.生成txt格式的文件清单====")

import os

# 通过给定的文件夹, 列举出这个文件夹当中, 所有的文件,以及文件夹, 子文件夹当中的所有文件
def listFilesToTxt(dir, file):
    # 1. 列举出, 当前给定的文件夹, 下的所有子文件夹, 以及子文件
    file_list = os.listdir(dir)
    # 2. 针对于, 列举的列表, 进行遍历
    for file_name in file_list:
        new_fileName = dir + "/" + file_name  #files/avi
        # 判定, 是否是目录, listFiles
        if os.path.isdir(new_fileName): #是目录
            file.write(new_fileName + "\n")
            listFilesToTxt(new_fileName, file)
        else:
            file.write("\t" + file_name + "\n")
    file.write("\n")


f = open("list.txt", "a")
listFilesToTxt("files", f)

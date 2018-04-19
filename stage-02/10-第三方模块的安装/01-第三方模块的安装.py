print("============单文件模块的安装============")
#先查看所有模块的路径 通过sys这个库查看
import sys
print(sys.path)
# 自己加载的单文件模块一般放在这个目录下'/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages']
#一下是测试
import TestSingleFileTool
TestSingleFileTool.printHello()

print("============安装带setup.py文件的安装============")
'''
1.先安装setuptools 源码去网站下载 然后进入到有setup.py的文件夹
2.通过命令行执行python3 setup.py install 安装setuptools
3.以安装第三方模块requests为例, 先下载下来 然后进入到有setup.py的文件夹
4.依旧执行命令行python3 setup.py install 就安装好了相应的模块
'''
import requests #安装好之后,导入没有报错


print("============.egg文件的安装============")
"""
1.安装egg文件,大前提是安装了setuptools这个工具
2.找到对应的文件夹,执行 easy_install xxxx.egg
"""

print("============.whl文件的安装============")
'''
首先,setuptools这个工具也能安装 命令和安装egg文件的一致
但是推荐使用pip安装(前提要安装pip)
pip3 install xxxx
easy_install xxxx
'''

'''
卸载包
pip3 uninstall xxx
'''
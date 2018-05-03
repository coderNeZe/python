# import os
# import time
# '''
# fork可以创建一个新的进程
# '''
# ret = os.fork() #他有两个返回值,会区分父子进程,主进程的ret>0  子进程的ret==0
# '''
# 父进程中fork的返回值,就是刚刚创建出来子进程的id
# '''
# print(ret)  # 855456 0  85546是主进程创造一个子进程后,子进程所在的进程是85546
# '''
# 注意:但你不能说这个ret == 855456 > 0  是主进程创建的子进程id 那就应该代表子进程才对呀? 你下边的判断是不是反了
# 这里一定要注意,区分父子进程 只看ret是否==0,ret等于0 就是子进程, ret > 0  就是父进程  而ret==855456只是说创建的子进程id是85546,不能作为区分父子进程
# '''
# if ret > 0:
#     while True:
#         print("----父进程---%d"%os.getpid()) #getpid打印出当前的进程 比如是85545
#         time.sleep(1)
# else:
#     while True:
#         print("----子进程---%d-%d"%(os.getpid(),os.getppid()))  #父进程创建出子进程 所以getppid打印他的父进程就是85545 而自己所在的进程的是85546
#         time.sleep(1)
#
# 85546
# ----父进程---85545
# 0
# ----子进程---85546-85545
print("------------------父子进程的先后顺序------------------")
import os
'''
主进程结束,不会因为子进程没有结束,而等待子进程
'''
#因为有延时,所以先注释
# import os
# import time
#
# ret = os.fork()
#
# if ret==0:
#     print("----子进程1---")
#     time.sleep(5)
#     print("----子进程2---")
# else:
#     print("----父进程---")
#     time.sleep(3)
#
# print("----over---")

print("------------------修改全局变量------------------")
#全局变量在多个进程中不共享
# import os
# import time
#
# g_num = 100
#
# ret = os.fork()
# if ret == 0:
#     print("----process-1----")
#     g_num += 1
#     print("---process-1 g_num=%d---"%g_num)
# else:
#     time.sleep(3)
#     print("----process-2----")
#     print("---process-2 g_num=%d---"%g_num)

#想要完成进程间的数据共享,需要一些方法:命名管道/无名管道/共享内存/消息队列/网络等

print("------------------多次fork------------------")
# import os
# import time
#
# #父进程
# ret = os.fork()
#
# if ret==0:
#     #子进程
#     print("--1--")
# else:
#     #父进程
#     print("--2--")
#
# #父子进程
# ret = os.fork()
# if ret==0:
#     #孙子
#     #2儿子
#     print("--11--")
# else:
#     #儿子
#     #父进程
#     print("--22--")

print("------------------Process创建进程------------------")
#fork不跨平台,不常用,用Process
# from multiprocessing import Process
#
# import time
#
# def test():
#     while True:
#         print("---test---")
#         time.sleep(1)
#
# p = Process(target=test)
# p.start() #让这个进程开始执行test函数里的代码
#
# while True:
#     print("---main---")
#     time.sleep(1)

print("------------------Process创建的子进程和主进程的结束------------------")
#Process创建的进程,主进程会等待子进程结束后,再结束
# from multiprocessing import Process
# import time
#
# def test():
#     for i in range(2): #模拟两秒后,子进程结束
#         print("---test---")
#         time.sleep(1)
#
# p = Process(target=test)
# p.start() #让这个进程开始执行test函数里的代码  创建子进程后,子进程开始运行,运行后发现,主进程并没有马上结束,而是等待子进程结束后,父进程再结束

print("------------------join子进程------------------")
#如果想等待子进程结束后,再运行 可以使用join

# from multiprocessing import Process
# import time
# import random
#
# def test():
#     for i in range(random.randint(1,5)):
#         print("----%d---"%i)
#         time.sleep(1)
#
# p = Process(target=test)
#
# p.start()
#
# p.join(1)#堵塞  如果不传时间,就等子进程结束
#
# print("----main----")

print("------------------Process子类创建进程------------------")

# from multiprocessing import Process
# import time
#
# class MyNewProcess(Process):
#     def run(self): #重写run方法
#         while True:
#             print("---1----")
#             time.sleep(1)
#
#
# p = MyNewProcess()
# p.start()  #start的时候,会自动的调用run方法
#
# while True:
#     print("---main----")
#     time.sleep(1)

print("------------------进程池------------------")
# from multiprocessing import Pool
# import os
# import random
# import time
#
# def worker(num):
#     for i in range(5):
#         print("===pid=%d==num=%d="%(os.getpid(), num))
#         time.sleep(1)
#
# #3表示 进程池中对多有3个进程一起执行
# pool = Pool(3)
#
# for i in range(10):
#     print("---%d---"%i)
#     #向进程池中添加任务
#     #注意：如果添加的任务数量超过了 进程池中进程的个数的话，那么不会导致添加不进入
#     #       添加到进程中的任务 如果还没有被执行的话，那么此时 他们会等待进程池中的
#     #       进程完成一个任务之后，会自动的去用刚刚的那个进程 完成当前的新任务
#     pool.apply_async(worker, (i,))  #非阻塞的方式
#
#
# pool.close()#关闭进程池，相当于 不能够再次添加新任务了
# pool.join()#主进程 创建／添加 任务后，主进程 默认不会等待进程池中的任务执行完后才结束
#             #而是 当主进程的任务做完之后 立马结束，，，如果这个地方没join,会导致
#             #进程池中的任务不会执行

print("------------------进程池-apply------------------")
# from multiprocessing import Pool
# import os
# import random
# import time
#
# def worker(num):
#     for i in range(5):
#         print("===pid=%d==num=%d="%(os.getpid(), num))
#         time.sleep(1)
#
# #3表示 进程池中对多有3个进程一起执行
# pool = Pool(3)
#
# for i in range(10):
#     print("---%d---"%i)
#     pool.apply(worker, (i,))#堵塞的方式
#
#
# pool.close()#关闭进程池，相当于 不能够再次添加新任务了
# pool.join()#主进程 创建／添加 任务后，主进程 默认不会等待进程池中的任务执行完后才结束
#             #而是 当主进程的任务做完之后 立马结束，，，如果这个地方没join,会导致
#             #进程池中的任务不会执行

print("------------------Queue------------------")
# from  multiprocessing import Queue
#
# q = Queue(3)
# q.put("消息1")
# q.put("消息2")
# print(q.full()) #False 未满
#
# q.put("消息3")
# print(q.full()) #True  已经满了
#
# #推荐的方式,先判断消息队列是否已满,再写入
# if not q.full():
#     q.put_nowait("消息4")
#
# #读取时,先判断消息队列是否为空,再读取
# if not q.empty():
#     for i in range(q.qsize()): #这句话会报错,不知道为啥
#         print(q.get_nowait())

print("------------------Queue实例------------------")
# #在父进程中创建两个子进程,一个往Queue里写数据,一个从Queue里读数据
# from multiprocessing import Process,Queue
# import os,time,random
#
# #写数据进程执行的代码
# def write(q):
#     for value in ['A','B','C']:
#         print("put %s to queue"%value)
#         q.put(value)
#         time.sleep(random.random())
#
# #读数据进程执行的代码
# def read(q):
#     while True:
#         if not q.empty():
#             value = q.get(True)
#             print("get %s from queue"%value)
#             time.sleep(random.random())
#         else:
#             break
#
# if __name__ == '__main__':
#     #父进程创建Queue,并传给各个子进程
#     q = Queue()
#     pw = Process(target=write,args=(q,))
#     pr = Process(target=read,args=(q,))
#
#     #启动子进程,写入
#     pw.start()
#     #等待pw结束:
#     pw.join()
#
#     #启动子进程pr,读取
#     pr.start()
#     pr.join()
#     print("所有数据都写入并且读完")

print("------------------进程池中的Queue------------------")
# #如果要使用Pool创建进程,就需要使用multiprocessing.Manager()中的Queue(),而不是multiprocessing.Queue(),否则会报错
# from multiprocessing import Manager,Pool
# import os,time,random
#
# def reader(q):
#     print("reader启动(%s),父进程为(%s)"%(os.getpid(),os.getppid()))
#     for i in range(q.qsize()):
#         print("reader从Queue获取到消息:%s"%q.get(True))
#     pass
#
# def writer(q):
#     print("write启动(%s),父进程为%s"%(os.getpid(),os.getppid()))
#     for i in "Haoge":
#         q.put(i)
#
# if __name__ == '__main__':
#     print("%s start"%os.getpid())
#     q = Manager().Queue() #使用Manager中的Queue来初始化
#     p = Pool()
#     p.apply(writer,(q,))#使用阻塞模式创建进程
#     p.apply(reader,(q,))
#     p.close()
#     p.join()
#     print("%s End"%os.getpid())

print("------------------使用多进程实现文件的拷贝------------------")
from multiprocessing import Pool,Manager
import os

def copyFileTask(name,oldName,newName,queue):
    fr = open(oldName+"/"+name)
    fw = open(newName+"/"+name,"w")

    content = fr.read()
    fw.write(content)

    fr.close()
    fw.close()
    queue.put(name)

    pass
if __name__ == '__main__':

    old_file_name = input("请输入要拷贝的文件夹名字:")
    new_file_name = os.mkdir(old_file_name+"_复件")

    fileNames = os.listdir(old_file_name)

    pool = Pool(5)
    queue = Manager().Queue()

    for name in fileNames:
        pool.apply_async(copyFileTask,args=(name,old_file_name,new_file_name,queue))

    num = 0
    allNum = len(fileNames)
    while num < allNum:
        queue.get()
        num += 1
        copyRate = num / allNum
        print("\r copy的进度是:%.2f%%"%(copyRate*100),end="")
    print("\n 已经完成copy")
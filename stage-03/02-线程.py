print("------------------01-使用线程完成多任务------------------")
# #可以明显看出使用了多线程并发的操作,花费时间要短很多
# #创建好的线程,需要调用start()方法来启动
# from threading import Thread
# import time
#
# #如果多个线程执行的都是同一个函数的话，各自之间不会有影响，各是个的
# def test():
#     print("哈哈哈哈")
#     time.sleep(1)
#
# if __name__ == '__main__':
#     for i in range(5):
#         t = Thread(target = test)
#         t.start()

print("------------------02-使用线程的第２种方式------------------")
# import threading
# import time
#
# class MyThread(threading.Thread):
#     def run(self):
#         for i in range(3):
#             time.sleep(1)
#             msg = "I'm "+self.name+' @ '+str(i) #name属性中保存的是当前线程的名字
#             print(msg)
#
# if __name__ == '__main__':
#     t = MyThread()
#     t.start()

print("------------------03-线程的执行顺序------------------")
# import threading
# import time
#
# class MyThread(threading.Thread):
#     def run(self):
#         for i in range(3):
#             time.sleep(1)
#             msg = "I'm "+self.name+' @ '+str(i)
#             print(msg)
# def test():
#     for i in range(5):
#         t = MyThread()
#         t.start()
# if __name__ == '__main__':
#     test()

print("------------------04-多线程使用全局变量------------------")
# from threading import Thread
# import time
#
# #线程之间共享全局变量
# g_num = 100
#
# def work1():
#     global g_num
#     for i in range(3):
#         g_num += 1
#
#     print("----in work1, g_num is %d---"%g_num)
#
#
# def work2():
#     global g_num
#     print("----in work2, g_num is %d---"%g_num)
#
#
# print("---线程创建之前g_num is %d---"%g_num)
#
# t1 = Thread(target=work1)
# t1.start()
#
# #延时一会，保证t1线程中的事情做完
# time.sleep(1)
#
# t2 = Thread(target=work2)
# t2.start()

print("------------------05-线程共享全局变量的问题------------------")
# from threading import Thread
# import time
#
# g_num = 0
#
# def test1():
#     global g_num
#     for i in range(1000000):
#         g_num += 1
#
#     print("---test1---g_num=%d"%g_num)
#
# def test2():
#     global g_num
#     for i in range(1000000):
#         g_num += 1
#
#     print("---test2---g_num=%d"%g_num)
#
#
# p1 = Thread(target=test1)
# p1.start()
#
# # time.sleep(3) #取消屏蔽之后 再次运行程序，结果会不一样，，，为啥呢？
#
# p2 = Thread(target=test2)
# p2.start()
#
# print("---g_num=%d---"%g_num)

print("------------------06-列表传递给线程------------------")
# from threading import Thread
# import time
#
# def work1(nums):
#     nums.append(44)
#     print("----in work1---",nums)
#
#
# def work2(nums):
#     #延时一会，保证t1线程中的事情做完
#     time.sleep(1)
#     print("----in work2---",nums)
#
# g_nums = [11,22,33]
#
# t1 = Thread(target=work1, args=(g_nums,))
# t1.start()
#
# t2 = Thread(target=work2, args=(g_nums,))
# t2.start()

print("------------------07-避免多线程对共享数据出错的方式------------------")
# from threading import Thread
# import time
#
# g_num = 0
# g_flag = 1
#
# def test1():
#     global g_num
#     global g_flag
#     if g_flag == 1:
#         for i in range(1000000):
#             g_num += 1
#
#         g_flag = 0
#
#     print("---test1---g_num=%d"%g_num)
#
# def test2():
#     global g_num
#     #轮询
#     while True:
#         if g_flag != 1:
#             for i in range(1000000):
#                 g_num += 1
#             break
#
#     print("---test2---g_num=%d"%g_num)
#
#
# p1 = Thread(target=test1)
# p1.start()
#
# #time.sleep(3) #取消屏蔽之后 再次运行程序，结果会不一样，，，为啥呢？
#
# p2 = Thread(target=test2)
# p2.start()
#
# print("---g_num=%d---"%g_num)


print("------------------08-使用互斥锁------------------")
# from threading import Thread, Lock
# import time
#
# g_num = 0
#
# def test1():
#     global g_num
#     #这个线程和test2线程都在抢着　对这个锁　进行上锁，如果有1方成功的上锁，那么导致另外
#     #一方会堵塞（一直等待）到这个锁被解开为止
#     mutex.acquire()
#     for i in range(1000000):
#         g_num += 1
#     mutex.release()#用来对mutex指向的这个锁　进行解锁，，，只要开了锁，那么接下来会让所有因为
#                     #这个锁　被上了锁　而堵塞的线程　进行抢着上锁
#
#     print("---test1---g_num=%d"%g_num)
#
# def test2():
#     global g_num
#     mutex.acquire()
#     for i in range(1000000):
#         g_num += 1
#     mutex.release()
#
#     print("---test2---g_num=%d"%g_num)
#
# #创建一把互斥锁，这个锁默认是没有上锁的
# mutex = Lock()
#
# p1 = Thread(target=test1)
# p1.start()
#
# #time.sleep(3) #取消屏蔽之后 再次运行程序，结果会不一样，，，为啥呢？
#
# p2 = Thread(target=test2)
# p2.start()
#
# print("---g_num=%d---"%g_num)

print("------------------10-多个线程使用非全局变量------------------")
# from threading import Thread
# import threading
# import time
#
# def test1():
#     #注意：
#     #   1. 全局变量在多个线程中　共享，为了保证正确运行需要锁
#     #   2. 非全局变量在每个线程中　各有一份，不会共享，当然了不需要加锁
#     name = threading.current_thread().name
#     print("----thread name is %s ----"%name)
#     g_num = 100
#     if name == "Thread-1":
#         g_num += 1
#     else:
#         time.sleep(2)
#     print("--thread is %s----g_num=%d"%(name,g_num))
#
# #def test2():
# #    time.sleep(1)
# #    g_num = 100
# #    print("---test2---g_num=%d"%g_num)
#
#
# p1 = Thread(target=test1)
# p1.start()
#
# p2 = Thread(target=test1)
# p2.start()


print("------------------11-同步的应用-----------------")
# from threading import Thread,Lock
# from time import sleep
#
# class Task1(Thread):
#     def run(self):
#         while True:
#             if lock1.acquire():#可以上锁
#                 print("------Task 1 -----")
#                 sleep(0.5)
#                 lock2.release()
#
# class Task2(Thread):
#     def run(self):
#         while True:
#             if lock2.acquire():
#                 print("------Task 2 -----")
#                 sleep(0.5)
#                 lock3.release()
#
# class Task3(Thread):
#     def run(self):
#         while True:
#             if lock3.acquire():
#                 print("------Task 3 -----")
#                 sleep(0.5)
#                 lock1.release()
#
# #使用Lock创建出的锁默认没有“锁上”
# lock1 = Lock()
# #创建另外一把锁，并且“锁上”
# lock2 = Lock()
# lock2.acquire()
# #创建另外一把锁，并且“锁上”
# lock3 = Lock()
# lock3.acquire()
#
# t1 = Task1()
# t2 = Task2()
# t3 = Task3()
#
# t1.start()
# t2.start()
# t3.start()

print("------------------12-生产者与消费者模式-----------------")
# # #encoding=utf-8
# import threading
# import time
#
# #python2中
# #from Queue import Queue
#
# #python3中
# from queue import Queue
#
# class Producer(threading.Thread):
#     def run(self):
#         global queue
#         count = 0
#         while True:
#             if queue.qsize() < 1000:
#                 for i in range(100): #每次生产100个
#                     count = count +1
#                     msg = '生成产品'+str(count)
#                     queue.put(msg)
#                     print(msg)
#             time.sleep(0.5)
#
# class Consumer(threading.Thread):
#     def run(self):
#         global queue
#         while True:
#             if queue.qsize() > 100:
#                 for i in range(3): #一次消费3个的意思
#                     msg = self.name + '消费了 '+queue.get()
#                     print(msg)
#             time.sleep(1)
#
#
# if __name__ == '__main__':
#     queue = Queue()
#
#     for i in range(500):
#         queue.put('初始产品'+str(i))
#     for i in range(2): #有两个生产者
#         p = Producer()
#         p.start()
#     for i in range(5):
#         c = Consumer() #有五个消费者
#         c.start()

print("------------------13-threadLocal-----------------")
# import threading
#
# # 创建全局ThreadLocal对象:
# local_school = threading.local()
#
# def process_student():
#     # 获取当前线程关联的student:
#     std = local_school.student
#     print('Hello, %s (in %s)' % (std, threading.current_thread().name))
#
# def process_thread(name):
#     # 绑定ThreadLocal的student:
#     local_school.student = name
#     process_student()
#
# t1 = threading.Thread(target= process_thread, args=('dongGe',), name='Thread-A')
# t2 = threading.Thread(target= process_thread, args=('老王',), name='Thread-B')
# t1.start()
# t2.start()

print("------------------14-异步-----------------")
# from multiprocessing import Pool
# import time
# import os
#
# def test():
#     print("---进程池中的进程---pid=%d,ppid=%d--"%(os.getpid(),os.getppid()))
#     for i in range(3):
#         print("----%d---"%i)
#         time.sleep(1)
#     return "hahah"
#
# def test2(args):
#     print("---callback func--pid=%d"%os.getpid())
#     print("---callback func--args=%s"%args)
#
# pool = Pool(3)
# pool.apply_async(func=test,callback=test2)
#
# #异步的理解：主进程正在做某件事情，突然　来了一件更需要立刻去做的事情，
# #那么这种，在父进程去做某件事情的时候　并不知道是什么时候去做，的模式　就称为异步
# while True:
#     time.sleep(1)
#     print("----主进程-pid=%d----"%os.getpid())


print("------------------15-GIL全局解释器锁-----------------")
#GIL实际上,是保证一个时刻只有一个线程在cpu中执行,python中的多线程其实是假的

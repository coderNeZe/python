#coding=utf-8

print("---------------------基本使用-------------------------")
from pymysql import *
# try:
#     conn = connect(host='localhost',port='3306',user='root',passwd='mysql',db='python3',charset='utf8')
#
#     cursorl = conn.cursor()
#     sql = "insert into students(name) values('锅小二') "
#     cursorl.execute(sql)
#     conn.commit()
#
#     cursorl.close()
#     conn.close()
# except Exception as e:
#     print(e.message)

print("---------------------参数化-------------------------")
try:
    name = input("请输入用户名:")
    conn = connect(host='localhost',port='3306',user='root',passwd='mysql',db='python3',charset='utf8')

    cursorl = conn.cursor()
    sql = "insert into students(name) values(%s)"
    cursorl.execute(sql,[name])
    conn.commit()

    cursorl.close()
    conn.close()
except Exception as e:
    print(e.message)

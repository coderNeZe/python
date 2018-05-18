#coding = utf-8

from mysqlHelper import MysqlHelper


#修改
name = input("请输入学生姓名:")
id1 = input("请输入学生编号")

sql = 'update student set name = %s where id = %s'
params = [name,id]

sqlhelper = MysqlHelper('localhost',3306,'python3','root','mysql')
sqlhelper.cud(sql,params)

#查询
sql = 'select id,name from students where id < 5'
sqlhelper = MysqlHelper('localhost',3306,'python3','root','mysql')
result = sqlhelper.all(sql)
print(result)

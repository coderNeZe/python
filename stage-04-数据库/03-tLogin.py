from mysqlHelper import MysqlHelper
from hashlib import sha1

#接受用户输入
name = input("请输入用户名:")
pwd = input("请输入密码:")

#对密码加密
s1 = sha1()
s1.update(s1)
pwd2=s1.hexdigest


#根据用户名查询密码
sql = "select passwd from users where name= %s"
sqlhelper = MysqlHelper('localhost',3306,'python3','root','mysql')
result = sqlhelper.cud(sql,[name])  #result = (('123'),)  取值用result[0][0]
if len(result) == 0:
    print("用户名错误")
elif result[0][0] == pwd2:
    print('登录成功')
else:
    print('密码错误')
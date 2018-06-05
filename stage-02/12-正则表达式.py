import re
'''
.                   匹配任意一个字符 除了\n
[]                  匹配[]中列举的字符
\d==[0-9]           匹配数字,即0-9
\D==[^0-9]          匹配非数字,即不是数字
\s                  匹配空白,即 空格 tab
\S                  匹配非空白
\w==[a-zA-Z0-9_]    匹配单词字符 即a-z,A-Z,0-9,_
\W==[^a-zA-Z0-9_]   匹配非单词字符


*       匹配前一个字符出现0次或者无限次,即可有可无  abc* ab abcccccc
+       匹配前一个字符出现1次或者无限次,即至少有一次  abc+ abc abccc
?       匹配前一个字符出现1次或者0次，即要么有1次，要么没有  abc?  ab abc
{m}     匹配前一个字符出现m次  ab{2}c abbc
{m,}    匹配前一个字符至少出现m次
{m,n}   匹配前一个字符出现从m到n次  ab{1,2}c   abc abbc

^  匹配字符串开头 ^abc abc
$  匹配字符串结尾 abc$ abc
\b 匹配一个单词的边界
\B 匹配非单词边界

'''

print("------------------------匹配手机号---------------------")
'''
手机号规则:
第一位必须是1
第二位必须是345678
^ 是取反[^345678] 意思是只要不是345678都可以
[a-z5-9]  所有a-z的字母和5到9的数字
'''
pattern = re.compile(r"^1[345678]\d{9}$")
m = pattern.match("13011111111")
print(m)


#提取http://www.baidu.com/
s = "http://www.baidu.com/message.asp?id=35"
print(re.sub(r"(http://.+?/).*", lambda x: x.group(1), s))
#或者
pattern = re.compile(r"(http://.+?/).*")
m = pattern.match(s).group(1)
print(m)

#匹配0-100之间的数字
re.compile(r"[1-9]?\d?|100$")

#贪婪的问题
str = '<div><p>岗位职责：</p><p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p></div>'
pattern = re.compile(r'</?.+?>')
m = pattern.sub("",str)
print("贪婪=====",m)

# #提取单词
# ss = "hello world ha ha"
# #方式1:
# print(re.split(r" +", ss))
# #方式2:
# print(re.findall(r"\b[a-zA_Z]+\b", ss))
#
# '''

# <h1>匹配分组</h1>
# <h1>(.*)</h1>

# <html><h1>匹配分组</h1></html>
#<(.+)><(.+)>.+</\2></\1>  对前边的内容进行了分组 后边直接\num就可以

# <html><h1>匹配分组</h1></html>
#<(?p<key1>.+)><(?p<key2>.+)>.+</(?p=key2)></(?p=key1)>  ?p<key1>分组起别名


# #匹配出，一个字符串第一个字母为大小字符，后面都是小写字母并且这些小写字母可有可无 *
# import re
# reg = r"^([A-Z][a-z]*)"
# ret = re.match(reg,"GoFd").group(1)
# print("sssss",ret)
#
# #匹配出，0到99之间的数字 ?
# import re
# reg = r"[1-9]?[0-9]"
# ret = re.match(reg,"99")
# print("sssss",ret)
#
# #匹配出，8到20位的密码，可以是大小写英文字母、数字、下划线
# import re
# reg = r"[A-Za-z0-9_]{8,20}"
# ret = re.match(reg,"99")
# print("sssss",ret)
#
#
# #匹配出163的邮箱地址，且@符号之前有4到20位，例如hello@163.com
# import re
# reg = r"[A-Za-z0-9]{4,20}@163.com"
# ret = re.match(reg,"hello@163.com")
# print("sssss",ret)

# #匹配163.com的邮箱地址
# import re
# reg = r"[\w]{4,20}@163\.com$"
# ret = re.match(reg,"xiaowang@163.com")
# print("sssss",ret)
#
# ret = re.match(r".*\bver\b","ho ver abc").group()
# print(ret)
# ret = re.match(r"(.*\b)ver\b","ho verabc")
# print(ret)



# pattern.match():#从起始位置开始查找,返回第一个符合规则的,只匹配一次
# pattern.search():     #从任何位置开始往后查找,返回第一个符合规则的,只匹配一次
# pattern.findall():    #所有的全部匹配,返回列表
# pattern.finditer():   #所有的全部匹配,返回的是一个迭代器 (很少用)
# pattern.split():      #分割字符串,返回列表
# pattern.sub():        #替换

#============================match============================
pattern = re.compile(r"\d+") #至少匹配一个数字
m = pattern.match("aaa123bbb456",3,5).group()
print("match===",m) #从起始位置开始查找,返回第一个符合规则的,只匹配一次,从3的位置开始 5的位置结束

pattern = re.compile(r"([a-z]+) ([a-z]+)",re.I)  #re.I 忽略大小写,re.S 全文匹配
m = pattern.match("Hello world hello Python").group(0)
print("match===",m)

#============================search============================
pattern = re.compile(r"\d+")
m = pattern.search("aa123bbb456")
print("search=====",m.group())
m = pattern.search('hello 123456 789')
print("search=====",m.group())

#============================findall============================
m = pattern.findall("hello 123456 789")
print("findall===",m)

m = pattern.findall("aaa123bbb456")
print("findall===",m)

m = pattern.finditer("aaa123bbb456")
for i in m:
    print("finditer===",i.group())

#============================split============================
pattern = re.compile(r"[\s\d\\;]+")
m = pattern.split(r"a bb\h2a;mm;  3   a")
print("split====",m)

#============================sub============================
pattern = re.compile(r"(\w+) (\w+)")
str = "hello 123,hello 456"
m = pattern.sub("hello world",str)
print("sub====",m)

m = pattern.sub(r"\2 \1",str)
print("sub====",m)

pattern = re.compile(r"\d+")
str = "abc123abc456"
m = pattern.sub("mmm",str)
print("sub====",m)

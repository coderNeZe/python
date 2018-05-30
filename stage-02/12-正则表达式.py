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

'''
result = re.match("wfh","wfhhhhhhhh")

print(result)

'''
手机号规则:
第一位必须是1
第二位必须是345678
^ 是取反[^345678] 意思是只要不是345678都可以
[a-z5-9]  所有a-z的字母和5到9的数字

'''
#手机号的正则
#"1[345678]\d{9}$"

#提取http://www.baidu.com/
s = "http://www.baidu.com/message.asp?id=35"
print(re.sub(r"(http://.+?/).*", lambda x: x.group(1), s))


#提取单词
ss = "hello world ha ha"
#方式1:
print(re.split(r" +", ss))
#方式2:
print(re.findall(r"\b[a-zA_Z]+\b", ss))

'''
* 匹配前一个字符出现0次或者无限次,即可有可无
s*   s 或者 sssssss....

+ 匹配前一个字符出现1次或者无限次,即至少有一次
s+  ss或者sssss.....
? 匹配前一个字符出现1次或者0次，即要么有1次，要么没有

{m} 匹配前一个字符出现m次
{m,}匹配前一个字符至少出现m次
{m,n}匹配前一个字符出现从m到n次
'''
#匹配出，一个字符串第一个字母为大小字符，后面都是小写字母并且这些小写字母可有可无 *
import re
reg = r"^([A-Z][a-z]*)"
ret = re.match(reg,"GoFd").group(1)
print("sssss",ret)

#匹配出，0到99之间的数字 ?
import re
reg = r"[1-9]?[0-9]"
ret = re.match(reg,"99")
print("sssss",ret)

#匹配出，8到20位的密码，可以是大小写英文字母、数字、下划线
import re
reg = r"[A-Za-z0-9_]{8,20}"
ret = re.match(reg,"99")
print("sssss",ret)


#匹配出163的邮箱地址，且@符号之前有4到20位，例如hello@163.com
import re
reg = r"[A-Za-z0-9]{4,20}@163.com"
ret = re.match(reg,"hello@163.com")
print("sssss",ret)

'''
^ 匹配字符串开头
$ 匹配字符串结尾
\b 匹配一个单词的边界
\B 匹配非单词边界
'''

#匹配163.com的邮箱地址
import re
reg = r"[\w]{4,20}@163\.com$"
ret = re.match(reg,"xiaowang@163.com")
print("sssss",ret)

ret = re.match(r".*\bver\b","ho ver abc").group()
print(ret)
ret = re.match(r"(.*\b)ver\b","ho verabc")
print(ret)

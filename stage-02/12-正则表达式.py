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
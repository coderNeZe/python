print("---------------不使用urlopen,使用自定义的去请求---------------")
# from urllib import request
#
# #构建一个HTTPHandle处理器对象,支持处理HTTP的请求
# # http_handler = request.HTTPHandler()
#
# #HTTPHandler可以加参数, debuglevel=1将会自动打开Debug log模式
# #程序在执行的时候会打印收发包的信息 一般调试用
# http_handler = request.HTTPHandler(debuglevel=1)
#
# #调用build_opener()方法构建一个自定义的opener对象,参数是构建的处理器对象
# opener = request.build_opener(http_handler)
#
# req = request.Request("http://www.baidu.com")
# res = opener.open(req)
# print(res.read())

print("---------------利用ProxyHandle,伪装ip---------------")
# from urllib import request
# #代理开关,是否启用代理
# proxyswitch = True
#
# #构建一个Handle处理器对象,参数是一个字典类型,包括代理类型和代理服务器IP+port
# httpproxy_handle = request.ProxyHandler({"http": "60.247.121.230:3128"})
# #构建一个没有代理的处理器对象
# nullproxy_handle = request.ProxyHandler({})
#
# if proxyswitch:
#     opener = request.build_opener(httpproxy_handle)
# else:
#     opener = request.build_opener(nullproxy_handle)
#
# #两种请求方式:方式1
# #构建一个全局的opener,之后所有的请求都可以用urlopen()方式去发送,也附带handle功能
# # request.install_opener(opener)
# # req = request.Request("http://www.baidu.com")
# # res = request.urlopen(req)
# # print(res.read())
#
# #方式2:
# #不使用全局构建的方法
# req = request.Request("http://www.baidu.com")
# res = opener.open(req)
# print(res.read())
#
# #如果使用私密的代理方式,需要账号密码 具体格式如下"账号:密码@ip:port"
# # httpproxy_handle = request.ProxyHandler({"http": "zhanghao:mima@60.247.121.230:3128"})

print("---------------代理和web客户端授权验证处理器的使用---------------")
# from urllib import request
#
# test = "test"
# password = "123456"
# webserver = "192.168.21.52"
#
# # 构建一个密码管理对象，可以用来保存和HTTP请求相关的授权账户信息
# passwordMgr = request.HTTPPasswordMgrWithDefaultRealm()
#
# # 添加授权账户信息，第一个参数realm如果没有指定就写None，后三个分别是站点IP，账户和密码
# passwordMgr.add_password(None, webserver, test, password)
#
# # HTTPBasicAuthHandler() HTTP基础验证处理器类
# httpauth_handler = request.HTTPBasicAuthHandler(passwordMgr)
#
# # 处理代理基础验证相关的处理器类 (如果是使用代理ip的账号密码,也可以用这个方法)
# #proxyauth_handler = urllib2.ProxyBasicAuthHandler(passwordMgr)
#
# # 构建自定义opener
# opener = request.build_opener(httpauth_handler)
#
# request = request.Request("http://192.168.21.52/")
#
# # 用授权验证信息
# response = opener.open(request)
#
# print(response.read())

print("---------------通过Cookielib和HTTPCookieProcess模拟登录---------------")
# from urllib import request,parse
# import http.cookiejar
#
# # 通过CookieJar()类构建一个cookieJar()对象，用来保存cookie的值
# cookie = http.cookiejar.CookieJar()
#
# # 通过HTTPCookieProcessor()处理器类构建一个处理器对象，用来处理cookie
# # 参数就是构建的CookieJar()对象
# cookie_handler = request.HTTPCookieProcessor(cookie)
#
# # 构建一个自定义的opener
# opener = request.build_opener(cookie_handler)
#
# # 通过自定义opener的addheaders的参数，可以添加HTTP报头参数
# opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36")]
#
# # renren网的登录接口
# url = "http://www.renren.com/PLogin.do"
#
# # 需要登录的账户密码
# data = {"email":"mr_mao_hacker@163.com", "password":"alarmchime"}
#
# # 通过urlencode()编码转换
# data = parse.urlencode(data)
#
# # 第一次是post请求，发送登录需要的参数，获取cookie
# request = request.Request(url, data = data)
#
# # 发送第一次的post请求，生成登录后的cookie(如果登录成功的话)
# response = opener.open(request)
#
# # print (response.read())
#
# # 第二次可以是get请求，这个请求将保存生成cookie一并发到web服务器，服务器会验证cookie通过
# response_deng = opener.open("http://www.renren.com/410043129/profile") #这个网址是必须登录后才能看到的
#
# # 获取登录后才能访问的页面信息
# print(response_deng.read())


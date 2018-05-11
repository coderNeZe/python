print("----------------------urllib获取网页数据-------------------------")
# from urllib import request
#
# ua_headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
# }
#
# # 通过urllib.Request() 方法构造一个请求对象
# req = request.Request("http://www.sina.com/",headers=ua_headers)
#
# # 向指定的url地址发送请求，并返回服务器响应的类文件对象
# response = request.urlopen(req)
#
# # 服务器返回的类文件对象支持Python文件对象的操作方法
# # read()方法就是读取文件里的全部内容，返回字符串
# html = response.read()
#
# # 返回 HTTP的响应码，成功返回200，4服务器页面出错，5服务器问题
# print(response.getcode())
#
# # 返回 返回实际数据的实际URL，防止重定向问题
# print(response.geturl())
#
# # 返回 服务器响应的HTTP报头
# print (response.info())
#
# # 打印响应内容
# print (response)

print("----------------------随机选择User-Agent-------------------------")
# from urllib import request
# import random
#
# url = "http://www.baidu.com/"
#
# # 可以是User-Agent列表，也可以是代理列表
# ua_list = [
#         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
#         "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
#         "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
#         "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
#         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
# ]
#
# # 在User-Agent列表里随机选择一个User-Agent
# user_agent = random.choice(ua_list)
#
# # 构造一个请求
# request = request.Request(url)
#
# # add_header()方法 添加/修改 一个HTTP报头
# request.add_header("User-Agent", user_agent)
#
# # get_header() 获取一个已有的HTTP报头的值，注意只能是第一个字母大写，其他的必须小写
# print(request.get_header("User-agent"))

print("----------------------urlencode-------------------------")
# from urllib import request,parse
#
# url = "http://www.baidu.com/s"
# keyword = input("请输入需要查询的字符串:")
# wd = {"wd":keyword}
# wd = parse.urlencode(wd)  #通过urlencode参数转换成=号形式
# fullurl = url + "?" + wd
# print(fullurl)
# req = request.Request(fullurl)
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# res = request.urlopen(req)
# print(res.read())


print("----------------------urllib2_post-------------------------")
# from urllib import request,parse
# #通过抓包的方式获取的url,并不是浏览器显示的url
# url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
# # 完整的headers
# headers = {
#         "Accept" : "application/json, text/javascript, */*; q=0.01",
#         "X-Requested-With" : "XMLHttpRequest",
#         "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
#         "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
#     }
#
# # 用户接口输入
# key = input("请输入需要翻译的文字:")
#
# # 发送到web服务器的表单数据
# formdata = {
# "type" : "AUTO",
# "i" : key,
# "doctype" : "json",
# "xmlVersion" : "1.8",
# "from" : "fanyi.web",
# "ue" : "UTF-8",
# "version":"2.1",
# "action" : "FY_BY_REALTIME",
# "typoResult" : "false"
# }
#
# # 经过urlencode转码
# data = parse.urlencode(formdata)
#
# # 如果Request()方法里的data参数有值，那么这个请求就是POST
# # 如果没有，就是Get
# req = request.Request(url, data = data, headers = headers)
#
# print(request.urlopen(req).read())

print("----------------------小案例-------------------------")
# from urllib import request,parse
#
# def loadPage(url, filename):
#     """
#         作用：根据url发送请求，获取服务器响应文件
#         url: 需要爬取的url地址
#         filename : 处理的文件名
#     """
#     print("正在下载 " + filename)
#     headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
#
#     req = request.Request(url, headers = headers)
#     return request.urlopen(req).read()
#
# def writePage(html, filename):
#     """
#         作用：将html内容写入到本地
#         html：服务器相应文件内容
#     """
#     print("正在保存 " + filename)
#     # 文件写入
#     with open(filename, "wb") as f:
#         f.write(html)
#     print("-" * 30)
#
# def tiebaSpider(url, beginPage, endPage):
#     """
#         作用：贴吧爬虫调度器，负责组合处理每个页面的url
#         url : 贴吧url的前部分
#         beginPage : 起始页
#         endPage : 结束页
#     """
#     for page in range(beginPage, endPage + 1):
#         pn = (page - 1) * 50
#         filename = "第" + str(page) + "页.html"
#         fullurl = url + "&pn=" + str(pn)
#         #print fullurl
#         html = loadPage(fullurl, filename)
#         #print html
#         writePage(html, filename)
#         print("谢谢使用")
#
# if __name__ == "__main__":
#     kw = input("请输入需要爬取的贴吧名:")
#     beginPage = int(input("请输入起始页："))
#     endPage = int(input("请输入结束页："))
#
#     url = "http://tieba.baidu.com/f?"
#     key = parse.urlencode({"kw": kw})
#     fullurl = url + key
#     tiebaSpider(fullurl, beginPage, endPage)

print("----------------------Ajax加载方式的数据获取-------------------------")
# from urllib import request,parse
#
# url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action"
#
# headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
#
# formdata = {
#         "start":"0",
#         "limit":"20"
#     }
#
# data = parse.urlencode(formdata)
#
# req = request.Request(url, data = data, headers = headers)
#
# print(request.urlopen(req).read())


print("----------------------忽略https的证书认证-------------------------")
# import ssl
# context = ssl._create_unverified_context() #忽略https中ssl的认证
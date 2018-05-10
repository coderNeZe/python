from urllib import request,parse

ua_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
}

url = "http://pm25.in/"
print("ssss")
req = request.Request(url,headers=ua_headers)
html = request.urlopen(req).read()
print(html)
with open("data.html", "wb") as f:
    f.write(html)

print("完成")
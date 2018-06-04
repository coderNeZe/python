'''
第4期作业：用python实现一个ui页面，如下图。页面中有一个输入框，实现输入城市名称（全拼或者汉字）点击搜索，展示这个城市7天之内的天气情况。
包括天气、温度、风向 、污染指数、限号等。在展示列表的最下方可输入邮箱地址 点击发送按钮可将上面获取到的城市天气信息发送到邮箱中。
Tips： 1、邮箱地址需要验证 2、做好输入内容异常的处理 3、参考网站：http://www.weather.com.cn/  （注：要温柔，别玩坏了）

例子：
城市：北京  日期：05.20 天气状况：多云 温度：21度  风向：西南风三到四级  污染指数：217  限号：7
城市：北京  日期：05.21 天气状况：阴了 温度：11度  风向：东南风三到四级  污染指数：247  限号：9
城市：北京  日期：05.22 天气状况：阳了 温度：31度  风向：东南风三到四级  污染指数：217  限号：4

'''
import tkinter as tk
import requests

window = tk.Tk()
window.title('my window')
window.geometry('300x300')

entry = tk.Entry(window,text='input your text here')
entry.place(x=20,y=20,anchor='nw')

def chekWeather():
    url = "http://www.weather.com.cn/"
    try:
        headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
        r = requests.get(url,headers = headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text[1000])
    except:
        print("信息爬取失败")

b1 = tk.Button(window, text='查询', width=3,height=2, command=chekWeather)
b1.place(x=220,y=12,anchor='nw')

window.mainloop()
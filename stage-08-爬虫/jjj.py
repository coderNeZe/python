# -*- coding:utf-8 -*-
from urllib import request,parse
from lxml import html
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

flag = True

class Spider:
    def __init__(self):
        self.pandan_data = pd.DataFrame()
        self.index = 0

    def startLoadData(self):
        """
        作用: 或者资源的方法
        """
        print("准备请求....")
        if flag:
            url = "file:///Users/Ne/Desktop/data.html"
        else:
            url = "http://pm25.in/"
        content = self.requestFun(url)
        link_list = content.xpath('///div[@class="all"]/div[@class="bottom"]//@href')
        for link in link_list:
            if flag:
                sub_url = "file:///Users/Ne/Desktop/subdata.html"
            else:
                sub_url = "http://pm25.in/" + link
            subcontent = self.requestFun(sub_url)
            city_name = subcontent.xpath('///div[@class="city_name"]/h2/text()')[0]
            header_info = subcontent.xpath('//div[@class="span12 data"]//div[@class="caption"]/text()')
            data_info = subcontent.xpath('//div[@class="span12 data"]//div[@class="value"]/text()')
            header_list = self.__disposeList(header_info)
            data_list = self.__disposeList(data_info)
            header_list.insert(0,"city")
            data_list.insert(0,city_name)
            self.__handleData(header_list,data_list)

    def __handleData(self,head_list,data_list):
        self.index += 1
        if self.index > 50:
            self.writePage(self.pandan_data, "cityAQI.scv")
            self.pandan_data.drop
            self.index = 0
            self.pandan_data = pd.DataFrame(np.array(data_list).reshape((1, 9)), columns=head_list)
        else:
            if self.pandan_data.empty:
                self.pandan_data = pd.DataFrame(np.array(data_list).reshape((1,9)), columns=head_list)
            else:
                temp_data = pd.DataFrame(np.array(data_list).reshape((1,9)), columns=head_list)
                self.pandan_data = self.pandan_data.append(temp_data,ignore_index=True)



    def __draw_picture(self):
        n = 50
        x = np.arange(n)
        y = 100
        plt.bar(x,y,width=5,facecolor="#9999ff",edgecolor="white")
        plt.xlim(0, 50)
        y_pos = np.arange(len("people"))
        plt.xticks(y_pos, "people")
        plt.title('城市AQI排行表')
        plt.show()


    def __disposeList(self,list):
        temp_list = []
        for info in list:
            data = info.replace('\n', '').replace(' ', '')
            if data != "":
                temp_list.append(data)
        return temp_list

    def requestFun(self,url):
        """
        负责请求数据
        :param url: 请求网址的url
        :return: 转换成xml后的数据格式
        """
        print("请求中.....")
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
        httpproxy_handle = request.ProxyHandler({"https":"101.37.79.125:3128"})
        opener = request.build_opener(httpproxy_handle)
        req = request.Request(url, headers=headers)
        ht = opener.open(req).read()
        ht = ht.decode("utf-8")
        return html.etree.HTML(ht)

    def writePage(self,item,name):
        """
            把每条数据逐个写入文件里
        """
        # 写入文件内
        print("正在写入数据....")
        with open(name, "a+") as f:
            f.writelines(str(item)+ "\n")
        print("写入完成")

    def startWork(self):
        self.startLoadData()

if __name__ == '__main__':
    s = Spider()
    s.startWork()




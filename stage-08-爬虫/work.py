# -*- coding:utf-8 -*-
from urllib import request,parse
from lxml import html
import pandas as pd
import numpy as np

# import matplotlib.pyplot as plt






class Spider:
    def __init__(self):
        pass

    def startLoadData(self):
        """
        作用: 或者资源的方法
        """
        print("准备请求....")
        url = "http://pm25.in/"#"file:///Users/Ne/Desktop/data.html" #
        content = self.requestFun(url)
        link_list = content.xpath('///div[@class="all"]/div[@class="bottom"]//@href')
        for link in link_list:
            sub_url = "http://pm25.in/"+link #"file:///Users/Ne/Desktop/subdata.html"#"http://pm25.in/" + link#"
            subcontent = self.requestFun(sub_url)
            city_name = subcontent.xpath('///div[@class="city_name"]/h2/text()')[0]
            # content_info = subcontent.xpath('//div[@class="span12 data"]/div[@class="span1"]//text()')
            header_info = subcontent.xpath('//div[@class="span12 data"]//div[@class="caption"]/text()')
            number_info = subcontent.xpath('//div[@class="span12 data"]//div[@class="value"]/text()')
            header = self.__disposeList(header_info)
            number = self.__disposeList(number_info)
            pd.DataFrame()
            # city_dic = map(self.__listTodic,header,number)
            # city_list_info = list(city_dic)
            # city_list_info.insert(0,{"city":city_name})
            # self.writePage(city_list_info,"city.scv")

    def sortList(self,x):
        print(x)
        return x[1]["AQI"]

    def __disposeList(self,list):
        temp_list = []
        for info in list:
            data = info.replace('\n', '').replace(' ', '')
            if data != "":
                temp_list.append(data)
        return temp_list

    def __listTodic(self,x,y):
        return {x:y}

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
            把每条段子逐个写入文件里
            item: 处理后的每条段子
        """
        # 写入文件内
        print("正在写入数据....")
        with open(name, "a+") as f:
            f.writelines(str(item )+ "\n")
        print("写入完成")

    def sortData(self):
        with open("city.scv","r+") as f:
            list = f.readlines()

        print(list)
        # result = sorted(list, key=lambda x:x[1])
        # self.writePage(result,"sort.scv")


    def startWork(self):
        self.startLoadData()

if __name__ == '__main__':
    s = Spider()
    s.startWork()
    # s.sortData()






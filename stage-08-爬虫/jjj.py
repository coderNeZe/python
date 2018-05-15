# -*- coding:utf-8 -*-
from urllib import request,parse
from lxml import html
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontManager, FontProperties
import pandas as pd
import csv

flag = True
analyze_data = 50
cityAQI_name= "cityAQI_name"


class Spider:
    def __init__(self):
        self.update_time = ""
        self.header_list = []

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

    def __disposeList(self, list):
        temp_list = []
        for info in list:
            data = info.replace('\n', '').replace(' ', '')
            if data != "":
                temp_list.append(data)
        return temp_list

    def startLoadData(self):
        """
        作用: 获取资源的方法
        """
        print("准备请求....")
        if flag:
            url = "file:///Users/Ne/python/stage-08-爬虫/data.html"
        else:
            url = "http://pm25.in/"
        content = self.requestFun(url)
        link_list = content.xpath('///div[@class="all"]/div[@class="bottom"]//@href')
        total_list = []
        for link in link_list:
            if flag:
                sub_url = "file:///Users/Ne/python/stage-08-爬虫/subdata.html"
            else:
                sub_url = "http://pm25.in/" + link
            subcontent = self.requestFun(sub_url)
            if len(self.update_time) == 0:
                #处理更新时间和标题
                self.update_time = subcontent.xpath('//div[@class="live_data_time"]/p/text()')[0]
                header_info = subcontent.xpath('//div[@class="span12 data"]//div[@class="caption"]/text()')
                self.header_list = self.__disposeList(header_info)
                self.header_list.insert(0, "city")

            #获取城市的名字
            city_name = subcontent.xpath('//div[@class="city_name"]/h2/text()')[0]
            #获取每个城市的数据
            data_info = subcontent.xpath('//div[@class="span12 data"]//div[@class="value"]/text()')
            data_list = self.__disposeList(data_info)
            data_list.insert(0,city_name)

            total_list.append(data_list)
        self.__handleData(total_list)

    def __handleData(self,total_list):
        total_list.sort(key=lambda x:int(x[1]))
        total_list.insert(0, self.header_list)
        for info in total_list:
            self.writeCityAQIinfo(info,cityAQI_name)

    def writeCityAQIinfo(self,item,file_name):
        """
            把每条数据逐个写入文件里
        """
        # 写入文件内
        print("正在写入数据....")
        with open(file_name, "a+", encoding="utf-8", newline='') as f:
            writer_tool =  csv.writer(f)
            writer_tool.writerow (item)
        print("写入完成")

    def draw_picture(self,filepath):
        pandas_data = pd.read_csv("cityAQI.csv").head(100)
        print(pandas_data)
        # filter_data = pandas_data["AQI"]
        # print(filter_data)
        # top50_data = pandas_data.head(analyze_data+1)
        # print(top50_data)

        # y_list = []
        # city_list = []
        # for list in new_list:
        #     if int(list[1]) == 0:
        #         continue
        #     y_list.append(int(list[1]))
        #     city_list.append(list[0])
        #     if int(len(city_list)) == analyze_data:
        #         break
        #
        # x = np.arange(analyze_data)
        #
        # plt.bar(x, y_list)
        #
        # plt.xticks(np.arange(int(len(city_list))),city_list,rotation=270,fontproperties=self.__getChineseFont(),fontsize=8)
        # plt.ylim(0,max(y_list)+5)
        #
        # plt.title('空气质量最好的50个城市({0})'.format(self.update_time),fontproperties=self.__getChineseFont())
        #
        # l1, = plt.plot(1,0,label='AQI',color='#9999ff',linewidth=5.0)
        # plt.legend(handles=[l1,],loc='best')
        #
        # plt.show()



        # plt.bar(x, y_list,color='rgb')
        #
        # plt.xticks(np.arange(int(len(city_list))),city_list,rotation=270,fontproperties=self.__getChineseFont(),fontsize=8)
        # plt.ylim(0,max(y_list)+5)
        #
        # plt.title('空气质量最好的50个城市({0})'.format(self.update_time),fontproperties=self.__getChineseFont())
        #
        # l1, = plt.plot(1,0,label='AQI',color='#9999ff',linewidth=5.0)
        # plt.legend(handles=[l1,],loc='best')
        #
        # plt.show()
    # def get_list_info(self,index,list):
    #     return list[index]

    @staticmethod
    def __getChineseFont():
        return FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

if __name__ == '__main__':
    s = Spider()
    s.startLoadData()
    s.draw_picture()


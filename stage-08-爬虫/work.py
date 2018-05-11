# -*- coding:utf-8 -*-
from urllib import request,parse
from lxml import html
# import matplotlib.pyplot as plt
# from numbers import
# from numpy.random import rand

class Spider:
    def __init__(self):
        pass

    def startLoadData(self):
        """
        作用: 或者资源的方法
        """
        # url = "file:///Users/Ne/Desktop/data.html"#"http://pm25.in/"
        print("准备请求....")
        url =  "http://pm25.in/"
        content = self.requestFun(url)
        link_list = content.xpath('///div[@class="all"]/div[@class="bottom"]//@href')
        for link in link_list:
            sub_url = "http://pm25.in/" + link
            # sub_url = "file:///Users/Ne/Desktop/subdata.html"
            subcontent = self.requestFun(sub_url)
            city_name = subcontent.xpath('///div[@class="city_name"]/h2/text()')[0]
            # header_info = subcontent.xpath('//div[@class="span12 data"]//div[@class="caption"]/text()')
            # header_info = subcontent.xpath('//div[@class="span12 data"]/div[@class="span1"]//text()')
            # print(header_info)
            # data_info = subcontent.xpath('//div[@class="span12 data"]//div[@class="value"]/text()')
            city_name = subcontent.xpath('///div[@class="city_name"]/h2/text()')[0]
            header_info = subcontent.xpath('//div[@class="span12 data"]/div[@class="span1"]//text()')
            heads = []
            for info in header_info:
                data = info.replace('\n', '').replace(' ', '')
                if data != "":
                    heads.append(data)

            heads.append(city_name)
            self.writePage(heads)

    def requestFun(self,url):
        """
        负责请求数据
        :param url: 请求网址的url
        :return: 转换成xml后的数据格式
        """
        print("请求中.....")
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
        httpproxy_handle = request.ProxyHandler({})
        opener = request.build_opener(httpproxy_handle)
        req = request.Request(url, headers=headers)
        ht = opener.open(req).read()
        ht = ht.decode("utf-8")
        return html.etree.HTML(ht)

    def writePage(self, item):
        """
            把每条段子逐个写入文件里
            item: 处理后的每条段子
        """
        # 写入文件内
        print("正在写入数据....")
        with open("city.txt", "a+") as f:
            f.writelines(str(item )+ "\n")

    def startWork(self):
        self.startLoadData()

if __name__ == '__main__':
    s = Spider()
    s.startWork()





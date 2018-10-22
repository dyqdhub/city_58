# -*- coding: utf-8 -*-
import scrapy


class TaobaoPySpider(scrapy.Spider):
    name = 'taobao_py'      #爬虫名称
    allowed_domains = ['taobao.com']    #爬虫爬去的主域名
    start_urls = ['http://www.llduang.com']
    def parse(self, response):
        html = response.body  # response是获取到的来自网站的返回
        # 以下四行将html存入文件
        filename = "index.html"
        file = open(filename, "wb")
        file.write(html)
        file.close()

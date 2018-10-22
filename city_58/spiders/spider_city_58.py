# -*- coding: utf-8 -*-
import scrapy


class SpiderCity58Spider(scrapy.Spider):
    name = 'spider_city_58'
    allowed_domains = ['58.com']
    start_urls = ['https://bj.58.com/']

    def parse(self, response):
        print("进入爬虫")
        print(response.url)
        print(response.body)
        pass

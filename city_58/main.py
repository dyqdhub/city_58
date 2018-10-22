#!/bin/python
# -*- coding: utf-8 -*-
#main.py 文件一般作为项目的入口

from scrapy import cmdline

cmdline.execute("scrapy crawl taobao_py".split())
# cmdline.execute("scrapy crawl spider_city_58".split())
#.split()方法，使用的是列表传参的方法，如果直接传入执行命令，由于不同系统的命令执行方法不同，可能会报错。使用列表传参的方法则避免报错
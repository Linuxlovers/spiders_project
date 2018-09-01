#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/1 0001 09:46
# @Author  : BigC
# @Site    : 
# @File    : crawlers_main.py
# @Software: PyCharm
# coding:utf8
from com.crawlers import download_manager
from com.crawlers import output_manager
from com.crawlers import parser_manager
from com.crawlers import url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = download_manager.DownloadManager()
        self.parser = parser_manager.ParserManager()
        self.output = output_manager.OutputManager()

    def craw(self, root_url):
        html_root = self.downloader.download(root_url)
        new_urls = self.parser.parseUrls(root_url,html_root)
        self.urls.add_new_urls(new_urls)
        count = 1
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (count, new_url))
                html_cont = self.downloader.download(new_url)
                new_data = self.parser.parse(new_url, html_cont)
                self.output.collect_data(new_data)
                if count == 1000:
                    break
                count += 1
            except:
                print('craw failed')

        self.output.output_html()


if __name__ == "__main__":
    root_url = "http://www.cnblogs.com/haiyan123/"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)

crawlers_main.py
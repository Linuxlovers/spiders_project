#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/1 0001 09:48
# @Author  : BigC
# @Site    : 
# @File    : download_manager.py
# @Software: PyCharm
# coding:utf8
import urllib2


class DownloadManager(object):

    def download(self, url):
        if url is None:
            return None
        response = urllib2.urlopen(url)
        if response.code != 200:
            return None
        return response.read()

download_main.py
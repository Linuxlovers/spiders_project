#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/12 0012 19:40
# @Author  : BWM
# @Site    :
# @File    : lianjia.py
# @Software: PyCharm
import re
from urllib.request import urlopen
import json
import ssl
#干掉SSL加密认证
ssl._create_default_https_context = ssl._create_unverified_context

def GetPage(url):
    return urlopen(url).read().decode("utf-8")
def Deal_Html(html):
    cont=re.compile(r'class="info clear"><div class="title">.*?data-sl="">(?P<title>.*?)'
                    r'</a>.*?data-el="region">(?P<address>.*?)</a>'
                    r'<span.*?</span>(?P<huxing>.*?)<span'
                    r'.*?</span>(?P<aera>.*?)<span'
                    r'.*?</span>(?P<chaoxiang>.*?)<span'
                    r'.*?</span>(?P<zhuangxiu>.*?)<'
                    r'(?:span class="divide">/</span>(?P<dianti>.*?)</div></div><div class="flood">)?'
                    r'.*?class="positionInfo">(?P<loucen>.*?)<span'
                    r'.*?</span>(?P<jianloushijian>.*?)<span'
                    r'.*?target="_blank">(?P<biaoqian>.*?)</a>'
                    r'.*?"followInfo">(?P<guanzhu>.*?)<span'
                    # r'.*?</span>(?P<daikan>.*?)<div'
                    r'.*?</span>(?P<daikan>.*?)<div class="tag">'
                    # r'.*?(?:class=".*?">(?P<fangben>.*?)</span>)?'
                    # r'.*?(?:<span class="taxfree">(?P<fangben>.*?)</span>)?'
                    r'(?:<span class=".*?">(?P<fangben>.*?)</span>)?'
                    r'(?:<span class="haskey">(?P<shijian>.*?)</span>)?'
                    r'</div><div class=.*?><div class=.*?><span>(?P<biaojia>.*?)</span>'
                    r'(?P<danwei>.*?)</div>'
                    r'.*?<div.*?<span>(?P<danjia>.*?)</span>'


                    ,re.S)
    s=cont.finditer(html)
    count=0
    # for el in s:
    #     print("***************************************")
    #     print(el.group("title"))
    #     print(el.group("address"))
    #     print(el.group("huxing"))
    #     print(el.group("aera"))
    #     print(el.group("chaoxiang"))
    #     print(el.group("zhuangxiu"))
    #     print(el.group("dianti"))
    #     print(el.group("loucen"))
    #     print(el.group("jianloushijian"))
    #     print(el.group("biaoqian"))
    #     print(el.group("guanzhu"))
    #     print(el.group("daikan"))
    #     print(el.group("fangben"))
    #     print(el.group("shijian"))
    #     print(el.group("biaojia"))
    #     print(el.group("danwei"))
    #     print(el.group("danjia"))

    for el in s:
       yield{
           "name": el.group("title").strip(),
           "title": el.group("title").strip(),
           "address": el.group("address").strip(),
           "huxing": el.group("huxing").strip(),
           "aera": el.group("aera").strip(),
           "chaoxiang": el.group("chaoxiang").strip(),
           "zhuangxiu": el.group("zhuangxiu").strip(),
           "dianti": el.group("dianti"),
           "loucen": el.group("loucen").strip(),
           "jianloushijian": el.group("jianloushijian").strip(),
           "biaoqian": el.group("biaoqian").strip(),
           "guanzhu": el.group("guanzhu").strip(),
           "daikan": el.group("daikan").strip(),
           "fangben": el.group("fangben"),
           "shijian": el.group("shijian"),
           "biaojia": el.group("biaojia").strip(),
           "danwei": el.group("danwei").strip(),
           "danjia": el.group("danjia").strip(),
       }
    return s,count



def main(url):
    #获取到搜索页面的html
    page=GetPage(url)
    # print(page)
    #匹配想要的内容
    c=Deal_Html(page)
    # print("一共",c[1],"条数据")
    f=open("chaoyang.txt",mode="a",encoding="utf-8")
    for c in c:
        c=json.dumps(c,ensure_ascii=False)+"\n"
        f.write(c)
    f.close()
# url="https://bj.lianjia.com/ershoufang/rs%E6%B2%99%E6%B2%B3/"#第一页

# url="https://bj.lianjia.com/ershoufang/changping/pg2rs%E6%B2%99%E6%B2%B3/"#第二页
di=[]
for i in range(1,101):
    url = ("https://bj.lianjia.com/ershoufang/chaoyang/pg%s/"%i)
    print(url)
    main(url)
# main(url)
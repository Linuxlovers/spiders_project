#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/24 0024 17:06
# @Author  : BigC
# @Site    : 
# @File    : shoppingcar.py
# @Software: PyCharm
product_list=[
    ('mac book',9000),
    ('tesla',900000),
    ('kindle',800),
    ('python book',105),
    ('bike',2000),
]
saving=input("please input your money:")
shoppingcar=[]
if saving.isdigit():
    saving=int(saving)
    while True:
        for i,v in enumerate(product_list,1):
            print(i,">>>>",v)
        choice=input("选择购买商品编号[退出：q]")
        if choice.isdigit():
            choice = int(choice)
            if choice>0 and choice<=len(product_list):
                p_iterm=product_list[choice-1]
                if p_iterm[1]<saving:
                    saving-=p_iterm[1]
                    shoppingcar.append(p_iterm)
                else:
                    print("余额不足，还剩%s块钱"%saving)

                print(p_iterm)
            else:
                print("编码不存在！")

        elif choice=='q':
            print("---------您已经购买以下商品---------")
            for i in shoppingcar:
                print(i)
            print("您还剩%s元钱"%saving)
            break
        else:
            print("invalid input")

        
        

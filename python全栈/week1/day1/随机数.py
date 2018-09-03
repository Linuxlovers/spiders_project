#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 0003 20:58
# @Author  : BigC
# @Site    : 
# @File    : 随机数.py
# @Software: PyCharm
from random import randint
answer=randint(1,10)
guess_num=int(input("请输入猜测数字:"))
if guess_num>answer:
    print("输入小一点的数字")
elif guess_num<answer:
    print("请输入大一点的数字")
else:
    print("猜测正确!")
print(answer)

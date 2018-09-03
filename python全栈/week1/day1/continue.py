#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 0003 20:01
# @Author  : BigC
# @Site    : 
# @File    : continue.py
# @Software: PyCharm
count = 0

while count <= 100 :
    count += 1
    if count > 5 and count < 95: #只要count在6-94之间，就不走下面的print语句，直接进入下一次loop
        continue
    print("loop ", count)

print("-----out of while loop ------")
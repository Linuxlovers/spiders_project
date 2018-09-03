#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 0003 15:45
# @Author  : BigC
# @Site    : 
# @File    : 作业1.py
# @Software: PyCharm

# print("""
# 文能提笔安天下,
# 武能上马定乾坤.
# 心存谋略略何人胜,
# 古今英雄唯是君.
# """)

goal_num=66
guess_time=0
while guess_time<3:
    guess_num=int(input("请输入你猜测的数字!"))
    if guess_num ==goal_num:
        print("恭喜您猜对了!")
        break
    elif guess_num>goal_num:
        print("请猜测小一点的数字!")
    else:
        print("请猜测大一点的数字")
        guess_time +=1

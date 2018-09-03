#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 0003 20:09
# @Author  : BigC
# @Site    : 
# @File    : while.py
# @Software: PyCharm
# flag=1
# while flag<7 or flag<11:
#     num=input("输入数字")


#求1-100的所有数的和
# count=0
# for i in range(1,101):
#     count=count+i
# print(count)


#输出 1-100 内的所有奇数
# for i in range(1,101):
#     if i%2!=0:
#         print(i)

#输出 1-100 内的所有偶数
# for i in range(1,101):
#     if i%2==0:
#         print(i)

#求1-2+3-4+5 ... 99的所有数的和
# start_num=1
# sum=0
# while start_num<100:
#     if start_num%2!=0:
#         sum=sum +start_num
#     else:
#         sum=sum -start_num
#     start_num+=1
# print(sum)


#用户登陆（三次机会重试）
user="bigc"
passwd="123456"
time=0
while time<3:
    guess_user=input("请输入用户名:")
    guess_passwd=input("请输入密码:")
    if guess_user ==user:
        if guess_passwd==passwd:
            print("恭喜您登陆成功!")
            break
        else:
            print("用户名或者密码错误")
    print("用户名或者密码错误")
    time+=1
print("对不起,你已经输入了3次!")

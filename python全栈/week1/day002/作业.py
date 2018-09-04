#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/4 0004 13:48
# @Author  : BigC
# @Site    : 
# @File    : 作业.py
# @Software: PyCharm
# print(1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)

# print(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)

# print(8 or 3 and 4 or 2 and 0 or 9 and 7)

# print(0 or 2 and 3 and 4 or 6 and 0 or 3)


# print(6 or 2 > 1)
# print(3 or 2 > 1)
# print(0 or 5 < 4)
# print(5 < 4 or 3)
# print(2 > 1 or 6)
# print(3 and 2 > 1)
# print(0 and 3 > 1)
# print(2 > 1 and 3)
# print(3 > 1 and 0)
# print(3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2)


#5设定1个理想数字如：66，让用户输入数字，如果比66大，则显示猜测 的结果大了；如果比66小，则显示猜测的结果小了;只有等于66，显示猜测结果 正确，然后退出循环。
# break_flag=True
# goal_num=66
# while break_flag:
#     guess_num=int(input("请输入猜测的数字:"))
#     if guess_num==goal_num:
#         print("恭喜猜对了")
#         break_flag=False
#     elif guess_num>goal_num:
#         print("猜大了")
#     else:
#         print("猜小了")

# goal_num=66
# while True:
#     guess_num=int(input("请输入猜测的数字:"))
#     if guess_num==goal_num:
#         print("恭喜猜对了")
#         break
#     elif guess_num>goal_num:
#         print("猜大了")
#     else:
#         print("猜小了")

#6
# goal_num=66
# try_time=0
# while try_time<3:
#     guess_num=int(input("请输入猜测的数字:"))
#     if guess_num==goal_num:
#         print("恭喜猜对了")
#         break
#     elif guess_num>goal_num:
#         print("猜大了")
#     else:
#         print("猜小了")
#     try_time+=1
#     if try_time==3:
#         print("太笨了你....")

#7
count=1
while count<=10:
    if count!=7:
        print(count)
    count+=1

#8.求1-100的所有数的和
# count=1
# sum=0
# while count<=100:
#     sum+=count
#     count+=1
# print(sum)

#9.输出 1-100 内的所有奇数
# count=0
# while count<=100:
#     if count%2!=0:
#         print(count)
#     count+=1

#10.输出 1-100 内的所有偶数
# count=1
# while count<=100:
#     if count%2==0:
#         print(count)
#     count+=1

#11.求1-2+3-4+5 ... 99的所有数的和.
# count=1
# sum=0
# while count<=99:
#     if count%2!=0:
#         sum=sum+count
#     else:
#         sum=sum-count
#     count+=1
# print(sum)

#12.用户登陆（三次输错机会）且每次输错误时显示剩余错误次数（提示：使用 字符串格式化）
# user="bigc"
# password="123456"
# break_flag=1
# while break_flag<=3:
#     int_user=input("请输入用户名:")
#     int_passwd=input("请输入密码:")
#     if int_user==user:
#         if int_passwd==password:
#             print("恭喜%s用户登录成功!" % (int_user))
#             break_flag=5
#         else:
#             print("用户名或者密码错误!已经尝试%s次!" % (break_flag))
#         # break
#     else:
#         print("用户名或者密码错误!已经尝试%s次!" % (break_flag))
#     break_flag+=1


# user="bigc"
# password="123456"
# break_flag=1
# while break_flag<=3:
#     int_user=input("请输入用户名:")
#     int_passwd=input("请输 入密码:")
#     if int_user==user and int_passwd==password:
#         print("恭喜%s用户登录成功!" % (int_user))
#         break
#     else:
#         print("用户名或者密码错误!已经尝试%s次!" % (break_flag))
#     break_flag+=1

#13. 用户输输入1个数. 判断这个数是否是1个质数(升级题).
# count=int(input("请输入一个数,让我们来判断是否是质数:"))
# test=0
# while test<=count:
#     if count/test==0:
#         print("%s这个数不是质数" % (count))
#     test+=1
# Python 程序用于检测用户输入的数字是否为质数
#
# 用户输入数字


# num = int(input("请输入一个数字: "))
#
# # 质数大于 1
# if num > 1:
#     # 查看因子
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "不是质数")
#             print(i, "乘于", num // i, "是", num)
#             break
#     else:
#         print(num, "是质数")
#
# # 如果输入的数字小于或等于 1，不是质数
# else:
#     print(num, "不是质数")


# if num>1:
#     num=int(input("输入一个数:"))
#     for i in (2,num):
#         if (num % i)==0:
#             print("%s不是质数" % (num))
#             break
#     else:
#         print("%s是质数" % (num))
# else:
#     print("%s是质数" % (num))



"""14. 输入1个告标语. 判断这个广告是否合法. 根据最新的广告法来判断. 广 告法内容过多. 我们就判断是否包含'最', '第一', '稀缺', '国家级'等字样. 如果包 含. 提示, 广告不合法           

例如,

　　1. 老男孩python世界第一. ==> 不合法                  

　　2. 今年过年不收礼啊. 收礼只收脑白金. ==> 合法
"""
# ad=input("请输入广告词进行检测是否合法:")
# if "最" in ad or '第一'in ad  or '稀缺' in ad:
#     print("%s  >>>不合法" % (ad))
# else:
#     print("%s  >>>合法" % (ad))

#14. 输入1个数. 判断这个数是几位数(算法实现)(升级题)
# num=int(input("请输入一个数字(小于999999)进行判断该数字是几位数:"))
# # if num >0:
# if num % 100000 >=0:
#     print("这个数是6位数")
# elif num % 10000 >=0:
#     print("这个数是5位数")
# elif num % 1000>= 0:
#     print("这个数是4位数")
#
# elif num % 100 >= 0:
#     print("这个数是3位数")
#
# elif num % 10 >= 0:
#     print("这个数是2位数")
#
# else:
#     print("这个数是个位数")

# num=int(input("请输入一个数字:"))
# print("这个数是",len(str(num)),"位数")

#
# count=0
# a=int(input("输入数字:"))
# b=a
# while a!=0:
#       a=a//10
#       count+=1
# print("%s是%s位数" %(b,count))



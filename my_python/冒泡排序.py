#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/26 0026 09:14
# @Author  : BigC
# @Site    : 
# @File    : 冒泡排序.py
# @Software: PyCharm
# 冒泡排序
# 比较相邻的元素大小，将小的前移，大的后移，就像水中的气泡一样，最小的元素经过几次移动，会最终浮到水面上。
#
# def bubbleSort(list):
#     if list != None:
#         if len(list) ==1:
#             pass
#         else:
#             for i in range(len(list)):
#                 for j in range(len(list)-1-i):
#                     if list[j]>list[j+1]:
#                         list[j],list[j+1] = list[j+1],list[j]
#
# if __name__ == '__main__':
#     list1 = [99,2,3,5,7,8,9,6,54,1,42]
#     bubbleSort(list1)
#     print(list1)

def Bubble_sort(list):
    if list !=None:
        if len(list)==1:
            pass
        else:
            for i in range(len(list)):
                for j in range(len(list)-1-i):
                    if list[j]>list[j+1]:
                        list[j],list[j+1]=list[j+1],list[j]

if __name__== '__main__':
    list1=[99,2,1,4,5,6,7,11,44,33,]
    Bubble_sort(list1)
    print("已经排好的数据如下：")
    print(list1)



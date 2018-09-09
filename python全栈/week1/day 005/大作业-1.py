#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/7 0007 21:45
# @Author  : BigC
# @Site    : 
# @File    : 大作业.py
# @Software: PyCharm
bodies = {}
bodies_key=[]
back_flag=1
num=0
while back_flag:
    menus = ("1, 录入", "2, 查询", "3, 删除", "4, 修改", "5, 退出")
    for i in menus:
        print(i)
    choice=input("请输入你的选择:")
    if choice.isdigit():
        choice=int(choice)
        if choice>0 and choice<len(menus)+1:

            if choice==1:
                while 1:
                    num +=1
                    bodies1 = {num: {'name': 'none', 'weight': 0, 'height': 0, 'BMI': 0,"体态":"none"}}
                    name = input("请输入名字:")
                    weight = input("请输入体重:")
                    if type(eval(weight)) == int or type(eval(weight)) == float:
                        pass
                    else:
                        print("请输入正确的体重格式")
                        continue
                    hight = input("请输入身高:")
                    if type(eval(hight)) == int or type(eval(hight)) == float:
                        pass
                    else:
                        print("请输入正确的身高格式")
                        continue
                    bodies1[num]["name"] = name
                    bodies1[num]["weight"] = weight
                    bodies1[num]["hight"] = hight
                    bodies1[num]["BMI"]='%.1f' % (float(weight)/(float(hight)**2))
                    #判断是否肥胖
                    if float(bodies1[num]["BMI"])<18.5:
                        bodies1[num]["体态"]="过轻"
                    elif float(bodies1[num]["BMI"])>18.5 and float(bodies1[num]["BMI"])<23.9:
                        bodies1[num]["体态"] = "正常"
                    elif float(bodies1[num]["BMI"]) > 24 and float(bodies1[num]["BMI"]) < 27:
                        bodies1[num]["体态"] = "过重"
                    elif float(bodies1[num]["BMI"]) > 28 and float(bodies1[num]["BMI"]) < 32:
                        bodies1[num]["体态"] = "肥胖"
                    elif float(bodies1[num]["BMI"]) > 32:
                        bodies1[num]["体态"] = "非常肥胖"

                    bodies.update(bodies1)
                    back_save=input("请输入是/否继续存信息")
                    if back_save=="是":
                        continue
                    elif back_save=="否":
                        break
                    else:
                        print("输入非法,退出修改")
                        break

            elif choice==2:
                while 1:
                    check_id = input("请输入你想查询的人的id:")
                    if check_id.isdigit():
                        if int(check_id) > 0 and int(check_id) <= len(bodies):
                            print("name:%s\nweight:%sKg\nhight:%sm\nBMI:%s\n体态:%s" % (bodies[int(check_id)]["name"],bodies[int(check_id)]["weight"],bodies[int(check_id)]["hight"],bodies[int(check_id)]["BMI"],bodies[int(check_id)]["体态"]))
                        else:
                            print("你输入的用户id不存在!")
                        check_again = input("请问你想要继续查询吗?是/否")
                        if check_again.upper() == "是":
                            continue
                        elif check_again.upper() == "否":
                            break
                        else:
                            print("输入非法,退出查询")
                            break
                    else:
                        print("输入不合法")
                        continue
            elif choice==3:
                while 1:
                    del_id = input("请输入你想删除的人的id:")
                    if del_id.isdigit():
                        if int(del_id) > 0 and int(del_id) <= len(bodies):
                            bodies.pop(int(del_id))
                            back = input("是/否要继续删除id?")
                            if back == "是":
                                continue
                            elif back == "否":
                                break
                            else:
                                print("选择非法,退出删除")
                                break
                        else:
                            print("输入不合法")
                            continue
                    else:
                        print("输入不合法")
                        continue
            elif choice==4:
                while 1:
                    modified_id = input("请输入你想修改的id")
                    if modified_id.isdigit():
                        if int(modified_id) > 0 and int(modified_id) <= len(bodies):
                            bodies[int(modified_id)]["name"] = input("请输入新的名字")
                            bodies[int(modified_id)]["weight"] = input("请输入新的体重")
                            bodies[int(modified_id)]["hight"] = input("请输入新的身高")
                            back_modified = input("请问你是否想要继续修改 是/否:")
                            if back_modified == "是":
                                continue
                            elif back_modified == "否":
                                break
                            else:
                                print("输入非法,退出修改")
                                break
                        else:
                            print("输入的id不存在")
                            continue
                    else:
                        print("输入不合法")
                        continue
            elif choice == 5:
                print("程序退出!")
                back_flag=0
            else:
                print("输入不合法,请重新输入")
                continue
        else:
            print("输入不合法!请重新输入")
            continue
    else:
        print("输入不合法!请重新输入")
        continue
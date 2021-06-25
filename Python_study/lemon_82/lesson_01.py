
# import keyword
# print(keyword.kwlist)

# print(type(20))
# print(type(10011.1))
# print(type(True))
# print(type(False))
# print(isinstance(3.1415,int))
# print(isinstance(3.1415,float))

# stu_info = '''
# 姓名：666666666666666666666666666666666666
#        性别：6666666666666666666
#             年龄：66666666666
#                   地址：66
# '''
# print(stu_info)
#
# str_01 = "软件自动化测试！"
# print(str_01[2])
# print(str_01[2:5:1])
# print(str_01[0:6:5])
# print(str_01[-1])
# print(str_01[::-1])

# str_01 = ("软件自动化测测试！")
# print(str_01[0:len(str_01):1])
# print(str_01.index("自"))
# print(str_01.find("自"))
# print(str_01.index("测"))
# print(str_01.find("测"))
# # print(str_01.index("1"))
# print(str_01.find("1"))

# print(str_01.count("测"))
# str_02 = str_01.replace("软件","硬件")
# print(str_02)

# name = "张飞"
# gender = "男"
# age = 33
# stress = "西川"
# print('''******学员信息********
# 姓名:%s
# 性别:%s
# 年龄:%d
# 联系地址:%s
# '''%(name,gender,age,stress))

# a = 333 + 333
# print("python" + str(a))
# a +=111
# print(a)
# a -=111
# print(a)
# print("python" * 10)
# c = 1000 / 10
# print(c)

# print(5>1)
# print(5>10)
# print("python" == "python")

# print(5>5 and 7>1)
# print(5>1 or 7>9)
# print(not 1>0)
# str_03 = ("软件自动化测试题目")
# print("软件" in str_03)

# list1 = [100,0.1,True,"软件",[1,2,3,4,5.5]]
# # print(list1)
# # print(len(list1))
# # print(list1.index("软件"))
# # print(list1[4])
# # print(list1[0:2:1])
# # list1.append("硬件")
# # print(list1)
# # list1.insert(4,"信号")
# # list1.extend([1.1,2.2,3.3])
# # print(list1)

# list1 = [100,0.1,True,"软件",[1,2,3,4,5.5]]
# list1.pop()
# print(list1)
# list1 = [100,0.1,True,"软件",[1,2,3,4,5.5]]
# list1.remove("软件")
# print(list1)
# list1 = [100,0.1,True,"软件",[1,2,3,4,5.5]]
# list1.clear()
# print(list1)

# list1 = [100,0.1,True,"软件",[1,2,3,4,5.5]]
# list1[0] = "丰田"
# list1[1] = "本田"
# print(list1)
# list1[2] = "本田"
# list1.append("本田")
# print(list1)
# print(list1.count("软件"))
#
# num = input("请输入你的年龄：")
# print("你的年龄是：{}".format(num))

# name = input("请输入姓名：")
# age = input("请输入年龄：")
# gender = input("请输入性别：")
# print('''*************************
# 姓名：{0}
# 性别：{2}
# 年龄：{1}
# *************************
# '''.format(name,age,gender))

# str1 = 'python hello aaa 123123aabb'
# # print(str1[str1.index("p"):str1.index("n")+1:1])
# # num1 = ("o a" in str1)
# # num2 = ("he" in str1)
# # num3 = ("ab" in str1)
# # print('''
# # "o a"是否是该字符串成员：{}
# # "he"是否是该字符串成员：{}
# # "ab"是否是该字符串成员：{}
# # '''.format(num1,num2,num3))
# # str2 = str1.replace("python","lemon")
# # print(str2)
# # print(str1.find("aaa"))
# # print(str1.find("aab"))

# 元组
# tuple1 = (100,100.11,"张飞",[1,1,2,3,4],(1,2,3,4,))
# print(tuple1)
# print(tuple1[2])
# print(tuple1[4][3])
# print(len(tuple1))
# list2 = list(tuple1)
# print(list2)
# list2[4] = "赵云"
# print(list2)
# tuple2 = tuple(list2)
# print(tuple2)

# #字典知识点练习：
# dict1 = {"姓名":"张飞","年龄":18,"性别":"男","身高":180,"体重":"80"}
# print(dict1["姓名"])      #通过key取value
# print(dict1.get("年龄"))  #通过key取value
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())
# dict1["地址"] = "汉中"   #key不存在就增加新的键值对
# print(dict1)
# dict1["姓名"] = "赵云"   #key已经存在就会修改元素值
# print(dict1)
# dict1.update({"电话":13888888888,"email":"lbl@qq.com"})  #增加多个键值对
# print(dict1)
# print(dict1.pop("地址"))
# print(dict1)

# #集合 set{},使用场景，给列表去重
# list3 = [11,22,33,11,11,22,33,44,55,66,77]
# set2 = set(list3)
# print(set2)
# list4 = list(set2)
# print(list4)

# # if判断练习
# money = int(input("请输入你的金额："))
# if money >= 200:
#     print("买个房子")
# elif money >=100:
#     print("付个首付")
# elif money >=50:
#     print("买个车")
# elif money >=50:
#     print("买个单车")
# else :
#     print("努力搬砖")

# for循环学习
# str2 = '我爱学习"python"!'
# count = 0   #计数器
# for i in str2 :
#     if i == "习" :
#         # break  #跳出循环，后面的循环不执行
#         continue #跳出本次循环，后面的循环依然会执行
#     print(i)
#     print("*" * 20)
#     count +=1
# print(count)
# print(len(str2))

# for j in range(0,9,1) :
#     print(j)

# 作业
# 1：a=[1,2,'6','summer'] 请用成员运算符判断 i是否在这个列表里面 -- if
# a = [1,2,'6','summer']
# print("i" in a)
# print("*" * 20)
# count = 0  #计数器
# for b in a :
#     if b == "i" :
#         count +=1
# if count > 0 :
#     print("找到{}个i".format(count))
# else :
#     print("没有i在此列表中")

# 2：dict_1={"class_id":45,'num':20} 请判断班级上课人数是否大于5
# 注：num表示课堂人数。如果大于5，输出人数。
# dict_1={"class_id":45,'num':20}
# if dict_1["num"] > 5 :
#     print(dict_1["num"])
# else :
#     print("班级人数没有达到5以上")

# list1 = ['倾卿', '沐槿', '喜君', '可口', '晨雾', '繁星']
# 列表当中的每一个值包含：姓名、性别、年龄、城市。以字典的形式表达。并且把字典都存在新的 list中，最后打印最终的列表。--list2=[]
# list1 = ['倾卿', '沐槿', '喜君', '可口', '晨雾', '繁星']
# dict1 = {"姓名":"","性别":"女","年龄":"18","城市":"深圳"}
# dict2 = {"姓名":"","性别":"女","年龄":"18","城市":"深圳"}
# dict3 = {"姓名":"","性别":"男","年龄":"20","城市":"广州"}
# dict4 = {"姓名":"","性别":"女","年龄":"18","城市":"武汉"}
# dict5 = {"姓名":"","性别":"男","年龄":"19","城市":"南京"}
# dict6 = {"姓名":"","性别":"男","年龄":"18","城市":"深圳"}
# dict1["姓名"] = list1[0]
# dict2["姓名"] = list1[1]
# dict3["姓名"] = list1[2]
# dict4["姓名"] = list1[3]
# dict5["姓名"] = list1[4]
# dict6["姓名"] = list1[5]
# list11 = list(dict1.values())
# list12 = list(dict2.values())
# list13 = list(dict3.values())
# list14 = list(dict4.values())
# list15 = list(dict5.values())
# list16 = list(dict6.values())
# # list2 = list11 + list12 + list13 + list14 + list15 + list16
# list2 = [list11,list12,list13,list14,list15,list16]
# print(list2)

# list0 = [1,2,3,1.11,True,"python","学习",[1,2,1,00]]
# for k in list0 :
#     print(k)
#     print("*" * 20)

# tuple1 = (1,2,3.3,"测试",[1,2,1],(3,3))
# for l in tuple1 :
#     print(l)
#     print("*" * 20)
#
# dict0 = {"姓名":"张","性别":"男","年龄":"19","城市":"南京"}
# for m in dict0 :
#     print(m)
#     print("*" * 20)
# for m in dict0.values() :
#     print(m)
#     print("*" * 20)
# for m in dict0.items() :
#     print(m)
#     print("*" * 20)

# dict2 = dict(name="李平",age=18,city="beijing")
# print(dict2)

# # python函数定义学习：
# def good_job(salary,bonus,subsidy,*args,**kwargs) :
#     print("salary金额是：{}".format(salary))
#     print("bonus金额是：{}".format(bonus))
#     print("subsidy金额是：{}".format(subsidy))
#     print("args金额是：{}".format(args))
#     print("kwargs金额是：{}".format(kwargs))
#     sum1 = salary + bonus + subsidy
#     for i in args :
#         sum1 +=i
#     for j in kwargs.values() :
#         sum1 +=j
#     print(sum1)
#     return sum1
# # 使用变量来接收返回值result
# result = good_job(10000,2000,800,450,500,a=800,b=90,c=10)   #位置传参：位置不能乱，依次传参
# # result = good_job(salary=10000,bonus=2000,subsidy=800)   #关键字传参
# if result >= 12000 :
#     print("薪资总额是：{}，这是一份好工作".format(result))
#
# 课后作业：
# 1.	把字符串转成列表 - list()
# str1 = "python自动化测试第4节课。"
# list1 = list(str1)
# print(list1)

# 2.	完成任意整数序列的相加 - 生成一个整数序列，里面全是数字。求里面所有数字的和
# a = range(10)
# print(a)
# b = 0
# for i in a :
#     b +=i
# print(b)

# 3.	定义函数：判断一个对象（列表，字典，字符串）的长度是否大于5，如果大于5，输出True；否则输出False。--if 判断嵌套
# def judgement_data(test_data) :
#     if isinstance(test_data,list) :
#         if len(test_data) > 5 :
#             print(test_data)
#             print("True")
#         else :
#             print("False")
#     elif isinstance(test_data,dict) :
#         if len(test_data) > 5 :
#             print(test_data)
#             print("True")
#         else:
#             print("False")
#     elif isinstance(test_data,str) :
#         if len(test_data) > 5 :
#             print(test_data)
#             print("True")
#         else:
#             print("False")
#     else :
#         print(test_data)
#         print("输入的数据不是列表、字典、字符串类型")
# judgement_data({"姓名":"张","年龄":"18","体重":"55","身高":"170","地址":"深圳","籍贯":"广东深圳"})



str1 = 'python hello aaa 123123aabb'
list01 = str1.split(" ")
print(list01)
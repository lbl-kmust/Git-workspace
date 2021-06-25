# 1. 用户输入一个数值，请判断用户输入的是否为偶数？是偶数输出True,不是输出False
# （提示:input输入的不管是什么，都会被转换成字符串，自己扩展，想办法转换为数值类型，再做判段，）
# a = int(input("请输入一个整数："))
# print(a)
# if a % 2 == 0 :
#     print("True")
# else :
#     print("False")

# 2. 现在有列表 li = [‘hello’,‘scb11’,‘!’],通过相关操作转换成字符串：'hello python18 !'（注意点:转换之后单词之间有空格）
# li = ['hello','scb11','!']
# li[0] = 'hello '
# li[1] = 'python18 '
# str1 = ''
# for i in li :
#     str1 +=i
# print(str1)

# 3. 现在有字符串：str1 = 'python hello aaa 123123aabb'
# 1）请计算 字符串中有多少个'a'
# 2）请找出字符串中'123'的下标起始位置
# 3）请分别判断  'o a'      'he'    'ab'  是否是该字符串中的成员？
# str1 = 'python hello aaa 123123aabb'
# print(str1.count("a"))
# print(str1.find('123'))
# if 'o a' in str1 :
#     print("'o a'是该字符串中的成员")
# else :
#     print("'o a'不是该字符串中的成员")
# if 'he' in str1 :
#     print("'he'是该字符串中的成员")
# else :
#     print("'he'不是该字符串中的成员")
# if 'ab' in str1 :
#     print("'ab'是该字符串中的成员")
# else :
#     print("'ab'不是该字符串中的成员")
#
# 4. 将给定字符串的PHP替换为Python
# best_language = "PHP is the best programming language in the world! "
# best_language = "PHP is the best programming language in the world! "
# best_language1 = best_language.replace("PHP","Python")
# print(best_language1)
#
# 5编写代码，提示用户输入1-7七个数字，分别代表周一到周日，如果输入的数字是6或7则为周末，打印输出“今天是周几”
# dict1 = {1:"一",2:"二",3:"三",4:"四",5:"五"}
# date1 = int(input("请输入1-7的一个数字："))
# if date1 not in range(1,8) :
#     print("请重新输入1-7以内的数字")
# elif date1 == 6 or date1 == 7 :
#     print("今天是周末")
# else :
#     print("今天是周{}".format(dict1.get(date1)))

# 6. 现在有一个列表 li2=[1，2，3，4，5]，
#      第一步：请通过相关的操作改成li2 = [0，1，2，3，66，4，5，11，22，33]
#     第二步：对li2进行排序处理
# 第三步：请写出删除列表中元素的方法，并说明每个方法的作用
# li2=[1,2,3,4,5]
# li2.insert(0,0)
# li2.insert(4,66)
# li2.extend([11,22,33])
# print(li2)
#
# li2.sort()
# print(li2)
# li2.sort(reverse=True)
# print(li2)
# li2.sort(reverse=False)
# print(li2)
# li2 = [1,2,3,4,5]
# li2.pop(2)   #通过索引删除
# print(li2)
# li3 = [1,2,3,8,4,5]
# li3.remove(8)  #删除指定元素
# print(li3)
# li4 = [1,2,3,8,4,5]
# li4.clear()  #清空
# print(li4)

# 7. 切片
# 1、li = [1,2,3,4,5,6,7,8,9] 请通过切片得出结果 [3,6,9]
# li = [1,2,3,4,5,6,7,8,9]
# li01 = li[2:len(li):3]
# print(li01)
# 2、s = 'python java php',通过切片获取: ‘java’
# s = 'python java php'
# s01 = s[7:11:1]
# print(s01)
# 3 、tu = ['a','b','c','d','e','f','g','h'],通过切片获取 [‘g’,‘b’]
# tu = ['a','b','c','d','e','f','g','h']
# tu01 = tu[6:0:-5]
# print(tu01)
# tu02 = tu[1:7:5]
# tu02.reverse()
# print(tu02)
#
# 8. 有5道题（通过字典来操作）：
#     1. 某比赛需要获取你的个人信息，设计一个程序，运行时分别提醒输入 姓名、性别、年龄 ，输入完了，请将数据存储起来，
# name = input("请输入你的名字：")
# gender = input("请输入你的性别：")
# age = input("请输入你的年龄：")
# dict01 = dict(姓名 = name,性别 = gender,年龄 = age)
# print(dict01)
#     2、数据存储完了，然后输出个人介绍，格式如下:  我的名字XXX，今年XXX岁，性别XX，喜欢敲代码
# name = input("请输入你的名字：")
# gender = input("请输入你的性别：")
# age = input("请输入你的年龄：")
# dict01 = dict(姓名 = name,性别 = gender,年龄 = age)
# print("我的名字{}，今年{}岁，性别{}，喜欢敲代码".format(dict01["姓名"],dict01["年龄"],dict01["性别"]))
#     3. 有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；
# name = input("请输入你的名字：")
# gender = input("请输入你的性别：")
# age = input("请输入你的年龄：")
# dict01 = dict(姓名 = name,性别 = gender,年龄 = age)
# height = input("请补充你的身高：")
# phone = input("请补充你的手机号：")
# dict02 = {"身高":height,"联系方式":phone}
# dict03 = {}
# dict03.update(dict01)
# dict03.update(dict02)
# print(dict03)
# print("我的名字{}，今年{}岁，性别{}，喜欢敲代码".format(dict01["姓名"],dict01["年龄"],dict01["性别"]))
#     4. 平台为了保护你的隐私，需要你删除你的联系方式；
# name = input("请输入你的名字：")
# gender = input("请输入你的性别：")
# age = input("请输入你的年龄：")
# dict01 = dict(姓名 = name,性别 = gender,年龄 = age)
# height = input("请补充你的身高：")
# phone = input("请补充你的手机号：")
# dict02 = {"身高":height,"联系方式":phone}
# dict03 = {}
# dict03.update(dict01)
# dict03.update(dict02)
# dict03.pop("联系方式")
# skill01 = input("擅长的技能1：")
# skill02 = input("擅长的技能2：")
# skill03 = input("擅长的技能3：")
# dict04 = {"擅长的技能1":skill01,"擅长的技能2":skill02,"擅长的技能3":skill03}
# dict03.update(dict04)
# print(dict03)
# 5. 你为了取得更好的成绩， 你添加了自己的擅长技能，至少需要 3 项

# 9. 一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，如果购买金额大于100元会给20%折扣。
# 编写一程序，询问购买价格，再显示出折扣（%10或20%）和最终价格。
# def discount_price(price) :
#     if  100 >= price >= 50 :
#         final_price = price * 0.9
#         discount = "%10"
#     elif price > 100 :
#         final_price = price * 0.8
#         discount = "%20"
#     else :
#         final_price = price
#         discount = "%0"
#     return final_price,discount
# price = float(input("请输入商品价格："))
# result = discount_price(price)
# print("商品价格是{}，折扣{},折扣价{}".format(price,result[1],result[0]))
#
# 11、一个 5 位数，判断它是不是回文数。例如： 12321 是回文数，个位与万位相同，十位与千位相同。 根据判断打印出相关信息

# def judge_data(data1) :
#     li1 = list(data1)
#     if li1[0] == li1[4] :
#         if li1[1] == li1[3] :
#             data_result = 1
#         else :
#             data_result = 0
#     else :
#         data_result = 0
#     return data_result
# data1 = input("请输入5位的整数：")
# result = judge_data(data1)
# print(result)
# if result== 1 :
#     print("输入的数：{},是回文数".format(data1))
# else :
#     print("输入的数：{},不是回文数".format(data1))

# 12、现有一个字典： dict = {'name':'小明,'age':18,'occup':'students','teacher': {'语文':'李老师','数学':'王老师','英语':'张老师'}}， '
# '请获取到小明同学的名字；然后再获取到小明的数学老师
# dict1 = {"name":"小明","age":18,"occup":"students","teacher": {"语文":"李老师","数学":"王老师","英语":"张老师"}}
# # print(dict1["name"])
# # print(dict1["teacher"]["数学"])
# 13、设计一个函数，获取一个100以内偶数的纯数字序列，并存到列表里， 然后求这些偶数数字的和
# sum1 = 0
# list1 = []
# for i in range(101) :
#     if i % 2 ==0 :
#         list1.append(i)
#         sum1 +=i
# print(list1)
# print(sum1)
# 14、输出99乘法表，结果如下：（提示嵌套for循环，格式化输出）
# for i in range(1,10) :
#     for j in range(1,i+1) :
#         print("{} * {} = {}\t".format(i,j,j*i),end=" ")
#     print()
# 有1 2 3 4 这四个数字，设计程序计算能组成多少个互不相同且无重复数字的3位数？分别是什么？
# num = 0
# li_sum = []
# for i in range(1,5) :
#     for j in range(1,5) :
#         for k in range(1,5) :
#             if i != j and i !=k and j != k :
#                 li = [i,j,k]
#                 str1 = [str(n) for n in li]
#                 print(''.join(str1))
#                 num +=1
#                 li_sum.append(''.join(str1))
# print("一共能组成{}个无重复数字组合，分别是{}".format(num,li_sum))

# 16、通过函数实现一个计算器，运行程序分别提示用户输入数字1，数字2，
# 然后再提示用户选择 ： 加【1】  减【2】 乘【3】 除【4】，每个方法使用一个函数来实现， 选择后调用对应的函数，然后返回结果。

d1 = int(input("请输入数字1或者数字2："))
d2 = int(input("请输入数字1或者数字2："))
d3 = int(input("选择 ： 加【1】  减【2】 乘【3】 除【4】"))
if d3 == 1 :
    result = d1 + d2
    print(result)
elif d3 == 2 :
    result = d1 - d2
    print(result)
elif d3 == 3 :
    result = d1 * d2
    print(result)
elif d3 == 4 :
    result = d1 / d2
    print(result)
else :
    print("选择有误")



# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 11:22:53 2021

@author: iansu
"""

#方法一
names = ["Chirs", "David", "Bill", "Amy", "James"]
scores = [83, 96, 92, 59, 77]

#找最高分跟最高分的名字
print("1.-------------------------------")
MaxScore = 0
MaxName = ""
for i in range(5):
    if scores[i] > MaxScore:
        MaxScore = scores[i]
        MaxName = names[i]
print("最高分:", MaxName, MaxScore)

#找最低分跟最低分的名字
print("2.-------------------------------")
MinScore = 999999
MinName = ""
for i in range(5):
    if scores[i] < MinScore:
        MinScore = scores[i]
        MinName = names[i]
print("最低分:", MinName, MinScore)

#計算平均
print("3.-------------------------------")
avg = sum(scores)/len(scores)
print("平均:", avg)



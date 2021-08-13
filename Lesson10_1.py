# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 10:26:52 2021

@author: iansu
"""

#方法二 名字跟分數合併成一個list
scores = ["Chris", 83,"David", 96, "Bill", 92, "Amy", 59, "James", 77]

#列印所有分數
print("0.----------------------------")
for i in range(1, 10, 2):
    print(scores[i])
    
#找出最高分和最高分的名字
print("1.----------------------------")
MaxScore = 0
MaxName = ""
for i in range(1, 10, 2):
    if scores[i] > MaxScore:
        MaxScore = scores[i]
        MaxName = scores[i-1]
print("最高分:", MaxName, MaxScore)

#找出最低分和最低分的名字
print("2.----------------------------")
MinScore = 99999
MinName = ""
for i in range(1, 10, 2):
    if scores[i] < MinScore:
        MinScore = scores[i]
        MinName = scores[i-1]
print("最低分:", MinName, MinScore)

#找出平均
print("3.----------------------------")
total = 0
for i in range(1, 10, 2):
    total = total + scores[i]
print("平均:", total/5)
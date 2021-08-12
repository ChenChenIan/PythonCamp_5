# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 09:50:59 2021

@author: iansu
"""

scores = [90, 70, 50, 95, 100, 40, 60, 85, 15, 75]

#用Max() 取最大值
print("1.-----------------------")
MaxScore = max(scores)
print(MaxScore)

#用Min() 取最小值
print("2.-----------------------")
MinScore = min(scores)
print(MinScore)

#用sorted() 排序
print("3.-----------------------")
SortedScore = sorted(scores)
print(SortedScore)

#用len() 計算總長度
print("4.-----------------------")
LenScore = len(scores)
print(LenScore)

#用sum() 加總
print("5.-----------------------")
SumScore = sum(scores)
print(SumScore)

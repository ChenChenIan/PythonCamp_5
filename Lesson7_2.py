# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 11:22:36 2021

@author: iansu
"""
#list清單的新增、讀取、插入和刪除用法
scores = [100, 90, 80]

#append新增
print("1.------------")
scores.append(70)
print(scores)

#讀取清單資料
print("2.------------")
print(scores[2])

#insert插入數字
print("3.------------")
print(scores)
scores.insert(1, 95)
print(scores)

#remove移除數字
print("4.------------")
print(scores)
scores.remove(80)
print(scores)
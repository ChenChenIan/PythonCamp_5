# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 12:25:58 2021

@author: iansu
"""
#挑戰 -- 用for loop印出1 ~ 50當中3的倍數
for i in range(1, 51):  #用for迴圈跑出1 ~ (51-1)的數
    if i % 3 == 0:  #用取餘數去取出3的倍數
        print(i)  #列印出來
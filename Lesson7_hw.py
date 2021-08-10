# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 12:49:10 2021

@author: iansu
"""
#回家挑戰 -- 練習建立清單
sport = ["籃球", "羽球", "桌球", "跑步"]  #建立四個最喜歡的運動清單

print("1.----------------------")
print(sport)  #在螢幕輸出那四種運動

print("2.----------------------")
sport.append("操場")  #加入常去的地方
print(sport)

print("3.----------------------")
sport.insert(2, 10)  #插入一個數字在第三位(index=2)的地方
print(sport)

print("4.----------------------")
sport.remove("跑步")  #刪除最後一個
print(sport)
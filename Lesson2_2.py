# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 11:40:43 2021

@author: iansu
"""
#課堂實作--及格還是不及格
score = input("請輸入數字?")  #讓使用者輸入分數
score = int(score)  #把分數從字串轉換成數字
if score >= 60:  #if 條件判斷式，這裡是判斷入果分數大於或等於60將會執行11行，記得在結尾加冒號
    print("恭喜你及格了!!!")  #要記住如果程式是在if的判斷裡面前面則要空四格
else:  #當分數不是大於或等於60將會執行13行程式碼，記得在結尾加冒號
    print("哈哈你不及格!!")  #要記住如果程式是在else的判斷裡面前面則要空四格
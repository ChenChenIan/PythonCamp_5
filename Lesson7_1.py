# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 12:43:27 2021

@author: iansu
"""

#星星塔

#1.用print製作
print("1.-------------")
print("*")
print("**")
print("***")
print("****")
print("*****")

#2.用while製作
print("2.-------------")
i = 1
while i < 6:
    print("*" * i)
    i = i + 1

#3.用for製作
print("3.-------------")
for i in range(5):
    print("*" * (i + 1))

#4.用while製作倒過來的
print("4.-------------")
i = 1
while i < 6:
    print("*" * (6-i))
    i = i + 1

#3.用for製作倒過來的
print("5.-------------")
for i in range(5):
    print("*" * (5 - i))

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 11:08:38 2021

@author: iansu
"""
#用函示的方法重製星星塔
def star(layer):
    for i in range(1, layer + 1):
        print("*" * i)
        
star(5)
star(10)
star(15)
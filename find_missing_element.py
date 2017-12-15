# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 15:26:36 2017

@author: VIPUL
"""

a1 = [1,2,3,4,5,6,7,8]
a2 = [1,3,4,7,2,6,8]

def find_missing_element(a1,a2):
    a1.sort()
    a2.sort()
    for num1,num2 in zip(a1,a2):
        if num1 != num2:
            return num1
    return a1[-1]

find_missing_element(a1,a2)
            
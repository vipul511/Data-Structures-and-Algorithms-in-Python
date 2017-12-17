# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 21:15:30 2017

@author: VIPUL
"""

def sum_of_digits(n):
    if len(str(n)) == 1:
        return n
    else:
        return (n % 10) + sum_of_digits(n//10)
    
sum_of_digits(341)
        
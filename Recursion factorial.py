# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 21:13:05 2017

@author: VIPUL
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
factorial(5)
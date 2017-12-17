# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 21:43:28 2017

@author: VIPUL
"""

def reverse_a_string(s):
    if len(s)<= 1:
        return s
    else:
        return reverse_a_string(s[1:]) + s[0]
    
print(reverse_a_string('abc'))
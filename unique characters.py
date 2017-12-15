# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 02:10:09 2017

@author: VIPUL
"""

s1 = 'abcdea'
s2 = 'abcde'

def unique_char(s):
    chars = set()
    for letter in s:
        if letter in chars:
            return False
        else:
            chars.add(letter)
    return True

unique_char(s1)
unique_char(s2)
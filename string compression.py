# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 22:40:10 2017

@author: VIPUL
"""

s = 'AAAABBBBCCCCCDDEEEE'
def string_compression(s):
    length = len(s)
    if length == 0:
        return ""
    if length ==1:
        return s+"1"
    r = ''
    last = s[0]
    cnt = 1
    i = 1
    while i < length:
        if s[i] == s[i-1]:
            cnt += 1
        else:
            r = r + s[i-1]+str(cnt)
            cnt = 1
        i+=1
    r = r+ s[i-1]+ str(cnt)
    print(r)
    
string_compression(s)
    
        
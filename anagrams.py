# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 14:38:49 2017

@author: VIPUL
"""

s = "public relations"
c = "crap built on lies"

def anagram1(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    return sorted(s1) == sorted(s2)
anagram1(s,c)
    
def anagram2(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    if(len(s1)!= len(s2)):
        return False
    count = {}
    for letter in s1:
        if letter in count:
            count[letter]+=1
        else:
            count[letter] = 1
    for letter in s2:
        if letter in count:
            count[letter]-=1
        else:
            count[letter] = 1
    for k in count:
        if count[k] != 0:
            return False
    return True

anagram2(s,c)
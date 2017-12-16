# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 00:19:04 2017

@author: VIPUL
"""

class Node(object):
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None
        
a = Node(5)
b = Node(3)
a.nextnode = b

print(a.nextnode.value)
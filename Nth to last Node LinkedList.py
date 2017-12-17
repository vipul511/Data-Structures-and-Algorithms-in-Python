# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 18:55:51 2017

@author: VIPUL
"""

def Nth_to_lastNode(n,head):
    right_pointer = head
    left_pointer = head
    for i in range(n-1):
        if not right_pointer.nextNode:
            raise LookupError("Error - n smaller than the linkedList")
        right_pointer.nextNode
    while right_pointer.nextNode!= None:
        right_pointer = right_pointer.nextNode
        left_pointer = left_pointer.nextNode
        
    return left_pointer
            
    
    
class Node(object):
    def __init__(self,value):
        self.value = value
        self.nextNode = None

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
a.nextNode = b
b.nextNode = c
c.nextNode = d
d.nextNode = e

f = Nth_to_lastNode(2,a)
f.value
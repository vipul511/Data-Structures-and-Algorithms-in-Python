# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 13:59:35 2017

@author: VIPUL
"""

class DoublyLinkedList(object):
    def __init__(self,value):
        self.value = value
        self.nextNode = None
        self.previousNode = None
    
a = DoublyLinkedList(5)
b = DoublyLinkedList(4)
c = DoublyLinkedList(3)

b.nextNode = a
b.previousNode = c
c.nextNode = b
a.previousNode = b

 
print(c.nextNode.nextNode.value)        
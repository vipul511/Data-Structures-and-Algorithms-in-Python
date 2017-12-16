# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 14:18:40 2017

@author: VIPUL
"""

class Node(object):
    def __init__(self,value):
        self.value = value
        self.nextNode  = None
        
def LinkedListReversal(head):
    if head == None:
        return head
    current = head
    nextnode = None
    previous = None
    
    while current:
        nextnode = current.nextNode
        current.nextNode = previous
        previous = current
        current = nextnode
    return previous

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextNode = b
b.nextNode = c
c.nextNode = d
d.nextNode = e

LinkedListReversal(a)

e.nextNode.value
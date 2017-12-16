# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 14:08:27 2017

@author: VIPUL
"""

class Node(object):
    def __init__(self,value):
        self.value = value
        self.nextNode = None

def detectCycle(root):
    if root.nextNode == None:
        return False
    
    runner = root
    follower = root
    
    while runner != None and runner.nextNode != None:
        follower = follower.nextNode
        runner = runner.nextNode.nextNode
        
        if runner == follower:
            return True
        
    return False


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
a.nextNode = b
b.nextNode = c
c.nextNode = d
d.nextNode = e
e.nextNode = a

detectCycle(a)

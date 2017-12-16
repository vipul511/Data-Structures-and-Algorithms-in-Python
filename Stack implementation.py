# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 16:00:09 2017

@author: VIPUL
"""

class stack(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[len(self.items)- 1]
    
s = stack()
s.push(5)
print(s.pop())
print(s.isEmpty())
print(s.peek())
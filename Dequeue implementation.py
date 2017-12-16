# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 19:43:45 2017

@author: VIPUL
"""

class Dequeue(object):
    def __init__(self):
        self.items = []
    def addFront(self,item):
        self.items.append(item)
    def addRear(self,item):
        self.items.insert(0,item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items == []



d = Dequeue()

d.addFront(2)
d.addFront(1)
d.addRear(3)

d.removeFront()        
d.removeRear()

d.isEmpty()
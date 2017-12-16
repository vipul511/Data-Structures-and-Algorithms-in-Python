# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 16:08:39 2017

@author: VIPUL
"""

class Queue(object):
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

q = Queue()
q.isEmpty()
q.enqueue(5)
q.enqueue(6)
q.dequeue()

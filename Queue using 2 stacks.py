# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 20:33:10 2017

@author: VIPUL
"""

"""Implementation of queue using two stascks"""

class Queue_using_two_stacks(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def enqueue(self,item):
        self.stack1.append(item)
        
    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop)
        return self.stack2.pop
    def isEmpty(self):
        return
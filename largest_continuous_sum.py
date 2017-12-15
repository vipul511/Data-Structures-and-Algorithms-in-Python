# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 21:45:24 2017

@author: VIPUL
"""
a = [1,2,-1,3,4,10,10,-10,-1]
def largest_continuous_sum(a):
    max_sum = current_sum = a[0]
    for num in a[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(max_sum, current_sum)
    return max_sum

largest_continuous_sum(a)
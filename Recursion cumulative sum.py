# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 21:10:32 2017

@author: VIPUL
"""
def cumulative_sum(n):
    if n== 0:
        return 0
    return n + cumulative_sum(n-1)

cumulative_sum(6)
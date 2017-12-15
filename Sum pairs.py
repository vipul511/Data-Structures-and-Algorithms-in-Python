# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 14:53:43 2017

@author: VIPUL
"""

def pair_sum(nums,k):
    if len(nums) < 2:
        return
    seen = set()
    output = set()
    for i in nums:
        target = k - i
        if target not in seen:
            seen.add(i)
        else:
            output.add((min(i,target),max(i,target)))
    #return len(output)
    print('\n'.join(map(str,list(output))))

pair_sum([1,3,2,2],4)
        
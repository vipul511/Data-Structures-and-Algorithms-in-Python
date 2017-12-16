# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 19:56:34 2017

@author: VIPUL
"""
def balanced_parenthesis(s):
    if len(s) == 0:
        return False
    if len(s) == 1:
        return False
    if len(s)%2 != 0 :
        return False
    open = set('([{')
    matches = set([('(',')'),('[',']'),('{','}')])
    stack = []
    for i in s:
        if i in open:
            stack.append(i)
        else:
            if len(stack)== 0:
                return False
            last_open = stack.pop()
            if (last_open,i) not in matches:
                return False
    return len(stack) == 0        

from nose.tools import assert_equal
class Test(object):
    def test(self,sol):
        assert_equal (sol('(()){}{{'),False)
        assert_equal (sol('(()){}{{}}'),True)
        print('all test cases passed')
        
t = Test()
t.test(balanced_parenthesis)
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 21:48:58 2017

@author: VIPUL
"""
s = "This is the best"
def sentence_reversal(sentence):
    length = len(sentence)
    spaces = [' ']
    words = []
    i = 0
    while i < length:
        if sentence[i] not in spaces:
            word_start = i
            while i < length and sentence[i] not in spaces:
                i+= 1
            words.append(sentence[word_start:i])
        i+= 1
    return ' '.join(reversed(words))
    
        
sentence_reversal(s)
        

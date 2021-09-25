#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 13:50:05 2021

@author: Nima Rahimian
"""


print("Havel-Hakimi algorithm")

def Havel(n):
    
    step = len(n)
    
    count = sum(map(lambda x : x % 2 == 1, n))
 
    for i in range(step):
        if n[i] >= len(n) or n[i] > 2 * (len(n) -1) or n[i] < 0 or count % 2 == 1:
            return False
            break;
    else:
        
        return True

def Hakimi(sequence):
    
    sequence.sort()
    sequence.reverse()
    
    array, step, min_idx = [], sequence[0], len(sequence)
    
    if min_idx > 1 and Havel(sequence) == True:
        
        for i in range(step):
            array.append(sequence[1:][i] - 1)
            
            
        if len(array) == 1:
            sequence[1] = array[0]
            print(sequence[1:])
            
            return Hakimi(sequence[1:])
        
        else: 
            sequence[1:len(array) + 1] = array
            print(sequence[1:])
            
            return Hakimi(sequence[1:])
        
    else: 
        
        return Havel(sequence)

# (Hakimi([9, 8, 8, 8, 6, 5, 4, 4, 2, 2]))
# print(Hakimi([3, 3, 1, 1, 1, 1, 1, 1]))
# print(Hakimi([2, 2, 2]))
# print(Hakimi([3, 3, 3, 1, 2]))
# print(Hakimi([6, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1]))
print(Hakimi([8, 1]))

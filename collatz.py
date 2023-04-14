#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 18:06:17 2021

@author: nimarahimian
"""

memo = {}                               # initialize the memo dictionary
def collatz_seq(n):
    if not n in memo:                   # check if already computed
        if n == 1:                      # if not compute it
            memo[n] = 1                 # cache it
        elif n % 2 == 0:
            memo[n] = collatz_seq(n // 2) + 1
        else:
            memo[n] = collatz_seq(3*n + 1) + 1
    return memo[n]                      # and return it



d = []
for i in range(1, 1000000):
    d.append(collatz_seq(i))

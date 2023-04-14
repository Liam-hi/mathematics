#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 19:58:53 2021

@author: nimarahimian
"""

st = '(12)'

α = {1 : 2, 2 : 1, 3 : 3}

ß = {1 : 3, 2 : 2, 3 : 1}

print(len(α))
print(ß)

for x, y in α.items():
    print(ß[α[x]])

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 21:34:05 2020

@author: podolnik
"""

data = []

with open('input.txt', mode='r') as f:
    data = [int(r.strip()) for r in f.readlines()]
    
# part 1
    
data.sort()

a = None
b = None

for i in range(len(data)):
    j = len(data) - 1
    
    a = data[i]
    
    while data[j] + a >= 2020 and j >= 0:
        if data[j] + a == 2020:
            b = data[j]
            break
        j -= 1
    
    if b is not None:
        break
    
print(a * b)

# part 2

a = None
b = None
c = None

for k in range(len(data)):    
    
    c = data[k]
    
    for i in range(len(data)):
        j = len(data) - 1
        
        a = data[i]
        
        while data[j] + a >= 2020 - c and j >= 0:
            if data[j] + a == 2020 - c:
                b = data[j]
                break
            j -= 1
    
        if b is not None:
            break
        
    if b is not None:
        break
    
print(a * b * c)
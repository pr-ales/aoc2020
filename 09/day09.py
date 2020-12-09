#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 08:29:43 2020

@author: podolnik
"""

data = []

with open('input.txt', mode='r') as f:
    data = [int(l.strip()) for l in f.readlines()]


# part 1
    
n_p = 25
invalid = None
    
for i in range(n_p, len(data)):
    preamble = set(data[i-n_p:i])
    
    ok = False
    for n in preamble:
        if data[i] - n in preamble:
            ok = True
            break

    if not ok:
        invalid = data[i]
        break
    
print(invalid)

# part 2

for i in range(len(data)):
        
    j = i + 2
    while sum(data[i:j]) <= invalid and j < len(data):
        j += 1        
        if sum(data[i:j]) == invalid:
            break
    
    if sum(data[i:j]) == invalid:
        print(max(data[i:j]) + min(data[i:j]))
        break
    
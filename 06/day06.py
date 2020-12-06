#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 10:12:49 2020

@author: podolnik
"""

data = []

with open('input.txt', mode='r') as f:
    group = []
    for l in f.readlines():
        l = l.strip()
        if len(l) == 0:
            data.append(group)
            group = []
        else:
            group.append(set(list(l)))
    if len(group) > 0:
        data.append(group)

# part 1
            
counts = [len(set.union(*g)) for g in data]

print(sum(counts))

# part 1
            
counts = [len(set.intersection(*g)) for g in data]

print(sum(counts))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 10:48:45 2020

@author: podolnik
"""

import numpy as np

data = []

def line2data(l):
    l = l.strip()
    l = l.replace('#', '1').replace('.', '0')
    d = [int(c) for c in list(l)]
    return d
    

with open('input.txt', mode='r') as f:
    data = [line2data(l) for l in f.readlines()]
    
data = np.array(data)

# day 1

num_rows = np.shape(data)[0]
num_cols = np.shape(data)[1]

pos_cols = np.mod(np.arange(1, num_rows) * 3, num_cols)
pos_rows = np.arange(1, num_rows)

trees = data[pos_rows, pos_cols]

print(np.sum(trees))

# day 2

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
trees_count = [0] * len(slopes)

for i, slope in enumerate(slopes):        
    pos_rows = np.arange(slope[1], num_rows, slope[1])
    pos_cols = np.mod(np.arange(1, len(pos_rows) + 1) * slope[0], num_cols)
    
    
    trees = data[pos_rows, pos_cols]
    trees_count[i] = np.sum(trees)
    
print(np.prod(trees_count))

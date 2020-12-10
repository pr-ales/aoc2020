#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 08:22:50 2020

@author: podolnik
"""

import numpy as np

data = []

with open('input.txt', mode='r') as f:
    data = [int(l.strip()) for l in f.readlines()]
    
# part 1
    
data.sort()
data.insert(0, 0)
data.append(data[-1] + 3)

data = np.array(data)

diff = data[1:] - data[:-1]

print(sum(diff == 1) * sum(diff == 3))

# part 2

plugs = {p: [] for p in data}
acc = {p: 0 for p in data}

n_d = len(data)

for i in range(n_d - 1):
    for j in range(i + 1, min(i + 4, n_d)):
        if data[j] - data[i] <= 3:
            plugs[data[i]].append(data[j])
    
acc[0] = 1

for p in plugs:
    conn = plugs[p]
    for c in conn:
        acc[c] += acc[p]
    
print(acc[data[-1]])
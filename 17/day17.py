#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 09:34:02 2020

@author: podolnik
"""

from time import time
import numpy as np

start_1 = time()

data = []

val_map = {'#': 1, '.': 0}

with open('input.txt', mode='r') as f:
    data = [[val_map[c] for c in list(l.strip())] for l in f.readlines()]

# part 1

def show(cubes):    
    cubes = np.array([[c[0], c[1], c[2]] for c in cubes])
    z_min = min(cubes[:,0])
    z_max = max(cubes[:,0]) + 1
    
    y_min = min(cubes[:,1])
    y_max = max(cubes[:,1]) + 1
    
    x_min = min(cubes[:,2])
    x_max = max(cubes[:,2]) + 1
    
    for z in range(z_min, z_max):
        sl = cubes[cubes[:,0] == z,:]
        print(' ---- z = {} ---- '.format(z))
        grid = [['.' for i in range(x_min, x_max)] for j in range(y_min, y_max)]
        for i in range(len(sl)):
            grid[sl[i,1] - y_min][sl[i,2] - x_min] = "#"
        for l in grid:
            print(''.join(l))

def iterate_nd(cubes, i_max, i = 0):
    if i == i_max:
        return(len(cubes))
        
    n_dim = len(next(iter(cubes)))
    d_dim = [-1, 0, 1]
    deltas = [[0] * n_dim for _ in range(pow(3, n_dim))]
    for d in range(n_dim):
        for j in range(len(deltas)):
            deltas[j][d] = d_dim[(j // pow(3, d)) % 3]
    
    neighbours = {c : -1 for c in cubes}
    for c in cubes:
        for d in deltas:
            n = tuple([c[j] + d[j] for j in range(n_dim)])
            
            if n in neighbours.keys():
                neighbours[n] += 1
            else:
                neighbours[n] = 1
                        
    new_cubes = set()
    for n in neighbours:
        if n in cubes and (neighbours[n] == 2 or neighbours[n] == 3):
            new_cubes.add(n)
        elif n not in cubes and neighbours[n] == 3:
            new_cubes.add(n)
    
    return iterate_nd(new_cubes, i_max, i + 1)

z = 0
cubes = set()
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == 1:
            cubes.add((z, y, x))
            
n = iterate_nd(cubes, 6)
end_1 = time()

print(n)
print(end_1 - start_1)

# part 2

start_2 = time()

t = 0
z = 0
cubes = set()
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == 1:
            cubes.add((t, z, y, x))

n = iterate_nd(cubes, 6)
end_2 = time()

print(n)
print(end_2 - start_2)
print(end_2 - start_1)

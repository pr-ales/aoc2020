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

z = 0
cubes = []
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == 1:
            cubes.append((z, y, x))

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
    
def iterate(cubes, i_max, i = 0):
    # print('iteration {}'.format(i))
    # show(cubes)
    
    if i == i_max:
        return(len(cubes))
    
    neighbours = {c : -1 for c in cubes}
    
    for c in cubes:
        for d_z in range(-1, 2):
            for d_y in range(-1, 2):
                for d_x in range(-1, 2):
                    z = c[0] + d_z
                    y = c[1] + d_y
                    x = c[2] + d_x
                    
                    n = (z, y, x)
                    
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
    
    return iterate(new_cubes, i_max, i + 1)

n = iterate(cubes, 6)
end_1 = time()

print(n)
print(end_1 - start_1)

# part 2

start_2 = time()

t = 0
z = 0
cubes = []
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == 1:
            cubes.append((t, z, y, x))


def iterate_4d(cubes, i_max, i = 0):
    if i == i_max:
        return(len(cubes))
    
    neighbours = {c : -1 for c in cubes}
    
    for c in cubes:
        for d_t in range(-1, 2):
            for d_z in range(-1, 2):
                for d_y in range(-1, 2):
                    for d_x in range(-1, 2):
                        t = c[0] + d_t
                        z = c[1] + d_z
                        y = c[2] + d_y
                        x = c[3] + d_x
                
                        n = (t, z, y, x)
                        
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
    
    return iterate_4d(new_cubes, i_max, i + 1)

n = iterate_4d(cubes, 6)
end_2 = time()

print(n)
print(end_2 - start_2)
print(end_2 - start_1)

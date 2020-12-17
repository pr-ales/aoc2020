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
            cubes.append([z, y, x])
            
cubes = np.array(cubes)

def show(cubes):    
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
#    print()
#    print('iteration {}'.format(i))
#    show(cubes)
    
    if i == i_max:
        return len(cubes)
    
    z_min = min(cubes[:,0]) - 1
    z_max = max(cubes[:,0]) + 2
    
    y_min = min(cubes[:,1]) - 1
    y_max = max(cubes[:,1]) + 2
    
    x_min = min(cubes[:,2]) - 1
    x_max = max(cubes[:,2]) + 2
    
    all_cubes = set([(c[0], c[1], c[2]) for c in cubes])
    new_cubes = []
    
    for z in range(z_min, z_max):
        for y in range(y_min, y_max):
            for x in range(x_min, x_max):
                idx = np.array([True for _ in range(len(cubes))])
                
                idx = np.logical_and(idx, z - 1 <= cubes[:,0])
                idx = np.logical_and(idx, cubes[:,0] <= z + 1)
                
                idx = np.logical_and(idx, y - 1 <= cubes[:,1])
                idx = np.logical_and(idx, cubes[:,1] <= y + 1)
                
                idx = np.logical_and(idx, x - 1 <= cubes[:,2])
                idx = np.logical_and(idx, cubes[:,2] <= x + 1)
                
                neighbors = sum(idx)
                cube = (z, y, x)
                active = cube in all_cubes
                
                if active:
                    neighbors -= 1
                
                cube_arr = [z, y, x]
                
                if active and (neighbors == 2 or neighbors == 3):
                    new_cubes.append(cube_arr)
                if not active and neighbors == 3:
                    new_cubes.append(cube_arr)    
    
    return iterate(np.array(new_cubes), i_max, i = i + 1)

n_cubes = iterate(cubes, 6)
end_1 = time()
print(n_cubes)
print(end_1 - start_1)

# part 2

start_2 = time()

z = 0 
t = 0
cubes_4d = []
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == 1:
            cubes_4d.append([t, z, y, x])
            
cubes_4d = np.array(cubes_4d)

def iterate_4d(cubes, i_max, i = 0):
#    print()
#    print('iteration {}'.format(i))
#    show(cubes)
    
    if i == i_max:
        return len(cubes)
    
    t_min = min(cubes[:,0]) - 1
    t_max = max(cubes[:,0]) + 2
    
    z_min = min(cubes[:,1]) - 1
    z_max = max(cubes[:,1]) + 2
    
    y_min = min(cubes[:,2]) - 1
    y_max = max(cubes[:,2]) + 2
    
    x_min = min(cubes[:,3]) - 1
    x_max = max(cubes[:,3]) + 2
    
    all_cubes = set([(c[0], c[1], c[2], c[3]) for c in cubes])
    new_cubes = []
    
    for t in range(t_min, t_max):
        for z in range(z_min, z_max):
            for y in range(y_min, y_max):
                for x in range(x_min, x_max):
                    idx = np.array([True for _ in range(len(cubes))])
                    
                    idx = np.logical_and(idx, t - 1 <= cubes[:,0])
                    idx = np.logical_and(idx, cubes[:,0] <= t + 1)
                    
                    idx = np.logical_and(idx, z - 1 <= cubes[:,1])
                    idx = np.logical_and(idx, cubes[:,1] <= z + 1)
                    
                    idx = np.logical_and(idx, y - 1 <= cubes[:,2])
                    idx = np.logical_and(idx, cubes[:,2] <= y + 1)
                    
                    idx = np.logical_and(idx, x - 1 <= cubes[:,3])
                    idx = np.logical_and(idx, cubes[:,3] <= x + 1)
                    
                    neighbors = sum(idx)
                    cube = (t, z, y, x)
                    active = cube in all_cubes
                    
                    if active:
                        neighbors -= 1
                    
                    cube_arr = [t, z, y, x]
                    
                    if active and (neighbors == 2 or neighbors == 3):
                        new_cubes.append(cube_arr)
                    if not active and neighbors == 3:
                        new_cubes.append(cube_arr)    
    
    return iterate_4d(np.array(new_cubes), i_max, i = i + 1)

n_cubes = iterate_4d(cubes_4d, 6)
end_2 = time()
print(n_cubes)
print(end_2 - start_2)
print(end_2 - start_1)
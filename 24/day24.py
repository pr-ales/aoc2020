#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 08:42:32 2020

@author: podolnik
"""

directions = {'e': (2, 0), 'se': (1, 2), 'sw': (-1, 2), 'w': (-2, 0), 'nw': (-1, -2), 'ne': (1, -2)}

def parse_line(line):
    line = line.strip()
    
    i = 0
    instructions = []
    while i < len(line):
        if line[i] == 'e' or line[i] == 'w':
            instructions.append(line[i])
        else:
            instructions.append(line[i:i+2])
            i += 1        
        i += 1
    return instructions
    
data = []

with open('input.txt', mode='r') as f:
    data = [parse_line(line) for line in f.readlines()]
   
# part 1
    
tiles = {}

for path in data:
    x, y = 0, 0
    for d in path:
        x += directions[d][0]
        y += directions[d][1]
        
    c = (x, y)
    
    if c in tiles:
        tiles.pop(c)
    else:
        tiles[c] = 1
        
odd = len(tiles)
print(odd)

# part 2
def adjacent(c):
    adj = []
    for d in directions:
        adj.append((c[0] + directions[d][0], c[1] + directions[d][1]))
    return adj

n_iter = 100

for i in range(n_iter):
    neighbors = {}
    
    for c in tiles:
        adj = adjacent(c)
        for a in adj:
            if a in neighbors:
                neighbors[a] += 1
            else:
                neighbors[a] = 1
    
    new_tiles = {}
    for c in tiles:
        if c not in neighbors:
            pass
        elif neighbors[c] > 2:
            pass
        else:
            new_tiles[c] = 1
        
        if c in neighbors:
            neighbors.pop(c)
    
    for c in neighbors:
        if neighbors[c] == 2:
            new_tiles[c] = 1
    
    tiles = new_tiles
    
print(len(tiles))

import matplotlib.pyplot as plt

x, y = zip(*tiles.keys())

plt.plot(x, y, linewidth = 0, marker='.')

plt.show()
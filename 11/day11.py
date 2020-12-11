#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 10:27:56 2020

@author: podolnik
"""

from time import time
import copy

start = time()

data = []

char_map = {'L': 0, '#': 1, '.': -1}
val_map = {0: 'L', 1: '#', -1: '.'}

with open('input.txt', mode='r') as f:
    data = [[char_map[c] for c in list(l.strip())] for l in f.readlines()]

def flip(state, row, col, condition_n, check_seats):
    total = sum([state[s[0]][s[1]] for s in check_seats])
    
    occupied = state[row][col] == 1
    empty = state[row][col] == 0
    
    if empty and total == 0:
        return 1
    if occupied and total >= condition_n:
        return 0
    
    return state[row][col]

def show(data):
    for l in data:
        print(''.join([val_map[c] for c in l ]))
    print()

# show(data)

# part 1
    
directions = [-1, 0, 1]
r_max = len(data)
c_max = len(data[0])

adjacent = [[[] for i in range(len(l))] for l in data]

for row in range(r_max):
    for col in range(c_max):
        if data[row][col] == 0:
            for d_r in directions:
                for d_c in directions:
                    if d_r == 0 and d_c == 0:
                        continue
                    else:
                        r = row + d_r
                        c = col + d_c
                        if c >= 0 and r >= 0 and c < c_max and r < r_max:
                            if data[r][c] == 0:
                                adjacent[row][col].append((r, c))

occupied = -1
state = copy.deepcopy(data)
        
while True:
    next_state = copy.deepcopy(state)    
    next_occupied = 0
    for r in range(len(state)):
        for c in range(len(state[0])):
            next_state[r][c] = flip(state, r, c, 4, adjacent[r][c])  
            next_occupied += next_state[r][c] == 1
   
    if next_occupied == occupied:
        break
    
    occupied = next_occupied
    state = next_state
    
print(occupied)

end_1 = time()
print(end_1 - start)

# part 2

closest = [[[] for i in range(len(l))] for l in data]

prep_start = time()

for row in range(r_max):
    for col in range(c_max):
        if data[row][col] == 0:
            for d_r in directions:
                for d_c in directions:
                    if d_r == 0 and d_c == 0:
                        continue
                    else:
                        r = row + d_r
                        c = col + d_c
                        while c >= 0 and r >= 0 and c < c_max and r < r_max:
                            if data[r][c] == 0:
                                closest[row][col].append((r, c))
                                break
                            r = r + d_r
                            c = c + d_c

prep_end = time()
print(prep_end - prep_start)

occupied = -1
state = copy.deepcopy(data)

while True:
    next_state = copy.deepcopy(state)    
    next_occupied = 0
    for r in range(len(state)):
        for c in range(len(state[0])):
            next_state[r][c] = flip(state, r, c, 5, closest[r][c])        
            next_occupied += next_state[r][c] == 1
   
    if next_occupied == occupied:
        break
    
    occupied = next_occupied
    state = next_state

print(occupied)

end_2 = time()
print(end_2 - end_1)
print(end_2 - start)
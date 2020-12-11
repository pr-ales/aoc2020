#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 10:27:56 2020

@author: podolnik
"""

import numpy as np
from time import time

start = time()

data = []

char_map = {'L': 0, '#': 1, '.': -1}
val_map = {0: 'L', 1: '#', -1: '.'}

with open('input.txt', mode='r') as f:
    data = np.array([[char_map[c] for c in list(l.strip())] for l in f.readlines()])
    
def new_state(data):
    return np.full(np.shape(data), np.nan)

def flip(state, row, col, condition_n, check_seats):
    r_max = len(state)
    c_max = len(state[0])
       
    filtered_seats = [(s[0] + row, s[1] + col) for s in check_seats if s[1] + col >= 0 and s[0] + row >= 0 and s[1] + col < c_max and s[0] + row < r_max]
    
    r = [s[0] for s in filtered_seats]
    c = [s[1] for s in filtered_seats]
    
    seats = state[r,c] == 1
    total = seats.sum()
    
    occupied = state[row,col] == 1
    empty = state[row,col] == 0
    
    if empty and total == 0:
        return 1
    if occupied and total >= condition_n:
        return 0
    
    return state[row, col]

def show(data):
    for l in data:
        print(''.join([val_map[c] for c in l ]))
    print()

# show(data)

# part 1
    
directions = [-1, 0, 1]

default_closest = []
for d_r in directions:
    for d_c in directions:
        if d_r == 0 and d_c == 0:
            pass
        else:
            default_closest.append((d_r, d_c))

state = np.array(data)
        
while True:
    next_state = new_state(state)    
    for r in range(len(state)):
        for c in range(len(state[0])):
            next_state[r,c] = flip(state, r, c, 4, default_closest)        
   
    if np.array_equal(next_state, state):
        break
    
    state = next_state
    
occupied = state == 1
print(occupied.sum())

end_1 = time()
print(end_1 - start)

# part 2

closest = [[[] for i in range(len(l))] for l in data]

r_max = len(data)
c_max = len(data[0])

for row in range(r_max):
    for col in range(c_max):
        if data[row,col] == 0:
            for d_r in directions:
                for d_c in directions:
                    if d_r == 0 and d_c == 0:
                        continue
                    else:
                        r = row + d_r
                        c = col + d_c
                        while c >= 0 and r >= 0 and c < c_max and r < r_max:
                            if data[r, c] == 0:
                                closest[row][col].append((r - row, c - col))
                                break
                            r = r + d_r
                            c = c + d_c

state = np.array(data)

while True:
    next_state = new_state(state)    
    for r in range(len(state)):
        for c in range(len(state[0])):
            check_seats = closest[r][c]
            next_state[r,c] = flip(state, r, c, 5, check_seats)        
   
    if np.array_equal(next_state, state):
        break
    
    state = next_state

occupied = state == 1
print(occupied.sum())

end_2 = time()
print(end_2 - end_1)
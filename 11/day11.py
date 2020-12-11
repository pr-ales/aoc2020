#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 10:27:56 2020

@author: podolnik
"""

import numpy as np

data = []

char_map = {'L': 0, '#': 1, '.': -1}
val_map = {0: 'L', 1: '#', -1: '.'}

with open('input.txt', mode='r') as f:
    data = np.array([[char_map[c] for c in list(l.strip())] for l in f.readlines()])
    
def new_state(data):
    return np.full(np.shape(data), np.nan)

def flip(data, row, col):
    r_max = len(data)
    c_max = len(data[0])
    seats = data[max(row-1,0):min(row+2, r_max),max(0, col-1):min(col+2, c_max)] == 1
    total = seats.sum()
    
    seat = data[row,col]
    
    occupied = data[row,col] == 1
    empty = data[row,col] == 0
    
    if empty and total == 0:
        return 1
    if occupied and total - 1 >= 4:
        return 0
    
    return data[row, col]

def show(data):
    for l in data:
        print(''.join([val_map[c] for c in l ]))
    print()

# show(data)

# part 1

state = np.array(data)

while True:
    next_state = new_state(state)    
    for r in range(len(state)):
        for c in range(len(state[0])):
            next_state[r,c] = flip(state, r, c)        
   
    if np.array_equal(next_state, state):
        break
    
    state = next_state

occupied = state == 1
print(occupied.sum())

# part 2

closest = [[[] for i in range(len(l))] for l in data]

r_max = len(data)
c_max = len(data[0])

directions = [-1, 0, 1]

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

def flip2(data, row, col):
    
    check_seats = closest[row][col]
    
    r = [s[0] + row for s in check_seats]
    c = [s[1] + col for s in check_seats]
    
    seats = data[r,c] == 1
    total = seats.sum()
    
    seat = data[row,col]
    
    occupied = data[row,col] == 1
    empty = data[row,col] == 0
    
    if empty and total == 0:
        return 1
    if occupied and total >= 5:
        return 0
    
    return data[row, col]


state = np.array(data)

while True:
    next_state = new_state(state)    
    for r in range(len(state)):
        for c in range(len(state[0])):
            next_state[r,c] = flip2(state, r, c)        
   
    if np.array_equal(next_state, state):
        break
    
    state = next_state

occupied = state == 1
print(occupied.sum())
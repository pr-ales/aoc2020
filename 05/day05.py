#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 09:04:13 2020

@author: podolnik
"""

data = []

with open('input.txt', mode='r') as f:
    data = [list(l.strip()) for l in f.readlines()]

# part 1

seat_ids = [0] * len(data)
    
for bp_i, bp in enumerate(data):    
    min_r = 0
    max_r = 127
    final_r = None
    for i in range(6):
        c = bp[i]
        
        if c == 'F':
            max_r = max_r - round((max_r - min_r) / 2)
        elif c == 'B':
            min_r = min_r + round((max_r - min_r) / 2)
        
    final_r = min_r if bp[6] == 'F' else max_r
            
    min_c = 0
    max_c = 7
    for i in range(7, 9):
        c = bp[i]
        
        if c == 'L':
            max_c = max_c - round((max_c - min_c) / 2)
        elif c == 'R':
            min_c = min_c + round((max_c - min_c) / 2)
    
    final_c = min_c if bp[9] == 'L' else max_c
    
    seat_id = final_r * 8 + final_c
    
    seat_ids[bp_i] = seat_id

print(max(seat_ids))

# part 2

seat_ids.sort()

for i in range(1, len(seat_ids)):
    if seat_ids[i] - seat_ids[i-1] == 2:
        print(seat_ids[i-1] + 1)
        break
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 09:04:13 2020

@author: podolnik
"""

data = []

with open('input.txt', mode='r') as f:
    data = [l.strip() for l in f.readlines()]

# part 1

seat_ids = [0] * len(data)
    
for bp_i, bp in enumerate(data):    
    binary = bp.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
    seat_ids[bp_i] = int(binary, 2)
    
print(max(seat_ids))

# part 2

seat_ids.sort()

for i in range(1, len(seat_ids)):
    if seat_ids[i] - seat_ids[i-1] == 2:
        print(seat_ids[i-1] + 1)
        break
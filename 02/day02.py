#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 08:28:50 2020

@author: podolnik
"""


data = []

def row2data(r):
    parts = r.split(' ')
    c_min = int(parts[0].split('-')[0])
    c_max = int(parts[0].split('-')[1])
    letter = parts[1][0]
    pwd = parts[2]
    return (c_min, c_max, letter, pwd)

with open('input.txt', mode='r') as f:
    data = [row2data(r.strip()) for r in f.readlines() if len(r.strip()) > 0]

# part 1
    
valid_1 = [r[3] for r in data if r[3].count(r[2]) >= r[0] and r[3].count(r[2]) <= r[1]]
valid_1_count = len(valid_1)
print(valid_1_count)

# part 2

valid_2 = [r[3] for r in data if (r[3][r[0] - 1] == r[2]) ^ (r[3][r[1] - 1] == r[2])]
valid_2_count = len(valid_2)
print(valid_2_count)
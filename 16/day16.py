#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 09:13:07 2020

@author: podolnik
"""

import re
from time import time

start_1 = time()

locations = {}
ticket = []
nearby = []

with open('input.txt', mode='r') as f:
    text = f.read()
    parts = text.split('\n\n')
    
    p = '([a-z ]*): ([0-9]*)-([0-9]*) or ([0-9]*)-([0-9]*)'
    matches = re.findall(p, parts[0])
    locations = {m[0]: ((int(m[1]), int(m[2])),(int(m[3]), int(m[4]))) for m in matches}
    
    ticket = [int(n) for n in parts[1].split('\n')[1].split(',')]
    
    lines = parts[2].split('\n')[1:-1]
    nearby = [[int(n) for n in l.split(',')] for l in lines]
    
# part 1

def get_invalid(n_list):
    invalid = []
    for n in n_list:
        valid = False
        for loc, val in locations.items():
            if val[0][0] <= n <= val[0][1] or val[1][0] <= n <= val[1][1]:
                valid = True
        if not valid:
            invalid.append(n)
    return invalid

all_invalid = [get_invalid(t) for t in nearby]
result = sum(sum(all_invalid, []))
end_1 = time()

print(result)
print(end_1 - start_1)

# part 2

start_2 = time()

filtered_tickets = []
if len(get_invalid(ticket)) == 0:
    filtered_tickets.append(ticket)

filtered_tickets.extend([t for t in nearby if len(get_invalid(t)) == 0])

def get_nonmatching(n_list):
    nonmatching = {loc: [] for loc in locations}
    for i, n in enumerate(n_list):
        for loc, val in locations.items():
            if val[0][0] <= n <= val[0][1] or val[1][0] <= n <= val[1][1]:
                pass
            else:
                nonmatching[loc].append(i)
                
    return nonmatching

all_nonmatching = [get_nonmatching(t) for t in filtered_tickets]
possible = {loc: [i for i in range(len(locations))] for loc in locations}

for c in all_nonmatching:
    for loc, val in c.items():
        for n in val:
            if n in possible[loc]:
                possible[loc].remove(n)

while True:
    certain = [loc for loc in possible if len(possible[loc]) == 1]
    for c in certain:
        i = possible[c][0]
        for loc in possible:
            if not loc == c and i in possible[loc]:
                possible[loc].remove(i)
    ok = True
    for loc in possible:
        if len(possible[loc]) > 1:
            ok = False
            break
    if ok:
        break
    
result = 1

for loc in possible:
    if 'departure' in loc:
        v = ticket[possible[loc][0]]
        result *= v

end_2 = time()
print(result)
print(end_2 - start_2)
print(end_2 - start_1)
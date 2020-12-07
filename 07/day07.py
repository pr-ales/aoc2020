#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 08:28:31 2020

@author: podolnik
"""

import re

data = {}

with open('input.txt', mode='r') as f:
    for l in f.readlines():
        parts = l.strip().split('bags contain')
        k = parts[0].strip()        
        
        matches = re.findall('([0-9]+) ([a-z]* [a-z]*) bag', parts[1])
        ib = {m[1]: int(m[0]) for m in matches}      
        
        data[k] = (ib)

# part 1
        
pivot = 'shiny gold'
        
bags = [[pivot]]

while True:
    next_bags = [spec for spec in data if len(set.intersection(set(bags[-1]), set(data[spec]))) > 0]
    
    if len(next_bags) > 0:
        bags.append(next_bags)
    else:
        break

compatible = sorted(list(set.union(*[set(b) for b in bags])))
print(len(compatible) - 1)

# part 2

def count_inner(all_bags, bag):    
    return sum([all_bags[bag][ib] * count_inner(all_bags, ib) for ib in all_bags[bag]]) + 1

inner_count = count_inner(data, pivot) - 1
print(inner_count)
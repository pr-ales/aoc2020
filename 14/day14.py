#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 08:55:11 2020

@author: podolnik
"""

import re
from time import time

start_1 = time()

data = {}

with open('input.txt', mode='r') as f:
    current_mask = None
    
    patt_mask = 'mask = ([01X]*)'
    patt_mem =  'mem\[([0-9]*)\] = ([0-9]*)'
    
    for l in f.readlines():
        m = re.match(patt_mask, l)
        if m:
            current_mask = m[1]
            data[current_mask] = []
        m = re.match(patt_mem, l)
        if m:
            data[current_mask].append((int(m[1]), int(m[2])))
            
# part 1
  
reg = {}          
            
for mask in data:
    masked = [i for i, c in enumerate(list(mask)) if c != 'X']
     
    for spec in data[mask]:
        addr, val = spec[0], spec[1]
        bin_v = list('{:036b}'.format(val))
        for i in masked:
            bin_v[i] = mask[i]
        
        bin_str = ''.join(bin_v)
        
        val = int(bin_str, 2)
        reg[addr] = val
        
val_sum = sum(reg.values())
print(val_sum)

end_1 = time()
print(end_1 - start_1)

# part 2

start_2 = time()

reg = {}          
            
for mask in data:
    masked = [i for i, c in enumerate(list(mask)) if c != 'X']
    floating = [i for i, c in enumerate(list(mask)) if c == 'X']
     
    for spec in data[mask]:
        addr, val = spec[0], spec[1]
        bin_addr = list('{:036b}'.format(addr))
        for i in masked:
            if mask[i] == '1':
                bin_addr[i] = mask[i]
        
        fmt = '{{:0{}b}}'.format(len(floating))
        n = pow(2, (len(floating)))
        for i in range(n):
            float_str = fmt.format(i)
            new_addr = list(bin_addr)
            
            for j in range(len(floating)):
                new_addr[floating[j]] = float_str[j]
            
            new_addr_str = ''.join(new_addr)
            addr = int(new_addr_str, 2)
            reg[addr] = val
            
        
val_sum = sum(reg.values())
end_2 = time()
print(val_sum)

print(end_2 - start_2)
print(end_2 - start_1)

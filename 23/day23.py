#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 08:28:12 2020

@author: podolnik
"""

from time import time

input_text = '389125467' # test input
input_text = '253149867'

cups = [int(c) for c in input_text]

def shuffle(cups, n_moves = 100):
    
    current = cups[0]
    n_cups = len(cups)

    for m in range(n_moves):
#        print(cups)
        i_c = cups.index(current)
        picked = []    
        i_adj = (i_c + 1) % n_cups
        for _ in range(3):
            if i_adj >= len(cups):
                i_adj = 0
            picked.append(cups.pop(i_adj))
        
#        print(current, picked)
        
        next_cup = current - 1 if current > 1 else max(cups)
        while next_cup in picked:
            next_cup = next_cup - 1 if next_cup > 1 else max(cups)
        
#        print(next_cup)
        
        i_n = cups.index(next_cup)
        
        for i in range(3):
            cups.insert(i_n + 1 + i, picked[i])
        
        current = cups[(cups.index(current) + 1) % n_cups]
        
        if m % 1000 == 0:
            print(m)
    return cups

cups = shuffle(cups)

print('final')

i_1 = cups.index(1)
ordering = [cups[(i_1 + i + 1) % len(cups)] for i in range(len(cups) - 1)]

print(''.join([str(c) for c in ordering]))

cups = [int(c) for c in input_text]

rest = [i for i in range(max(cups) + 1, 1000001)]
cups.extend(rest)

cups = shuffle(cups, n_moves = 1000000)

i_1 = cups.index(1)
stars = [cups[(i_1 + i + 1) % len(cups)] for i in range(2)]
print(stars, stars[0] * stars[1])



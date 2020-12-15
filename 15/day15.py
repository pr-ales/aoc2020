#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 08:41:58 2020

@author: podolnik
"""

from time import time

start_1 = time()

text, turns = '0,5,4,1,10,14,7', 2020
#text, turns = '0,3,6', 10

data = [int(c) for c in text.split(',')]

# part 1

def play(data, turns):
    stats = dict(zip(list(data), [[i, i] for i in range(len(data))]))
    game = set(data[:-1])
    last = data[-1]
        
    for i in range(len(data), turns):
        prev_last = last
        if last not in game:
            last = 0
        else:
            last_i = stats[last][0]
            last = i - last_i - 1
            if last not in stats:
                stats[last] = [i, i]
                        
        game.add(prev_last)
        stats[last][0] = stats[last][1]
        stats[last][1] = i
                
    return last, stats
    
last, stats = play(data, turns)
end_1 = time()

print(last)
print(end_1 - start_1)

# part 2

start_2 = time()

turns = 30000000

last, stats = play(data, turns)
end_2 = time()

print(last)
print(end_2 - start_2)
print(end_2 - start_1)
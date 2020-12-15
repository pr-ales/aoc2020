#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 08:41:58 2020

@author: podolnik
"""

text, turns = '0,5,4,1,10,14,7', 2020
#text, turns = '0,3,6', 10

data = [int(c) for c in text.split(',')]

# part 1

def play(data, turns):
    stats = dict(zip(list(data), [[i, i] for i in range(len(data))]))
    game = [0 for _ in range(turns)]
    for i in range(len(data)):
        game[i] = data[i]
    last = data[-1]
        
    for i in range(len(data), turns):
        if last not in game[:-1]:
            last = 0
        else:
            last_i = stats[last][-2]
            last = i - last_i - 1
            if last not in stats:
                stats[last] = [i, i]
                        
        game[i] = last
        stats[last][0] = stats[last][1]
        stats[last][1] = i
                
    return last
    
last = play(data, turns)
print(last)

# part 2

turns = 30000000

spoken = play(data, turns)
print(spoken[-1])
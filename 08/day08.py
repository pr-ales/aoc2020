#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 08:35:01 2020

@author: podolnik
"""

data = []

with open('input.txt', mode='r+') as f:
    data = [(l.strip().split(' ')[0], int(l.strip().split(' ')[1])) for l in f.readlines()]


def program(data):    
    executed = set()
    
    acc = 0
    pos = 0
    last = len(data) - 1
    
    while pos not in executed and pos <= last:
        executed.add(pos)
        
        instruction = data[pos]
                
        if instruction[0] == 'acc':
            acc += instruction[1]
            pos += 1
        elif instruction[0] == 'jmp':
            pos += instruction[1]
        else:
            pos += 1
    
    return acc, pos == last + 1
    
print(program(data))

switched = {'nop': 'jmp', 'jmp': 'nop'}

for i in range(len(data)):
    instruction = data[i]
    
    if instruction[0] in switched:
        data[i] = (switched[instruction[0]], instruction[1])        
        result = program(data)
        if result[1]:
            print(result)
        
    data[i] = instruction
        
    

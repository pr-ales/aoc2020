#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 09:44:45 2020

@author: podolnik
"""

from time import time

start_1 = time()

data = []
operators = ['*', '+']    

def parse_line(line):
    
    prep = line.replace(')', ' )');
    prep = prep.replace('(', '( ');
    parts = prep.strip().split(' ')
    
    eq = []
    tree = [eq]
    
    for c in parts:
        if c.isdigit():
            eq.append(int(c))
        elif c in operators:
            eq.append(c)
        elif c == '(':
            ne = []
            eq.append(ne)
            eq = ne            
            tree.append(ne)
        elif c == ')':
            tree.pop(-1)
            eq = tree[-1]
    
    return eq

with open('input.txt', mode='r') as f:
    data = [parse_line(l) for l in f.readlines()]

# part 1

def evaluate(eq):
    stack = 0
    op = None
    
    for elem in eq:
        t = type(elem)
        if t is int or t is list:
            val = evaluate(elem) if t is list else elem
            
            if op == '+' or op is None:
                stack += val
                op = None
            elif op == '*':
                stack *= val
                op = None
                    
        elif t is str:
            op = elem
    
    return stack

results = [evaluate(eq) for eq in data]
total = sum(results)
end_1 = time()
print(total)
print(end_1 - start_1)

# part 2

start_2 = time()

def evaluate_2(eq):
    stack = []
    op = None
    
    for elem in eq:
        t = type(elem)
        if t is int or t is list:
            val = evaluate_2(elem) if t is list else elem
            
            if op == '*' or op is None:
                stack.append([val])
            elif op == '+':
                stack[-1].append(val)
                
        elif t is str:
            op = elem
    
    sums = [sum(elems) for elems in stack]
    prod = 1
    for n in sums:
        prod *= n
    
    return prod

results = [evaluate_2(eq) for eq in data]
total = sum(results)
end_2 = time()
print(total)
print(end_2 - start_2)
print(end_2 - start_1)
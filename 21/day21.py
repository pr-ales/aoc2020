#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 08:55:16 2020

@author: podolnik
"""

menu = []

def parse_line(line):
    parts = line.strip().split(' (contains ')
    
    ingredients = [w for w in parts[0].split(' ')]
    allergens = [w for w in parts[1].replace(')', '').split(', ')]
    
    return (ingredients, allergens)

with open('input.txt', mode='r') as f:
    menu = [parse_line(l) for l in f.readlines()]

# part 1

all_allergens = sorted(set.union(*[set(allergens) for _, allergens in menu]))
all_candidates = {a: sorted(set.intersection(*[set(i1) for i1, a1 in menu if a in a1])) for a in all_allergens}

while True:
    certain = [all_candidates[a][0] for a in all_candidates if len(all_candidates[a]) == 1]
    
    n = 0
    for c in certain:
        n = 0
        for a in all_candidates:
            if c in all_candidates[a] and len(all_candidates[a]) > 1:
                all_candidates[a].remove(c)
            n += len(all_candidates[a])
    
    if n == len(all_candidates):
        break

allergen_assignment = {a: all_candidates[a][0] for a in all_candidates}
allergen_ingredients = set(allergen_assignment.values())

occurences = sum([sum([1 for i in il if i not in allergen_ingredients]) for il, _ in menu])
print(occurences)

# part 2

canonical_list = ','.join([allergen_assignment[k] for k in sorted(allergen_assignment.keys())])
print(canonical_list)
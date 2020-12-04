#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 08:28:44 2020

@author: podolnik
"""

import re

data = []

def lines2data(lines):
    line = ' '.join(lines)
    matches = re.findall('([a-z]{3}):([^\s]+)', line)
    d = {m[0]: m[1] for m in matches}
    return d


lines = []
with open('input.txt', mode='r') as f:
    for l in f.readlines():
        l = l.strip()
        if len(l) > 1:
            lines.append(l)
        else:
            data_row = lines2data(lines)
            data.append(data_row)
            lines = []
    if len(lines) > 0:    
        data_row = lines2data(lines)
        data.append(data_row)
        
# part 1
        
required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
matching_1 = []

for r in data:
    ok = True
    for f in required:
        if f not in r:
            ok = False
            break
    if ok:
        matching_1.append(r)

print(len(matching_1))

# part 2

matching_2 = []

for r in data:
    ok = 0
    
    field = 'byr'
    if field in r:
        if re.match('[0-9]{4}', r[field]):
            v = int(r[field])
            if v >= 1920 and v <= 2002:
                ok += 1
       
    field = 'iyr'
    if field in r:
        if re.match('[0-9]{4}', r[field]):
            v = int(r[field])
            if v >= 2010 and v <= 2020:
                ok += 1
       
    field = 'eyr'
    if field in r:
        if re.match('[0-9]{4}', r[field]):
            v = int(r[field])
            if v >= 2020 and v <= 2030:
                ok += 1
    
    field = 'hgt'
    if field in r:
        if re.match('([0-9])*in', r[field]):
            v = int(r[field].replace('in', ''))
            if v >= 59 and v <= 76:
                ok += 1
        elif re.match('([0-9])*cm', r[field]):
            v = int(r[field].replace('cm', ''))
            if v >= 150 and v <= 193:
                ok += 1
    
    field = 'hcl'
    if field in r:
        if re.match('#[0-9a-f]{6}', r[field]):
            ok += 1
        
    field = 'ecl'
    if field in r:
        if r[field] in set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
            ok += 1
        
    field = 'pid'    
    if field in r:
        if re.match('^[0-9]{9}$', r[field]):
            ok += 1
            print(r[field])
    
    if ok == 7:
        matching_2.append(r)
    
print(len(matching_2))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 10:02:30 2020

@author: podolnik
"""

import regex as re

rules = {}
messages = []

with open('input.txt', mode='r') as f:
    text = f.read()
    parts = text.split('\n\n')
    
    pattern = '([0-9]*):(?: ([ 0-9]*))*\n'
    matches = re.findall(pattern, text)
    for m in matches:
        refs = [int(n) for n in m[1].split(' ')]
        rules[int(m[0])] = refs
    
    pattern = '([0-9]*): \"([ab]+)\"\n'
    matches = re.findall(pattern, text)
    for m in matches:
        rules[int(m[0])] = m[1]
    
    pattern = '([0-9]*):(?: ([ 0-9]*))* \|(?: ([ 0-9]*))*\n'
    matches = re.findall(pattern, text)
    for m in matches:
        refs_1 = [int(n) for n in m[1].split(' ')]
        refs_2 = [int(n) for n in m[2].split(' ')]
        rules[int(m[0])] = (refs_1, refs_2)

    messages = [l.strip() for l in parts[1].split('\n')]

# part 1
    
def get_pattern(i_r):
    def join_rules(i_r, r_def, gid):
        # '(?&{})' is some recursive regex magic for part 2
        return ''.join([get_rule(i) if i != i_r else '(?&{})'.format(gid) for i in r_def])
    def get_rule(i_r):
        gid = 'gid{}'.format(i_r)
        r_def = rules[i_r]
        t = type(r_def)
        if t == str:
            return r_def
        if t == list:
            return '(?<{}>'.format(gid) + join_rules(i_r, r_def, gid) + ')'
        if t == tuple:
            return '(?<{}>'.format(gid)  + join_rules(i_r, r_def[0], gid) + '|' + join_rules(i_r, r_def[1], gid) + ')'
        
    return '^' + get_rule(i_r) + '$'

rule_0 = get_pattern(0)

matches = [mes for mes in messages if re.match(rule_0, mes)]

print(len(matches))

# part 2
# 8: 42 | 42 8
# 11: 42 31 | 42 11 31

rules[8] = ([42], [42, 8])
rules[11] = ([42, 31], [42, 11, 31])

rule_0 = get_pattern(0)
matches = [mes for mes in messages if re.match(rule_0, mes)]
print(len(matches))


rule_8 = get_pattern(8)
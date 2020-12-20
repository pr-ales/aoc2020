#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 09:07:32 2020

@author: podolnik
"""

import copy


tiles = {}

with open('input.txt', mode='r') as f:
    parts = [p.strip() for p in f.read().split('\n\n')]
    
    for p in parts:
        lines = p.split('\n')
        if len(lines) > 2:
            tile_id = int(lines[0].replace(':', '').split(' ')[1])
            tile_data = [list(l) for l in lines[1:]]
            tiles[tile_id] = tile_data

tile_d = len(next(iter(tiles.values())))

edges_1 = ['t', 'l', 'b', 'r']
edges_2 = ['t', 'l', 'b', 'r', 'tf', 'lf', 'bf', 'rf']

def get_indices(edge):
    if edge == 't':
        return zip([0] * tile_d, range(0, tile_d))
    if edge == 'l':
        return zip((range(0, tile_d)), [0] * tile_d)
    if edge == 'b':
        return zip([tile_d - 1] * tile_d, range(0, tile_d))
    if edge == 'r':
        return zip(range(0, tile_d), [tile_d - 1] * tile_d)
    if edge == 'tf':
        return zip([0] * tile_d, range(tile_d - 1, -1, -1))
    if edge == 'lf':
        return zip(range(tile_d - 1, -1, -1), [0] * tile_d)
    if edge == 'bf':
        return zip([tile_d - 1] * tile_d, range(tile_d - 1, -1, -1))
    if edge == 'rf':
        return zip(range(tile_d - 1, -1, -1), [tile_d - 1] * tile_d)
    
matching = {}
connections = {t: [] for t in tiles}
    
for id_1, tile_1 in tiles.items():
    matching[id_1] = {e: {} for e in edges_1}
    for id_2, tile_2 in tiles.items():
        if id_1 != id_2:
            for e_1 in edges_1:
                idx_1 = list(get_indices(e_1))
                for e_2 in edges_2:
                    idx_2 = list(get_indices(e_2))
                    do_match = True
                    for i in range(tile_d):
                        i_1 = idx_1[i]
                        i_2 = idx_2[i]
                        if tile_1[i_1[0]][i_1[1]] != tile_2[i_2[0]][i_2[1]]:
                            do_match = False
                            break
                    if do_match:
                        matching[id_1][e_1][id_2] = e_2
                        connections[id_1].append(id_2)
                    
corners = set(['tl', 'lt', 'tr', 'rt', 'bl', 'lb', 'br', 'rb'])

neighbors = {i: {} for i in range(2, 5)}

for m in matching:    
    c = [e for e in edges_1 if len(matching[m][e]) == 1]
    neighbors[len(c)][m] = c
        
result = 1
for c in neighbors[2]:
    result *= c
    
print(result)


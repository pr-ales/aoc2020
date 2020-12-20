#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 09:07:32 2020

@author: podolnik
"""

import math

class MonsterError(Exception):
    pass

class Tile:
    
    sides = {'t': 'b', 'l': 'r', 'b': 't', 'r': 'l'}
    directions = {'t': (-1, 0), 'l': (0, -1), 'b': (1, 0), 'r': (0, 1)}

    def __init__(self, grid, tile_id = 0):
        self.tile_id = tile_id
        self.grid = grid
        self.d = len(grid)
        
    def flip(self):
        self.grid = [[l[self.d - i - 1] for i in range(self.d)] for l in self.grid]
    
    def show(self):
        for l in self.grid:
            print(''.join([str(c) for c in l]))
    
    def rotate(self, n = 1):
        ng = [['x' for c in range(len(l))] for l in self.grid]
        for i in range(n):
            for r in range(len(self.grid)):
                for c in range(len(self.grid[r])):
                    ng[c][self.d - r - 1] = self.grid[r][c]
        self.grid = ng
        
    def get_edge(self, side):
        idx = []
        if side == 't':
            idx = zip([0] * self.d, range(0, self.d))
        if side == 'l':
            idx =  zip((range(0, self.d)), [0] * self.d)
        if side == 'b':
            idx = zip([self.d - 1] * self.d, range(0, self.d))
        if side == 'r':
            idx = zip(range(0, self.d), [self.d - 1] * self.d)
        return [self.grid[i[0]][i[1]] for i in idx]
    
    @staticmethod
    def compare_edges(e_1, e_2):
        l = len(e_1)
        if l != len(e_2):
            raise ValueError()
        for i in range(len(e_1)):
            if e_1[i] != e_2[i]:
                return False
        return True
    
    def get_fitting_side(self, candidate : Tile):
        for side in Tile.sides:
            edge = self.get_edge(side)
            neigh_side = Tile.sides[side]
            
            for _ in range(4):
                neigh_edge = candidate.get_edge(neigh_side)
                if Tile.compare_edges(edge, neigh_edge):
                    return side
                candidate.rotate()
            
            candidate.flip()
            
            for _ in range(4):
                neigh_edge = candidate.get_edge(neigh_side)
                if Tile.compare_edges(edge, neigh_edge):
                    return side
                candidate.rotate()
                
        return None
    
    def find_monsters(self, monster):
        n_monsters = 0
        rots = 0
        flips = 0
        while True:
            r_max = self.d - len(monster) + 1
            c_max = self.d - len(monster[0]) + 1
            
            for r0 in range(r_max):
                for c0 in range(c_max):
                    
                    try:
                        for rm in range(len(monster)):
                            for cm in range(len(monster[rm])):
                                if monster[rm][cm] == ' ':
                                    pass
                                elif monster[rm][cm] == '#':
                                    r = r0 + rm
                                    c = c0 + cm
                                    if self.grid[r][c] == '#' or self.grid[r][c] == 'O':
                                        pass
                                    else:
                                        raise MonsterError
                        n_monsters += 1             
                        for rm in range(len(monster)):
                            for cm in range(len(monster[rm])):
                                r = r0 + rm
                                c = c0 + cm
                               
                                if monster[rm][cm] == '#':
                                    self.grid[r][c] = 'O'
                    except MonsterError:
                        pass
                    
            if n_monsters > 0:
                break           
            
            if rots == 3 and flips == 1:
                break
            elif rots == 3:
                self.flip()
                flips = 1
                rots = 0
            else:
                self.rotate()
                rots += 1            
    
    def count_crosses(self):
        n = 0
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                if self.grid[r][c] == '#':
                    n += 1
        return n
        

tiles = {}

with open('input.txt', mode='r') as f:
    parts = [p.strip() for p in f.read().split('\n\n')]
    
    for p in parts:
        lines = p.split('\n')
        if len(lines) > 2:
            tile_id = int(lines[0].replace(':', '').split(' ')[1])
            grid = [list(l) for l in lines[1:]]
            tiles[tile_id] = Tile(grid, tile_id = tile_id)

n_grid = int(math.sqrt(len(tiles))) * 2 + 1
c = n_grid // 2 + 1
r = c

tile_grid = [[None for i in range(n_grid)] for j in range(n_grid)]

pivot_i = next(iter(tiles.keys()))
pivot = tiles[pivot_i]

tile_grid[r][c] = pivot
tiles.pop(pivot_i)

pivots = [pivot_i]
placed = {pivot_i: (r, c)}

while len(tiles) > 0:
    to_pop = []
    next_pivot = None
    for tile_i in tiles:
        candidate = tiles[tile_i]
        fitting_side = pivot.get_fitting_side(candidate)
        if fitting_side is not None:
            direction = Tile.directions[fitting_side]
            r1 = r + direction[0]
            c1 = c + direction[1]
            tile_grid[r1][c1] = candidate
            placed[candidate.tile_id] = (r1, c1)
            
            next_pivot = candidate
            to_pop.append(candidate.tile_id)
    
    if next_pivot is None:
        for placed_id in placed:
            if placed_id not in pivots:
                r, c = placed[placed_id]
                next_pivot = tile_grid[r][c]

    pivot = next_pivot
    r, c = placed[pivot.tile_id]
    pivots.append(pivot.tile_id)
    
    for i in to_pop:
        tiles.pop(i)
        
min_r = None
min_c = None
max_r = None
max_c = None

for r in range(n_grid):
    for c in range(n_grid):
        if tile_grid[r][c] is not None:
            min_r = r if min_r is None else min(min_r, r)
            min_c = c if min_c is None else min(min_c, c)
            max_r = r if max_r is None else max(max_r, r)
            max_c = c if max_c is None else max(max_c, c)
            
tile_grid = [[tile_grid[r][c] for c in range(min_c, max_c + 1)] for r in range(min_r, max_r + 1)]
n_grid = len(tile_grid)

result_1 = tile_grid[0][0].tile_id * tile_grid[0][n_grid - 1].tile_id * tile_grid[n_grid - 1][0].tile_id * tile_grid[n_grid - 1][n_grid - 1].tile_id
print(result_1)

# part 2

d_tile = tile_grid[0][0].d

n_pic = n_grid * (d_tile - 2)

picture_grid = [[' ' for _ in range(n_pic)] for _ in range(n_pic)]

for r in range(n_grid):
    for c in range(n_grid):
        r0 = r * (d_tile - 2)
        c0 = c * (d_tile - 2) 
        tile = tile_grid[r][c]
        for rr in range(1, tile.d - 1):
            for cc in range(1, tile.d - 1):
                picture_grid[r0 + rr - 1][c0 + cc - 1] = tile.grid[rr][cc]
        
picture = Tile(picture_grid)

monster = [list('                  # '), 
           list('#    ##    ##    ###'), 
           list(' #  #  #  #  #  #   ')]
                
picture.find_monsters(monster)
picture.show()

n_crosses = picture.count_crosses()
print(n_crosses)
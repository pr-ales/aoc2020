#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 08:28:12 2020

@author: podolnik
"""

from time import time

#input_text = '389125467' # test input
input_text = '253149867'

class Cup:
    def __init__(self, val, next_cup = None):
        self.val = int(val)
        self.next_cup = next_cup
  
    def get_data(self, count = -1):
        data = [self.val]
        next_cup = self.next_cup
        i = 0
        while next_cup != self and next_cup is not None:
            data.append(next_cup.val)
            next_cup = next_cup.next_cup
            i += 1
            
            if count > 0 and i >= count:
                break
            
        return data
    
    def show(self):
        data = self.get_data()
        print(', '.join([str(v) for v in data]))
        
    @staticmethod
    def get_chain(input_text, million = False):
        arr = list(input_text)
        helper = {}
        
        first_cup = Cup(arr[0])
        prev_cup = first_cup
        
        helper[first_cup.val] = first_cup
        
        for i in range(1, len(arr)):
            next_cup = Cup(arr[i])
            helper[next_cup.val] = next_cup
            
            prev_cup.next_cup = next_cup
            prev_cup = next_cup
        
        if million:
            prev_cup
            for i in range(len(arr) + 1, 1000001):
                next_cup = Cup(i)
                helper[next_cup.val] = next_cup
                
                prev_cup.next_cup = next_cup
                prev_cup = next_cup
                        
        prev_cup.next_cup = first_cup
        
        return first_cup, helper
    
    def cut(self, n):
        cut = self.next_cup
        seam = self.next_cup
        for i in range(n - 1):
            seam = seam.next_cup
        
        self.next_cup = seam.next_cup
        seam.next_cup = None
        return cut
    
    def insert(self, cup):
        last = cup
        while last.next_cup is not None:
            last = last.next_cup
            
        last.next_cup = self.next_cup
        self.next_cup = cup
    
    def shuffle(self, helper, n_iter = 10):
        max_val = max(helper.keys())
        
        pivot = self
        
        for i in range(n_iter):
                       
            picked = pivot.cut(3)
            dest_val = max_val if pivot.val == 1 else pivot.val - 1
            
            while picked.contains(dest_val):
                dest_val = max_val if dest_val == 1 else dest_val - 1
            
            dest_cup = helper[dest_val]
            dest_cup.insert(picked)
            
            pivot = pivot.next_cup
        
    def contains(self, val):
        cup = self
        while True:
            if cup.val == val:
                return True
            cup = cup.next_cup
            if cup is None or cup == self:
                return False
        
        
start_1 = time()
chain, helper = Cup.get_chain(input_text)

chain.shuffle(helper, n_iter = 100)
data = helper[1].get_data()
end_1 = time()

print(''.join([str(c) for c in data[1:]]))
print(end_1 - start_1)

start_2 = time()
chain, helper = Cup.get_chain(input_text, million = True)

chain.shuffle(helper, n_iter = 10000000)
data = helper[1].get_data(count=2)
end_2 = time()
print(data[1] * data[2])
print(end_2 - start_2)


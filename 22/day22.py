#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 09:07:08 2020

@author: podolnik
"""

import copy
from time import time

start_1 = time()

starting_deck_1 = []
starting_deck_2 = []

with open('input.txt', mode='r') as f:
    parts = f.read().split('\n\n')
    
    starting_deck_1 = [int(l) for l in parts[0].split('\n')[1:] if len(l) > 0]
    starting_deck_2 = [int(l) for l in parts[1].split('\n')[1:] if len(l) > 0]


def play(deck_1, deck_2):
    while len(deck_1) > 0 and len(deck_2) > 0:
        card_1 = deck_1.pop(0)
        card_2 = deck_2.pop(0)
        
        if card_1 > card_2:
            deck_1.extend([card_1, card_2])
        elif card_2 > card_1:
            deck_2.extend([card_2, card_1])
            
    return deck_1 if len(deck_1) > len(deck_2) else deck_2

deck_1 = copy.deepcopy(starting_deck_1)
deck_2 = copy.deepcopy(starting_deck_2)

deck = play(deck_1, deck_2)
n = len(deck)
points = [(n - i) * deck[i] for i in range(n)]
end_1 = time()

print(sum(points))
print(end_1 - start_1)

start_2 = time()

n_games = 0
n_hits = 0

all_results = {}
played_states = set()

def get_key(deck_1, deck_2):
    return tuple(deck_1 + [0] + deck_2)

def play_recursive(deck_1, deck_2, history):
    global all_results
    global played_states
    global n_games
    global n_hits
    
    def check_history(deck_1, deck_2, history):
        hist_key = get_key(deck_1, deck_2)
        
        if hist_key in history:
            return True
            
        history.add(hist_key)
        return False
     
    n_games += 1
    this_game = n_games
    
    n_rounds = 1
    result = None
    
    while len(deck_1) > 0 and len(deck_2) > 0:
#        print('game {}, round {}'.format(this_game, n_rounds))
        n_rounds += 1
        
        if check_history(deck_1, deck_2, history):
            result = (1, this_game, n_rounds, deck_1)
            n_hits += 1
            break
        else:
            card_1 = deck_1.pop(0)
            card_2 = deck_2.pop(0)
            
            if len(deck_1) >= card_1 and len(deck_2) >= card_2:
                rec_deck_1 = copy.deepcopy(deck_1[:card_1])
                rec_deck_2 = copy.deepcopy(deck_2[:card_2])
                
                sub_result = play_recursive(rec_deck_1, rec_deck_2, set())
                winner = sub_result[0]
                
                if winner == 1:
                    deck_1.extend([card_1, card_2])
                else:
                    deck_2.extend([card_2, card_1])
            else:                
                if card_1 > card_2:
                    deck_1.extend([card_1, card_2])
                elif card_2 > card_1:
                    deck_2.extend([card_2, card_1])
         
    if result is None:
        result = (1, this_game, n_rounds, deck_1) if len(deck_1) > len(deck_2) else (2, this_game, n_rounds, deck_2)
    
    return result
      
deck_1 = copy.deepcopy(starting_deck_1)
deck_2 = copy.deepcopy(starting_deck_2)

history = set()
result = play_recursive(deck_1, deck_2, history)
deck = result[-1]
n = len(deck)
points = [(n - i) * deck[i] for i in range(n)]
end_2 = time()

print(sum(points))
print(end_2 - start_2)       

history = list(history)   
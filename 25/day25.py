#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 08:30:29 2020

@author: podolnik
"""

def transform(loop_size, subject_number = 7):
    modulo = 20201227
    return pow(subject_number, loop_size, modulo)

def get_loop_size(public_key, subject_number = 7):
    loop_size = 1
    while True:
        t_sn = transform(loop_size, subject_number)
        if t_sn == public_key:
            return loop_size
        loop_size += 1


pubk_test = 5764801
ls = get_loop_size(pubk_test)

pubk_door = 1965712
pubk_card = 19072108

ls_door = get_loop_size(pubk_door)

enc_key = transform(ls_door, pubk_card)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 09:23:11 2020

@author: podolnik
"""
import math
from time import time

start = time()

my_time = 0
buses = []

with open('input.txt', mode='r') as f:
    lines = f.readlines()
    my_time = int(lines[0].strip())
    buses = [int(b) if b != 'x' else -1 for b in lines[1].strip().split(',') ]

# part 1 
    
min_delta = None
min_i = -1

for i, b in enumerate(buses):
    if b >= 0:
        n = math.ceil(my_time / b)
        delta = n * b - my_time
        
        if min_delta is None or delta < min_delta:
            min_delta = delta
            min_i = i

end = time()
print(buses[min_i] * min_delta)
print(end - start)

# part 2

start_1 = time()

remainders = [(buses[i], (buses[i] - i) % buses[i]) for i in range(len(buses)) if buses[i] > 0]

all_prod = 1
for r in remainders:
    all_prod *= r[0]
    
total_sum = 0
total_prod = 0
for r in remainders:
    bus_prod = 1
    for r_1 in remainders:
        if r is not r_1:
            bus_prod *= r_1[0]
 
    total_sum += bus_prod
    total_prod += bus_prod * r[1]
    print ('{0} x === {1} (mod {2})'.format(bus_prod, r[1] * bus_prod, all_prod))

total_prod = total_prod % all_prod

print()
print ('{0} x === {1} (mod {2})'.format(total_sum, total_prod, all_prod))
print()

p = total_sum
q = total_prod
m = all_prod

# solving an equation p x === q (mod m)
# or p * x + m * k = q, where a, k, q and m are positive integers
#    a * x + b * y = c has a solution if c = n * gcd(a, b)
# if a == p and b == m, gcd(p, m) = 1
# thus q = n * m

def gcd(a, b):
    while b > 0:
        s = b
        b = a % b
        a = s
    return a

k = 0
a = 0

# flip this to True to get a slow solution (many... hours?)
while False:
    rhs = k * m + q
    
    if rhs % p == 0 :#and a >= 100000000000000:
        a = int(rhs / p)
        break
    else:
        print(k, int(rhs / p))
    
    k += 1

end_1 = time()

print(a)
print(end_1 - start_1)

# part 2 from Chinese remainder theorem using standard algorithms (thanks wiki)
# extended gcd: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
# solution to Chinese remainder theorem: https://en.wikipedia.org/wiki/Chinese_remainder_theorem

start_2 = time()

def extended_gcd(a, b):
    (old_r, r) = (a, b)
    (old_s, s) = (1, 0)
    (old_t, t) = (0, 1)
    
    while not r == 0:
        q = old_r // r
        (old_r, r) = (r, old_r - q * r)
        (old_s, s) = (s, old_s - q * s)
        (old_t, t) = (t, old_t - q * t)
    
    return (old_s, old_t)

x = 0
for i in range(len(remainders)):
    n_i = remainders[i][0]
    a_i = remainders[i][1]
    N_i = all_prod // n_i
    
    M_i, m_i = extended_gcd(N_i, n_i)
    
    x += a_i * M_i * N_i
    
x = x % all_prod
end_2 = time()

print(x)

print(end_2 - start_2)

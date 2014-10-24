# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 14:49:55 2014

@author: raffaelerainone
"""
from math import sqrt
from time import clock

#the following gives the sum of all the 1≤ divisor < n of n
def is_abundant(n):
    is_it = False
    summ = 1
    if n>3:
        i = 2
        while i <= int(sqrt(n)):
            if n%i == 0:
                summ += i
                summ += (n/i)
            i += 1
    if summ > n:
        is_it = True
    return is_it

#The following gives all the abundant integers less than limit.
def find_abundant(limit):
    abundants = []
    for i in range(11,limit):
        if is_abundant(i):
            abundants.append(i)
    return abundants

start = clock()
our_set = find_abundant(28124)

#Find all the integers ≤ 28123 that are sum of two abundants.
sum_of_abundants = [False]*28124
for i in range(len(our_set)):
    j = i
    while our_set[i]+our_set[j] < len(sum_of_abundants) and j < len(our_set):
        sum_of_abundants[our_set[i]+our_set[j]] = True
        j += 1

#Find the sum of all the integers that are not sum of two abundants.
total = 0
for n in range(len(sum_of_abundants)):
    if not sum_of_abundants[n]:
        total += n

print total, clock()-start
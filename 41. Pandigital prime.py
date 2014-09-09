# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 14:17:15 2014

@author: raffaelerainone
"""

from math import sqrt
import itertools

def is_prime(n):
    check = True
    i=2
    if n>3:
        while check and i<=int(sqrt(n)):
            if n%i == 0:
                check = False
            i += 1
    elif n==1:
        check = False
    elif n==2 or n==3:
        check = True
    return check


def n_pandigital(n):
    lst = []
    the_set = []
    for i in range(1,n+1):
        i=str(i)        
        lst.append(i)
    lst = "".join(lst)
    for item in itertools.permutations(lst):
        the_set.append(int("".join(item)))
    return the_set

max = 1 
for n in range(2,10):
    for nmbr in n_pandigital(n):
        if is_prime(nmbr) and nmbr > max:
            max = nmbr

print max
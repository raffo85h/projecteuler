# -*- coding: utf-8 -*-
"""
Created on Mon Sep  1 11:01:40 2014

@author: raffaelerainone
"""
from itertools import product
from operator import itemgetter
from time import clock

def sum_dig(n):
    str_n = str(n)
    sum = 0
    for i in range(0,len(str_n)):
        sum += int(str_n[i])
    return sum

start = clock()

'''
The following stores the values [a^b, a, b] in the array A and then sort A.
However we only need the maximum. So see code from line 30.
A = []
for a, b in product(range(1,100),range(1,100)):
    A.append([sum_dig(a**b),a,b])

A = sorted(A,key=itemgetter(0))
print A[len(A)-1], clock()-start,'s'
'''
max_sum = 0
for a, b in product(range(1,100),range(1,100)):
    if sum_dig(a**b)>max_sum:
        max_sum = sum_dig(a**b)
print 'The answer is:', max_sum
print 'Time:',clock()-start,'s'
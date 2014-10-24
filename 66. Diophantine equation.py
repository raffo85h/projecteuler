# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 21:45:19 2014

@author: Raffo
"""
from math import sqrt
from time import clock

def prime_sieve(n):
    """
    Return a list of prime numbers from 2 to a prime < n. Very fast (n<10,000,000) in 0.4 sec.
    
    Example:
    >>>prime_sieve(25)
    [2, 3, 5, 7, 11, 13, 17, 19, 23]

    Algorithm & Python source: Robert William Hanks

http://stackoverflow.com/questions/17773352/python-sieve-prime-numbers

    """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

print prime_sieve(104)

#These equations are also known as Pell's equations.

def pell(d):
    p, k, x1, y, sd = 1, 1, 1, 0, sqrt(d)
    while k != 1 or y == 0:
        p = k * (p/k+1) - p
        p = p - int((p - sd)/k) * k
 
        x = (p*x1 + d*y) / abs(k)
        y = (p*y + x1) / abs(k)
        k = (p*p - d) / k
        x1 = x
    return x

start = clock() 
L = 1000
print max((pell(d),d) for d in prime_sieve(L)), clock()-start
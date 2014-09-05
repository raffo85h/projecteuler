# -*- coding: utf-8 -*-
"""
Created on Tue Sep  2 10:12:23 2014

@author: raffaelerainone
"""

'''
Problem 64.
How many continued fractions of sqrt(N),
for N ≤ 10000 have an odd period?
=========================================
The alghorithm is given by stardard facts
on continued fractions.
'''

from math import sqrt

def continued_fraction_sqrt(N):
    A = []
    M = []
    D = []
    M.append(0)
    D.append(1.0)
    A.append(int(sqrt(N)))
    i=1
    count=0
    while True:# A[i]!=2*A[0]:
        M.append(D[i-1]*A[i-1]-M[i-1])
        D.append((N-M[i]**2)/D[i-1])
        A.append(int((sqrt(N)+M[i])/D[i]))
        count+=1
        if A[i]==2*A[0]:
            break
        i+=1
    return count

result = 0
for N in range(1,10000):
    if sqrt(N)**2!=N and continued_fraction_sqrt(N)%2==1:
        result+=1
print result
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 09:56:52 2014

@author: raffaelerainone
"""
from math import sqrt
from fractions import gcd
from time import clock
'''
a = m^2 - n^2
b = 2mn
c = m^2 + n^2
p = a + b + c = 2m(m + n) < limit --> 2m^2 < limit --> m < sqrt(limit/2)
--> n < limit - 2m^2
'''
def construct_triangles(limit):
    list_of_perimeters = []
    for x in range(limit):
        list_of_perimeters.append(0)
    for m in range(2, int(sqrt(limit/2)) + 1):
        n = 1
        while n < m and n < limit - 2*(m**2) + 1:
            if gcd(n,m)==1 and (n+m)%2==1:
                p = 2*m*(m+n)
                k = 1
                while k*p <= limit:
                    list_of_perimeters[k*p-1]+=1
                    k += 1
            n += 1
    result = 0
    for x in list_of_perimeters:
        if x == 1:
            result += 1
    return result
'''Too Slow:
A = construct_triangles(15000)
B = [x for x in A if A.count(x)==1]
'''
start = clock()
print construct_triangles(1500000), clock()-start
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 15:52:33 2014

@author: raffaelerainone
"""
from time import clock
from math import sqrt

def is_prime(n):
    check=True
    i=2
    while check and i<=sqrt(n):
        if n%i==0:
           check=False
        i+=1
    return check
    
start = clock()

lim=50*(10**6)
A=[]

prime_2 = [i for i in range(2,int(lim**(0.5))) if is_prime(i)]
prime_3 = [i for i in prime_2 if i<(int(lim**(0.34)))]
prime_4 = [i for i in prime_3 if i<(int(lim**(0.25)))]

for i in prime_2:
    for j in prime_3:
        for k in prime_4:
            x=(i**2)+(j**3)+(k**4)
            if x<lim:
                A.append(x)
print len(set(A))

print clock() - start
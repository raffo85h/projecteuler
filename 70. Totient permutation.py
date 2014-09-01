# -*- coding: utf-8 -*-
"""
Created on Mon Sep  1 14:04:35 2014

@author: raffaelerainone
"""

'''
For problem 70. we see that if n=p_1^{a_1}*...*p_l^{a_l} then
n/phi(n)=(p_1*..*p_l)/(p_1-1)*...*(p_l-1)
Therefore in order to have a minimum ratio we need l=2 & a_1=a_2=1.

IDEA:
1.Getting the prime factorisation is Hard & Slow.

2.Rather than checking for all the integers in [1,10**7] it is better
to construct numbers <10**7 that decompose as product of two primes.

Therefore we need to know the primes in [1,sqrt(10**7)].
These prime can be eaily found and we easily do the checking desccribed.
'''

from math import sqrt

def is_prime(n): #return True if n is prime and False otherwise
    check = True
    i=2
    while check and i<=int(sqrt(n)):
        if n%i==0:
            check = False
        i+=1
    return check
#For n=p*q where p, q are prime we check if it is a totient permutation
#notice that phi(n)=(p-1)(q-1)
def is_totient_permutation(p,q):
    if sorted(str(p*q))==sorted(str((p-1)*(q-1))):
        return True
    else:
        return False

primes = [2]
for i in range(3,int(sqrt(10**8))):
    if is_prime(i):
        primes.append(i)


minimum_quotient = 2
minimum_n=2

for i in primes:
    for j in primes:
        if i!=j and i*j<10**7 and is_totient_permutation(i,j):
            if minimum_quotient > float(i*j)/float(((i-1)*(j-1))):
                minimum_quotient = float(i*j)/float(((i-1)*(j-1)))
                minimum_n = i*j
print minimum_n,minimum_quotient
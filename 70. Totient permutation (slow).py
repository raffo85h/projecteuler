# -*- coding: utf-8 -*-
"""
Created on Mon Sep  1 11:26:07 2014

@author: raffaelerainone
"""
#Brute force method. Too slow!

from math import sqrt
from operator import itemgetter
from time import clock

def is_prime(n): #return True if n is prime and False otherwise
    check = True
    i=2
    while check and i<=int(sqrt(n)):
        if n%i==0:
            check = False
        i+=1
    return check
'''
Let 1<n = p_1^{a_1}...p_l^{a_l}
The following returns the array  A=[[p_1,a_1],...[p_l,a_l]]
'''
def prime_decomposition(n):
    if is_prime(n):
        return [[n,1]]
    else:
        A = []
        for i in range(2,n):#int(sqrt(n))+1):
            if is_prime(i):
                j=0
                check_division = True
                while check_division :
                    if n%i == 0:
                        j += 1
                        if n/i%1 == 0:
                            n /= i
                        else:
                            check_division = False
                    else:
                        check_division = False
                if j>0:
                    A.append([i,j])
    return sorted(A,key=itemgetter(0))
'''
if we only need the primes that divide n then we use the following
'''
def prime_divisors(n):
    if is_prime(n):
        return [n]
    else:
        A = []
        for i in range(2,int(sqrt(n))+1):
            if is_prime(i) and float(n)/float(i)%1 == 0:
                A.append(i)
                if is_prime(n/i):
                    A.append(n/i)
    return A

'''
There is a nice formula that computes the totient function value
of an integer 1<n = p_1^{a_1}...p_l^{a_l}"
phi(n)=n*Prod_{i=1,..,l}(1-1/p_i)
We use the array gotten from prime_divisors(n)
'''
def totient(n):
    if n==1:
        value==1
    else:
        value = n
        A=prime_divisors(n)
        for i in range(len(A)):
            value*=float(1.0-1.0/float(A[i]))
    return int(value)

def is_a_permutation(n):
    if set(str(n))==set(str(totient(n))):
        return True
    else:
        return False
'''
start = clock()
quotient = 2
result = 2
for n in range(2,10**6):
	if is_a_permutation(n):
		prod=1.0
		for p in prime_divisors(n):
			prod*=float(p)/float(p-1)
		if prod<quotient:
			quotient=prod
			result=n
print result
print clock()-start
'''
print prime_decomposition(8319823)
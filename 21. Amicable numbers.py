# -*- coding: utf-8 -*-
"""
Created on Sat Aug 23 18:03:35 2014

@author: raffaelerainone
"""
import math
def list_divisors(n):
    A=[1]
    if n!=1:
        for i in range(2,int(math.sqrt(n))):
            if n%i==0:
                A.append(i)
                A.append(n/i)
#if the sqare root of n is an integer & it | n then we only add 1
        if int(math.sqrt(n)) == math.sqrt(n):
            if n%int(math.sqrt(n))==0:
                A.append(int(math.sqrt(n)))
    return A

def array_sum(A):
#just sum all the elements in the array A
    sum=0
    for i in range(0,len(A)):
        sum+=A[i]
    return sum

def amicable(n):
#this returns n if it is amicable and 0 otherwise
# important: by def we want d(n)=b , d(b)=n AND n!=b.
    if n == array_sum(list_divisors(array_sum(list_divisors(n)))) and n!=array_sum(list_divisors(n)):
        return True
    else:
        return False

result=0
for i in range(1,10001):
    if amicable(i) == True:
        result += i

print result
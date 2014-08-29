# -*- coding: utf-8 -*-
import time
import math
def num_factors(n):
    total=2
    for i in range(2,int(math.sqrt(n))):
        if n%i==0:
            total+=2 #add 2 because both i and n/i divide n
    if int(math.sqrt(n))== math.sqrt(n):#if the sqare root of n is an integer & it | n then we only add 1
        if n%int(math.sqrt(n))==0:
            total+=1
    return total

def triang(n):
    return n*(n+1)/2

start = time.time()
i = 7
k = True
while k:
    if num_factors(triang(i))>499:
        print triang(i)
        print time.time()-start
        k = False
    i+=1
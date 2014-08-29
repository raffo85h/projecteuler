# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 17:11:42 2014

@author: raffaelerainone
"""
#I THINK THIS IS EFFICIENT!
import itertools #needed to compute the permutations of a number
import math
#import time

def is_prime(n):
    check = True
    i=2
    while i<int(math.sqrt(n)+1) and check:
        if n%i==0:
            check=False
        i+=1
    return check

#start = time.time()
final_check=True
number_to_check=1000
while final_check:
    if is_prime(number_to_check)==True:
        number=str(number_to_check)
#A comprise the permutations of the prime integer we are considering, without repetition
        A= list(set(itertools.permutations(number)))
        B=[number_to_check]
        for x in A:
            if int(x[0]+x[1]+x[2]+x[3])>1000:
                permutation_of_n = int(x[0]+x[1]+x[2]+x[3])
                if permutation_of_n!=number_to_check and is_prime(permutation_of_n)==True:
#if a permutation of our original number n is prime (and not n) we add it to B
                        B.append(permutation_of_n)
        B=sorted(list(set(B))) # we want B to be sorted to optimise the computation as in (*)
        if B[0]!=1487:
            for index_1 in range(0,len(B)-2):
                for index_2 in range(index_1+1,len(B)-1):
                    for index_3 in range(index_2+1,len(B)):
                        if B[index_3]-B[index_2]==B[index_2]-B[index_1]: #(*)
                            final_check=False
                            print str(B[index_1])+str(B[index_2])+str(B[index_3])
    number_to_check+=1
#print time.time()-start
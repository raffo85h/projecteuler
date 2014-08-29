# -*- coding: utf-8 -*-
"""
Created on Sat Aug 23 15:19:42 2014

@author: raffaelerainone
"""
import time
def generate_sequence(n):
    A=[n]
    check=True
    i=0
    while check :
        if A[i]%2 == 0:
            A.append(A[i]/2)
            if A[i]/2==1:
                check = False
        else:
            A.append(3*A[i]+1)
        i+=1
    return len(A)
    
start = time.time()

the_number_is = 1
length_is = 1
for i in range(2,1000000):
    a = generate_sequence(i)
    if a > length_is :
        the_number_is = i
        length_is = a

print the_number_is
print time.time()-start
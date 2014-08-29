# -*- coding: utf-8 -*-
"""
Created on Sat Aug 23 17:59:56 2014

@author: raffaelerainone
"""

A=str(2**1000)
sum=0
for i in range(0,len(A)):
    sum+=int(A[i])
print sum